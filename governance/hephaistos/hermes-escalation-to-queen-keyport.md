---
type: governance-doc
title: Hermes → Queen Keyport Escalation Schema
aliases:
- Hermes → Queen Keyport Escalation Schema
- governance/hephaistos/hermes-escalation-to-queen-keyport
tags:
- governance
- ai
- hermes
- hephaistos
- queen-keyport
- governance-doc
- escalation
- keyport
- queen
- halted
- color-purple
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: governance
canonical_path: governance/hephaistos/hermes-escalation-to-queen-keyport.md
backlink_count: 6
backlinks:
- '[[.github/agents/hermes.agent]]'
- '[[.github/agents/queen-keyport.agent]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
- '[[governance/hephaistos/HEPHAISTOS]]'
- '[[governance/hephaistos/ethics-escalation-criteria]]'
---

# Hermes → Queen Keyport Escalation Schema

## Purpose

This document defines the machine-checkable escalation handoff from Hermes (scope: routing) back to Queen Keyport (scope: governance). Hermes sends this packet when routing or integration reveals a failure, constraint violation, scope drift, or governance-requiring decision. Queen Keyport receives the packet and issues a resolution.

---

## Required Fields

```json
{
  "escalation_version": "1.0",
  "escalation_id": "<uuid>",
  "timestamp": "<ISO-8601>",
  "origin_agent": "Hermes",
  "destination_agent": "Queen Keyport",

  "originating_task": {
    "task_id": "<must match the queen-keyport-to-hermes handoff task_id>",
    "original_governance_decision": "<approve | approve-with-constraints>",
    "constraints_in_effect": [
      "<constraint 1>",
      "<constraint 2>"
    ]
  },

  "escalation_trigger": {
    "type": "<constraint-violation | scope-drift | integration-failure | monitoring-anomaly | new-risk-discovered | authority-gap>",
    "description": "<specific description of what triggered escalation>",
    "severity": "<low | medium | high | critical>",
    "evidence": "<what Hermes observed — direct evidence only>"
  },

  "routing_status": {
    "was_work_halted": "<true | false>",
    "halt_reason": "<why routing was stopped, or 'not-halted'>",
    "affected_systems": ["<system-1>", "..."],
    "last_known_safe_state": "<description of state before the triggering event, or 'unknown'>"
  },

  "hermes_options": [
    {
      "option": "<option description>",
      "consequence": "<what this choice means for routing>",
      "risk": "<risk if this option is chosen>"
    }
  ],

  "escalation_class": "<return-to-governance | return-to-hephaistos | operator-required>",

  "argus_flag": "<none | flagged — if Argus audit is recommended due to this escalation>"
}
```

---

## Validation Rules

1. `escalation_id` must be unique. Duplicate escalation IDs are rejected.
2. `originating_task.task_id` must match a prior `queen-keyport-to-hermes` packet. Orphaned escalations (no upstream task_id) are rejected.
3. `escalation_trigger.severity` of `critical` triggers immediate halt — `routing_status.was_work_halted` must be `true`.
4. `hermes_options` must contain at least two options. Queen Keyport must have a choice, not a fait accompli.
5. `escalation_class` determines destination:
   - `return-to-governance` → Queen Keyport resolves and re-issues routing approval
   - `return-to-hephaistos` → Scope itself must be redesigned; Queen Keyport cannot resolve within current constraints
   - `operator-required` → Neither agent can resolve; Martin must decide

---

## Queen Keyport Resolution Options

Queen Keyport must respond with one of:

| Resolution | Meaning |
|---|---|
| `resume-with-modified-constraints` | Routing may resume; constraints updated to address the trigger |
| `resume-unchanged` | Hermes observation was within acceptable bounds; proceed |
| `halt-and-return-to-hephaistos` | Scope must be redesigned before routing can continue |
| `halt-pending-operator-decision` | Consequence too high for governance-only resolution |
| `invoke-argus` | Escalation reveals systemic governance concern; Argus audit required before any routing resumes |

---

## Completion Gate

Queen Keyport may issue a resolution only when:
- [ ] `escalation_id` is verified unique and `task_id` matches upstream handoff
- [ ] `escalation_trigger.evidence` is direct evidence, not assertion
- [ ] `hermes_options` contains at least two options with consequences named
- [ ] `routing_status.last_known_safe_state` is recorded (for rollback if needed)
- [ ] If `severity` is `critical`: `was_work_halted` is `true`

---

## Escalation Log

Every escalation and its resolution must be logged. No escalation may be silently dropped.

Log fields:
- `escalation_id`
- `timestamp`
- `trigger_type` and `severity`
- `queen_keyport_resolution`
- `resolution_timestamp`
- `routing_resumed`: `<true | false>`

---

## Relay Ledger Requirement

Every dispatch of this packet must produce a relay entry in `ledgers/RELAY-LEDGER.md`
with `type: Hermes→QK`. The entry is written at dispatch time. See `RELAY-LEDGER.md`
for schema and integrity rules.

---

## Status

**Active.** Created 2026-04-09 as part of Wave 3 governance architecture remediation (P1 remainder).
Completes the three-schema handoff loop: HEPHAISTOS → Queen Keyport → Hermes → (escalation) → Queen Keyport.

## Related

- [[ethics-escalation-criteria]]
- [[queen-keyport.agent]]
- [[hermes.agent]]
- [[Governance and PHAROS MOC]]
- [[HEPHAISTOS]]
