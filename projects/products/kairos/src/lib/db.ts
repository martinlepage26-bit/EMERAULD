import type { Env } from '../env';
import { newId, nowIso } from './ids';

export type Row = Record<string, unknown>;

/**
 * Thin D1 wrapper. The point of routing every read through `scoped` is that
 * account isolation becomes a property of the helper rather than something each
 * query has to remember: D1 has no row-level security, so a forgotten
 * `WHERE account_id = ?` is a cross-tenant data leak.
 */
export class Db {
  constructor(private readonly d1: D1Database) {}

  async all<T = Row>(sql: string, ...binds: unknown[]): Promise<T[]> {
    const res = await this.d1
      .prepare(sql)
      .bind(...binds)
      .all<T>();
    return res.results ?? [];
  }

  async first<T = Row>(sql: string, ...binds: unknown[]): Promise<T | null> {
    return (await this.d1
      .prepare(sql)
      .bind(...binds)
      .first<T>()) as T | null;
  }

  async run(sql: string, ...binds: unknown[]): Promise<D1Result> {
    return this.d1
      .prepare(sql)
      .bind(...binds)
      .run();
  }

  async batch(statements: Array<{ sql: string; binds: unknown[] }>): Promise<void> {
    if (statements.length === 0) return;
    await this.d1.batch(statements.map((s) => this.d1.prepare(s.sql).bind(...s.binds)));
  }

  /** Fetch a single row that must belong to `accountId`, or null. */
  async scoped<T = Row>(table: string, id: string, accountId: string): Promise<T | null> {
    return this.first<T>(`SELECT * FROM ${table} WHERE id = ? AND account_id = ?`, id, accountId);
  }
}

export function db(env: Env): Db {
  return new Db(env.DB);
}

/**
 * Append-only audit record. Called by every engine on every state change that a
 * creator could later dispute ("why did this go out?"). Failures here are
 * swallowed deliberately: losing an audit line must not roll back the work it
 * describes, but it is logged so the gap is visible.
 */
export async function audit(
  env: Env,
  entry: {
    accountId: string | null;
    actor: string;
    action: string;
    entityType: string;
    entityId?: string | null;
    detail?: unknown;
  },
): Promise<void> {
  try {
    await db(env).run(
      `INSERT INTO audit_events (id, account_id, actor, action, entity_type, entity_id, detail, created_at)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?)`,
      newId('aud'),
      entry.accountId,
      entry.actor,
      entry.action,
      entry.entityType,
      entry.entityId ?? null,
      JSON.stringify(entry.detail ?? {}),
      nowIso(),
    );
  } catch (err) {
    console.error('audit write failed', entry.action, err);
  }
}

export function currentPeriod(at = new Date()): string {
  return `${at.getUTCFullYear()}-${String(at.getUTCMonth() + 1).padStart(2, '0')}`;
}

export async function meter(
  env: Env,
  accountId: string,
  metric: string,
  delta = 1,
): Promise<void> {
  await db(env).run(
    `INSERT INTO usage_counters (account_id, period, metric, value)
     VALUES (?, ?, ?, ?)
     ON CONFLICT(account_id, period, metric) DO UPDATE SET value = value + excluded.value`,
    accountId,
    currentPeriod(),
    metric,
    delta,
  );
}

export async function usageFor(
  env: Env,
  accountId: string,
  metric: string,
  period = currentPeriod(),
): Promise<number> {
  const row = await db(env).first<{ value: number }>(
    `SELECT value FROM usage_counters WHERE account_id = ? AND period = ? AND metric = ?`,
    accountId,
    period,
    metric,
  );
  return row?.value ?? 0;
}
