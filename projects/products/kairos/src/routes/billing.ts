import { Hono } from 'hono';
import { z } from 'zod';
import type { AppBindings } from '../env';
import { db } from '../lib/db';
import { requireAuth } from '../lib/auth';
import { badRequest, notFound, unauthorized } from '../lib/errors';
import { PLANS, type AccountRecord } from '../lib/types';
import { createCheckoutSession, handleStripeEvent, verifyStripeSignature } from '../engines/billing';

export const billing = new Hono<AppBindings>();

/** Escapes text interpolated into the HTML pages below. */
function esc(value: string | number): string {
  return String(value).replace(
    /[&<>"']/g,
    (ch) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[ch] as string,
  );
}

// These pages carry Stripe return URLs in browser history, so no referrer
// leakage, no scripts, and no search indexing.
const PAGE_HEADERS = {
  'content-security-policy': "default-src 'none'; style-src 'unsafe-inline'",
  'referrer-policy': 'no-referrer',
  'x-robots-tag': 'noindex',
};

/** Minimal page shell for the browser-facing Stripe return routes. */
function page(title: string, body: string): string {
  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(title)} · Kairos</title>
<style>body{font-family:system-ui,sans-serif;max-width:36rem;margin:4rem auto;padding:0 1rem;color:#1a1a1a}h1{font-size:1.4rem}table{border-collapse:collapse}td,th{padding:.3rem .8rem;text-align:left;border-bottom:1px solid #ddd}</style>
</head>
<body><h1>${esc(title)}</h1>${body}</body>
</html>`;
}

/**
 * Stripe checkout return pages. Checkout redirects the customer's browser
 * here, so both must exist and be unauthenticated. Entitlement is granted by
 * the webhook, never by reaching this page, so the session_id query param is
 * deliberately ignored and never reflected into the response. The copy stays
 * conditional because anyone can load these URLs and delayed payment methods
 * redirect before the payment settles.
 */
billing.get('/billing/done', (c) =>
  c.html(
    page(
      'Checkout complete',
      `<p>If you just completed checkout, your payment is being processed and
       your account upgrades automatically once it settles, usually within
       moments. You can close this page and return to the app.</p>`,
    ),
    200,
    PAGE_HEADERS,
  ),
);

billing.get('/pricing', (c) => {
  // Set by the cancel_url Stripe redirects to; the value is compared, never
  // reflected.
  const canceled = c.req.query('canceled') === '1';
  const rows = Object.values(PLANS)
    .filter((p) => p.id !== 'trial')
    .map(
      (p) =>
        `<tr><td>${esc(p.name)}</td><td>$${esc(p.monthlyPriceUsd)}/mo</td>` +
        `<td>${esc(p.channels)} channels, ${esc(p.postsPerMonth)} posts, ${esc(p.repliesPerMonth)} replies</td></tr>`,
    )
    .join('');
  return c.html(
    page(
      'Plans',
      `${canceled ? '<p>Checkout was canceled and nothing was charged. Start a new checkout from the app whenever you are ready.</p>' : ''}
       <table><tr><th>Plan</th><th>Price</th><th>Includes</th></tr>${rows}</table>`,
    ),
    200,
    PAGE_HEADERS,
  );
});

/** Public, unauthenticated: what the marketing page needs to render honestly. */
billing.get('/v1/config', (c) =>
  c.json({ signupEnabled: c.env.SIGNUP_ENABLED === 'true' }),
);

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
