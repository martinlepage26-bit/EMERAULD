---
type: governance-doc
title: STATUS — Self-Audit Against Co-Equal Authority Spec
aliases:
- STATUS — Self-Audit Against Co-Equal Authority Spec
tags:
- governance
- ai
- hephaistos
- governance-doc
- global
- equal
- keyport
- queen
- conflict
status: active
domain: governance
created: '2026-06-21'
updated: '2026-06-26'
vault_area: governance
canonical_path: governance/global/HEPHAISTOS-STATUS.md
backlink_count: 9
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[_vault/ARCHITECTURE-STATUS-MARKING-CHECKLIST]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
- '[[governance/hephaistos/HEPHAISTOS_OPERATIONS]]'
- '[[governance/hephaistos/STATUS]]'
- '[[governance/hephaistos/hephaistos-to-queen-keyport]]'
- '[[governance/hephaistos/hephaistos-to-specialist-guideline-pull]]'
- '[[hephaistos/agents/hephaistos]]'
- '[[memory/local-session/project_hephaistos]]'
---

# STATUS — Self-Audit Against Co-Equal Authority Spec

**Date:** 2026-04-18  
**Scope:** Live Claude and Codex entry surfaces that govern `hephaistos` work at the
global and repo-local levels.  
**Binding reference:** `CO-EQUAL-AUTHORITY-DECISION.md`

---

## Audit Question

Do the live Claude and Codex entry files instruct the agents in a way that matches
the binding co-equal authority model for Hephaistos and Queen Keyport?

This is a self-audit of the live entry surfaces:

- Claude (global): `~/.claude/CLAUDE.md`
- Claude (repo): `hephaistos/CLAUDE.md`
- Codex (global): `/home/cerebrhoe/AGENTS.md`
- Codex (repo): `hephaistos/AGENTS.md`

It is not a claim that every historical report or template in the repo is fully free of
older hierarchy language.

---

## Co-Equal Criteria

Derived from `CO-EQUAL-AUTHORITY-DECISION.md`:

1. Hephaistos and Queen Keyport are co-equal authorities; neither outranks the other.
2. Each authority operates within its own scope without requiring approval from the other.
3. If they conflict, neither proceeds; the conflict is surfaced and arbitrated.
4. Hermes is downstream of both and does not adjudicate unresolved conflict.
5. The entrypoint should not imply a "primary over" or "final decision authority" hierarchy.

---

## Claude Status — Global Surface

**File:** `~/.claude/CLAUDE.md`  
**Status:** PASS

**Evidence**

- It delegates to the root and repo-local control stack:
  - `/home/cerebrhoe/AGENTS.md`
  - `/home/cerebrhoe/hephaistos/AGENTS.md`
- The global invariant no longer implies a default governance winner.
- It preserves evidence and unresolved-conflict discipline:
  - "Direct evidence beats fluency."
  - "If a high-consequence conflict remains unresolved, degrade the boundary and stop promotion."

**Verdict**

The global Claude boot router is now compatible with the co-equal model. The earlier
"Governance constraints beat implementation preference" wording was repaired to avoid
implying a default hierarchy win.

---

## Claude Status — Repo Surface

**File:** `CLAUDE.md`  
**Status:** PASS

**Evidence**

- Scope separation is explicit:
  - `HEPHAISTOS` for scope, artifact type, architecture, build strategy, and skill composition.
  - `Queen Keyport` for governance, risk, evidence bars, controls, approvals, refusals, and consequence.
  - `Hermes` for routing, integration, monitoring, and escalation.
- Co-equal operation is explicit:
  - "both Hephaistos and Queen Keyport work their scope areas — in parallel or sequence as the task requires"
  - "Neither authority gates the other within its own scope."
- Hermes is correctly downstream:
  - "Hermes proceeds only after both have cleared, or after the operator has arbitrated a conflict between them."

**Verdict**

`hephaistos/CLAUDE.md` matches the binding co-equal model. No active hierarchy language
was found in the repo-local Claude entrypoint.

---

## Codex Status — Global Surface

**File:** `/home/cerebrhoe/AGENTS.md`  
**Status:** PASS

**Evidence**

- The root dispatcher states:
  - "`HEPHAISTOS` and `Queen Keyport` are co-equal authorities"
  - "full model at `CO-EQUAL-AUTHORITY-DECISION.md`"
- It does not assign final decision authority to Queen Keyport.
- It keeps canonical handoff packet authority below the co-equal model rather than
  above it.

**Verdict**

The global Codex surface is aligned with the co-equal model and does not reinstate the
older hierarchy.

---

## Codex Status — Repo Surface

**File:** `AGENTS.md`  
**Status:** PASS

**Evidence**

- Co-equal authority is explicit:
  - "Hephaistos and Queen Keyport are co-equal authorities."
  - "Neither outranks the other."
  - "Neither holds veto by default."
- Separate scope without mutual approval is explicit:
  - "Each operates within its own scope without requiring approval from the other."
- Conflict path is explicit:
  - "When their directions conflict on the same task, neither proceeds"
  - "the operator (Martin) arbitrates"
  - "The resolution is recorded before work resumes."
- Hermes is correctly downstream:
  - "Hermes receives work only after Hephaistos and Queen Keyport have both cleared"
  - "Hermes does not adjudicate Hephaistos/Queen Keyport conflicts"
  - "Hermes escalates them back to the co-equal pair."

**Verdict**

`hephaistos/AGENTS.md` matches the binding co-equal model and correctly frames Hermes
as downstream of unresolved Hephaistos/Queen Keyport conflict.

---

## Overall Status

**Claude (global):** PASS  
**Claude (repo):** PASS  
**Codex (global):** PASS  
**Codex (repo):** PASS

The active agent entry surfaces are aligned with the co-equal authority decision.

---

## Residual Risk

This self-audit does **not** mean the entire repo is clean of older hierarchy framing.
Historical reports and some older artifacts may still contain superseded Tier 0 / Tier 1
language. Those should be treated as non-binding when they conflict with:

- `CO-EQUAL-AUTHORITY-DECISION.md`
- `AGENTS.md`
- `CLAUDE.md`
- `HEPHAISTOS.md`
- `QUEEN-KEYPORT.md`
- `ORCHESTRATION.md`

## Wave 1 Completion Check

This status file originally flagged two remaining Wave 1 blockers under
`CO-EQUAL-AUTHORITY-DECISION.md`. They have now been closed in the active handoff
surface.

Completed follow-up:

1. The three handoff templates were amended to use scope/co-equal framing instead of
   Tier 0 / Tier 1 / Tier 2 authority labels:
   - `hephaistos-to-queen-keyport.md`
   - `queen-keyport-to-hermes.md`
   - `hermes-escalation-to-queen-keyport.md`
   - mirrored copies under `templates/`

2. The remaining unilateral override language in the long templates was tightened so
   unresolved vetoes route to scope redesign, co-equal conflict recording, or operator
   arbitration rather than a default HEPHAISTOS override.

3. The disagreement test case required by the spec now exists at
   `hq-disagreement-test-case.md` and confirms Hermes does not route unresolved
   Hephaistos/Queen Keyport conflict.

So the correct reading is:

- entry-surface co-equal audit: PASS
- active handoff-template co-equal audit: PASS
- disagreement test case: PASS

## Related

- [[project_hephaistos]]
- [[hephaistos-to-specialist-guideline-pull]]
- [[hephaistos-to-queen-keyport]]
- [[hephaistos.agent]]
- [[ARCHITECTURE-STATUS-MARKING-CHECKLIST]]
- [[hephaistos]]
- [[HEPHAISTOS_OPERATIONS]]
- [[Governance and PHAROS MOC]]
- [[STATUS]]
