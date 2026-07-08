---
type: governance-doc
title: Wave 2 Cleanup Tasks
aliases:
- Wave 2 Cleanup Tasks
tags:
- governance
- ai
- hephaistos
- governance-doc
- tier
- wave
- pairings
- equal
- scope
status: active
domain: governance
created: '2026-06-21'
updated: '2026-06-26'
vault_area: governance
canonical_path: governance/hephaistos/WAVE2-CLEANUP.md
backlink_count: 3
backlinks:
- '[[Areas/Writing/Research and Papers MOC]]'
- '[[wiki/Supersession Registry]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
---

> **HISTORICAL DOCUMENT — Pre-Wave-1 Architecture (superseded 2026-04-17)**
> Contains Tier 0/Tier 1/Tier 2 hierarchy language that does not reflect the current co-equal authority model.
> Binding authority: `CO-EQUAL-AUTHORITY-DECISION.md`, `AGENTS.md`, `HEPHAISTOS.md`, `QUEEN-KEYPORT.md`, `ORCHESTRATION.md`.
> Do not treat tier language in this document as current.

# Wave 2 Cleanup Tasks

Items deferred from Wave 1. Do not action until Wave 1 has been in use for at least two weeks on real work (per CO-EQUAL-AUTHORITY-DECISION.md).

---

## SKILL-MAP.md — Tier Reference Cleanup — COMPLETE (2026-04-18)

All 17 tier references resolved in two passes:

- 4 architectural contradictions (Tier 0/1/2 preambles, Overlap Summary table) — fixed first
- 7 section headers converted to scope labels
- 5 tracking labels converted to `scope: X` pattern
- 1 body cross-reference updated ("See Tier 1" → "See Governance skills")

---

## SKILL-MAP.md — Remaining Tier References — COMPLETE (2026-04-18, commit 74e65af)

4 label-only tier references resolved:

1. **Line 70** — `agent-development` pairings: `(Tier 3)` → `(scope: research)`
2. **Line 144** — `lead-research-assistant` pairings: `(Tier 3, method selection)` → `(scope: research, method selection)`
3. **Line 145** — `lead-research-assistant` pairings: `(Tier 3, background work)` → `(scope: research, background work)`
4. **Line 1386** — Skills Not In Corpus block: `registered as Tier 2 right-arm (co-equal with philosopher)` → `registered as right-arm to Queen Keyport (co-equal with philosopher)`

---

## SKILL-MAP.md — Body Placement Discrepancy — RESOLVED (2026-04-18, commit 74e65af)

`free-tool-strategy` body moved from `## Meta and Composition Skills` to `## Routing Connector Skills (scope: routing)`, inserted as first entry before `hermes-dependency-mapper`. Tracking label and body placement now consistent.

---

*Logged: Wave 1 Stage 6 close, 2026-04-18*
*Updated: Wave 3 close, 2026-04-18*

## Related

- [[Research and Papers MOC]]
- [[Supersession Registry]]
