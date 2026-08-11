---
type: raw-source
aliases: [orphan-raw-2026-05-06-029]
graph_repair: 2026-05-06
---

# if.switchboard Full Explainer v1.4 — SIP Extension Edition

Danny Stocker | ds@infrafabric.io | InfraFabric Research | 2026-03-02
Status: review
Last review date: 2026-03-02
Next checkpoint date: 2026-03-15
Checkpoint scope: internal review closure plus go/no-go decision for promoting v1.4 to canonical public switchboard surface.
Accountable and responsible approver: Danny Stocker | ds@infrafabric.io
LLM-assist disclosure: drafted and validated with rook-014 (Claude) and rook-002 (Codex) runtime assistance; accountable human author remains Danny Stocker.
Supersedes: `docs/711-if-switchboard-full-explainer-v1.3-2026-02-27T133500Z.md`

## Who | Why | What | Where | When | How

This block defines scope, audience, and execution context at the top of the document so every downstream claim can be traced back to an explicit frame.

| Dimension | Current answer |
|---|---|
| Who | Executives deciding release language; operators running SIP-backed agents; engineers owning enforcement paths; external reviewers auditing control-plane claims. |
| Why | Runtime hardening across four task IDs (IF-2276/2277/2279/2281) materially changed what the system can do and what can be claimed; v1.3 docs did not yet reflect the full Phase 1/2 enforcement surface or the live inter-agent proof. |
| What | `if.switchboard` extended with SIP-style endpoint registration, call routing, voicemail-queue fallback, ownership/quarantine enforcement (Phase 1), and attestation/revoke lifecycle (Phase 2). |
| Where | Internal sources: `docs/710-if-switchboard-agent-lifecycle-spec-v1-2026-02-27.md`, `tmp/if_2277/`, `tmp/if_2279/`, `tmp/if_2281/`. Public no-login surfaces: `/llm/blackboard/**`, `/llm/signals/**`, `/llm/products/if-switchboard/**`. |
| When | 30/60/90 minutes: refresh endpoint registry, queue depth, and lease status. 3/6/9 hours: reconcile runtime behavior with published wording after code changes. Day-scale: user testing, external reviewer pass, publication gate. |
| How | Append-only HMAC-SHA256 signed ledgers; five enforcement points; attestation lifecycle with reason-coded delivery decisions; adaptive heartbeat daemon; claim-boundary discipline against a black/white registry. |

*If the v1.2 and v1.4 boundary is fuzzy at the top, review decisions are made against stale claims.*

## Problem Statement

The core risk in releasing `if.switchboard` documentation is inference inflation: reviewers mistake reachability and active traffic for universal enforcement guarantees.

Four concrete failure patterns addressed by this revision:

1. **[Resolved P0] Register-only quarantine is security theatre.** When Phase 1 initially targeted only the `register` endpoint, quarantined endpoints could still receive calls, drain queued messages, and appear in routing responses. Enforcement without propagation is not enforcement.

2. **[Closed with operator detection; code mitigation deferred] Live room chat is not the same as governed delivery.** Built-in room agents (`if.agent.executor`, `if.agent.critic`, `if.agent.orchestrator`) produce plausible coordination language in real time but do not run inference. The `targeted_gate_passed` field in bridge response JSON distinguishes real delivery from ghost agent responses — a distinction invisible to any reviewer reading room output alone.

3. **[Active P1] Documentation drift creates procurement risk.** Published canonical surfaces remained at v1.2 while the runtime moved through Phase 1/2 hardening. Any claim made against the published pack without noting the delta is a stale claim.

4. **[Active P1] Tooling mismatch can silently hide attestation history.** `GET /sip/attestations` requires camelCase `endpointId`; clients using `endpoint_id` can receive empty/incorrect results and misclassify endpoint state.

*When enforcement scope is stated as broader than what the code checks, the stated scope is the lie.*

## Goal

Produce a single document that a skeptical external reviewer can use to:

- Classify any specific `if.switchboard` claim as proven, bounded, or unproven.
- Replay the enforcement checks from public no-login surfaces and the listed verification commands.
- Understand the delivery model precisely enough to distinguish live-answer, voicemail, and blocked modes.
- See where the agent lifecycle contract and attestation plane extend the base routing control plane.

Secondary goal: keep product proposition language (packaging, SLA posture, proof cadence) in sync with runtime evidence posture so that commercial and technical claims are never further apart than one weekly evidence refresh cycle (<=7 days).

*If a reviewer cannot classify the claim in one read, the boundary is still too weak.*

## Execution-time Model

Work in these windows:

- **30/60/90 minutes**: refresh endpoint registry, gate status, queue depth, signature mode. Run lint against any wording change. Operator must be present for real-time SIP checks.
- **3/6/9 hours**: reconcile any runtime code change with wording in this document. Run enforcement matrix. Update claim registry if scope changes.
- **Day-scale**: user testing takes days even under accelerated process. Publication gate, external reviewer pass, and formal approval require separate scheduling.

Two clocks now run in parallel:

- *Runtime clock*: SIP heartbeat intervals (4–45s), lease TTL (60–300s), queue drain timing.
- *Evidence clock*: evidence refresh cadence, wording gate checks, reviewer packet updates.

If these clocks drift, published language can become stale while the runtime continues to evolve. Maximum accepted drift for this paper is 24 hours, enforced by the publish-gate freshness check in Release Language Guardrails.

*If cadence slips, yesterday's proof becomes today's over-claim.*

## Document Navigation by Audience

Navigate directly to the section that answers your specific decision question; reading only one lane without Claims Discipline can inflate assurance beyond what the evidence supports.

| Audience | Register mode | Section | Decision question answered |
|---|---|---|---|
| Executives / Business Leaders | `abstract-first` | [Executive Decision Surface](#executive-decision-surface) | Can we use `if.switchboard` in product/partner language today? |
| Power Users / Operators | `domain-native` | [Operational Runbook View](#operational-runbook-view) | How do I run, monitor, and recover a SIP-backed agent session? |
| Engineers / Implementers | `domain-native` | [Implementation View](#implementation-view) | What does the enforcement stack check, and where are the known gaps? |
| LLM Runtime Developers | `domain-native` | [Runtime Contract View](#runtime-contract-view) | What can a downstream agent runtime rely on for delivery guarantees? |
| External Reviewers / Auditors | `mixed` | [Claims Discipline](#claims-discipline), [Evidence Hierarchy](#evidence-hierarchy), [External Reviewer Packet](#external-reviewer-packet) | What is independently replayable vs operator-corroborated? |
| Product / Commercial | `mixed` | [Product Proposition](#product-proposition) | What can be said about packaging, SLA, and proof cadence right now? |

Operator-facing sections: Operational Runbook View, Appendix A.
Reviewer/auditor sections: Claims Discipline, Evidence Hierarchy, External Reviewer Packet, Appendix B.

*Wrong audience routing creates certainty the system never earned.*

## System Diagram

This diagram traces the full runtime path from call initiation to verified decision context, including live dispatch, voicemail fallback, and policy enforcement at every hop.

```mermaid
flowchart TD
  A[Caller endpoint] -->|POST /sip/call| B{Target live in room?}
  B -->|yes — immediate| C[sip.call dispatch]
  B -->|no — voicemail| D[Redis queue sip:queue:<endpoint> TTL=-1]
  D -->|await heartbeat| HB[POST /sip/heartbeat (adaptive 4–45s)]
  HB -->|drain| E[sip.call.dequeued dispatch]
  C --> F[Receiver agent inference]
  E --> F
  F -->|POST /sip/call reply| A

  G[POST /sip/register] --> H[Ownership checks]
  H --> I{allow / deny / quarantine / revoke}
  I -->|allow| J[Route / call / queue — enforced delivery]
  I -->|deny| P[REGISTRATION_DENIED]
  I -->|quarantine| K[Heartbeat only — no payload delivery]
  I -->|revoke| L[TARGET_ENDPOINT_REVOKED — blocked all paths]

  M[POST /sip/attest · POST /sip/revoke] --> R[Endpoint state mutation]
  R --> I
  R --> N[HMAC-SHA256 signed JSONL ledger]
  T[GET /sip/attestations] --> N
  N --> O[/llm/blackboard + /llm/signals evidence surfaces]
```

ASCII fallback:

```text
caller
  └─► POST /sip/call
        ├─ target live?  ──YES──► dispatch immediately ──► receiver ──► reply call
        └─ target absent ──NO───► Redis queue (TTL=-1) ──► heartbeat(4–45s) ──► drain ──► receiver ──► reply call

POST /sip/register
  └─► ownership checks
        ├─ allow          ──► route/call/queue enforced
        ├─ deny           ──► registration rejected
        ├─ quarantine     ──► heartbeat only, no payload
        └─ revoked        ──► TARGET_ENDPOINT_REVOKED all paths

POST /sip/attest | POST /sip/revoke ──► endpoint state mutation ──► affects future delivery decisions
state changes + attestation reads ──► signed JSONL ledger ──► /llm/blackboard evidence
```

Interpretation: the system attempts live delivery first. If the target is not present, the call enters a queue that persists indefinitely (Redis TTL=-1) until the target heartbeats and drains. Policy state (quarantine, revoke) is checked at every delivery decision point — not only at registration time.

*If any hop is implicit, assurance degrades into narrative.*

## Executive Decision Surface

This section provides decision-ready language tied to current measurable posture, for stakeholders who need a binary status summary rather than technical depth.

### Decision table (current posture — 2026-03-02)

| Decision question | Current answer | Evidence basis | Risk if ignored |
|---|---|---|---|
| Is live inter-agent call delivery proven? | Yes — recorded handshake, callId `8a0f2c3a`, 2026-03-02T02:43:15Z | `tmp/if_2279/rook014_received_call.json` | False "unproven" narrative delays legitimate use |
| Is quarantine enforced across all delivery paths? | Yes — five enforcement points verified | `tmp/if_2277/` proof artifacts | Register-only security theatre persists |
| Is attestation/revoke part of active enforcement? | Yes — reason-coded delivery decisions in place | `tmp/if_2281/matrix_*/` artifacts | Trust lifecycle unmanaged |
| Is voicemail-style queue delivery durable? | Yes — Redis TTL=-1 confirmed, survives relay restart | Runtime redis-cli TTL check, Tier B | Queue persistence assumed, not verified |
| Is GA / certification language justified now? | No — status is `preview` | Dual-gate snapshot: knowledge scope MET, routing fidelity NOT MET with open P1 findings | Procurement over-claim |
| Is the published canonical pack current? | No — v1.2 published, v1.3 draft, v1.4 this doc | `docs/712-if-switchboard-status-snapshot-v1.0-2026-03-02T045025Z.md` | Reviewers reading v1.2 miss Phase 1/2 hardening |
| Can we describe `if.switchboard` as operational and transparent? | Yes | Public `/llm/blackboard/**` and `/llm/signals/**` no-login access | False "inactive" narrative |

### Freshness snapshot for this revision

- **IF-2276**: Redis LIST debate relay with append-only `thread.jsonl`. This is the channel where the P0 enforcement gap was identified under adversarial discussion and Phase 1 scope was expanded from one checkpoint to five checkpoints.
- **IF-2277**: Five enforcement points on register/call/queue-drain/route-direct/route-next-available. Plus heartbeat carve-out (quarantined endpoints can heartbeat but cannot receive payloads). HMAC-SHA256 signed audit chain.
- **IF-2279**: Live cross-agent SIP handshake — rook-014 opened 180s listener window, rook-002 called, received in ~2s. First independently recorded two-agent coordinated action on this host.
- **IF-2281**: Phase 2 attestation plane — `POST /sip/attest`, `POST /sip/revoke`, `GET /sip/attestations`, append-only JSONL ledger with `prev_entry_hash` chain. Reason-code hardening: `TARGET_ENDPOINT_REVOKED` vs `TARGET_ENDPOINT_QUARANTINED` now distinct in delivery responses.
- **IF-2282**: Adaptive heartbeat controller in daemon — 4s min, 45s max, lease guard at ≤75s remaining TTL, pre-nudge watch at 70% of 60s nudge timeout.

*If decision language outruns evidence, rollback starts with words first.*

## Operational Runbook View

This runbook converts claim boundaries into repeatable runtime checks that operators can execute without additional context or escalation.

### Operating mode model

Five distinct operating modes operators must distinguish:

| Mode | Condition | Behavior | Recovery |
|---|---|---|---|
| **Live-answer** | Target has active room WebSocket presence | Call dispatched immediately, sub-100ms delivery | N/A — normal path |
| **Voicemail** | Target registered but not currently live | Call queued at `sip:queue:<endpoint>` (TTL=-1) | Wait for target heartbeat drain; no action needed if daemon is running |
| **Offline mailbox** | Target lease expired or never registered (`unroutable`) | Call cannot route; no delivery mode emitted | Re-register target endpoint before retrying call |
| **Blocked — quarantine** | Target registered under unattested namespace | Heartbeat succeeds; call/queue-drain/route blocked | Attest the endpoint via `POST /sip/attest` |
| **Blocked — revoked** | Target explicitly revoked | All paths blocked: `TARGET_ENDPOINT_REVOKED` | No unblock path without new registration cycle |

### Measured latency envelope (observed on mtl-01, 2026-03-02)

| Step | Measured range | Notes |
|---|---|---|
| `POST /sip/call` queue write | 20–46 ms | Redis-backed enqueue path |
| Heartbeat poll align | 0–8 s | Zero if heartbeat fires immediately; up to base interval otherwise |
| Queue drain | 28–42 ms | When heartbeat poll aligns immediately |
| Inference (DeepSeek in daemon) | ~2.8–3.0 s | Dominant per-turn cost; provider-dependent |
| Return `POST /sip/call` reply | 17–20 ms | Symmetric call path |
| **Total — best case** | ~3 s | Queue write + immediate drain + inference |
| **Total — worst case (45s poll)** | ~48 s | Queue write + full idle backoff cycle + inference; occurs when lease guard is not active and no traffic has reset interval |
| **Inference provider failure** | no reply for that turn | Daemon logs inference error, skips response, heartbeat loop continues; next turn/nudge can recover |

Analogy: this is voicemail, not email. There is a ring attempt first (live dispatch). Only if no answer does the call queue. The caller does not need to know which mode fired — the delivery outcome is identical from the payload receiver's perspective.

### Adaptive heartbeat profile

| Condition | Interval | Trigger logic |
|---|---|---|
| Active traffic received | 4s (min) | Reset to minimum on any incoming call |
| Idle — no traffic | +4s per cycle, up to 45s | Linear backoff preserves server capacity |
| Lease guard | 4s (min) | Fire at minimum when `leaseExpiresAt` ≤ 75s remaining |
| Pre-nudge watch | ≤5s | When partner silence approaches 70% of 60s nudge threshold |
| Heartbeat failure | immediate re-register | On 4xx/5xx heartbeat response |

Total idle backoff time before reaching 45s maximum: approximately 220s (4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 45 — 11 steps).

### Runtime health gates — operator checklist

1. Endpoint registered and lease valid (`leaseExpiresAt` > now).
2. Endpoint not quarantined for delivery paths (check `attestation_state` in registry).
3. Queue depth bounded and draining (monitor `sip:queue:<endpoint>` key depth).
4. Nudge logic fires when partner silence exceeds 60s threshold.

### Publication health gates — document checklist

1. Bible resolver verification passes (`ok=true`).
2. Strict scaffold lint passes (`diagram`, `audience-nav`, `anchor-stress`).
3. Blocked-phrase scan returns zero matches.

### Fallback and recovery ladder

1. **Partner not responding** — nudge fires at 60s silence; if still no response, re-check registration and queue depth.
2. **Lease expired** — re-register endpoint; queued calls survive lease expiry and will drain after re-registration.
3. **Relay restarted (high-impact known limitation)** — in-memory SIP registry is cleared; re-register and re-attest all endpoints before delivery recovers. Queued calls in Redis survive relay restart (`TTL=-1`), but attestation and lease states must be reconstructed.
4. **Attestation rejected** — verify token hash against `sip_endpoint_owners.json`; check that `from_endpoint_id` field is used (not deprecated `caller_endpoint_id`).
5. **Queue not draining** — confirm heartbeat is running with valid lease; confirm endpoint attestation state allows queue-drain path.

*Skipping gates under pressure turns preview risk into incident risk.*

## Implementation View

This section maps concrete components to enforcement behavior and documents known implementation boundaries so engineers can locate and verify each claim independently.

### Core component map

| Component | File / Path | Responsibility | Current state |
|---|---|---|---|
| SIP bridge server | `tmp/codex-bridge-chat/server.js` | Endpoint registry, call routing, queue, attest/revoke APIs | Active |
| SIP endpoint registry | Redis — host 127.0.0.1:6379 (SIP sidecar) | Lease storage, ownership state, attestation state | Active |
| Call queue | Redis key `sip:queue:<endpoint>` | Store-and-forward, TTL=-1 | Active |
| Autonomous daemon | `scripts/if_agent_daemon.py` | Register → adaptive heartbeat → drain → inference → reply | Active, operator-controlled |
| Attestation CLI | `scripts/if_sip_attest.py` | `attest`, `revoke`, `list` subcommands with JSONL audit log | Active |
| Daemon control | `scripts/if_agent_daemon_ctl.sh` | Start/stop/status wrapper for daemon | Active |
| Systemd unit | `/etc/systemd/system/if-agent-daemon@.service` | Templated unit; `Restart=always`, `NoNewPrivileges=true` | Active |
| Debate relay | `scripts/if_debate_turn.sh` | Redis LIST turn exchange and append-only `thread.jsonl` | Active |
| Endpoint ownership | `.codex/sip_endpoint_owners.json` | Static token-hash → endpoint map for ownership seeding | Active |
| Attestation ledger | `tmp/codex-bridge-chat/evidence/sip_attestations.jsonl` | Append-only HMAC-SHA256 signed attestation/revoke log | Active |

Note: Host Redis at 127.0.0.1:6379 is the SIP sidecar. It is separate from CT240 Redis at CT240:6380 (LiveKit). The `if.bus` spine is NATS JetStream, not Redis — Redis is explicitly the SIP-sidecar transport only.

### Phase 1: SIP Ownership Enforcement (IF-2277)

Five enforcement points delivered:

| Enforcement point | Trigger | Behavior on quarantined target |
|---|---|---|
| `POST /sip/register` | Namespace reservation check + token-hash ownership | `RESERVED_NAMESPACE_DENIED` or quarantine on mismatch |
| `POST /sip/call` | Pre-delivery state check | Payload blocked; heartbeat-only carve-out preserved |
| `GET /sip/queue` drain | Queue drain gate check | Drain blocked for quarantined endpoints |
| `POST /sip/route/direct` | Direct route resolution | Quarantined endpoints excluded |
| `POST /sip/route/next-available` | Pool selection | Quarantined endpoints excluded from candidate set |

Audit chain: every block event emits a signed audit record with `token_hash` and `reason_code`. The audit chain uses `prev_entry_hash` linking — a deleted or modified entry breaks the chain.

Known protocol attribution note: use `from_endpoint_id` (not deprecated `caller_endpoint_id`) when calling the SIP API. The wrong field causes audit events to show `from: if.api.sip` instead of the actual caller endpoint.

### Phase 2: Attestation Plane (IF-2281)

Three new APIs:

| API | Method | Behavior |
|---|---|---|
| `/if/api/v1/sip/attest` | POST | Promote endpoint from quarantine to attested state; clears delivery block |
| `/if/api/v1/sip/revoke` | POST | Permanently block endpoint; `TARGET_ENDPOINT_REVOKED` on all delivery paths |
| `/if/api/v1/sip/attestations` | GET | List attestation history; requires `endpointId` (camelCase) query param |

Reason-code matrix post-Phase 2:

| State | Register | Call delivery | Queue drain | Route | Validation coverage |
|---|---|---|---|---|---|
| Unregistered | N/A | `TARGET_NOT_FOUND` | N/A | excluded | tested on call path |
| Quarantined | quarantine record written | blocked | blocked | excluded | tested |
| Attested | allowed | delivered | delivered | included | tested |
| Revoked | blocked | `TARGET_ENDPOINT_REVOKED` | blocked | excluded | tested |

Known implementation caveats:
- `GET /sip/attestations` requires camelCase `endpointId` param; snake_case `endpoint_id` returns empty.
- Revoke `actorId` attribution shows `if.api.static` instead of the requesting actor (auth middleware override; attest path threads actor correctly).
- Reason codes are uppercase in call delivery responses (`TARGET_ENDPOINT_REVOKED`) and lowercase in routing responses (`target_endpoint_revoked`) — naming artifact, not semantic difference.

### Agent Lifecycle Contract (doc 710)

The native agent lifecycle contract (`docs/710-if-switchboard-agent-lifecycle-spec-v1-2026-02-27.md`) defines a formal FSM layered above the SIP session:

**State machine:**

```text
spawning → ready → running → waiting → completed
                                     ↘ failed
                                     ↘ timed_out
                         → closed (terminal from any state)
```

**Core operations:**

| Operation | API path | Description |
|---|---|---|
| spawn | `POST /if/api/v1/sip/agents` | Create agent with `task_id`, `sid`, `owner`, `capabilities` |
| message | `POST /if/api/v1/sip/agents/{id}/message` | Send payload to running agent |
| wait | `GET /if/api/v1/sip/agents/{id}/status` | Poll agent state; returns FSM state + last heartbeat |
| close | `DELETE /if/api/v1/sip/agents/{id}` | Graceful shutdown; records closeout evidence |
| interrupt | `POST /if/api/v1/sip/agents/{id}/interrupt` | Force state transition without normal completion path |
| heartbeat | `POST /if/api/v1/sip/agents/{id}/heartbeat` | Lease keepalive; prevents `timed_out` transition |

Rollout phases: Phase A (shadow — log only) → Phase B (enforce ownership, advisory on FSM) → Phase C (strict FSM enforcement, fail-closed) → Phase D (promotion to stable).

Current posture: Phase A/B boundary.
- Production-enforced now: endpoint ownership checks plus quarantine/revoke blocking across register/call/queue-drain/route-direct/route-next-available.
- Advisory/staging now: strict lifecycle transition rejection and full fail-closed FSM behavior.

### Autonomous Inference Daemon (if_agent_daemon.py)

The daemon closes the gap between SIP routing infrastructure and actual agent conversation autonomy:

```
start
  └─► register endpoint (agent.<alias>)
        └─► heartbeat loop [adaptive interval]
              ├─ drain queued calls if present
              │     └─► DeepSeek inference on call text
              │           └─► POST /sip/call reply to caller
              └─ nudge if partner silent > 60s
                    └─► POST /sip/call "are you still there?"
```

Key implementation note: the daemon uses `from_endpoint_id` (canonical field; see Phase 1 attribution note) for all outbound calls. Sessions are isolated via `.codex/sip_session_{alias}.env` files loaded by the systemd unit.
Failure behavior note: if inference fails, daemon logs the error and skips that response turn; it does not crash and continues heartbeat + queue-drain loop.

### Debate Relay (IF-2276)

Redis LIST queues at `debate:inbox:rook-014` and `debate:inbox:rook-002`. LPUSH to post, BRPOP to drain. Each turn is appended to an append-only `thread.jsonl` log. The relay served as the structured communication channel through which the Phase 1 enforcement scope was negotiated and agreed (Turn 6 — Codex flagged register-only as security theatre; Turn 8 — five-point scope agreed).

*Open P0/P1 vectors make wording upgrades indefensible.*

## Runtime Contract View

This contract specifies how agent-to-agent coordination behaves at runtime and what downstream systems may rely on, including what this contract explicitly does not guarantee.

### Contract entities

- **Endpoint**: semantic identity `agent.<alias>`, registered against token-hash ownership.
- **Call**: directed message with `from_endpoint_id`, `target_endpoint_id`, `text`, and optional metadata.
- **Queue item**: deferred call for non-live endpoints; persists indefinitely (TTL=-1) independent of lease state.
- **Heartbeat**: lease refresh that optionally triggers queue drain; adaptive interval 4–45s.
- **Attestation state**: `quarantined` | `attested` | `revoked` — applied at every delivery decision point.
- **Lease**: time-bounded registration validity; `defaultLeaseMs: 60000`, `maxLeaseMs: 300000`. Daemon requests 300s; server grants 60s by default (not a mismatch — server enforces its ceiling).

### Contract APIs (current surface)

```
POST   /if/api/v1/sip/register
POST   /if/api/v1/sip/heartbeat
POST   /if/api/v1/sip/call
GET    /if/api/v1/sip/queue
POST   /if/api/v1/sip/route/direct
POST   /if/api/v1/sip/route/next-available
POST   /if/api/v1/sip/attest
POST   /if/api/v1/sip/revoke
GET    /if/api/v1/sip/attestations?endpointId=<endpoint>
POST   /if/api/v1/sip/agents          (lifecycle contract — Phase A/B)
POST   /if/api/v1/sip/agents/{id}/message
GET    /if/api/v1/sip/agents/{id}/status
DELETE /if/api/v1/sip/agents/{id}
POST   /if/api/v1/sip/agents/{id}/interrupt
POST   /if/api/v1/sip/agents/{id}/heartbeat
```

Note: `route/direct` and `route/next-available` are POST endpoints, not GET. Sending GET returns 404.

Lifecycle API stability:
- `POST /sip/agents`, `/message`, `/status`, `/interrupt`, `/heartbeat`, `DELETE /agents/{id}` are **preview/experimental** at the current Phase A/B boundary.
- Base SIP APIs (`register`, `heartbeat`, `call`, `queue`, `route/*`, `attest`, `revoke`, `attestations`) are **active preview** and subject to additive-only changes.

### Delivery modes

| Mode | `delivery_mode` field | Trigger condition |
|---|---|---|
| `immediate` | `sip.call` | Target has active room WebSocket at time of call |
| `queued` | `sip.call.dequeued` | Target not live; call retained in Redis queue |
| `blocked` | not delivered | Quarantine or revoke policy gate — `reason_code` field explains |
| `unroutable` | none | Target not registered / lease expired before delivery mode decision |

### Ghost agent trap

Verified identification method for built-in server cycle vs real inference delivery:

- Built-in room agents (`if.agent.executor`, `if.agent.critic`, `if.agent.orchestrator`) respond in real time and produce plausible coordination language.
- Real targeted delivery sets `targeted_gate_passed: true` in the bridge response JSON.
- Built-in server cycle never sets this field to true.
- Operators must check this field, not room output text, to confirm delivery reached an inference session.

### Contract boundary

The contract supports asynchronous delivery continuity with explicit policy-gated decisions. It does not imply:

- Exactly-once delivery across all modes.
- HA or partition-tolerance guarantees.
- Certification or SLA commitments from this runtime alone.

*If required fields are optional in practice, trust fails closed too late.*

## Claims Discipline

This section defines exactly what is proven, bounded, and unproven — the gate that any external reviewer must be able to replay before accepting a claim at face value.

### Dual-gate snapshot (as of 2026-03-02)

| Gate | Status | Evidence |
|---|---|---|
| Knowledge-scope gate | MET — 232 consecutive pass windows | `docs/data/if_switchboard_knowledge_scope.gate-status.json` (`evaluated_utc=2026-03-02T10:00:19Z`) |
| Sustained routing fidelity gate | NOT MET — 1/10 windows collected; minimum windows and minimum consecutive passes unmet | `docs/data/if_switchboard_if2022_routing_fidelity.gate-status.json` (`evaluated_utc=2026-02-20T09:48:28Z`) |

A gate is MET only when all checks pass across the minimum consecutive window. In this paper, a "window" means one hourly validation window (target cadence 1h, jitter tolerated). The routing fidelity gate cannot be declared MET while known P1 findings remain open.

### Claim registry

**Proven claims (Tier A — independently replayable):**

- `if.switchboard` SIP register/call/queue/route APIs are reachable and respond to authenticated requests.
- Five enforcement points are active: register, call, queue-drain, route/direct, route/next-available.
- Quarantined endpoints can heartbeat but cannot receive payloads.
- Attested endpoints receive calls normally.
- Revoked endpoints receive `TARGET_ENDPOINT_REVOKED` on all delivery paths.
- Inter-agent call delivery was demonstrated live: callId `8a0f2c3a`, 2026-03-02T02:43:15Z, ~2s latency.
- Queue items persist with Redis TTL=-1, independent of lease expiry or relay restart.
- Attestation/revoke ledger is append-only with `prev_entry_hash` chain.

**Bounded claims (Tier B — operator-corroborated, not independently replayable without relay access):**

- Adaptive heartbeat daemon operates at 4–45s intervals with lease-guard and nudge logic.
- Inference round-trip is approximately 3s best-case with DeepSeek API.
- Autonomous inter-agent conversation is possible with two running daemons (single call delivery is Tier A; sustained multi-turn autonomy remains Tier B).
- Debate relay produced the enforcement scope expansion from 1 to 5 enforcement points.

**Not proven / non-claims:**

- Exactly-once delivery semantics across all coordination lanes.
- HA / partition-tolerance assurances beyond observed Redis availability.
- Immunity from future bypasses without ongoing red-team verification windows.
- Compliance certification of any kind.
- Suitability for regulated workloads without supplemental evidence review.

### Non-claims

These prohibitions hold for this revision and cannot be softened without matching evidence:

- No claim of exactly-once semantics for voicemail delivery mode.
- No claim of multi-region HA or partition-tolerance.
- No claim that preview evidence equals compliance certification.
- No claim that every runtime path is permanently bypass-proof.
- No claim that queue persistence alone equals governance sufficiency.
- No claim that built-in room agents are interchangeable with inference sessions.

Publication rule: if a sentence can be read as "guaranteed", it must be removed or narrowed. Enforce with blocked-phrase scan (`guarantee|always|never fail|100%|bypass-proof`) plus human review for implicit guarantee framing.

*If proven and unproven states blur, stronger claims become invalid by default.*

## Release Language Guardrails

These guardrails bind document language to current evidence state; any wording that outpaces this boundary is blocked before publication regardless of how well-intentioned the framing is.

### Approved language

- "`if.switchboard` is a preview-status coordination control plane with active, no-login reviewer visibility."
- "SIP delivery supports live dispatch and queue-backed voicemail fallback with explicit policy gates at every delivery point."
- "Endpoint ownership, quarantine, attestation, and revoke are enforced at five delivery checkpoints."
- "Inter-agent call delivery is operationally demonstrated; the autonomous daemon model is operator-controlled and experimental."
- "Published canonical documentation remains v1.2; this v1.4 draft reflects Phase 1/2 hardening not yet on the public surface."

### Blocked language

- Any sentence claiming enforcement covers paths not listed in the Phase 1/2 tables.
- Any sentence claiming routing fidelity gate is MET while open findings exist.
- Any sentence implying the daemon runs without operator initiation or oversight. `systemd Restart=always` is operator-configured resilience, not autonomous initiation.
- Any sentence conflating built-in room agent responses with inference delivery.
- Any claim of exactly-once, HA, or certification.
- Any sentence implying the published pack (v1.2) covers Phase 1/2 hardening.

### Publish gate (preflight sequence)

1. Bible resolver verify (`if_bibles_latest.py verify`) — must return `ok: true`.
2. Scaffold lint (`lint_if_whitepaper_scaffold.py --require-diagram --require-audience-nav --require-anchor-stress`).
3. Path masking check — zero absolute local-root path literals in publishable output; internal references use repo-relative forms (`docs/...`, `tmp/...`, `scripts/...`).
4. Blocked phrase scan — zero matches.
5. Runtime evidence freshness check — gate-status file timestamp within 24h.

*If blocked phrases survive review, compliance tone cannot save the claim.*

## Product Proposition

Source basis: derived from `docs/709-if-product-proposition-data-patch-v1.0-2026-02-26.md` with v1.4 claim-boundary updates for current gate posture.

### Current packaging posture

| Offer | Description | Availability |
|---|---|---|
| **if.trace Verify (public, no-login)** | Artifact integrity verification — hash + public receipt. Positioned as immutability proof, not truth validation. | Live |
| **InfraFabric Control Plane Preview (pilot)** | `if.bus` + `if.switchboard` + `if.blackboard` + `if.gov` in bounded pilot. Governed orchestration with observable evidence debt. | Advanced preview |
| **Enterprise (design partner)** | Dedicated deployment / self-host options / RBAC+SSO roadmap by scope. Commercialization via contact + architecture cadrage + evidence plan. | Contact |

### SLA posture (recommended language)

| Stage | Language |
|---|---|
| Preview | "Best effort, non-contractual SLA." |
| Pilot (contractual) | Internal SLO + timestamped incidents + signed postmortem. |
| GA (future) | Planned SLA (target 99.9 → 99.95), service credits, explicit exclusions. Earliest realistic window currently estimated as Q3 2026 if gate and Phase 3 conditions are met (intent, not commitment). |

Market signal: mature actors publish conditional SLAs with service credits and explicit scope (service/plan). A preview product should not publish any claim of "high availability" without a contractual boundary.

### Proof cadence

| Frequency | Content |
|---|---|
| Weekly | Gate status summary + evidence debt update |
| Monthly | `if.trace` integrity snapshot + incident summary |
| Quarterly | External review pack — claims vs proofs |
| Annual | Compliance scope review — attestations, limits, third-party availability |

### Public communication boundary

To say:

- "if.trace is in production for integrity proof."
- "The remainder of the stack is in advanced preview with published operational evidence."
- "We separate runtime technical capability from commercial readiness."

Not to say:

- "Production-ready platform."
- "Enterprise SLA guaranteed."
- "End-to-end certified compliance."

*If commercial language runs ahead of runtime evidence, the gap is a liability.*

## 30/60/90 Plan

This plan sequences hardening and language updates without letting narrative outrun runtime; milestones without explicit outputs are not milestones.

### 30 days

- Close `from_endpoint_id` attribution gap in revoke path (actorId shows `if.api.static` instead of requesting actor).
- Fix `GET /sip/attestations` CLI param: `if_sip_attest.py list` must send `endpointId` (camelCase), not `endpoint_id`.
- Inject `DEEPSEEK_API_KEY` into `.codex/sip_session_{alias}.env` so the systemd unit is fully self-contained without manual env injection.
- Publish one signed weekly runtime posture summary for SIP + blackboard surfaces (HMAC-SHA256 signed JSONL summary plus linked receipt).
- Promote this v1.4 document to canonical public switchboard surface once publish-gate checks pass; publish explicit v1.2→v1.4 claims diff.

### 60 days

- Adversarial replay against register/call/queue/route paths — publish outcomes.
- Expand attestation workflows with operator review checkpoints (human-in-the-loop for revoke actions).
- Standardize daemon deployment profile for both peer agents; confirm both restart cleanly after relay restart.
- Debate conductor deliverable: design doc + prototype script that automates turn-taking and capture, with failover handoff to operator mode.

### 90 days

- Re-evaluate `preview` ceiling only if routing fidelity gate passes consistently over a sustained window.
- If gate regresses, publish explicit regression note and keep status unchanged.
- JWT / Phase 3 token migration: signed short-lived tokens with `sub`/`scope`/`tenant`/`project`; sunset static bearer token.
- NATS JetStream deployment: replace Redis Streams as `if.bus` spine; Redis scope narrows to SIP-sidecar only.
- Regression clause: any reopened P0/P1 in 30-day items freezes promotion and shifts 60/90-day milestones until remediation evidence is published.

Milestone discipline: dates and outputs must be explicit; claim strength cannot increase without matching evidence.

*If milestones slip without claim rollback, the roadmap itself becomes risk.*

## External Reviewer Packet

This packet is the no-login minimum for external technical review. No local access required.

**Published canonical surfaces (v1.2 — current public):**

```
https://infrafabric.io/llm/products/if-switchboard/full-explainer-v1.2.md.txt
https://infrafabric.io/llm/products/if-switchboard/full-explainer-v1.1.md.txt
https://infrafabric.io/llm/products/if-switchboard/index.md.txt
```

Verification stamp for canonical surfaces (`as_of_utc=2026-03-02T10:34:00Z`):

| URL | SHA-256 |
|---|---|
| `https://infrafabric.io/llm/products/if-switchboard/full-explainer-v1.2.md.txt` | `9af5ae267b2ed6fec8854d6e76642002dc312a3d33b1592ebe6479457ad6f4f0` |
| `https://infrafabric.io/llm/products/if-switchboard/full-explainer-v1.1.md.txt` | `1c0de184bf29a4a4fd001c30db2aeece39eb7f629ba7e551a2840ef317561ef7` |
| `https://infrafabric.io/llm/products/if-switchboard/index.md.txt` | `b689b1ec0d16de6956bf77c2775a77586bdd179adf1162159e47ed10dac4080d` |

**Coordination evidence (public no-login):**

```
https://infrafabric.io/llm/if.registry.json.txt
https://infrafabric.io/llm/blackboard/index.md.txt
https://infrafabric.io/llm/blackboard/tasks.open.md.txt
https://infrafabric.io/llm/blackboard/tasks.sessions.md.txt
https://infrafabric.io/llm/blackboard/tasks.search.md.txt
https://infrafabric.io/llm/signals/index.md.txt
https://infrafabric.io/llm/signals/recent.md.txt
https://infrafabric.io/llm/session-state.md.txt
```

What this packet supports:

- Reachability and transparency assertions.
- Active coordination surfaces.
- Explicit task status and claim boundaries.

What this packet does not support alone:

- Certification assertions.
- Blanket strict-enforcement assertions.
- Closed-adversary conclusion without Tier A/B supplemental evidence.

Note to reviewer: the v1.3/v1.4 hardening (Phase 1/2) is not yet published to the public surface. Operator-local artifacts at `tmp/if_2277/`, `tmp/if_2279/`, and `tmp/if_2281/` constitute Tier B evidence for the hardening claims. Replay instructions are in Appendix A.

Promotion gate for replacing v1.2 with v1.4:

1. Appendix A replay steps pass with expected outcomes.
2. Two open P1 findings (`L3-RT-03`, `L3-RT-04`) are closed or explicitly accepted with signed risk note.
3. Published v1.2→v1.4 claims diff is attached in the release packet.

*If private context is required to trust core claims, the packet is incomplete.*

## Evidence Hierarchy

This hierarchy separates independently replayable proof from operator-local corroboration so reviewers can weight each claim correctly without requiring private access.

| Tier | Evidence class | Reproducibility | Use in claims |
|---|---|---|---|
| **Tier A** | Public no-login surfaces; signed task snapshots with `prev_entry_hash` chain | High — any reviewer can replay | Primary for public status statements |
| **Tier A-stale** | Previously public evidence older than freshness threshold | Medium — replayable but not current-state-safe | Historical context only until refreshed |
| **Tier B** | Operator-run enforcement matrix; local daemon traces; relay-captured handshake JSON | Medium — reproducible with relay access and stated commands | Supporting; can be promoted after stable pass windows are published |
| **Tier C** | Narrative / operator testimony / session log excerpts | Low — not independently replayable | Context only; never sole basis for any public claim |

Promotion path: Tier B artifacts promote to Tier A only after: (1) verbatim replay instructions published, (2) consistent pass across >=10 consecutive verification windows, (3) human approval from accountable author.

Window definition for this promotion path: one verification window equals one hourly validation run (target cadence 1h, jitter tolerated).

Demotion path: Tier A evidence is demoted to Tier A-stale when freshness exceeds threshold, when a runtime change invalidates prior replay assumptions, or when an open P0/P1 directly touches the cited claim path.

*Operator testimony presented as independent proof fails audit instantly.*

## Appendix A: Verification Commands

Bible and scaffold gate:

```bash
python3 scripts/if_bibles_latest.py refresh
python3 scripts/if_bibles_latest.py resolve \
  --bible-id if.whitepapers.bible --channel authoring_default --format path
python3 scripts/if_bibles_latest.py verify \
  --bible-id if.whitepapers.bible \
  --pointer-index docs/208-if-whitepapers-bible-pointer-index.md
python3 scripts/lint_if_whitepaper_scaffold.py \
  --md docs/714-if-switchboard-full-explainer-v1.4-2026-03-02T090000Z.md \
  --require-diagram --require-audience-nav --require-anchor-stress
```

SIP/blackboard runtime checks (no-login):

```bash
curl -fsS https://infrafabric.io/llm/if.registry.json.txt \
  | jq '.products[] | select(.product_id=="if.switchboard") | {product_id,status,path}'
curl -fsS https://infrafabric.io/llm/blackboard/tasks.open.md.txt | head -n 30
curl -fsS https://infrafabric.io/llm/signals/recent.md.txt | head -n 20
```

Enforcement matrix replay (Tier B — requires relay access):

```bash
# Auth setup
# TOKEN must map to a hashed ownership entry in .codex/sip_endpoint_owners.json.
# Without a valid token, register/call/attest/revoke will be rejected.

# Phase 1 — five enforcement points
# 1. Register unattested → quarantine
curl -X POST http://localhost:3030/if/api/v1/sip/register \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"endpoint_id":"agent.test-001","lease_ms":60000}'

# 2. Call unattested → blocked
curl -X POST http://localhost:3030/if/api/v1/sip/call \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"target_endpoint_id":"agent.test-001","from_endpoint_id":"agent.rook-014","text":"hello"}'

# 3. Attest
curl -X POST http://localhost:3030/if/api/v1/sip/attest \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"endpoint_id":"agent.test-001","actor_id":"agent.rook-014","reason":"test attestation"}'

# 4. Call attested → delivered or queued
curl -X POST http://localhost:3030/if/api/v1/sip/call \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"target_endpoint_id":"agent.test-001","from_endpoint_id":"agent.rook-014","text":"hello"}'

# 5. Revoke → blocked all paths
curl -X POST http://localhost:3030/if/api/v1/sip/revoke \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"endpoint_id":"agent.test-001","actor_id":"agent.rook-014","reason":"test revoke"}'

# 6. List attestations (camelCase param required)
curl "http://localhost:3030/if/api/v1/sip/attestations?endpointId=agent.test-001" \
  -H "Authorization: Bearer $TOKEN"

# Negative test A: missing/invalid auth token on register
curl -i -X POST http://localhost:3030/if/api/v1/sip/register \
  -H "Authorization: Bearer invalid-token" \
  -d '{"endpoint_id":"agent.test-unauth","lease_ms":60000}'
# Expected: 401/403 auth failure, no successful registration record.

# Negative test B: call revoked endpoint
curl -i -X POST http://localhost:3030/if/api/v1/sip/call \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"target_endpoint_id":"agent.test-001","from_endpoint_id":"agent.rook-014","text":"should fail"}'
# Expected: blocked delivery with reason TARGET_ENDPOINT_REVOKED.

# Negative test C: wrong query param casing
curl -i "http://localhost:3030/if/api/v1/sip/attestations?endpoint_id=agent.test-001" \
  -H "Authorization: Bearer $TOKEN"
# Expected: empty/misleading result; use endpointId instead.
```

Queue durability check:

```bash
redis-cli -h 127.0.0.1 -p 6379 TTL "sip:queue:agent.rook-014"
# Expected: -1 (no expiry)
redis-cli -h 127.0.0.1 -p 6379 LLEN "sip:queue:agent.rook-014"
```

*If checks cannot be replayed verbatim, assertions remain testimony, not evidence.*

## Appendix B: Red-Team Closeout Summary

This appendix records the current closure posture of each hardening line identified through structured debate and adversarial review, including open items that still constrain status language.

- **L3-RT-01** (IF-2276 debate, Turn 6): Codex identified register-only enforcement as a P0 class risk — quarantine without enforcement propagation is security theatre. Resolution: expanded Phase 1 scope from 1 to 5 enforcement points. Status: **closed**.
- **L3-RT-02**: Ghost agent trap identified — built-in room agents produce plausible coordination language without inference. Resolution: `targeted_gate_passed` field documented; operators instructed to check JSON response not room text. Status: **closed (documented), code-level mitigation deferred**.
- **L3-RT-03** (open): `from_endpoint_id` vs `caller_endpoint_id` attribution gap in revoke path. Revoke actorId shows `if.api.static`. Status: **open P1 — target close date 2026-04-01**.
- **L3-RT-04** (open): `GET /sip/attestations` CLI param case mismatch (`endpoint_id` vs `endpointId`). Status: **open P1 — target close date 2026-04-01**.
- **L3-RT-05** (open): Relay restart clears in-memory SIP registry and attestation/lease state, forcing re-register + re-attest before delivery resumes. Status: **open P1 — accepted preview limitation until persistent registry backing is shipped**.

Current closeout posture:
- IF-2276: done.
- IF-2277: done.
- IF-2279: done.
- IF-2281: done — with two open P1 findings documented above.
- IF-2282 (adaptive heartbeat): done.
- Residual: preview, with continued verification required.

*Open fail lanes require constrained status, regardless of narrative quality.*

## Appendix C: Knowledge Graph — Additional Relevant Docs

The following documents were identified through knowledge-graph dependency analysis as directly relevant to the `if.switchboard` SIP extension work but were not included in the primary referenced corpus (docs 640/709/710/711/712/713). Each provides critical context for the design rationale, threat model, or operational integration patterns that underpin the extension architecture.

| Tier | Doc ID | Filename | Version/date cue | Relevance to SIP Extension Work |
|---|---|---|---|---|
| Foundational | 85 | `85-if-bus-runtime-spec.md` | runtime spec | Defines NATS JetStream as the `if.bus` message spine; clarifies that Redis is exclusively a SIP-sidecar transport. Essential for understanding queue semantics and how SIP interoperates with the broader event bus topology. |
| Foundational | 310 | `310-if-s2-intra-agent-comms-sip-redis-deep-dive-2026-02-06T005940Z.md` | 2026-02-06 | Deep-dive on SIP+Redis: signed envelope authentication, contamination controls, blocker protocol, and Redis key design patterns. Foundational design rationale for the production SIP layer. |
| Foundational | 364 | `364-if-context-if-blackboard-if-api-sip-dual-identity-and-global-async-wake-profile-v1-2026-02-09.md` | 2026-02-09 | Canonical reference for `agent_id` vs endpoint SIP URI/DID mapping, global async wake, push wake with if.trace challenge-response, and threat model (DID recycling, CID spoofing, replay). Direct prerequisite for understanding the attestation plane design. |
| Contextual | 601 | `601-if-trace-full-explainer-v1.0-2026-02-19T095245Z.md` | v1.0, 2026-02-19 | Details the `if.trace` audit trail and provenance tracking framework. Attestation/revoke decisions append HMAC-SHA256 signed JSONL ledger entries — if.trace is the broader audit framework those entries extend. |
| Contextual | 654 | `654-if-partner-llm-interoperability-and-custody-contract-v1.0-2026-02-22T032254Z.md` | v1.0, 2026-02-22 | Partner LLM interoperability and custody contract. Directly relevant when third-party agents register SIP endpoints and external integration custody requirements apply. |
| Contextual | 2256 | `2256-debates-and-redteams-orchestration-runbook-v1.2-2026-02-27.md` | v1.2, 2026-02-27 | Latest debate and red-team orchestration runbook. Governs the debate relay (IF-2276) operational pattern that produced the Phase 1 enforcement scope expansion from 1 to 5 enforcement points. |

### Graph query note

Knowledge-graph gate status at time of this revision: **232 consecutive pass windows, 100% pass rate** (`evaluated_utc=2026-03-02T10:00:19Z`). Windows are hourly validation windows (target cadence 1h, jitter tolerated). Gate-status metadata: `docs/data/if_switchboard_knowledge_scope.gate-status.json`.

*If the knowledge graph was not checked, the corpus may be incomplete and downstream claims inherit that gap.*

## Conclusion

This revision upgrades `if.switchboard` from a routing control-plane description to a runtime-verified, enforcement-hardened coordination system with a formal voicemail delivery model, an attestation lifecycle, and an autonomous daemon capability.

What is stronger now:

- Delivery continuity (voicemail queue, TTL=-1, survives relay restart).
- Identity and policy enforcement scope (five points, not one).
- Attestation lifecycle clarity (attest/revoke/list with reason-coded decisions).
- Measurable latency framing (3s best-case, 48s worst-case, operator-observed).
- Autonomous agent conversation without constant operator relay.
- Formal agent lifecycle FSM (doc 710) designed and in Phase A/B rollout (strict transition enforcement remains staging, not yet production-enforced).

What remains intentionally constrained:

- Certification language — preview status stands.
- Blanket strictness claims — two open P1 findings documented.
- Reliability claims beyond measured evidence windows.
- Published canonical pack — v1.2 is public; v1.4 is this draft.

Decision summary: keep `preview` language, keep hard wording gates, keep publishing evidence faster than marketing claims.

Pre-v1.5 bridge: close open P1 items, publish v1.4 to canonical surface, and keep Tier B to Tier A promotions tied to explicit hourly-window evidence.

*If the conclusion claims more than the evidence, the whole paper collapses at review time.*

*Style Guide: Whitepaper v4.22*
*Writing Standard Source: if.whitepapers.bible v4.22 — `docs/2264-if-whitepapers-bible-v4.22-2026-03-02T094707Z.md`*

## Related

- [[if.bus Full Explainer v1.5 (Switchboard-Integrated, Claim-Boundary Strict)]]
- [[if.switchboard + if.blackboard Unified Full Explainer v1.2 (Evidence-Dense)]]
- [[if.blackboard Full Explainer v1.2 (Four-Audience, Claim-Boundary Strict)]]
- [[Governance and PHAROS MOC]]
- [[Governed Revision Loop — Responsible Self-Improving Agents]]
