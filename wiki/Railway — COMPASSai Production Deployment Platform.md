---
type: wiki
title: Railway — COMPASSai Production Deployment Platform
aliases:
- Railway deployment
- Railway PaaS
- COMPASSai Railway
- wiki/Railway — COMPASSai Production Deployment Platform
tags:
- pharos
- compassai
- deployment
- infrastructure
- railway
- wiki
- railway-compassai-production-deployment-platform-md
- classifier
- construction
- deployed
- color-orange
status: active
created: '2026-06-22'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Railway — COMPASSai Production Deployment Platform.md
backlink_count: 4
backlinks:
- '[[wiki/COMPASSai — Governance Engine]]'
- '[[wiki/Governance and PHAROS MOC]]'
- '[[wiki/Weekly Review — 2026-06-26]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
---

# Railway — COMPASSai Production Deployment Platform

> For future Claude: Railway (railway.app) is the PaaS platform where [[COMPASSai — Governance Engine]] is deployed to production as of 2026-06-22. Load this note when working on COMPASSai deployment, environment variables, or production infrastructure decisions.

## Summary

Railway is the production deployment platform for [[COMPASSai — Governance Engine]] as confirmed during the 2026-06-22 classifier delivery session. The EU AI Act classifier expansion, Quebec Construction Regulatory Classifier (`/api/v1/qc-construction/`), and regulatory corpus schema (`reg_ingest.py`) were all deployed to Railway production in that session. See [[COMPASSai — EU AI Act Classifier Expansion and Quebec Construction Module (2026-06-22)]] for the full delivery detail.

## Context

Railway replaced any local-stack or self-hosted deployment as the production environment for [[COMPASSai — Governance Engine]]. The move to Railway is consistent with the Web/SaaS architecture decision made on 2026-04-18 and recorded in `raw sources/2026-05-06_trismegiste-operator-state.md`. The deployment is on the current machine host (`/home/martin/`), not the legacy cerebrhoe machine paths that appear in earlier wiki notes.

**Security constraint (operator-confirmed 2026-06-22):** Never commit passwords or secrets to git-tracked files — not even in dev fixtures or README seed examples. Use environment variables (`$AURORAI_EMAIL`, `$AURORAI_PASSWORD`) for any credential references.

## Details

**Deployed services confirmed on Railway (as of 2026-06-22):**
- COMPASSai backend — `compassai/backend/server.py` (EU AI Act classifier: `classify_euai_act()` function)
- Quebec Construction Classifier — `compassai/backend/routers/qc_construction.py` (~500 lines)
- REST endpoints: `/api/v1/qc-construction/` (GET /domains, POST /assess, POST /use-cases/{id}/assess, POST /reg-docs, GET /reg-docs, GET /reg-docs/{id}, GET /regulators)
- Regulatory corpus schema — `compassai/backend/reg_ingest.py`

**Verification evidence:** 7/7 Quebec Construction smoke-test cases passed before Railway deploy; commit 9bb696b (insurance claims adjudication fix) deployed and confirmed on Railway.

**Gate model confirmed on Railway:** `intake_complete → risk_assessed → controls_satisfied → approved_for_deploy` — Risk tiers T0–T3.

## Non-Claims

- Do not assume [[AurorA — COMPASSai Input Module]] is also deployed to Railway; its deployment status has not been confirmed in vault evidence as of this note.
- Do not assume HELIX or other PHAROS-suite services share this Railway deployment without separate verification.
- Do not use legacy local-stack URLs (`http://127.0.0.1:9205/api/`) as production endpoints; those describe pre-Railway local-dev evidence.

## Related

- [[COMPASSai — Governance Engine]]
- [[COMPASSai — EU AI Act Classifier Expansion and Quebec Construction Module (2026-06-22)]]
- [[AurorA — COMPASSai Input Module]]
- [[PHAROS-AI Webservice — pharos-ai.ca]]
- [[Governance and PHAROS MOC]]
