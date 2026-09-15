import type { Env } from '../env';
import { audit, db, meter } from '../lib/db';
import { newId, nowIso } from '../lib/ids';
import { canGenerate, controlsFor } from '../lib/governance';
import type { ChannelRecord, PillarRecord, SlotRecord } from '../lib/types';
import { DRAFT_SCHEMA, draftPrompt, strategySystem } from '../ai/prompts';
import { generateJson, loadCreator, recordUsage, OPERATOR_SYSTEM_REF } from './shared';
import type { Job } from '../queue/jobs';

const VARIANTS = 3;

interface DraftResponse {
  variants: Array<{ hook: string; body: string }>;
}

/**
 * Drafts content for one planned slot.
 *
 * Several variants are generated per slot rather than one. The extra cost is
 * small next to a token budget dominated by the cached prefix, and it gives the
 * growth engine something to compare when it decides what this creator's
 * audience actually responds to.
 */
export async function handleContentDraft(
  env: Env,
  job: Job,
  payload: Record<string, unknown>,
): Promise<void> {
  const slotId = String(payload.slotId ?? '');
  const angle = String(payload.angle ?? '');
  if (!slotId) throw new Error('content.draft requires a slotId');

  const slot = await db(env).first<SlotRecord>(`SELECT * FROM slots WHERE id = ?`, slotId);
  if (!slot) throw new Error(`Slot ${slotId} not found`);
  if (slot.status !== 'planned') return; // already drafted, or cancelled

  const { account, strategy, pillars } = await loadCreator(env, slot.account_id);

  const gate = await canGenerate(env, account);
  if (!gate.allowed) {
    await markSlot(env, slotId, 'skipped');
    await audit(env, {
      accountId: account.id,
      actor: 'system:content',
      action: 'draft.skipped',
      entityType: 'slot',
      entityId: slotId,
      detail: { reason: gate.reason },
    });
    return;
  }

  const channel = await db(env).first<ChannelRecord>(
    `SELECT * FROM channels WHERE id = ?`,
    slot.channel_id,
  );
  const pillar = pillars.find((p) => p.id === slot.pillar_id);
  if (!channel || !pillar) {
    await markSlot(env, slotId, 'failed');
    throw new Error(`Slot ${slotId} references a missing channel or pillar`);
  }

  await markSlot(env, slotId, 'drafting');

  const { data, result } = await generateJson<DraftResponse>(env, {
    stableSystem: OPERATOR_SYSTEM_REF,
    creatorSystem: strategySystem(strategy, pillars),
    userPrompt: draftPrompt({
      platform: channel.platform,
      pillarName: pillar.name,
      angle,
      variants: VARIANTS,
      winningExamples: await topPerformers(env, account.id, channel.platform),
    }),
    schema: DRAFT_SCHEMA as unknown as Record<string, unknown>,
    effort: 'medium',
  });

  await recordUsage(env, account.id, result.usage);

  if (result.refused || !data || data.variants.length === 0) {
    await markSlot(env, slotId, 'failed');
    await audit(env, {
      accountId: account.id,
      actor: 'system:content',
      action: 'draft.refused',
      entityType: 'slot',
      entityId: slotId,
      detail: { category: result.refusalCategory },
    });
    return;
  }

  const banned = parseList(strategy.banned_phrases);
  const controls = await controlsFor(env, account.id);
  const now = nowIso();
  let index = 0;

  for (const variant of data.variants.slice(0, VARIANTS)) {
    const violation = banned.find((phrase) =>
      variant.body.toLowerCase().includes(phrase.toLowerCase()),
    );
    // The banned-phrase list is a promise to the creator, so it is enforced in
    // code after generation rather than trusted to the prompt alone.
    if (violation) {
      await audit(env, {
        accountId: account.id,
        actor: 'system:content',
        action: 'draft.rejected',
        entityType: 'slot',
        entityId: slotId,
        detail: { reason: 'banned phrase', phrase: violation },
      });
      continue;
    }

    index++;
    // Variant 1 is the candidate for publishing; the rest are alternates the
    // creator can swap in. Under autopilot the candidate is pre-approved.
    const isCandidate = index === 1;
    const autoApprove = isCandidate && controls.autopilot_publishing === 1;

    await db(env).run(
      `INSERT INTO posts
         (id, account_id, slot_id, channel_id, pillar_id, variant, hook, body,
          status, approved_at, approved_by, generation_meta, created_at, updated_at)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
      newId('post'),
      account.id,
      slotId,
      channel.id,
      pillar.id,
      index,
      variant.hook.slice(0, 300),
      variant.body,
      autoApprove ? 'approved' : 'draft',
      autoApprove ? now : null,
      autoApprove ? 'autopilot' : null,
      JSON.stringify({
        model: result.model,
        angle,
        input_tokens: result.usage.inputTokens,
        output_tokens: result.usage.outputTokens,
        cache_read_tokens: result.usage.cacheReadTokens,
      }),
      now,
      now,
    );
    await meter(env, account.id, 'drafts_generated');
  }

  if (index === 0) {
    await markSlot(env, slotId, 'failed');
    return;
  }

  await markSlot(env, slotId, controls.autopilot_publishing === 1 ? 'approved' : 'ready');
  await audit(env, {
    accountId: account.id,
    actor: 'system:content',
    action: 'draft.created',
    entityType: 'slot',
    entityId: slotId,
    detail: { variants: index, autopilot: controls.autopilot_publishing === 1 },
  });
}

/**
 * The creator's own best-performing posts, used to calibrate voice. Restricted
 * to the same platform because what reads well on LinkedIn reads as padding on X.
 */
async function topPerformers(env: Env, accountId: string, platform: string): Promise<string[]> {
  const rows = await db(env).all<{ body: string }>(
    `SELECT p.body
       FROM posts p
       JOIN channels c ON c.id = p.channel_id
       JOIN post_metrics m ON m.post_id = p.id
      WHERE p.account_id = ? AND c.platform = ? AND p.status = 'published'
      ORDER BY m.score DESC
      LIMIT 3`,
    accountId,
    platform,
  );
  return rows.map((r) => r.body);
}

async function markSlot(env: Env, slotId: string, status: SlotRecord['status']): Promise<void> {
  await db(env).run(
    `UPDATE slots SET status = ?, updated_at = ? WHERE id = ?`,
    status,
    nowIso(),
    slotId,
  );
}

function parseList(raw: string): string[] {
  try {
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) ? parsed.map(String).filter(Boolean) : [];
  } catch {
    return [];
  }
}

export type { PillarRecord };
