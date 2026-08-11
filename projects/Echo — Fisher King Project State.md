---
type: project
title: Echo — Fisher King Project State
tags:
- project
- fisher-king
- echo
- voice
- implementation-surface
- projects
- site
- profile
- implementation
- martin
status: active
priority: medium
created: '2026-05-07'
updated: '2026-08-07'
vault_area: projects
canonical_path: projects/Echo — Fisher King Project State.md
backlink_count: 10
backlinks:
- '[[Areas/PHAROS/2026-06-29 - idea-discovery]]'
- '[[wiki/Fisher King Hub — Project Recovery Map]]'
- '[[wiki/Healing the Fisher King Project Note Templates]]'
- '[[wiki/Master Project Tracker — 2026]]'
- '[[wiki/Projects Hub]]'
- '[[memory/daily/2026-06-22]]'
- '[[memory/daily/2026-06-23]]'
- '[[memory/daily/2026-06-24]]'
- '[[memory/daily/2026-06-25]]'
- '[[memory/daily/2026-06-26]]'
---

# Echo — Fisher King Project State

## Status
active — disambiguated (see 2026-08-02 below); healing project closed, product-tracking continues

> [!info] Disambiguation resolved — 2026-08-02
> **Verified fact (read the live repo and code directly, this session):** Echo is a real, implemented, deployed public app — not a discourse-feedback surface, not planned/conceptual. It moved hosts and stacks since this note's 2026-05-07/06-26 snapshots: the `/home/cerebrhoe/martin-lepage-site/` Astro implementation described below is from the *previous* host and is dead (per [[Areas/PHAROS/Old Host Retirement Record — cerebrhoe and WSL (2026-07-09)|Old Host Retirement Record]]). The current, live implementation is a standalone Expo Router app on Cloudflare Workers — see Canonical State & Artifact below for the corrected paths. The Core Question below is answered: **live public app**, specifically a browser-native voice reader (TTS readback + STT dictation).

## Core Question (historical — see resolution above)
What is Echo in the system: a voice/TTS utility, a discourse feedback surface, a public app, or a downstream implementation test of the PHAROS method?

## Why It Matters Now
Echo is not yet well documented inside EMERAULD, but external workspace evidence shows it is a real surface: Martin site pages, TTS/transcription functions, Playwright outputs, and a HEPHAISTOS rebuilt profile. The profile marks Echo as bounded-low confidence and planned/conceptual in one snapshot, while the Martin site appears to contain implemented public surfaces. That mismatch is the wound.

*(2026-08-02: wound closed — see disambiguation above. The mismatch was a stale profile plus a host migration, not an actual ambiguity in what Echo is.)*

## Current Direction
~~Heal by source recovery. Do not overclaim Echo's status until the public site implementation and HEPHAISTOS profile are reconciled.~~ *(superseded 2026-08-02 — reconciled; see below)*

Track as an active PHAROS/Martin-surface product. Next open items are feature-completeness (PDF parsing on the edge runtime, provider-error UX) and a session-continuity register (see Next Synthesis Move), not identity.

## Canonical State & Artifact
- Primary Canonical Artifact: this note (no separate `wiki/Echo — Canonical Position` note created yet — see Next Synthesis Move)
- **Current Implementation Surface (2026-08-02, verified live):** `/home/martin/work/web-apps/ECHOapp` (`apps/web-apps/ECHOapp/` per [[Areas/PHAROS/company|company.md]]'s product table) — Expo Router (SDK 54) + React Native app, three screens (Readback / Dictation / Library)
- **Backend/edge (2026-08-02, verified live):** `workers/echo-ai/src/worker.js` — Cloudflare Worker serving the Expo web export as static assets plus `/api/*` (Deepgram Aura-2 TTS, Whisper large-v3-turbo STT via Workers AI; D1-backed drafts/transcripts storage; edge `.txt`/`.md`/`.docx` parsing). A parallel FastAPI/Motor Python backend (`backend/server.py`) exists with pluggable providers (Piper/OpenAI/ElevenLabs/Workers AI/local SpeechT5 clone voices) but is not what's live in production.
- **Live URL:** https://echo-ai.martinlepage26.workers.dev/readback
- Superseded (dead, previous host): `/home/cerebrhoe/martin-lepage-site/src/pages/echo/index.astro`, `/home/cerebrhoe/martin-lepage-site/functions/api/echo-tts.js`, `/home/cerebrhoe/martin-lepage-site/functions/api/echo-transcribe.js`, `/home/cerebrhoe/HEPHAISTOS_BUILD/.../04_IMPLEMENTATION_SURFACE_echo_PROFILE.md`
- Artifact Status: live and verified (this session read the code, ran the backend test suite, deployed, and curl-tested the production API)
- Confidence: high (direct code read + live verification, not inference)
- Last reviewed: 2026-08-02
- Review Owner/Signatory: Martin

## Active Tensions (historical, resolved 2026-08-02)
- ~~HEPHAISTOS profile says planned/conceptual, with bounded-low confidence.~~ Profile was stale/previous-host; current implementation is confirmed live.
- ~~Martin site contains Echo pages, scripts, and deployment artifacts.~~ Correct, but that surface is retired — Echo now lives at `web-apps/ECHOapp` + `workers/echo-ai`, not `martin-lepage-site`.
- ~~Echo may be a voice utility, a PHAROS feedback channel, or both.~~ Resolved: voice utility (readback + dictation), packaged as a public app, not a feedback channel.

## Contradictions To Preserve
- Echo should not be promoted as a mature product if the canonical note is missing. *(This note now serves that role; no risk of overclaiming remains, but see Next Synthesis Move — a dedicated `wiki/` canonical note is still the more durable long-term home.)*
- It also should not be dismissed as imaginary when code and public-surface artifacts exist. *(No longer at risk — implementation is verified live, not just claimed.)*

## Relevant Materials
- `/home/martin/work/web-apps/ECHOapp/PRODUCT.md`, `PRD.md` (memory/), `README.md` — product intent, design principles, accessibility stance
- `/home/martin/work/web-apps/ECHOapp/workers/echo-ai/src/worker.js`, `wrangler.toml`, `README.md` — edge implementation
- `/home/martin/work/web-apps/ECHOapp/backend/server.py`, `speech_providers.py` — parallel Python API (not production)
- `/home/martin/work/web-apps/ECHOapp/docs/handoff/` — prior session handoffs (provider decouple, Workers AI wiring, deploy attempts)
- Historical/dead (previous host, kept for provenance only): `/home/cerebrhoe/HEPHAISTOS_BUILD/.../04_IMPLEMENTATION_SURFACE_echo_PROFILE.md`, `/home/cerebrhoe/martin-lepage-site/src/pages/echo/index.astro`, `/home/cerebrhoe/martin-lepage-site/src/scripts/echo-*.js`, `/home/cerebrhoe/martin-lepage-site/tests/echo-dictation-utils.test.mjs`

## Recent Moves
- External file discovery found Echo implemented in Martin site. *(historical — that surface is now retired)*
- HEPHAISTOS rebuilt profile preserves an older or bounded interpretation: discourse feedback and recursion commentary, planned/conceptual. *(historical — superseded)*
- **2026-08-07 — durable-speech repair + clone-tunnel hardening.** Root cause of production TTS 502s found and fixed (Workers AI free daily neurons exhausted → SpeechT5 clone made a mandatory fallback, not just a demo path, at both the Worker and Pages-proxy layers; bare 502s replaced with real JSON errors). Same-day code-review refactor split the 986-line `worker.js` and 2179-line `echo-reader.js` into modular layers, no behavior change. Follow-up same day: closed the tunnel-fragility residual risk flagged by the repair — the SpeechT5 clone origin moved from an ephemeral `trycloudflare.com` quick tunnel to a named Cloudflare Tunnel (`echo-clone-api.pharos-ai.ca`) fronted by `systemd --user` units (`echo-clone-backend.service`, `echo-clone-tunnel.service`, both `Restart=on-failure`) with `loginctl enable-linger` set, so the clone origin now survives host reboot without an interactive login. All verified live in production this session (hardline site, Worker/Aura path, Expo direct-Worker path). See `web-apps/ECHOapp/docs/handoff/echo-durable-speech-repair-2026-08-07.md` and `echo-clone-tunnel-hardening-2026-08-07.md`.
- **2026-08-02 — Library tab fixed + shipped to production.** The live Cloudflare Workers deploy had drafts/transcripts/file-import fully broken (503s) since the app moved off the Python/Mongo backend — nothing implemented storage on the edge. Added D1-backed drafts/transcripts CRUD to `workers/echo-ai/src/worker.js` matching the frontend's existing contract; implemented `/api/parse-file` on the edge for `.txt`/`.md`/`.docx` (pure-JS zip+XML extraction via `fflate`; `.pdf` returns a clear 415 rather than a generic failure — edge PDF parsing is still unimplemented, flagged as an open item below); dictation transcripts now auto-save to Library. Added accessibility labels/roles/states across all three screens and the tab bar (previously none, despite PRODUCT.md's Accessibility & Inclusion section). Verified: backend pytest (11/11), frontend `tsc`/`eslint` clean, local `wrangler dev` smoke tests, then live curl checks against production confirming `storage: "d1"` and working create/list/delete. D1 database `echo-ai-db` provisioned and migrated on the `Martinlepage26@me.com` Cloudflare account; deployed via `scripts/deploy-cf.sh`.

## Consequence Binding
- What changes if we execute the next move? → *(2026-08-02: identity question already answered by this update.)* Remaining next move (edge PDF parsing, or a dedicated `wiki/` canonical note) would close the last documentation/feature gaps, not the identity gap.
- Real outcome / decision advanced: product role and status clarified — Echo is a live, working voice-reader app, actively maintained.
- Review/sign-off needed: none for the identity question (resolved by direct verification). Martin's call on whether a separate `wiki/Echo — Canonical Position` note is still worth creating given this project note now carries the same information.

## Blockers
- ~~No canonical EMERAULD wiki note.~~ Addressed by this update (project note now carries current, verified state); a dedicated `wiki/` note is optional polish, not a blocker.
- ~~Possible drift between profile status and live implementation.~~ Resolved — verified directly against the live repo and production deploy.
- ~~Public role unclear.~~ Resolved.
- ~~Edge runtime has no PDF parser.~~ Resolved 2026-08-02 same day (commit `92d6c89`, edge `.pdf` parsing via `unpdf`) — this note's own "Open" line was stale until this 2026-08-07 pass caught it.
- **Open (product-level, not identity-level):** no rate-limiting on the Workers deploy equivalent to the Python API's per-IP limiter; `memory/PRD.md` inside the ECHOapp repo itself is stale (still describes the retired OpenAI-only stack and doesn't mention Workers AI, D1, or the SpeechT5 clone-voice provider). Tunnel/reboot fragility for the clone origin — closed 2026-08-07, see Recent Moves.

## Next Synthesis Move
~~Open the Echo page and scripts, create a canonical Echo wiki note, and reconcile whether Echo is live product, voice utility, or PHAROS method test surface.~~ *(Reconciliation done directly in this project note, 2026-08-02.)* Optional remaining polish: promote this into a dedicated `wiki/Echo — Canonical Position.md` per the original [[Areas/PHAROS/2026-06-29 - idea-discovery|idea-discovery]] plan, if Martin still wants a `wiki/`-level canonical note distinct from the project tracker.

