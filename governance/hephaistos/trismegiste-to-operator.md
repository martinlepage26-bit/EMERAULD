---
type: governance-doc
title: Trismégiste → Operator Delivery Schema
aliases:
- Trismégiste → Operator Delivery Schema
- governance/hephaistos/trismegiste-to-operator
tags:
- governance
- ai
- hephaistos
- trismegiste
- governance-doc
- delivery
- trism
- giste
- json
- pattern
- color-purple
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: governance
canonical_path: governance/hephaistos/trismegiste-to-operator.md
backlink_count: 3
backlinks:
- '[[CLAUDE]]'
- '[[wiki/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
entity_type: Workflow
entity_id: trismegiste_to_operator_delivery_workflow
entity_aliases: []
entity_confidence: high
---

# Trismégiste → Operator Delivery Schema

## Purpose

This document defines the machine-checkable delivery from Trismégiste to the Operator. Trismégiste is parallel — external to the three-agent hierarchy — and delivers synthesis directly to the Operator via persisted state files. This schema captures **what** was delivered, **where** it was persisted, and **whether** an operator action is needed.

**Scope:** personal knowledge synthesis, operator continuity, vault state, business-state updates, decision records, open questions.

---

## Required Fields

```json
{
  "schema_version": "1.0",
  "delivery_id": "<uuid — one per delivery event>",
  "timestamp": "<ISO-8601 — with timezone>",
  "origin_agent": "Trismégiste",
  "destination": "Operator",

  "delivery_type": "<active-threads-update | decision-record | open-question | synthesis-insight | vault-status | business-state-update | cross-project-pattern>",

  "content": {
    "summary": "<one-sentence statement of what's being delivered>",
    "detail": {
      "<delivery-type-specific fields — see examples below>"
    },
    "links": [
      {
        "target": "<wiki note | raw source | memory file | external resource>",
        "path": "<absolute or vault-relative path>"
      }
    ]
  },

  "persistence": {
    "written_to": [
      "<file path — typically session-state.md, trismegiste-state.md, or memory/daily/>"
    ],
    "timestamp_of_persistence": "<ISO-8601>",
    "append_or_overwrite": "<append | overwrite | merge>"
  },

  "action_needed": {
    "required": "<true | false>",
    "type": "<decision | review | ack-only | informational>",
    "by_when": "<ISO-8601 | next-session | none>",
    "what_to_decide": "<if type=decision: one-sentence framing of the decision point>"
  },

  "cross_layer_notes": [
    "<optional: if this delivery has implications for the three-agent stack, name them — but Trismégiste does not route to the stack directly; this is documentary>"
  ]
}
```

---

## Validation Rules

1. `persistence.written_to` must be non-empty — every delivery is persisted. Trismégiste does not make ephemeral deliveries.
2. `delivery_type` must be one of the seven defined types.
3. If `action_needed.required` is `true`, `action_needed.type` and `action_needed.what_to_decide` (or equivalent framing) must be set.
4. `links` should be non-empty for `delivery_type` values involving synthesis or cross-project-pattern — Trismégiste's synthesis is supposed to be linked into the vault graph, not standalone.
5. `cross_layer_notes` is advisory only; it does not route Trismégiste's output to the three-agent stack. Trismégiste remains parallel.

---

## Delivery-type-specific detail fields

### active-threads-update

```json
{
  "threads_changed": [
    {
      "thread_name": "<e.g., 'Paper 25 peer review', 'Lavoie onboarding'>",
      "old_status": "<previous state>",
      "new_status": "<current state>",
      "blockers": [],
      "next_action": "<what's next for this thread>"
    }
  ]
}
```

### decision-record

```json
{
  "decision": "<what was decided>",
  "decided_by": "Operator",
  "context": "<why this decision was made>",
  "implications": "<what changes as a result>",
  "reversibility": "<reversible | irreversible | bounded>"
}
```

### open-question

```json
{
  "question": "<the question>",
  "context": "<why it's open>",
  "candidate_answers": ["<option 1>", "<option 2>"],
  "blocking": "<what's blocked pending this question>"
}
```

### synthesis-insight

```json
{
  "insight": "<the pattern or connection Trismégiste observed>",
  "evidence": [
    {
      "source": "<wiki note / raw source / conversation trace>",
      "classification": "<direct-evidence | supported-inference | speculation>"
    }
  ],
  "implications": "<what this changes for ongoing work>"
}
```

### vault-status

```json
{
  "total_notes": "<integer>",
  "new_since_last_delivery": "<integer>",
  "orphans": "<count of notes without links>",
  "mocs_updated": ["<MOC name>"],
  "vector_store_status": "<current | stale | rebuilding>"
}
```

### business-state-update

```json
{
  "metric": "<e.g., '90-day revenue challenge progress'>",
  "previous_value": "<prior value>",
  "current_value": "<current value>",
  "delta_drivers": "<what caused the change>",
  "trend": "<on-track | behind | ahead | stalled>"
}
```

### cross-project-pattern

```json
{
  "pattern": "<the recurring pattern across projects>",
  "projects_observed": ["<PHAROS | DocSort | research | governance>"],
  "implications": "<what this suggests about operator-level strategy>"
}
```

---

## Persistence targets (canonical locations)

| Delivery type | Primary persistence |
|---|---|
| active-threads-update | `/home/cerebrhoe/trismegiste-state.md` + `EMERAULD/session-state.md` |
| decision-record | `EMERAULD/session-state.md` + relevant wiki note |
| open-question | `/home/cerebrhoe/trismegiste-state.md` (Open Questions section) |
| synthesis-insight | `EMERAULD/wiki/<topic>.md` (new or updated) + MOC link |
| vault-status | `EMERAULD/session-state.md` (Vault Status section) |
| business-state-update | `EMERAULD/memory.md` + `memory/daily/<date>.md` |
| cross-project-pattern | `EMERAULD/wiki/<pattern>.md` + relevant MOC |

---

## What this schema does NOT include

- No routing to HEPHAISTOS, Queen Keyport, or Hermes. Trismégiste is parallel — external to the hierarchy.
- No governance-decision field. Trismégiste reports, it does not govern.
- No approval gate. Operator reads and decides; Trismégiste does not wait for approval.

---

## Status

**Active.** Created 2026-04-23 during Phase F remediation of the agent ecosystem audit (`AGENT_AUDIT_2026-04-23.md`), closes finding F-025.

## Related

- [[Governance and PHAROS MOC]]
- [[CLAUDE]]
