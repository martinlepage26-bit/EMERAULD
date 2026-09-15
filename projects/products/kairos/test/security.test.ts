import { describe, it, expect, afterEach } from 'vitest';
import { createHarness, type TestHarness } from './helpers/d1';
import { encryptSecret, decryptSecret, isEncrypted, needsReencryption } from '../src/lib/crypto';
import { channelToken } from '../src/lib/channels';
import { rateLimit } from '../src/lib/rate-limit';
import type { Env } from '../src/env';
import type { ChannelRecord } from '../src/lib/types';

let harness: TestHarness | null = null;

afterEach(() => {
  harness?.close();
  harness = null;
});

function setup(overrides: Partial<Env> = {}): TestHarness {
  harness = createHarness(overrides);
  return harness;
}

describe('secret encryption', () => {
  it('round-trips a token', async () => {
    const h = setup();
    const token = 'ya29.a0AfB_byC-real-looking-oauth-token';

    const stored = await encryptSecret(h.env, token);
    expect(await decryptSecret(h.env, stored)).toBe(token);
  });

  it('never stores the plaintext anywhere in the ciphertext', async () => {
    const h = setup();
    const token = 'super-secret-creator-token';

    const stored = await encryptSecret(h.env, token);
    // The whole point: a database dump must not contain the token.
    expect(stored).not.toContain(token);
    expect(stored.startsWith('v1:')).toBe(true);
  });

  it('produces a different ciphertext each time for the same input', async () => {
    const h = setup();

    const a = await encryptSecret(h.env, 'same-token');
    const b = await encryptSecret(h.env, 'same-token');

    // A random IV per encryption. Identical ciphertexts would leak that two
    // creators connected the same account.
    expect(a).not.toBe(b);
    expect(await decryptSecret(h.env, a)).toBe(await decryptSecret(h.env, b));
  });

  it('refuses to decrypt under a different key rather than returning garbage', async () => {
    const h = setup();
    const stored = await encryptSecret(h.env, 'token');

    const other = createHarness({ TOKEN_ENCRYPTION_KEY: 'a-completely-different-key-32-chars-x' });
    try {
      // GCM authentication catches this. Silently returning a bad token would
      // surface as a confusing platform 401 instead of a key problem.
      await expect(decryptSecret(other.env, stored)).rejects.toThrow(/could not decrypt/i);
    } finally {
      other.close();
    }
  });

  it('detects a tampered ciphertext', async () => {
    const h = setup();
    const stored = await encryptSecret(h.env, 'token');

    const parts = stored.split(':');
    const flipped = `${parts[0]}:${parts[1]}:${'A'}${(parts[2] as string).slice(1)}`;
    await expect(decryptSecret(h.env, flipped)).rejects.toThrow();
  });

  it('rejects a key that is too short to be random', async () => {
    const h = setup({ TOKEN_ENCRYPTION_KEY: 'short' });
    await expect(encryptSecret(h.env, 'token')).rejects.toThrow(/at least 32/i);
  });

  it('passes through a pre-encryption plaintext value and flags it for rewrite', async () => {
    const h = setup();
    // A row written before encryption existed should keep working rather than
    // handing AES ciphertext to a platform API.
    expect(await decryptSecret(h.env, 'legacy-plaintext-token')).toBe('legacy-plaintext-token');
    expect(isEncrypted('legacy-plaintext-token')).toBe(false);
    expect(needsReencryption('legacy-plaintext-token')).toBe(true);
    expect(needsReencryption(await encryptSecret(h.env, 'x'))).toBe(false);
    expect(needsReencryption(null)).toBe(false);
  });
});

describe('channelToken', () => {
  function channel(token: string | null): ChannelRecord {
    return {
      id: 'chan_1',
      account_id: 'acct_1',
      platform: 'x',
      handle: 'creator',
      external_id: null,
      access_token: token,
      status: 'connected',
      posts_per_week: 5,
    };
  }

  it('decrypts on the way out', async () => {
    const h = setup();
    const stored = await encryptSecret(h.env, 'the-real-token');

    expect(await channelToken(h.env, channel(stored))).toBe('the-real-token');
  });

  it('returns empty string for a channel with no token', async () => {
    const h = setup();
    expect(await channelToken(h.env, channel(null))).toBe('');
  });
});

describe('rate limiting', () => {
  it('allows up to the limit then refuses', async () => {
    const h = setup();

    for (let i = 0; i < 3; i++) {
      const res = await rateLimit(h.env, 'ip:1.2.3.4', 3, 3600);
      expect(res.allowed).toBe(true);
      expect(res.remaining).toBe(2 - i);
    }

    const blocked = await rateLimit(h.env, 'ip:1.2.3.4', 3, 3600);
    expect(blocked.allowed).toBe(false);
    expect(blocked.resetSeconds).toBeGreaterThan(0);
  });

  it('counts each caller separately', async () => {
    const h = setup();

    await rateLimit(h.env, 'ip:1.1.1.1', 1, 3600);
    expect((await rateLimit(h.env, 'ip:1.1.1.1', 1, 3600)).allowed).toBe(false);
    // One abusive address must not lock everyone else out.
    expect((await rateLimit(h.env, 'ip:2.2.2.2', 1, 3600)).allowed).toBe(true);
  });

  it('fails open when KV is unavailable', async () => {
    const h = setup({
      CACHE: {
        get: async () => {
          throw new Error('KV is down');
        },
        put: async () => undefined,
      } as unknown as KVNamespace,
    });

    // A throttle on a low-value endpoint should not take signup down with it.
    expect((await rateLimit(h.env, 'ip:9.9.9.9', 1, 3600)).allowed).toBe(true);
  });
});
