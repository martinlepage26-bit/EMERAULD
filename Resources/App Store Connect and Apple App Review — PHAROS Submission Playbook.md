---
type: resource
title: App Store Connect and Apple App Review — PHAROS Submission Playbook
aliases:
- App Store Connect
- ASC
- Apple App Review
tags:
- resource
- app-store
- asc
- apple
- mobile
- submission
status: active
created: '2026-07-08'
updated: '2026-07-08'
---

# App Store Connect and Apple App Review — PHAROS Submission Playbook

> For future Claude: this is the shared reference for Apple App Store Connect (ASC) submission and App Review across PHAROS mobile apps (clearday live in review, montreal-plus pending setup). Load it before any iOS submission task to avoid repeating the rejections already hit. Synthesized 2026-07-08 by the nightly pass from three same-day notes (confidence: high; all claims sourced from those notes).

## Summary

App Store Connect is Apple's submission and review surface. PHAROS state as of 2026-07-08: [[Areas/PHAROS/clearday — Mobile App and App Store Review State|clearday]] (ASC app ID `6776464254`, bundle `app.clearday.mobile`) was rejected on 2026-07-06 and is being remediated; [[Areas/PHAROS/Montréal+ (montreal-plus) — Mobile App|Montréal+]] has an ASC API key on disk with iOS "second wave" ASC setup still pending.

## Context

- The clearday ASC IAP setup plus RevenueCat configuration and TestFlight shipping was the first real governed task to produce a named co-equal authority conflict; see [[Areas/PHAROS/Co-Equal Authority Conflict — clearday ASC-RevenueCat Governed Task (2026-07-06)]].
- Subscription setup in ASC is coupled to [[Resources/RevenueCat — Subscription Layer for PHAROS Mobile Apps|RevenueCat]] entitlements; builds arrive via [[Resources/Expo and EAS — React Native Build Toolchain (PHAROS Mobile)|EAS]].

## Details

**Rejection guidelines already hit (clearday, 2026-07-06):**
1. **Guideline 2.3.8** — placeholder icons (unmodified Expo default template art). Fixed 2026-07-08 with the selected `5-cycle-ring` asset kit; considered closed pending EAS build 4.
2. **Guideline 2.1(a)** — no demo account for reviewers. Fixed via a reviewer account granted Plus client-side (`REVIEW_ACCOUNT_EMAILS` in `src/lib/subscription.ts`); Martin must register the account in-app and enter its credentials in ASC's App Review Information field himself. Credentials never go in the vault.
3. **Guideline 1.5** — broken support URL.

**Playbook items for the next submission (any app):**
- Ship real brand icons, never scaffold defaults (2.3.8 is a guaranteed rejection).
- Provide a working demo account in App Review Information before submitting (2.1(a)).
- Verify the support URL resolves (1.5).
- Verify monetization env keys exist in the production build itself; the clearday mock-Plus risk shows a missing key produces a fake-functional purchase flow that would fail 2.1 review or, worse, pass it.

**Credential boundary:** the montreal-plus note records that an Apple ASC API key exists on disk but was not read; keep it that way in vault notes per the standing rule against writing credentials.

## Related

- [[Areas/PHAROS/clearday — Mobile App and App Store Review State]]
- [[Areas/PHAROS/Montréal+ (montreal-plus) — Mobile App]]
- [[Areas/PHAROS/Co-Equal Authority Conflict — clearday ASC-RevenueCat Governed Task (2026-07-06)]]
- [[Resources/RevenueCat — Subscription Layer for PHAROS Mobile Apps]]
- [[Resources/Expo and EAS — React Native Build Toolchain (PHAROS Mobile)]]
