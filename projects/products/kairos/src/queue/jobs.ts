import type { Env } from '../env';
import { db, audit } from '../lib/db';
import { newId, nowIso } from '../lib/ids';
import { RetryableError } from '../lib/errors';

export type JobKind =
  | 'plan.generate'      // build calendar slots for the next horizon
  | 'content.draft'      // generate a post for a planned slot
  | 'publish.dispatch'   // push an approved post to its platform
  | 'metrics.collect'    // pull performance for a published post
  | 'growth.rebalance'   // reweight pillars, schedule recycles
  | 'inbox.sync'         // pull new inbound messages for a channel
  | 'reply.draft'        // draft a reply for a conversation
  | 'reply.send'         // send an approved reply
  | 'billing.reconcile'; // check subscription health, apply dunning

export interface Job {
  id: string;
  account_id: string | null;
  kind: JobKind;
  payload: string;
  attempts: number;
  max_attempts: number;
}

export type JobHandler = (env: Env, job: Job, payload: Record<string, unknown>) => Promise<void>;

export interface EnqueueOptions {
  accountId?: string | null;
  runAfter?: Date;
  maxAttempts?: number;
  /**
   * Collapses duplicate work. Enqueuing the same key twice is a no-op, which is
   * what lets cron ticks overlap safely without double-publishing.
   */
  idempotencyKey?: string;
}

export async function enqueue(
  env: Env,
  kind: JobKind,
  payload: Record<string, unknown> = {},
  opts: EnqueueOptions = {},
): Promise<string | null> {
  const id = newId('job');
  const now = nowIso();
  const res = await db(env).run(
    `INSERT OR IGNORE INTO jobs
       (id, account_id, kind, payload, run_after, status, attempts, max_attempts,
        idempotency_key, created_at, updated_at)
     VALUES (?, ?, ?, ?, ?, 'pending', 0, ?, ?, ?, ?)`,
    id,
    opts.accountId ?? null,
    kind,
    JSON.stringify(payload),
    (opts.runAfter ?? new Date()).toISOString(),
    opts.maxAttempts ?? 5,
    opts.idempotencyKey ?? null,
    now,
    now,
  );
  // `INSERT OR IGNORE` reports zero changes when the idempotency key already exists.
  return res.meta.changes > 0 ? id : null;
}

/**
 * Claims up to `limit` due jobs. D1 has no `SELECT ... FOR UPDATE`, so each
 * candidate is claimed with a conditional UPDATE and kept only if this worker
 * won the race. Overlapping cron invocations therefore cannot both run one job.
 */
export async function claim(env: Env, limit: number): Promise<Job[]> {
  const now = nowIso();
  const candidates = await db(env).all<Job>(
    `SELECT id, account_id, kind, payload, attempts, max_attempts
       FROM jobs
      WHERE status = 'pending' AND run_after <= ?
      ORDER BY run_after ASC
      LIMIT ?`,
    now,
    limit,
  );

  const lockUntil = new Date(Date.now() + 5 * 60_000).toISOString();
  const claimed: Job[] = [];

  for (const job of candidates) {
    const res = await db(env).run(
      `UPDATE jobs
          SET status = 'running', locked_until = ?, attempts = attempts + 1, updated_at = ?
        WHERE id = ? AND status = 'pending'`,
      lockUntil,
      now,
      job.id,
    );
    if (res.meta.changes === 1) claimed.push({ ...job, attempts: job.attempts + 1 });
  }

  return claimed;
}

/** Returns stuck jobs to the queue after their lock expires. */
export async function reapExpiredLocks(env: Env): Promise<number> {
  const res = await db(env).run(
    `UPDATE jobs
        SET status = 'pending', locked_until = NULL, updated_at = ?
      WHERE status = 'running' AND locked_until IS NOT NULL AND locked_until < ?`,
    nowIso(),
    nowIso(),
  );
  return res.meta.changes;
}

async function succeed(env: Env, job: Job): Promise<void> {
  await db(env).run(
    `UPDATE jobs SET status = 'done', locked_until = NULL, last_error = NULL, updated_at = ?
      WHERE id = ?`,
    nowIso(),
    job.id,
  );
}

async function fail(env: Env, job: Job, err: unknown): Promise<void> {
  const message = err instanceof Error ? err.message : String(err);
  const retryable = err instanceof RetryableError;
  const exhausted = job.attempts >= job.max_attempts;

  if (!retryable || exhausted) {
    await db(env).run(
      `UPDATE jobs SET status = 'dead', locked_until = NULL, last_error = ?, updated_at = ?
        WHERE id = ?`,
      message.slice(0, 1000),
      nowIso(),
      job.id,
    );
    await audit(env, {
      accountId: job.account_id,
      actor: 'system:queue',
      action: 'job.dead',
      entityType: 'job',
      entityId: job.id,
      detail: { kind: job.kind, attempts: job.attempts, error: message.slice(0, 500) },
    });
    return;
  }

  // Exponential backoff with jitter, so a platform outage does not produce a
  // synchronized retry stampede once it recovers.
  const base = err.retryAfterSeconds * Math.pow(2, job.attempts - 1);
  const delay = Math.min(base, 3600) * (0.75 + Math.random() * 0.5);
  await db(env).run(
    `UPDATE jobs
        SET status = 'pending', locked_until = NULL, run_after = ?, last_error = ?, updated_at = ?
      WHERE id = ?`,
    new Date(Date.now() + delay * 1000).toISOString(),
    message.slice(0, 1000),
    nowIso(),
    job.id,
  );
}

export async function drain(
  env: Env,
  handlers: Record<JobKind, JobHandler>,
  limit: number,
): Promise<{ processed: number; failed: number }> {
  await reapExpiredLocks(env);

  const jobs = await claim(env, limit);
  let failed = 0;

  for (const job of jobs) {
    const handler = handlers[job.kind];
    if (!handler) {
      await fail(env, job, new Error(`No handler registered for job kind "${job.kind}"`));
      failed++;
      continue;
    }
    try {
      const payload = JSON.parse(job.payload) as Record<string, unknown>;
      await handler(env, job, payload);
      await succeed(env, job);
    } catch (err) {
      console.error(`job ${job.kind} (${job.id}) failed`, err);
      await fail(env, job, err);
      failed++;
    }
  }

  return { processed: jobs.length, failed };
}
