import { Hono } from 'hono';
import { z } from 'zod';
import type { AppBindings } from '../env';
import { db } from '../lib/db';
import { requireAuth } from '../lib/auth';
import { badRequest, notFound, unauthorized } from '../lib/errors';
import { PLANS, type AccountRecord } from '../lib/types';
import { createCheckoutSession, handleStripeEvent, verifyStripeSignature } from '../engines/billing';

export const billing = new Hono<AppBindings>();

/** Minimal page shell for the browser-facing Stripe return routes. */
function page(title: string, body: string): string {
  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${title} — Kairos</title>
<style>body{font-family:system-ui,sans-serif;max-width:36rem;margin:4rem auto;padding:0 1rem;color:#1a1a1a}h1{font-size:1.4rem}table{border-collapse:collapse}td,th{padding:.3rem .8rem;text-align:left;border-bottom:1px solid #ddd}</style>
</head>
<body><h1>${title}</h1>${body}</body>
</html>`;
}

/**
 * Stripe checkout return pages. Checkout redirects the customer's browser
 * here, so both must exist and be unauthenticated. Entitlement is granted by
 * the webhook, never by reaching this page — so the session_id query param is
 * deliberately ignored and never reflected into the response.
 */
billing.get('/billing/done', (c) =>
  c.html(
    page(
      'Payment received',
      `<p>Your subscription payment went through. Your account is upgraded
       automatically within a few moments — you can close this page and return
       to the app.</p>`,
    ),
  ),
);

billing.get('/pricing', (c) => {
  const rows = Object.values(PLANS)
    .filter((p) => p.id !== 'trial')
    .map(
      (p) =>
        `<tr><td>${p.name}</td><td>$${p.monthlyPriceUsd}/mo</td>` +
        `<td>${p.channels} channels, ${p.postsPerMonth} posts, ${p.repliesPerMonth} replies</td></tr>`,
    )
    .join('');
  return c.html(
    page(
      'Plans',
      `<p>Checkout was canceled — nothing was charged. Start a new checkout
       from the app whenever you are ready.</p>
       <table><tr><th>Plan</th><th>Price</th><th>Includes</th></tr>${rows}</table>`,
    ),
  );
});

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
