import type { Env } from '../env';
import { audit, db, meter } from '../lib/db';
import { newId, nowIso } from '../lib/ids';
import { canAutoReply } from '../lib/governance';
import { adapterFor } from '../adapters/registry';
import type { ChannelRecord, ConversationRecord } from '../lib/types';
import { REPLY_SCHEMA, TRIAGE_SCHEMA, replyPrompt, strategySystem, triagePrompt } from '../ai/prompts';
import { generateJson, loadCreator, recordUsage, OPERATOR_SYSTEM_REF } from './shared';
import { enqueue, type Job } from '../queue/jobs';

interface TriageResponse {
  intent: string;
  priority: number;
  reasoning: string;
}

interface ReplyResponse {
  reply: string;
  confidence: number;
  escalate: boolean;
  escalation_reason: string;
}

/** Cron entry point: queue an inbox sync for every connected channel. */
export async function enqueueInboxSyncs(env: Env): Promise<number> {
  const channels = await db(env).all<{ id: string; account_id: string }>(
    `SELECT c.id, c.account_id
       FROM channels c
       JOIN accounts a ON a.id = c.account_id
      WHERE c.status = 'connected' AND a.status IN ('active', 'past_due')
      LIMIT 500`,
  );

  const bucket = Math.floor(Date.now() / (15 * 60_000));
  let enqueued = 0;
  for (const channel of channels) {
    const id = await enqueue(
      env,
      'inbox.sync',
      { channelId: channel.id },
      {
        accountId: channel.account_id,
        // One sync per channel per 15-minute bucket.
        idempotencyKey: `inbox:${channel.id}:${bucket}`,
      },
    );
    if (id) enqueued++;
  }
  return enqueued;
}

export async function handleInboxSync(
  env: Env,
  _job: Job,
  payload: Record<string, unknown>,
): Promise<void> {
  const channelId = String(payload.channelId ?? '');
  if (!channelId) throw new Error('inbox.sync requires a channelId');

  const channel = await db(env).first<ChannelRecord>(
    `SELECT * FROM channels WHERE id = ?`,
    channelId,
  );
  if (!channel || channel.status !== 'connected') return;

  const since = new Date(Date.now() - 3600_000).toISOString();
  const inbound = await adapterFor(env, channel.platform).fetchInbound(
    channel.access_token ?? '',
    since,
  );

  for (const message of inbound) {
    const conversationId = await upsertConversation(env, channel, message.threadId, {
      authorHandle: message.authorHandle,
      lastMessageAt: message.createdAt,
    });

    const res = await db(env).run(
      `INSERT OR IGNORE INTO messages
         (id, conversation_id, account_id, direction, body, external_id, created_at)
       VALUES (?, ?, ?, 'inbound', ?, ?, ?)`,
      newId('msg'),
      conversationId,
      channel.account_id,
      message.body,
      message.externalId,
      message.createdAt,
    );
    // Only draft a reply when the message is genuinely new. Re-syncing an
    // already-seen thread must not produce a second reply.
    if (res.meta.changes === 0) continue;

    await enqueue(
      env,
      'reply.draft',
      { conversationId },
      {
        accountId: channel.account_id,
        idempotencyKey: `reply-draft:${message.externalId}`,
      },
    );
  }
}

async function upsertConversation(
  env: Env,
  channel: ChannelRecord,
  threadId: string,
  info: { authorHandle: string; lastMessageAt: string },
): Promise<string> {
  const existing = await db(env).first<{ id: string }>(
    `SELECT id FROM conversations WHERE channel_id = ? AND platform_thread_id = ?`,
    channel.id,
    threadId,
  );

  if (existing) {
    await db(env).run(
      `UPDATE conversations
          SET last_message_at = ?, status = CASE WHEN status = 'answered' THEN 'open' ELSE status END,
              updated_at = ?
        WHERE id = ?`,
      info.lastMessageAt,
      nowIso(),
      existing.id,
    );
    return existing.id;
  }

  const id = newId('conv');
  const now = nowIso();
  await db(env).run(
    `INSERT INTO conversations
       (id, account_id, channel_id, platform_thread_id, author_handle, intent, priority,
        status, last_message_at, created_at, updated_at)
     VALUES (?, ?, ?, ?, ?, 'unclassified', 3, 'open', ?, ?, ?)`,
    id,
    channel.account_id,
    channel.id,
    threadId,
    info.authorHandle,
    info.lastMessageAt,
    now,
    now,
  );
  return id;
}

/**
 * Classifies a conversation and drafts a reply.
 *
 * Triage and drafting are two calls rather than one because the intent decides
 * whether the reply may send unattended, and folding that decision into the same
 * call that writes the reply lets a persuasive draft argue for its own release.
 */
export async function handleReplyDraft(
  env: Env,
  _job: Job,
  payload: Record<string, unknown>,
): Promise<void> {
  const conversationId = String(payload.conversationId ?? '');
  if (!conversationId) throw new Error('reply.draft requires a conversationId');

  const convo = await db(env).first<ConversationRecord>(
    `SELECT * FROM conversations WHERE id = ?`,
    conversationId,
  );
  if (!convo || convo.status === 'ignored') return;

  const { account, strategy, pillars } = await loadCreator(env, convo.account_id);
  const creatorSystem = strategySystem(strategy, pillars);

  const messages = await db(env).all<{ body: string; direction: string }>(
    `SELECT body, direction FROM messages WHERE conversation_id = ?
      ORDER BY created_at DESC LIMIT 10`,
    conversationId,
  );
  const inboundBodies = messages
    .filter((m) => m.direction === 'inbound')
    .map((m) => m.body)
    .reverse();
  if (inboundBodies.length === 0) return;

  const triage = await generateJson<TriageResponse>(env, {
    stableSystem: OPERATOR_SYSTEM_REF,
    creatorSystem,
    userPrompt: triagePrompt({ author: convo.author_handle, messages: inboundBodies }),
    schema: TRIAGE_SCHEMA as unknown as Record<string, unknown>,
    effort: 'low',
    maxTokens: 2_000,
  });
  await recordUsage(env, account.id, triage.result.usage);

  const intent = triage.data?.intent ?? 'unclassified';
  const priority = triage.data?.priority ?? 3;

  await db(env).run(
    `UPDATE conversations SET intent = ?, priority = ?, updated_at = ? WHERE id = ?`,
    intent,
    priority,
    nowIso(),
    conversationId,
  );

  // Spam gets closed rather than answered. Answering it trains the sender that
  // the account replies, and costs the creator attention for nothing.
  if (intent === 'spam') {
    await db(env).run(
      `UPDATE conversations SET status = 'ignored', updated_at = ? WHERE id = ?`,
      nowIso(),
      conversationId,
    );
    return;
  }

  const channel = await db(env).first<ChannelRecord>(
    `SELECT * FROM channels WHERE id = ?`,
    convo.channel_id,
  );

  const draft = await generateJson<ReplyResponse>(env, {
    stableSystem: OPERATOR_SYSTEM_REF,
    creatorSystem,
    userPrompt: replyPrompt({
      intent,
      author: convo.author_handle,
      messages: inboundBodies,
      platform: channel?.platform ?? 'social',
    }),
    schema: REPLY_SCHEMA as unknown as Record<string, unknown>,
    effort: 'medium',
    maxTokens: 4_000,
  });
  await recordUsage(env, account.id, draft.result.usage);

  if (draft.result.refused || !draft.data) {
    await db(env).run(
      `UPDATE conversations SET status = 'awaiting_review', updated_at = ? WHERE id = ?`,
      nowIso(),
      conversationId,
    );
    return;
  }

  // A model that asks to escalate is telling us its own confidence is unreliable,
  // so the confidence figure is discarded rather than averaged in.
  const confidence = draft.data.escalate ? 0 : clamp01(draft.data.confidence);
  const gate = await canAutoReply(env, account, intent, confidence);

  const draftId = newId('rdr');
  const now = nowIso();
  await db(env).run(
    `INSERT INTO reply_drafts
       (id, conversation_id, account_id, body, confidence, status, auto_approved,
        created_at, updated_at)
     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)`,
    draftId,
    conversationId,
    account.id,
    draft.data.reply,
    confidence,
    gate.allowed ? 'approved' : 'pending',
    gate.allowed ? 1 : 0,
    now,
    now,
  );

  await db(env).run(
    `UPDATE conversations SET status = 'awaiting_review', updated_at = ? WHERE id = ?`,
    nowIso(),
    conversationId,
  );

  await audit(env, {
    accountId: account.id,
    actor: 'system:engagement',
    action: gate.allowed ? 'reply.auto_approved' : 'reply.queued_for_review',
    entityType: 'conversation',
    entityId: conversationId,
    detail: {
      intent,
      confidence,
      escalate: draft.data.escalate,
      escalationReason: draft.data.escalation_reason,
      gate: gate.reason,
    },
  });

  if (gate.allowed) {
    await enqueue(
      env,
      'reply.send',
      { draftId },
      { accountId: account.id, idempotencyKey: `reply-send:${draftId}` },
    );
  }
}

export async function handleReplySend(
  env: Env,
  _job: Job,
  payload: Record<string, unknown>,
): Promise<void> {
  const draftId = String(payload.draftId ?? '');
  if (!draftId) throw new Error('reply.send requires a draftId');

  const draft = await db(env).first<{
    id: string;
    conversation_id: string;
    account_id: string;
    body: string;
    status: string;
  }>(`SELECT * FROM reply_drafts WHERE id = ?`, draftId);
  if (!draft || draft.status !== 'approved') return;

  const convo = await db(env).first<ConversationRecord>(
    `SELECT * FROM conversations WHERE id = ?`,
    draft.conversation_id,
  );
  if (!convo) return;

  const channel = await db(env).first<ChannelRecord>(
    `SELECT * FROM channels WHERE id = ?`,
    convo.channel_id,
  );
  if (!channel || channel.status !== 'connected') return;

  const sent = await adapterFor(env, channel.platform).sendReply({
    threadId: convo.platform_thread_id,
    body: draft.body,
    accessToken: channel.access_token ?? '',
  });

  const now = nowIso();
  await db(env).batch([
    {
      sql: `UPDATE reply_drafts SET status = 'sent', sent_at = ?, updated_at = ? WHERE id = ?`,
      binds: [now, now, draftId],
    },
    {
      sql: `UPDATE conversations SET status = 'answered', updated_at = ? WHERE id = ?`,
      binds: [now, draft.conversation_id],
    },
    {
      sql: `INSERT INTO messages
              (id, conversation_id, account_id, direction, body, external_id, created_at)
            VALUES (?, ?, ?, 'outbound', ?, ?, ?)`,
      binds: [
        newId('msg'),
        draft.conversation_id,
        draft.account_id,
        draft.body,
        sent.externalId,
        now,
      ],
    },
  ]);

  await meter(env, draft.account_id, 'replies_sent');
  await audit(env, {
    accountId: draft.account_id,
    actor: 'system:engagement',
    action: 'reply.sent',
    entityType: 'conversation',
    entityId: draft.conversation_id,
    detail: { draftId, platform: channel.platform, dryRun: env.DRY_RUN !== 'false' },
  });
}

function clamp01(n: number): number {
  if (!Number.isFinite(n)) return 0;
  return Math.min(1, Math.max(0, n));
}
