import type { Env } from '../env';
import { audit, db, meter } from '../lib/db';
import { nowIso } from '../lib/ids';
import { canPublish } from '../lib/governance';
import { adapterFor } from '../adapters/registry';
import type { AccountRecord, ChannelRecord, PostRecord } from '../lib/types';
import { enqueue, type Job } from '../queue/jobs';
import { RetryableError } from '../lib/errors';

const LOOKAHEAD_MS = 15 * 60_000;

/**
 * Cron entry point: converts approved slots that are about to come due into
 * publish jobs. Kept separate from the dispatch handler so that scanning is
 * cheap and idempotent, and the actual network call happens in a retryable job.
 */
export async function enqueueDuePublishes(env: Env): Promise<number> {
  const due = await db(env).all<{ post_id: string; account_id: string }>(
    `SELECT p.id AS post_id, p.account_id
       FROM slots s
       JOIN posts p ON p.slot_id = s.id AND p.variant = 1
      WHERE s.status = 'approved'
        AND p.status = 'approved'
        AND s.scheduled_for <= ?
      LIMIT 200`,
    new Date(Date.now() + LOOKAHEAD_MS).toISOString(),
  );

  let enqueued = 0;
  for (const row of due) {
    const id = await enqueue(
      env,
      'publish.dispatch',
      { postId: row.post_id },
      {
        accountId: row.account_id,
        // One publish job per post, ever. This is the guard that stops an
        // overlapping cron tick from posting the same thing twice.
        idempotencyKey: `publish:${row.post_id}`,
      },
    );
    if (id) enqueued++;
  }
  return enqueued;
}

export async function handlePublishDispatch(
  env: Env,
  _job: Job,
  payload: Record<string, unknown>,
): Promise<void> {
  const postId = String(payload.postId ?? '');
  if (!postId) throw new Error('publish.dispatch requires a postId');

  const post = await db(env).first<PostRecord>(`SELECT * FROM posts WHERE id = ?`, postId);
  if (!post) throw new Error(`Post ${postId} not found`);
  if (post.status === 'published') return;
  if (post.status !== 'approved' && post.status !== 'publishing') {
    // Someone rejected or edited it between scheduling and dispatch.
    return;
  }

  const account = await db(env).first<AccountRecord>(
    `SELECT * FROM accounts WHERE id = ?`,
    post.account_id,
  );
  if (!account) throw new Error(`Account ${post.account_id} not found`);

  const gate = await canPublish(env, account);
  if (!gate.allowed) {
    // A blocked publish is held, not discarded: the post stays approved and the
    // slot is marked so the creator can see what did not go out and why.
    await db(env).run(
      `UPDATE slots SET status = 'skipped', updated_at = ? WHERE id = ?`,
      nowIso(),
      post.slot_id,
    );
    await audit(env, {
      accountId: account.id,
      actor: 'system:publishing',
      action: 'publish.blocked',
      entityType: 'post',
      entityId: postId,
      detail: { reason: gate.reason },
    });
    return;
  }

  const channel = await db(env).first<ChannelRecord>(
    `SELECT * FROM channels WHERE id = ?`,
    post.channel_id,
  );
  if (!channel) throw new Error(`Channel ${post.channel_id} not found`);
  if (channel.status !== 'connected') {
    throw new RetryableError(`Channel ${channel.handle} is ${channel.status}`, 900);
  }

  await setStatus(env, postId, 'publishing');

  const adapter = adapterFor(env, channel.platform);
  const mediaUrls = await resolveMedia(env, post.media_keys);

  let published;
  try {
    published = await adapter.publish({
      body: post.body,
      mediaUrls,
      accessToken: channel.access_token ?? '',
      externalAccountId: channel.external_id,
    });
  } catch (err) {
    await db(env).run(
      `UPDATE posts SET status = 'approved', last_error = ?, updated_at = ? WHERE id = ?`,
      (err instanceof Error ? err.message : String(err)).slice(0, 500),
      nowIso(),
      postId,
    );
    // Returned to 'approved' rather than 'failed' so a retryable error gets
    // another attempt from the queue instead of needing manual re-approval.
    throw err;
  }

  const now = nowIso();
  await db(env).batch([
    {
      sql: `UPDATE posts
               SET status = 'published', published_at = ?, external_post_id = ?,
                   external_url = ?, last_error = NULL, updated_at = ?
             WHERE id = ?`,
      binds: [now, published.externalPostId, published.url, now, postId],
    },
    {
      sql: `UPDATE slots SET status = 'published', updated_at = ? WHERE id = ?`,
      binds: [now, post.slot_id],
    },
  ]);

  await meter(env, account.id, 'posts_published');
  await audit(env, {
    accountId: account.id,
    actor: 'system:publishing',
    action: 'publish.succeeded',
    entityType: 'post',
    entityId: postId,
    detail: { platform: channel.platform, url: published.url, dryRun: env.DRY_RUN !== 'false' },
  });

  // Two collections: an early read for the growth loop, and a settled read once
  // distribution has finished. A single measurement at either point misleads.
  for (const [label, delayMs] of [
    ['early', 2 * 3600_000],
    ['settled', 26 * 3600_000],
  ] as const) {
    await enqueue(
      env,
      'metrics.collect',
      { postId },
      {
        accountId: account.id,
        runAfter: new Date(Date.now() + delayMs),
        idempotencyKey: `metrics:${postId}:${label}`,
      },
    );
  }
}

async function resolveMedia(env: Env, mediaKeysJson: string): Promise<string[]> {
  let keys: string[];
  try {
    const parsed = JSON.parse(mediaKeysJson);
    keys = Array.isArray(parsed) ? parsed.map(String) : [];
  } catch {
    return [];
  }
  return keys.map((key) => `${env.PUBLIC_BASE_URL}/media/${encodeURIComponent(key)}`);
}

async function setStatus(env: Env, postId: string, status: PostRecord['status']): Promise<void> {
  await db(env).run(
    `UPDATE posts SET status = ?, updated_at = ? WHERE id = ?`,
    status,
    nowIso(),
    postId,
  );
}
