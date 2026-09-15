import type { Context, Next } from 'hono';
import type { AppBindings, Env } from '../env';
import { unauthorized } from './errors';
import { db } from './db';
import { newId, nowIso, sha256Hex } from './ids';

const KEY_PREFIX = 'kai_sk_';

export interface IssuedKey {
  id: string;
  plaintext: string;
}

/**
 * Mints an API key. The plaintext is returned exactly once, at creation; only a
 * SHA-256 digest is persisted, so a database read cannot recover a working key.
 */
export async function issueApiKey(
  env: Env,
  accountId: string,
  name: string,
): Promise<IssuedKey> {
  const bytes = new Uint8Array(24);
  crypto.getRandomValues(bytes);
  const secret = [...bytes].map((b) => b.toString(16).padStart(2, '0')).join('');
  const plaintext = `${KEY_PREFIX}${secret}`;
  const id = newId('key');

  await db(env).run(
    `INSERT INTO api_keys (id, account_id, name, key_hash, prefix, created_at)
     VALUES (?, ?, ?, ?, ?, ?)`,
    id,
    accountId,
    name,
    await sha256Hex(plaintext),
    plaintext.slice(0, KEY_PREFIX.length + 6),
    nowIso(),
  );

  return { id, plaintext };
}

export async function resolveApiKey(
  env: Env,
  presented: string,
): Promise<{ accountId: string; keyId: string } | null> {
  if (!presented.startsWith(KEY_PREFIX)) return null;

  const row = await db(env).first<{ id: string; account_id: string; revoked_at: string | null }>(
    `SELECT id, account_id, revoked_at FROM api_keys WHERE key_hash = ?`,
    await sha256Hex(presented),
  );
  if (!row || row.revoked_at) return null;

  // Best-effort last-used stamp; a failure here should not block the request.
  await db(env)
    .run(`UPDATE api_keys SET last_used_at = ? WHERE id = ?`, nowIso(), row.id)
    .catch(() => undefined);

  return { accountId: row.account_id, keyId: row.id };
}

export async function requireAuth(c: Context<AppBindings>, next: Next): Promise<Response | void> {
  const header = c.req.header('authorization') ?? '';
  const token = header.startsWith('Bearer ') ? header.slice(7).trim() : '';
  if (!token) throw unauthorized('Provide an API key as `Authorization: Bearer kai_sk_...`');

  const resolved = await resolveApiKey(c.env, token);
  if (!resolved) throw unauthorized('API key is unknown or revoked');

  c.set('ctx', resolved);
  await next();
}
