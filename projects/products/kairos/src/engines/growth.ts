import type { Env } from '../env';
import { audit, db } from '../lib/db';
import { newId, nowIso } from '../lib/ids';
import { adapterFor } from '../adapters/registry';
import type { ChannelRecord, PillarRecord, PostRecord } from '../lib/types';
import type { Job } from '../queue/jobs';
import type { MetricsSnapshot } from '../adapters/types';

/**
 * Value weights per engagement action, expressed relative to a like.
 *
 * These encode a judgement: a follow is worth far more to a creator than a like,
 * because it is the only action that compounds into future distribution. A
 * creator optimising for likes gets a popular account that sells nothing.
 */
const ACTION_VALUE = {
  likes: 1,
  comments: 4,
  shares: 6,
  saves: 5,
  clicks: 3,
  follows: 20,
} as const;

const LOOKBACK_DAYS = 30;
const RECYCLE_MIN_AGE_DAYS = 45;
const SMOOTHING = 0.4; // how far a weight moves toward its new target per cycle

export function scoreOf(m: MetricsSnapshot): number {
  const value =
    m.likes * ACTION_VALUE.likes +
    m.comments * ACTION_VALUE.comments +
    m.shares * ACTION_VALUE.shares +
    m.saves * ACTION_VALUE.saves +
    m.clicks * ACTION_VALUE.clicks +
    m.follows * ACTION_VALUE.follows;

  // Per-thousand-impressions so a post that reached 400 people and a post that
  // reached 40,000 are comparable. Posts with no impression data fall back to
  // raw value, which keeps LinkedIn (which does not report impressions on this
  // endpoint) from scoring zero across the board.
  return m.impressions > 0 ? (value / m.impressions) * 1000 : value;
}

export async function handleMetricsCollect(
  env: Env,
  _job: Job,
  payload: Record<string, unknown>,
): Promise<void> {
  const postId = String(payload.postId ?? '');
  if (!postId) throw new Error('metrics.collect requires a postId');

  const post = await db(env).first<PostRecord>(`SELECT * FROM posts WHERE id = ?`, postId);
  if (!post || post.status !== 'published' || !post.external_post_id) return;

  const channel = await db(env).first<ChannelRecord>(
    `SELECT * FROM channels WHERE id = ?`,
    post.channel_id,
  );
  if (!channel || channel.status !== 'connected') return;

  const snapshot = await adapterFor(env, channel.platform).fetchMetrics(
    channel.access_token ?? '',
    post.external_post_id,
  );

  await db(env).run(
    `INSERT INTO post_metrics
       (id, post_id, account_id, captured_at, impressions, likes, comments, shares,
        saves, clicks, follows, score)
     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
    newId('met'),
    postId,
    post.account_id,
    nowIso(),
    snapshot.impressions,
    snapshot.likes,
    snapshot.comments,
    snapshot.shares,
    snapshot.saves,
    snapshot.clicks,
    snapshot.follows,
    scoreOf(snapshot),
  );
}

/**
 * Rewrites pillar weights from measured performance and queues recycles.
 *
 * This is the part that turns automation into a growth engine. Without it the
 * system publishes the same distribution of content forever, no matter what the
 * audience responds to.
 */
export async function handleGrowthRebalance(env: Env, job: Job): Promise<void> {
  const accountId = job.account_id;
  if (!accountId) throw new Error('growth.rebalance requires an account_id');

  const since = new Date(Date.now() - LOOKBACK_DAYS * 86_400_000).toISOString();

  // Latest metric per post, averaged by pillar. Using the latest rather than the
  // mean of all snapshots avoids double-counting the early and settled reads.
  const perf = await db(env).all<{ pillar_id: string; avg_score: number; n: number }>(
    `SELECT p.pillar_id,
            AVG(latest.score) AS avg_score,
            COUNT(*) AS n
       FROM posts p
       JOIN (
         SELECT m.post_id, m.score
           FROM post_metrics m
           JOIN (
             SELECT post_id, MAX(captured_at) AS captured_at
               FROM post_metrics
              WHERE account_id = ?
              GROUP BY post_id
           ) newest
             ON newest.post_id = m.post_id AND newest.captured_at = m.captured_at
       ) latest ON latest.post_id = p.id
      WHERE p.account_id = ? AND p.published_at >= ?
      GROUP BY p.pillar_id`,
    accountId,
    accountId,
    since,
  );

  const pillars = await db(env).all<PillarRecord>(
    `SELECT * FROM pillars WHERE account_id = ? AND active = 1`,
    accountId,
  );
  if (pillars.length === 0) return;

  // A pillar needs a few posts before its average means anything. Below the
  // floor it keeps its current weight rather than being judged on one lucky post.
  const MIN_SAMPLES = 3;
  const usable = perf.filter((p) => p.n >= MIN_SAMPLES);
  if (usable.length < 2) {
    await audit(env, {
      accountId,
      actor: 'system:growth',
      action: 'rebalance.deferred',
      entityType: 'account',
      entityId: accountId,
      detail: { reason: 'Not enough measured pillars yet', measured: usable.length },
    });
    return;
  }

  const overallMean = usable.reduce((sum, p) => sum + p.avg_score, 0) / usable.length;
  if (overallMean <= 0) return;

  const scoreById = new Map(usable.map((p) => [p.pillar_id, p.avg_score] as const));
  const changes: Array<{ name: string; from: number; to: number }> = [];

  for (const pillar of pillars) {
    const measured = scoreById.get(pillar.id);
    if (measured === undefined) continue;

    const target = clamp(measured / overallMean, 0.25, 3);
    // Move partway toward the target so one strong month does not collapse the
    // calendar onto a single pillar, which reads as repetitive to an audience.
    const next = round2(pillar.weight + (target - pillar.weight) * SMOOTHING);
    if (Math.abs(next - pillar.weight) < 0.01) continue;

    await db(env).run(
      `UPDATE pillars SET weight = ?, updated_at = ? WHERE id = ?`,
      next,
      nowIso(),
      pillar.id,
    );
    changes.push({ name: pillar.name, from: pillar.weight, to: next });
  }

  const recycled = await scheduleRecycles(env, accountId);

  await audit(env, {
    accountId,
    actor: 'system:growth',
    action: 'rebalance.applied',
    entityType: 'account',
    entityId: accountId,
    detail: { overallMean: round2(overallMean), changes, recycled },
  });
}

/**
 * Re-queues proven posts. An audience turns over, and the best-performing post
 * from two months ago will be new to most of the people who see it now. This is
 * the cheapest distribution a creator has, and nobody does it by hand.
 */
async function scheduleRecycles(env: Env, accountId: string): Promise<number> {
  const cutoff = new Date(Date.now() - RECYCLE_MIN_AGE_DAYS * 86_400_000).toISOString();

  const winners = await db(env).all<PostRecord & { score: number }>(
    `SELECT p.*, m.score
       FROM posts p
       JOIN post_metrics m ON m.post_id = p.id
      WHERE p.account_id = ?
        AND p.status = 'published'
        AND p.published_at <= ?
        AND p.recycled_from IS NULL
        AND NOT EXISTS (SELECT 1 FROM posts r WHERE r.recycled_from = p.id)
      ORDER BY m.score DESC
      LIMIT 3`,
    accountId,
    cutoff,
  );

  let count = 0;
  for (const winner of winners) {
    // Land the recycle in an empty slot a few days out rather than displacing
    // something already planned.
    const when = new Date(Date.now() + (3 + count) * 86_400_000);
    when.setUTCHours(15, 0, 0, 0);

    const slotId = newId('slot');
    const now = nowIso();
    const inserted = await db(env).run(
      `INSERT OR IGNORE INTO slots
         (id, account_id, channel_id, pillar_id, scheduled_for, status, created_at, updated_at)
       VALUES (?, ?, ?, ?, ?, 'approved', ?, ?)`,
      slotId,
      accountId,
      winner.channel_id,
      winner.pillar_id,
      when.toISOString(),
      now,
      now,
    );
    if (inserted.meta.changes === 0) continue;

    await db(env).run(
      `INSERT INTO posts
         (id, account_id, slot_id, channel_id, pillar_id, variant, hook, body,
          status, approved_at, approved_by, recycled_from, created_at, updated_at)
       VALUES (?, ?, ?, ?, ?, 1, ?, ?, 'approved', ?, 'autopilot:recycle', ?, ?, ?)`,
      newId('post'),
      accountId,
      slotId,
      winner.channel_id,
      winner.pillar_id,
      winner.hook,
      winner.body,
      now,
      winner.id,
      now,
      now,
    );
    count++;
  }

  return count;
}

function clamp(n: number, lo: number, hi: number): number {
  return Math.min(hi, Math.max(lo, n));
}

function round2(n: number): number {
  return Math.round(n * 100) / 100;
}
