---
type: resource
title: Blink (blink.new) — App Scaffold and Hosted Backend Platform
aliases:
- Blink
- blink.new
- blinkdotnew
tags:
- resource
- blink
- scaffold
- expo
- platform
status: active
created: '2026-07-08'
updated: '2026-07-08'
---

# Blink (blink.new) — App Scaffold and Hosted Backend Platform

> For future Claude: Blink (blink.new, npm scope `@blinkdotnew`) is an app-scaffold plus hosted-backend platform behind a family of projects generated on this host around 2026-06-16. Two vault notes reference "the Blink pattern" with no shared anchor; this note is that anchor. Synthesized 2026-07-08 by the nightly pass from those notes, not from direct platform research (confidence: medium on platform description, high on local usage).

## Summary

Blink is a scaffold-and-backend platform: projects are generated from a Blink starter template and persist data through Blink's hosted backend via `@blinkdotnew/sdk` (UI kit `@blinkdotnew/mobile-ui` on mobile). On this host it accounts for a family of Blink-generated apps, including [[Areas/PHAROS/fantasycast-gay — Expo App|fantasycast-gay]] and the [[Areas/PHAROS/Reflexive Inhabitation Audit — Built App|Reflexive Inhabitation Audit app]].

## Context

- [[Areas/PHAROS/fantasycast-gay — Expo App]]: an Expo/React Native project scaffolded from the Blink starter template (`@blinkdotnew/sdk` + `@blinkdotnew/mobile-ui`), described as "same family as other Blink-generated apps on this host"; its git history starts at "Initial commit from Blink".
- [[Areas/PHAROS/Reflexive Inhabitation Audit — Built App]]: persists data through the Blink platform's hosted backend (`@blinkdotnew/sdk`), API wiring in `src/lib/blink-api.ts`.
- Relationship to [[Resources/Expo and EAS — React Native Build Toolchain (PHAROS Mobile)|Expo/EAS]]: Blink scaffolds Expo apps; build and submission still go through the standard Expo/EAS toolchain.

## Details

- The scaffold family on this host dates to roughly 2026-06-16 (per the fantasycast note's framing of the scaffold batch).
- Pattern to expect in Blink-scaffolded repos: minimal git history ("Initial commit from Blink"), `@blinkdotnew/*` dependencies, hosted-backend persistence rather than a local API, and starter code that may remain unmodified even when the app has a distinct product identity (fantasycast-gay is titled as a product but the code inside is still the unmodified starter, per its note).
- Unresolved: no vault note records Blink's pricing, backend data residency, or account ownership for the hosted backend. Verify before shipping any Blink-backed app to real users.

## Related

- [[Areas/PHAROS/fantasycast-gay — Expo App]]
- [[Areas/PHAROS/Reflexive Inhabitation Audit — Built App]]
- [[Resources/Expo and EAS — React Native Build Toolchain (PHAROS Mobile)]]
