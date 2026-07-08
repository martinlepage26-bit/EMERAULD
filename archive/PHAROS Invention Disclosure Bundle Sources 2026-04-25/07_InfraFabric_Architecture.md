---
type: archive-record
title: InfraFabric Architecture
tags:
- archive
- pharos
- archive-record
- pharos-invention-disclosure-bundle-sources-2026-04-25
- canon
- explainer
- current
- infrafabric
- switchboard
status: archived
priority: low
created: '2026-04-25'
updated: '2026-06-26'
vault_area: archive
canonical_path: archive/PHAROS Invention Disclosure Bundle Sources 2026-04-25/07_InfraFabric_Architecture.md
backlink_count: 2
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Areas/PHAROS/InfraFabric Architecture]]'
---

# InfraFabric Architecture

See also [[Governance and PHAROS MOC]].
See also [[if.blackboard Full Explainer v1.3 (Multi-Audience, Split-Boundary Strict)]].
See also [[if.whitepapers.bible (v4.23)]].
See also [[InfraFabric Architecture]].
## Summary
InfraFabric is a modular AI governance and infrastructure platform. Its current product center is **if.switchboard**. The architecture claims are governed by an explicit canon hierarchy — not all documents carry equal authority. The CANON-INDEX defines what is current, what is historical, and what is narrative. Related to [[IF.EMOTION — Empathetic AI Architecture]] and [[Recursive Deterministic AI Governance — Method and Paper]].

## Context
InfraFabric's public surface: `infrafabric.io`. The canon bundle (as of 2026-03-11) contains product explainers, recursive process files, and companion narrative materials. They are not interchangeable. The recursive process layer stays in canon because InfraFabric makes claims not only about runtime behavior but about how runtime claims are challenged and kept bounded.

---

## Canon Hierarchy (from CANON-INDEX, 2026-03-11)

### Reading Rule
- **Current product canon** — present-tense source of truth for product posture, claim boundaries, and review language
- **Recursive process canon** — governs how claims are challenged, bounded, escalated, or promoted; part of canon because the operating method is part of the system
- **Companion narrative lane** — useful positioning/concept material, but not governing operational truth
- **Historical / compare-only** — keep for lineage or contrast; do not cite as current canonical statement

### Default Review Order
1. Public roadmap (v1.1, 2026-03-10)
2. if.switchboard full explainer (v1.6, 2026-03-09) — current product center
3. if.bus full explainer (v1.5, 2026-03-03)
4. if.blackboard full explainer (v1.3, 2026-03-06)
5. if.trace full explainer (v1.2, 2026-03-03)
6. if.context full explainer (v1.3, 2026-03-03)
7. if.knowledge full explainer (v1.1, 2026-03-03)
8. Whitepapers bible (v4.23, 2026-03-02)
9. Recursive process files — only as needed for challenge, escalation, or method review
10. Companion narrative lane — only after architectural and claim-boundary layer is clear

---

## Module Map

| Module | Role | Current Canon |
|---|---|---|
| **if.switchboard** | Product center; current governed interconnect/switchboard posture | Strongest current InfraFabric product explainer |
| **if.bus** | Transport/control boundary; runtime bus claims, fail-closed selectors, auth-path scope, source/deployed parity posture | Current standalone if.bus canon |
| **if.blackboard** | Coordination/evidence surface; public reviewability, task surfaces, boundary from SIP and routing claims | Current standalone if.blackboard canon |
| **if.trace** | Audit/provenance layer; receipts, replayability, artifact integrity, trace review posture | Use when reviewing evidence and verification chain |
| **if.context** | Context substrate; bounded current posture | Current, but internally composite; read with status discipline |
| **if.knowledge** | Knowledge/graph substrate; public-vs-internal knowledge graph posture and product projection logic | Current, but internally composite; use with same caution |
| **if.api** | Connector/API boundary; `if.api` scope and integration posture | Supporting current canon where connector scope matters |
| **if.gov** | Governance/council/triage method; shows how review and decision logic are structured rather than improvised | Recursive process canon |

---

## Recursive Process Canon Files

These stay in canon because InfraFabric makes claims about how runtime claims are challenged and kept bounded:

| File | Process role | Why it stays |
|---|---|---|
| Whitepapers bible (v4.23) | Documentation discipline | Defines claim-boundary, freshness, negative-test, and publication-boundary rules |
| if.gov explainer (v1.1) | Governance/council/triage method | Shows how review and decision logic are structured rather than improvised |
| Debate/red-team structure whitepaper (v1.2) | Red-team and debate method | Keeps adversarial review and structured dissent visible in the process |
| Implementation philosophy whitepaper (v1.0) | Implementation philosophy | Explains why parts of the control model are framed the way they are |
| Agent Rook explainer (v1.4) | Autonomous/air-gap control posture | Retains offline, air-gap, and sub-agent hardening as part of the review loop |

If a reviewer asks "how do you know when not to widen a claim?" or "where is the recursive challenge mechanism?", route them to these files.

---

## Companion Narrative Lane (Not Governing Canon)

- InfraFabric miniseries (v1.0) — story/positioning series; concept and narrative framing
- Story white paper (v1.0) — narrative product writing; positioning and communication experiments
- Story product explainer (v1.1) — module-specific narrative framing
- **IF.EMOTION combined whitepaper** — separate IF.EMOTION narrative bundle; parallel product/pitch lane, not governing InfraFabric architecture canon

**Rule**: companion files can enrich explanation, but they must not silently override `preview`, `bounded`, `Tier B`, `non-claim`, or roadmap gating language from the current product canon.

---

## Historical Files (Compare-Only)

- if.blackboard v1.2 — older revision
- if.switchboard v1.4 — superseded by v1.6
- if.switchboard + if.blackboard unified v1.2 — useful synthesis snapshot, not the current split canonical set

---

## Review Hygiene Rules

- If a file conflicts with the current product canon, prefer the current product canon
- If a narrative file sounds stronger than a bounded explainer, prefer the bounded explainer
- If a current claim depends on missing `tmp/*` or operator-local evidence, preserve the claim boundary and label the evidence class rather than silently broadening the claim
- If simplifying this pack later, do not remove the recursive process canon unless intentionally weakening claim auditability

---

## Canon Short Form (Honest One-Liner Answer to "What Is Current?")

- InfraFabric's current public-safe entrypoint is the roadmap
- if.switchboard is the current product center
- if.bus, if.blackboard, and if.trace are the main supporting module explainers
- if.context and if.knowledge are current substrate docs but need careful reading (contain stitched revision material)
- The recursive process layer stays in canon because the system's truth depends on bounded review, governance, and challenge loops
- IF.EMOTION combined whitepaper is a separate narrative lane, not the main architecture canon

---

## Insights

- InfraFabric treats the governance method itself as part of what it is selling — not a feature, but a structural claim. This is unusual and requires the recursive process layer to remain in canon
- The modular naming convention (`if.*`) creates a consistent namespace that signals scope separation — each module is bounded rather than bundled
- The Rook harness (`agent-rook`) is the autonomous/air-gap control model for sub-agents — the same governance logic applied to non-human actors in the system

## Open Questions

- What is the relationship between if.switchboard and if.bus? (interconnect vs. transport)
- How does if.gov relate to the PHAROS governance method? Are they the same logic at different scales?
- What does "internally composite" mean for if.context and if.knowledge? What was stitched, and from what?

## Sources
- `raw sources/000-CANON-INDEX.md`
- Related: [[IF.EMOTION — Empathetic AI Architecture]]
- Related: [[Recursive Deterministic AI Governance — Method and Paper]]
