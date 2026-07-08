---
type: governance-doc
title: Right-Arm Veto Authority
aliases:
- Right-Arm Veto Authority
- governance/hephaistos/right-arm-veto-authority
tags:
- governance
- ai
- hephaistos
- governance-doc
- veto
- keyport
- queen
- analyst
- breach
- color-purple
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: governance
canonical_path: governance/hephaistos/right-arm-veto-authority.md
backlink_count: 3
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
- '[[governance/hephaistos/CO-EQUAL-AUTHORITY-DECISION]]'
entity_type: Workflow
entity_id: right_arm_veto_procedure_workflow
entity_aliases: []
entity_confidence: high
---

# Right-Arm Veto Authority

## Purpose

This document defines the binding veto framework for Philosopher and Power-Analyst when they serve as right-arms to Queen Keyport. A veto blocks a governance decision from proceeding to Hermes until it is resolved.

---

## Authority Structure

Right-arm veto authority is **binding but not final**. It blocks routing. It does not override Queen Keyport's synthesis authority.

| Agent | Veto Type | Triggered When |
|---|---|---|
| Philosopher | Wisdom Breach | The scope or decision violates a core normative principle, creates irresolvable value contradiction, or fails the Diamond-Eyes test |
| Power-Analyst | Structural Integrity | The scope or decision is structurally impossible, creates hidden power asymmetries that cannot be mitigated, or harms populations it claims to serve |

Queen Keyport **synthesizes both inputs and decides**. A veto is an input signal requiring explicit resolution — not an autonomous block.

---

## Veto Procedure

### Step 1 — Trigger

A right-arm raises a veto by stating:
```
VETO TRIGGERED — [Philosopher | Power-Analyst]
Type: [Wisdom Breach | Structural Integrity]
Finding: <specific finding>
Required resolution: <what must change>
```

### Step 2 — Queen Keyport Receives

Queen Keyport receives the veto finding alongside the original scope and all other inputs. She does not suppress or ignore the veto signal.

### Step 3 — Queen Keyport Resolves

Queen Keyport must explicitly choose one of:

| Resolution | Meaning |
|---|---|
| `accept-veto-revise-scope` | Scope is returned to HEPHAISTOS for redesign |
| `accept-veto-modify-constraints` | Governance constraints are tightened to address the veto |
| `override-with-rationale` | Queen Keyport overrides the veto with explicit written rationale; override is logged and auditable |
| `escalate-to-hephaistos` | Scope conflict cannot be resolved at governance level; returned upstream |

### Step 4 — Logging

Every veto and its resolution is logged in the handoff packet (`veto_status` field in `queen-keyport-to-hermes.md`). No veto may be silently dropped.

---

## Veto Limits

- Right-arms cannot veto on grounds of preference, efficiency, or stylistic disagreement.
- Philosopher cannot veto on structural grounds (that is Power-Analyst's domain).
- Power-Analyst cannot veto on normative grounds alone without structural evidence.
- A veto requires a specific finding, not a general concern.

---

## Veto Resolution Authority

| Situation | Authority |
|---|---|
| Implementation-level gap | Queen Keyport resolves |
| Structural ethics violation | HEPHAISTOS must redesign scope |
| Irresolvable wisdom breach | Escalate; do not proceed |
| Queen Keyport overrides | Override is logged, not hidden |

---

## Status

**Active.** Created 2026-04-09 during Wave 3 governance architecture remediation.
Previously referenced in `INTEGRATION-PROGRESS.md` as complete but missing — now exists.

## Related

- [[Governance and PHAROS MOC]]
- [[CO-EQUAL-AUTHORITY-DECISION]]
