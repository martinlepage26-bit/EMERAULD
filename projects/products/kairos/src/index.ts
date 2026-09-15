import { Hono } from 'hono';
import type { AppBindings, Env } from './env';
import { jobBatchSize } from './env';
import { AppError } from './lib/errors';
import { db } from './lib/db';
import { drain, enqueue, type JobHandler, type JobKind } from './queue/jobs';

import { accounts } from './routes/accounts';
import { workspace } from './routes/workspace';
import { inbox } from './routes/inbox';
import { billing } from './routes/billing';

import { handlePlanGenerate } from './engines/strategy';
import { handleContentDraft } from './engines/content';
import { enqueueDuePublishes, handlePublishDispatch } from './engines/publishing';
import { handleGrowthRebalance, handleMetricsCollect } from './engines/growth';
import { enqueueInboxSyncs, handleInboxSync, handleReplyDraft, handleReplySend } from './engines/engagement';
import { handleBillingReconcile } from './engines/billing';

const HANDLERS: Record<JobKind, JobHandler> = {
  'plan.generate': handlePlanGenerate,
  'content.draft': handleContentDraft,
  'publish.dispatch': handlePublishDispatch,
  'metrics.collect': handleMetricsCollect,
  'growth.rebalance': handleGrowthRebalance,
  'inbox.sync': handleInboxSync,
  'reply.draft': handleReplyDraft,
  'reply.send': handleReplySend,
  'billing.reconcile': handleBillingReconcile,
};

const app = new Hono<AppBindings>();

app.onError((err, c) => {
  if (err instanceof AppError) {
    return c.json({ error: { code: err.code, message: err.message, detail: err.detail } }, err.status as never);
  }
  console.error('unhandled error', err);
  return c.json({ error: { code: 'internal_error', message: 'Something went wrong' } }, 500);
});

app.get('/health', async (c) => {
  const queue = await db(c.env).first<{ pending: number; dead: number }>(
    `SELECT
       SUM(CASE WHEN status = 'pending' THEN 1 ELSE 0 END) AS pending,
       SUM(CASE WHEN status = 'dead' THEN 1 ELSE 0 END) AS dead
     FROM jobs`,
  );
  return c.json({
    ok: true,
    environment: c.env.ENVIRONMENT,
    dryRun: c.env.DRY_RUN !== 'false',
    queue: { pending: queue?.pending ?? 0, dead: queue?.dead ?? 0 },
  });
});

app.route('/', accounts);
app.route('/', workspace);
app.route('/', inbox);
app.route('/', billing);

app.notFound((c) => c.json({ error: { code: 'not_found', message: 'No such endpoint' } }, 404));

/** Accounts eligible for autonomous work: paying or trialling, and not paused. */
async function activeAccountIds(env: Env): Promise<string[]> {
  const rows = await db(env).all<{ id: string }>(
    `SELECT a.id
       FROM accounts a
       JOIN automation_controls ac ON ac.account_id = a.id
      WHERE a.status IN ('active', 'past_due')
        AND (ac.paused_until IS NULL OR ac.paused_until < ?)
      LIMIT 2000`,
    new Date().toISOString(),
  );
  return rows.map((r) => r.id);
}

/**
 * Sweeps published posts whose metrics have gone stale. The publish path already
 * schedules two collections per post; this is the safety net for posts whose
 * collection jobs died, so a gap in measurement does not silently corrupt the
 * pillar weights the growth engine derives.
 */
async function enqueueStaleMetrics(env: Env): Promise<number> {
  const rows = await db(env).all<{ id: string; account_id: string }>(
    `SELECT p.id, p.account_id
       FROM posts p
      WHERE p.status = 'published'
        AND p.published_at >= ?
        AND NOT EXISTS (
          SELECT 1 FROM post_metrics m
           WHERE m.post_id = p.id AND m.captured_at >= ?
        )
      LIMIT 200`,
    new Date(Date.now() - 7 * 86_400_000).toISOString(),
    new Date(Date.now() - 24 * 3600_000).toISOString(),
  );

  const bucket = Math.floor(Date.now() / 3600_000);
  let n = 0;
  for (const row of rows) {
    const id = await enqueue(
      env,
      'metrics.collect',
      { postId: row.id },
      { accountId: row.account_id, idempotencyKey: `metrics:${row.id}:sweep:${bucket}` },
    );
    if (id) n++;
  }
  return n;
}

export default {
  fetch: app.fetch,

  /**
   * Five schedules, each doing one thing. Splitting them means a slow daily
   * planning run cannot starve the every-minute queue drain, which is what
   * actually publishes posts on time.
   */
  async scheduled(event: ScheduledController, env: Env, ctx: ExecutionContext): Promise<void> {
    const work = async (): Promise<void> => {
      switch (event.cron) {
        case '* * * * *': {
          const res = await drain(env, HANDLERS, jobBatchSize(env));
          if (res.processed > 0) {
            console.log(`queue: processed ${res.processed}, failed ${res.failed}`);
          }
          break;
        }

        case '*/15 * * * *': {
          const [publishes, syncs] = await Promise.all([
            enqueueDuePublishes(env),
            enqueueInboxSyncs(env),
          ]);
          console.log(`scheduler: ${publishes} publishes, ${syncs} inbox syncs queued`);
          break;
        }

        case '17 * * * *': {
          console.log(`metrics sweep: ${await enqueueStaleMetrics(env)} collections queued`);
          break;
        }

        case '10 5 * * *': {
          const ids = await activeAccountIds(env);
          const day = new Date().toISOString().slice(0, 10);
          for (const accountId of ids) {
            await enqueue(env, 'plan.generate', {}, {
              accountId,
              idempotencyKey: `plan:${accountId}:${day}`,
            });
            await enqueue(env, 'growth.rebalance', {}, {
              accountId,
              idempotencyKey: `rebalance:${accountId}:${day}`,
            });
          }
          console.log(`daily: queued planning and rebalance for ${ids.length} accounts`);
          break;
        }

        case '20 6 * * *': {
          const day = new Date().toISOString().slice(0, 10);
          await enqueue(env, 'billing.reconcile', {}, { idempotencyKey: `billing:${day}` });
          break;
        }

        default:
          console.warn(`No handler for cron "${event.cron}"`);
      }
    };

    ctx.waitUntil(work());
  },
};
