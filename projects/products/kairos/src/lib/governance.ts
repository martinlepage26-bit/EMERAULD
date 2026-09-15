import type { Env } from '../env';
import { db, usageFor } from './db';
import { PLANS, type AccountRecord, type AutomationControls, type PlanId } from './types';

export interface GateResult {
  allowed: boolean;
  reason?: string;
}

const ALLOW: GateResult = { allowed: true };

export async function controlsFor(env: Env, accountId: string): Promise<AutomationControls> {
  const row = await db(env).first<AutomationControls>(
    `SELECT * FROM automation_controls WHERE account_id = ?`,
    accountId,
  );
  if (row) return row;

  // Absent controls mean autopilot off. A creator who has never made a choice
  // has not consented to unattended publishing.
  return {
    account_id: accountId,
    autopilot_publishing: 0,
    autopilot_replies: 0,
    paused_until: null,
    daily_publish_cap: 10,
    daily_reply_cap: 25,
    updated_at: new Date().toISOString(),
  };
}

async function countToday(env: Env, accountId: string, sql: string): Promise<number> {
  const since = new Date(Date.now() - 24 * 3600_000).toISOString();
  const row = await db(env).first<{ n: number }>(sql, accountId, since);
  return row?.n ?? 0;
}

/**
 * The single gate every publish passes through. It answers one question: is this
 * account, right now, permitted to put something in front of an audience without
 * a human in the loop?
 */
export async function canPublish(env: Env, account: AccountRecord): Promise<GateResult> {
  if (account.status === 'canceled') return deny('Subscription is canceled');
  if (account.status === 'paused') return deny('Account is paused');

  const controls = await controlsFor(env, account.id);
  if (!controls.autopilot_publishing) return deny('Publishing autopilot is off for this account');
  if (controls.paused_until && controls.paused_until > new Date().toISOString()) {
    return deny(`Automation is paused until ${controls.paused_until}`);
  }

  const published = await countToday(
    env,
    account.id,
    `SELECT COUNT(*) AS n FROM posts WHERE account_id = ? AND published_at >= ?`,
  );
  if (published >= controls.daily_publish_cap) {
    return deny(`Daily publish cap reached (${controls.daily_publish_cap})`);
  }

  const plan = planFor(account.plan);
  const monthly = await usageFor(env, account.id, 'posts_published');
  if (monthly >= plan.postsPerMonth) {
    return deny(`Monthly post allowance used (${plan.postsPerMonth} on ${plan.name})`);
  }

  return ALLOW;
}

/**
 * Replies carry more risk than posts: they are addressed to a person, and a bad
 * one reads as the creator personally saying something careless. The confidence
 * floor is therefore checked here rather than left to the drafting model.
 */
export async function canAutoReply(
  env: Env,
  account: AccountRecord,
  intent: string,
  confidence: number,
): Promise<GateResult> {
  if (account.status === 'canceled' || account.status === 'paused') {
    return deny(`Account status is ${account.status}`);
  }

  const controls = await controlsFor(env, account.id);
  if (!controls.autopilot_replies) return deny('Reply autopilot is off for this account');
  if (controls.paused_until && controls.paused_until > new Date().toISOString()) {
    return deny(`Automation is paused until ${controls.paused_until}`);
  }

  // Never send unattended into a conversation where being wrong is expensive.
  if (intent === 'hostile' || intent === 'lead' || intent === 'collab') {
    return deny(`Intent "${intent}" always goes to the creator`);
  }

  const rule = await db(env).first<{ action: string; min_confidence: number }>(
    `SELECT action, min_confidence FROM reply_rules
      WHERE account_id = ? AND intent = ? AND active = 1`,
    account.id,
    intent,
  );
  if (!rule) return deny(`No auto-reply rule configured for intent "${intent}"`);
  if (rule.action !== 'auto_send') return deny(`Rule for "${intent}" is ${rule.action}`);
  if (confidence < rule.min_confidence) {
    return deny(`Confidence ${confidence.toFixed(2)} is below the ${rule.min_confidence} floor`);
  }

  const sent = await countToday(
    env,
    account.id,
    `SELECT COUNT(*) AS n FROM reply_drafts WHERE account_id = ? AND sent_at >= ?`,
  );
  if (sent >= controls.daily_reply_cap) {
    return deny(`Daily reply cap reached (${controls.daily_reply_cap})`);
  }

  const plan = planFor(account.plan);
  const monthly = await usageFor(env, account.id, 'replies_sent');
  if (monthly >= plan.repliesPerMonth) {
    return deny(`Monthly reply allowance used (${plan.repliesPerMonth} on ${plan.name})`);
  }

  return ALLOW;
}

/** Generation is metered too, so a runaway loop cannot burn unbounded API spend. */
export async function canGenerate(env: Env, account: AccountRecord): Promise<GateResult> {
  if (account.status === 'canceled') return deny('Subscription is canceled');
  const plan = planFor(account.plan);
  const drafted = await usageFor(env, account.id, 'drafts_generated');
  // Drafting headroom is 3x the publish allowance: variants and rejected drafts
  // are normal, unbounded regeneration is not.
  if (drafted >= plan.postsPerMonth * 3) {
    return deny('Monthly drafting allowance used');
  }
  return ALLOW;
}

export function planFor(id: PlanId): (typeof PLANS)[PlanId] {
  return PLANS[id] ?? PLANS.trial;
}

function deny(reason: string): GateResult {
  return { allowed: false, reason };
}
