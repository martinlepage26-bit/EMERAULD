---
type: wiki
title: InfraFabric Architecture
aliases:
- InfraFabric Architecture
- wiki/InfraFabric Architecture
tags:
- wiki
- infrafabric-architecture-md
- canon
- explainer
- infrafabric
- switchboard
- blackboard
- color-orange
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/InfraFabric Architecture.md
backlink_count: 48
backlinks:
- '[[wiki/90-Day $1M Challenge — Status Report]]'
- '[[wiki/AI Infrastructure Stack]]'
- '[[wiki/Agent Session Phenomenology]]'
- '[[wiki/Architectural AI Governance — Willis and PBSAI]]'
- '[[wiki/CLI-Anything — Agent Harness for Tool Integration]]'
- '[[wiki/CODEX Writing Projects Manifest]]'
- '[[wiki/COMPASSai — Governance Engine]]'
- '[[wiki/Causal Mechanisms in the Social Sciences — Hedström & Ylikoski (Mechanistic
  Explanation)]]'
- '[[wiki/Claude Code Skill Corpus]]'
- '[[wiki/First Method Paper — Recursive AI Governance as Executable Method]]'
- '[[wiki/Founder Charter — Lepage and Stocker]]'
- '[[wiki/GSD — Get-Shit-Done Claude Code System]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Areas/PHAROS/HEPHAISTOS Agent Architecture]]'
- '[[wiki/Hermes Dashboard — Professional Governance Tool]]'
- '[[Areas/PHAROS/Historical Academic Portfolio — Pre-PHAROS Scholarly Work]]'
- '[[wiki/Home]]'
- '[[wiki/IF.EMOTION — Empathetic AI Architecture]]'
- '[[wiki/InfraFabric Codex Alignment — System-Shaper Frame]]'
- '[[wiki/InfraFabric MCP Stack — Remote Bundles]]'
- '[[wiki/InfraFabric R0.5 Rollout — Hosted API Migration (2026-06-29 to 2026-06-30)]]'
- '[[wiki/Kickstart App Prompt — Template and Synthesis Framework]]'
- '[[wiki/LOTUS Model — Agency and Social Positioning]]'
- '[[wiki/MCP and Runtime Integration MOC]]'
- '[[wiki/Martin Lepage Professional Identity]]'
- '[[Areas/PHAROS/Martin Lepage — Professional Profile]]'
- '[[Areas/PHAROS/PHAROS AI Ethics Submission — Springer Draft]]'
- '[[Areas/PHAROS/PHAROS Invention Disclosure]]'
- '[[wiki/PHAROS Licensing Prospectus]]'
- '[[Areas/PHAROS/PHAROS Method — Technical Reference]]'
- '[[wiki/Personal and Projects MOC]]'
- '[[wiki/ROOK — Session Boundary Model]]'
- '[[wiki/Reboot — Performance, Gender, and Computing of Identity]]'
- '[[wiki/Research and Papers MOC]]'
- '[[wiki/SYSTEM CHECK]]'
- '[[wiki/September 2024 Research Retrospective]]'
- '[[wiki/Stacklight-owner-explainer]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[_vault/VAULT-LINKING-AUDIT-2026-05-01]]'
- '[[archive/PHAROS Invention Disclosure Bundle Sources 2026-04-25/07_InfraFabric_Architecture]]'
- '[[wiki/claude-peers-mcp — Claude Peer Network]]'
- '[[wiki/if.blackboard — Coordination Evidence Spec Sheet (2026-06-27)]]'
- '[[wiki/if.switchboard — InfraFabric Product Center]]'
- '[[maps/PHAROS Method Map]]'
- '[[memory/daily/2026-06-27]]'
- '[[memory/daily/2026-06-30]]'
- '[[session-state]]'
- '[[wiki/skills/architecture]]'
---

# InfraFabric Architecture

## Summary
InfraFabric is a modular AI governance and infrastructure platform. Its current product center is **if.switchboard**. The architecture claims are governed by an explicit canon hierarchy — not all documents carry equal authority. The CANON-INDEX defines what is current, what is historical, and what is narrative. Related to [[IF.EMOTION — Empathetic AI Architecture]] and [[Recursive Deterministic AI Governance — Method and Paper]].

## Context
InfraFabric's public surface: `infrafabric.io`. The canon bundle (as of 2026-03-11) contains product explainers, recursive process files, and companion narrative materials. They are not interchangeable. The recursive process layer stays in canon because InfraFabric makes claims not only about runtime behavior but about how runtime claims are challenged and kept bounded — structurally, the same gate-and-judgment discipline operationalized in [[Mythocritique to PHAROS — The 2010 Master's Thesis as Methodological Keystone|the keystone substrate]] (Egyptian gate-formulas, Osirian recursive method, *if.gov* as the operationalization of the Council that judges Thomas's *procès*).

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
| **[[if.switchboard — InfraFabric Product Center\|if.switchboard]]** | Product center; current governed interconnect/switchboard posture | Strongest current InfraFabric product explainer |
| **if.bus** | Transport/control boundary; runtime bus claims, fail-closed selectors, auth-path scope, source/deployed parity posture | Current standalone if.bus canon |
| **if.blackboard** | Coordination/evidence surface; task/session/signal ledger, debt queues, and boundary from SIP/routing claims | Current standalone if.blackboard canon; see [[if.blackboard — Coordination Evidence Spec Sheet (2026-06-27)]] for the current liveness/auth caveat |
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

## Related

- [[Research and Papers MOC]]
- [[07_InfraFabric_Architecture]]
- [[Founder Charter — Lepage and Stocker]]
- [[90-Day $1M Challenge — Status Report]]
- [[InfraFabric Codex Alignment — System-Shaper Frame]] — operator-side adoption diagnostic: maps InfraFabric surfaces to actual Codex-on-machine behaviors (system-shaper frame vs “MCP operator” assumption)
- [[if.blackboard — Coordination Evidence Spec Sheet (2026-06-27)]] — current spec sheet and claim boundary for the blackboard coordination-evidence surface.
- [[InfraFabric Philosophy-As-Implementation Whitepaper (v1.0)]]
- [[Santé-France — Critical Full Explainer (v2.0, dependency-gated rebuild)]]
- [[if-radar_skydrone Full Explainer v1.1 (Data, Mechanics, Freshness, and Boundaries)]]
- [[if.api Full Explainer (Four-Audience, Claim-Boundary Strict)]]
- [[if.blackboard Full Explainer v1.3 (Multi-Audience, Split-Boundary Strict)]]
- [[if.bus Full Explainer v1.5 (Switchboard-Integrated, Claim-Boundary Strict)]]
- [[if.context Full Explainer v1.3 (Consolidated 1000+ Dense Lines)]]
- [[if.knowledge Full Explainer v1.1 (Consolidated 1000+ Dense Lines)]]
- [[if.switchboard + if.blackboard Unified Full Explainer v1.2 (Evidence-Dense)]]
- [[if.whitepapers.bible changelog pointer (v4.23)]]
