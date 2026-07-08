---
type: governance-doc
title: Operator → HENRY Handoff Schema
aliases:
- Operator → HENRY Handoff Schema
- governance/hephaistos/operator-to-henry
tags:
- governance
- ai
- hephaistos
- henry
- governance-doc
- preflight
- none
- task
- color-purple
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: governance
canonical_path: governance/hephaistos/operator-to-henry.md
backlink_count: 3
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
- '[[governance/hephaistos/HENRY]]'
---

# Operator → HENRY Handoff Schema

## Purpose

This document defines the machine-checkable handoff from the Operator (Martin) to HENRY for direct invocation. HENRY is an independent specialist at Argus level — invoked by the Operator, not routed through the HEPHAISTOS / Queen Keyport / Hermes chain. This schema captures the preflight constraints HENRY needs to do its job: the claim type it's permitted to make, the venue spec it's writing to, and the source material it's working from.

**Scope:** writing tasks — research papers, novels, policy briefs, workflow design, peer-review stress-tests. Any output that HENRY produces directly.

---

## Required Fields

```json
{
  "handoff_version": "1.0",
  "task_id": "<uuid — optional for one-shot invocations>",
  "timestamp": "<ISO-8601>",
  "origin_agent": "Operator",
  "destination_agent": "HENRY",

  "mode": "<research-to-paper | novel | governance-writing | workflow-design | peer-review-stress-test>",

  "preflight": {
    "format": "<IMRaD | humanities-social-theory | mixed-methods-policy | essay | novel | policy-brief | white-paper | grant-application>",
    "claim_type": "<descriptive | associational | causal | normative>",
    "venue": "<specific journal name | class name | client name | gumroad | linkedin | personal | none>",
    "word_limit": "<integer | range | none>",
    "abstract_length": "<integer | none>",
    "citation_style": "<APA | Chicago-notes | Chicago-author-date | Vancouver | AMA | MLA | none>",
    "figure_table_limits": "<integer | none>",
    "bilingual": "<en | fr | both | none>"
  },

  "task": {
    "objective": "<one-sentence statement of what HENRY is producing>",
    "input_artifacts": [
      "<path or inline content reference>"
    ],
    "output_expected": [
      "<draft | revision | claim-evidence-matrix | peer-review-critique | title-set | workflow-spec | continuity-note>"
    ],
    "author_voice_reference": "<path to existing manuscript for voice matching | none>"
  },

  "methodological_reference": {
    "consults_hephaistos": "<true | false>",
    "hephaistos_docs": [
      "/home/cerebrhoe/hephaistos/HEPHAISTOS.md",
      "/home/cerebrhoe/hephaistos/HEPHAISTOS_OPERATIONS.md",
      "/home/cerebrhoe/hephaistos/DIAMOND-EYES.md"
    ],
    "binding_level": "reference-only"
  },

  "deadlines": {
    "desired_delivery": "<ISO-8601 | none>",
    "hard_deadline": "<ISO-8601 | none>"
  },

  "known_constraints": [
    "<constraint-1>",
    "<constraint-2>"
  ],

  "escalation_triggers": [
    "<condition that requires HENRY to stop and escalate to Operator>"
  ]
}
```

---

## Validation Rules

1. `preflight.format` must be set — HENRY will not draft to an unspecified format.
2. `preflight.claim_type` must be set — HENRY will not draft when the allowed claim type is unspecified (prevents overclaiming).
3. `task.mode` must be one of the five defined modes. Unknown modes are rejected.
4. `task.input_artifacts` must be non-empty OR `task.objective` must explicitly state "operator will provide inline."
5. `methodological_reference.binding_level` must be `reference-only` — HEPHAISTOS guidelines are consulted, never commanded.
6. If `mode == novel`, `task.author_voice_reference` must be present when operating on an existing manuscript (voice continuity requirement).
7. If `mode == peer-review-stress-test`, `task.input_artifacts` must point to the manuscript being critiqued; HENRY acts as Reviewer-#2.

---

## Completion Gate

HENRY may treat the packet as complete only when:
- [ ] All required fields are present
- [ ] `preflight.format` and `preflight.claim_type` are both set
- [ ] `task.objective` is unambiguous
- [ ] At least one output is named in `task.output_expected`
- [ ] Source material is either in `input_artifacts` or explicitly marked inline

If any are missing, HENRY returns the packet with a scope-clarification request. This is **not** an escalation to the three-agent stack — HENRY returns to the Operator directly.

---

## What this schema does NOT include

- No governance-decision field. HENRY is not gated by Queen Keyport approval. QK may flag concerns about the output post-delivery; the Operator decides.
- No Hermes routing directive. HENRY's delivery is direct to Operator.
- No HEPHAISTOS binding-instruction field. HEPHAISTOS guidelines are consulted as `reference-only`.

---

## Status

**Active.** Created 2026-04-23 during Phase F remediation of the agent ecosystem audit (`AGENT_AUDIT_2026-04-23.md`), closes finding F-023.

## Related

- [[Governance and PHAROS MOC]]
- [[HENRY]]
