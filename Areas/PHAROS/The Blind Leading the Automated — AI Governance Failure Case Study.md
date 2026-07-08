---
type: wiki
title: The Blind Leading the Automated — AI Governance Failure Case Study
aliases:
- Blind Leading Automated
- ChatGPT Codex Governance Failure
- PHAROS SPA Case Study
tags:
- pharos
- governance-failure
- codex
- delegation
- ai-governance
- case-study
- autoethnography
- areas
- the-blind-leading-the-automated-ai-governance-failure-case-study-md
- accumulation
- unindexable
- lineage
- failure
- narrowed
- color-purple
status: active
created: '2026-04-16'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/The Blind Leading the Automated — AI Governance Failure Case Study.md
backlink_count: 8
backlinks:
- '[[wiki/AI Governance Failure Cases]]'
- '[[Areas/PHAROS/AI Paper Prompt — PHAROS Recursive Workflow Case Study]]'
- '[[Areas/Writing/AI Recruiting Has an Accessibility Problem — Lepage (2026)]]'
- '[[wiki/Care, Ethics, and Governance]]'
- '[[Resources/Evidence Discipline and Epistemics]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[maps/PHAROS Method Map]]'
- '[[projects/COMPASSai — Fisher King Project State]]'
---

# The Blind Leading the Automated — AI Governance Failure Case Study

## Summary

A first-person case study by Martin Lepage analyzing how using [[PHAROS Cross-AI Strategy Matrix|ChatGPT (Agatha)]] to generate [[HEPHAISTOS|Codex]] prompts — without feedback mechanisms between the layers — produced a cascade of governance failures: an 18.5% tool call failure rate, lineage confidence collapse, an unindexable SPA architecture, and six-repository sprawl. Published under PHAROS / pharos-ai.ca.

## Context

This is the applied case study that grounds the [[PHAROS AI Lineage — Source of Truth]] in concrete consequences. It serves as the primary governance stress test referenced in the [[AI Paper Prompt — PHAROS Recursive Workflow Case Study]] and maps directly onto the failure modes documented across the [[AI Society Manuscript — From AI Anxiety to Recursive Governance]]. The paper functions as the most expensive and convincing case study in Martin's practice — a governance consultant whose own system failed his own audit criteria.

## Details

**The setup:** Over 9 days and 132 Codex sessions, ChatGPT (Agatha persona) generated Codex prompts. Codex executed them. Martin supervised from two levels of abstraction above the actual code. Neither system had visibility into the other's environment.

**Sprint data:**
- 25,917 tool calls across 132 sessions
- 18.5% failure rate
- Failure pattern: cascading death spirals — missing dependency → retry loop → session timeout; no circuit breaker
- Lineage confidence below 0.7 in 61% of records (cannot trace which prompt produced which code)

**Three named failure modes:**

1. **SPA trap (architecture by accumulation):** No single decision produced an unindexable JavaScript SPA. Dozens of locally reasonable micro-decisions — each optimizing for the next prompt — converged on a structure that defeats the site's primary purpose: discoverability. pharos-ai.ca has zero search engine indexation.

2. **Six-repository sprawl (governance debt):** PHAROS code distributed across pharos-ai, govern-ai, Agency, AurorAI, CompassAI, Governess. Integration logic was generated across sessions that referenced components in other repos without verifying their current state. Routes may reference components that don't exist at expected paths. Traceability collapsed.

3. **Structurally broken feedback loop:** Three conditions for functioning governance were all absent simultaneously:
   - Instruction issuer (ChatGPT) had no visibility into execution environment
   - Executor (Codex) had no authority to refuse or escalate structurally unsound instructions
   - No independent monitoring layer existed

**Governance lesson (first principle for PHAROS engagements):** Delegation chains between AI systems require the same governance controls as delegation chains between humans and institutions — traceable authority flow, escalation mechanisms at the execution layer, and monitoring independent of both instruction and execution layers.

**Client-organization mapping:** The SPA accumulation failure maps directly onto how compliance controls drift through organizations: policy → narrowed checklist → further narrowed implementation → end-user artifact that may no longer reflect the original requirement.

**Resolution:** Migration to static rendering. Highest-priority technical fix for discoverability.

## Key Ideas

- Capability without governance architecture produces capability debt
- "Architecture by accumulation" is a failure mode governance frameworks rarely name explicitly
- The audit trail is the single most important artifact in a governance-sensitive system; when lineage collapses, the output is a liability with a login page
- Oversight at too great an altitude from the code is not oversight — it is the illusion of supervision

## Sources

- Raw: `raw sources/blind-leading-automated-2026-04-16.md`
- Origin: MASTER PACK — authored case study by Martin Lepage, PHAROS

## Related

- [[PHAROS AI Lineage — Source of Truth]]
- [[PHAROS Cross-AI Strategy Matrix]]
- [[AI Society Manuscript — From AI Anxiety to Recursive Governance]]
- [[HEPHAISTOS]]
- [[GSD — Get Shit Done Context Engineering System]]
- [[History]]
