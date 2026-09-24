#!/usr/bin/env node
/**
 * C2 — the live round-trip gate.
 *
 * Every other test in this repo replaces `fetch` before it runs, which is
 * correct for unit tests and is also why the suite once stayed green while the
 * dashboard could not reach the API at all and read five field names the API
 * never returned. This script is the one check that executes against the real
 * deployed dependency, so it is the only one that can go red for those.
 *
 * It deliberately does NOT call /health. /health is unauthenticated, reads a
 * jobs-table count, and returns ok:true regardless of CORS, bindings, or
 * response shape — it would have passed with every defect this gate exists to
 * catch. A check that cannot fail for the failure it names is the thing the
 * governance review called a decoration with the grammar of a check.
 *
 * Origins are read from wrangler.jsonc rather than restated here, so the gate
 * cannot silently drift from the config it is guarding.
 *
 * Usage:
 *   KAIROS_API_KEY=kai_sk_... npm run test:contract
 */

import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const root = join(here, '..', '..');

/** Same whole-line-comment convention test/config.test.ts relies on. */
function loadWrangler() {
  const raw = readFileSync(join(root, 'wrangler.jsonc'), 'utf8');
  return JSON.parse(
    raw.split('\n').filter((l) => !/^\s*\/\//.test(l)).join('\n'),
  );
}

const cfg = loadWrangler();
const prod = cfg.env.production.vars;

// Defaults are production, read from config so the gate cannot drift from what
// it guards. The overrides exist to exercise this script against a local
// Worker; the target is printed in the header and the summary so an overridden
// run can never be mistaken for the production gate in CI output.
const OVERRIDDEN = Boolean(process.env.KAIROS_CONTRACT_BASE);
const API = (process.env.KAIROS_CONTRACT_BASE || prod.PUBLIC_BASE_URL).replace(/\/$/, '');
const DASHBOARD_ORIGINS = (process.env.KAIROS_CONTRACT_ORIGIN || prod.DASHBOARD_ORIGINS)
  .split(',').map((o) => o.trim()).filter(Boolean);
const DASHBOARD = DASHBOARD_ORIGINS[0];
const UNLISTED = 'https://not-the-dashboard.invalid';

const KEY = process.env.KAIROS_API_KEY;

let pass = 0;
let fail = 0;
let unverified = 0;
const failures = [];

function ok(label, detail) {
  pass++;
  console.log(`  [32mPASS[0m  ${label}${detail ? `  ${detail}` : ''}`);
}
function bad(label, detail) {
  fail++;
  failures.push(`${label} — ${detail}`);
  console.log(`  [31mFAIL[0m  ${label}\n        ${detail}`);
}
/**
 * Distinct from pass on purpose. An empty collection cannot confirm item-level
 * field names, and counting that as a pass would recreate the original bug:
 * a check reporting success for something it never examined.
 */
function skip(label, why) {
  unverified++;
  console.log(`  [33mUNVERIFIED[0m  ${label}\n        ${why}`);
}

function assert(cond, label, detail) {
  if (cond) ok(label);
  else bad(label, detail);
}

/** Preflight responses cache per origin; a stale one makes a correct allowlist look broken. */
function bust(path) {
  return `${API}${path}${path.includes('?') ? '&' : '?'}_cb=${Date.now()}${Math.random().toString(16).slice(2)}`;
}

async function preflight(origin, path = '/v1/me') {
  const res = await fetch(bust(path), {
    method: 'OPTIONS',
    headers: {
      origin,
      'access-control-request-method': 'GET',
      'access-control-request-headers': 'authorization',
    },
  });
  return res.headers.get('access-control-allow-origin');
}

async function getJson(path) {
  const res = await fetch(bust(path), {
    headers: { authorization: `Bearer ${KEY}`, origin: DASHBOARD },
  });
  const body = await res.json().catch(() => null);
  return { status: res.status, body, acao: res.headers.get('access-control-allow-origin') };
}

/** Walks a dotted path; returns a sentinel for "absent" so `null`/0/"" survive. */
const ABSENT = Symbol('absent');
function at(obj, path) {
  return path.split('.').reduce((o, k) => (o != null && k in o ? o[k] : ABSENT), obj);
}

function expectKeys(label, obj, keys) {
  for (const k of keys) {
    const v = at(obj, k);
    assert(v !== ABSENT, `${label} has ${k}`, `missing — the client reads this`);
  }
}

function expectAbsent(label, obj, keys) {
  for (const k of keys) {
    const v = at(obj, k);
    assert(
      v === ABSENT,
      `${label} does not resurrect ${k}`,
      `present again — this name was a real defect (F2); a client reading it would break`,
    );
  }
}

// ---------------------------------------------------------------------------

console.log(`\nC2 live contract gate`);
console.log(`  API        ${API}`);
console.log(`  dashboard  ${DASHBOARD}`);
console.log(`  target     ${OVERRIDDEN ? 'OVERRIDDEN (not the production gate)' : 'production'}\n`);

if (!KEY) {
  console.error(
    '  Refusing to run without KAIROS_API_KEY.\n' +
    '  This gate exists because a suite that silently skips the only check\n' +
    '  touching the real dependency is how the original defects survived.\n' +
    '  Pass a key for an account on the deployed Worker:\n\n' +
    '    KAIROS_API_KEY=kai_sk_... npm run test:contract\n',
  );
  process.exit(2);
}

console.log('Reachability — can a browser on the deployed dashboard reach this API? (F1)');
{
  const allowed = await preflight(DASHBOARD);
  assert(
    allowed === DASHBOARD,
    'deployed dashboard origin is in the live allowlist',
    `preflight returned access-control-allow-origin=${allowed === null ? '(none)' : allowed}; ` +
      `the deployed dashboard cannot read this API`,
  );

  const unlisted = await preflight(UNLISTED);
  assert(
    unlisted === null,
    'an unlisted origin is refused',
    `preflight returned access-control-allow-origin=${unlisted}; the allowlist is not exact`,
  );
}

console.log('\nAuthentication');
{
  const res = await fetch(bust('/v1/me'), { headers: { authorization: 'Bearer kai_sk_notarealkey' } });
  assert(res.status === 401, 'an invalid key is rejected', `expected 401, got ${res.status}`);
}

console.log('\nResponse shapes — does the API still return what the client reads? (F2)');

{
  const { status, body, acao } = await getJson('/v1/me');
  if (status !== 200) {
    bad('/v1/me responds 200', `got ${status} — check KAIROS_API_KEY`);
  } else {
    assert(acao === DASHBOARD, '/v1/me sends CORS headers on the real response', `acao=${acao}`);
    expectKeys('/v1/me', body, [
      'account.plan', 'account.status', 'plan.name', 'plan.channels',
      'controls.autopilot_publishing', 'controls.autopilot_replies',
      'controls.daily_publish_cap', 'channels',
    ]);
    expectAbsent('/v1/me', body, ['account.plan_id', 'controls.autopilot']);
  }
}

{
  const { status, body } = await getJson('/v1/insights');
  if (status !== 200) {
    bad('/v1/insights responds 200', `got ${status}`);
  } else {
    expectKeys('/v1/insights', body, [
      'window', 'totals.posts', 'totals.impressions', 'totals.engagements', 'totals.follows',
      'pillars', 'usage.postsPublished', 'usage.repliesSent', 'usage.planLimits.postsPerMonth',
      'hoursSaved.hours', 'hoursSaved.basis',
    ]);
    expectAbsent('/v1/insights', body, ['hours_saved']);
  }
}

// Collection endpoints: the envelope is always assertable, item fields only
// when the account actually has rows. The difference is reported, never hidden.
const collections = [
  {
    path: '/v1/calendar', envelope: 'slots',
    item: ['id', 'scheduled_for', 'status', 'platform', 'pillar'], forbidden: [],
  },
  {
    path: '/v1/posts?status=draft', envelope: 'posts',
    item: ['id', 'hook', 'body', 'status', 'variant', 'platform'], forbidden: ['content'],
  },
  {
    path: '/v1/inbox', envelope: 'conversations',
    item: ['id', 'author_handle', 'priority', 'status', 'last_message_at', 'platform'],
    forbidden: [], forbiddenEnvelope: ['messages'],
  },
];

for (const c of collections) {
  const { status, body } = await getJson(c.path);
  if (status !== 200) {
    bad(`${c.path} responds 200`, `got ${status}`);
    continue;
  }
  const rows = at(body, c.envelope);
  assert(Array.isArray(rows), `${c.path} returns ${c.envelope}[]`, `envelope key ${c.envelope} missing or not an array`);
  for (const k of c.forbiddenEnvelope ?? []) {
    assert(at(body, k) === ABSENT, `${c.path} does not resurrect ${k}`, `present again — this name was a real defect (F2)`);
  }

  if (!Array.isArray(rows) || rows.length === 0) {
    skip(
      `${c.path} item fields`,
      `no rows on this account, so item-level names could not be checked. ` +
        `Run against an account with data to close this.`,
    );
    continue;
  }
  const row = rows[0];
  expectKeys(`${c.path}[0]`, row, c.item);
  expectAbsent(`${c.path}[0]`, row, c.forbidden);
}

// ---------------------------------------------------------------------------

console.log(`\n${'─'.repeat(64)}`);
console.log(`  ${pass} passed   ${fail} failed   ${unverified} unverified`);

if (unverified > 0 && fail === 0) {
  console.log(
    `\n  ${unverified} check(s) could not run for lack of data. That is not a pass:\n` +
    `  item-level field names stay unguarded until this runs against an\n` +
    `  account with calendar slots, drafts, and inbox conversations.`,
  );
}

if (fail > 0) {
  console.log(`\n  Failures:`);
  for (const f of failures) console.log(`    - ${f}`);
  console.log('');
  process.exit(1);
}

console.log('');
process.exit(0);
