---
type: project
title: COMPASSai — Fisher King Project State
tags:
- project
- fisher-king
- compassai
- pharos
- governance-engine
- projects
- engine
- module
- saas
- suite
status: in-progress
priority: high
created: '2026-05-07'
updated: '2026-06-26'
vault_area: projects
canonical_path: projects/COMPASSai — Fisher King Project State.md
backlink_count: 7
backlinks:
- '[[wiki/Fisher King Hub — Project Recovery Map]]'
- '[[wiki/Healing the Fisher King Project Note Templates]]'
- '[[wiki/Master Project Tracker — 2026]]'
- '[[wiki/Projects Hub]]'
- '[[archive/session-state/session-state-003]]'
- '[[memory/agents/Decisions]]'
- '[[memory/daily/2026-06-22]]'
---

# COMPASSai — Fisher King Project State

## Status
active

## Core Question
How do I stabilize COMPASSai as the PHAROS governance engine without letting stale architecture notes, repo sprawl, and narrative-reality gaps overstate what the engine currently does?

## Why It Matters Now
COMPASSai is the engine layer of the PHAROS product stack. It is not a side project: AurorA feeds it, Hermes observes the operator surface, PHAROS-AI is the public access point, and HELIX/PHAROS work depends on credible governance processing. The wound is truth alignment. The current wiki note says architecture is TBD, while later operator-state evidence says Web/SaaS was decided on 2026-04-18. Older tracker evidence also records a serious L99 narrative-reality gap where a hash-chained shell produced unconditional PROMOTE behavior before later fixes.

## Current Direction
Heal. Treat COMPASSai as active but not automatically production-credible. The recovery task is to reconcile product architecture, repo/module source of truth, and the real implemented capability surface.

## Canonical State & Artifact
- Primary Canonical Artifact: [[COMPASSai — Governance Engine]]
- Intake Partner: [[AurorA — COMPASSai Input Module]]
- Product Stack Artifact: [[PHAROS Product Stack]]
- Current Evidence Conflict: wiki says architecture TBD; raw operator-state says Web/SaaS decided 2026-04-18
- Artifact Status: active, load-bearing, truth-alignment required
- Supersedes:
- Superseded by:
- Confidence: high for importance, medium for current implementation state
- Last reviewed: 2026-06-22
- Review Owner/Signatory: Martin

## Active Tensions
- COMPASSai is named as the governance engine, but old notes still hedge architecture as web app vs desktop.
- Repo/module evidence is spread across PHAROS-SUITE, standalone CompassAI paths, historical raw sources, public project pages, and audit outputs.
- Prior work had a critical narrative-reality gap: governance pipeline claims outran actual deterministic behavior.

## Contradictions To Preserve
- COMPASSai is central to PHAROS productization.
- Central does not mean production-ready. Its authority depends on implemented gates, tests, and evidence landing from AurorA.

## Relevant Materials
- [[COMPASSai — Governance Engine]]
- [[AurorA — COMPASSai Input Module]]
- [[PHAROS Product Stack]]
- [[PHAROS-AI Webservice — pharos-ai.ca]]
- [[L99 PHAROS Migration Artifacts 2026-04-19]]
- [[Portfolio Restructuring Review — March 2026]]
- [[The Blind Leading the Automated — AI Governance Failure Case Study]]
- `raw sources/2026-05-06_trismegiste-operator-state.md`
- `raw sources/# Govern Suite Operations Runbook.txt.md`
- `/home/cerebrhoe/PHAROS-SUITE/repos/pharos-suite/compassai`
- `/home/cerebrhoe/PHAROS-SUITE/repos/CompassAI`
- `/home/cerebrhoe/martin-lepage-site/src/content/projects/compassai-governance-engine.md`

## Recent Moves
- COMPASSai naming normalized in the master tracker.
- Later operator-state evidence records Web/SaaS architecture as decided on 2026-04-18.
- L99 migration artifacts preserved a test-contract and deployment-hardening boundary after earlier narrative-reality gaps.
- **2026-06-22 — Major classifier delivery (Railway production):**
  - EU AI Act classifier expanded: 9 Annex III groups (added Art. 6(1) safety-component group for radiology/medical AI/autonomous vehicles); GPAI detection (Title VIII Arts. 51–52); Art. 5 prohibited-practice expansion; insurance claims adjudication added to essential services (commit 9bb696b — gap found during results review where UC was misclassified as limited_risk)
  - Quebec Construction Regulatory Classifier built: 12 domains, 10 regulators, article-level obligations, `/api/v1/qc-construction/` endpoints; expert-report domain carries AI citation hallucination-risk flag
  - Regulatory corpus schema (`reg_ingest.py`) with LégisQuébec XML + Justice Canada XML parsers; 19 priority stubs seeded
  - 23 use cases total in production (12 original + 11 chaotic from Grok mock dataset)
  - HELIX integration module added by Codex (experimental; affects uncertainty_fields, controls, gating)
  - Claim boundary confirmed: these modules support compliance review; they do not certify legal compliance
  - Security constraint confirmed: never commit passwords to git-tracked files; use env vars

## Consequence Binding
- What changes if we execute the next move? -> COMPASSai becomes a governed engine surface with a clear source of truth and claim boundary.
- Real outcome / decision advanced: stale TBD wording removed or explicitly superseded; implementation truth becomes inspectable.
- Review/sign-off needed: Martin confirms the authoritative repo/module and whether Web/SaaS is binding.

## Blockers
- Stale architecture status in [[COMPASSai — Governance Engine]].
- Multiple repo/module locations and historical references.
- Need to distinguish fixed test-pass evidence from production readiness.
- Relationship to HELIX and PHAROS commercial launch must be bounded, not assumed.

## Next Synthesis Move
Open the current COMPASSai module, verify implemented routes/tests against the runbook, then update [[COMPASSai — Governance Engine]] with a short "Current Architecture Decision" section: Web/SaaS, source-of-truth path, implemented capabilities, non-claims, and remaining deployment blockers.

