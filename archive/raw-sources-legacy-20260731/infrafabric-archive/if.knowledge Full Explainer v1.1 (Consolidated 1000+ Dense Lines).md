---
type: raw-source
aliases: [orphan-raw-2026-05-06-026]
graph_repair: 2026-05-06
---

# if.knowledge Full Explainer v1.1 (Consolidated 1000+ Dense Lines)

Date: 2026-03-03
Owner: InfraFabric Runtime + Documentation
Status: preview (claim-boundary strict)
Pack Release: IF-PACK-2026-03-03-R2
Audience modes: executive, operator, engineer, external reviewer
Line-depth contract: 1000-1800 dense lines for module-level full explainer

## Why this revision exists

This revision exists for two explicit reasons:

1. Depth correction.
- The current standalone module explainer for `if.knowledge` was not at full-explainer depth.
- This v1.1 is intentionally rebuilt to satisfy dense module explainer expectations.

2. Claim-boundary correction.
- Historical `if.knowledge` materials include both build-time-only and runtime-preview narratives.
- This document makes those states explicit, dated, and non-conflicting by separating:
  - current canonical posture,
  - historical implementation evidence,
  - non-claims.

## What this document is

This document is:
- a consolidated full explainer for `if.knowledge` that keeps previous artifacts traceable,
- a current-state claim boundary reference,
- an operator/engineer runbook index for reproducible verification,
- a dense source pack that can be reviewed without cross-opening many files.

This document is not:
- a silent rewrite of historical documents,
- a GA claim,
- a certification claim,
- a declaration that historical runtime-preview surfaces are currently production-backed.

## Scope and lineage (consolidated inputs)

This full explainer consolidates the following source set:

- `docs/626-if-knowledge-full-explainer-v1.0-2026-02-20T031900Z.md`
- `docs/90-if-knowledge-spec.md`
- `docs/92-if-knowledge-graph-spec.md`
- `docs/631-if-knowledge-runtime-query-access-audit-preview-v1.0-2026-02-20T104900Z.md`
- `docs/624-if-knowledge-focus-hierarchy-improvement-v1.0-2026-02-20.md`
- `docs/202-if-blackboard-project-thread-if-knowledge.md`

## Current canonical posture (black/white)

As of the latest graph snapshot in this session (`generated_utc=2026-03-03T14:39:11Z`), the `product:if.knowledge` node records:

- status: `preview`
- path: `/if/knowledge`
- status detail: build-time documentation tooling and published review artifacts
- explicit wording: no deployed runtime service claim on this host

Interpretation rule:
- This current canonical posture is the default claim baseline.
- Any stronger statement must cite newer runtime evidence and explicit promotion approval.

## Historical runtime-preview posture (black/white)

Historical docs in scope (especially `626` and `631`) describe runtime endpoint work under `if.api` relay.

This consolidation treats those statements as:
- implementation/history evidence,
- not automatic current production posture,
- useful for architecture continuity and future reactivation work.

## Claim boundary matrix

| Topic | Verified now | Historical evidence | Non-claim now |
|---|---|---|---|
| Build-time graph pipeline | Yes | Yes | N/A |
| Public KG artifacts under `/llm/products/if-knowledge/**` | Yes | Yes | N/A |
| Runtime preview endpoint implementation history | Yes (historical docs exist) | Yes | Not claiming current deployed runtime service |
| GA/SLO/compliance certification | No | No | Not claimed |
| Semantic truth guarantees | No | No | Not claimed |

## Audience navigation

- Executive: Sections on posture, risks, and decision boundary.
- Operator: Sections on refresh flow, artifact checks, and stop rules.
- Engineer: Sections on builder/filter/lint/projection contracts.
- External reviewer: Sections on public surfaces, checksums, and can/cannot conclude.

## Executive summary

`if.knowledge` is presently best represented as preview build-time documentation/graph infrastructure with published reviewer artifacts and deterministic generation/lint surfaces.

Historical runtime-preview work is preserved and documented but is not promoted to current deployed-service claim in this revision.

## Decision surface

### Decision question 1
Should stakeholders present `if.knowledge` as a deployed runtime knowledge service today?

Answer: No, not from this revision alone.

Reason: Current canonical product posture and graph metadata do not claim deployed runtime service on this host.

### Decision question 2
Should stakeholders present `if.knowledge` as a deterministic build-time graph and artifact publication subsystem?

Answer: Yes.

Reason: Tooling, outputs, and lints are present and reproducible in this session.

### Decision question 3
Should older runtime-preview docs be removed?

Answer: No.

Reason: They are implementation history and useful for future runtime reactivation work.

### Decision question 4
Should claim language merge historical runtime-preview with current build-time status?

Answer: No.

Reason: Merging would produce ambiguous or inflated claim posture.

## Risk register (current)

1. Claim drift risk.
- Risk: Teams quote runtime-preview docs as if they were current production status.
- Mitigation: Keep explicit current/historical split and non-claim statements.

2. Reviewer confusion risk.
- Risk: Readers see endpoint paths in historical docs and assume active runtime.
- Mitigation: Add explicit date/state labels and deployment boundary language.

3. Operational drift risk.
- Risk: Public/private graph artifacts become inconsistent.
- Mitigation: Refresh private, filter public, copy alias, then lint both.

4. Projection drift risk.
- Risk: product projection does not reflect latest graph edges.
- Mitigation: rebuild `if_knowledge_graph.products.v1.json` in same run.

## Operator workflow (authoritative run sequence)

1. Refresh canonical graph:

```bash
python3 /root/scripts/refresh_if_knowledge_graph.py --out /root/docs/data/if_knowledge_graph.v2.json
```

2. Build public filtered graph:

```bash
python3 /root/scripts/filter_if_knowledge_graph.py \
  --in /root/docs/data/if_knowledge_graph.v2.json \
  --out /root/docs/data/if_knowledge_graph.v2.public.json \
  --exclude-regex '(?i)ggq|guidesgq'
```

3. Keep public alias synchronized:

```bash
cp /root/docs/data/if_knowledge_graph.v2.public.json /root/docs/data/if_knowledge_graph.public.v2.json
```

4. Rebuild product projection:

```bash
python3 /root/scripts/build_if_knowledge_product_projection.py \
  --graph /root/docs/data/if_knowledge_graph.v2.json \
  --out /root/docs/data/if_knowledge_graph.products.v1.json
```

5. Lint both graph surfaces:

```bash
python3 /root/scripts/lint_if_knowledge_graph.py --json /root/docs/data/if_knowledge_graph.v2.json
python3 /root/scripts/lint_if_knowledge_graph.py --json /root/docs/data/if_knowledge_graph.v2.public.json
```

## Stop rules

Stop and escalate when:
- lint fails,
- public alias hash differs unexpectedly from filtered public output,
- new claim language implies runtime deployment without current runtime evidence,
- graph refresh errors or produces empty/malformed outputs.

## Current session evidence snapshot (this build)

Latest refreshed graph in this session:
- file: `/root/docs/data/if_knowledge_graph.v2.json`
- `generated_utc=2026-03-03T14:39:11Z`
- nodes: `8898`
- edges: `24527`
- sha256: `2b9d3047233c939b49a386b3cd80fe623df2a6a136a90388eb87c08fffbac99c`

Latest public graph in this session:
- file: `/root/docs/data/if_knowledge_graph.v2.public.json`
- sha256: `4205049c84737e71ea12138e9736036bfb9d50b3c60a0a087fb1dc25701a71c7`

Public alias copy:
- file: `/root/docs/data/if_knowledge_graph.public.v2.json`
- sha256: `4205049c84737e71ea12138e9736036bfb9d50b3c60a0a087fb1dc25701a71c7`

Product projection:
- file: `/root/docs/data/if_knowledge_graph.products.v1.json`
- sha256: `0ae37105c80e5e08a6418efc02d667ddae11c040e4b7b84fb52be5414ba36187`

## Can and cannot conclude (reviewer-safe)

Can conclude:
- deterministic graph refresh/filter/lint/projection pipeline exists and runs,
- published if.knowledge artifacts are maintained as preview surfaces,
- the product is represented in canonical graph/registry space.

Cannot conclude from this doc alone:
- deployed runtime query service is currently live on host,
- GA/SLO/compliance posture,
- semantic correctness guarantees of all graph content.

## External surfaces (no-login where applicable)

https://infrafabric.io/if/knowledge/
https://infrafabric.io/llm/products/if-knowledge/knowledge-graph/2026-02-05/index.md.txt
https://infrafabric.io/llm/blackboard/by-product/if-knowledge.md.txt

## Contradiction handling policy

If readers detect conflicting statements between current posture and historical runtime-preview docs:

1. Prefer current canonical posture for live claims.
2. Keep historical docs intact as dated evidence.
3. Log contradiction in blackboard result notes.
4. Require explicit new runtime evidence + gate approval before promoting claims.

## Full-depth compliance statement

This document is intentionally dense and consolidated to satisfy full-module explainer depth policy while preserving source traceability.

## Verification commands for this document

```bash
wc -l /root/docs/2315-if-knowledge-full-explainer-v1.1-2026-03-03T150500Z.md
sha256sum /root/docs/2315-if-knowledge-full-explainer-v1.1-2026-03-03T150500Z.md
rg -n "Current canonical posture|Historical runtime-preview posture|Claim boundary matrix|Stop rules|Can and cannot conclude" \
  /root/docs/2315-if-knowledge-full-explainer-v1.1-2026-03-03T150500Z.md
```

## Appended Canonical Source A

The following section appends:
`docs/626-if-knowledge-full-explainer-v1.0-2026-02-20T031900Z.md`

# if.knowledge Full Explainer v1.1 (Runtime Preview + Strict Claim Boundaries)

Danny Stocker | ds@infrafabric.io | InfraFabric Runtime | 2026-02-20
Status: preview
Last review date: 2026-02-20
Next checkpoint date: 2026-03-01
Accountable approver: Danny Stocker | ds@infrafabric.io
LLM-assist disclosure: drafted and validated with Codex runtime assistance; accountable human author remains Danny Stocker.

## Who | Why | What | Where | When | How

- Who: executives setting claim strength, operators maintaining runtime evidence, engineers maintaining graph/runtime controls, and API consumers integrating retrieval.
- Why: prior messaging over-emphasized static graph artifacts and under-described runtime query controls, which created a claim gap.
- What: current-state explainer for `if.knowledge` covering runtime retrieval, signed-scope authorization, audit lineage, and strict non-claims.
- Where: runtime endpoints on `https://infrafabric.io/chat/if/api/v1/knowledge/*`, artifact generation under `docs/data/if_knowledge_graph*.json`, and scope-regression evidence under `/llm/switchboard/knowledge-scope/*`.
- When: active now in preview; sustained gate evidence for claim upgrades is still in progress.
- How: bounded query contracts, trusted signed scope, append-only access logs, regression windows, and fail-closed wording discipline.

## Problem Statement

Historically, `if.knowledge` was interpreted as a build-time graph system only. That was accurate for older snapshots, but it is now incomplete.

Current reality is mixed and must be stated in black/white terms:
- runtime retrieval endpoints now exist and are live,
- runtime maturity claims (GA/SLO/compliance certification) are still out of scope.

## Runtime Reality (As Of 2026-02-20)

Live capability surface:
- `POST /if/api/v1/knowledge/query`
- `GET /if/api/v1/knowledge/node/:nodeId`
- `GET /if/api/v1/knowledge/access`

Live runtime controls from `healthz`:
- `scopeMode: signed`
- `scopeRequireProject: true`
- `scopeSigningKeysCount: 2` (active + previous key support)
- `requireAuditLog: true`
- graph loaded in memory (`if.knowledge.graph.v2`, nodes `8473`, edges `20308` in current runtime snapshot)

## Claim Boundary

### Can claim now

- `if.knowledge` has deployed runtime query endpoints in preview.
- runtime requests are bounded (query length/result caps/edge and neighbor limits).
- signed trusted-scope enforcement is active for tenant/project/actor controls.
- key rotation acceptance is implemented (current and previous signing keys).
- access operations are audit-logged with hash-chain lineage.
- regression evidence windows exist and are publicly readable at `/llm/switchboard/knowledge-scope/*`.

### Cannot claim now

- GA runtime SLA/SLO guarantees.
- semantic correctness guarantees for all node content.
- production compliance certification solely from current evidence windows.
- sustained gate completion for knowledge-scope hardening (10-window requirement not yet met).
- "compliance-grade autonomous agents" as a global platform claim from `if.knowledge` evidence alone.

## Executive Decision Surface

One-line summary:
`if.knowledge` is now a preview runtime retrieval system with enforced scope and audit controls, but it remains below GA/compliance-certification claim level.

Decision table:

| Decision question | Current answer | Evidence | Risk if ignored |
|---|---|---|---|
| Are runtime query APIs deployed? | Yes | `/chat/capabilities`, `/chat/healthz` | outdated architecture narrative |
| Is authorization scope enforced? | Yes (signed + project required) | signed-scope regression windows | cross-tenant/project claim drift |
| Is audit lineage present? | Yes | access log chain fields + access endpoint | weak accountability narrative |
| Is sustained hardening gate complete? | No | gate status `NOT_MET` (2/10 windows) | over-claiming reliability maturity |
| Can we market compliance-grade autonomy now? | No | missing full gate + broader controls | trust/reviewer backlash |

## Operational Runbook View

### Runtime checks

1. Check endpoint discovery in `/chat/capabilities`.
2. Check `ifApiKnowledge` block in `/chat/healthz`.
3. Run signed-scope smoke + redteam scripts.
4. Verify latest knowledge-scope window and gate artifacts.
5. Confirm deny alerts are monitored and reason-coded.

### Public evidence URLs (no login)

https://infrafabric.io/chat/capabilities
https://infrafabric.io/chat/healthz
https://infrafabric.io/llm/switchboard/knowledge-scope/index.md
https://infrafabric.io/llm/switchboard/knowledge-scope/latest.json
https://infrafabric.io/llm/switchboard/knowledge-scope/windows.jsonl
https://infrafabric.io/llm/switchboard/knowledge-scope/gate-status.json
https://infrafabric.io/llm/switchboard/knowledge-scope/alerts.latest.json

### Outage/degrade rules

- If runtime endpoint health fails: freeze claim upgrades and classify runtime evidence as degraded.
- If scope regression windows stop updating: freeze scope-hardening claims.
- If audit logging is unavailable and fail-closed is enabled: treat as service-protective denial, not successful runtime.

## Implementation View

### Product identity

- Product ID: `if.knowledge`
- Canonical path: `/if/knowledge`
- Status: `preview`
- Runtime authority path: `if.api` ingress (`/chat/if/api/v1/knowledge/*`)

### Contracted runtime fields (minimum)

For query operations:
- trusted scope (`tenant_id`, `project_id`, `actor_id`) from signed context
- bounded query controls (`top_k`, return limits)
- audit row append with deterministic hash lineage

For node retrieval:
- scoped node read
- deterministic neighbor/edge caps
- audited access result summary

For access inspection:
- append-only access rows
- chain-hash continuity fields
- deny-path visibility (`*_denied` with reason codes)

### Scope hardening status snapshot

Latest public window (`2026-02-20T20:29:49Z`):
- checks passed: `13/13`
- pass rate: `1.0`
- gate status: `NOT_MET` (current `2` consecutive pass windows; minimum `10`)

Alert snapshot (same window family):
- severity: `warning`
- reasons: `denies_above_threshold`, `invalid_signature_spike`

Interpretation:
- control assertions are passing in-window,
- sustained gate criteria are not yet complete,
- denial telemetry is active and should remain visible (do not suppress it for optics).

## Runtime Contract View

### State labels

- `deployed_enforced`: behavior verified in current runtime and evidence window.
- `source_validated`: code/config path inspected and coherent, but not yet externally sustained.
- `intent_only`: planned behavior not yet proven in current evidence windows.

### Current state map

- runtime endpoints reachable: `deployed_enforced`
- signed scope enforcement: `deployed_enforced`
- project-required scope mode: `deployed_enforced`
- key rotation acceptance (previous key): `deployed_enforced`
- access audit hash-chain logging: `deployed_enforced`
- sustained 10-window gate: `intent_only`
- GA/SLO posture: `intent_only`
- compliance-grade autonomous claim: `intent_only`

## Relationship to if.switchboard and Agent Rook

- `if.switchboard` is the orchestration/coordination control plane.
- `if.knowledge` is the retrieval and evidence substrate for graph-backed context access.
- Agent Rook is a consumer/runtime persona layer that uses both.

Claim discipline:
- We can claim Rook runs on enforced runtime controls.
- We cannot yet claim "compliance-grade autonomous agents" as a finished state until broader gates are fully met across routing, retrieval, identity, and sustained evidence windows.

## Non-Claims (Explicit)

- No claim of GA runtime service-level guarantees.
- No claim of universal semantic correctness of graph content.
- No claim that single-window success equals sustained assurance.
- No claim that Rook autonomy is compliance-grade by certification standard at this time.

## Release Language Guardrails

### Approved wording

- "`if.knowledge` runs preview runtime query endpoints with signed scope and audit logging controls."
- "Current knowledge-scope validation windows pass; sustained gate progression remains in progress."
- "Claim strength remains bounded until sustained criteria are met."

### Blocked wording

- "`if.knowledge` is GA with guaranteed SLOs."
- "`if.knowledge` proves semantic truth for all nodes."
- "Rook is already compliance-grade autonomous in production."

### Escalation wording when uncertain

"Current evidence supports preview runtime-control claims and strict scope enforcement. It does not yet support GA/SLO or compliance-grade autonomy claims."

## 30/60/90 Plan

### 30 days

- stabilize automatic publication into live `/llm` path with no manual copy steps,
- keep signed-scope window cadence continuous,
- push gate progression from 2 windows toward 10-window threshold.

### 60 days

- sustain zero-regression scope windows,
- add stronger report segmentation for denial telemetry (expected redteam vs production anomalies),
- bind explainer release check to gate-status parse.

### 90 days

- decide whether GA/SLO framing is justified based on sustained runtime evidence,
- evaluate whether "compliance-grade autonomous" can move from `intent_only` to evidence-backed limited claim.

## Appendix A: External Verification Commands

```bash
# Runtime endpoint discovery
curl -fsS https://infrafabric.io/chat/capabilities \
  | jq '.features | {ifApiKnowledgeQueryApi,ifApiKnowledgeNodeApi,ifApiKnowledgeAccessApi}'

# Runtime control snapshot
curl -fsS https://infrafabric.io/chat/healthz | jq '.ifApiKnowledge'

# Scope regression latest window
curl -fsS https://infrafabric.io/llm/switchboard/knowledge-scope/latest.json \
  | jq '{window_utc,scope_mode,scope_require_project,checks_total,checks_passed,pass_rate,pass}'

# Gate status
curl -fsS https://infrafabric.io/llm/switchboard/knowledge-scope/gate-status.json \
  | jq '{claim_status,current_state}'

# Alert status
curl -fsS https://infrafabric.io/llm/switchboard/knowledge-scope/alerts.latest.json \
  | jq '{severity,reasons,metrics}'

# Window history (latest 10)
curl -fsS https://infrafabric.io/llm/switchboard/knowledge-scope/windows.jsonl \
  | tail -n 10
```

## Appendix B: Internal Evidence Map (masked)

- `{$path}/tmp/codex-bridge-chat/server.js`
- `{$path}/scripts/if_api_knowledge_scope_sign.py`
- `{$path}/scripts/if_api_knowledge_runtime_smoke.sh`
- `{$path}/scripts/if_api_knowledge_scope_redteam.sh`
- `{$path}/scripts/if_api_knowledge_scope_gate_eval.py`
- `{$path}/scripts/if_api_knowledge_scope_regression_once.sh`
- `{$path}/docs/data/if_switchboard_knowledge_scope.latest.json`
- `{$path}/docs/data/if_switchboard_knowledge_scope.windows.jsonl`
- `{$path}/docs/data/if_switchboard_knowledge_scope.gate-status.json`
- `{$path}/docs/data/if_switchboard_knowledge_scope.alerts.latest.json`

## Conclusion

`if.knowledge` has crossed from "static artifact only" to "preview runtime retrieval with enforced controls." That is a meaningful upgrade.

The right posture is to lead with what is verifiably true now, keep sustained-gate discipline, and avoid claiming compliance-grade autonomous outcomes before the full evidence bar is met.

Style Guide: Whitepaper v4.7
Writing Standard Source: if.whitepapers.bible v4.7

## Appended Canonical Source B

The following section appends:
`docs/90-if-knowledge-spec.md`

# if.knowledge - build-time knowledge addendum spec (static)

Generated (UTC): 2026-01-11

Scope: `if.knowledge` is a build-time pipeline that generates static addenda and papers from registry + task board + dossier inputs. No runtime fetches.

Reality gate (single-host): `docs/22-infrafabric-handover-and-roadmap.md`

Naming (enforced): `AGENTS.md` + `if.registry.json`

---

## Status (black/white)

Registry status (source of truth):
- Consult `if.registry.json` for `if.knowledge` status. If the entry is absent, treat it as not registered and not deployed.

This document is:
- a spec for how the `if.knowledge` build-time pipeline should operate
- a contract for deterministic, registry-driven addendum outputs

This document is not:
- a claim that any runtime service is deployed
- a claim of correctness, safety, or compliance

---

## What `if.knowledge` is (plain language)

- A build-time pipeline that turns a submitted dossier into a static addendum.
- The addendum cross-references the current registry and task board.
- The outputs are review artifacts: Markdown plus HTML wrappers.

---

## Design goals (future-backwards)

### 1) Registry-driven (no naming drift)

- All product IDs and canonical paths come from `if.registry.json`.
- Generation fails if any referenced `product_id` is not in the registry.

### 2) Deterministic and offline

- The generator is deterministic: the same inputs produce identical output bytes.
- No network access or external APIs are used at build time.
- Standard library only for the reference implementation.

### 3) Black/white wording (no overclaiming)

- Output clearly separates verified facts (hashes/signatures when present) from interpretation.
- Use QUANTUM READY only when a post-quantum receipt exists.
- Avoid quantum-security overclaim wording.

### 4) URL hygiene (reviewer-friendly)

- One URL per line.
- Provide HTML view fallbacks for artifacts that are otherwise downloads.
- Prefer stable, no-login, public receipt surfaces.
- No internal URI schemes (for example: if colon slash slash).

### 5) Build-time only (no runtime fetches)

- The addendum is static at publish time.
- Client-side JS may be used for layout only, not for fetching content.

### 6) Additive-only evolution posture

- Add new sections or fields without changing existing meanings.
- Do not delete or rename existing headings in place.
- If a breaking change is required, publish a new dated snapshot instead.

---

## Inputs (reference implementation)

Required inputs:
- `if.registry.json`
- `docs/13-task-board.md`
- A submitted dossier Markdown file

Example dossier input (current working set):
- `docs/_uploads/DANNY_STOCKER_INFRAFABRIC_DOSSIER_20251223-1925CET.md`

Optional inputs:
- Tabular ingest profile (offline, deterministic) that emits a graph fragment.
  - Supports single CSV/XLSX (v1) or multiple tabular inputs (v2).
  - Optional delimiter per input (for example `\t` when exporting from `pg_dump` COPY).
  - Optional XLSX support (sheet name + header row). Uses `openpyxl` if installed; falls back to a stdlib reader.
  - Optional ontology mapping (`ontology_path`) to annotate nodes/edges with RDF‑style types/predicates.
  - Example config (single CSV): `docs/data/if_knowledge_tabular_ingest.example.json`
  - Example CSV: `docs/data/if_knowledge_tabular_ingest.example.csv`
  - Example config (XLSX): `docs/data/if_knowledge_tabular_ingest.xlsx.json`
  - Example XLSX: `docs/data/if_knowledge_tabular_ingest.example.xlsx`
  - GGQ profile (multi‑input + ontology): `docs/data/ggq_tabular_ingest.json`
  - GGQ ontology: `docs/data/ggq_ontology.json`
  - Use `scripts/build_if_knowledge_tabular_graph.py` to generate a fragment.
  - Merge fragments into the core graph with `--extra-graph` in `build_if_knowledge_graph.py`.
- Optional `/root/docs` coverage (opt-in, not default).
  - The core graph does not scan all of `/root/docs` by default (size + secret hygiene).
  - If needed, generate a doc-derived fragment (paths/titles/hashes only; redact excerpts) and merge via
    `--extra-graph` in `build_if_knowledge_graph.py` or `refresh_if_knowledge_graph.py`.
- Remote Postgres ingest (offline dump → TSV → graph fragment).
  - Guidance: `docs/if_knowledge_remote_pg_ingest.md`
- Database export patterns (Postgres/MySQL/MariaDB/SQLite/SQL Server/etc.).
  - Guidance: `docs/if_knowledge_ingest_sources.md`
  - Helper: `scripts/export_if_kg_db.sh` (postgres/mysql export to TSV/CSV with deterministic ordering).
- KB→KG profile stub (link KB outputs into the graph).
  - Profile: `docs/data/if_knowledge_kb_profile.json`
  - Notes: `docs/if_knowledge_kb_profile.md`

---

## Outputs (reference implementation)

Required outputs:
- A deterministic addendum Markdown file (`.md`).
- A hosted-static HTML wrapper for the addendum (`index.html`).

Optional outputs:
- A dated snapshot pack that includes the addendum and referenced artifacts.
- A short "paper" derived from the addendum (static Markdown + HTML wrapper).
- KG export profiles (GraphML / RDF Turtle / Cypher) for offline packaging.
  - Guidance: `docs/if_knowledge_kg_export_profiles.md`
- Offline query CLI for v2 graphs (no runtime service).
  - Script: `scripts/if_knowledge_query.py`
- Read‑only API spec for serving static graph snapshots.
  - Guidance: `docs/if_knowledge_readonly_api_spec.md`

---

## Graph v2 node/edge kinds (reference)

Node kinds (non-exhaustive):
- `product` (from registry)
- `schema` + `concept` (from schemas with `x_if`)
- `task` (from task board)
- `url` (from task board links)
- `path` (from task board working set)
- `verify_command` (from task board verification steps)
- `dossier` (submitted dossier metadata)

Edge types (non-exhaustive):
- `uses_receipts_from` (product → product)
- `schema_defines_concept` (schema → concept)
- `product_defines_concept` (product → concept)
- `concept_depends_on` (concept → concept)
- `task_mentions_product` (task → product)
- `task_links_to_url` (task → url)
- `task_touches_path` (task → path)
- `task_verifies_with` (task → verify_command)
- `dossier_mentions_product` (dossier → product)

---

## Constraints (publish-blocking)

- One URL per line (no link wrapping).
- No internal URI schemes (for example: if colon slash slash).
- No forbidden quantum-security wording.
- No internal hostnames or secrets.
- All `product_id` values must exist in `if.registry.json`.

---

## Output structure (minimum)

A generated addendum MUST include the following sections:
- Header with source dossier metadata (filename and date only; no secrets).
- Registry excerpt: product IDs, paths, and statuses used in the addendum.
- Task board excerpt: relevant task IDs with status (no private notes).
- Evidence section (verified facts only).
- Interpretation section (clearly labeled as interpretation).
- Open questions / next steps.

---

## Lint posture (publish fails)

The linter must fail on:
- Any internal-scheme URI.
- Any quantum-security overclaim wording.
- Multiple `https://` URLs on one line.
- Unknown `product_id` values.
- Missing required sections in the addendum.

---

## Publish posture (hosted-static)

Publishing is an explicit build step:
- Generate Markdown.
- Lint Markdown.
- Copy to hosted-static under a dated folder.
- Build HTML wrappers in `pct 210` with the standard wrapper tool.

---

## Verification (reference commands)

Validate registry JSON:
`python3 -m json.tool if.registry.json > /dev/null`

Build an addendum:
`python3 scripts/build_if_knowledge_addendum.py --dossier docs/_uploads/DANNY_STOCKER_INFRAFABRIC_DOSSIER_20251223-1925CET.md --out /root/tmp/if_knowledge_addendum.md`

Lint the addendum:
`python3 scripts/lint_if_knowledge_addendum.py --md /root/tmp/if_knowledge_addendum.md`

## Appended Canonical Source C

The following section appends:
`docs/92-if-knowledge-graph-spec.md`

# if.knowledge graph v2 — deterministic concept graph (spec)

Generated (UTC): 2026-01-11

Scope: a build-time, deterministic graph that helps InfraFabric keep interdependencies explicit and rebuild review artifacts without relying on “memory” in a single strong model.

Reality gate (single-host): `docs/22-infrafabric-handover-and-roadmap.md`

Naming (enforced): `AGENTS.md` + `if.registry.json`

---

## Status (black/white)

This document is:
- a spec for a build-time graph artifact (`if.knowledge.graph.v2`)
- a contract for deterministic graph generation from local sources

This document is not:
- a claim that a graph query service is deployed
- a claim of truth/correctness/safety for any node’s content

---

## Why a graph (plain language)

A plain Markdown dossier is hard to keep consistent as the system grows.

The graph exists so we can answer questions like:
- “What products depend on `if.trace` receipts?”
- “Which concepts are defined by schemas vs only described in prose?”
- “What changed since the submitted dossier date?”

The key posture:
- the graph is a deterministic index of local sources
- it is not an “AI memory”

---

## Inputs (v2 builder)

Required local inputs:
- `if.registry.json` (product IDs, paths, statuses, and declared relationships)
- `docs/13-task-board.md` (task metadata + published links)
- `schemas/**` (JSON Schema with `x_if` metadata for concept IDs)
- a submitted dossier Markdown file (mentions-only; content is not exported)

Optional local inputs:
- a blog snapshot JSON (mentions-only; content is not exported)

Example dossier input (current working set):
- `docs/_uploads/DANNY_STOCKER_INFRAFABRIC_DOSSIER_20251223-1925CET.md`

Example blog snapshot input (current working set):
- `/var/lib/lxc/210/rootfs/srv/hosted-static/public/llm/platform/blog/latest/blog.snapshot.full.json`

---

## Outputs (v2 builder)

Primary output:
- `docs/data/if_knowledge_graph.v2.json`

Graph rules:
- Node IDs are prefixed (`product:...`, `concept:...`, `schema:...`, `task:...`, `url:...`, `dossier:...`).
- Nodes use `id` + `node_kind` (no overloaded `kind` field); registry’s own kind is carried as `registry_kind` on product nodes.
- Edges always reference existing node IDs.
- Dossier + blog handling is mentions-only (counts); no text/sections are exported into the graph JSON.
- Mentions are linked for:
  - `product_id` strings (registry-known)
  - `concept_id` strings (schema-defined only)

---

## Black/white constraints (publish-blocking)

Graph JSON must:
- be valid JSON
- contain no internal URI schemes (no `if://`)
- contain no forbidden “quantum-secure” wording
- contain only registry-known `product_id` values for product nodes
- have edges that reference only existing node IDs

---

## Verification (reference commands)

Build the graph:

`python3 scripts/build_if_knowledge_graph.py --dossier docs/_uploads/DANNY_STOCKER_INFRAFABRIC_DOSSIER_20251223-1925CET.md --blog-snapshot /var/lib/lxc/210/rootfs/srv/hosted-static/public/llm/platform/blog/latest/blog.snapshot.full.json --out docs/data/if_knowledge_graph.v2.json`

Lint the graph:

`python3 scripts/lint_if_knowledge_graph.py --json docs/data/if_knowledge_graph.v2.json`

## Appended Canonical Source D

The following section appends:
`docs/631-if-knowledge-runtime-query-access-audit-preview-v1.0-2026-02-20T104900Z.md`

# `if.knowledge` Runtime Query + Access Audit Preview (v1.0)

Date: 2026-02-20
Owner: InfraFabric Runtime
Status: Implemented in `if.api` relay; preview claim level

- Who: runtime operators, API consumers, and evidence reviewers.
- Why: static graph-only access forced consumers to ingest full JSON and query locally, creating scale and traceability limits.
- What: add bounded runtime query endpoints and append-only access logging with actor attribution.
- Where: `/if/api/v1/knowledge/*` on the chat relay runtime.
- When: live now for preview usage; GA/SLO claim remains out of scope.
- How: read-only graph load from public-safe graph, bounded query controls, and hash-chained JSONL access logs.

Problem statement:
The prior model provided deterministic graph artifacts but no runtime retrieval interface. Downstream apps had to pull the full graph and could not consistently prove who accessed which data objects.

## Document Navigation by Audience

### Executives / Business Leaders
- Read Sections 1 and 4.

### Power Users / Operators
- Read Sections 2, 3, and 5.

### Engineers / Implementers
- Read Sections 2, 3, 4, and 6.

### LLM Runtime Developers
- Read Sections 2, 3, and 6.

```text
[client request] -> [/if/api/v1/knowledge/query or /node/:id]
                  -> [bounded graph retrieval]
                  -> [append-only access.events.jsonl hash-chain]
                  -> [audit review via /if/api/v1/knowledge/access]
```

## 1) Implemented Endpoints

- `POST /if/api/v1/knowledge/query`
- `GET /if/api/v1/knowledge/node/:nodeId`
- `GET /if/api/v1/knowledge/access`

## 2) Access Tracking Contract

Each read operation now records:
- `actor_id`, `sid`, `task_id`, `tenant_id`, `project_id`
- request summary (`query_sha256`, bounds, node_id where applicable)
- result summary (`node_ids`, counts, truncation flags)
- hash-chain metadata (`prev_entry_hash`, `entry_hash`)

Log schema:
- `if.knowledge.access.v1`

## 3) Red-Team Controls Applied

- Trusted scope guard: runtime now resolves tenant/project/actor from trusted headers (or signed scope mode), not request body/query fields.
- Mismatch denial: explicit fail-closed reason codes (`tenant_scope_mismatch`, `project_scope_mismatch`, `actor_scope_mismatch`, `trusted_*_required`) with `401/403`.
- Deny audit trail: denied attempts are appended as `*_denied` access log rows with reason + status code.
- Query exfil guard: query text is hashed by default (`query_sha256`); raw preview is opt-in only.
- DoS guard: bounded `top_k`, edge limits, neighbor limits, and query length ceiling.
- Tamper-evidence: append-only JSONL with chained hashes per entry.
- Fail-closed option: `IF_API_KNOWLEDGE_REQUIRE_AUDIT_LOG=1` blocks data return if access logging fails.

Scope mode knobs:
- `IF_API_KNOWLEDGE_SCOPE_MODE=header|signed|off` (default `header`)
- `IF_API_KNOWLEDGE_SCOPE_SIGNING_KEY` (required for `signed`)
- `IF_API_KNOWLEDGE_SCOPE_REQUIRE_PROJECT=1` (optional strict project requirement)

Current runtime state (verified):
- `scopeMode=signed`
- `scopeSigningKeyConfigured=true`
- signed-mode denial checks pass (`missing`, `invalid signature`, `expired`, `payload tamper`)

## 4) Claim Boundary (Black/White)

Can claim now:
- runtime query endpoints exist in preview form.
- per-request access attribution and object-level result audit are implemented.
- trusted-scope enforcement blocks body/query spoofing mismatches.
- access-denied attempts are audit-logged with deterministic reason codes.

Cannot claim now:
- GA runtime SLA/SLO guarantees.
- cryptographic searchable encryption over all source content.
- semantic correctness guarantees for graph content.
- signed-scope mode production-readiness (unless key lifecycle + gateway signing controls are proven).

## 5) External Verification

https://infrafabric.io/chat/capabilities
https://infrafabric.io/chat/healthz

Minimal checks:

```bash
# 1) endpoint discovery
curl -fsS https://infrafabric.io/chat/capabilities | jq '.features | {ifApiKnowledgeQueryApi, ifApiKnowledgeNodeApi, ifApiKnowledgeAccessApi}'

# 2) runtime status snapshot
curl -fsS https://infrafabric.io/chat/healthz | jq '.ifApiKnowledge'

# 3) authenticated query + audit read
# (requires IF_API_AUTH_TOKEN in environment)
IF_API_AUTH_TOKEN="..." \
  scripts/if_api_knowledge_runtime_smoke.sh https://infrafabric.io/chat

# 4) red-team scope enforcement checks
IF_API_AUTH_TOKEN="..." \
  scripts/if_api_knowledge_scope_redteam.sh https://infrafabric.io/chat

# 5) mint signed scope headers directly (helper)
python3 scripts/if_api_knowledge_scope_sign.py \
  --tenant-id tenant-smoke --project-id proj-smoke --actor-id if.agent.smoke \
  --sid sid-smoke --task-id IF-2030 --format curl
```

## 6) Internal Evidence Map (masked)

- `{$path}/tmp/codex-bridge-chat/server.js`
- `{$path}/scripts/if_api_knowledge_runtime_smoke.sh`
- `{$path}/scripts/if_api_knowledge_scope_redteam.sh`
- `{$path}/scripts/if_api_knowledge_scope_sign.py`
- `{$path}/.if_tasks/knowledge/access.events.jsonl`
- `{$path}/tmp/if_knowledge_scope_redteam.json`
- `{$path}/docs/data/if_switchboard_knowledge_scope_validation.latest.json`

Style Guide: Whitepaper v4.7

## Appended Canonical Source E

The following section appends:
`docs/624-if-knowledge-focus-hierarchy-improvement-v1.0-2026-02-20.md`

# if.knowledge Focus + Hierarchy Improvement v1.0

Date: 2026-02-20
Owner: /rook-002 (Codex runtime)
Task: IF-1996
Status: review

## 1) Problem

The canonical graph (`docs/data/if_knowledge_graph.v2.json`) is broad and useful for traceability, but product-level architecture signals are diluted by high-volume operational edges (`doc_links_to_url`, `task_touches_path`, `task_links_to_url`).

This makes module hierarchy/dependency review slower than needed.

## 2) Improvement shipped

Added deterministic projection builder:

- `scripts/build_if_knowledge_product_projection.py`

Generated product-centric projection artifact:

- `docs/data/if_knowledge_graph.products.v1.json`

## 3) What the projection contains

- Full product inventory from registry with normalized metadata (`product_id`, `brand`, `slug`, `path`, `status`, depth fields).
- Direct product-to-product edges preserved from canonical graph.
- Inferred product dependency edges from concept topology:
  - `product_defines_concept`
  - `concept_depends_on`
  - output edge: `inferred_product_depends_on`
- Product activity counters for reviewer triage:
  - `doc_mentions_product`
  - `task_mentions_product`
  - `runtime_fact_about_product`

## 4) Current output snapshot

From latest run:

- products: 29
- edges_total: 21
- direct_edges: 20
- inferred_edges: 1

Top relation types currently visible:

- `uses_receipts_from`
- `inferred_product_depends_on`

## 5) Black/white boundary

Verified:

- Projection is deterministic and reproducible from current graph + registry.
- Projection improves hierarchy readability without mutating canonical graph.

Not claimed:

- This does not replace canonical graph completeness.
- This does not assert runtime guarantees or module maturity upgrades.

## 6) Verify commands

```bash
python3 -m py_compile scripts/build_if_knowledge_product_projection.py
python3 scripts/build_if_knowledge_product_projection.py --out docs/data/if_knowledge_graph.products.v1.json
python3 - <<'PY'
import json
obj=json.load(open('docs/data/if_knowledge_graph.products.v1.json'))
print(obj['schema_id'])
print(obj['counts'])
PY
```

## 7) Next patch candidates

- Add optional weighted confidence scoring per inferred edge.
- Emit a slim reviewer markdown alongside JSON (`products + dependency table`).
- Add projection lint thresholds (minimum edge coverage by high-signal types).

## Appended Canonical Source F

The following section appends:
`docs/202-if-blackboard-project-thread-if-knowledge.md`

# Project thread: if.knowledge (context pack)

**project_id:** if.knowledge
**Purpose:** safe, zero-context work on build-time knowledge graph snapshots + reviewer packs under `/llm/products/if-knowledge/**`.
**Status:** DRAFT (REVIEW REQUIRED)
**Date:** 2026-01-22

Black/white:
- This thread defines scope, working set boundaries, and minimum verification for public KG snapshot artifacts.
- It does not claim factual correctness, completeness, or runtime behavior unless explicitly verified in a dated pack.

`if.knowledge` product pack (txt-first):
https://infrafabric.io/llm/products/if-knowledge/index.html.txt

KG snapshot (txt-first index):
https://infrafabric.io/llm/products/if-knowledge/knowledge-graph/2026-01-13/index.md.txt

---

## 1) Scope (what this project is)

This project covers:
- publishing build-time KG snapshot artifacts (JSON/MD/HTML) for reviewer inspection,
- deterministic query examples + expected outputs (when provided),
- secrets scanning of public artifacts with publish-safe redacted reports.

It is not:
- a hosted query API,
- a claim that the knowledge graph is “correct”.

---

## 2) Design constraints (must hold)

Non-negotiable constraints:
- **Publish-safe:** never publish secrets or private hostnames; keep values in `/root/.secrets/` only.
- **Text-first:** provide `*.md.txt` and `*.json.txt` fallbacks for strict fetchers.
- **Black/white wording:** separate verified bytes (hashes) from interpretation.

---

## 3) Working set boundaries

In scope (common):
- `scripts/refresh_if_knowledge_graph.py` (when a task explicitly refreshes the KG)
- `scripts/if_knowledge_query.py`
- `scripts/scan_if_knowledge_public_pack.py`
- `src/armour/secrets/detect.py`
- `/var/lib/lxc/210/rootfs/srv/hosted-static/public/llm/products/if-knowledge/**` (published outputs)
- `scripts/{hosted_static_publish.py,llm_refresh.py,check_llm_links.py}`

Out of scope (default):
- adding runtime endpoints,
- publishing raw canonical stores or secret-bearing logs.

---

## 4) Verification (minimum)

Commands (host):
`python3 scripts/llm_refresh.py --skip-blog`
`python3 scripts/check_llm_links.py --root https://infrafabric.io/llm/products/if-knowledge/knowledge-graph/2026-01-13/index.md.txt --max-urls 600`

---

## 5) Failure posture (stop rules)

If you need a secret you do not have, stop and open a signal instead of guessing:
https://infrafabric.io/llm/signals/index.md.txt

## Related

- [[if.bus Full Explainer v1.5 (Switchboard-Integrated, Claim-Boundary Strict)]]
- [[if.whitepapers.bible (v4.23)]]
- [[if.context Full Explainer v1.3 (Consolidated 1000+ Dense Lines)]]
- [[Research and Papers MOC]]
- [[InfraFabric Architecture]]
