---
type: product
title: fantasycast-gay — Expo App
tags:
- mobile-app
- expo
- react-native
- blink-scaffold
- unstarted
- pharos
- vm-inventory
status: active
domain: pharos
created: '2026-07-08'
updated: '2026-07-08'
vault_area: Areas
canonical_path: Areas/PHAROS/fantasycast-gay — Expo App.md
---

# fantasycast-gay — Expo App

> For future Claude: this note documents a directory found on disk during a
> vault-coverage sweep of `apps/mobile-apps/` on the mtl-03 VM. It had zero
> vault coverage before this note. Treat the "what it is" section skeptically
> — the directory name implies an idea (gay-oriented fantasy casting/dating
> app) but the code inside is still the unmodified Blink Expo starter
> template. Verify against disk before assuming any feature work exists.

## Summary

`fantasycast-gay` is an Expo/React Native project scaffolded from the Blink
starter template, sitting at
`/home/martin/apps/mobile-apps/fantasycast-gay/`. As of this audit it
contains only the default template screens — no app-specific UI, no custom
entities, no branding beyond the directory name. It is best read as a
reserved slot / idea placeholder rather than a built product.

## Context

- Source read: `README.md`, `package.json`, `app.json`, and the `app/`
  directory (read-only; no credentials or keys inspected beyond noting
  `.env.local` exists — its contents were not read).
- Git history: two commits, both titled "Initial commit from Blink" /
  "Initial commit" — file mtimes on disk are 2026-06-16. No subsequent
  commits, no evidence of custom feature work.
- `app/` contains exactly three files: `index.tsx`, `_layout.tsx`,
  `+not-found.tsx` — the stock Expo Router skeleton, unmodified.
- `app.json` still declares the template's own identity: app name
  `blink-expo-starter`, iOS bundle id `com.blink.expostarter`, Android
  package `com.blink.expostarter`, and an EAS `projectId` placeholder
  (`"your-project-id-here"`) — none of these have been customized for a
  "fantasycast-gay" product identity yet.
- `package.json` name is also `blink-expo-starter`, version `1.0.0`.

## Details

**Stack (as declared in `package.json`):**
- Expo SDK ~54, Expo Router ~6 (file-based navigation)
- React 19.1.0 / React Native 0.81.5
- TypeScript
- `@blinkdotnew/sdk` + `@blinkdotnew/mobile-ui` — this is a Blink-platform
  scaffold (same family as other Blink-generated apps on this host, see
  Related below)
- TanStack Query, AsyncStorage, Reanimated, Gesture Handler
- Notable Expo modules present but unused by any custom screen yet:
  `expo-location`, `expo-image-picker`, `expo-av`, `expo-haptics`,
  `expo-linear-gradient` — these hint at an intended feature set (media,
  location-aware matching/casting, photo upload) consistent with a
  dating/casting-style app, but none of it is wired into the three stock
  screens present.
- Build tooling: EAS Build configured (`eas.json`) but pointed at a
  placeholder project id; `bun` supported as a faster alternative to `npm`.

**State: pre-development / scaffold only.** No product decisions,
onboarding flow, data model, or backend integration exist on disk. This is
functionally an empty shell reserved under a suggestive name.

## Related

- [[Areas/PHAROS/App Ideas — Hybrid Gaming Entertainment Social Fitness Music (2026)]] — the vault's existing catalog of unbuilt app concepts; this scaffold is a candidate for cross-referencing there if the fantasy-casting concept gets formalized.
- [[Areas/PHAROS/PHAROS Product Stack]] — canonical bridge note for the PHAROS product family; `fantasycast-gay` is not yet part of any shipped stack.
- [[Areas/PHAROS/Montréal+ (montreal-plus) — Mobile App]] — another mobile app on the same VM, at a much more advanced (near-shippable) stage; useful contrast for "scaffold vs. shippable" maturity.
- [[Areas/PHAROS/Reflexive Inhabitation Audit — Built App]] — another same-day (2026-06-16) Blink-scaffolded project on this host, for cross-referencing the Blink-template pattern.
