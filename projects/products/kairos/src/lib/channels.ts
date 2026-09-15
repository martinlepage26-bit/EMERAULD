import type { Env } from '../env';
import { decryptSecret } from './crypto';
import type { ChannelRecord } from './types';

/**
 * The single read path for a channel's access token.
 *
 * Every engine goes through this rather than touching `channel.access_token`
 * directly, so there is exactly one place where a stored token becomes usable
 * plaintext. A direct field read would silently hand AES ciphertext to a
 * platform API and surface as a confusing 401.
 */
export async function channelToken(env: Env, channel: ChannelRecord): Promise<string> {
  if (!channel.access_token) return '';
  return decryptSecret(env, channel.access_token);
}
