---
type: wiki
aliases: [pharos-ai.ca, PHAROS webservice, PHAROS public site, "PHAROS-AI Webservice — Product Stack"]
tags: [pharos, webservice, deployment, cloudflare]
status: active
created: 2026-04-18
updated: 2026-04-28
---

# PHAROS-AI Webservice — pharos-ai.ca

## Summary

`pharos-ai.ca` is the canonical public-facing web service for [[PHAROS AI Ethics Submission — Springer Draft|PHAROS]], operated by [[Martin Lepage — Professional Profile|Martin Lepage]] through PHAROS Inc. (Québec). It is the production deployment surface for the [[PHAROS Method — Technical Reference|PHAROS governance method]] and its commercial products. All public PHAROS communications, documentation, and governance tool access route through this domain.

## Context

The site runs on the `pharos-suite` repository at `/home/cerebrhoe/PHAROS-SUITE/`. Deployment target: Cloudflare Pages (frontend) + Cloudflare Workers (API). Stack: React 18 + FastAPI + MongoDB.

`govern-ai.ca` is a legacy redirect only — `pharos-ai.ca` is the sole canonical domain. The `martin-lepage-site` repo and `martin.govern-ai.ca` are the Martin identity surface; do not cross-publish between surfaces.

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
- `govern-ai.ca` — legacy redirect only
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
