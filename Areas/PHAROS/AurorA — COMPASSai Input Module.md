---
type: wiki
title: AurorA — COMPASSai Input Module
aliases:
- AurorA
- Aurora input module
tags:
- pharos
- product
- compassai
- client-facing
- aurora
- areas
- aurora-compassai-input-module-md
- aurorai
- engine
- spelling
- color-purple
status: active
created: '2026-04-18'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/AurorA — COMPASSai Input Module.md
backlink_count: 22
backlinks:
- '[[Areas/Writing/AI Society Manuscript — From AI Anxiety to Recursive Governance]]'
- '[[Areas/PHAROS/COMPASSai — EU AI Act Classifier Expansion and Quebec Construction Module (2026-06-22)]]'
- '[[Areas/PHAROS/COMPASSai — Governance Engine]]'
- '[[wiki/EMERAULD Graph Architecture — Link Density and Vector Layer (2026-05-25)]]'
- '[[Areas/PHAROS/Evidence-to-Publication Bridge — PHAROS Product-to-Manuscript Routing]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Areas/PHAROS/Hermes Dashboard — Professional Governance Tool]]'
- '[[archive/wiki-2026-07-08/L99 PHAROS Migration Artifacts 2026-04-19]]'
- '[[Areas/PHAROS/PHAROS]]'
- '[[Areas/PHAROS/PHAROS AI Ethics Submission — Springer Draft]]'
- '[[Areas/PHAROS/PHAROS Scholarly Publication Track]]'
- '[[wiki/RDAIG Method Editorial Consolidation — 2026]]'
- '[[wiki/Railway — COMPASSai Production Deployment Platform]]'
- '[[wiki/Research Hub]]'
- '[[Areas/Writing/Research and Papers MOC]]'
- '[[wiki/Weekly Review — 2026-06-26]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[memory/agents/Vibe]]'
- '[[memory/daily/2026-06-22]]'
- '[[projects/AurorA — Fisher King Project State]]'
- '[[projects/COMPASSai — Fisher King Project State]]'
- '[[session-state]]'
---

# AurorA — COMPASSai Input Module

## Summary

AurorA is the client-facing input and evidence-legibility module for [[COMPASSai — Governance Engine]], the PHAROS governance engine. Later operator-state evidence records AurorA as the file-deposit module inside COMPASSai as of 2026-04-18: clients upload files to AurorA, then governed evidence is handed off to COMPASSai. Developed by [[Martin Lepage — Professional Profile|Martin Lepage]] through PHAROS Inc.

## Context

AurorA sits at the intake boundary of the [[PHAROS Method — Technical Reference|PHAROS 10-stage pipeline]]. It is the first gate clients encounter — the interface through which material enters the governance process before reaching [[COMPASSai — Governance Engine]] for deterministic processing.

Because AurorA is client-facing, it must operate bilingually (EN/FR) and meet the admissibility standards defined in the PHAROS runbook (see [[PHAROS Runbook SOP]]). Material accepted by AurorA is governed; material rejected or flagged at intake never reaches the engine.

Access for clients routes conceptually through [[PHAROS-AI Webservice — pharos-ai.ca]] once deployed. Current local-stack evidence still uses older `AurorAI` service naming in runbooks and paths, so public claims should use the canonical product spelling **AurorA** while treating `AurorAI` as legacy implementation/repo spelling until reconciled.

## Details

**Position in the PHAROS product stack:**
- AurorA: client-facing intake (this note)
- [[COMPASSai — Governance Engine]]: processing engine
- [[Hermes Dashboard — Professional Governance Tool]]: operator activity view
- [[PHAROS-AI Webservice — pharos-ai.ca]]: public deployment surface

**Intake responsibilities:**
- Structured case submission from client organizations
- Document and artifact upload for governance evaluation
- Provenance capture and intake manifest generation
- Pre-admissibility screening before engine handoff

**Current architecture decision:** AurorA is the file-deposit module inside COMPASSai (decided 2026-04-18; recorded in `raw sources/2026-05-06_trismegiste-operator-state.md`).

**Current implementation evidence:** Local-stack runbook material describes an `AurorAI` backend at `http://127.0.0.1:9206/api/`, Mongo database `aurorai`, bearer-token protection, and a handoff path that posts generated evidence packages to CompassAI `/api/v1/evidence`. The same runbook records accepted current limits: PDF and TXT are supported, DOC/DOCX are not, and heuristic extraction may be used if the LLM path is not configured. This evidence is local-stack evidence, not proof of public production readiness.

**Source-of-truth candidates:** Current evidence points to `/home/cerebrhoe/PHAROS-SUITE/repos/pharos-suite/aurorai` and older/parallel traces at `/home/cerebrhoe/PHAROS-SUITE/repos/AurorAI`, `/home/cerebrhoe/repos/AurorAI`, and the Martin public project page source at `/home/cerebrhoe/martin-lepage-site/src/content/projects/aurorai.md`. These paths require a live repo check before any public capability claim.

## Key Ideas
- First client touchpoint in the PHAROS governance pipeline
- Intake gate that shapes what reaches the governance engine
- Bilingual, client-facing by design
- Canonical product spelling is AurorA; `AurorAI` remains legacy implementation/repo spelling until fully reconciled

## Open Questions
- Integration with InfraFabric intake modules?
- Which current path is authoritative for the active module?
- What is the exact accepted-input contract beyond PDF/TXT in the current local stack?
- Which pre-admissibility checks are implemented versus planned?

## Non-Claims

- Do not present AurorA as a mature public upload portal unless live deployment, auth, storage, and handoff have been verified.
- Do not claim DOC/DOCX support from old aspiration notes; local-stack evidence says PDF/TXT only.
- Do not erase legacy `AurorAI` traces without mapping them to the current AurorA naming policy.

## Evidence-to-Publication Bridge

AurorA supports publication claims about bounded corpus formation, intake admissibility, and evidence legibility at the pre-engine boundary. Use it in the [[PHAROS Scholarly Publication Track]] only where intake manifests, rejection rules, or handoff evidence are named — for example admissibility and provenance language in [[Recursive Deterministic AI Governance — Method and Paper]] or pre-deployment gating in [[PHAROS AI Ethics Submission — Springer Draft]]. Downstream processing evidence lives in [[COMPASSai — Governance Engine]]; adversarial continuity evidence lives in [[HELIX Desktop Corpus — Protocol Evolution and Stress-Test Runs (2026-05-06)]]. Route through [[PHAROS]] and [[Research Hub]] rather than treating intake as a standalone scholarly node.

## Related

- [[COMPASSai — Governance Engine]]
- [[RECURSO — Final Audit and Ethical Review]]
- [[PHAROS Method — Technical Reference]]
- [[PHAROS Runbook SOP]]
- [[PHAROS-AI Webservice — pharos-ai.ca]]
- [[Governance and PHAROS MOC]]
- [[Free-First Architecture]]
- [[Govern Suite Cheat Sheet]]
- [[Govern Suite Operations Runbook]]
- [[Recursive Deterministic AI Governance — Method and Paper]]
- [[AI Society Manuscript — From AI Anxiety to Recursive Governance]]
- [[PHAROS AI Ethics Submission — Springer Draft]]
- [[PHAROS]]
- [[PHAROS Scholarly Publication Track]]
- [[Research Hub]]
- [[HELIX Desktop Corpus — Protocol Evolution and Stress-Test Runs (2026-05-06)]]
