import { describe, it, expect, afterEach } from 'vitest';
import { createHarness, seedAccount, type TestHarness } from './helpers/d1';
import { claim, drain, enqueue, reapExpiredLocks, type JobHandler, type JobKind } from '../src/queue/jobs';
import { RetryableError } from '../src/lib/errors';

let harness: TestHarness | null = null;

function setup(): TestHarness {
  harness = createHarness();
  seedAccount(harness);
  return harness;
}

afterEach(() => {
  harness?.close();
  harness = null;
});

function handlers(partial: Partial<Record<JobKind, JobHandler>>): Record<JobKind, JobHandler> {
  const noop: JobHandler = async () => undefined;
  return {
    'plan.generate': noop,
    'content.draft': noop,
    'publish.dispatch': noop,
    'metrics.collect': noop,
    'growth.rebalance': noop,
    'inbox.sync': noop,
    'reply.draft': noop,
    'reply.send': noop,
    'billing.reconcile': noop,
    ...partial,
  };
}

describe('job queue', () => {
  it('collapses duplicate work behind an idempotency key', async () => {
    const h = setup();

    const first = await enqueue(h.env, 'publish.dispatch', { postId: 'p1' }, {
      accountId: 'acct_test',
      idempotencyKey: 'publish:p1',
    });
    const second = await enqueue(h.env, 'publish.dispatch', { postId: 'p1' }, {
      accountId: 'acct_test',
      idempotencyKey: 'publish:p1',
    });

    expect(first).toBeTruthy();
    // This is the guard that stops overlapping cron ticks double-publishing.
    expect(second).toBeNull();

    const count = h.sqlite.prepare('SELECT COUNT(*) AS n FROM jobs').get() as { n: number };
    expect(count.n).toBe(1);
  });

  it('claims each job exactly once across concurrent drains', async () => {
    const h = setup();
    for (let i = 0; i < 5; i++) {
      await enqueue(h.env, 'metrics.collect', { postId: `p${i}` }, { accountId: 'acct_test' });
    }

    const [a, b] = await Promise.all([claim(h.env, 10), claim(h.env, 10)]);
    const ids = [...a, ...b].map((j) => j.id);

    expect(ids.length).toBe(5);
    expect(new Set(ids).size).toBe(5);
  });

  it('does not claim jobs scheduled for the future', async () => {
    const h = setup();
    await enqueue(h.env, 'metrics.collect', {}, {
      accountId: 'acct_test',
      runAfter: new Date(Date.now() + 3600_000),
    });

    expect(await claim(h.env, 10)).toHaveLength(0);
  });

  it('retries a retryable failure with backoff, then buries it', async () => {
    const h = setup();
    await enqueue(h.env, 'inbox.sync', {}, { accountId: 'acct_test', maxAttempts: 2 });

    const failing = handlers({
      'inbox.sync': async () => {
        throw new RetryableError('platform is down', 10);
      },
    });

    const first = await drain(h.env, failing, 10);
    expect(first.failed).toBe(1);

    let job = h.sqlite.prepare('SELECT * FROM jobs').get() as {
      status: string;
      attempts: number;
      run_after: string;
    };
    expect(job.status).toBe('pending');
    expect(job.attempts).toBe(1);
    // Backoff must push the retry into the future, or the queue spins.
    expect(new Date(job.run_after).getTime()).toBeGreaterThan(Date.now());

    // Make it due again and exhaust the attempt budget.
    h.sqlite
      .prepare(`UPDATE jobs SET run_after = ?`)
      .run(new Date(Date.now() - 1000).toISOString());
    await drain(h.env, failing, 10);

    job = h.sqlite.prepare('SELECT * FROM jobs').get() as typeof job;
    expect(job.status).toBe('dead');
    expect(job.attempts).toBe(2);
  });

  it('buries a permanent failure without retrying', async () => {
    const h = setup();
    await enqueue(h.env, 'content.draft', {}, { accountId: 'acct_test', maxAttempts: 5 });

    await drain(
      h.env,
      handlers({
        'content.draft': async () => {
          throw new Error('slot references a missing pillar');
        },
      }),
      10,
    );

    const job = h.sqlite.prepare('SELECT * FROM jobs').get() as { status: string; attempts: number };
    // A malformed job retried five times is five identical failures.
    expect(job.status).toBe('dead');
    expect(job.attempts).toBe(1);
  });

  it('returns jobs whose lock expired back to the queue', async () => {
    const h = setup();
    await enqueue(h.env, 'reply.send', {}, { accountId: 'acct_test' });
    await claim(h.env, 1);

    h.sqlite
      .prepare(`UPDATE jobs SET locked_until = ?`)
      .run(new Date(Date.now() - 60_000).toISOString());

    expect(await reapExpiredLocks(h.env)).toBe(1);
    expect(await claim(h.env, 1)).toHaveLength(1);
  });

  it('marks a handled job done and records an audit line when one dies', async () => {
    const h = setup();
    await enqueue(h.env, 'growth.rebalance', {}, { accountId: 'acct_test', maxAttempts: 1 });
    await enqueue(h.env, 'plan.generate', {}, { accountId: 'acct_test' });

    const res = await drain(
      h.env,
      handlers({
        'growth.rebalance': async () => {
          throw new Error('boom');
        },
      }),
      10,
    );

    expect(res.processed).toBe(2);
    expect(res.failed).toBe(1);

    const done = h.sqlite
      .prepare(`SELECT COUNT(*) AS n FROM jobs WHERE status = 'done'`)
      .get() as { n: number };
    expect(done.n).toBe(1);

    const audits = h.sqlite
      .prepare(`SELECT action FROM audit_events WHERE action = 'job.dead'`)
      .all();
    expect(audits).toHaveLength(1);
  });
});
