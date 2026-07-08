---
type: wiki
title: COMPASSai — Governance Engine
aliases:
- COMPASSai
- COMPASS AI
- governance engine
tags:
- pharos
- product
- governance-software
- compassai
- areas
- compassai-governance-engine-md
- classifier
- module
- aurora
- construction
- color-purple
status: active
created: '2026-04-18'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/COMPASSai — Governance Engine.md
backlink_count: 25
backlinks:
- '[[Areas/Writing/AI Society Manuscript — From AI Anxiety to Recursive Governance]]'
- '[[Areas/PHAROS/AurorA — COMPASSai Input Module]]'
- '[[Areas/PHAROS/COMPASSai — EU AI Act Classifier Expansion and Quebec Construction Module (2026-06-22)]]'
- '[[Areas/PHAROS/ComplyScan — Bilingual Law 25 - AI Act Compliance SaaS]]'
- '[[wiki/EMERAULD Graph Architecture — Link Density and Vector Layer (2026-05-25)]]'
- '[[Areas/PHAROS/Evidence-to-Publication Bridge — PHAROS Product-to-Manuscript Routing]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Areas/PHAROS/Hermes Dashboard — Professional Governance Tool]]'
- '[[archive/wiki-2026-07-08/L99 PHAROS Migration Artifacts 2026-04-19]]'
- '[[wiki/Master Project Tracker — 2026]]'
- '[[Areas/PHAROS/PHAROS]]'
- '[[Areas/PHAROS/PHAROS AI Ethics Submission — Springer Draft]]'
- '[[Areas/PHAROS/PHAROS Scholarly Publication Track]]'
- '[[Areas/PHAROS/PHAROS-AI Webservice — pharos-ai.ca]]'
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

# COMPASSai — Governance Engine

## Summary

COMPASSai is the governance engine software product within the [[PHAROS AI Ethics Submission — Springer Draft|PHAROS]] ecosystem — now recorded as a Web/SaaS application decision as of 2026-04-18 — that operationalizes the [[PHAROS Method — Technical Reference|PHAROS recursive governance method]] for client-facing use. It receives structured input through [[AurorA — COMPASSai Input Module]], its client-facing intake layer. COMPASSai is developed and operated by [[Martin Lepage — Professional Profile|Martin Lepage]] through PHAROS Inc.

## Context

COMPASSai is the product that converts the PHAROS governance pipeline into a deployable tool for organizations running AI inference workflows. It sits at the intersection of the [[PHAROS Runbook SOP|governance SOP]] and the [[InfraFabric Architecture]] module stack.

Earlier versions of this note described the architecture as TBD. Later operator-state evidence records the decision as Web/SaaS on 2026-04-18, aligned with the [[PHAROS-AI Webservice — pharos-ai.ca]] front door and direct client-facing assessment workflow. Treat the old desktop-vs-web language as superseded unless a newer architecture decision reverses it.

The [[Hermes Dashboard — Professional Governance Tool]] provides Martin's own activity-lane view of governance operations; COMPASSai is the client-facing counterpart.

## Details

**Role in the PHAROS stack:**
- Input layer: [[AurorA — COMPASSai Input Module]] (client-facing intake)
- Engine: COMPASSai (governance processing — this note)
- Operator view: [[Hermes Dashboard — Professional Governance Tool]]
- Public deployment: [[PHAROS-AI Webservice — pharos-ai.ca]]

**Current architecture decision:** Web/SaaS application available online for clients (decided 2026-04-18; recorded in `raw sources/2026-05-06_trismegiste-operator-state.md`).

**Current implementation evidence:** Local-stack runbook material describes a CompassAI backend at `http://127.0.0.1:9205/api/`, Mongo database `compassai`, JWT-protected routes, and an evidence-ingest route that can accept the internal service token used by AurorA/AurorA handoff. This is local operational evidence, not proof of public production readiness.

**Source-of-truth candidates:** Current evidence points to `/home/cerebrhoe/PHAROS-SUITE/repos/pharos-suite/compassai` and older/parallel traces at `/home/cerebrhoe/PHAROS-SUITE/repos/CompassAI`, `/home/cerebrhoe/repos/CompassAI`, and the Martin public project page source at `/home/cerebrhoe/martin-lepage-site/src/content/projects/compassai-governance-engine.md`. These paths require a live repo check before any public capability claim.

> [!warning] Contradiction detected
> Source-of-truth paths above reference `/home/cerebrhoe/...` — the old development machine. The vault was migrated from the cerebrhoe/softinfo host to the current host (`/home/martin/`) on 2026-06-21 (see CLAUDE.md Vault Status 2026-06-21). Today's session (2026-06-22) confirmed COMPASSai is deployed to [[Railway — COMPASSai Production Deployment Platform|Railway]] production, with active code at `compassai/backend/server.py` and `compassai/backend/routers/qc_construction.py` (relative paths on the current machine). The cerebrhoe paths are likely stale or inaccessible from the current host. Verify the active repo path on the current machine before using these paths for any source lookup.

**Governance alignment:** COMPASSai implements the 10-stage PHAROS pipeline (see [[PHAROS Invention Disclosure]]) and must enforce the consequence-binding map, admissibility rules, and promotion statuses described in the [[PHAROS Method — Technical Reference]].

**Gate model (confirmed 2026-06-22):** `intake_complete → risk_assessed → controls_satisfied → approved_for_deploy` — Risk tiers T0–T3.

**EU AI Act classifier (as of 2026-06-22):** Full 9-group Annex III coverage implemented; Art. 6(1) safety-component pathway (Group 9); GPAI detection (Title VIII Arts. 51–52); Art. 5 prohibited-practice expansion; insurance claims adjudication added to essential services (commit 9bb696b). Deployed to Railway. See [[COMPASSai — EU AI Act Classifier Expansion and Quebec Construction Module (2026-06-22)]] for full detail.

**Quebec Construction Regulatory Classifier (new, 2026-06-22):** `/api/v1/qc-construction/` — 12 domains, 10 regulators (RBQ, CCQ, CNESST, CMMTQ, Info-Excavation, MELCCFP, OPC, CRTC, CNB-QC, MTQ), article-level obligations, citation hints. Expert-report domain carries hallucination-risk flag: all AI-generated citations must be marked `[SUGGESTION — VALIDER AVEC SOURCE OFFICIELLE]`.

**Regulatory corpus schema (new, 2026-06-22):** `reg_ingest.py` — LégisQuébec XML + Justice Canada XML parsers; 19 priority regulatory stubs seeded to production.

**Claim boundary (operator-confirmed):** These modules support compliance review; they do not certify legal compliance.

## Key Ideas
- Governance engine that turns the PHAROS method into a product
- Client-facing intake through AurorA
- Web/SaaS deployed to Railway (production as of 2026-06-22)
- EU AI Act classifier now covers all 9 Annex III groups, GPAI, and Art. 5
- Quebec Construction module adds regulatory domain coverage for the Quebec market
- Capability claims must be bounded to verified routes, tests, and deployment evidence

## Open Questions
- Integration depth with InfraFabric modules
- Relationship to the Hermes Dashboard — separate interface or same product?
- Full chaotic UC (23 total) re-assessment after 9bb696b insurance fix deployment

## Non-Claims

- Do not present COMPASSai as publicly production-ready unless the live deployment, auth, database, and assessment routes have been verified.
- Do not claim the full PHAROS 10-stage pipeline is operational merely because route shells or tests exist.
- Do not conflate older `CompassAI` repo traces with the current `COMPASSai` product name without source reconciliation.

## Evidence-to-Publication Bridge

COMPASSai is implementation evidence for the [[PHAROS Scholarly Publication Track]], not a parallel scholarly cluster. Cite it only where named routes, gate transitions, classifier outputs, or deployment records support a manuscript claim — for example gate-model language in [[Recursive Deterministic AI Governance — Method and Paper]], consequence-binding framing in [[PHAROS AI Ethics Submission — Springer Draft]], or revisability under institutional constraint in [[AI Society Manuscript — From AI Anxiety to Recursive Governance]]. Pair with [[AurorA — COMPASSai Input Module]] for intake/admissibility evidence and [[HELIX Desktop Corpus — Protocol Evolution and Stress-Test Runs (2026-05-06)]] for adversarial stress-test evidence. Return context through [[PHAROS]] and [[Research Hub]].

## Related
- [[AurorA — COMPASSai Input Module]]
- [[RECURSO — Final Audit and Ethical Review]]
- [[COMPASSai — EU AI Act Classifier Expansion and Quebec Construction Module (2026-06-22)]]
- [[PHAROS Method — Technical Reference]]
- [[PHAROS Invention Disclosure]]
- [[EU AI Act and Law 25 — Regulatory Pressure Window]]
- [[Hermes Dashboard — Professional Governance Tool]]
- [[PHAROS-AI Webservice — pharos-ai.ca]]
- [[Governance and PHAROS MOC]]
- [[Recursive Deterministic AI Governance — Method and Paper]]
- [[First Method Paper — Recursive AI Governance as Executable Method]]
- [[AI Society Manuscript — From AI Anxiety to Recursive Governance]]
- [[PHAROS AI Ethics Submission — Springer Draft]]
- [[PHAROS]]
- [[PHAROS Scholarly Publication Track]]
- [[Research Hub]]
- [[HELIX Desktop Corpus — Protocol Evolution and Stress-Test Runs (2026-05-06)]]
