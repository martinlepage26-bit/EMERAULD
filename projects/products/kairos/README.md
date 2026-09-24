# KAIROS

A subscription platform that plans, publishes, and grows a creator's audience without the creator scheduling posts or answering messages by hand.

Named for the Greek sense of *kairos*: not clock time, but the opportune moment. What the system decides is when a thing should be said, and to whom.

## What it does

A creator describes their positioning, voice, and content pillars once, then connects their channels. From there the system runs five loops on its own:

- **Plans.** Builds a rolling fourteen-day calendar, allocating across pillars by measured performance rather than by guess.
- **Drafts.** Generates several variants per slot in the creator's voice, enforcing their banned-phrase list in code after generation.
- **Publishes.** Dispatches on schedule through platform adapters, with retry, backoff, and idempotency that make double-posting structurally impossible.
- **Answers.** Triages inbound messages by intent and priority, drafts replies, and sends only the ones that pass an explicit confidence and policy gate.
- **Compounds.** Measures what worked, rewrites pillar weights from the results, and recycles proven posts to an audience that has since turned over.

Autopilot is off by default. Every loop checks a per-account stop condition, daily caps, and a pause window before it acts, and writes an audit line when it does.

## Stack

Cloudflare Workers, D1, R2, KV. Hono for routing, Zod for validation, the Anthropic TypeScript SDK for generation, Stripe for subscriptions. One Worker, five cron triggers, no server.

The operator dashboard is a separate Next.js app in `frontend/`, exported as static assets to Cloudflare Pages at https://kairos-dashboard-dy4.pages.dev. It authenticates with the same `kai_sk_` API key the Worker issues at signup, held in the browser that typed it. Because it runs on its own origin, the Worker must list that origin in `DASHBOARD_ORIGINS` or the browser blocks every request; `test/config.test.ts` fails the build if production ever points that back at a dev server.

## Quick start

```bash
npm install
npm run check     # typecheck source and tests
npm test          # 61 tests against real SQLite via a D1 shim, fully offline
npm run db:local  # apply migrations
npm run dev       # http://localhost:8789
```

`npm test` is hermetic: it replaces every network call, which is right for unit
tests and is also why it cannot notice the API and its clients drifting apart.
That gap is covered by one separate gate:

```bash
KAIROS_API_KEY=kai_sk_... npm run test:contract
```

`test/contract/live.mjs` runs against the **deployed** Worker from the deployed
dashboard's origin, and is the only check here that executes against the real
dependency. It asserts that the dashboard origin is in the live CORS allowlist,
that an unlisted origin is refused, and that every field the dashboard reads is
still present — including that five field names which were once wrong have not
come back. Deliberately not a `/health` probe: `/health` is unauthenticated and
returns `ok:true` regardless of CORS, bindings, or response shape, so it would
pass while the dashboard was entirely unable to read the API. Checks that cannot
fail for the failure they name are worse than no check.

Run it before merging anything that touches a route response or `DASHBOARD_ORIGINS`.
It refuses to run without a key rather than skipping, and reports checks it could
not perform as `UNVERIFIED` rather than counting them as passes.

`DRY_RUN` defaults to `true`, so the whole pipeline runs end to end with simulated platform calls. Nothing is posted anywhere from local dev. Live posting exists only in the `production` wrangler environment (`env.production` in `wrangler.jsonc` sets `DRY_RUN` to `"false"`), which deploys via `npm run deploy` (`wrangler deploy --env production`).

Copy `.dev.vars.example` to `.dev.vars` first. `TOKEN_ENCRYPTION_KEY` is required before any channel can be connected: creator access tokens are encrypted with it before they reach the database, and rotating it makes existing tokens undecryptable.

```bash
# Create an account and keep the returned API key
curl -X POST localhost:8789/v1/accounts \
  -H 'content-type: application/json' \
  -d '{"email":"you@example.com","displayName":"Your Name"}'

# Then: PUT /v1/strategy, POST /v1/pillars, POST /v1/channels
# The first channel triggers planning immediately.
curl localhost:8789/v1/calendar -H "authorization: Bearer kai_sk_..."
```

## API

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/v1/accounts` | Sign up, returns the API key once |
| `GET` | `/v1/me` | Account, plan, controls, channels |
| `PUT` | `/v1/strategy` | Positioning, voice, banned phrases |
| `GET POST` | `/v1/pillars` | Content pillars |
| `POST` | `/v1/channels` | Connect a platform |
| `PUT` | `/v1/controls` | Autopilot, caps, pause window |
| `GET` | `/v1/calendar` | Planned and drafted slots |
| `POST` | `/v1/calendar/plan` | Trigger a planning run |
| `GET` | `/v1/posts` | Drafts and published posts |
| `POST` | `/v1/posts/:id/approve` | Approve, optionally edited |
| `POST` | `/v1/posts/:id/reject` | Reject a draft |
| `GET` | `/v1/inbox` | Triage queue, most consequential first |
| `POST` | `/v1/replies/:id/approve` | Approve and send a reply |
| `PUT` | `/v1/reply-rules` | Per-intent auto-send policy |
| `GET` | `/v1/insights` | Performance, pillar weights, hours saved |
| `GET` | `/v1/plans` | Pricing |
| `POST` | `/v1/billing/checkout` | Stripe checkout session |
| `POST` | `/webhooks/stripe` | Signed webhook receiver |
| `GET` | `/media/:key` | Serves post media to fetching platforms (capability URL) |
| `GET` | `/health` | Queue depth and dead-letter count |

## Pricing

| Plan | Price | Channels | Posts | Replies |
|---|---|---|---|---|
| Solo | $49 | 2 | 60 | 200 |
| Pro | $149 | 5 | 200 | 800 |
| Studio | $399 | 15 | 700 | 2,000 |
| Agency | $999 | 50 | 2,000 | 5,000 |

Allowances are enforced in `governance.ts`, not merely displayed. Every tier clears 70% gross margin at full consumption; the derivation is in `docs/UNIT-ECONOMICS.md`.

## Documentation

- [`docs/90-DAY-PLAN.md`](docs/90-DAY-PLAN.md): the path to $50,000 MRR, and why the volume path fails on arithmetic
- [`docs/UNIT-ECONOMICS.md`](docs/UNIT-ECONOMICS.md): cost per operation, margin by plan, what breaks the model
- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md): the loops, the caching constraint, the governance surface
