import { Hono } from 'hono';
import { z } from 'zod';
import type { AppBindings } from '../env';
import { db } from '../lib/db';
import { requireAuth } from '../lib/auth';
import { badRequest, notFound, unauthorized } from '../lib/errors';
import { PLANS, type AccountRecord } from '../lib/types';
import { createCheckoutSession, handleStripeEvent, verifyStripeSignature } from '../engines/billing';

export const billing = new Hono<AppBindings>();

billing.get('/v1/plans', (c) =>
  c.json({
    plans: Object.values(PLANS)
      .filter((p) => p.id !== 'trial')
      .map((p) => ({
        id: p.id,
        name: p.name,
        monthlyPriceUsd: p.monthlyPriceUsd,
        priceLookupKey: `kairos_${p.id}_monthly`,
        includes: {
          channels: p.channels,
          postsPerMonth: p.postsPerMonth,
          repliesPerMonth: p.repliesPerMonth,
          seats: p.seats,
        },
      })),
  }),
);

billing.use('/v1/billing/checkout', requireAuth);

billing.post('/v1/billing/checkout', async (c) => {
  const { accountId } = c.get('ctx');
  const parsed = z
    .object({ priceLookupKey: z.string() })
    .safeParse(await c.req.json().catch(() => ({})));
  if (!parsed.success) throw badRequest('Invalid checkout payload', parsed.error.issues);

  const account = await db(c.env).first<AccountRecord>(
    `SELECT * FROM accounts WHERE id = ?`,
    accountId,
  );
  if (!account) throw notFound('Account');

  return c.json(await createCheckoutSession(c.env, account, parsed.data.priceLookupKey));
});

/**
 * Stripe webhook. The raw body is read before parsing because the signature is
 * computed over exact bytes: re-serializing parsed JSON changes them and the
 * verification fails.
 */
billing.post('/webhooks/stripe', async (c) => {
  const signature = c.req.header('stripe-signature') ?? '';
  const raw = await c.req.text();

  if (!signature || !(await verifyStripeSignature(c.env, raw, signature))) {
    throw unauthorized('Invalid Stripe signature');
  }

  let event;
  try {
    event = JSON.parse(raw);
  } catch {
    throw badRequest('Webhook body was not valid JSON');
  }

  await handleStripeEvent(c.env, event);
  // Stripe retries on any non-2xx, so acknowledge once the event is handled.
  return c.json({ received: true });
});
