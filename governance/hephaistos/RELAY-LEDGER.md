---
type: governance-doc
title: RELAY LEDGER — Handoff Protocol and Audit Record
aliases:
- RELAY LEDGER — Handoff Protocol and Audit Record
- governance/hephaistos/RELAY-LEDGER
tags:
- governance
- ai
- hephaistos
- governance-doc
- relay
- arbitration
- ledger
- operator
- entry
- color-purple
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: governance
canonical_path: governance/hephaistos/RELAY-LEDGER.md
backlink_count: 3
backlinks:
- '[[wiki/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
- '[[governance/hephaistos/ORCHESTRATION]]'
---

# RELAY LEDGER — Handoff Protocol and Audit Record

**Status:** Active. Canonicalized 2026-04-26.  
**Predecessor:** Proposed schema at `ledgers/patches/2026-04-23/ledgers-proposed.md` (deferred since 2026-04-23).  
**Live record:** `ledgers/RELAY-LEDGER.md`

---

## Purpose

The Relay Ledger is the runtime audit record for all inter-agent transitions in the
three-agent stack and its specialist extensions. It is distinct from:

- **Handoff schemas** — define packet format; listed under Handoff Schema Registry below
- **Master Tracker** — records task-level work, decisions, and session summaries
- **ORCHESTRATION.md** — describes the workflow conceptually

The Relay Ledger records what *actually moved* between agents and how each transition
resolved. It is the audit trail for the handoff chain.

---

## Handoff Schema Registry

All defined inter-agent handoff schemas. The Relay Ledger references these by name;
it does not duplicate their content.

| Transition | Schema file |
|---|---|
| HEPHAISTOS → Queen Keyport (scope packet) | `hephaistos-to-queen-keyport.md` |
| Queen Keyport → Hermes (governance decision) | `queen-keyport-to-hermes.md` |
| Hermes → Queen Keyport (escalation) | `hermes-escalation-to-queen-keyport.md` |
| Operator → HENRY (research/writing task) | `operator-to-henry.md` |
| Operator → Gadget (frontier scouting/build) | `operator-to-gadget.md` |
| HEPHAISTOS → Specialist (guideline pull) | `hephaistos-to-specialist-guideline-pull.md` |
| Trismégiste → Operator (continuity report) | `trismegiste-to-operator.md` |
| Operator → resolution (arbitration directive) | Defined in `CO-EQUAL-AUTHORITY-DECISION.md` § Arbitration record minimum fields |

Schemas not yet formalized (Argus → Operator, Hermes → HEPHAISTOS scope return) are
recorded in the ledger as `schema: none` until schemas are written.

---

## Entry Format

Each relay event produces one ledger entry. Entries are append-only.

```
---
relay_id: <unique — format: RELAY-YYYYMMDD-NNN>
type: <task-init | H→QK | QK→Hermes | Hermes→QK | Hermes→H | H↔QK-conflict | QK→Operator | Operator→resolution | routing-complete | Operator→HENRY | Operator→Gadget | Argus→Operator | Trismégiste→Operator | meta | audit>
timestamp: <ISO-8601>
from_agent: <HEPHAISTOS | Queen Keyport | Hermes | Argus | HENRY | Gadget | Trismégiste | Operator>
to_agent: <HEPHAISTOS | Queen Keyport | Hermes | Argus | HENRY | Gadget | Trismégiste | Operator>
task_id: <uuid or descriptive-slug — must match upstream handoff packet if applicable>
schema_ref: <schema file used, or "none">
status: <dispatched | accepted | returned | blocked | escalated | arbitrated | resolved | complete>
summary: <one sentence — what is being relayed and why>
key_decisions: |
  - <decision 1>
  - <decision 2>
open_items: |
  - <item the receiving agent must address>
conflict_flag: <none | H/QK-conflict | right-arm-veto | both>
arbitration_ref: <tracker location of arbitration record, or "none">
veto_resolution: <not-applicable | resolved-by-queen-keyport | scope-revised-by-hephaistos | co-equal-arbitration-recorded | overridden-by-operator-arbitration>
diamond_eyes_cleared: <true | false | escalated | not-applicable>
provenance: <Claude-based | human-based | external | mixed>
human_confirmed: <true | false>
notes: <optional — degraded claims, open risks, or context>
---
```

---

## Entry Types

| Type | Writer | When |
|---|---|---|
| `task-init` | Operator or initiating agent | Task begins |
| `H→QK` | HEPHAISTOS | Scope packet dispatched |
| `QK→Hermes` | Queen Keyport | Governance decision issued |
| `Hermes→QK` | Hermes | Exception escalation |
| `Hermes→H` | Hermes | Scope issue returned |
| `H↔QK-conflict` | Detecting agent | Co-equal conflict declared; neither proceeds |
| `QK→Operator` | Queen Keyport | Conflict escalated to operator |
| `Operator→resolution` | Record-keeper (agent writing the tracker arbitration entry) | Operator directive issued |
| `routing-complete` | Hermes | Routing finished |
| `Operator→HENRY` | Operator | HENRY invoked directly |
| `Operator→Gadget` | Operator | Gadget invoked directly |
| `Argus→Operator` | Argus | Audit finding surfaced |
| `Trismégiste→Operator` | Trismégiste | Operator continuity report |
| `meta` | Any agent or Operator | Administrative (ledger creation, architecture changes) |
| `audit` | Auditing agent | Audit event |

---

## Protocol — When to Write

Every packet dispatch, conflict declaration, operator arbitration, and routing
completion must produce a relay entry. Undocumented transitions are protocol
violations. The entry is written at dispatch time, not after resolution.

**Blocking events** — the following must produce an entry with `status: blocked`
before any further action:

- Right-arm veto triggered on QK's governance decision
- H/QK conflict declared
- Hermes halts routing on `escalation_trigger.severity: critical`
- Operator arbitration requested but not yet issued

**Resolution entries** — when a blocked state resolves, a second entry is written
with `status: resolved`, referencing the original `relay_id` in `notes`.

---

## Integrity Rules

1. Every packet dispatch produces a relay entry. No silent handoffs.
2. Entries are append-only. No retroactive edits.
3. `relay_id` must be unique. Format: `RELAY-YYYYMMDD-NNN` (NNN = sequential within day).
4. Conflict entries are written before operator escalation, not after.
5. `status: blocked` entries must name the blocker explicitly in `notes`.
6. `arbitration_ref` must point to an existing tracker entry — not a placeholder or memory claim.
7. `diamond_eyes_cleared: false` blocks routing. Hermes returns packet to Queen Keyport.
8. `veto_resolution: overridden-by-operator-arbitration` requires the arbitration record to be present per `CO-EQUAL-AUTHORITY-DECISION.md` before the entry is considered complete.
9. A relay entry with `human_confirmed: false` is provisional. Work may proceed but the entry is flagged for operator review at session close.

---

## Relationship to Existing Records

| Existing artifact | Relationship to Relay Ledger |
|---|---|
| Handoff schemas | Define packet format. Relay entries reference schemas; they do not repeat packet content. |
| Master Tracker | Records task decisions and session summaries. Relay Ledger records inter-agent state transitions. Neither substitutes for the other. |
| Arbitration records (in tracker) | `arbitration_ref` in relay entries points to these. Arbitration record content is not duplicated in the ledger. |
| Escalation log (hermes-escalation-to-queen-keyport.md) | The escalation schema requires its own escalation log. Relay entries reference escalation events; the escalation log provides the full packet record. |
| `hq-disagreement-test-case.md` | Canonical test of the arbitration path. Ledger entry type `H↔QK-conflict` + `Operator→resolution` covers live instances of this scenario. |
| `ledgers/patches/2026-04-23/ledgers-proposed.md` | Predecessor proposal. Superseded by this document. |

---

## Archival

Monthly, on the 15th (aligned with the tracker archive cycle): move prior-month entries
to `ledgers/archive/RELAY-YYYY-MM.md`. The live ledger retains the current month only.

If the live ledger exceeds 500 entries before the 15th, mid-month archival is permitted
with an explicit `meta` entry recording the reason.

---

## Promotion Check Addition

The ORCHESTRATION_OPERATIONS.md Promotion Check must include:

- [ ] All relay entries for this task are complete and non-provisional
- [ ] No `status: blocked` entry without a corresponding `status: resolved` entry
- [ ] If `veto_resolution: overridden-by-operator-arbitration`: `arbitration_ref` points to a complete tracker record

## Related

- [[Governance and PHAROS MOC]]
- [[ORCHESTRATION]]
