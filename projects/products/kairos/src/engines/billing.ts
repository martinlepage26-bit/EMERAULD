import type { Env } from '../env';
import { audit, db } from '../lib/db';
import { nowIso } from '../lib/ids';
import { RetryableError, badRequest } from '../lib/errors';
import { PLANS, type AccountRecord, type PlanId } from '../lib/types';
import { enqueue, type Job } from '../queue/jobs';

const STRIPE_API = 'https://api.stripe.com/v1';

/** Maps a Stripe price lookup key back to a plan. Set these on the Stripe prices. */
const PRICE_LOOKUP_TO_PLAN: Record<string, PlanId> = {
  kairos_solo_monthly: 'solo',
  kairos_pro_monthly: 'pro',
  kairos_studio_monthly: 'studio',
  kairos_agency_monthly: 'agency',
};

async function stripe<T>(
  env: Env,
  path: string,
  form?: Record<string, string>,
): Promise<T> {
  const res = await fetch(`${STRIPE_API}${path}`, {
    method: form ? 'POST' : 'GET',
    headers: {
      authorization: `Bearer ${env.STRIPE_SECRET_KEY}`,
      'content-type': 'application/x-www-form-urlencoded',
    },
    body: form ? new URLSearchParams(form).toString() : undefined,
  });

  if (res.status === 429 || res.status >= 500) {
    throw new RetryableError(`Stripe returned ${res.status}`, 60);
  }
  if (!res.ok) {
    throw new Error(`Stripe ${path} failed (${res.status}): ${(await res.text()).slice(0, 300)}`);
  }
  return (await res.json()) as T;
}

export async function createCheckoutSession(
  env: Env,
  account: AccountRecord,
  priceLookupKey: string,
): Promise<{ url: string }> {
  if (!PRICE_LOOKUP_TO_PLAN[priceLookupKey]) {
    throw badRequest(`Unknown price "${priceLookupKey}"`);
  }

  const prices = await stripe<{ data: Array<{ id: string }> }>(
    env,
    `/prices?lookup_keys[]=${encodeURIComponent(priceLookupKey)}&limit=1`,
  );
  const price = prices.data[0];
  if (!price) throw badRequest(`Price "${priceLookupKey}" is not configured in Stripe`);

  const session = await stripe<{ url: string }>(env, '/checkout/sessions', {
    mode: 'subscription',
    'line_items[0][price]': price.id,
    'line_items[0][quantity]': '1',
    success_url: `${env.PUBLIC_BASE_URL}/billing/done?session_id={CHECKOUT_SESSION_ID}`,
    cancel_url: `${env.PUBLIC_BASE_URL}/pricing`,
    client_reference_id: account.id,
    customer_email: account.email,
    'subscription_data[metadata][account_id]': account.id,
    'metadata[account_id]': account.id,
  });

  return { url: session.url };
}

/**
 * Verifies a Stripe webhook signature.
 *
 * Without this, anyone who learns the endpoint URL can POST a fabricated
 * `subscription.created` and grant themselves a paid plan.
 */
export async function verifyStripeSignature(
  env: Env,
  payload: string,
  signatureHeader: string,
): Promise<boolean> {
  const parts = new Map(
    signatureHeader.split(',').map((kv) => {
      const idx = kv.indexOf('=');
      return [kv.slice(0, idx).trim(), kv.slice(idx + 1).trim()] as const;
    }),
  );

  const timestamp = parts.get('t');
  const signature = parts.get('v1');
  if (!timestamp || !signature) return false;

  // Reject replays of an old, legitimately-signed payload.
  const ageSeconds = Math.abs(Date.now() / 1000 - Number(timestamp));
  if (!Number.isFinite(ageSeconds) || ageSeconds > 300) return false;

  const key = await crypto.subtle.importKey(
    'raw',
    new TextEncoder().encode(env.STRIPE_WEBHOOK_SECRET),
    { name: 'HMAC', hash: 'SHA-256' },
    false,
    ['sign'],
  );
  const mac = await crypto.subtle.sign(
    'HMAC',
    key,
    new TextEncoder().encode(`${timestamp}.${payload}`),
  );
  const expected = [...new Uint8Array(mac)].map((b) => b.toString(16).padStart(2, '0')).join('');

  return timingSafeEqual(expected, signature);
}

function timingSafeEqual(a: string, b: string): boolean {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

interface StripeEvent {
  id: string;
  type: string;
  data: { object: Record<string, unknown> };
}

export async function handleStripeEvent(env: Env, event: StripeEvent): Promise<void> {
  const object = event.data.object;

  switch (event.type) {
    case 'checkout.session.completed': {
      const accountId = String(object.client_reference_id ?? '');
      const customer = String(object.customer ?? '');
      const subscription = String(object.subscription ?? '');
      if (!accountId) return;

      await db(env).run(
        `UPDATE accounts
            SET stripe_customer_id = ?, stripe_subscription_id = ?, status = 'active', updated_at = ?
          WHERE id = ?`,
        customer,
        subscription,
        nowIso(),
        accountId,
      );
      await qualifyReferral(env, accountId);
      break;
    }

    case 'customer.subscription.created':
    case 'customer.subscription.updated': {
      const accountId = await accountIdForSubscription(env, object);
      if (!accountId) return;

      const plan = planFromSubscription(object);
      const stripeStatus = String(object.status ?? '');
      const status =
        stripeStatus === 'active' || stripeStatus === 'trialing'
          ? 'active'
          : stripeStatus === 'past_due' || stripeStatus === 'unpaid'
            ? 'past_due'
            : 'paused';

      await db(env).run(
        `UPDATE accounts SET plan = ?, status = ?, updated_at = ? WHERE id = ?`,
        plan,
        status,
        nowIso(),
        accountId,
      );
      await audit(env, {
        accountId,
        actor: 'system:billing',
        action: 'subscription.updated',
        entityType: 'account',
        entityId: accountId,
        detail: { plan, status, stripeStatus },
      });
      break;
    }

    case 'customer.subscription.deleted': {
      const accountId = await accountIdForSubscription(env, object);
      if (!accountId) return;

      // Cancellation stops automation immediately. Leaving autopilot on for a
      // lapsed account means publishing on behalf of someone who stopped paying.
      await db(env).batch([
        {
          sql: `UPDATE accounts SET status = 'canceled', plan = 'trial', updated_at = ? WHERE id = ?`,
          binds: [nowIso(), accountId],
        },
        {
          sql: `UPDATE automation_controls
                   SET autopilot_publishing = 0, autopilot_replies = 0, updated_at = ?
                 WHERE account_id = ?`,
          binds: [nowIso(), accountId],
        },
      ]);
      await audit(env, {
        accountId,
        actor: 'system:billing',
        action: 'subscription.canceled',
        entityType: 'account',
        entityId: accountId,
        detail: {},
      });
      break;
    }

    case 'invoice.payment_failed': {
      const accountId = await accountIdForSubscription(env, {
        ...object,
        id: object.subscription,
      });
      if (!accountId) return;

      await db(env).run(
        `UPDATE accounts SET status = 'past_due', updated_at = ? WHERE id = ?`,
        nowIso(),
        accountId,
      );
      await audit(env, {
        accountId,
        actor: 'system:billing',
        action: 'payment.failed',
        entityType: 'account',
        entityId: accountId,
        detail: { invoice: object.id },
      });
      break;
    }

    default:
      // Unhandled event types are acknowledged rather than retried.
      break;
  }
}

async function accountIdForSubscription(
  env: Env,
  object: Record<string, unknown>,
): Promise<string | null> {
  const metadata = (object.metadata ?? {}) as Record<string, unknown>;
  const fromMetadata = metadata.account_id ? String(metadata.account_id) : '';
  if (fromMetadata) return fromMetadata;

  const subscriptionId = String(object.id ?? '');
  if (!subscriptionId) return null;

  const row = await db(env).first<{ id: string }>(
    `SELECT id FROM accounts WHERE stripe_subscription_id = ?`,
    subscriptionId,
  );
  return row?.id ?? null;
}

function planFromSubscription(object: Record<string, unknown>): PlanId {
  const items = (object.items ?? {}) as { data?: Array<{ price?: { lookup_key?: string } }> };
  const lookup = items.data?.[0]?.price?.lookup_key ?? '';
  return PRICE_LOOKUP_TO_PLAN[lookup] ?? 'trial';
}

/**
 * A referral qualifies when the referred account actually pays, not when it
 * signs up. Rewarding signups pays for fake accounts.
 */
async function qualifyReferral(env: Env, referredAccountId: string): Promise<void> {
  const referral = await db(env).first<{ id: string; referrer_account_id: string }>(
    `SELECT id, referrer_account_id FROM referrals
      WHERE referred_account_id = ? AND status = 'pending'`,
    referredAccountId,
  );
  if (!referral) return;

  await db(env).run(
    `UPDATE referrals SET status = 'qualified' WHERE id = ?`,
    referral.id,
  );
  await enqueue(
    env,
    'billing.reconcile',
    { referralId: referral.id },
    {
      accountId: referral.referrer_account_id,
      idempotencyKey: `referral-reward:${referral.id}`,
    },
  );
}

/**
 * Daily subscription hygiene. Two jobs in one: nudge accounts whose trial is
 * ending, and stop automation for accounts that have been past due long enough
 * that the card is not coming back.
 */
export async function handleBillingReconcile(env: Env, job: Job): Promise<void> {
  const graceCutoff = new Date(Date.now() - 7 * 86_400_000).toISOString();

  const lapsed = await db(env).all<{ id: string }>(
    `SELECT id FROM accounts WHERE status = 'past_due' AND updated_at <= ?`,
    graceCutoff,
  );

  for (const account of lapsed) {
    await db(env).batch([
      {
        sql: `UPDATE accounts SET status = 'paused', updated_at = ? WHERE id = ?`,
        binds: [nowIso(), account.id],
      },
      {
        sql: `UPDATE automation_controls
                 SET autopilot_publishing = 0, autopilot_replies = 0, updated_at = ?
               WHERE account_id = ?`,
        binds: [nowIso(), account.id],
      },
    ]);
    await audit(env, {
      accountId: account.id,
      actor: 'system:billing',
      action: 'account.paused_for_nonpayment',
      entityType: 'account',
      entityId: account.id,
      detail: { graceDays: 7 },
    });
  }

  const expiredTrials = await db(env).all<{ id: string }>(
    `SELECT id FROM accounts
      WHERE plan = 'trial' AND status = 'active'
        AND trial_ends_at IS NOT NULL AND trial_ends_at <= ?`,
    nowIso(),
  );

  for (const account of expiredTrials) {
    await db(env).run(
      `UPDATE automation_controls
          SET autopilot_publishing = 0, autopilot_replies = 0, updated_at = ?
        WHERE account_id = ?`,
      nowIso(),
      account.id,
    );
    await audit(env, {
      accountId: account.id,
      actor: 'system:billing',
      action: 'trial.expired',
      entityType: 'account',
      entityId: account.id,
      detail: {},
    });
  }

  // Referral rewards arrive on this job with a referralId payload.
  const payload = JSON.parse(job.payload) as { referralId?: string };
  if (payload.referralId) {
    await db(env).run(
      `UPDATE referrals SET status = 'rewarded', reward_applied_at = ? WHERE id = ? AND status = 'qualified'`,
      nowIso(),
      payload.referralId,
    );
    await audit(env, {
      accountId: job.account_id,
      actor: 'system:billing',
      action: 'referral.rewarded',
      entityType: 'referral',
      entityId: payload.referralId,
      detail: { rewardMonths: 1 },
    });
  }
}

export { PLANS };
