---
type: wiki
title: HELIX Production Shipping Runbook — Web, iOS, Android (2026-04-19)
aliases:
- HELIX shipping instructions
- HELIX deployment runbook
- HELIX v0.1.0 release
tags:
- workflow
- deliverable
- deployment
- helix
- cloudflare-pages
- eas
- runbook
- pharos-suite
- mobile
- web
- archive
- helix-production-shipping-runbook-web-ios-android-2026-04-19-md
- android
- shipping
- color-teal
status: active
created: '2026-04-30'
updated: '2026-06-26'
vault_area: archive
canonical_path: archive/wiki-2026-07-08/HELIX Production Shipping Runbook — Web, iOS, Android (2026-04-19).md
backlink_count: 6
backlinks:
- '[[wiki/Custom GPT Products — PHAROS AI GPT Roster]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Areas/PHAROS/HELIX — Value Proposition and Buyer Profile]]'
- '[[wiki/Inderscience IJAIGHR Submission Pipeline — Self-Polygraph Manuscript]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[projects/HELIX — Fisher King Project State]]'
---

# HELIX Production Shipping Runbook — Web, iOS, Android (2026-04-19)

## Summary
The shipping playbook for HELIX v0.1.0 across three surfaces — Cloudflare Pages (web), iOS App Store (EAS), Google Play (EAS) — plus the three companion governance documents that constitute the deliverable. The runbook is dated 2026-04-19 and lives at `/home/cerebrhoe/SHIPPING-INSTRUCTIONS.md`. This wiki note captures the workflow, verification gates, and the gates the runbook itself does not name (DNS, secrets rotation, bilingual EN/FR audit). Connected to [[AI Infrastructure Stack]], [[Cloudflare Pages-to-Worker Migration — Build and Asset Behavior]], and [[PHAROS Runbook SOP]]. Raw capture: `raw sources/2026-04-30_helix-shipping-instructions-runbook.md`.

## Context
HELIX is a [[Governance Stress-Test Protocols — Index|governance stress-test platform]] that runs the four-phase Pharos sequence (MÖBIUS, TRANSIT, PHAROS, TRAP) across multi-provider LLM endpoints (Anthropic, OpenAI, Google). The shipping runbook treats the platform as three coordinated artifacts (web app, mobile apps, governance docs) and assumes the [[PHAROS-AI Webservice — pharos-ai.ca|PHAROS-AI surface]] is the canonical narrative home. This note captures how that ship moves end-to-end and where it intersects existing PHAROS deployment doctrine.

## Details

### What ships

- **Web platform** — React + Vite at `/home/cerebrhoe/helix-app/`; target Cloudflare Pages; auto-deploy on push to `main`.
- **Mobile apps** — React Native + Expo at `/home/cerebrhoe/helix-mobile/`; built and submitted via EAS to iOS App Store and Google Play.
- **Governance documentation** — three narrative files at `/home/cerebrhoe/`: `HELIX-GOVERNANCE-POSITIONING.md` (technical foundation), `HELIX-EXECUTIVE-SUMMARY.md` (leadership brief), `HELIX-GOVERNANCE-IMPLEMENTATION.md` (4-phase implementation playbook).

### Web deployment sequence

1. `git remote add origin … && git push -u origin main`.
2. Cloudflare dashboard → Pages → Connect to Git → select repository.
3. Build settings: Framework `None`, Build command `npm run build`, Output directory `dist`.
4. Deploy → auto-deploy on every push to `main` to `helix.pages.dev`.
5. Optional custom domain (e.g., `helix.pharos-ai.ca`).

The build/output topology matches what was already documented in [[Cloudflare Pages-to-Worker Migration — Build and Asset Behavior]]; if HELIX is later migrated from Pages to a Worker-served surface, that note is the reference.

### Mobile deployment sequence

1. `npm install -g eas-cli && eas login`.
2. iOS: `npm run build-ios` → `eas submit --platform ios`. Apple review window 24–48 hr.
3. Android: `npm run build-android` → `eas submit --platform android`. Google review window 2–4 hr.

### Stated timeline (per the runbook)

| Stage | Duration |
|---|---|
| Web → Cloudflare | 15 min |
| iOS build | 15 min |
| iOS App Store review | 24–48 hr |
| Android build | 15 min |
| Android Play review | 2–4 hr |
| **Total to live** | **2–3 days** |

### Post-launch checklist

- **Day 1** — web URL accessible; mobile builds clean; dev/staging/prod working.
- **Day 2–3** — both stores in review; review feedback monitored.
- **Launch day** — both stores live; downloads work on real devices; web platform fully operational; documentation accessible.
- **Week 1** — zero critical issues; full HELIX governance tests runnable; metrics + reporting working; multi-provider API connectivity tested.

### Stated month-1 success metrics

Web: 500+ visitors, 50+ HELIX tests, 0 critical bugs. iOS: 100+ downloads, 4.5+ stars. Android: 150+ downloads, 4.5+ stars. Governance program: 3+ orgs onboarded, 10+ AI systems tested, 5+ certifications issued. These are publisher's own targets and should be treated as bounded claims, not external validation. Verification at the [[Hermes Dashboard — Professional Governance Tool]] level.

### Gates the runbook does not name

The runbook is internal-deployment-shaped; production governance requires the gates below. Treating them as part of "shipping" rather than "post-launch" is the doctrine implied by [[PHAROS Runbook SOP]] and the [[5-1 Rule — Locked Spec Hardening (Argus Stress Test)]]:

- **DNS / TLS** — `helix.pharos-ai.ca` resolved and TLS confirmed before announcement.
- **Secrets** — Anthropic, OpenAI, and Google API keys rotated and stored as environment variables on the Cloudflare Pages project and on the EAS build profile (operator-managed; per the credential-rotation closure already recorded in operator memory).
- **Bilingual EN/FR audit** — every UI string in EN and FR per the binding [[PHAROS SURFACE]] rule. The runbook does not flag this; it is a hard gate.
- **Diamond-Eyes pass** — wisdom-and-care review alongside technical correctness, per [[Diamond-Eyes — Aesthetic Refinement Skill]]. Required before promotion claims like "ready for production."
- **Cross-publish boundary** — HELIX is governance-platform-shaped and lives on the [[PHAROS SURFACE]]; do not announce it from the [[MARTIN SURFACE]] without an explicit cross-publish decision.

### Version 1.0 release notes (per the runbook)

HELIX v0.1.0 — Governance Training Platform. Features: full Pharos governance framework integration; four-phase governance testing (MÖBIUS, TRANSIT, PHAROS, TRAP); multi-provider API support; real-time conversation transcripts; governance metrics and reporting; mobile-optimized UI; dark theme.

## Related

- [[PHAROS Runbook SOP]]
- [[Cloudflare Pages-to-Worker Migration — Build and Asset Behavior]]
- [[PHAROS-AI Webservice — pharos-ai.ca]]
- [[Governance Stress-Test Protocols — Index]]
- [[Diamond-Eyes — Aesthetic Refinement Skill]]
- [[Hermes Dashboard — Professional Governance Tool]]
- [[5-1 Rule — Locked Spec Hardening (Argus Stress Test)]]
- [[AI Infrastructure Stack]]
- [[PHAROS Commercial Strategy]]
- [[README]]
- [[2026-04-30_helix-shipping-instructions-runbook]]
