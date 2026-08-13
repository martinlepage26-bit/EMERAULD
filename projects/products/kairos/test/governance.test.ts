import { describe, it, expect, afterEach } from 'vitest';
import { createHarness, seedAccount, type TestHarness } from './helpers/d1';
import { canAutoReply, canPublish, controlsFor } from '../src/lib/governance';
import { db, meter } from '../src/lib/db';
import type { AccountRecord } from '../src/lib/types';

let harness: TestHarness | null = null;

afterEach(() => {
  harness?.close();
  harness = null;
});

async function accountFor(h: TestHarness, id = 'acct_test'): Promise<AccountRecord> {
  const row = await db(h.env).first<AccountRecord>(`SELECT * FROM accounts WHERE id = ?`, id);
  if (!row) throw new Error('seed failed');
  return row;
}

function setup(opts: Parameters<typeof seedAccount>[1] = {}): TestHarness {
  harness = createHarness();
  seedAccount(harness, opts);
  return harness;
}

describe('publishing gate', () => {
  it('refuses when autopilot has never been switched on', async () => {
    const h = setup({ autopilotPublishing: false });
    const gate = await canPublish(h.env, await accountFor(h));

    // An account that has made no choice has not consented to unattended posting.
    expect(gate.allowed).toBe(false);
    expect(gate.reason).toContain('autopilot is off');
  });

  it('allows publishing once autopilot is on', async () => {
    const h = setup({ autopilotPublishing: true });
    expect((await canPublish(h.env, await accountFor(h))).allowed).toBe(true);
  });

  it('honours a pause window and resumes after it lapses', async () => {
    const h = setup({ autopilotPublishing: true });

    h.sqlite
      .prepare(`UPDATE automation_controls SET paused_until = ?`)
      .run(new Date(Date.now() + 3600_000).toISOString());
    expect((await canPublish(h.env, await accountFor(h))).allowed).toBe(false);

    h.sqlite
      .prepare(`UPDATE automation_controls SET paused_until = ?`)
      .run(new Date(Date.now() - 1000).toISOString());
    expect((await canPublish(h.env, await accountFor(h))).allowed).toBe(true);
  });

  it('enforces the daily publish cap', async () => {
    const h = setup({ autopilotPublishing: true, dailyPublishCap: 2 });
    const now = new Date().toISOString();

    h.sqlite
      .prepare(
        `INSERT INTO channels (id, account_id, platform, handle, status, posts_per_week, connected_at, updated_at)
         VALUES ('chan_1', 'acct_test', 'x', 'creator', 'connected', 5, ?, ?)`,
      )
      .run(now, now);
    h.sqlite
      .prepare(
        `INSERT INTO pillars (id, account_id, name, description, weight, active, created_at, updated_at)
         VALUES ('pil_1', 'acct_test', 'Craft', '', 1.0, 1, ?, ?)`,
      )
      .run(now, now);

    for (let i = 0; i < 2; i++) {
      // Distinct times per slot: a channel cannot hold two slots at one instant.
      const scheduledFor = new Date(Date.now() - (i + 1) * 3600_000).toISOString();
      h.sqlite
        .prepare(
          `INSERT INTO slots (id, account_id, channel_id, pillar_id, scheduled_for, status, created_at, updated_at)
           VALUES (?, 'acct_test', 'chan_1', 'pil_1', ?, 'published', ?, ?)`,
        )
        .run(`slot_${i}`, scheduledFor, now, now);
      h.sqlite
        .prepare(
          `INSERT INTO posts (id, account_id, slot_id, channel_id, pillar_id, variant, hook, body,
                              status, published_at, created_at, updated_at)
           VALUES (?, 'acct_test', ?, 'chan_1', 'pil_1', 1, 'h', 'b', 'published', ?, ?, ?)`,
        )
        .run(`post_${i}`, `slot_${i}`, now, now, now);
    }

    const gate = await canPublish(h.env, await accountFor(h));
    expect(gate.allowed).toBe(false);
    expect(gate.reason).toContain('Daily publish cap');
  });

  it('stops publishing for a canceled subscription', async () => {
    const h = setup({ autopilotPublishing: true, status: 'canceled' });
    expect((await canPublish(h.env, await accountFor(h))).allowed).toBe(false);
  });

  it('enforces the monthly plan allowance', async () => {
    const h = setup({ autopilotPublishing: true, plan: 'solo' });
    // Solo allows 60 posts per month.
    await meter(h.env, 'acct_test', 'posts_published', 60);

    const gate = await canPublish(h.env, await accountFor(h));
    expect(gate.allowed).toBe(false);
    expect(gate.reason).toContain('Monthly post allowance');
  });
});

describe('auto-reply gate', () => {
  async function withRule(h: TestHarness, intent: string, action: string, min = 0.85) {
    h.sqlite
      .prepare(
        `INSERT INTO reply_rules (id, account_id, intent, action, min_confidence, active, created_at)
         VALUES (?, 'acct_test', ?, ?, ?, 1, ?)`,
      )
      .run(`rule_${intent}`, intent, action, min, new Date().toISOString());
  }

  it('never auto-sends into a lead, collab, or hostile thread', async () => {
    const h = setup({ autopilotReplies: true });
    // Even with an explicit auto_send rule and maximum confidence.
    await withRule(h, 'lead', 'auto_send', 0);
    await withRule(h, 'hostile', 'auto_send', 0);

    const account = await accountFor(h);
    expect((await canAutoReply(h.env, account, 'lead', 1)).allowed).toBe(false);
    expect((await canAutoReply(h.env, account, 'hostile', 1)).allowed).toBe(false);
    expect((await canAutoReply(h.env, account, 'collab', 1)).allowed).toBe(false);
  });

  it('holds a reply that falls below the confidence floor', async () => {
    const h = setup({ autopilotReplies: true });
    await withRule(h, 'question', 'auto_send', 0.9);

    const account = await accountFor(h);
    expect((await canAutoReply(h.env, account, 'question', 0.7)).allowed).toBe(false);
    expect((await canAutoReply(h.env, account, 'question', 0.95)).allowed).toBe(true);
  });

  it('refuses an intent with no configured rule', async () => {
    const h = setup({ autopilotReplies: true });
    const gate = await canAutoReply(h.env, await accountFor(h), 'support', 1);

    // Absence of a rule is not permission.
    expect(gate.allowed).toBe(false);
    expect(gate.reason).toContain('No auto-reply rule');
  });

  it('respects a queue_for_review rule', async () => {
    const h = setup({ autopilotReplies: true });
    await withRule(h, 'praise', 'queue_for_review');

    expect((await canAutoReply(h.env, await accountFor(h), 'praise', 1)).allowed).toBe(false);
  });
});

describe('controls default', () => {
  it('defaults to autopilot off when no row exists', async () => {
    harness = createHarness();
    const controls = await controlsFor(harness.env, 'acct_missing');

    expect(controls.autopilot_publishing).toBe(0);
    expect(controls.autopilot_replies).toBe(0);
  });
});
