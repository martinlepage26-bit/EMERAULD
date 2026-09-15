export interface AccountRecord {
  id: string;
  email: string;
  display_name: string;
  timezone: string;
  plan: PlanId;
  status: 'active' | 'past_due' | 'paused' | 'canceled';
  stripe_customer_id: string | null;
  stripe_subscription_id: string | null;
  trial_ends_at: string | null;
  referral_code: string;
  referred_by: string | null;
  created_at: string;
  updated_at: string;
}

export interface StrategyRecord {
  id: string;
  account_id: string;
  positioning: string;
  audience: string;
  tone: string;
  proof_points: string;
  banned_phrases: string;
  cta_library: string;
}

export interface PillarRecord {
  id: string;
  account_id: string;
  name: string;
  description: string;
  weight: number;
  active: number;
}

export interface ChannelRecord {
  id: string;
  account_id: string;
  platform: string;
  handle: string;
  external_id: string | null;
  access_token: string | null;
  status: 'connected' | 'expired' | 'revoked' | 'error';
  posts_per_week: number;
}

export interface SlotRecord {
  id: string;
  account_id: string;
  channel_id: string;
  pillar_id: string;
  scheduled_for: string;
  status:
    | 'planned'
    | 'drafting'
    | 'ready'
    | 'approved'
    | 'publishing'
    | 'published'
    | 'failed'
    | 'skipped';
}

export interface PostRecord {
  id: string;
  account_id: string;
  slot_id: string;
  channel_id: string;
  pillar_id: string;
  variant: number;
  hook: string;
  body: string;
  media_keys: string;
  status: 'draft' | 'approved' | 'publishing' | 'published' | 'failed' | 'rejected';
  approved_at: string | null;
  approved_by: string | null;
  published_at: string | null;
  external_post_id: string | null;
  external_url: string | null;
  recycled_from: string | null;
}

export interface ConversationRecord {
  id: string;
  account_id: string;
  channel_id: string;
  platform_thread_id: string;
  author_handle: string;
  intent: string;
  priority: number;
  status: 'open' | 'awaiting_review' | 'answered' | 'ignored';
  last_message_at: string;
}

export interface AutomationControls {
  account_id: string;
  autopilot_publishing: number;
  autopilot_replies: number;
  paused_until: string | null;
  daily_publish_cap: number;
  daily_reply_cap: number;
  updated_at: string;
}

export type PlanId = 'trial' | 'solo' | 'pro' | 'studio' | 'agency';

export interface PlanDefinition {
  id: PlanId;
  name: string;
  monthlyPriceUsd: number;
  channels: number;
  postsPerMonth: number;
  repliesPerMonth: number;
  seats: number;
}

/**
 * Plan limits are enforced in the engines, not just displayed.
 *
 * Reply allowances are the binding constraint on margin: a reply costs roughly
 * three fifths of what a post costs to produce, and heavy accounts send far more
 * replies than posts. Each allowance below is set so that an account consuming
 * its full quota still leaves at least 70% gross margin. The derivation is in
 * docs/UNIT-ECONOMICS.md, and changing a number here without re-running that
 * model is how a plan quietly stops being profitable.
 */
export const PLANS: Record<PlanId, PlanDefinition> = {
  trial: {
    id: 'trial',
    name: 'Trial',
    monthlyPriceUsd: 0,
    channels: 2,
    postsPerMonth: 20,
    repliesPerMonth: 50,
    seats: 1,
  },
  solo: {
    id: 'solo',
    name: 'Solo',
    monthlyPriceUsd: 49,
    channels: 2,
    postsPerMonth: 60,
    repliesPerMonth: 200,
    seats: 1,
  },
  pro: {
    id: 'pro',
    name: 'Pro',
    monthlyPriceUsd: 149,
    channels: 5,
    postsPerMonth: 200,
    repliesPerMonth: 800,
    seats: 2,
  },
  studio: {
    id: 'studio',
    name: 'Studio',
    monthlyPriceUsd: 399,
    channels: 15,
    postsPerMonth: 700,
    repliesPerMonth: 2000,
    seats: 5,
  },
  agency: {
    id: 'agency',
    name: 'Agency',
    monthlyPriceUsd: 999,
    channels: 50,
    postsPerMonth: 2000,
    repliesPerMonth: 5000,
    seats: 20,
  },
};
