---
type: wiki
title: RAGE — Recursive Artifact Governance Engine Proposal (2026-05-11)
aliases:
- RAGE proposal
- Recursive Artifact Governance Engine
- artifact graph governance engine
- wiki/RAGE — Recursive Artifact Governance Engine Proposal (2026-05-11)
tags:
- governance
- architecture
- observability
- graph
- audit
- recursive-systems
- product-concept
- wiki
- rage-recursive-artifact-governance-engine-proposal-2026-05-11-md
- rage
- score
- proposal
- recursive
- color-purple
status: active
created: '2026-05-12'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/RAGE — Recursive Artifact Governance Engine Proposal (2026-05-11).md
backlink_count: 9
backlinks:
- '[[wiki/Control Protocols MOC]]'
- '[[wiki/Desktop and Downloads Scan — 2026-05-12]]'
- '[[wiki/EMERAULD Thematic Analysis — Claude-Codex Pass (2026-05-25)]]'
- '[[wiki/Governance Controls and Mechanisms]]'
- '[[wiki/Governance and PHAROS MOC]]'
- '[[wiki/Recursive Governance Theory]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[raw/Desktop-Downloads-scan-2026-05-12/downloads/RAGE-dep-report]]'
- '[[session-state]]'
source:
- raw/Desktop-Downloads-scan-2026-05-12/downloads/RAGE-dep-report.md
---

# RAGE — Recursive Artifact Governance Engine Proposal (2026-05-11)

## Summary

RAGE is framed as a graph-native governance observability layer for multi-step AI systems. The core proposition: store every transformation artifact (prompt, model output, critique, revision, decision) as a traceable graph, then score recursive-risk dynamics (drift, confidence inflation, provenance loss) across the chain rather than judging only final outputs.

Verification report: `raw/intake-report-desktop-downloads-scan-2026-05-12.json`.

## Core Model

- **Artifact graph ontology**: nodes for source/evidence/prompt/output/critique/decision, with explicit transformation edges.
- **Governance metrics**:
  - Semantic Drift Score (SDS)
  - Authority Amplification Index (AAI)
  - Provenance Integrity Ratio (PIR)
- **Composite risk signal**: Recursive Governance Risk Score (RGRS) used for threshold-based alerts.

## System Architecture (Proposed)

- Capture/ingestion hooks in agent pipelines.
- Property-graph storage (Neo4j/Neptune/TigerGraph/ArangoDB candidates discussed).
- Embedding and semantic-analysis layer.
- Scoring/alert engine with rule triggers.
- Audit dashboard with lineage drill-down.

## Why It Matters Here

The proposal is conceptually aligned with PHAROS/HELIX evidence discipline:
- It operationalizes "show the path, not just the answer."
- It converts recursive instability into measurable control signals.
- It is a potential productization bridge between protocol-level governance and enterprise monitoring budgets.

## Boundary

This is a proposal/spec artifact, not a deployed runtime in this vault pass. It should be treated as design intent and market positioning material until implementation evidence is attached.

## Related

- [[Control Protocols MOC]]
- [[Evidence Discipline and Epistemics]]
- [[Recursive Governance Theory]]
- [[Governance Controls and Mechanisms]]
- [[Provisional Arbitration Charter — Argus Layer 9.5]] — governance resolution route when evidence/authority conflicts remain unresolved
- [[Delta Closure Frame — Conditions, Actors, Constraints]] — closure discipline for converting a detected governance delta into named current/target states under constraints
- [[HELIX 3.0 Desktop Build Snapshot — Recursive Governor and Law 25 Control Surface (2026-05-11)]]
- [[Governance and PHAROS MOC]]
- [[RAGE-dep-report]]
