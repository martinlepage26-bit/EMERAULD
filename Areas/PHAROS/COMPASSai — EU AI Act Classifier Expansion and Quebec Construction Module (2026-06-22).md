---
type: wiki
title: COMPASSai — EU AI Act Classifier Expansion and Quebec Construction Module (2026-06-22)
aliases:
- COMPASSai EU AI Act classifier
- Quebec Construction Classifier
- COMPASSai classifier 2026-06
tags:
- pharos
- compassai
- eu-ai-act
- law-25
- quebec
- construction
- governance-software
- classifier
- areas
- compassai-eu-ai-act-classifier-expansion-and-quebec-construction-module-2026-06-22-md
- gpai
- regulatory
- color-orange
status: active
created: '2026-06-22'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/COMPASSai — EU AI Act Classifier Expansion and Quebec Construction Module (2026-06-22).md
backlink_count: 7
backlinks:
- '[[Areas/PHAROS/COMPASSai — Governance Engine]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/Railway — COMPASSai Production Deployment Platform]]'
- '[[wiki/Weekly Review — 2026-06-26]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[memory/daily/2026-06-22]]'
- '[[session-state]]'
---

# COMPASSai — EU AI Act Classifier Expansion and Quebec Construction Module (2026-06-22)

> For future Claude: Major feature delivery session for [[COMPASSai — Governance Engine]] on 2026-06-22. Covers the full EU AI Act classifier gap-analysis and fix (all 9 Annex III groups, Art. 6(1), GPAI), a new Quebec Construction Regulatory Classifier module (12 domains, 10 regulators), and a regulatory document corpus schema with 19 priority stubs seeded to Railway production. Load this note when working on COMPASSai compliance modules or when resuming classifier development.

## Summary

This session delivered three major classifier enhancements to [[COMPASSai — Governance Engine]], all deployed to Railway production: (1) a comprehensive EU AI Act Annex III gap-analysis and fix covering all 9 groups including Art. 6(1) safety-component pathway and GPAI Title VIII detection; (2) a new Quebec Construction Regulatory Classifier module at `/api/v1/qc-construction/` covering 12 domains and 10 regulators; and (3) a regulatory document corpus schema (`reg_ingest.py`) with parsers for LégisQuébec XML and Justice Canada XML and 19 priority stubs seeded. Work was orchestrated via [[tmux AI Council]] with Codex (%1) and Grok (%0) running concurrently.

## Context

This work responds to two gaps identified during mock-dataset seeding: (a) Grok's 12 use cases revealed missing Annex III coverage for radiology AI, GPAI systems, and insurance claims adjudication; (b) no Quebec construction regulatory layer existed in COMPASSai despite the project's Quebec market focus. The [[Regulatory Arbitrage — EU AI Act + Law 25 + 93-Day Window (Synthesis)]] commercial argument depends on COMPASSai actually implementing these regimes.

**Claim boundary (verbatim, operator-confirmed):** These modules support compliance review; they do not certify legal compliance.

## Details

### EU AI Act Classifier — Gap Analysis and Fixes

**File:** `compassai/backend/server.py` — `classify_euai_act()` function

**Annex III groups expanded (was 8 → 9 groups, each with 8–15 new keywords):**

| Group | Domain | Key additions |
|-------|--------|---------------|
| 1 | Biometric systems | extended biometric surveillance terms |
| 2 | Critical infrastructure | extended infrastructure vulnerability terms |
| 3 | Education | extended automated marking, proctoring terms |
| 4 | Employment | extended hiring, scoring, firing terms |
| 5 | Essential services | **insurance claims adjudication added** (claim denial, claims adjudication, coverage decision, insurance claim, claims processing, fraud denial, fast track claim, reserve setting, bad faith, benefit denial, adverse action) |
| 6 | Law enforcement | extended predictive policing terms |
| 7 | Migration / asylum | extended border control terms |
| 8 | Justice / democracy | extended judicial AI terms |
| **9** | **Safety component of regulated product (Art. 6(1))** | **new group**: radiology, clinical decision support, medical imaging, patient triage, cancer detection, diagnostic AI, autonomous vehicle, functional safety, IEC 61508, ISO 26262 |

**GPAI detection added (`_GPAI_SIGNALS` list):**
- Keywords: foundation model, LLM, GPT, Gemini, Claude, Mistral, LLaMA, Falcon, multimodal model
- Triggers Title VIII obligations (Arts. 51–52, 53, systemic risk check)
- Returns `gpai_detected: true`, `gpai_obligations: [...]` in assess output

**Art. 5 prohibited practices expanded:**
- Added: dark patterns, addictive design, cognitive status targeting, mass biometric surveillance, emotion surveillance at work

**`informational` automation_level:** No longer triggers `limited_risk` (bug fix — informational tools were incorrectly classified as limited-risk)

**Art. 6(1) separation:** `annex_iii_canonical` (groups 1–8) is now separated from `art6_matches` (group 9) in the return dict. Group 9 triggers Module B (notified body) conformity note rather than Module A.

**Key commits:**
- Classifier gap analysis + 9-group expansion: committed ~2026-06-22
- Insurance claims adjudication fix: commit `9bb696b` (added to `5_essential_services`)

**Gap found during results review:** UC for insurance claims fraud was classified as `limited_risk` instead of `high_risk`. Root cause: `5_essential_services` lacked keywords for claims adjudication. Fixed in commit 9bb696b and deployed.

### Quebec Construction Regulatory Classifier

**File:** `compassai/backend/routers/qc_construction.py` (new, ~500 lines)

**12 Domains:**
1. Plumbing and drain work
2. French drain and exterior drainage
3. Excavation
4. Sewer backup emergency
5. Contaminated soil
6. Confined space
7. Road occupation
8. Weekend/emergency dispatch
9. Consumer quote/contract
10. Commercial quote/contract
11. Expert report drafting — **HALLUCINATION RISK flagged**: all regulatory citations generated by AI in expert reports must be marked `[SUGGESTION — VALIDER AVEC SOURCE OFFICIELLE]`
12. Google review and SMS consent

**10 Regulators mapped:**
- RBQ (Régie du bâtiment du Québec)
- CCQ (Commission de la construction du Québec)
- CNESST (Commission des normes, de l'équité, de la santé et de la sécurité du travail)
- CMMTQ (Corporation des maîtres mécaniciens en tuyauterie du Québec)
- Info-Excavation
- MELCCFP (Ministère de l'Environnement)
- OPC (Office de la protection du consommateur)
- CRTC (Communications)
- CNB-QC (Code national du bâtiment – Québec)
- MTQ (Ministère des Transports du Québec)

**Each domain includes:** article-level obligations, citation hints, key_obligations list

**REST endpoints:** `/api/v1/qc-construction/` — GET /domains, POST /assess, POST /use-cases/{id}/assess, POST /reg-docs, GET /reg-docs, GET /reg-docs/{id}, GET /regulators

**Smoke tested 7/7 cases passing before Railway deploy.**

### Regulatory Document Corpus Schema

**File:** `compassai/backend/reg_ingest.py` (new)

**Sources catalogued:**
- LégisQuébec: laws XML, regulations XML, title-code CSV maps
- Justice Canada: official website, Open Canada Bulk XML, GitHub mirror (laws-lois-xml), XML data dictionary
- Municipal: Montréal, Laval, Longueuil

**Metadata schema per document:** jurisdiction, language, document_id, title, chapter_code, regulation_number, version_date, effective_date, source_url, source_sha, content_sha, licence, official_status

**Priority stubs (19):** B-1.1 (RBQ), R-20 (CCQ), S-2.1 (CNESST), P-40.1 (OPC), Q-2 (MELCCFP), C-26 (RBQ), RSSST, Code de construction, Code de sécurité, RPRT, LPC regulation, Canada Labour Code, CASL, CEPA, NPC (and 4 more)

**CLI:** `python -m compassai.backend.reg_ingest seed`

### Mock Governance Dataset — Stress-Test UCs

Grok seeded 12 original use cases (UC-005–UC-012) as the primary mock governance dataset. Codex added 15 chaotic stress-test UCs (UC-005–UC-019) with intentionally noisy/contradictory inputs to test [[AurorA — COMPASSai Input Module]] normalization and COMPASSai uncertainty handling. Total: 23 use cases in production as of this session.

### HELIX Integration (Codex, Experimental)

Codex delivered `compassai/src/modules/helix-integration.ts` — HELIX probe results now affect `uncertainty_fields`, controls, and gating in the governance engine. Bounded as experimental draft (not production contract).

### Security Constraint (Operator-Confirmed)

**NEVER commit passwords to git-tracked files, even in dev fixtures.** Use env vars (`$AURORAI_EMAIL` / `$AURORAI_PASSWORD`) in README seed examples.

### Gate Model (Confirmed)

COMPASSai gate model: `intake_complete → risk_assessed → controls_satisfied → approved_for_deploy`
Risk tiers: T0–T3

## Open Items at Session End

- **Send results table to Grok** (interrupted by context compaction — 23-UC assessment table, insurance claims gap found/fixed, re-assess request)
- **Re-assess Insurance Claims UC** after 9bb696b deploy confirms `high_risk` + `5_essential_services`
- **Priority regulatory stubs** — seed_and_assess_qc.py background poll may or may not have completed
- **helix/ restructure** — large uncommitted changes remain (package.json, TSX migration, backend/, etc.)
- **Chaotic UCs full assessment** — all 23 UCs with updated classifier

## Related

- [[COMPASSai — Governance Engine]]
- [[AurorA — COMPASSai Input Module]]
- [[EU AI Act and Law 25 — Regulatory Pressure Window]]
- [[Regulatory Arbitrage — EU AI Act + Law 25 + 93-Day Window (Synthesis)]]
- [[HELIX 3.0 Desktop Build Snapshot — Recursive Governor and Law 25 Control Surface (2026-05-11)]]
- [[Governance and PHAROS MOC]]
