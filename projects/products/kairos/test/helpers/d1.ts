import { DatabaseSync } from 'node:sqlite';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import type { Env } from '../../src/env';

const here = dirname(fileURLToPath(import.meta.url));

/**
 * A D1-shaped facade over node:sqlite.
 *
 * Testing the queue and the governance gates against mocks proves only that the
 * mocks agree with themselves. Both depend on real SQL behaviour (conditional
 * UPDATE row counts, unique-index conflicts, aggregate queries), so the tests
 * run the actual migration and the actual statements.
 */
class StatementShim {
  private binds: unknown[] = [];
  constructor(private readonly sqlite: DatabaseSync, private readonly sql: string) {}

  bind(...values: unknown[]): this {
    // SQLite has no boolean type; D1 accepts them and coerces.
    this.binds = values.map((v) => (typeof v === 'boolean' ? (v ? 1 : 0) : v));
    return this;
  }

  async all<T>(): Promise<{ results: T[] }> {
    const stmt = this.sqlite.prepare(this.sql);
    return { results: stmt.all(...(this.binds as never[])) as T[] };
  }

  async first<T>(): Promise<T | null> {
    const stmt = this.sqlite.prepare(this.sql);
    return (stmt.get(...(this.binds as never[])) as T) ?? null;
  }

  async run(): Promise<{ meta: { changes: number } }> {
    const stmt = this.sqlite.prepare(this.sql);
    const res = stmt.run(...(this.binds as never[]));
    return { meta: { changes: Number(res.changes) } };
  }
}

export class D1Shim {
  constructor(readonly sqlite: DatabaseSync) {}

  prepare(sql: string): StatementShim {
    return new StatementShim(this.sqlite, sql);
  }

  async batch(statements: StatementShim[]): Promise<unknown[]> {
    const out: unknown[] = [];
    for (const s of statements) out.push(await s.run());
    return out;
  }
}

export interface TestHarness {
  env: Env;
  sqlite: DatabaseSync;
  close(): void;
}

export function createHarness(overrides: Partial<Env> = {}): TestHarness {
  const sqlite = new DatabaseSync(':memory:');
  sqlite.exec('PRAGMA foreign_keys = ON;');
  sqlite.exec(readFileSync(join(here, '..', '..', 'migrations', '0001_init.sql'), 'utf8'));

  const env = {
    DB: new D1Shim(sqlite) as unknown as D1Database,
    MEDIA: {} as R2Bucket,
    CACHE: {} as KVNamespace,
    ENVIRONMENT: 'test',
    DRAFT_MODEL: 'claude-opus-5',
    STRATEGY_MODEL: 'claude-opus-5',
    DRY_RUN: 'true',
    JOB_BATCH_SIZE: '25',
    PUBLIC_BASE_URL: 'https://test.invalid',
    ANTHROPIC_API_KEY: 'test-key',
    STRIPE_SECRET_KEY: 'sk_test',
    STRIPE_WEBHOOK_SECRET: 'whsec_test',
    AUTH_SIGNING_KEY: 'test-signing-key',
    ...overrides,
  } as Env;

  return { env, sqlite, close: () => sqlite.close() };
}

/** Inserts a minimally complete account so gate tests have something to gate. */
export function seedAccount(
  h: TestHarness,
  opts: {
    id?: string;
    plan?: string;
    status?: string;
    autopilotPublishing?: boolean;
    autopilotReplies?: boolean;
    dailyPublishCap?: number;
    dailyReplyCap?: number;
  } = {},
): string {
  const id = opts.id ?? 'acct_test';
  const now = new Date().toISOString();

  h.sqlite
    .prepare(
      `INSERT INTO accounts (id, email, display_name, timezone, plan, status, referral_code, created_at, updated_at)
       VALUES (?, ?, ?, 'UTC', ?, ?, ?, ?, ?)`,
    )
    .run(id, `${id}@test.invalid`, 'Test Creator', opts.plan ?? 'pro', opts.status ?? 'active', id.toUpperCase(), now, now);

  h.sqlite
    .prepare(
      `INSERT INTO automation_controls
         (account_id, autopilot_publishing, autopilot_replies, daily_publish_cap, daily_reply_cap, updated_at)
       VALUES (?, ?, ?, ?, ?, ?)`,
    )
    .run(
      id,
      opts.autopilotPublishing ? 1 : 0,
      opts.autopilotReplies ? 1 : 0,
      opts.dailyPublishCap ?? 10,
      opts.dailyReplyCap ?? 25,
      now,
    );

  return id;
}
