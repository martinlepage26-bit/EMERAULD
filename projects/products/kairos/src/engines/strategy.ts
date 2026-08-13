import type { Env } from '../env';
import { audit, db } from '../lib/db';
import { newId, nowIso } from '../lib/ids';
import { canGenerate } from '../lib/governance';
import type { AccountRecord, ChannelRecord, PillarRecord, StrategyRecord } from '../lib/types';
import { generateJson, recordUsage, OPERATOR_SYSTEM_REF } from './shared';
import { CALENDAR_SCHEMA, calendarPrompt, strategySystem } from '../ai/prompts';
import { enqueue, type Job } from '../queue/jobs';

const HORIZON_DAYS = 14;

interface CalendarResponse {
  slots: Array<{
    pillar_name: string;
    day_offset: number;
    hour_utc: number;
    angle: string;
  }>;
}

/**
 * Fills the planning horizon for one account.
 *
 * The horizon is a rolling window rather than a batch: this runs daily and tops
 * up whatever is missing, so a creator who connects a channel mid-cycle is
 * caught up on the next tick without anyone scheduling anything by hand.
 */
export async function handlePlanGenerate(env: Env, job: Job): Promise<void> {
  const accountId = job.account_id;
  if (!accountId) throw new Error('plan.generate requires an account_id');

  const account = await db(env).first<AccountRecord>(
    `SELECT * FROM accounts WHERE id = ?`,
    accountId,
  );
  if (!account) throw new Error(`Account ${accountId} not found`);

  const gate = await canGenerate(env, account);
  if (!gate.allowed) {
    await audit(env, {
      accountId,
      actor: 'system:strategy',
      action: 'plan.skipped',
      entityType: 'account',
      entityId: accountId,
      detail: { reason: gate.reason },
    });
    return;
  }

  const strategy = await db(env).first<StrategyRecord>(
    `SELECT * FROM strategies WHERE account_id = ?`,
    accountId,
  );
  const pillars = await db(env).all<PillarRecord>(
    `SELECT * FROM pillars WHERE account_id = ? AND active = 1`,
    accountId,
  );
  if (!strategy || pillars.length === 0) {
    await audit(env, {
      accountId,
      actor: 'system:strategy',
      action: 'plan.skipped',
      entityType: 'account',
      entityId: accountId,
      detail: { reason: 'Onboarding incomplete: strategy or pillars missing' },
    });
    return;
  }

  const channels = await db(env).all<ChannelRecord>(
    `SELECT * FROM channels WHERE account_id = ? AND status = 'connected'`,
    accountId,
  );

  for (const channel of channels) {
    await planChannel(env, account, channel, strategy, pillars);
  }
}

async function planChannel(
  env: Env,
  account: AccountRecord,
  channel: ChannelRecord,
  strategy: StrategyRecord,
  pillars: PillarRecord[],
): Promise<void> {
  const horizonEnd = new Date(Date.now() + HORIZON_DAYS * 86_400_000).toISOString();

  const existing = await db(env).first<{ n: number }>(
    `SELECT COUNT(*) AS n FROM slots
      WHERE channel_id = ? AND scheduled_for BETWEEN ? AND ?
        AND status NOT IN ('skipped', 'failed')`,
    channel.id,
    nowIso(),
    horizonEnd,
  );

  const target = Math.ceil((channel.posts_per_week / 7) * HORIZON_DAYS);
  const needed = target - (existing?.n ?? 0);
  if (needed <= 0) return;

  // Feed recent angles back in so the planner does not restate last week's post.
  const recent = await db(env).all<{ hook: string }>(
    `SELECT hook FROM posts
      WHERE channel_id = ? AND hook != ''
      ORDER BY created_at DESC LIMIT 20`,
    channel.id,
  );

  const { data, result } = await generateJson<CalendarResponse>(env, {
    stableSystem: OPERATOR_SYSTEM_REF,
    creatorSystem: strategySystem(strategy, pillars),
    userPrompt: calendarPrompt({
      platform: channel.platform,
      postsNeeded: needed,
      horizonDays: HORIZON_DAYS,
      pillars,
      recentAngles: recent.map((r) => r.hook),
    }),
    schema: CALENDAR_SCHEMA as unknown as Record<string, unknown>,
    model: env.STRATEGY_MODEL,
    effort: 'high',
  });

  await recordUsage(env, account.id, result.usage);

  if (result.refused || !data) {
    await audit(env, {
      accountId: account.id,
      actor: 'system:strategy',
      action: 'plan.refused',
      entityType: 'channel',
      entityId: channel.id,
      detail: { category: result.refusalCategory },
    });
    return;
  }

  const byName = new Map(pillars.map((p) => [p.name.toLowerCase(), p] as const));
  const fallbackPillar = pillars[0]!;
  let created = 0;

  for (const slot of data.slots.slice(0, needed)) {
    const pillar = byName.get(slot.pillar_name.toLowerCase()) ?? fallbackPillar;
    const when = slotTime(slot.day_offset, slot.hour_utc);
    // Past-dated slots would publish the instant they were created, which is not
    // what "scheduled" means to a creator reviewing next week's calendar.
    if (when.getTime() < Date.now()) continue;

    const slotId = newId('slot');
    const now = nowIso();
    const res = await db(env).run(
      `INSERT OR IGNORE INTO slots
         (id, account_id, channel_id, pillar_id, scheduled_for, status, created_at, updated_at)
       VALUES (?, ?, ?, ?, ?, 'planned', ?, ?)`,
      slotId,
      account.id,
      channel.id,
      pillar.id,
      when.toISOString(),
      now,
      now,
    );
    // A zero-change insert means this channel already has a slot at that exact
    // time. Skipping is correct: the calendar is already occupied.
    if (res.meta.changes === 0) continue;

    created++;
    await enqueue(
      env,
      'content.draft',
      { slotId, angle: slot.angle },
      {
        accountId: account.id,
        // Draft a day before publish so there is a review window.
        runAfter: new Date(Math.max(Date.now(), when.getTime() - 86_400_000)),
        idempotencyKey: `draft:${slotId}`,
      },
    );
  }

  await audit(env, {
    accountId: account.id,
    actor: 'system:strategy',
    action: 'plan.generated',
    entityType: 'channel',
    entityId: channel.id,
    detail: { requested: needed, created, model: result.model },
  });
}

function slotTime(dayOffset: number, hourUtc: number): Date {
  const d = new Date();
  d.setUTCDate(d.getUTCDate() + clamp(dayOffset, 0, HORIZON_DAYS));
  d.setUTCHours(clamp(hourUtc, 0, 23), 0, 0, 0);
  return d;
}

function clamp(n: number, lo: number, hi: number): number {
  return Math.min(hi, Math.max(lo, Math.round(n)));
}
