---
type: governance-doc
title: Queen Keyport → Hermes Handoff Schema
aliases:
- Queen Keyport → Hermes Handoff Schema
- governance/hephaistos/queen-keyport-to-hermes
tags:
- governance
- ai
- hermes
- hephaistos
- queen-keyport
- governance-doc
- veto
- keyport
- arbitration
- approve
- queen
- color-purple
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: governance
canonical_path: governance/hephaistos/queen-keyport-to-hermes.md
backlink_count: 6
backlinks:
- '[[.github/agents/hermes.agent]]'
- '[[.github/agents/queen-keyport.agent]]'
- '[[wiki/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
- '[[governance/hephaistos/ORCHESTRATION]]'
- '[[governance/hephaistos/hephaistos-to-queen-keyport]]'
entity_type: Workflow
entity_id: qk_to_hermes_handoff_workflow
entity_aliases: []
entity_confidence: high
---

# Queen Keyport → Hermes Handoff Schema

## Purpose

This document defines the machine-checkable handoff from Queen Keyport (scope: governance) to Hermes (scope: routing). Hermes receives this packet only after Queen Keyport has issued an explicit `approve` or `approve-with-constraints` decision. All other statuses are not routed to Hermes.

---

## Required Fields

```json
{
  "handoff_version": "1.0",
  "task_id": "<uuid — must match the originating hephaistos-to-queen-keyport handoff>",
  "timestamp": "<ISO-8601>",
  "origin_agent": "Queen Keyport",
  "destination_agent": "Hermes",

  "governance_decision": {
    "status": "<approve | approve-with-constraints | reject | bounded | degraded>",
    "rationale": "<why this decision>",
    "constraints": [
      "<mandatory constraint 1>",
      "<mandatory constraint 2>"
    ],
    "evidence_threshold": "<what level of evidence is required for claims in this task>",
    "refusal_conditions": [
      "<condition that would require escalation back to Queen Keyport>"
    ]
  },

  "mandatory_gates": {
    "diamond_eyes_passed": "<true | false>",
    "bias_check_required": "<true | false>",
    "research_ethics_required": "<true | false>",
    "right_arm_veto_cleared": "<true | false — both right arms either cleared or veto resolved>"
  },

  "routing_requirements": {
    "target_systems": ["<system-1>", "..."],
    "coordination_sequence": "<sequential | parallel | conditional>",
    "monitoring_metrics": ["<metric-1>", "..."],
    "escalation_triggers": ["<condition that returns work to Queen Keyport>"]
  },

  "open_risks": [
    "<named risk that Hermes must track>"
  ],

  "veto_status": {
    "philosopher_veto": "<none | triggered — must be resolved before routing>",
    "power_analyst_veto": "<none | triggered — must be resolved before routing>",
    "resolution": "<not-applicable | resolved-by-queen-keyport | scope-revised-by-hephaistos | co-equal-arbitration-recorded | overridden-by-operator-arbitration>"
  }
}
```

---

## Validation Rules

1. `governance_decision.status` must be `approve` or `approve-with-constraints` for routing to proceed. All other statuses block Hermes.
2. `mandatory_gates.diamond_eyes_passed` must be `true`. If `false`, route returns to Queen Keyport.
3. Both veto fields must be `none` or have a documented resolution before Hermes receives the packet. An unresolved triggered veto or unresolved Hephaistos/Queen Keyport conflict blocks routing.
4. `routing_requirements.escalation_triggers` must be non-empty — Hermes must always know when to return work to governance.
5. `task_id` must match the upstream HEPHAISTOS handoff. Orphaned routing packets (no upstream task_id) are rejected.
6. If `veto_status.resolution` is `overridden-by-operator-arbitration`, the arbitration record must exist in the tracker with all required fields (conflict_id, hephaistos_position, queen_keyport_position, right_arm_inputs, operator_directive, veto_active_at_arbitration, veto_supersession, timestamp, recorded_by) per `CO-EQUAL-AUTHORITY-DECISION.md`. A partial arbitration record does not satisfy this rule. If `veto_active_at_arbitration` is No and the operator directive is silent on veto coverage, the record-keeper must route to the operator for explicit confirmation before this packet is issued.

---

## Completion Gate

Hermes may begin routing only when:
- [ ] `governance_decision.status` is `approve` or `approve-with-constraints`
- [ ] `mandatory_gates.diamond_eyes_passed` is `true`
- [ ] Both veto fields resolved
- [ ] `routing_requirements.escalation_triggers` defined
- [ ] `task_id` matches upstream handoff
- [ ] If `veto_status.resolution` is `overridden-by-operator-arbitration`: tracker arbitration record exists with all required fields

---

## Relay Ledger Requirement

Every dispatch of this packet must produce a relay entry in `ledgers/RELAY-LEDGER.md`
with `type: QK→Hermes`. The entry is written at dispatch time. See `RELAY-LEDGER.md`
for schema and integrity rules.

---

## Status

**Active.** Created 2026-04-09 during Wave 3 governance architecture remediation.

## Related

- [[hephaistos-to-queen-keyport]]
- [[queen-keyport.agent]]
- [[hermes.agent]]
- [[Governance and PHAROS MOC]]
- [[ORCHESTRATION]]
