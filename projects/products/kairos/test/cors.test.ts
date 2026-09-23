import { describe, it, expect, afterEach } from 'vitest';
import worker from '../src/index';
import { createHarness, type TestHarness } from './helpers/d1';

/**
 * The dashboard is a separate app on its own origin, so every one of its calls
 * is cross-origin. Without these headers the browser blocks the response before
 * any application code sees it, which looks exactly like a rejected API key.
 */

let harness: TestHarness | null = null;

afterEach(() => {
  harness?.close();
  harness = null;
});

const ALLOWED = 'https://dash.test.invalid';

function setup(overrides = {}): TestHarness {
  harness = createHarness(overrides);
  return harness;
}

function preflight(origin: string): Request {
  return new Request('https://api.test.invalid/v1/me', {
    method: 'OPTIONS',
    headers: {
      origin,
      'access-control-request-method': 'GET',
      'access-control-request-headers': 'authorization',
    },
  });
}

describe('cross-origin access', () => {
  it('answers a preflight from an allowed origin without requiring auth', async () => {
    const h = setup();
    const res = await worker.fetch(preflight(ALLOWED), h.env);

    // A preflight carries no Authorization header by definition. If auth ran
    // first it would 401 here and the browser would never send the real call.
    expect(res.status).toBeLessThan(300);
    expect(res.headers.get('access-control-allow-origin')).toBe(ALLOWED);
  });

  it('allows the authorization header the API requires', async () => {
    const h = setup();
    const res = await worker.fetch(preflight(ALLOWED), h.env);

    expect(res.headers.get('access-control-allow-headers')?.toLowerCase()).toContain('authorization');
  });

  it('gives an unlisted origin no access-control headers', async () => {
    const h = setup();
    const res = await worker.fetch(preflight('https://attacker.test.invalid'), h.env);

    expect(res.headers.get('access-control-allow-origin')).toBeNull();
  });

  it('echoes the allowed origin on a real request, not a wildcard', async () => {
    const h = setup();
    const res = await worker.fetch(
      new Request('https://api.test.invalid/health', { headers: { origin: ALLOWED } }),
      h.env,
    );

    expect(res.status).toBe(200);
    expect(res.headers.get('access-control-allow-origin')).toBe(ALLOWED);
  });

  it('serves no origin at all when the allowlist is empty', async () => {
    const h = setup({ DASHBOARD_ORIGINS: '' });
    const res = await worker.fetch(preflight(ALLOWED), h.env);

    expect(res.headers.get('access-control-allow-origin')).toBeNull();
  });

  it('still refuses an unauthenticated non-preflight request', async () => {
    const h = setup();
    const res = await worker.fetch(
      new Request('https://api.test.invalid/v1/me', { headers: { origin: ALLOWED } }),
      h.env,
    );

    // CORS is not authentication: allowing the origin must not admit the call.
    expect(res.status).toBe(401);
  });
});
