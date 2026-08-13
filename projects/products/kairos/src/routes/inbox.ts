import { Hono } from 'hono';
import { z } from 'zod';
import type { AppBindings } from '../env';
import { audit, db } from '../lib/db';
import { newId, nowIso } from '../lib/ids';
import { requireAuth } from '../lib/auth';
import { badRequest, notFound } from '../lib/errors';
import { enqueue } from '../queue/jobs';

export const inbox = new Hono<AppBindings>();

inbox.use('/v1/inbox', requireAuth);
inbox.use('/v1/inbox/*', requireAuth);
inbox.use('/v1/replies/*', requireAuth);
inbox.use('/v1/reply-rules', requireAuth);

/**
 * The triage queue, ordered the way a creator should work it: most consequential
 * first. Conversations already answered by autopilot are excluded by default,
 * because the point is to show only what still needs a person.
 */
inbox.get('/v1/inbox', async (c) => {
  const { accountId } = c.get('ctx');
  const includeAnswered = c.req.query('includeAnswered') === 'true';
  const limit = Math.min(200, Math.max(1, Number(c.req.query('limit') ?? 50)));

  const rows = await db(c.env).all(
    `SELECT cv.id, cv.author_handle, cv.intent, cv.priority, cv.status, cv.last_message_at,
            ch.platform,
            (SELECT body FROM messages m WHERE m.conversation_id = cv.id AND m.direction = 'inbound'
              ORDER BY m.created_at DESC LIMIT 1) AS latest_message,
            (SELECT id FROM reply_drafts d WHERE d.conversation_id = cv.id AND d.status = 'pending'
              ORDER BY d.created_at DESC LIMIT 1) AS pending_draft_id
       FROM conversations cv
       JOIN channels ch ON ch.id = cv.channel_id
      WHERE cv.account_id = ?
        AND (? = 1 OR cv.status NOT IN ('answered', 'ignored'))
      ORDER BY cv.priority ASC, cv.last_message_at DESC
      LIMIT ?`,
    accountId,
    includeAnswered ? 1 : 0,
    limit,
  );

  return c.json({ conversations: rows });
});

inbox.get('/v1/inbox/:id', async (c) => {
  const { accountId } = c.get('ctx');
  const id = c.req.param('id');

  const convo = await db(c.env).scoped('conversations', id, accountId);
  if (!convo) throw notFound('Conversation');

  const messages = await db(c.env).all(
    `SELECT direction, body, created_at FROM messages
      WHERE conversation_id = ? ORDER BY created_at ASC LIMIT 50`,
    id,
  );
  const drafts = await db(c.env).all(
    `SELECT id, body, confidence, status, auto_approved, sent_at, created_at
       FROM reply_drafts WHERE conversation_id = ? ORDER BY created_at DESC`,
    id,
  );

  return c.json({ conversation: convo, messages, drafts });
});

const approveSchema = z.object({ body: z.string().min(1).max(4000).optional() });

inbox.post('/v1/replies/:id/approve', async (c) => {
  const { accountId, keyId } = c.get('ctx');
  const draftId = c.req.param('id');

  const draft = await db(c.env).scoped<{ id: string; status: string; body: string }>(
    'reply_drafts',
    draftId,
    accountId,
  );
  if (!draft) throw notFound('Reply draft');
  if (draft.status === 'sent') throw badRequest('That reply was already sent');

  const parsed = approveSchema.safeParse(await c.req.json().catch(() => ({})));
  if (!parsed.success) throw badRequest('Invalid approval payload', parsed.error.issues);
  const body = parsed.data.body ?? draft.body;

  await db(c.env).run(
    `UPDATE reply_drafts SET body = ?, status = 'approved', updated_at = ? WHERE id = ?`,
    body,
    nowIso(),
    draftId,
  );
  await audit(c.env, {
    accountId,
    actor: `key:${keyId}`,
    action: 'reply.approved',
    entityType: 'reply_draft',
    entityId: draftId,
    detail: { edited: body !== draft.body },
  });

  await enqueue(
    c.env,
    'reply.send',
    { draftId },
    { accountId, idempotencyKey: `reply-send:${draftId}` },
  );

  return c.json({ ok: true });
});

inbox.post('/v1/replies/:id/reject', async (c) => {
  const { accountId, keyId } = c.get('ctx');
  const draftId = c.req.param('id');

  const draft = await db(c.env).scoped<{ id: string; conversation_id: string; status: string }>(
    'reply_drafts',
    draftId,
    accountId,
  );
  if (!draft) throw notFound('Reply draft');
  if (draft.status === 'sent') throw badRequest('That reply was already sent');

  const now = nowIso();
  await db(c.env).batch([
    {
      sql: `UPDATE reply_drafts SET status = 'rejected', updated_at = ? WHERE id = ?`,
      binds: [now, draftId],
    },
    {
      sql: `UPDATE conversations SET status = 'open', updated_at = ? WHERE id = ?`,
      binds: [now, draft.conversation_id],
    },
  ]);

  await audit(c.env, {
    accountId,
    actor: `key:${keyId}`,
    action: 'reply.rejected',
    entityType: 'reply_draft',
    entityId: draftId,
    detail: {},
  });

  return c.json({ ok: true });
});

const rulesSchema = z.object({
  rules: z
    .array(
      z.object({
        intent: z.enum(['question', 'praise', 'support', 'lead', 'collab', 'spam', 'hostile']),
        action: z.enum(['auto_send', 'queue_for_review', 'ignore']),
        minConfidence: z.number().min(0).max(1).default(0.85),
      }),
    )
    .max(10),
});

/**
 * Per-intent auto-send policy. Note that governance.ts refuses to auto-send
 * leads, collabs, and hostile threads regardless of what is configured here:
 * the rule table can tighten the policy, never loosen it past that floor.
 */
inbox.put('/v1/reply-rules', async (c) => {
  const { accountId, keyId } = c.get('ctx');
  const parsed = rulesSchema.safeParse(await c.req.json().catch(() => ({})));
  if (!parsed.success) throw badRequest('Invalid reply rules payload', parsed.error.issues);

  const now = nowIso();
  for (const rule of parsed.data.rules) {
    await db(c.env).run(
      `INSERT INTO reply_rules (id, account_id, intent, action, min_confidence, active, created_at)
       VALUES (?, ?, ?, ?, ?, 1, ?)
       ON CONFLICT(account_id, intent) DO UPDATE SET
         action = excluded.action,
         min_confidence = excluded.min_confidence,
         active = 1`,
      newId('rule'),
      accountId,
      rule.intent,
      rule.action,
      rule.minConfidence,
      now,
    );
  }

  await audit(c.env, {
    accountId,
    actor: `key:${keyId}`,
    action: 'reply_rules.updated',
    entityType: 'account',
    entityId: accountId,
    detail: { rules: parsed.data.rules },
  });

  return c.json({ ok: true, rules: parsed.data.rules });
});
