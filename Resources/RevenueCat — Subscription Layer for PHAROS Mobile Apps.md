---
type: resource
title: RevenueCat — Subscription Layer for PHAROS Mobile Apps
aliases:
- RevenueCat
- react-native-purchases
tags:
- resource
- revenuecat
- subscriptions
- iap
- mobile
- clearday
status: active
created: '2026-07-08'
updated: '2026-07-08'
---

# RevenueCat — Subscription Layer for PHAROS Mobile Apps

> For future Claude: RevenueCat is the subscription/entitlement platform (SDK `react-native-purchases`) used for PHAROS mobile monetization, currently in clearday. Load this note when working on in-app purchases, the Clearday Plus tier, or the open mock-Plus production risk. Synthesized 2026-07-08 by the nightly pass from two same-day notes (confidence: high; all claims sourced from those notes).

## Summary

RevenueCat handles the "Clearday Plus" subscription for [[Areas/PHAROS/clearday — Mobile App and App Store Review State|clearday]] via `react-native-purchases`: entitlement `plus`, product IDs `clearday_plus_monthly` / `clearday_plus_yearly` ($7.99 CAD/mo or $59.99 CAD/yr, 14-day trial on annual only). Its configuration is also the gated external step in the [[Areas/PHAROS/Co-Equal Authority Conflict — clearday ASC-RevenueCat Governed Task (2026-07-06)|clearday ASC/RevenueCat governed task]].

## Context

- Wiring lives in clearday's `src/lib/subscription.ts`; RevenueCat user identity is bound through `initSubscription(userId)` (the wiring item disputed in the co-equal authority conflict record).
- Reviewer accounts listed in `REVIEW_ACCOUNT_EMAILS` are granted Plus client-side only; neither RevenueCat nor the Base44 backend grants Plus server-side (see [[Resources/Base44 — Hosted Low-Code App Platform (PHAROS Usage Map)|Base44]]).

## Details

**The mock-Plus production risk (open, high priority, as of 2026-07-08):** clearday's subscription layer silently falls back to a client-side mock mode whenever the `EXPO_PUBLIC_REVENUECAT_*` env vars are absent at build time. iOS build 3 (EAS, 2026-07-07) shipped with `eas env:list production` returning "No variables found", so no RevenueCat API key (`appl_...`) is in the built Hermes bundle, and `eas.json` defines no env blocks. Consequence if unfixed: a production build would fake-grant Plus on any purchase tap with no real payment and no server-side check. The RevenueCat key must be wired into the EAS production env (see [[Resources/Expo and EAS — React Native Build Toolchain (PHAROS Mobile)]]) and verified before the next App Store submission.

General pattern worth keeping: RevenueCat integrations that mock themselves when env keys are missing fail silently and look functional in review; verify the key is present in the actual built bundle, not just in local config.

## Related

- [[Areas/PHAROS/clearday — Mobile App and App Store Review State]]
- [[Areas/PHAROS/Co-Equal Authority Conflict — clearday ASC-RevenueCat Governed Task (2026-07-06)]]
- [[Resources/App Store Connect and Apple App Review — PHAROS Submission Playbook]]
- [[Resources/Expo and EAS — React Native Build Toolchain (PHAROS Mobile)]]
