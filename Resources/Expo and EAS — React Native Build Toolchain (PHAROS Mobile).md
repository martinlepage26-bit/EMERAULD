---
type: resource
title: Expo and EAS — React Native Build Toolchain (PHAROS Mobile)
aliases:
- Expo
- EAS
- Expo Application Services
tags:
- resource
- expo
- eas
- react-native
- mobile
- build
status: active
created: '2026-07-08'
updated: '2026-07-08'
---

# Expo and EAS — React Native Build Toolchain (PHAROS Mobile)

> For future Claude: Expo (React Native framework) plus EAS (Expo Application Services, the hosted build/submit/env-var service) is the build toolchain for PHAROS Expo apps: clearday in production use, fantasycast-gay scaffolded. The single most important operational fact here is the EAS env-var model, which caused clearday's open mock-Plus risk. Synthesized 2026-07-08 by the nightly pass from two same-day notes (confidence: high; all claims sourced from those notes).

## Summary

EAS builds run in Expo's cloud with environment variables injected from EAS-side configuration, not from local `.env` files. [[Areas/PHAROS/clearday — Mobile App and App Store Review State|clearday]] (Expo SDK 56, EAS project `3522d57f-6d80-4856-8f03-6e4c88bf1404`) hit exactly this: build 3 completed 2026-07-07 while `eas env:list production` returned "No variables found", so the `EXPO_PUBLIC_REVENUECAT_*` keys never entered the Hermes bundle. [[Areas/PHAROS/fantasycast-gay — Expo App|fantasycast-gay]] (Expo SDK ~54, Expo Router ~6) has EAS Build configured with a placeholder projectId.

## Context

- Blink-scaffolded projects (see [[Resources/Blink (blink.new) — App Scaffold and Hosted Backend Platform]]) are Expo apps and inherit this toolchain.
- Store submission downstream of EAS goes through [[Resources/App Store Connect and Apple App Review — PHAROS Submission Playbook|App Store Connect]]; monetization keys feed [[Resources/RevenueCat — Subscription Layer for PHAROS Mobile Apps|RevenueCat]].

## Details

**Env-var model (the operational trap):** `EXPO_PUBLIC_*` variables are baked into the JS bundle at build time. If they are absent from the EAS environment (`eas env:list <profile>`) and `eas.json` defines no env blocks, the build succeeds silently without them; any code with a fallback path (like clearday's mock subscription mode) then looks functional while running degraded. Check before every production build: `eas env:list production` must show the expected keys, or `eas.json` must define them per profile.

**Verification habits recorded in the source notes:**
- `expo config --type prebuild` to confirm icon/splash/notification asset wiring (used to verify clearday's 2.3.8 icon fix).
- Inspect the built Hermes bundle for expected key prefixes (e.g. `appl_...` for RevenueCat) rather than trusting local config.

**Known state (2026-07-08):** clearday awaiting build 4 with icons fixed and RevenueCat keys still to be wired into the EAS production env; fantasycast-gay buildable in principle but still carries the unmodified Blink starter code and a placeholder EAS projectId.

## Related

- [[Areas/PHAROS/clearday — Mobile App and App Store Review State]]
- [[Areas/PHAROS/fantasycast-gay — Expo App]]
- [[Resources/RevenueCat — Subscription Layer for PHAROS Mobile Apps]]
- [[Resources/App Store Connect and Apple App Review — PHAROS Submission Playbook]]
- [[Resources/Blink (blink.new) — App Scaffold and Hosted Backend Platform]]
