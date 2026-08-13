import { describe, it, expect } from 'vitest';
import { scoreOf } from '../src/engines/growth';
import { EMPTY_METRICS } from '../src/adapters/types';
import { verifyStripeSignature } from '../src/engines/billing';
import { strategySystem, platformNote } from '../src/ai/prompts';
import type { Env } from '../src/env';
import type { PillarRecord, StrategyRecord } from '../src/lib/types';

describe('engagement scoring', () => {
  it('normalizes by reach so small and large accounts compare', () => {
    const small = scoreOf({ ...EMPTY_METRICS, impressions: 1_000, likes: 20 });
    const large = scoreOf({ ...EMPTY_METRICS, impressions: 100_000, likes: 2_000 });

    // Same 2% like rate at two orders of magnitude of reach.
    expect(small).toBeCloseTo(large, 5);
  });

  it('values a follow far above a like', () => {
    const liked = scoreOf({ ...EMPTY_METRICS, impressions: 1_000, likes: 10 });
    const followed = scoreOf({ ...EMPTY_METRICS, impressions: 1_000, follows: 10 });

    // A follow compounds into future distribution; a like does not.
    expect(followed).toBeGreaterThan(liked * 10);
  });

  it('falls back to raw value when a platform reports no impressions', () => {
    // LinkedIn's social-actions endpoint returns no impression count, and
    // dividing by zero would score every LinkedIn post at zero forever.
    const score = scoreOf({ ...EMPTY_METRICS, impressions: 0, likes: 5, comments: 2 });
    expect(score).toBe(5 * 1 + 2 * 4);
  });

  it('scores an empty snapshot at zero rather than NaN', () => {
    expect(scoreOf(EMPTY_METRICS)).toBe(0);
  });
});

describe('stripe signature verification', () => {
  const env = { STRIPE_WEBHOOK_SECRET: 'whsec_test_secret' } as Env;

  async function sign(payload: string, timestamp: number, secret: string): Promise<string> {
    const key = await crypto.subtle.importKey(
      'raw',
      new TextEncoder().encode(secret),
      { name: 'HMAC', hash: 'SHA-256' },
      false,
      ['sign'],
    );
    const mac = await crypto.subtle.sign(
      'HMAC',
      key,
      new TextEncoder().encode(`${timestamp}.${payload}`),
    );
    const hex = [...new Uint8Array(mac)].map((b) => b.toString(16).padStart(2, '0')).join('');
    return `t=${timestamp},v1=${hex}`;
  }

  const payload = JSON.stringify({ id: 'evt_1', type: 'checkout.session.completed' });

  it('accepts a correctly signed recent payload', async () => {
    const now = Math.floor(Date.now() / 1000);
    const header = await sign(payload, now, 'whsec_test_secret');
    expect(await verifyStripeSignature(env, payload, header)).toBe(true);
  });

  it('rejects a payload signed with the wrong secret', async () => {
    const now = Math.floor(Date.now() / 1000);
    const header = await sign(payload, now, 'whsec_attacker');
    // Without this check, anyone who finds the endpoint can grant themselves a plan.
    expect(await verifyStripeSignature(env, payload, header)).toBe(false);
  });

  it('rejects a replay of an old but validly signed payload', async () => {
    const old = Math.floor(Date.now() / 1000) - 600;
    const header = await sign(payload, old, 'whsec_test_secret');
    expect(await verifyStripeSignature(env, payload, header)).toBe(false);
  });

  it('rejects a tampered payload', async () => {
    const now = Math.floor(Date.now() / 1000);
    const header = await sign(payload, now, 'whsec_test_secret');
    expect(await verifyStripeSignature(env, `${payload} `, header)).toBe(false);
  });

  it('rejects a malformed header', async () => {
    expect(await verifyStripeSignature(env, payload, 'garbage')).toBe(false);
    expect(await verifyStripeSignature(env, payload, '')).toBe(false);
  });
});

describe('prompt assembly', () => {
  const strategy: StrategyRecord = {
    id: 'strat_1',
    account_id: 'acct_1',
    positioning: 'Fractional CFO for agencies',
    audience: 'Agency owners doing 1M to 5M a year',
    tone: 'Blunt, numerate, no motivational filler',
    proof_points: JSON.stringify(['Took 40 agencies through a pricing rebuild']),
    banned_phrases: JSON.stringify(['game-changer', 'unlock your potential']),
    cta_library: JSON.stringify(['Reply CFO and I will send the model']),
  };

  const pillars: PillarRecord[] = [
    { id: 'p1', account_id: 'acct_1', name: 'Pricing', description: 'Rates', weight: 1.4, active: 1 },
  ];

  it('carries banned phrases and proof points into the cached prefix', () => {
    const prompt = strategySystem(strategy, pillars);

    expect(prompt).toContain('game-changer');
    expect(prompt).toContain('Took 40 agencies');
    expect(prompt).toContain('Pricing');
  });

  it('survives malformed JSON in the strategy columns', () => {
    // A truncated write should degrade the prompt, not throw mid-generation.
    const broken = { ...strategy, banned_phrases: 'not json', proof_points: '{}' };
    expect(() => strategySystem(broken, pillars)).not.toThrow();
  });

  it('gives each platform its own length guidance', () => {
    expect(platformNote('x')).toContain('280');
    expect(platformNote('linkedin')).toContain('see more');
    expect(platformNote('unknown-platform')).toContain('200 words');
  });
});
