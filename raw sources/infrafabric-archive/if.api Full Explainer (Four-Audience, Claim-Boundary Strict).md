---
type: raw-source
aliases: [orphan-raw-2026-05-06-020]
graph_repair: 2026-05-06
---

# if.api Full Explainer (Four-Audience, Claim-Boundary Strict)

Danny Stocker | ds@infrafabric.io | InfraFabric Research | 2026-02-23
Status: review
Last review date: 2026-02-23
Next checkpoint date: 2026-03-08
Accountable and responsible approver: Danny Stocker | ds@infrafabric.io
LLM-assist disclosure: drafted and validated with Codex runtime assistance; accountable human author remains Danny Stocker.

## Who | Why | What | Where | When | How

- Who: executives approving release language, operators maintaining preview posture, engineers implementing adapters and contracts, and LLM runtime developers integrating envelope outputs.
- Why: keep `if.api` externally understandable without implying runtime guarantees that are not currently committed.
- What: a full explainer for `if.api` with black/white boundaries across adapter inventory, demo evidence, and runtime claim posture.
- Where: `/if/api/`, registry surfaces, locked deep-dive packs (versioned snapshots that are frozen in place and superseded by new files), adapter specs under `docs/data`, and schema files under `schemas/if-api`.
- When: immediate use for release/governance wording, adapter coverage decisions, and phased roadmap execution.
- How: registry-first wording, no-login evidence links, explicit non-claims, and fail-closed publication gates.

## Problem statement

`if.api` is the InfraFabric integration layer for external API (Application Programming Interface) systems. The recurring failure mode is claim collapse across three distinct realities:
- adapter inventory and contract assets in source,
- no-login demo and deep-dive publication surfaces,
- external runtime endpoint commitments.

If these are blurred, preview posture is overstated as General Availability (GA) and reviewer trust breaks.

Concrete collapse example:
- A reviewer sees a reachable GitHub webhook demo and infers a publicly committed webhook ingestion runtime with SLA/SLO terms. That commitment is not currently claimed.

## Goal

Enable a skeptical reviewer to answer, in black/white terms:
- what `if.api` proves today,
- what is inventory/demo evidence versus runtime enforcement,
- what remains intentionally preview-only.

## Execution-time model

- 30/60/90 minutes: refresh registry posture, run URL liveness checks, refresh evidence tables.
- 3/6/9 hours: reconcile source inventory, public deep-dive artifacts, and outward wording.
- Day-scale: external reviewer pass and governance decision on claim upgrades.

## Claim Boundary

`if.api` proves:
- preview-status public surfaces exist and are reachable,
- adapter/spec inventory artifacts are present and inspectable,
- demo/deep-dive evidence is no-login accessible.

`if.api` does not prove:
- public production runtime endpoint contracts,
- GA availability/SLO commitments,
- universal adapter quality equivalence,
- legal/compliance certification.

Registry status `preview` means public docs/evidence plus active internal work exists. It does not imply shipped runtime endpoint guarantees.

Cross-reference:
- `if.bus` remains `preview`; it carries routing/runtime controls and its own claim boundary.
- `if.trace` is `shipped` for byte-integrity receipt surfaces; referencing it does not upgrade `if.api` status.

## Document Navigation by Audience

- Executives / Business Leaders: [Executive Decision Surface](#executive-decision-surface)
- Power Users / Operators: [Operational Runbook View](#operational-runbook-view)
- Engineers / Implementers: [Implementation View](#implementation-view)
- LLM Runtime Developers: [Runtime Contract View](#runtime-contract-view)

## System Diagram

```mermaid
flowchart TD
  A[External System Event] --> B[if.api Adapter]
  B --> C[Normalized Envelope]
  C --> D[if.bus Routing (preview)]
  D --> E[Workflow or Decision Surface]
  E --> F[Optional if.trace Binding (shipped integrity layer)]

  G[Adapter Spec + Schema] --> B
  H[Registry status preview] --> I[Release language guardrails]
```

```text
ASCII fallback:
external system -> if.api adapter -> normalized envelope -> if.bus -> workflow
                                          -> optional if.trace binding
registry preview -> release wording guardrails
```

### Source vs Public Surface Split (critical)

```mermaid
flowchart LR
  S1[Source Inventory] --> S2[Adapter specs + schema files + demo scripts]
  S2 --> P1[Published Deep-Dive and Demo URLs]
  P1 --> P2[External Reviewer Packet]
  P2 --> P3[Preview claim posture]

  P3 --> X1[No public runtime endpoint contract claim]
```

```text
ASCII fallback:
source inventory -> published evidence URLs -> reviewer verification -> preview posture only
```

## Executive Decision Surface

### 1) One-page answer

`if.api` is a preview integration layer with real public documentation and evidence surfaces. It is not currently positioned as a public runtime endpoint contract.

### 2) Decision table (current)

| Decision question | Current answer | Evidence state | Risk if ignored |
|---|---|---|---|
| Is `if.api` publicly reachable as a product surface? | Yes | `200` on `/if/api/` and registry mirror alignment | perceived vaporware or stale docs |
| Is `if.api` status `preview` in registry truth? | Yes | `if.registry.json` local + public mirror show `preview` | accidental GA over-claim |
| Are no-login deep-dive and demo artifacts available? | Yes | deep-dive and demo URLs return `200` | weak external due-diligence posture |
| Are public runtime endpoint contracts claimed? | No | explicit non-claim in page copy and this explainer | operational/legal overstatement |
| Is adapter inventory evidence present in source? | Yes | adapter specs, schemas, and demo scripts are present | roadmap appears narrative-only |
| Are all adapters at equivalent production maturity? | No | current inventory spans multiple maturity tiers (see implementation quality table) | teams assume uniform reliability and over-commit |

### 3) Boardroom interpretation

- Strong today: public preview surface, inspectable adapter inventory, and no-login demo/deep-dive evidence.
- Narrow by design: no public runtime endpoint contract claim.
- Gate for stronger claims: external endpoint contract commitment + sustained runtime evidence.

### 4) Approve / defer / block framing

- Approve: preview language for integration inventory, adapter contracts, and no-login reviewer evidence.
- Defer: statements implying GA runtime endpoints or SLA/SLO guarantees (target checkpoint: 2026-03-15).
- Block: any wording that treats demo reachability as production runtime commitment.

### 5) Assumption most likely to be wrong

Assumption: because demos and deep-dive packs are public and rich, runtime endpoint guarantees are implied.

Invalidation test: if any outward copy equates "public demos" with "public API runtime commitments", block publication until wording is corrected.

## Operational Runbook View

### 1) Canonical operating rule

Operate `if.api` as preview-first, evidence-backed: if claim strength and evidence strength diverge, downgrade claim language immediately.

### 2) Runtime posture checks

1. Confirm registry alignment: `product_id=if.api`, `status=preview`, `path=/if/api`.
2. Confirm canonical public URLs in this paper resolve `2xx/3xx`.
3. Confirm page copy still states no public runtime endpoint contracts are claimed.
4. Confirm non-claims are present in executive and release-language sections.
5. If any canonical URL in this paper returns `4xx`/`5xx`, block publication until fixed.

### 3) Canonical no-login surfaces

https://infrafabric.io/if/api/
https://infrafabric.io/llm/if.registry.json.txt
https://infrafabric.io/llm/products/if-api/
https://infrafabric.io/llm/products/if-api/deep-dive/2026-02-01/index.md.txt
https://infrafabric.io/llm/products/if-api/deep-dive/2026-02-01-v1.0.1/index.md.txt
https://infrafabric.io/static/hosted/review/if-api-deep-dive/2026-02-01/index.html
https://infrafabric.io/static/hosted/review/if-api-integrations-inventory/2026-01-10/index.html
https://infrafabric.io/static/hosted/review/if-api-github-webhook-demo/2026-01-05/index.html
https://infrafabric.io/static/hosted/review/if-api-production-control-demo/2026-01-08/index.html
https://infrafabric.io/if/bus/
https://infrafabric.io/if/trace/

### 3b) Monitoring boundary (explicit)

- `if.api` currently has no public runtime endpoint contract surface, so there is no public runtime process heartbeat/SLO dashboard claimed in this paper.
- Monitoring focus for this revision is evidence-surface integrity: URL liveness, registry drift, and wording drift.
- If endpoint commitments are introduced, add runtime process/latency/error monitoring artifacts before any status language upgrade.

### 4) Incident posture

Fail closed when any of these occurs:
- canonical URL returns `4xx`/`5xx`,
- registry status/path drifts from expected values,
- outward copy implies runtime endpoint commitments not present in evidence.

### 5) Rollback principle

Rollback claims before code. If evidence and language drift, remove stronger wording first.

## Implementation View

### 1) Product identity and status

- Product ID: `if.api`
- Brand label: `IF.api (integrations)`
- Canonical path: `/if/api`
- Registry status: `preview`
- Runtime posture label: `active_internal` (registry status detail)

### 2) Source inventory snapshot (current host)

- Demo scripts: `39` files matching `scripts/if_api_*_demo.py`.
- Adapter spec JSONs: `9` files matching `docs/data/if_api_adapter_spec.*.json`.
- Schema files: `4` files under `schemas/if-api/*.schema.json`.
- Juakali fintech adapter modules (source lane): `9` modules under `/root/tmp/forgejo_dannystocker/infrafabric/if.api/fintech`.

Sample source files:
- `scripts/if_api_acquire_google_maps_demo.py`
- `scripts/if_api_gcp_quota_usage.py`
- `docs/data/if_api_adapter_spec.google_places_new.v1.json`
- `docs/data/if_api_adapter_spec.meta_graph_igdm.v1.json`
- `schemas/if-api/adapter_spec.schema.json`

### 2b) Adapter spec example (illustrative, redacted to boundary fields)

```json
{
  "spec_id": "if-api-google-places-new-2026-02-03",
  "adapter": {
    "adapter_id": "google.places.new",
    "provider": "Google Maps Platform",
    "status": "preview",
    "auth": {
      "type": "api_key",
      "secret_ref": "secrets://if/api/google/maps_api_key"
    }
  },
  "endpoints": [
    {
      "name": "places_search_text",
      "method": "POST",
      "path": "/v1/places:searchText"
    }
  ],
  "carrier_manifest_ref": "schemas/if-bus/carrier_manifest.schema.json"
}
```

### 2c) Normalized output example (illustrative demo event)

```json
{
  "adapter_id": "github.push.demo",
  "input_kind": "webhook.github.push",
  "normalized_event": {
    "event": "push",
    "integration": "github",
    "input_sha256": "29ed81a254ba70108386a09688d159f131734fbc915fcfaf2ad0ae0cc8e82765",
    "summary": {
      "commit_count": 2,
      "head_commit_id": "c0ffee25404a1f0d0a1b2c3d4e5f60718293a4b5"
    }
  },
  "emitted_utc": "2026-01-05T00:01:00Z",
  "claim_state": "source_validated"
}
```

### 2d) Current inventory quality classification (explicit, conservative)

| Tier | Current count basis | Count | Boundary |
|---|---|---:|---|
| `release-candidate` | adapters with externally committed runtime endpoint contract | 0 | no committed endpoint family in this revision |
| `review-ready` | adapters with formal spec JSON under `docs/data/if_api_adapter_spec.*.json` | 9 | contract artifacts exist; still preview posture |
| `experimental` | demo scripts not yet mapped to a release-candidate endpoint contract | 39 (inventory), at least 30 not spec-backed by count-difference heuristic | demos prove patterns, not runtime commitments |
| `source-only` | Juakali fintech + robotics/drone modules present in source trees without published no-login contract/evidence packet | 13 code modules (+1 defense architecture spec) | useful implementation signal; no public runtime commitment |

### 2e) Juakali fintech adapter lane (newly included for complete adapter view)

Source root:
- `/root/tmp/forgejo_dannystocker/infrafabric/if.api/fintech`

Modules detected:
- Mobile money: `mpesa`, `mtn-momo`, `airtel-money`, `orange-money`
- Messaging: `africas-talking`
- KYC: `smile-identity`, `transunion`
- Core banking/microfinance: `mifos`, `musoni`

Observed maturity boundary (black/white):
- Proven now (`source_validated`): adapter code exists across all 9 modules.
- Not yet proven (`intent_only`):
  - IF.bus publisher wiring is TODO-marked in `airtel_money_adapter.py`, `mtn_momo_adapter.py`, and `orange_money_adapter.py`.
  - `mpesa_adapter.py` still documents placeholder credential encryption for production replacement.

### 2f) Legal-corpus adapter consolidation references (task-prep links)

Primary legal corpus sources to consolidate:
- `if-legal-corpus` mirror: `/root/tmp/forgejo_dannystocker/if-legal-corpus`
- Secondary mirror: `/root/tmp/if_arbitrate_demo_search/if-legal-corpus`
- France legal API ingestion artifacts (PISTE/Legifrance): `/root/tmp/if1388/legifrance_api_batch_run6_strict_uas_final`
- SkyDrone law/funding research artifacts:
  - `/root/tmp/if1388/ai_law_grants_depth_run1`
  - `/root/tmp/if1388/ai_law_grants_depth_run2`
  - `/root/tmp/if1388/defense_ai_law_run1`

Consolidation boundary:
- These references expand adapter/data coverage visibility.
- They do not upgrade `if.api` from `preview` or create runtime endpoint commitments.

### 2g) Robotics and drone adapter lane (newly included for complete adapter view)

Physical integration source root:
- `/root/tmp/forgejo_dannystocker/infrafabric/src/integrations/physical`

Detected modules:
- `drone_fleet_adapter.py` (multi-protocol drone control surface; large implementation file)
- `opentrons_adapter.py` (stub)
- `qiskit_adapter.py` (stub)
- `ros2_bridge.py` (stub)

Defense architecture reference:
- `/root/tmp/forgejo_dannystocker/infrafabric/if.api/defense/cuas/README.md` (status labeled as architecture specification)

Related research/evidence packs:
- `docs/378-if-context-skydrone-full-system-consolidated-review-pack-v1-2026-02-10.md`
- `docs/379-if-context-skydrone-60q-navigator-and-cache-warm-delta-pack-v1-2026-02-10.md`
- `docs/380-if-context-skydrone-prompt-retune-scorecard-v1-2026-02-10.md`

Observed maturity boundary (black/white):
- Proven now (`source_validated`): robotics/drone adapter source files and C-UAS architecture spec are present.
- Not yet proven (`intent_only`): public no-login runtime endpoint commitments for these modules are not evidenced in this revision.

### 2h) Expanded module matrix (current checkout + roadmap cross-check)

Current `if.api` categories detected in source checkout (`/root/tmp/forgejo_dannystocker/infrafabric/if.api`):
- `broadcast` (`12` files)
- `communication` (`17` files)
- `data` (`3` files)
- `defense` (`1` file)
- `fintech` (`47` files)
- `llm` (`83` files)
- `security` (`1` file)

Cloud/orchestration-related modules detected:
- `if.api/data/redis/redis_swarm_coordinator.py` (present)
- `src/core/logistics/redis_swarm_coordinator.py` (present)
- `monitoring/recovery/recovery_orchestrator.py` (present)

Cross-module SIP orchestration note:
- `if.switchboard` (Redis-backed SIP orchestration) is an adjacent runtime module that integrates with `if.api/communication/sip/adapters`.
- In this explainer, switchboard is treated as a dependency/integration surface, not counted as a native `if.api` adapter module.

Roadmap cross-check source:
- `/root/tmp/forgejo_dannystocker/infrafabric/docs/api/API_ROADMAP.md`

Roadmap-referenced but currently missing in this checkout:
- `if.api/cloud/stackcp`
- `if.api/cloud/oci`
- `if.api/data/file-cache`
- `if.api/broadcast/ndi`
- `if.api/communication/h323`
- `if.api/messaging`

Boundary interpretation:
- Present paths are counted as `source_validated` only.
- Missing roadmap paths remain `intent_only` until source and evidence artifacts exist in the same revision line.

### 3) Public evidence artifacts

- Product page: public preview positioning and non-claim line on runtime endpoints.
- Locked deep dives: `2026-02-01` and `2026-02-01-v1.0.1` indexes.
- Hosted review artifacts: integrations inventory and representative demos.

### 4) Evidence highlights

- Registry and product page align on `preview` posture for `if.api`.
- Public deep-dive indexes are reachable and labeled as locked snapshots.
- Demo/index artifacts exist for integration and resolver patterns.
- No claim evidence is presented for public runtime endpoint contracts.

### 5) Known boundary risk

`https://infrafabric.io/llm/products/if-api/` is a legacy wrapper surface and may lag registry wording in some fields; registry mirror remains the primary claim boundary.

## Runtime Contract View

### 1) Contract goals for runtime clients

- deterministic adapter output shape,
- explicit status and non-claim semantics,
- no implicit upgrade from preview docs to runtime guarantees.

### 2) Minimum contract fields (document/runtime boundary)

```json
{
  "contract_id": "if.api.runtime.v1",
  "required": [
    "adapter_id",
    "input_kind",
    "normalized_event",
    "emitted_utc",
    "claim_state"
  ],
  "optional": [
    "trace_reference",
    "schema_version",
    "contract_profile"
  ],
  "forbidden_inference": [
    "ga_runtime_endpoint",
    "compliance_certified",
    "slo_committed"
  ]
}
```

### 2a) Runtime payload example (required concrete instance)

```json
{
  "adapter_id": "github.push.demo",
  "input_kind": "webhook.github.push",
  "normalized_event": {
    "event": "push",
    "integration": "github",
    "summary": {
      "commit_count": 2
    }
  },
  "emitted_utc": "2026-01-05T00:01:00Z",
  "claim_state": "source_validated",
  "schema_version": "demo.v1",
  "contract_profile": "if.api.runtime.v1"
}
```

### 2b) Backward-compatibility rule (explicit)

- Required fields and their meaning are frozen within `if.api.runtime.v1`.
- Optional fields may be added with defaults.
- Breaking semantic changes require a new contract version and migration note.

### 3) Runtime state labels

- `deployed_enforced`: behavior proven in deployed runtime evidence.
- `source_validated`: behavior proven in source/tests or demos.
- `intent_only`: planned behavior with no sufficient evidence yet.

### 4) Current state map

- Adapter inventory presence: `source_validated`.
- Public deep-dive/demo publication: `deployed_enforced` (public reachability proven).
- Public runtime endpoint contract commitments: `intent_only` (not claimed).

## What is intentionally not claimed

- No claim that `if.api` currently exposes GA runtime endpoints.
- No claim that all adapter demos are production-hardened.
- No claim that preview artifacts equal contractual SLA/SLO commitments.
- No claim of legal/compliance certification from adapter docs alone.

## Release Language Guardrails

### 1) Approved wording

- "`if.api` is preview with live public surfaces for adapter contracts and evidence packs."
- "`if.api` currently emphasizes repeatable integration contracts and no-login review artifacts."
- "Public runtime endpoint contracts are not yet committed."

### 2) Blocked wording

- "`if.api` is GA."
- "`if.api` guarantees production endpoint availability."
- "All adapters are production-certified."

### 3) Registry-status guardrail

- `preview` remains required wording until runtime endpoint contract commitments are explicitly evidenced and approved.

### 4) Enforcement mechanism (owner + process)

- Owner: accountable approver named in header.
- Runtime evidence owner: active operator maintaining `if.api` evidence checks.
- Continuity owner: backup reviewer/operator must rerun minimal external checks before claim upgrades.
- Publish gate before claim upgrades:
  1. rerun canonical URL liveness checks,
  2. rerun registry alignment check for `if.api`,
  3. run scaffold lint,
  4. record pass/fail in blackboard task closeout.
- If any gate fails, wording remains conservative (`preview`, no runtime endpoint commitment claims).
- Any canonical URL used in this document returning `4xx`/`5xx` blocks publication until fixed.

## 30/60/90 plan

### 30 days

- Maintain no-login evidence freshness for deep-dive and demo surfaces.
- Define candidate endpoint-selection criteria for first external commitment (quality tier, error budget history, replay controls, and ownership).
- Add recurring drift check between registry mirror and `if.api` page wording.
- Build a single adapter coverage ledger merging:
  - spec-backed adapters (`docs/data/if_api_adapter_spec.*.json`),
  - demo adapters (`scripts/if_api_*_demo.py`),
  - Juakali fintech source adapters (`/root/tmp/forgejo_dannystocker/infrafabric/if.api/fintech`).

30-day risk analysis:
- Risk: wording drift between registry and legacy wrapper surfaces.
  - Mitigation: registry-first release gating and weekly diff checks.
- Risk: demo inventory interpreted as runtime guarantee.
  - Mitigation: keep runtime non-claim line in top section and release guardrails.
- Risk: adapter spec expansion without uniform quality bar.
  - Mitigation: publish adapter acceptance checklist before claim upgrades.

### 60 days

- Publish adapter quality matrix (`experimental | review-ready | release-candidate`) with criteria.
- Select first candidate endpoint contract surface using the published matrix and publish the selection rationale.
- Promote selected operator-assisted evidence to immutable no-login mirrors.
- Add contract versioning notes for first externally committed endpoint family.
- Integrate the imported coverage-roadmap scaffold from `/root/docs/_uploads/if.api-coverage-roadmap.md` as an `if.api`-specific execution matrix (phases, owners, risk register).

### 90 days

- Reassess status only if endpoint contract commitments and sustained runtime evidence exist.
- Publish outcome as `no change` or `upgrade candidate` with explicit evidence matrix.
- Run cross-lane consolidation pass for legal/fintech adapters and publish a single no-login inventory artifact with hash-pinned manifest.

## Imported Roadmap Integration Note (explicit)

Imported file:
- `/root/docs/_uploads/if.api-coverage-roadmap.md`

What was integrated:
- phased roadmap structure,
- owner/timeline framing,
- explicit risk-register posture.

What was not imported:
- domain-specific FRANK-AI/Garmin business claims,
- acquisition recommendation claims,
- any runtime guarantee language not evidenced in `if.api` artifacts.

## External Reviewer Packet

https://infrafabric.io/if/api/
https://infrafabric.io/llm/if.registry.json.txt
https://infrafabric.io/llm/products/if-api/
https://infrafabric.io/llm/products/if-api/deep-dive/2026-02-01/index.md.txt
https://infrafabric.io/llm/products/if-api/deep-dive/2026-02-01-v1.0.1/index.md.txt
https://infrafabric.io/static/hosted/review/if-api-deep-dive/2026-02-01/index.html
https://infrafabric.io/static/hosted/review/if-api-integrations-inventory/2026-01-10/index.html
https://infrafabric.io/static/hosted/review/if-api-github-webhook-demo/2026-01-05/index.html
https://infrafabric.io/static/hosted/review/if-api-production-control-demo/2026-01-08/index.html
https://infrafabric.io/if/bus/
https://infrafabric.io/if/trace/

Cross-module links rationale:
- `if.bus` is included because `if.api` normalized outputs route through bus topics in the current architecture.
- `if.trace` is included because selected `if.api` outputs may bind to trace receipts for byte-integrity evidence.

What reviewers can conclude now:
- `if.api` is publicly surfaced and registry-listed as `preview`.
- no-login deep-dive/demo artifacts are reachable.
- integration inventory/spec posture is evidence-backed as a preview capability surface.

What reviewers cannot conclude now:
- GA runtime endpoint commitments,
- production SLO/SLA guarantees,
- compliance certification.

## Evidence Hierarchy (required boundary)

| Evidence tier | Current artifact examples | Reviewer reproducibility | Promotion path |
|---|---|---|---|
| Independent | `if.api` page, registry mirror, deep-dive indexes, hosted review demo/inventory pages | no-login third-party fetchable | already independent |
| Operator-assisted | source inventory counts from local filesystem, local contract/schema checks | requires host/repo access | target mirror checkpoint: 2026-03-15 via `if-api-inventory-manifest` publication (`index.html` + `inventory_manifest.v1.json` + per-file `sha256`) on a no-login immutable URL |

## Appendix A: Verification commands used for this revision

### Minimal external verification set (no-login, 3-5 commands)

```bash
# 1) Registry truth for if.api
curl -fsSL https://infrafabric.io/llm/if.registry.json.txt \
  | jq -c '.products[] | select(.product_id=="if.api") | {product_id,status,path,runtime_state,usage_posture}'

# 2) Core page posture check
curl -fsSL https://infrafabric.io/if/api/ | grep -Eo 'Status \(black/white\):[^<]+' | head -n 1

# 3) Locked deep-dive index (v1.0)
curl -fsSL https://infrafabric.io/llm/products/if-api/deep-dive/2026-02-01/index.md.txt | sed -n '1,80p'

# 4) Locked deep-dive index (v1.0.1)
curl -fsSL https://infrafabric.io/llm/products/if-api/deep-dive/2026-02-01-v1.0.1/index.md.txt | sed -n '1,80p'

# 5) Hosted inventory page reachability
curl -fsSI https://infrafabric.io/static/hosted/review/if-api-integrations-inventory/2026-01-10/index.html | head -n 10
```

### Full operator verification set (internal/host)

```bash
# workspace root
cd /root

# latest bible verify
python3 scripts/if_bibles_latest.py refresh
python3 scripts/if_bibles_latest.py resolve --bible-id if.whitepapers.bible --channel authoring_default --format path
python3 scripts/if_bibles_latest.py verify --bible-id if.whitepapers.bible --pointer-index docs/208-if-whitepapers-bible-pointer-index.md
```

```bash
# local registry entry for if.api
python3 - <<'PY'
import json
from pathlib import Path
obj=json.loads(Path('if.registry.json').read_text())
for p in obj.get('products', []):
    if p.get('product_id') == 'if.api':
        print(json.dumps(p, indent=2, ensure_ascii=False))
        break
PY
```

```bash
# source inventory counts
python3 - <<'PY'
from pathlib import Path
print({
  'demo_scripts': len(list(Path('scripts').glob('if_api_*_demo.py'))),
  'adapter_specs': len(list(Path('docs/data').glob('if_api_adapter_spec.*.json'))),
  'schemas': len(list(Path('schemas/if-api').glob('*.schema.json')))
})
PY
```

```bash
# canonical URL liveness gate for this explainer packet
for u in \
  'https://infrafabric.io/if/api/' \
  'https://infrafabric.io/llm/if.registry.json.txt' \
  'https://infrafabric.io/llm/products/if-api/' \
  'https://infrafabric.io/llm/products/if-api/deep-dive/2026-02-01/index.md.txt' \
  'https://infrafabric.io/llm/products/if-api/deep-dive/2026-02-01-v1.0.1/index.md.txt' \
  'https://infrafabric.io/static/hosted/review/if-api-deep-dive/2026-02-01/index.html' \
  'https://infrafabric.io/static/hosted/review/if-api-integrations-inventory/2026-01-10/index.html' \
  'https://infrafabric.io/static/hosted/review/if-api-github-webhook-demo/2026-01-05/index.html' \
  'https://infrafabric.io/static/hosted/review/if-api-production-control-demo/2026-01-08/index.html' \
  'https://infrafabric.io/if/bus/' \
  'https://infrafabric.io/if/trace/'; do
  code=$(curl -sS -o /dev/null -w '%{http_code}' "$u")
  echo "$code $u"
  case "$code" in
    2*|3*) ;;
    *) echo "BLOCKER: non-2xx/3xx URL in canonical packet"; exit 1;;
  esac
done
```

## Appendix B: Non-claims reminder block

- Preview status does not equal GA endpoint contract.
- Public demo pages do not equal production runtime commitments.
- Adapter inventory breadth does not equal uniform production hardening.

## Conclusion

`if.api` is in a strong preview position when described precisely:
- public integration surfaces are reachable,
- deep-dive and demo evidence is no-login accessible,
- source inventory evidence is concrete and inspectable,
- runtime endpoint commitments remain intentionally unclaimed.

Key action now: keep registry and page wording in lockstep while promoting operator-assisted inventory evidence to immutable no-login summaries.

Key risk now: teams infer endpoint guarantees from demo richness and overstate runtime commitments.

The correct posture is high-integrity preview language with strict claim boundaries.

*If we let demo breadth speak louder than contract truth, reliability will fail at the exact moment trust is tested.*

Style Guide: Whitepaper v4.0
Writing Standard Source: if.whitepapers.bible v4.0

## Related

- [[if.trace Full Explainer (Bible v4.23, Six-Audience, Claim-Boundary Strict)]]
- [[Governance and PHAROS MOC]]
- [[InfraFabric Architecture]]
