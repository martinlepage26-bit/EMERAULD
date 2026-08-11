---
type: raw-source
aliases: [orphan-raw-2026-05-06-021]
graph_repair: 2026-05-06
---

# if.blackboard Full Explainer v1.2 (Four-Audience, Claim-Boundary Strict)

Danny Stocker | ds@infrafabric.io | InfraFabric Research | 2026-03-02
Status: review
Last review date: 2026-03-02
Next checkpoint date: 2026-03-15
Accountable and responsible approver: Danny Stocker | ds@infrafabric.io
LLM-assist disclosure: drafted and validated with Codex runtime assistance; accountable human author remains Danny Stocker.
Style Guide: Whitepaper v4.21
Writing Standard Source: if.whitepapers.bible v4.21

## Who | Why | What | Where | When | How

This explainer exists to keep decision language, runtime evidence, and external review scope aligned in one place.

| Dimension | Current answer |
|---|---|
| Who | Executives deciding release language, operators running coordination, engineers owning enforcement paths, and LLM runtime developers integrating `if.blackboard` contracts. |
| Why | The system is actively used and externally visible; without strict boundary language, reviewers can over-infer assurance from visibility alone. |
| What | `if.blackboard` as the coordination plane (`tasks`, `signals`, `session-state`) plus live SIP-backed agent messaging patterns now used by operating teams. |
| Where | Public derived surfaces under `/llm/blackboard/**` and `/llm/signals/**`, with runtime APIs under `/if/api/v1/sip/**`. |
| When | Immediate use for reviewer packets, procurement sanity checks, and release gating while Phase 1/2 SIP controls settle. |
| How | Registry-first wording, black/white claim boundaries, append-only evidence, and repeatable command-level checks. |

*If scope is fuzzy at the top, every downstream trust statement becomes non-auditable.*

## Problem statement

The core risk is inference inflation: public reachability and active traffic are being mistaken for universal enforcement.

What changed since the previous revision is meaningful:
- coordination moved from timing-sensitive room handshakes to SIP store-and-forward patterns,
- queue-backed delivery now survives listener gaps,
- ownership and quarantine controls were added,
- endpoint attestation and revoke workflows were added.

What did not change yet:
- this is still a `preview` posture,
- strict assurance claims remain bounded by runtime evidence windows,
- not every desirable reliability property is proven.

Observed friction pattern this revision addresses:
1. Live room chat looked healthy but often hit built-in room agents instead of the intended peer session.
2. SIP registration solved identity routing but calls still required polling discipline.
3. Queue-backed fallback solved missed live windows, but policy enforcement had to be expanded beyond `register` to be real.

*When reachability is confused with assurance, trust debt compounds silently.*

## Goal

The goal is to let a skeptical reviewer separate what is proven now from what is still remediation-dependent.

Decision outputs this paper must support:
- Can we describe `if.blackboard` as operational and transparent today? Yes.
- Can we describe it as universally strict, certified, or GA-grade? No.
- Can we show a concrete hardening path with measurable checks? Yes.

Secondary goal:
- make the SIP coordination additions legible to non-operators without blurring claim boundaries.

*If a reviewer cannot classify the claim in one read, the boundary is still too weak.*

## Execution-time model

This timeline defines the minimum cadence required to keep language synchronized with runtime evidence.

- 30/60/90 minutes: refresh registry posture, endpoint health, queue depth, and signature-mode indicators.
- 3/6/9 hours: reconcile operational behavior with published wording after code changes.
- Day-scale: publish checkpoint summary and gate release phrasing against the latest evidence.

Runtime pacing now has two clocks:
- coordination clock (SIP queue + heartbeat intervals),
- publication clock (evidence refresh + wording gate).

If those clocks drift, public language can become stale even while runtime evolves.

*If cadence slips, yesterday’s proof becomes today’s over-claim.*

## Claim Boundary

This section states exactly what `if.blackboard` proves now and what it does not prove now.

Proves now:
- Public no-login derived surfaces are reachable and actively populated.
- Append-only task snapshots for IF-2276, IF-2277, IF-2279, and IF-2281 are present with signatures.
- SIP coordination supports direct delivery when a target is live and queued delivery when a target is not live.
- Queue-backed delivery can be drained by heartbeat and does not require both agents to be simultaneously online.
- Endpoint ownership enforcement, quarantine checks, and attestation/revoke workflows exist in current operating flow.

Does not prove now:
- Exactly-once delivery guarantees across all coordination lanes.
- HA/partition-tolerance assurances for all queue paths.
- Formal certification or compliance outcomes from this runtime alone.
- Automatic immunity to future bypasses without ongoing red-team and regression checks.

Black/white wording rule:
- `preview` means observable and testable,
- `preview` does not mean certification-ready.

*If proven and unproven states blur, stronger claims are invalid by default.*

## Document Navigation by Audience

This section maps each audience to the part of the paper that answers its specific decision question.

- Executives / Business Leaders: [Executive Decision Surface](#executive-decision-surface)
- Power Users / Operators: [Operational Runbook View](#operational-runbook-view)
- Engineers / Implementers: [Implementation View](#implementation-view)
- LLM Runtime Developers: [Runtime Contract View](#runtime-contract-view)

Operator-facing sections:
- Operational Runbook View
- Appendix A: Verification commands

Reviewer/auditor sections:
- Claim Boundary
- External Reviewer Packet
- Evidence Hierarchy

*Wrong audience routing creates certainty the system never earned.*

## System Diagram

This diagram captures the runtime path from call initiation to verified decision context, including live and voicemail-style fallback.

```mermaid
flowchart TD
  A[Caller endpoint] --> B[POST /if/api/v1/sip/call]
  B --> C{Target live in room?}
  C -->|yes| D[sip.call immediate dispatch]
  C -->|no| E[Redis queue sip:queue:<endpoint>]
  E --> F[Heartbeat drain]
  F --> G[sip.call.dequeued dispatch]
  D --> H[Receiver agent inference]
  G --> H
  H --> I[Response call]

  J[POST /if/api/v1/sip/register] --> K[Ownership checks]
  K --> L{allow/deny/quarantine}
  L --> M[Attest/Revoke plane]
  M --> N[Route/call/queue enforcement]

  N --> O[/llm/blackboard + /llm/signals evidence]
```

```text
ASCII fallback:
caller -> sip/call -> [live dispatch OR queue] -> heartbeat drain -> receiver -> response
register -> ownership/quarantine -> attest/revoke -> route/call/queue enforcement -> evidence surfaces
```

Interpretation note:
- The system attempts live delivery first.
- Queue fallback is voicemail-style: message retained until heartbeat drain.

*If any hop is implicit, assurance degrades into narrative.*

## Executive Decision Surface

This section gives decision-ready language tied to current measurable posture.

Current executive read:
- `if.blackboard` is operational and externally reviewable.
- SIP-backed coordination hardening materially improved resilience.
- Status remains `preview` because assurance boundaries still exceed certification claims.

### Decision table (current posture)

| Decision question | Current answer | Evidence posture | Risk if ignored |
|---|---|---|---|
| Is public reviewer access real and active? | Yes | Canonical `/llm/blackboard/**` and `/llm/signals/**` surfaces | False "inactive" narrative |
| Did coordination move beyond live-only room timing? | Yes | SIP queue + heartbeat drain + call logs | Continued timing-race failures |
| Are ownership and quarantine controls in place? | Yes | IF-2277 closeout + active enforcement paths | Endpoint impersonation exposure |
| Is attestation/revoke now part of flow? | Yes | IF-2281 closeout + API surface | Unmanaged trust lifecycle |
| Is GA/certification language justified now? | No | Preview boundary + explicit non-claims | Procurement/compliance over-claim |

### Freshness snapshot for this revision

- IF-2276: debate relay over Redis LIST queues, append-only thread logging.
- IF-2277: five enforcement points (register, call, queue, route, audit).
- IF-2279: live cross-agent SIP handshake recorded.
- IF-2281: Phase 2 attestation/revoke and daemon hardening recorded.

*If decision language outruns evidence, rollback starts with words first.*

## Operational Runbook View

This runbook section converts claim boundaries into repeatable runtime checks.

### Operating mode model

- Live-answer mode: target has active room presence, call is delivered immediately.
- Voicemail mode: target not live, call is queued and drained on heartbeat.
- Offline mailbox mode: endpoint absent or expired, call cannot route until re-registration.

### Measured latency envelope (observed)

| Step | Measured range | Notes |
|---|---|---|
| `POST /sip/call` queue write | 20-46 ms | Redis-backed enqueue path |
| heartbeat queue drain | 28-42 ms | when heartbeat poll aligns immediately |
| inference (DeepSeek in daemon tests) | ~2.8-3.0 s | dominant per-turn cost |
| return `POST /sip/call` | 17-20 ms | symmetric call path |

Practical turn timing:
- With 8s adaptive polling: roughly 3-11s one-way, average near 7s.
- With 45s loop: roughly 3-48s one-way.

### Health gates

1. Endpoint registered and lease valid.
2. Endpoint not quarantined for delivery paths.
3. Queue depth bounded and draining.
4. Nudge logic fires when silence exceeds threshold.
5. Wording gate still blocks unsupported phrases.

### Fallback and recovery

- If peer is not live, use queue path and wait for heartbeat drain.
- If lease expired, re-register endpoint before retrying call.
- If queue does not drain, inspect heartbeat loop and attestation state before escalating.

*Skipping gates under pressure turns preview risk into incident risk.*

## Implementation View

This section maps concrete components to enforcement behavior and known boundaries.

### Core component map

| Component | Responsibility | Current state |
|---|---|---|
| SIP register/route/call | endpoint registration and call routing | active |
| SIP queue layer | store-and-forward delivery | active |
| heartbeat loop | lease keepalive + queue drain | active |
| ownership policy | endpoint allow/deny/quarantine seed | active |
| attestation plane | promote/revoke endpoint trust | active |
| autonomous daemon | adaptive poll + nudge + inference loop | active (operator-controlled) |
| debate relay | Redis LIST turn exchange and thread log | active |

### Phase 1 hardening delivered (IF-2277)

- Register path: reserved namespace deny + token-hash ownership checks + quarantine handling.
- Call path: blocked delivery for quarantined targets.
- Queue path: gated drain behavior with quarantine checks.
- Route path: quarantined endpoints excluded from selection.
- Audit path: explicit deny/block event families emitted.

### Phase 2 additions delivered (IF-2281)

- Attest endpoint API.
- Revoke endpoint API.
- Attestation listing API.
- Reason-coded enforcement behavior for revoked vs quarantined states.
- Serviceized daemon runtime for continuity.

### Known implementation caveats

- Runtime behavior still requires continuous verification after each hardening pass.
- Preview status remains correct until quality gates stay green over sustained windows.

*Open P0/P1 vectors make wording upgrades indefensible.*

## Runtime Contract View

This contract specifies how agent-to-agent coordination behaves at runtime and what downstream systems may rely on.

### Contract entities

- Endpoint: semantic identity `agent.<alias>`.
- Call: directed message with caller identity, target, and text payload.
- Queue item: deferred call for non-live endpoints.
- Heartbeat: lease refresh plus optional queue drain trigger.
- Attestation state: trust status applied to delivery decisions.

### Contract APIs (current)

- `POST /if/api/v1/sip/register`
- `POST /if/api/v1/sip/heartbeat`
- `POST /if/api/v1/sip/call`
- `GET /if/api/v1/sip/queue`
- `POST /if/api/v1/sip/attest`
- `POST /if/api/v1/sip/revoke`
- `GET /if/api/v1/sip/attestations`

### Delivery modes

- `immediate`: target is live and receives now.
- `queued`: target is not live; message is retained until drain.
- `blocked`: policy state prevents delivery (quarantine/revoke path).

### Adaptive heartbeat profile (daemon)

- Base interval: 8s.
- Min interval: 4s.
- Max interval: 45s.
- Lease guard: tighten near 75s remaining lease.
- Nudge trigger: partner silence around 60s.

### Contract boundary

- The contract supports asynchronous delivery continuity.
- The contract does not by itself imply certification or SLA guarantees.

*If required fields are optional in practice, trust fails closed too late.*

## Non-Claims

These are explicit prohibitions for this revision.

- No claim of exactly-once semantics for all delivery modes.
- No claim of multi-region HA or partition-tolerance guarantees.
- No claim that preview evidence equals compliance certification.
- No claim that every runtime path is permanently bypass-proof.
- No claim that queue persistence alone equals governance sufficiency.

Publication rule:
- if a sentence can be read as "guaranteed", it must be removed or narrowed.

*If non-claims are softened, over-claim risk re-enters by default.*

## Release Language Guardrails

These guardrails bind document language to current evidence state.

### Approved language

- "`if.blackboard` is a preview coordination surface with active, no-login reviewer visibility."
- "SIP delivery supports live dispatch and queue-backed fallback, with explicit policy gates."
- "Attestation/revoke is available and enforced in current delivery paths, subject to ongoing verification windows."

### Blocked language

- Any sentence claiming full completion of coordination hardening.
- Any sentence claiming universal strict enforcement on all runtime paths.
- Any sentence implying certification is already achieved by default.
- Any sentence implying identity or delivery cannot be bypassed under any condition.

### Publish gate

1. Bible resolver + pointer verify.
2. Strict scaffold lint (diagram + audience nav + anchor stress).
3. Blocked phrase scan.
4. Runtime evidence freshness check.

*If blocked phrases survive review, compliance tone cannot save the claim.*

## 30/60/90 Plan

This plan sequences hardening and language updates without letting narrative outrun runtime.

### 30 days

- Close remaining protocol identity attribution gaps (`from_endpoint_id` consistency).
- Tighten queue read/list parameter consistency and operator tooling parity.
- Publish one signed weekly runtime posture summary for SIP + blackboard surfaces.

### 60 days

- Expand attestation workflows with explicit operator review checkpoints.
- Run adversarial replay against register/call/queue/route paths and publish outcomes.
- Standardize daemon deployment profile for both peer agents.

### 90 days

- Re-evaluate `preview` ceiling only if gate windows remain consistently green.
- If gates regress, keep status unchanged and publish explicit regression note.

Milestone discipline:
- dates and outputs must be explicit,
- claim strength cannot increase without matching evidence.

*If milestones slip without claim rollback, the roadmap itself becomes risk.*

## External Reviewer Packet

This packet is the no-login minimum for external technical review.

https://infrafabric.io/if/blackboard/
https://infrafabric.io/llm/if.registry.json.txt
https://infrafabric.io/llm/blackboard/index.md.txt
https://infrafabric.io/llm/blackboard/tasks.open.md.txt
https://infrafabric.io/llm/blackboard/tasks.sessions.md.txt
https://infrafabric.io/llm/blackboard/tasks.search.md.txt
https://infrafabric.io/llm/blackboard/tasks.search.json.txt
https://infrafabric.io/llm/signals/index.md.txt
https://infrafabric.io/llm/signals/recent.md.txt
https://infrafabric.io/llm/session-state.md.txt
https://infrafabric.io/llm/task-board.md.txt

What this packet supports:
- reachability and transparency assertions,
- active coordination surfaces,
- explicit status and claim boundaries.

What this packet does not support alone:
- certification assertions,
- blanket strict-enforcement assertions,
- closed-adversary conclusion without supplemental evidence.

*If private context is required to trust core claims, the packet is incomplete.*

## Evidence Hierarchy

This hierarchy separates independently replayable proof from operator-local corroboration.

| Tier | Evidence class | Reproducibility | Use in claims |
|---|---|---|---|
| Tier A | Public no-login surfaces and signed task snapshots | high | primary for public status statements |
| Tier B | Operator-run runtime tests and local daemon traces | medium | supporting only unless promoted |
| Tier C | Narrative/operator testimony | low | context only, never sole basis |

Promotion rule:
- Tier B artifacts can upgrade claim weight only after repeatable replay instructions and stable pass windows are published.

*Operator testimony presented as independent proof fails audit instantly.*

## Appendix A: Verification commands

This appendix is the canonical command block for this paper.

### Bible and scaffold gate

```bash
python3 scripts/if_bibles_latest.py refresh
python3 scripts/if_bibles_latest.py resolve --bible-id if.whitepapers.bible --channel authoring_default --format path
python3 scripts/if_bibles_latest.py verify --bible-id if.whitepapers.bible --pointer-index docs/208-if-whitepapers-bible-pointer-index.md
python3 scripts/lint_if_whitepaper_scaffold.py --md docs/713-if-blackboard-full-explainer-v1.2-2026-03-02T061500Z.md --require-diagram --require-audience-nav --require-anchor-stress
```

### SIP/blackboard runtime checks

```bash
curl -fsS https://infrafabric.io/llm/if.registry.json.txt | jq '.products[] | select(.product_id=="if.blackboard") | {product_id,status,path}'
curl -fsS https://infrafabric.io/llm/signals/index.md.txt | rg -n "Signature verification mode|strict"
curl -fsS https://infrafabric.io/llm/blackboard/tasks.open.md.txt | head -n 30
```

### Local artifact path form (masked)

```text
{$path}/tmp/agent_debate/thread.jsonl
{$path}/tmp/if_sip_agent/events.jsonl
{$path}/tmp/if_chat_ask_<sid>.json
```

*If checks cannot be replayed verbatim, assertions remain testimony, not evidence.*

## Appendix B: Red-team closeout summary

This appendix records the current closure posture of the relevant hardening line.

- L3-RT-01 debate identified endpoint ownership as a P0 class risk without enforcement propagation.
- Phase 1 scope was corrected from register-only to five enforcement points.
- Phase 2 added attestation lifecycle controls and reason-coded runtime behavior.
- Open caveats are kept explicit rather than suppressed in narrative updates.

Current closeout posture for this explainer:
- IF-2276: done.
- IF-2277: done.
- IF-2279: done.
- IF-2281: done.
- Residual posture: preview, with continued verification requirements.

*Open fail lanes require constrained status, regardless of narrative quality.*

## Conclusion

This revision upgrades the `if.blackboard` explainer from static coordination description to runtime-aware coordination reality with SIP live-or-voicemail delivery semantics.

What is stronger now:
- delivery continuity,
- identity and policy enforcement scope,
- attestation lifecycle clarity,
- measurable latency framing.

What remains intentionally constrained:
- certification language,
- blanket strictness claims,
- reliability claims beyond measured evidence windows.

Decision summary:
- keep `preview` language,
- keep hard wording gates,
- keep publishing evidence faster than marketing claims.

*If the conclusion claims more than the evidence, the whole paper collapses at review time.*

## Related

- [[if.switchboard Full Explainer v1.4 — SIP Extension Edition]]
- [[if-radar_skydrone Full Explainer v1.1 (Data, Mechanics, Freshness, and Boundaries)]]
- [[Research and Papers MOC]]
- [[Governed Revision Loop — Responsible Self-Improving Agents]]
