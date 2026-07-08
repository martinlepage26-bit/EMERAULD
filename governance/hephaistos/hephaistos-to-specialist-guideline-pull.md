---
type: governance-doc
title: HEPHAISTOS ⇢ Specialist Guideline-Pull Schema
aliases:
- HEPHAISTOS ⇢ Specialist Guideline-Pull Schema
tags:
- governance
- ai
- hephaistos
- governance-doc
- consulted
- gadget
- specialist
- pull
status: active
domain: governance
created: '2026-06-21'
updated: '2026-06-26'
vault_area: governance
canonical_path: governance/hephaistos/hephaistos-to-specialist-guideline-pull.md
backlink_count: 5
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
- '[[governance/global/HEPHAISTOS-STATUS]]'
- '[[governance/hephaistos/CO-EQUAL-AUTHORITY-DECISION]]'
- '[[governance/hephaistos/hephaistos-to-queen-keyport]]'
---

# HEPHAISTOS ⇢ Specialist Guideline-Pull Schema

## Purpose

Machine-checkable record of a specialist (HENRY or Gadget) consulting HEPHAISTOS's methodological guidelines. This is a **pull**, not a **push** — HEPHAISTOS publishes guideline documents; specialists consult them as reference material. The schema documents **which** docs were consulted, **when**, and **what guidance was sought**.

**Scope:** any HENRY or Gadget invocation where methodological discipline matters. Enables post-hoc audit (by Argus or Operator) of whether the specialist honored the reference material.

---

## Required Fields

```json
{
  "schema_version": "1.0",
  "pull_id": "<uuid — one per pull event>",
  "task_id": "<uuid — matches the upstream operator-to-{henry|gadget} handoff>",
  "timestamp": "<ISO-8601>",
  "consumer": "<HENRY | Gadget>",
  "publisher": "HEPHAISTOS",
  "pull_type": "methodological-reference",

  "docs_consulted": [
    {
      "path": "<absolute path>",
      "section": "<section title or line range, if specific>",
      "consulted_for": "<what guidance was sought — one sentence>"
    }
  ],

  "derived_decisions": [
    {
      "decision": "<what the specialist decided based on consulted material>",
      "evidence_path": "<doc path + section that informed this decision>",
      "classification": "<direct-evidence | supported-inference | speculation>"
    }
  ],

  "binding_level": "reference-only",

  "conflict_log": [
    {
      "conflict": "<if operator's handoff preflight/constraints conflicted with consulted material>",
      "resolution": "<escalated-to-operator | operator-input-took-precedence | no-conflict>"
    }
  ],

  "security_reference_log": [
    {
      "security_doc_consulted": "<path — typically HEPHAISTOS_OPERATIONS.md or QUEEN-KEYPORT.md>",
      "guidance_found": "<what the doc said about this class of operation>",
      "specialist_action": "<proceeded | declined | escalated | sought-operator-clarification>"
    }
  ],

  "audit_hook": {
    "operator_can_inspect": true,
    "argus_can_audit": true,
    "queen_keyport_can_flag": true
  }
}
```

---

## Validation Rules

1. `binding_level` must always be `reference-only`. Structural guarantee that HEPHAISTOS publishes guidelines, not commands.
2. `docs_consulted` must be non-empty if the upstream `operator-to-{henry|gadget}` packet set `methodological_reference.consults_hephaistos = true`.
3. `derived_decisions[].classification` follows evidence-class discipline.
4. `conflict_log` must be non-empty if consulted material contradicted any part of the operator's input. Silent suppression is a refusal condition.
5. `security_reference_log` must be non-empty when the task involves credentials, secret files, or permission-scoped external systems (applies primarily to Gadget; optional for HENRY).

---

## Concrete examples

### HENRY consulting HEPHAISTOS for causal-claim evidence threshold

HENRY is drafting a paper; operator preflight says "causal claim." HENRY consults `HEPHAISTOS.md` § Consequence Classification for evidence requirements. Records:
- `docs_consulted`: HEPHAISTOS.md § Evidence Requirements; consulted_for "causal-claim evidence threshold"
- `derived_decisions`: "Paper requires RCT or quasi-experimental design to support causal claim" (classification: direct-evidence)

### Gadget consulting for scoped credential discipline

Gadget is evaluating an MCP integration requiring Cloudflare token. Consults `HEPHAISTOS_OPERATIONS.md` § Secret Handling and `QUEEN-KEYPORT.md` § Refusal Conditions. Records both consults in `security_reference_log`. Gadget's `specialist_action`: "proceeded-with-scoped-Zone:Edit-token".

In both cases, HEPHAISTOS never commanded the specialist. Specialist consulted published doctrine, interpreted for current task, acted.

---

## What this schema does NOT allow

- No "binding instruction" field. HEPHAISTOS cannot issue direct commands.
- No "override" field. HEPHAISTOS cannot require post-hoc changes.
- No approval status. This schema does not gate specialist work.
- HEPHAISTOS influence on a specific specialist output routes via the Operator: Operator reads HEPHAISTOS's position, Operator decides, Operator routes to specialist.

---

## Status

**Active.** Created 2026-04-23; consolidates prior `hephaistos-to-henry-guideline-pull.md` and `hephaistos-to-gadget-guideline-pull.md` (closes F-024).

## Related

- [[hephaistos-to-queen-keyport]]
- [[HEPHAISTOS-STATUS]]
- [[hephaistos.agent]]
- [[Governance and PHAROS MOC]]
- [[CO-EQUAL-AUTHORITY-DECISION]]
