import { Hono } from 'hono';
import { z } from 'zod';
import type { AppBindings } from '../env';
import { audit, db, usageFor } from '../lib/db';
import { nowIso } from '../lib/ids';
import { requireAuth } from '../lib/auth';
import { badRequest, notFound } from '../lib/errors';
import { PLANS, type AccountRecord, type PostRecord } from '../lib/types';
import { enqueue } from '../queue/jobs';

export const workspace = new Hono<AppBindings>();

workspace.use('/v1/calendar', requireAuth);
workspace.use('/v1/calendar/*', requireAuth);
workspace.use('/v1/posts', requireAuth);
workspace.use('/v1/posts/*', requireAuth);
workspace.use('/v1/insights', requireAuth);

workspace.get('/v1/calendar', async (c) => {
  const { accountId } = c.get('ctx');
  const days = Math.min(60, Math.max(1, Number(c.req.query('days') ?? 14)));
  const until = new Date(Date.now() + days * 86_400_000).toISOString();

  const slots = await db(c.env).all(
    `SELECT s.id, s.scheduled_for, s.status, c.platform, c.handle, pi.name AS pillar,
            p.id AS post_id, p.hook, p.body, p.status AS post_status
       FROM slots s
       JOIN channels c ON c.id = s.channel_id
       JOIN pillars pi ON pi.id = s.pillar_id
       LEFT JOIN posts p ON p.slot_id = s.id AND p.variant = 1
      WHERE s.account_id = ? AND s.scheduled_for <= ?
      ORDER BY s.scheduled_for ASC`,
    accountId,
    until,
  );

  return c.json({ slots });
});

/** Manual trigger for the planner. The cron does this daily; this is for onboarding. */
workspace.post('/v1/calendar/plan', async (c) => {
  const { accountId } = c.get('ctx');
  const bucket = Math.floor(Date.now() / 3600_000);
  const id = await enqueue(
    c.env,
    'plan.generate',
    {},
    { accountId, idempotencyKey: `plan:${accountId}:${bucket}` },
  );
  return c.json({ queued: Boolean(id), note: id ? undefined : 'A plan run is already queued this hour' });
});

workspace.get('/v1/posts', async (c) => {
  const { accountId } = c.get('ctx');
  const status = c.req.query('status');
  const limit = Math.min(200, Math.max(1, Number(c.req.query('limit') ?? 50)));

  const rows = status
    ? await db(c.env).all(
        `SELECT p.*, c.platform FROM posts p JOIN channels c ON c.id = p.channel_id
          WHERE p.account_id = ? AND p.status = ? ORDER BY p.created_at DESC LIMIT ?`,
        accountId,
        status,
        limit,
      )
    : await db(c.env).all(
        `SELECT p.*, c.platform FROM posts p JOIN channels c ON c.id = p.channel_id
          WHERE p.account_id = ? ORDER BY p.created_at DESC LIMIT ?`,
        accountId,
        limit,
      );

  return c.json({ posts: rows });
});

const editSchema = z.object({ body: z.string().min(1).max(6000).optional() });

/**
 * Approving a variant promotes it to the slot's publishing candidate. This is
 * the human-in-the-loop path: with autopilot off, nothing publishes until a
 * request lands here.
 */
workspace.post('/v1/posts/:id/approve', async (c) => {
  const { accountId, keyId } = c.get('ctx');
  const postId = c.req.param('id');

  const post = await db(c.env).scoped<PostRecord>('posts', postId, accountId);
  if (!post) throw notFound('Post');
  if (post.status === 'published') throw badRequest('That post is already published');

  const parsed = editSchema.safeParse(await c.req.json().catch(() => ({})));
  if (!parsed.success) throw badRequest('Invalid edit payload', parsed.error.issues);
  const body = parsed.data.body ?? post.body;

  const now = nowIso();
  await db(c.env).batch([
    // Demote whatever was the candidate, so exactly one variant is variant 1.
    {
      sql: `UPDATE posts SET variant = 2, status = 'draft', updated_at = ?
             WHERE slot_id = ? AND id != ? AND variant = 1`,
      binds: [now, post.slot_id, postId],
    },
    {
      sql: `UPDATE posts
               SET variant = 1, body = ?, status = 'approved', approved_at = ?,
                   approved_by = ?, updated_at = ?
             WHERE id = ?`,
      binds: [body, now, `key:${keyId}`, now, postId],
    },
    {
      sql: `UPDATE slots SET status = 'approved', updated_at = ? WHERE id = ?`,
      binds: [now, post.slot_id],
    },
  ]);

  await audit(c.env, {
    accountId,
    actor: `key:${keyId}`,
    action: 'post.approved',
    entityType: 'post',
    entityId: postId,
    detail: { edited: body !== post.body },
  });

  return c.json({ ok: true });
});

workspace.post('/v1/posts/:id/reject', async (c) => {
  const { accountId, keyId } = c.get('ctx');
  const postId = c.req.param('id');

  const post = await db(c.env).scoped<PostRecord>('posts', postId, accountId);
  if (!post) throw notFound('Post');
  if (post.status === 'published') throw badRequest('That post is already published');

  const now = nowIso();
  await db(c.env).run(
    `UPDATE posts SET status = 'rejected', updated_at = ? WHERE id = ?`,
    now,
    postId,
  );

  // If the rejected post was the candidate, the slot has nothing to publish.
  const remaining = await db(c.env).first<{ n: number }>(
    `SELECT COUNT(*) AS n FROM posts WHERE slot_id = ? AND status IN ('draft', 'approved')`,
    post.slot_id,
  );
  if ((remaining?.n ?? 0) === 0) {
    await db(c.env).run(
      `UPDATE slots SET status = 'skipped', updated_at = ? WHERE id = ?`,
      now,
      post.slot_id,
    );
  }

  await audit(c.env, {
    accountId,
    actor: `key:${keyId}`,
    action: 'post.rejected',
    entityType: 'post',
    entityId: postId,
    detail: {},
  });

  return c.json({ ok: true });
});

/**
 * The number a creator actually cares about: is this working, and what is
 * working. Pillar performance is surfaced because it is what the growth engine
 * acts on, and an automated system that changes strategy silently is not one
 * anybody trusts for long.
 */
workspace.get('/v1/insights', async (c) => {
  const { accountId } = c.get('ctx');
  const since = new Date(Date.now() - 30 * 86_400_000).toISOString();

  const account = await db(c.env).first<AccountRecord>(
    `SELECT * FROM accounts WHERE id = ?`,
    accountId,
  );
  if (!account) throw notFound('Account');

  const totals = await db(c.env).first<{
    posts: number;
    impressions: number;
    engagements: number;
    follows: number;
  }>(
    `SELECT COUNT(DISTINCT p.id) AS posts,
            COALESCE(SUM(m.impressions), 0) AS impressions,
            COALESCE(SUM(m.likes + m.comments + m.shares + m.saves), 0) AS engagements,
            COALESCE(SUM(m.follows), 0) AS follows
       FROM posts p
       LEFT JOIN post_metrics m ON m.post_id = p.id
      WHERE p.account_id = ? AND p.published_at >= ?`,
    accountId,
    since,
  );

  const pillars = await db(c.env).all(
    `SELECT pi.name, pi.weight, COUNT(DISTINCT p.id) AS posts,
            ROUND(AVG(m.score), 2) AS avg_score
       FROM pillars pi
       LEFT JOIN posts p ON p.pillar_id = pi.id AND p.published_at >= ?
       LEFT JOIN post_metrics m ON m.post_id = p.id
      WHERE pi.account_id = ? AND pi.active = 1
      GROUP BY pi.id
      ORDER BY avg_score DESC`,
    since,
    accountId,
  );

  const hoursSaved = await estimateHoursSaved(c.env, accountId);

  return c.json({
    window: '30d',
    totals,
    pillars,
    usage: {
      postsPublished: await usageFor(c.env, accountId, 'posts_published'),
      repliesSent: await usageFor(c.env, accountId, 'replies_sent'),
      planLimits: PLANS[account.plan],
    },
    hoursSaved,
  });
});

/**
 * A deliberately conservative estimate, shown to the creator as the retention
 * argument. The per-item minutes are stated in the response so nobody has to
 * take the headline number on faith.
 */
async function estimateHoursSaved(
  env: AppBindings['Bindings'],
  accountId: string,
): Promise<{ hours: number; basis: Record<string, number> }> {
  const since = new Date(Date.now() - 30 * 86_400_000).toISOString();

  const posts = await db(env).first<{ n: number }>(
    `SELECT COUNT(*) AS n FROM posts WHERE account_id = ? AND published_at >= ?`,
    accountId,
    since,
  );
  const replies = await db(env).first<{ n: number }>(
    `SELECT COUNT(*) AS n FROM reply_drafts WHERE account_id = ? AND sent_at >= ?`,
    accountId,
    since,
  );

  const MINUTES_PER_POST = 12;
  const MINUTES_PER_REPLY = 2;
  const minutes = (posts?.n ?? 0) * MINUTES_PER_POST + (replies?.n ?? 0) * MINUTES_PER_REPLY;

  return {
    hours: Math.round((minutes / 60) * 10) / 10,
    basis: {
      posts: posts?.n ?? 0,
      minutesPerPost: MINUTES_PER_POST,
      replies: replies?.n ?? 0,
      minutesPerReply: MINUTES_PER_REPLY,
    },
  };
}
