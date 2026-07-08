---
type: product
title: clearday — Mobile App and App Store Review State
tags:
- clearday
- pharos
- mobile
- expo
- app-store
- revenuecat
- monetization
- health-app
- areas
status: active
domain: pharos
created: '2026-07-08'
updated: '2026-07-08'
vault_area: Areas
canonical_path: Areas/PHAROS/clearday — Mobile App and App Store Review State.md
---

> For future Claude: this note documents Clearday, a PHAROS product app that was previously only glancingly mentioned in the vault. It exists to give session context on what the app is, why Apple rejected it on 2026-07-06, what has been fixed since, and what production risk remains open. Source paths are cited inline so claims can be re-verified against the live repos rather than trusted from memory. Never write credentials (passwords, API keys, tokens) into this note even when updating it.

## Summary

Clearday is a bilingual (EN/FR) Expo React Native mobile app for perimenopause symptom and cycle tracking, with AI-assisted education ("Ask"), pattern insights, and clinician-summary export. It is a PHAROS product app (not client work), operated by Martin Lepage / Pharos AI Inc. The mobile repo lives at `/home/martin/apps/mobile-apps/clearday-mobile`; a companion web surface (marketing site, privacy policy, support page) lives at `/home/martin/websites/clearday`. As of 2026-07-06 the app was rejected by Apple App Review; as of 2026-07-08 two of three rejection reasons are fixed and the app carries an unresolved production-monetization risk (mock-Plus mode) that must be closed before resubmission.

## Context

**Product identity** (source: `/home/martin/apps/mobile-apps/clearday-mobile/clearday-app-description-claude-code-chrome-2026-07-06.md`, 2026-07-06):
- Stack: Expo SDK 56, React Native 0.85, React 19, expo-router, NativeWind v4, TanStack Query v5, Base44 REST backend (function `cleardayCore2`).
- App Store Connect app ID `6776464254`, bundle ID `app.clearday.mobile`, EAS project `3522d57f-6d80-4856-8f03-6e4c88bf1404`, brand color `#2D6A4F`.
- Target launch markets: Canada, US, France, Belgium, Switzerland. Positioning is explicitly educational, not medical.
- Monetization: freemium + "Clearday Plus" subscription via RevenueCat (`react-native-purchases`). Free tier = daily log, 7-day history, 3 Ask/week. Plus tier ($7.99 CAD/mo or $59.99 CAD/yr, 14-day trial on annual only) = unlimited history, patterns tab, unlimited Ask, clinician summaries. Product IDs `clearday_plus_monthly` / `clearday_plus_yearly`, RevenueCat entitlement `plus`.

**App Store review rejection** (source: `/home/martin/.claude/projects/-home-martin/memory/project_clearday_appreview.md`, dated 2026-07-06/2026-07-08 — ASC app `6776464254`):

Apple rejected the app on 2026-07-06 for three reasons:
1. **Guideline 2.3.8** — placeholder icons. All six icon files in `assets/` were unmodified Expo default template art (blue chevron); no brand icon source existed in the repo.
2. **Guideline 2.1(a)** — no demo account provided for reviewers.
3. **Guideline 1.5** — broken support URL.

**Fixes since 2026-07-06, as of 2026-07-08:**
- **Demo account** — code now grants Plus entitlement to a reviewer account, gated by a constant `REVIEW_ACCOUNT_EMAILS` in `src/lib/subscription.ts`. Account name only, per this note's confidentiality rule: **appreview@clearday.app**. Martin must register that account in-app and enter its credentials in App Store Connect's App Review Information field himself (never stored in this vault). The entitlement grant is client-side only — the Base44 backend never grants Plus server-side.
- **Support URL** — the site repo `/home/martin/websites/clearday` had no `/support` route. A static bilingual `support/index.html` was added, committed, and deployed 2026-07-06 to both GitHub Pages (`martinlepage26-bit.github.io/clearday/`) and a Cloudflare Pages project (`clearday-e9i.pages.dev`, personal Cloudflare account) with custom domain `clearday.govern-ai.ca` active. A second custom domain, `clearday.pharos-ai.ca`, is registered on the same Pages project but was still pending a CNAME record in the pharos-ai.ca zone as of 2026-07-06 — neither the wrangler OAuth session nor the Lavoie Cloudflare API token had DNS write access there, so this requires a manual dashboard step. The root `clearday.app` domain itself sits on Namecheap default parking DNS, not on Cloudflare at all.
- **Icons** — resolved 2026-07-08. Six complete Expo icon/splash asset kits were generated as candidates (`store-assets/icon-candidates/{1-sunrise-field,2-deep-dawn,3-c-aperture,4-horizon,5-cycle-ring,6-radiant}/`); Martin selected **5-cycle-ring** over the AI-recommended 3-c-aperture. The chosen kit was applied over `assets/`, `app.json` updated (adaptive icon background `#FAFAF8`, monochrome image added, `expo-splash-screen` configured, `expo-notifications` icon switched to the monochrome silhouette — which incidentally fixed a pre-existing Android notification-icon bug). Verified via `expo config --type prebuild` and a composited Android mask render. Changes were uncommitted as of 2026-07-08. The 2.3.8 icon blocker is considered closed pending the next EAS build (build 4).

**Mock-Plus production risk (open, high priority):** iOS build 3 finished on EAS 2026-07-07, but `eas env:list production` returned "No variables found" — no RevenueCat API key (`appl_...`) was present in the built Hermes bundle. The subscription layer (`src/lib/subscription.ts`) silently falls back to a client-side mock mode whenever the `EXPO_PUBLIC_REVENUECAT_*` env vars are absent at build time, and `eas.json` has no env blocks defined. Practical consequence: a production build submitted without EAS-side environment variables would fake-grant Plus entitlement on any purchase tap, with no real payment processed and no server-side check. This must be verified and closed (RevenueCat key wired into the EAS production env) before the next submission, or the app risks both a failed purchase flow in production and a renewed App Store rejection.

**Other state as of 2026-07-08:**
- Android production builds have failed 7 consecutive times with `EAS_BUILD_UNKNOWN_GRADLE_ERROR` (most recently 2026-07-07); a paid EAS plan's larger resource class is likely needed. Android submission is deferred, not currently blocking the iOS resubmission.
- The 7-day free-history gate (a freemium acceptance criterion) is wired and covered by `freemium.test.ts` — verified 2026-07-08 after an earlier grep-based check had incorrectly reported it missing.
- The mobile repo has its own git history (remote `martinlepage26-bit/clearday-mobile`); as of 2026-07-08 it had 4 unpushed Android-fix commits and uncommitted icon/version changes.
- Full execution handoff with RevenueCat + App Store Connect setup steps, product/entitlement IDs, and acceptance criteria: `/home/martin/apps/mobile-apps/clearday-mobile/clearday-mobile-claude-chrome-handoff-2026-07-06.md`.

**Web surface** (source: `/home/martin/websites/clearday/LAUNCH-GUIDE.md` and `PROGRESS.md`, last updated 2026-06-29/2026-07-06): a separate Vite-based marketing site at `/home/martin/websites/clearday` (`LAUNCH-GUIDE.md` is a step-by-step Google Play submission guide; Google Play submission has not yet occurred). `PROGRESS.md` tracks outstanding i18n gaps (7 hardcoded English strings needing translation), ESLint warnings (18, all unused imports), and a GDPR/Quebec Law 25 compliance checklist flagging gaps in data export/portability and privacy-policy linkage from in-app Settings. Google Play submission is a separate, later-stage task from the iOS App Store resubmission described above.

**Governed ASC/RevenueCat task connection (2026-07-06):** the icon, demo-account, and support-URL fixes above were produced under a governed "boil the ocean" execution handoff (`clearday-mobile-claude-chrome-handoff-2026-07-06.md`) that also defines the remaining external, credential-gated steps: creating the RevenueCat project and connecting it to App Store Connect, importing the two subscription products, creating the `plus` entitlement, and wiring the resulting API key into the EAS production build environment. As of 2026-07-08 a follow-up prompt pack (`clearday-claude-chrome-prompts-2026-07-08.md`, same repo) sequences these external ASC/RevenueCat steps; after the RevenueCat key is confirmed set, the next step is cutting EAS iOS build 4 and resubmitting.

## Details

| Item | Value | Source |
|---|---|---|
| Mobile repo | `/home/martin/apps/mobile-apps/clearday-mobile` | repo listing, 2026-07-08 |
| Web repo | `/home/martin/websites/clearday` | repo listing, 2026-07-08 |
| ASC App ID | `6776464254` | app description, 2026-07-06 |
| Bundle ID | `app.clearday.mobile` | app description, 2026-07-06 |
| Brand color | `#2D6A4F` (deep teal green) | app description, 2026-07-06 |
| Rejection reasons | 2.3.8 icons, 2.1(a) demo account, 1.5 support URL | project_clearday_appreview.md, 2026-07-06 |
| Demo account (name only) | appreview@clearday.app | project_clearday_appreview.md, 2026-07-06 |
| Open risk | mock-Plus fallback in production build absent RevenueCat env key | project_clearday_appreview.md, verified 2026-07-08 |
| Icon fix status | closed 2026-07-08, pending build 4 | project_clearday_appreview.md, 2026-07-08 |
| Android build status | 7 consecutive Gradle failures, deferred | project_clearday_appreview.md, 2026-07-08 |
| Web deployment | GitHub Pages + Cloudflare Pages (`clearday.govern-ai.ca` live; `clearday.pharos-ai.ca` pending CNAME) | project_clearday_appreview.md, 2026-07-06 |

This app sits within the broader [[Areas/PHAROS/PHAROS Product Stack|PHAROS Product Stack]] as a consumer-facing mobile product rather than a governance-tooling product, and its release-readiness work follows the same PHAROS operating discipline (uncommitted-until-verified changes, explicit acceptance criteria, credential-gated external steps left to Martin) used across the stack.

## Related

- [[Areas/PHAROS/PHAROS Product Stack|PHAROS Product Stack]]
- [[Areas/Personal/Personal and Projects MOC|Personal and Projects MOC]]
