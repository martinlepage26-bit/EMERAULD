---
type: wiki
title: PHAROS-AI Webservice — pharos-ai.ca
aliases:
- pharos-ai.ca
- PHAROS webservice
- PHAROS public site
- PHAROS-AI Webservice — Product Stack
tags:
- pharos
- webservice
- deployment
- cloudflare
- areas
- pages
- public
- govern
- wiki
status: active
domain: pharos
created: '2026-04-18'
updated: '2026-08-05'
vault_area: Areas
canonical_path: Areas/PHAROS/PHAROS-AI Webservice — pharos-ai.ca.md
backlink_count: 27
backlinks:
- '[[Areas/PHAROS/AI Governance Public Statement and Market Impact Pack]]'
- '[[Areas/PHAROS/AurorA — COMPASSai Input Module]]'
- '[[Areas/PHAROS/COMPASSai — Governance Engine]]'
- '[[Areas/PHAROS/Cloudflare Pages-to-Worker Migration — Build and Asset Behavior]]'
- '[[Areas/PHAROS/ComplyScan — Bilingual Law 25 - AI Act Compliance SaaS]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Areas/PHAROS/Hermes Dashboard — Professional Governance Tool]]'
- '[[Areas/PHAROS/PHAROS AI Commercial Launch — 8-Stream Deploy (2026-05-01)]]'
- '[[Areas/PHAROS/PHAROS External Proof Packet — Procurement-Unblock 2026-04-28]]'
- '[[Areas/PHAROS/Railway — COMPASSai Production Deployment Platform]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[archive/session-state/session-state-001]]'
- '[[archive/wiki-2026-07-08/Codex Handoff — PHAROS AI Design Review (2026-05-01)]]'
- '[[archive/wiki-2026-07-08/DG Website Logo Rebrand & Governance Audit — 2026-05-01]]'
- '[[archive/wiki-2026-07-08/Documents Root Intake — Hermes Action Map 2026-04-28]]'
- '[[archive/wiki-2026-07-08/HELIX Production Shipping Runbook — Web, iOS, Android (2026-04-19)]]'
- '[[archive/wiki-2026-07-08/L99 PHAROS Migration Artifacts 2026-04-19]]'
- '[[archive/wiki-2026-07-08/PHAROS LinkedIn April 2026 Publishing Routine]]'
- '[[archive/wiki-2026-07-08/PHAROS Migration Runbook — PR4 Deploy and Cloudflare Migration (2026-04-19)]]'
- '[[artifacts/2026-04-19-pharos-migration-pr4/_manifest/MANIFEST]]'
- '[[artifacts/stale-projects-2026-07-04]]'
- '[[artifacts/stale-projects-2026-07-05]]'
- '[[artifacts/stale-projects-2026-07-06]]'
- '[[artifacts/stale-projects-2026-07-07]]'
- '[[memory/daily/2026-05-01]]'
- '[[projects/AurorA — Fisher King Project State]]'
- '[[projects/COMPASSai — Fisher King Project State]]'
---

# PHAROS-AI Webservice — pharos-ai.ca

## Summary

`pharos-ai.ca` is the canonical public-facing web service for [[PHAROS AI Ethics Submission — Springer Draft|PHAROS]], operated by [[Martin Lepage — Professional Profile|Martin Lepage]] through PHAROS Inc. (Québec). It is the production deployment surface for the [[PHAROS Method — Technical Reference|PHAROS governance method]] and its commercial products. All public PHAROS communications, documentation, and governance tool access route through this domain.

## Context

The site runs on the `pharos-suite` repository at `/home/cerebrhoe/PHAROS-SUITE/`. Deployment target: Cloudflare Pages (frontend) + Cloudflare Workers (API). Stack: React 18 + FastAPI + MongoDB.

`govern-ai.ca` (bare/apex) is a legacy redirect only from the pre-rebrand "Govern AI" era — `pharos-ai.ca` is the sole canonical PHAROS domain. `martin.govern-ai.ca` (a subdomain on that same zone) is the live Martin identity surface. Corrected 2026-08-05 (joint Hephaistos/Argus/Hermes audit, see [[CLAUDE]]): it is not hosted via a separate `martin-lepage-site` repo — `martin-lepage-site` is the Cloudflare Pages *project name*, sourced from the git repo `martinlepage26-bit.github.io` (GitHub Pages itself unused, 404s), and the same deploy also answers at `martin-lepage-phd.pharos-ai.ca`. Do not cross-publish between the PHAROS and Martin surfaces regardless. Caution: the `govern-ai.ca` zone also hosts unrelated products (patent-workbench, clearday, axis, fantasycast subdomains) — don't assume the whole zone belongs to either surface.

The webservice is the primary access point for [[COMPASSai — Governance Engine]] once that product is live. Related governance tools include the [[Hermes Dashboard — Professional Governance Tool]] which provides activity lanes for the operator.

## Details

**Stack:**
- Frontend: React 18, React Router 6, Tailwind CSS, Shadcn UI, craco
- Backend: FastAPI, MongoDB (Motor), Pydantic v2
- Deploy: Cloudflare Pages (frontend), Cloudflare Workers (API)
- Design system: Swiss Scholar — Newsreader (headings), Public Sans (body), JetBrains Mono (code)
- Bilingual: EN + FR required on every UI string — no exceptions

**Domain rules:**
- `pharos-ai.ca` — canonical production
- `govern-ai.ca` (bare/apex) — legacy redirect only; the `martin.govern-ai.ca` subdomain on the same zone is Martin's live personal site, not covered by this redirect rule (see Context above)
- `pharos-suite-review.pages.dev` — deleted preview surface, not current authority

**Governance note:** The webservice is the public artifact of [[PHAROS Company Registration and Security Incidents|PHAROS Inc.]]. Its deployment is tracked in `PHAROS-SUITE/memory/cloudflare-readiness-2026-03-06.md`.

**Public-surface content note:** [[PHAROS LinkedIn April 2026 Publishing Routine]] and [[AI Governance Public Statement and Market Impact Pack]] are now the strongest root Documents captures for how the canonical `pharos-ai.ca` surface should be narrated externally after the Govern AI → PHAROS transition.

## Key Ideas
- Canonical surface for PHAROS governance services
- Bilingual EN/FR is non-negotiable at the UI layer
- Cloudflare Pages + Workers is the deployment architecture

## Related
- [[PHAROS Method — Technical Reference]]
- [[PHAROS Company Registration and Security Incidents]]
- [[COMPASSai — Governance Engine]]
- [[Cloudflare Pages-to-Worker Migration — Build and Asset Behavior]]
- [[Hermes Dashboard — Professional Governance Tool]]
- [[Governance and PHAROS MOC]]
- [[PHAROS LinkedIn April 2026 Publishing Routine]]
- [[AI Governance Public Statement and Market Impact Pack]]
- [[PHAROS Migration Runbook — PR4 Deploy and Cloudflare Migration (2026-04-19)]] — Operator action list from the 2026-04-19 session documenting the govern-ai → pharos-ai namespace migration, PR #4 push, and Cloudflare Pages/D1/R2 renames that established the current deployment state
