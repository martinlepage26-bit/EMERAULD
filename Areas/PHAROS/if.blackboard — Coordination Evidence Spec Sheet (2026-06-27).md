---
type: tool-spec
title: if.blackboard — Coordination Evidence Spec Sheet (2026-06-27)
aliases:
- if.blackboard
- if_blackboard
- InfraFabric Blackboard
- Blackboard
- if.tasks
tags:
- infrafabric
- blackboard
- agent-ledger
- coordination
- evidence
- governance
- mcp
- tool-spec
- areas
- redirected
- task
- sign
- pharos
status: active
domain: pharos
created: '2026-06-27'
updated: '2026-06-27'
vault_area: Areas
canonical_path: Areas/PHAROS/if.blackboard — Coordination Evidence Spec Sheet (2026-06-27).md
backlink_count: 14
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[Areas/PHAROS/Agent Bus — Design Record (Retired Runtime)]]'
- '[[Areas/PHAROS/InfraFabric Architecture]]'
- '[[Areas/PHAROS/InfraFabric MCP Stack — Remote Bundles]]'
- '[[Areas/PHAROS/InfraFabric R0.5 Rollout — Hosted API Migration (2026-06-29 to 2026-06-30)]]'
- '[[Areas/PHAROS/Stacklight-owner-explainer]]'
- '[[Areas/PHAROS/if.switchboard — InfraFabric Product Center]]'
- '[[Areas/PHAROS/micro1 — Data Licensing Opportunity (PHAROS)]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[archive/session-state/session-state-003]]'
- '[[memory/daily/2026-06-27]]'
- '[[memory/daily/2026-06-30]]'
- '[[memory/daily/2026-07-01]]'
evidence_boundary: Local InfraFabric canon plus public endpoint liveness check from this machine on 2026-06-27; no authenticated remote write test performed. Access-pattern section updated 2026-07-01 against the R0.5 Postgres authority runbook (2026-06-29) and mtl-03 handover (2026-06-30); durable-authority claims not independently re-tested from this session.
local_sources:
- raw sources/infrafabric-archive/if.blackboard Full Explainer v1.3 (Multi-Audience, Split-Boundary Strict).md
- governance/global/AGENTS.md
- governance/hephaistos/PHASE-2-INTEGRATION-ROADMAP.md
- governance/hephaistos/BOWIE.md
- wiki/InfraFabric MCP Stack — Remote Bundles.md
- wiki/InfraFabric Architecture.md
- /home/martin/infra/micro1/4164-pharos-micro1-operational-data-licensing-blackboard-iftrace-assessment-2026-06-08.md
- /home/martin/infra/micro1/docs/4391-infrafabric-blackboard-micro1-explainer-2026-06.md
- /home/martin/infra/micro1/camilo-meeting-cheat-sheet.md
- /home/martin/apps/stacklight/documentation/agents/5009-if-blackboard-postgres-authority-runbook-2026-06-29.md
- /home/martin/apps/stacklight/documentation/agents/5011-stacklight-blackboard-mtl03-fresh-session-handover-2026-06-30.md
checked_urls:
- https://infrafabric.io/llm/blackboard/index.md.txt
- https://infrafabric.io/llm/blackboard/tasks.open.md.txt
- https://infrafabric.io/llm/blackboard/tasks.search.json.txt
- https://infrafabric.io/llm/signals/index.md.txt
- https://infrafabric.io/llm/if.registry.json.txt
---

# if.blackboard — Coordination Evidence Spec Sheet (2026-06-27)

`if.blackboard` is InfraFabric's append-only coordination evidence surface: a durable ledger for task state, session binding, signals, checkpoints, verification records, and closeout evidence. Its job is not to route messages or certify conclusions. Its job is to make agent work reviewable after the fact and resumable across sessions without relying on memory, transcript fragments, or trust in an agent's closing sentence.

**Short form:** `if.blackboard` is the source of truth for durable agent task state. On resume, read the task row, then the latest checkpoint, then the closeout, then artifact references, then prior searches.

**Current claim boundary:** local InfraFabric canon supports the module as a `preview`, `active_internal`, high-internal-use coordination/evidence module. A live public endpoint check from this machine on 2026-06-27 found the historical `/llm/blackboard/**` and `/llm/signals/**` URLs redirecting to the InfraFabric sign-in surface, so old "public no-login" language must be treated as historical unless reverified with current auth/publication policy.

> [!info] Superseded access pattern — resolved 2026-07-01
> The SSH/MCP access pattern described below (`root@infrafabric.io` → Proxmox container 270 → local script/JSONL mutation) was accurate as of this note's creation (2026-06-27) but was migrated two days later. As of the [[InfraFabric R0.5 Rollout — Hosted API Migration (2026-06-29 to 2026-06-30)|R0.5 rollout (2026-06-29)]], `if.blackboard` durable reads/writes go exclusively through a **hosted HTTPS API** at `https://api.infrafabric.io`, backed by **PostgreSQL on host `mtl-02`** (database `if_blackboard`, table `if_blackboard.r05_events`). Direct script, JSONL, local database, and SSH-wrapper mutation paths now fail closed by design — they are not an alternate durable path, they are disabled. The MCP entrypoint changed accordingly: `iftransport mcp if_blackboard` now launches an API-backed stdio shim (`if_blackboard_api_mcp_server.py`) that calls the hosted API, not the old SSH-tunneled `if-blackboard-mcp-server.mjs`. This closes the contradiction flagged against [[Stacklight-owner-explainer]], which described the post-migration state correctly. Source: `/home/martin/apps/stacklight/documentation/agents/5009-if-blackboard-postgres-authority-runbook-2026-06-29.md` (status as of 2026-06-29T19:59Z) and `5011-stacklight-blackboard-mtl03-fresh-session-handover-2026-06-30.md`. The rest of this spec sheet (data model, claim register, non-claims) still holds; only the **access/transport path** changed.

---

## Identity

| Field | Spec |
|---|---|
| Canonical product id | `if.blackboard` |
| Legacy alias | `if.tasks` |
| Local MCP server name | `if_blackboard` |
| Product family | [[InfraFabric Architecture]] |
| Category | Coordination evidence / append-only task ledger |
| Historical registry posture | `preview`, `active_internal`, `high_internal` in the 2026-03-06 local canon |
| Access pattern (until 2026-06-29) | Remote MCP wrapper over SSH to `root@infrafabric.io` → Proxmox container 270 → local script/JSONL mutation; do not use direct `10.10.10.170` URLs from this machine — **superseded, see below** |
| Access pattern (current, from R0.5, 2026-06-29) | Hosted HTTPS API at `https://api.infrafabric.io`, PostgreSQL authority on `mtl-02` (`if_blackboard.r05_events`); MCP entrypoint is an API-backed stdio shim (`if_blackboard_api_mcp_server.py`), not an SSH tunnel; direct script/DB/SSH-wrapper mutation fails closed |
| Primary local vault note | [[InfraFabric MCP Stack — Remote Bundles]] |

---

## What It Does

`if.blackboard` records the structured evidence of agent work:

- Task creation and task status transitions.
- Session binding between an agent, task, and `sid`.
- Acceptance criteria / definition of done before closeout.
- Typed checkpoints such as progress, last verified state, next step, traps, open questions, and artifact references.
- Signal records for blockers, help requests, escalations, and verification events.
- Closeout records with result evidence and, in documented blackboard data products, SHA-256 result hashes.
- Derived queues that expose work state, context debt, missing DoD, missing evidence, and task-session joins.
- Machine-readable export/search surfaces when the public or authenticated renderer is available.

The useful governance property is not that the board makes work perfect. It is that it makes work inspectable, resumable, and difficult to silently smooth over.

---

## What It Is Not

`if.blackboard` should not absorb claims that belong to other InfraFabric modules.

| Not A | Why |
|---|---|
| `if.switchboard` | Switchboard owns audited reachability, wake delivery, contact registration, request/response routing, and delivery records. |
| `if.bus` | Bus owns transport/control boundary claims. |
| `if.context` | Context owns bounded recall, post-its, and resumable context packs. |
| `if.trace` | Trace owns receipt/provenance/integrity surfaces. |
| Chat | Blackboard is durable state, not conversational exchange. |
| Certification engine | It does not certify correctness, compliance, safety, or legal conclusions by itself. |
| Message-delivery guarantee | It does not prove exactly-once delivery, SIP queue correctness, route selection, or delivery timing. |
| Multi-host durability proof | Local append-only JSONL discipline does not by itself prove fleet-grade immutability or distributed durability. |

**Boundary test:** if a sentence would become false while the blackboard ledger remained intact but switchboard delivery semantics changed, the sentence does not belong in a blackboard spec.

---

## Data Model

### Core Event Streams

Historical local canon and June 2026 audit material identify three core event families:

| Store | Role |
|---|---|
| `tasks.events.jsonl` | Task creation, updates, checkpoints, closeouts, ownership, acceptance state, evidence pointers. |
| `sessions.events.jsonl` | Session lifecycle and task/session continuity. |
| `signals.events.jsonl` | Help, blocker, escalation, verification, and coordination signals. |

### Blackboard Entry Anatomy

| Field | Purpose |
|---|---|
| Task ID | Stable sequential work identifier, e.g. `IF-3477`. |
| Session binding | Connects the task to the session where it was initiated or resumed. |
| Acceptance criteria | Falsifiable done conditions written before closeout. |
| Typed checkpoint | Structured mid-task state for future agents. |
| Traps | Hard-won failure modes and environment-specific gotchas that must carry forward. |
| Intent vs. result | Separates intended work from actual result, including partial or blocked outcomes. |
| Artifact refs | Files, URLs, commits, reports, or evidence packages that support the closeout. |
| Result hash | Hash of closeout/result payload where the workflow requires tamper-evident sealing. |

---

## Derived Surfaces

The 2026-03-06 canonical explainer names these blackboard-owned derived surfaces:

| Surface | Intended Role | Current 2026-06-27 Check |
|---|---|---|
| `/llm/blackboard/index.md.txt` | Blackboard index / entrypoint | Redirected to InfraFabric sign-in from this machine. |
| `/llm/blackboard/tasks.open.md.txt` | Open-task feed | Redirected to sign-in. |
| `/llm/blackboard/tasks.open.ready.md.txt` | Ready-to-pick queue | Redirected to sign-in. |
| `/llm/blackboard/tasks.open.with_context.md.txt` | Open tasks with context links | Redirected to sign-in. |
| `/llm/blackboard/tasks.open.missing_context.md.txt` | Context-debt queue | Redirected to sign-in. |
| `/llm/blackboard/tasks.open.missing_dod.md.txt` | Missing-acceptance-criteria queue | Redirected to sign-in. |
| `/llm/blackboard/tasks.done.missing_evidence.md.txt` | Closed tasks with evidence debt | Redirected to sign-in. |
| `/llm/blackboard/tasks.sessions.md.txt` | Task-session join surface | Redirected to sign-in. |
| `/llm/blackboard/tasks.search.json.txt` | Machine-readable task search/export | Redirected to sign-in; JSON could not be parsed without auth. |
| `/llm/signals/index.md.txt` | Signals and escalation entrypoint | Redirected to sign-in. |
| `/llm/if.registry.json.txt` | Registry mirror | Redirected to sign-in; JSON could not be parsed without auth. |

**Interpretation:** this does not disprove the module. It changes the current publication claim. As of this check, public no-login reviewability is not verified from this machine; use "authenticated or previously public derived views" until the publication policy is confirmed.

---

## Operating Contract

The local contract is:

1. Create task record before doing governed work.
2. Bind task to session and agent identity.
3. Record acceptance criteria before closure.
4. Checkpoint material changes in state.
5. Carry traps forward rather than burying them in transcripts.
6. Close with evidence references and result hash where required.
7. Use derived queues to expose debt rather than hiding it.
8. Treat blackboard state as authoritative over memory when resuming.

For the local laptop, the access rule from `governance/global/AGENTS.md` controlled durable access through 2026-06-27: use the configured remote MCP wrappers and `root@infrafabric.io`; do not use direct `10.10.10.170` MCP URLs. As of the 2026-06-29 R0.5 rollout, that rule is superseded: the only normal durable path is the hosted API (`https://api.infrafabric.io`), accessed via `if-cli blackboard api ...` or the API-backed MCP shim; bare legacy local writer verbs fail closed rather than falling back to SSH/script mutation.

---

## Integration Map

| Neighbor | Relationship |
|---|---|
| [[InfraFabric Architecture]] | Places `if.blackboard` as a supporting module, below the `if.switchboard` product center. |
| [[InfraFabric MCP Stack — Remote Bundles]] | Documents local `if_blackboard` MCP wrapper and SSH tunnel risk. |
| `if.switchboard` | Routes/reaches agents; blackboard records durable state and evidence. |
| `if.context` | Supplies bounded recall/context; blackboard records task state and checkpoints. |
| `if.trace` | Supplies provenance/integrity receipts; blackboard holds coordination evidence and debt queues. |
| Hermes | Reads/writes routing and escalation state after authorized clearance. |
| Queen Keyport / Argus | Can audit blackboard records for governance chain, refusal conditions, and escalation evidence. |
| BOWIE | May write approved `if.blackboard` task/checkpoint/verification records when workflow authority permits. |

---

## Business / Data-Asset Posture

June 2026 Micro1 materials frame `if.blackboard` as a real agent-work trace corpus, not a synthetic prompt set:

- Approved external shorthand: 3,800+ task IDs accumulated across 10 months.
- Curated catalogue: 49 selected entries across 10 thematic domains.
- Possible evaluation path: controlled NDA-gated evaluation batch before any broad export or rights discussion.
- High-value signal classes: trap propagation, root-cause falsification, calibrated partial claims, suspension with clean handoff, adversarial self-review, experiment design, multi-lane convergence, safety-gate reasoning, filing-grade IP precision, and institutional knowledge capture.
- June 2026 internal audit language says blackboard/signals data is meaningful but likely licensable only after redaction, normalization, client-data review, and methodology-leakage review.

**Commercial red line:** do not promise raw-ledger transfer, broad downstream rights, exclusivity, or full-event availability before scope, rights, redaction, and field-of-use controls are locked.

---

## Claim Register

### Supported

- `if.blackboard` is a coordination evidence surface for durable task, signal, checkpoint, and verification records.
- It is designed around append-only event discipline and derived task-state views.
- It supports multi-session continuity by making task state separate from chat memory.
- It is locally configured as an MCP-accessible remote service through the InfraFabric bundle.
- It has business value as real-world agent workflow data when curated and governed.

### Bounded

- Historical local canon says `/llm/blackboard/**` and `/llm/signals/**` were no-login review surfaces; current public/no-login availability is not verified on 2026-06-27.
- Signed-event coverage exists in June 2026 audit materials, but current coverage was not remeasured in this pass.
- Hash-closeout patterns are documented; do not assume every historical record has full hash/evidence closure.
- "Append-only" means workflow mutation discipline; it is not the same claim as cryptographic immutability or distributed ledger durability.

### Do Not Claim

- No exactly-once delivery.
- No SIP, routing, or queue-correctness claim.
- No certification, SLA, safety, legal, or compliance conclusion by itself.
- No fleet/multi-host durability claim.
- No unrestricted licensability of the full raw ledger.
- No public no-login liveness claim until current endpoint behavior is resolved.

---

## Readiness Checklist

Before using `if.blackboard` as evidence for a serious claim:

- Current registry status is fetched or explicitly marked stale.
- Auth/publication posture for `/llm/blackboard/**` is known.
- Task event, session event, and signal event counts have timestamps.
- Signed-event coverage is measured for the relevant slice.
- Writer path is tested with a non-sensitive record.
- Derived views are confirmed to update after write.
- Search/export surface is verified for the intended consumer.
- Missing context, missing DoD, and missing evidence queues are reviewed.
- Client/confidential data risk is classified before export.
- Methodology-leakage risk is reviewed before any data sale or external sample.

---

## Open Questions

- Is the current redirect to sign-in intentional publication hardening, a routing regression, or an auth-wall change?
- What is the current `if.registry.json` row for `if.blackboard` after March 2026?
- ~~What writer CLI/tool path should be treated as canonical today?~~ **Resolved 2026-07-01:** `if-cli blackboard api ...` against the hosted `https://api.infrafabric.io` API; bare legacy local writer verbs fail closed.
- What event schemas are stable enough for external evaluation batches?
- Which fields require redaction before Micro1-style sharing?
- Does the Relay Ledger storage binding from the HEPHAISTOS Phase 2 roadmap exist yet?
- What is the current signed-event coverage for task, session, and signal stores?
- What retention and field-of-use terms should bind any ongoing delta feed?

---

## Sources

- [[InfraFabric Architecture]]
- [[InfraFabric MCP Stack — Remote Bundles]]
- [[InfraFabric R0.5 Rollout — Hosted API Migration (2026-06-29 to 2026-06-30)]]
- [[Stacklight-owner-explainer]]
- `governance/global/AGENTS.md`
- `governance/hephaistos/PHASE-2-INTEGRATION-ROADMAP.md`
- `governance/hephaistos/BOWIE.md`
- `raw sources/infrafabric-archive/if.blackboard Full Explainer v1.3 (Multi-Audience, Split-Boundary Strict).md`
- `/home/martin/infra/micro1/4164-pharos-micro1-operational-data-licensing-blackboard-iftrace-assessment-2026-06-08.md`
- `/home/martin/infra/micro1/docs/4391-infrafabric-blackboard-micro1-explainer-2026-06.md`
- `/home/martin/infra/micro1/camilo-meeting-cheat-sheet.md`
- `/home/martin/apps/stacklight/documentation/agents/5009-if-blackboard-postgres-authority-runbook-2026-06-29.md`
- `/home/martin/apps/stacklight/documentation/agents/5011-stacklight-blackboard-mtl03-fresh-session-handover-2026-06-30.md`
- Checked on 2026-06-27: https://infrafabric.io/llm/blackboard/index.md.txt, https://infrafabric.io/llm/blackboard/tasks.search.json.txt, https://infrafabric.io/llm/signals/index.md.txt, https://infrafabric.io/llm/if.registry.json.txt
