import { describe, expect, it } from 'vitest';
import { handleStripeEvent } from '../src/engines/billing';
import { createHarness, seedAccount, type TestHarness } from './helpers/d1';

interface AccountRow {
  stripe_customer_id: string | null;
  stripe_subscription_id: string | null;
  status: string;
  plan: string;
}

function accountRow(h: TestHarness, id: string): AccountRow {
  return h.sqlite
    .prepare(
      `SELECT stripe_customer_id, stripe_subscription_id, status, plan FROM accounts WHERE id = ?`,
    )
    .get(id) as unknown as AccountRow;
}

function checkoutCompleted(eventId: string, object: Record<string, unknown>) {
  return { id: eventId, type: 'checkout.session.completed', data: { object } };
}

describe('stripe webhook handling', () => {
  it('activates a paid checkout and stores the stripe ids', async () => {
    const h = createHarness();
    const acct = seedAccount(h, { plan: 'trial', status: 'paused' });

    await handleStripeEvent(
      h.env,
      checkoutCompleted('evt_paid', {
        client_reference_id: acct,
        customer: 'cus_A',
        subscription: 'sub_A',
        payment_status: 'paid',
      }),
    );

    const row = accountRow(h, acct);
    expect(row.status).toBe('active');
    expect(row.stripe_customer_id).toBe('cus_A');
    expect(row.stripe_subscription_id).toBe('sub_A');
    h.close();
  });

  it('does not activate a completed session whose payment has not settled', async () => {
    const h = createHarness();
    const acct = seedAccount(h, { plan: 'trial', status: 'paused' });

    // Async payment methods complete the session before the payment settles;
    // activation belongs to the later async_payment_succeeded event.
    await handleStripeEvent(
      h.env,
      checkoutCompleted('evt_unpaid', {
        client_reference_id: acct,
        customer: 'cus_A',
        subscription: 'sub_A',
        payment_status: 'unpaid',
      }),
    );

    const row = accountRow(h, acct);
    expect(row.status).toBe('paused');
    expect(row.stripe_customer_id).toBeNull();
    h.close();
  });

  it('never blanks stored stripe ids when a delivery lacks the fields', async () => {
    const h = createHarness();
    const acct = seedAccount(h);
    h.sqlite
      .prepare(`UPDATE accounts SET stripe_customer_id = 'cus_A', stripe_subscription_id = 'sub_A' WHERE id = ?`)
      .run(acct);

    await handleStripeEvent(
      h.env,
      checkoutCompleted('evt_sparse', { client_reference_id: acct, payment_status: 'paid' }),
    );

    const row = accountRow(h, acct);
    expect(row.stripe_customer_id).toBe('cus_A');
    expect(row.stripe_subscription_id).toBe('sub_A');
    h.close();
  });

  it('applies each event id at most once', async () => {
    const h = createHarness();
    const acct = seedAccount(h, { plan: 'trial', status: 'paused' });
    const event = checkoutCompleted('evt_once', {
      client_reference_id: acct,
      customer: 'cus_A',
      subscription: 'sub_A',
      payment_status: 'paid',
    });

    await handleStripeEvent(h.env, event);
    // A later event cancels the account; a Stripe retry of the original
    // delivery must not resurrect it.
    h.sqlite.prepare(`UPDATE accounts SET status = 'canceled' WHERE id = ?`).run(acct);
    await handleStripeEvent(h.env, event);

    expect(accountRow(h, acct).status).toBe('canceled');
    h.close();
  });

  it('keeps the stored plan when the price lookup key is unknown', async () => {
    const h = createHarness();
    const acct = seedAccount(h, { plan: 'agency', status: 'active' });
    h.sqlite.prepare(`UPDATE accounts SET stripe_subscription_id = 'sub_A' WHERE id = ?`).run(acct);

    await handleStripeEvent(h.env, {
      id: 'evt_unknown_price',
      type: 'customer.subscription.updated',
      data: {
        object: {
          id: 'sub_A',
          status: 'active',
          metadata: {},
          items: { data: [{ price: { lookup_key: 'kairos_agency_annual' } }] },
        },
      },
    });

    const row = accountRow(h, acct);
    expect(row.plan).toBe('agency');
    expect(row.status).toBe('active');
    h.close();
  });
});
