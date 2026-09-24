/**
 * Kairos on a plain Node host (CT920 dev), without Cloudflare.
 *
 * The Worker code is unchanged: this file supplies the three bindings it
 * expects (D1, R2, KV) from local equivalents, runs the five cron schedules in
 * process, and serves the static dashboard export from the same port so the
 * browser never makes a cross-origin call.
 */
import { DatabaseSync } from 'node:sqlite';
import { existsSync, mkdirSync, readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { Hono } from 'hono';
import { serve } from '@hono/node-server';
import { serveStatic } from '@hono/node-server/serve-static';
import worker from '../index';
import type { Env } from '../env';

// ---------- D1 over node:sqlite (same shape the test suite uses) ----------

class Statement {
  private binds: unknown[] = [];
  constructor(private readonly sqlite: DatabaseSync, private readonly sql: string) {}
  bind(...values: unknown[]): this {
    this.binds = values.map((v) => (typeof v === 'boolean' ? (v ? 1 : 0) : v === undefined ? null : v));
    return this;
  }
  async all<T>() { return { results: this.sqlite.prepare(this.sql).all(...(this.binds as never[])) as T[] }; }
  async first<T>() { return ((this.sqlite.prepare(this.sql).get(...(this.binds as never[])) as T) ?? null); }
  async run() {
    const res = this.sqlite.prepare(this.sql).run(...(this.binds as never[]));
    return { meta: { changes: Number(res.changes) } };
  }
}

class D1 {
  constructor(readonly sqlite: DatabaseSync) {}
  prepare(sql: string) { return new Statement(this.sqlite, sql); }
  async batch(statements: Statement[]) {
    const out: unknown[] = [];
    this.sqlite.exec('BEGIN');
    try {
      for (const s of statements) out.push(await s.run());
      this.sqlite.exec('COMMIT');
    } catch (err) {
      this.sqlite.exec('ROLLBACK');
      throw err;
    }
    return out;
  }
}

/** Applies each migration once, in filename order, tracked in _migrations. */
function migrate(sqlite: DatabaseSync, dir: string): void {
  sqlite.exec(`CREATE TABLE IF NOT EXISTS _migrations (name TEXT PRIMARY KEY, applied_at TEXT NOT NULL)`);
  const done = new Set((sqlite.prepare(`SELECT name FROM _migrations`).all() as { name: string }[]).map((r) => r.name));
  for (const file of readdirSync(dir).filter((f) => f.endsWith('.sql')).sort()) {
    if (done.has(file)) continue;
    sqlite.exec('BEGIN');
    sqlite.exec(readFileSync(join(dir, file), 'utf8'));
    sqlite.prepare(`INSERT INTO _migrations (name, applied_at) VALUES (?, ?)`).run(file, new Date().toISOString());
    sqlite.exec('COMMIT');
    console.log(`migration applied: ${file}`);
  }
}

// ---------- KV (rate-limit counters only; losing them on restart is harmless) ----------

class Kv {
  private store = new Map<string, { value: string; expires: number }>();
  async get(key: string) {
    const hit = this.store.get(key);
    if (!hit) return null;
    if (hit.expires && hit.expires < Date.now()) { this.store.delete(key); return null; }
    return hit.value;
  }
  async put(key: string, value: string, opts?: { expirationTtl?: number }) {
    this.store.set(key, { value, expires: opts?.expirationTtl ? Date.now() + opts.expirationTtl * 1000 : 0 });
  }
  async delete(key: string) { this.store.delete(key); }
}

// ---------- R2 on the filesystem (read path is all the routes use) ----------

class R2 {
  constructor(private readonly root: string) { mkdirSync(root, { recursive: true }); }
  private path(key: string) {
    const p = resolve(this.root, key);
    if (!p.startsWith(resolve(this.root) + '/')) throw new Error('Invalid media key');
    return p;
  }
  async get(key: string) {
    const p = this.path(key);
    if (!existsSync(p)) return null;
    const bytes = readFileSync(p);
    return {
      body: bytes,
      httpEtag: `"${bytes.length}"`,
      writeHttpMetadata(_headers: Headers) { /* content type is not tracked locally */ },
    };
  }
  async put(key: string, value: ArrayBuffer | Uint8Array | string) {
    const p = this.path(key);
    mkdirSync(dirname(p), { recursive: true });
    writeFileSync(p, typeof value === 'string' ? value : Buffer.from(value as ArrayBuffer));
    return {};
  }
}

// ---------- boot ----------

const need = (name: string) => {
  const v = process.env[name];
  if (!v) throw new Error(`${name} is required`);
  return v;
};

const dataDir = need('KAIROS_DATA_DIR');
mkdirSync(dataDir, { recursive: true });
const sqlite = new DatabaseSync(join(dataDir, 'kairos.sqlite'));
sqlite.exec('PRAGMA journal_mode = WAL; PRAGMA foreign_keys = ON; PRAGMA busy_timeout = 5000;');
migrate(sqlite, need('KAIROS_MIGRATIONS_DIR'));

const env = {
  DB: new D1(sqlite) as unknown as D1Database,
  MEDIA: new R2(join(dataDir, 'media')) as unknown as R2Bucket,
  CACHE: new Kv() as unknown as KVNamespace,
  ENVIRONMENT: process.env.ENVIRONMENT ?? 'dev-ct920',
  DRAFT_MODEL: process.env.DRAFT_MODEL ?? 'claude-opus-5',
  STRATEGY_MODEL: process.env.STRATEGY_MODEL ?? 'claude-opus-5',
  DRY_RUN: process.env.DRY_RUN ?? 'true',
  JOB_BATCH_SIZE: process.env.JOB_BATCH_SIZE ?? '25',
  PUBLIC_BASE_URL: need('PUBLIC_BASE_URL'),
  DASHBOARD_ORIGINS: process.env.DASHBOARD_ORIGINS ?? '',
  AI_MODE: process.env.AI_MODE ?? 'agent',
  AGENT_TOKEN: process.env.AGENT_TOKEN,
  ANTHROPIC_API_KEY: process.env.ANTHROPIC_API_KEY ?? '',
  STRIPE_SECRET_KEY: process.env.STRIPE_SECRET_KEY ?? '',
  STRIPE_WEBHOOK_SECRET: process.env.STRIPE_WEBHOOK_SECRET ?? '',
  AUTH_SIGNING_KEY: need('AUTH_SIGNING_KEY'),
  TOKEN_ENCRYPTION_KEY: need('TOKEN_ENCRYPTION_KEY'),
} as Env;

const pending = new Set<Promise<unknown>>();
const ctx = {
  waitUntil(p: Promise<unknown>) { pending.add(p); p.finally(() => pending.delete(p)).catch(() => {}); },
  passThroughOnException() {},
  props: {},
} as unknown as ExecutionContext;

// ---------- the five schedules, in process ----------

let running = false;
async function tick(): Promise<void> {
  if (running) return; // a slow drain must not overlap the next one
  running = true;
  try {
    const now = new Date();
    const m = now.getUTCMinutes();
    const h = now.getUTCHours();
    const due = ['* * * * *'];
    if (m % 15 === 0) due.push('*/15 * * * *');
    if (m === 17) due.push('17 * * * *');
    if (h === 5 && m === 10) due.push('10 5 * * *');
    if (h === 6 && m === 20) due.push('20 6 * * *');
    for (const cron of due) {
      await worker.scheduled({ cron, scheduledTime: now.getTime() } as ScheduledController, env, ctx);
      await Promise.allSettled([...pending]);
    }
  } catch (err) {
    console.error('scheduler tick failed', err);
  } finally {
    running = false;
  }
}

// Queue drains every 15s rather than every minute: agent answers arrive
// asynchronously and the dev loop should not wait a full minute to see them.
setInterval(() => {
  const s = new Date().getUTCSeconds();
  if (s < 15) void tick();
  else void (async () => {
    if (running) return;
    running = true;
    try {
      await worker.scheduled({ cron: '* * * * *', scheduledTime: Date.now() } as ScheduledController, env, ctx);
      await Promise.allSettled([...pending]);
    } finally { running = false; }
  })();
}, 15_000);

// ---------- HTTP ----------

const app = new Hono();
const dashboardDir = process.env.KAIROS_DASHBOARD_DIR;
if (dashboardDir && existsSync(dashboardDir)) {
  app.use('/*', async (c, next) => {
    const p = new URL(c.req.url).pathname;
    if (c.req.method !== 'GET' || p.startsWith('/v1/') || p === '/health') return next();
    return serveStatic({ root: dashboardDir })(c, next);
  });
}
app.all('*', (c) => worker.fetch(c.req.raw, env, ctx));

const port = Number(process.env.PORT ?? 3480);
const host = process.env.HOST ?? '127.0.0.1';
serve({ fetch: app.fetch, port, hostname: host }, () => {
  console.log(`kairos listening on http://${host}:${port} (AI_MODE=${env.AI_MODE}, DRY_RUN=${env.DRY_RUN})`);
});
