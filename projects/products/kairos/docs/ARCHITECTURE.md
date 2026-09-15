# KAIROS architecture

## The shape of the thing

KAIROS is one Cloudflare Worker. There is no server to keep alive, no queue broker, and no scheduler process. Five cron expressions and a D1-backed job table do the work that would normally need a background worker fleet.

```
HTTP  ──▶  Hono router  ──▶  D1
                             R2 (media)
                             KV (cache)

cron  ──▶  scheduled()  ──▶  job queue (D1)  ──▶  engines  ──▶  adapters  ──▶  platforms
                                                     │
                                                     └──▶  Claude (Messages API)
```

## Why a D1 job table instead of Cloudflare Queues

Queues would work and would be less code. The table was chosen for three reasons that matter to a solo operator.

The backlog is inspectable with SQL, so "why did this creator's post not go out" is one query rather than a support ticket. The whole system runs locally against `node:sqlite` in tests, so queue behaviour is covered by real tests rather than mocks. And there is no additional service to reason about when something goes wrong at 2am.

The cost is that claiming is not free. D1 has no `SELECT ... FOR UPDATE`, so `claim()` selects candidates and then takes each one with a conditional `UPDATE ... WHERE status = 'pending'`, keeping only the rows where `changes === 1`. Two overlapping cron invocations therefore cannot both run one job. That property is tested directly.

## The five loops

| Cron | Does |
|---|---|
| `* * * * *` | Drains the job queue |
| `*/15 * * * *` | Enqueues due publishes and inbox syncs |
| `17 * * * *` | Sweeps published posts with stale metrics |
| `10 5 * * *` | Tops up the planning horizon, rebalances pillar weights |
| `20 6 * * *` | Subscription reconciliation and dunning |

They are separate schedules rather than one dispatcher so that a slow daily planning run cannot starve the every-minute drain, which is what actually gets posts out on time.

## The engine chain

```
plan.generate ──▶ content.draft ──▶ publish.dispatch ──▶ metrics.collect
      ▲                                                        │
      └──────────────── growth.rebalance ◀─────────────────────┘

inbox.sync ──▶ reply.draft ──▶ reply.send
```

The loop back from `metrics.collect` to `growth.rebalance` is the part that makes this a growth engine rather than a scheduler. Pillar weights are rewritten from measured performance, and those weights drive the next calendar. Without that edge the system publishes the same distribution of content forever regardless of what the audience responds to.

Two details in that loop are deliberate. Weights move only partway toward their target each cycle, because one strong month should not collapse the calendar onto a single pillar. And a pillar needs at least three measured posts before it is judged at all, because an average over one lucky post is noise.

## Prompt caching as an architectural constraint

Every system prompt is assembled in stability order: an operator prompt identical across all accounts, then the creator's strategy, then the volatile request. A cache breakpoint sits at the end of the creator's strategy.

This is not a micro-optimization. It is roughly a tenfold cost difference on the largest input span, and it dictates real constraints on the code: `OPERATOR_SYSTEM` is a deploy-level edit because changing one byte invalidates every cached prefix in the fleet, and every engine builds its prefix through the same `loadCreator` helper so that planning, drafting, and replies all share one cache entry per account.

## Governance is structural, not advisory

The vault's standing ethical layer requires that automated pipelines have a stop condition, an audit trail, and a rollback path. Each is a table rather than a convention.

`automation_controls` is the stop condition. Autopilot defaults to off, and an account with no row gets autopilot off rather than a permissive default, because a creator who has never made a choice has not consented to unattended publishing. There are daily caps and a pause window.

`audit_events` is the trail. Every engine writes on every state change a creator could later dispute. Audit writes are deliberately allowed to fail without rolling back the work they describe, but they log when they do, so a gap is visible rather than silent.

The rollback path is that nothing is destructive. A blocked publish holds the post as approved and marks the slot skipped rather than discarding the content. A rejected reply reopens the conversation.

Two policies are enforced in code rather than in prompts, because a prompt is a request and a gate is a guarantee. The banned-phrase list is checked after generation, and `governance.ts` refuses to auto-send replies on lead, collaboration, and hostile threads no matter what the per-intent rules table says. The rules table can tighten policy and never loosen it past that floor.

## Failure handling

The distinction that matters is retryable against permanent. A rate limit, a connection failure, or a 5xx becomes a `RetryableError` and gets exponential backoff with jitter. A malformed request or a missing record fails immediately and lands in the dead-letter state, because retrying a 400 five times is five identical failures and a delay before anyone notices.

A publish that fails mid-flight returns the post to `approved` rather than `failed`, so the queue retries it rather than requiring manual re-approval.

## Multi-tenancy

D1 has no row-level security. Account isolation is a property of the `Db.scoped()` helper and of every query carrying `account_id`. This is the sharpest edge in the codebase: one forgotten `WHERE account_id = ?` is a cross-tenant data leak, and nothing in the database will catch it.

## Testing approach

Tests run against real SQLite through a D1-shaped shim, executing the actual migration and the actual statements. Queue claiming, backoff, idempotency, and the governance gates all depend on real SQL behaviour such as conditional update row counts and unique-index conflicts. Mocking those would prove only that the mocks agree with themselves.

The suite caught one real design property while being written: the test for daily publish caps initially inserted two slots at the same timestamp on one channel and failed on the uniqueness index, which was the index correctly refusing to double-book a channel.

## Running it

```bash
npm install
npm run check          # typecheck source and tests
npm test               # 30 tests against real SQLite
npm run db:local       # apply migrations to local D1
npm run dev            # wrangler dev on port 8789
```

`DRY_RUN` defaults to `true`, so every outbound platform call is simulated. The full pipeline runs end to end before any creator has connected an account. Simulated metrics are drawn from a seeded distribution rather than returned as zeros, because a growth engine fed constant zeros never demonstrates that it reweights.
