import { isDryRun, type Env } from '../env';
import { SimulatedAdapter } from './simulated';
import { XAdapter } from './x';
import { LinkedInAdapter } from './linkedin';
import type { PlatformAdapter } from './types';

export const SUPPORTED_PLATFORMS = ['x', 'linkedin', 'instagram', 'threads'] as const;
export type Platform = (typeof SUPPORTED_PLATFORMS)[number];

const LIVE: Partial<Record<Platform, () => PlatformAdapter>> = {
  x: () => new XAdapter(),
  linkedin: () => new LinkedInAdapter(),
};

export function isSupportedPlatform(value: string): value is Platform {
  return (SUPPORTED_PLATFORMS as readonly string[]).includes(value);
}

/**
 * Resolves the adapter for a platform.
 *
 * Instagram and Threads have no live adapter yet, so they fall through to the
 * simulator even outside dry-run. That is deliberate: a creator on those plans
 * sees planning and drafting work while publishing stays visibly simulated,
 * rather than the system claiming a post went out when nothing did.
 */
export function adapterFor(env: Env, platform: string): PlatformAdapter {
  if (isDryRun(env)) return new SimulatedAdapter(platform);
  const build = isSupportedPlatform(platform) ? LIVE[platform] : undefined;
  return build ? build() : new SimulatedAdapter(platform);
}

export function hasLiveAdapter(platform: string): boolean {
  return isSupportedPlatform(platform) && LIVE[platform] !== undefined;
}
