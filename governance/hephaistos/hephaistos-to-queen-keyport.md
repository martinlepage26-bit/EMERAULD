---
type: governance-doc
title: HEPHAISTOS → Queen Keyport Handoff Schema
aliases:
- HEPHAISTOS → Queen Keyport Handoff Schema
- governance/hephaistos/hephaistos-to-queen-keyport
tags:
- governance
- ai
- hephaistos
- queen-keyport
- governance-doc
- keyport
- queen
- relay
- scope
- color-purple
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: governance
canonical_path: governance/hephaistos/hephaistos-to-queen-keyport.md
backlink_count: 10
backlinks:
- '[[.github/agents/hephaistos.agent]]'
- '[[.github/agents/queen-keyport.agent]]'
- '[[wiki/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
- '[[governance/global/HEPHAISTOS-STATUS]]'
- '[[governance/hephaistos/ORCHESTRATION]]'
- '[[governance/hephaistos/hephaistos-to-specialist-guideline-pull]]'
- '[[governance/hephaistos/queen-keyport-to-hermes]]'
- '[[hephaistos/agents/hephaistos]]'
- '[[memory/local-session/project_hephaistos]]'
entity_type: Workflow
entity_id: hephaistos_to_qk_handoff_workflow
entity_aliases: []
entity_confidence: high
---

# HEPHAISTOS → Queen Keyport Handoff Schema

## Purpose

This document defines the machine-checkable handoff from HEPHAISTOS (scope: forging) to Queen Keyport (scope: governance). It transmits the current scope definition for governance synthesis without making forging primary over governance. Queen Keyport may name preliminary constraints in parallel; incomplete handoffs are returned to HEPHAISTOS as scope-clarification requests, not hierarchy escalations.

---

## Required Fields

```json
{
  "handoff_version": "1.0",
  "task_id": "<uuid>",
  "timestamp": "<ISO-8601>",
  "origin_agent": "HEPHAISTOS",
  "destination_agent": "Queen Keyport",

  "scope": {
    "objective": "<what is being built, analyzed, revised, or decided>",
    "artifact_type": "<system | dataset | narrative | agent | analysis | policy | other>",
    "audience": "<who receives this artifact>",
    "evidence_required": "<what evidence or structure the artifact must be grounded in>"
  },

  "consequence_domain": {
    "primary": "<governance | interpretive | structural-power | research | writing | routing | mixed>",
    "secondary": "<optional second domain>",
    "severity": "<low | medium | high | critical>"
  },

  "skill_composition": {
    "primary_skill": "<skill-name>",
    "secondary_skills": ["<skill-name>", "..."],
    "right_arms_activated": ["philosopher", "fully-rounded-power-analyst"],
    "composition_rationale": "<why this composition>"
  },

  "failure_modes": [
    "<unacceptable outcome 1>",
    "<unacceptable outcome 2>"
  ],

  "open_risks": [
    "<named uncertainty or degraded claim>"
  ],

  "diamond_eyes_check": {
    "question": "Does this scope serve genuine flourishing?",
    "answer": "<yes | escalate | revise>",
    "notes": "<if not yes, what needs to change>"
  },

  "right_arm_veto_gate": {
    "philosopher_input": "<conceptual stakes identified>",
    "power_analyst_input": "<structural map or leverage analysis>",
    "divergence": "<none | named — both inputs forwarded to Queen Keyport>"
  }
}
```

---

## Validation Rules

1. All required fields must be present and non-empty.
2. `consequence_domain.severity` of `high` or `critical` triggers full five-lane review.
3. `diamond_eyes_check.answer` must be `yes` before the packet is treated as scope-complete. If `escalate` or `revise`, return to HEPHAISTOS for scope revision while Queen Keyport may record preliminary constraints.
4. If `right_arm_veto_gate.divergence` is not `none`, Queen Keyport receives both positions and synthesizes. Neither position is suppressed.
5. `open_risks` must be explicit — empty array is only valid when consequence severity is `low`.

---

## Completion Gate

Queen Keyport may treat the packet as complete only when:
- [ ] All required fields are present
- [ ] `diamond_eyes_check.answer` is `yes`
- [ ] `scope.objective` is unambiguous
- [ ] `consequence_domain.severity` is set and reviewed
- [ ] Right-arm inputs are both present (or explicitly marked as not applicable with rationale)

---

## Relay Ledger Requirement

Every dispatch of this packet must produce a relay entry in `ledgers/RELAY-LEDGER.md`
with `type: H→QK`. The entry is written at dispatch time. See `RELAY-LEDGER.md` for
schema and integrity rules.

---

## Status

**Active.** Created 2026-04-09 during Wave 3 governance architecture remediation.

## Related

- [[project_hephaistos]]
- [[queen-keyport.agent]]
- [[hephaistos.agent]]
- [[queen-keyport-to-hermes]]
- [[hephaistos-to-specialist-guideline-pull]]
- [[HEPHAISTOS-STATUS]]
- [[hephaistos]]
- [[Governance and PHAROS MOC]]
- [[ORCHESTRATION]]
