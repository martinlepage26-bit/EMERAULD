const ALPHABET = '0123456789abcdefghjkmnpqrstvwxyz'; // Crockford base32, no ambiguous glyphs

/**
 * Prefixed, sortable-ish identifier. The random suffix is drawn from the Workers
 * CSPRNG, so ids are safe to expose in URLs.
 */
export function newId(prefix: string): string {
  const bytes = new Uint8Array(16);
  crypto.getRandomValues(bytes);
  let out = '';
  for (const b of bytes) out += ALPHABET[b % ALPHABET.length];
  return `${prefix}_${out}`;
}

export function nowIso(): string {
  return new Date().toISOString();
}

/** Referral codes are read aloud and typed by hand, so keep them short. */
export function newReferralCode(): string {
  const bytes = new Uint8Array(6);
  crypto.getRandomValues(bytes);
  let out = '';
  for (const b of bytes) out += ALPHABET[b % ALPHABET.length];
  return out.toUpperCase();
}

export async function sha256Hex(input: string): Promise<string> {
  const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(input));
  return [...new Uint8Array(digest)].map((b) => b.toString(16).padStart(2, '0')).join('');
}
