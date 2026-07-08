---
type: product
title: Montréal+ (montreal-plus) — Mobile App
tags:
- mobile-app
- capacitor
- civic-tech
- montreal
- store-submission
- ship-assessment
- pharos
- vm-inventory
- product
- areas
status: active
domain: pharos
created: '2026-07-08'
updated: '2026-07-08'
vault_area: Areas
canonical_path: Areas/PHAROS/Montréal+ (montreal-plus) — Mobile App.md
backlink_count: 4
backlinks:
- '[[Areas/PHAROS/PHAROS Product Stack]]'
- '[[Areas/PHAROS/fantasycast-gay — Expo App]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
---

# Montréal+ (montreal-plus) — Mobile App

> For future Claude: this product exists in **two divergent, incompatible
> lineages** — a GitHub repo that is the billing/CI source of truth, and an
> untracked local directory with the better UI and a fake paywall. Do not
> assume the local disk copy is deployable, and do not assume the GitHub
> copy has the AI assistant. Read the ship-assessment handoff before touching
> either. This note synthesizes disk state as of 2026-07-08; treat it as a
> snapshot, not a live status.

## Summary

Montréal+ is a Capacitor-based civic-assistant mobile app for Montréal
(permits, waste collection, parking, 311 reporting) with a bundled AI
assistant. It exists as **two divergent versions**: the GitHub repo
`martinlepage26-bit/MTL-PLUS` (real Play Billing, green CI, source of truth
for shipping) and an untracked local fork at
`/home/martin/apps/mobile-apps/montreal-plus/` (better onboarding/UI + a real
Anthropic-backed AI assistant, but a **fake paywall** that only writes to
localStorage). A dated ship-readiness assessment
(`docs/handoff/ship-assessment-2026-07-08.md`) concluded the app is **not
shippable today** but close on Android, with reconciling the two forks as the
top-priority action.

## Context

Sources read (read-only):
- `/home/martin/apps/mobile-apps/montreal-plus/BUILD.md` (French-language
  build guide, Capacitor 6, `npm run` command reference, App Store /
  Play Store asset requirements, bundle id `ca.pharos.montreal`)
- No `README.md` exists in the local directory
- `/home/martin/.claude/projects/-home-martin/memory/project_montreal_plus.md`
  (prior session memory, dated 2026-07-08)
- `/home/martin/apps/mobile-apps/montreal-plus/docs/handoff/ship-assessment-2026-07-08.md`
  — found via glob under `docs/handoff/`, dated 2026-07-08, authored by
  Claude (Fable 5) on mtl-03, described as "evidence-based: every claim
  below was verified on disk, in git, in GitHub Actions, or over HTTP
  during this session"

Credential/signing material **exists but was not read**: an Apple App Store
Connect API key (`AuthKey_JXYZY4G4JR.p8`) sits in the app directory, and an
Android upload keystore exists at `~/.montreal-plus.keystore` (loaded into
GitHub Actions secrets as of 2026-06-29). Their presence is noted only —
paths and file contents were not inspected beyond confirming they exist on
disk, per read-only handling rules.

## Details

### Two lineages compared

| | GitHub `MTL-PLUS` main (source of truth) | Local `montreal-plus/` (untracked, this box) |
|---|---|---|
| app.js | 381 lines, v1 UI | 768 lines, "v2 + Capacitor Native Layer" |
| Billing | **Real** — `billing.js` + cordova-plugin-purchase (Play Billing) + StoreKit 2 adapter | **Fake** — `upgrade()` writes localStorage only |
| AI assistant | Canned answers, no API call | Real Anthropic integration via Cloudflare Worker proxy (`worker.js`) |
| Onboarding / upsell | No | Yes |
| Capacitor version | 7 (`ca.pharosai.montrealplus`) | 6 (`ca.pharos.montreal`) |
| CI | Green — signed AAB builds succeed (last verified 2026-06-29) | Cannot build locally (mtl-03 is aarch64; Android AAPT2 is x86-64 only) |
| Plan ladder | Household $9.99 / Pro $49 / Team $199+ | Resident $9.99 / Pro $49/mo or $399/yr |

The build constraint is structural, not incidental: **CI is the only build
path** for this app on this host.

### Ship-assessment verdict (2026-07-08, verbatim summary)

**Not shippable today, but close on Android.** The core blocker is that two
divergent versions exist and neither is complete alone. Verified-done items:
Capacitor 7 Android project committed with full icon/splash set; upload
keystore loaded into GitHub secrets; 4 consecutive green signed-AAB CI runs
(2026-06-29); a complete `PLAY_STORE.md` runbook in-repo; an iOS build
workflow drafted but not yet activated (no Apple secrets configured); Apple
Developer account/API key present on disk; a generic (not app-specific)
privacy policy live at pharos-ai.ca/privacy-policy.

**Near-path work (Android, ~1–2 engineering days) per the assessment:**
1. Reconcile the fork — merge local v2's UI/AI layer onto the GitHub billing
   lineage before it is lost (it exists only as untracked files on this
   disk).
2. Lock the permanent Android package id now — `ca.pharosai.montrealplus`
   is a declared placeholder and cannot change after first Play upload.
3. Unify the plan ladder (Household/Pro/Team vs. Resident/Pro) so Play
   Console subscription ids match `billing.js` exactly.
4. Deploy the Cloudflare Worker AI backend and fix the relative `WORKER_URL`
   (currently `/api/ask`, dead inside a native WebView).
5. Secrets hygiene — local `build.gradle` hardcodes a keystore password;
   move to the CI-injected signing pattern. Move the Apple API key out of
   the project directory.
6. Device-test the purchase flow (flagged in `PLAY_STORE.md` as reviewed but
   never tested on-device) — mandatory before production.

**Business tasks (cannot be done from this box):** register a Play Console
account (company account recommended to skip the 20-tester/14-day
closed-testing gate); create the app + three subscriptions; store listing
assets — the on-disk store-screenshots zip is an empty 22-byte file; a
1.2 MB demo `.mp4` may serve as promo-video source material.

**iOS is a second wave**: the build workflow needs Apple secrets (none set),
the iOS in-app-purchase dependency referenced in `billing.js` is missing
from `package.json` (iOS billing silently no-ops as written), and App Store
Connect setup is still pending.

### Store-submission readiness

The assessment explicitly frames the app as appearing close to
store-submission-ready on the Android side: signing material (keystore) and
an Apple auth key already exist on disk, CI produces a signed release
artifact, and a Play Store runbook is written. Submission is nonetheless
blocked on the fork-reconciliation and business-account decisions above —
"near-ready infrastructure" should not be read as "ready to submit."

### Key risks (from the assessment)
- **Data loss**: the better UI/AI fork is uncommitted and untracked on one
  disk only.
- **Policy rejection**: shipping the local v2 as-is (visible paywall, no
  real billing) is a guaranteed Play/App Store rejection.
- **Git hygiene**: `/home/martin/apps/mobile-apps` itself is the MTL-PLUS
  git clone, with unrelated app directories sitting untracked inside it.

### Pending Martin decisions
Permanent package id, plan-ladder naming, and personal-vs-company Play
account. Per the assessment, engineering work can proceed autonomously once
those three are set.

## Related

- [[Areas/PHAROS/PHAROS Product Stack]] — canonical PHAROS product-family bridge note.
- [[Areas/PHAROS/fantasycast-gay — Expo App]] — another mobile app on the same VM, at a much earlier (scaffold-only) stage; useful contrast for "scaffold vs. near-shippable" maturity.
- [[Areas/PHAROS/App Ideas — Hybrid Gaming Entertainment Social Fitness Music (2026)]] — vault's broader app-concept catalog.
