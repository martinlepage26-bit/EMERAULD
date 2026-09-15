import type { Env } from '../env';

/**
 * Envelope encryption for secrets held in D1.
 *
 * Channel access tokens are the highest-value data in the system: one of them
 * lets the holder post as the creator. D1 rows are readable by anything with
 * database access (a console session, a leaked backup, an injection bug in an
 * unrelated query), so the tokens are encrypted with a key that lives only in
 * the Worker's secret store and never in the database.
 *
 * AES-GCM with a random 96-bit IV per value. The IV is stored alongside the
 * ciphertext, which is safe and standard: GCM requires the IV be unique per
 * encryption under a given key, not secret.
 */

const VERSION = 'v1';
const IV_BYTES = 12;

let cachedKey: CryptoKey | null = null;
let cachedKeySource: string | null = null;

async function importKey(env: Env): Promise<CryptoKey> {
  const secret = env.TOKEN_ENCRYPTION_KEY;
  if (!secret || secret.length < 32) {
    throw new Error(
      'TOKEN_ENCRYPTION_KEY must be set to at least 32 characters before channel tokens can be stored',
    );
  }

  // Within one isolate the key material never changes, so importing once saves
  // a derivation on every publish.
  if (cachedKey && cachedKeySource === secret) return cachedKey;

  // SHA-256 the secret to get exactly 256 bits regardless of how the operator
  // generated it. This is a key-derivation convenience, not a KDF against a
  // low-entropy password: the secret is expected to be random.
  const material = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(secret));
  const key = await crypto.subtle.importKey('raw', material, { name: 'AES-GCM' }, false, [
    'encrypt',
    'decrypt',
  ]);

  cachedKey = key;
  cachedKeySource = secret;
  return key;
}

function toBase64(bytes: Uint8Array): string {
  let binary = '';
  for (const b of bytes) binary += String.fromCharCode(b);
  return btoa(binary);
}

function fromBase64(value: string): Uint8Array {
  const binary = atob(value);
  const out = new Uint8Array(binary.length);
  for (let i = 0; i < binary.length; i++) out[i] = binary.charCodeAt(i);
  return out;
}

/** Returns `v1:<iv>:<ciphertext>`, both base64. */
export async function encryptSecret(env: Env, plaintext: string): Promise<string> {
  const key = await importKey(env);
  const iv = crypto.getRandomValues(new Uint8Array(IV_BYTES));
  const ciphertext = await crypto.subtle.encrypt(
    { name: 'AES-GCM', iv },
    key,
    new TextEncoder().encode(plaintext),
  );
  return `${VERSION}:${toBase64(iv)}:${toBase64(new Uint8Array(ciphertext))}`;
}

export function isEncrypted(value: string): boolean {
  return value.startsWith(`${VERSION}:`);
}

/**
 * Decrypts a stored secret.
 *
 * A value without the version prefix is returned unchanged. That path exists so
 * a database written before encryption was added keeps working rather than
 * silently publishing with a garbage token; `channelNeedsReencryption` flags
 * those so they can be migrated on next write.
 */
export async function decryptSecret(env: Env, stored: string): Promise<string> {
  if (!isEncrypted(stored)) return stored;

  const parts = stored.split(':');
  if (parts.length !== 3) {
    throw new Error('Stored secret is malformed: expected v1:<iv>:<ciphertext>');
  }
  const [, ivB64, dataB64] = parts as [string, string, string];

  const key = await importKey(env);
  try {
    const plaintext = await crypto.subtle.decrypt(
      { name: 'AES-GCM', iv: fromBase64(ivB64) },
      key,
      fromBase64(dataB64),
    );
    return new TextDecoder().decode(plaintext);
  } catch {
    // GCM authentication failure means either the wrong key or a tampered row.
    // Both are operator-visible problems, so fail loudly rather than returning
    // an empty token that would surface as a confusing platform 401.
    throw new Error(
      'Could not decrypt a stored secret. TOKEN_ENCRYPTION_KEY may have changed since it was written.',
    );
  }
}

/** True when a stored value predates encryption and should be rewritten. */
export function needsReencryption(stored: string | null): boolean {
  return Boolean(stored) && !isEncrypted(stored as string);
}
