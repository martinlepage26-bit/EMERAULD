---
type: project
title: AurorA — Fisher King Project State
tags:
- project
- fisher-king
- aurora
- compassai
- pharos
- intake
- projects
- module
- deposit
- says
status: in-progress
priority: high
created: '2026-05-07'
updated: '2026-06-26'
vault_area: projects
canonical_path: projects/AurorA — Fisher King Project State.md
backlink_count: 6
backlinks:
- '[[wiki/Fisher King Hub — Project Recovery Map]]'
- '[[wiki/Healing the Fisher King Project Note Templates]]'
- '[[wiki/Master Project Tracker — 2026]]'
- '[[wiki/Projects Hub]]'
- '[[archive/session-state/session-state-003]]'
- '[[memory/daily/2026-06-22]]'
---

# AurorA — Fisher King Project State

## Status
active

## Core Question
How do I stabilize AurorA as the PHAROS intake and evidence-legibility layer without confusing the older AurorA standalone/repo history with the current COMPASSai file-deposit module?

## Why It Matters Now
AurorA is the first gate clients encounter before COMPASSai. If AurorA is unclear, the whole PHAROS product stack loses admissibility at intake: client documents, provenance, evidence manifests, and pre-screening all depend on this layer. The wound is naming and source-of-truth drift: AurorA appears in older repos/runbooks, while the vault standard says AurorA and later evidence says it is the file-deposit module inside COMPASSai.

## Current Direction
Heal. Treat AurorA as the active intake/evidence module, but reconcile spelling, legacy standalone traces, and actual module location before making public claims.

## Canonical State & Artifact
- Primary Canonical Artifact: [[AurorA — COMPASSai Input Module]]
- Downstream Engine: [[COMPASSai — Governance Engine]]
- Product Stack Artifact: [[PHAROS Product Stack]]
- Current Evidence Conflict: wiki says design phase/no deployment; raw operator-state says AurorA file-deposit module inside COMPASSai was decided 2026-04-18
- Artifact Status: active, intake-critical, source-reconciliation required
- Supersedes: legacy `AurorA` standalone framing, if Martin confirms
- Superseded by:
- Confidence: high for importance, medium for current implementation state
- Last reviewed: 2026-05-07
- Review Owner/Signatory: Martin

## Active Tensions
- The canonical app-name discipline says AurorA, but many code and raw-source traces still use AurorA.
- The wiki note describes no production deployment as of 2026-04-18; later state says the intake architecture was decided the same day.
- AurorA must be client-facing and bilingual, but also fail closed before evidence reaches COMPASSai.

## Contradictions To Preserve
- AurorA should lower the barrier for client intake.
- It must also reject, defer, or flag material that fails provenance/admissibility requirements.

## Relevant Materials
- [[AurorA — COMPASSai Input Module]]
- [[COMPASSai — Governance Engine]]
- [[PHAROS Product Stack]]
- [[PHAROS Runbook SOP]]
- [[PHAROS-AI Webservice — pharos-ai.ca]]
- [[L99 PHAROS Migration Artifacts 2026-04-19]]
- [[Portfolio Restructuring Review — March 2026]]
- `raw sources/2026-05-06_trismegiste-operator-state.md`
- `raw sources/# Govern Suite Operations Runbook.txt.md`
- `/home/cerebrhoe/PHAROS-SUITE/repos/pharos-suite/aurorai`
- `/home/cerebrhoe/PHAROS-SUITE/repos/AurorA`
- `/home/cerebrhoe/martin-lepage-site/src/content/projects/aurorai.md`

## Recent Moves
- AurorA note exists as the client-facing COMPASSai input module.
- Later operator-state evidence records AurorA as a file-deposit module inside COMPASSai.
- System checks identify a legacy AurorA standalone/ghost repo and absorbed module traces.
- **2026-06-22 — Chaotic stress-test UCs seeded:** 15 intentionally noisy/contradictory use cases (UC-005–UC-019) added by Codex to test AurorA normalization and COMPASSai uncertainty handling. IDP pipeline downstream from intake. 23 total UCs in production.

## Consequence Binding
- What changes if we execute the next move? -> AurorA becomes an intake gate with clear spelling, source path, and admissibility role.
- Real outcome / decision advanced: legacy AurorA traces are demoted or mapped, and current AurorA is positioned correctly.
- Review/sign-off needed: Martin confirms whether AurorA is fully superseded by AurorA.

## Blockers
- Legacy AurorA naming and repo traces.
- Need to verify current module location and route surface.
- Intake responsibilities are inferred but not fully specified as a client workflow.
- Deployment env vars and API-token boundaries remain operationally sensitive.

## Next Synthesis Move
Create a short AurorA source-of-truth section in [[AurorA — COMPASSai Input Module]]: exact spelling, legacy-name policy, active module path, accepted file/input types, pre-admissibility checks, handoff contract to COMPASSai, and current non-claims.

