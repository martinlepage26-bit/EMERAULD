---
type: wiki
title: Right-Arm Extension Decision — Hephaistos and Hermes Advisory Consultation
  (2026-04-18)
aliases:
- Right-Arm Extension Decision
- Hephaistos right-arm consultation
- Hermes exception consultation
- wiki/Right-Arm Extension Decision — Hephaistos and Hermes Advisory Consultation
  (2026-04-18)
tags:
- governance
- hephaistos
- hermes
- queen-keyport
- right-arm
- binding-decision
- architecture
- wiki
- right-arm-extension-decision-hephaistos-and-hermes-advisory-consultation-2026-04-18-md
- arms
- consultation
- implications
- analyst
- color-purple
status: active
created: '2026-05-04'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Right-Arm Extension Decision — Hephaistos and Hermes Advisory
  Consultation (2026-04-18).md
backlink_count: 8
backlinks:
- '[[.github/agents/hephaistos.agent]]'
- '[[wiki/Governance and PHAROS MOC]]'
- '[[wiki/HEPHAISTOS Agent Architecture]]'
- '[[wiki/Vault Deep Linking Pass — 2026-05-06]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[_vault/VAULT-LINKING-AUDIT-2026-05-01]]'
- '[[governance/hephaistos/RIGHT-ARM-EXTENSION-DECISION]]'
- '[[raw/Clippings/Agent Architecture Patterns and Decision Framework]]'
---

# Right-Arm Extension Decision — Hephaistos and Hermes Advisory Consultation (2026-04-18)

## Summary

A binding governance decision (2026-04-18) extending the co-equal authority model to clarify when Hephaistos and Hermes may consult the right-arm specialists (Philosopher, Power-Analyst) beyond Queen Keyport's governance scope. Decision 1: Hephaistos may consult right-arms on a **case-triggered advisory basis** when forging tasks have normative or power implications. Decision 2: Hermes may consult right-arms as an **exception escalation path** when routing reveals new normative or power dimensions not present at governance decision time. Right-arms' binding veto authority remains scoped to Queen Keyport — unchanged. Source of truth: `/home/cerebrhoe/hephaistos/RIGHT-ARM-EXTENSION-DECISION.md`. Extends [[HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)]].

## Context

The co-equal authority model established Hephaistos and Queen Keyport as co-equal authorities in separate scopes. Right-arms (Philosopher, fully-rounded-power-analyst) were preserved as Queen Keyport's with binding veto over governance decisions. Two architectural questions were left open: (1) Does Hephaistos consult right-arms under the co-equal model? (2) Does Hermes consult right-arms during routing? Leaving these open produced drift risk — agents could self-author right-arm scope extensions without explicit authorization. This decision closes both questions.

See [[CO-EQUAL-AUTHORITY-DECISION.md]] (hephaistos) for the parent authority model.

## Details

### Decision 1 — Hephaistos: Case-Triggered Advisory Consultation

**Trigger conditions** (Hephaistos consults right-arms when the forging task has):
- **Normative implications** — the artifact defines how something *should* work, encodes values, or shapes evaluation of users or institutions → Philosopher
- **Power implications** — the artifact concentrates access, allocates resources, or organizes who benefits and pays costs → Power-Analyst
- **Both** — normative framing with structural-power consequences → both

**Non-trigger (routine):** Technical decisions with no values or power implications — artifact type selection, evidence requirements, skill composition mechanics, build strategy choices.

**Authority relationship:**
- Right-arms advise; they do not hold binding veto over forging decisions
- Hephaistos may accept, modify, or decline right-arm input
- Decline must be recorded with rationale when the task has clear normative/power implications

**Examples (triggers):**
- Designing an agent that evaluates job applications → Philosopher (what counts as "fit"?) + Power-Analyst (who benefits from this evaluation frame?)
- Building a tool that allocates research funding → Power-Analyst

**Examples (non-triggers):**
- Choosing between PostgreSQL and SQLite for an internal log store → technical decision
- Deciding whether a skill should be one file or two → composition mechanic

### Decision 2 — Hermes: Exception Consultation on New Information

**Trigger conditions** (Hermes escalates to right-arms when routing surfaces):
- **New normative dimension** — integration reveals conceptual implications Queen Keyport didn't see at decision time → Philosopher
- **New power dimension** — routing path or monitoring signal reveals structural-power implications not present in the governance packet → Power-Analyst
- **Material change in operational meaning** — what the decision means in practice diverges from what it meant on paper

**Non-trigger:** Routing decisions that execute the governance decision as specified. Routing is not re-review.

**Authority relationship:**
- Right-arm consultation is an escalation, not a routine step
- Output routes back to Queen Keyport (governance re-review) or Hephaistos (forging scope) — not resolved by Hermes unilaterally
- Hermes does not adjudicate; Hermes surfaces

**Examples (triggers):**
- QK approves routing user data to external analytics; routing reveals the service's parent company operates in a surveillance context → Power-Analyst escalation
- QK approves deployment of an educational tool; integration reveals the platform's pedagogy contradicts the tool's stated values → Philosopher escalation

### What This Does Not Change

- Right-arms' **binding veto authority remains scoped to Queen Keyport** — unchanged
- Philosopher and Power-Analyst remain co-equal with each other
- Queen Keyport still synthesizes right-arm input on governance decisions
- The operator still arbitrates Hephaistos/Queen Keyport conflicts
- Diamond-Eyes remains the shared validation gate across all authorities

### Declared Risks (L99)

- **Over-consultation drift** — Hephaistos may over-trigger on technical tasks to appear thorough. Mitigation: non-trigger examples establish the boundary.
- **Under-consultation drift** — Hephaistos may miss subtle normative/power implications. Mitigation: when in doubt, trigger. False positives are cheaper.
- **Hermes scope creep** — exception consultation could expand into routine review. Mitigation: must name the specific surfaced-information criterion; cannot invoke on general complexity.
- **Right-arm overload** — three authorities consulting instead of one. Mitigation: Hephaistos and Hermes consultations are lower-frequency by construction.

### Implementation Note

Implementation of updates to HEPHAISTOS.md, HERMES.md, ORCHESTRATION.md, SKILL-MAP.md was deferred to Wave 2 at decision time. The binding spec is `/home/cerebrhoe/hephaistos/RIGHT-ARM-EXTENSION-DECISION.md`.

## Related

- [[hephaistos.agent]]
- [[VAULT-LINKING-AUDIT-2026-05-01]]
- [[Agent Architecture Patterns and Decision Framework]]
- [[HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)]] — parent wave of governance work
- [[Governance and PHAROS MOC]] — primary governance index
- [[Architecture Translation Guide — Eight Operators to Three-Agent Stack]] — architecture reference
- [[HEPHAISTOS Agent Architecture]] — agent architecture cluster
- [[RIGHT-ARM-EXTENSION-DECISION]]
