import type { Env } from '../env';

export interface RateLimitResult {
  allowed: boolean;
  remaining: number;
  resetSeconds: number;
}

/**
 * Fixed-window rate limit backed by Workers KV.
 *
 * Used on the unauthenticated endpoints, where there is no API key to attribute
 * abuse to. Signup in particular writes account rows and mints API keys, so an
 * unthrottled caller can fill the database and exhaust the referral-code space
 * for free.
 *
 * A fixed window lets a caller burst across a boundary (up to 2x the limit in
 * one instant). That is an accepted trade: the alternative needs either a
 * Durable Object or a read-modify-write per request, and the threshold here is
 * set low enough that a boundary burst is still harmless. KV's eventual
 * consistency means the count can also lag briefly across regions, which is
 * tolerable for abuse control and would not be for billing.
 */
export async function rateLimit(
  env: Env,
  key: string,
  limit: number,
  windowSeconds: number,
): Promise<RateLimitResult> {
  const window = Math.floor(Date.now() / 1000 / windowSeconds);
  const cacheKey = `rl:${key}:${window}`;

  let count = 0;
  try {
    const existing = await env.CACHE.get(cacheKey);
    count = existing ? Number.parseInt(existing, 10) || 0 : 0;
  } catch {
    // A KV read failure must not take the endpoint down. Failing open is the
    // right call for a throttle on a low-value endpoint; it would be the wrong
    // call for an authorization check.
    return { allowed: true, remaining: limit, resetSeconds: windowSeconds };
  }

  if (count >= limit) {
    const elapsed = Math.floor(Date.now() / 1000) % windowSeconds;
    return { allowed: false, remaining: 0, resetSeconds: windowSeconds - elapsed };
  }

  try {
    await env.CACHE.put(cacheKey, String(count + 1), { expirationTtl: windowSeconds + 60 });
  } catch {
    // Same reasoning: a write failure loses one increment, not the request.
  }

  return { allowed: true, remaining: limit - count - 1, resetSeconds: windowSeconds };
}

/**
 * Best-effort client identity for throttling. Cloudflare sets CF-Connecting-IP
 * on every request that reaches a Worker and it cannot be spoofed by the
 * client, unlike X-Forwarded-For.
 */
export function clientKey(req: Request): string {
  return req.headers.get('cf-connecting-ip') ?? 'unknown';
}
