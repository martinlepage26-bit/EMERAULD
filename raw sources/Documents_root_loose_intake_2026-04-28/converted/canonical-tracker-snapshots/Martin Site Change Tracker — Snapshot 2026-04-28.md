---
type: raw-source
title: Martin Site Change Tracker — Snapshot 2026-04-28
tags:
- raw-source
status: preserved
created: '2026-04-28'
vault_area: raw sources
canonical_path: raw sources/Documents_root_loose_intake_2026-04-28/converted/canonical-tracker-snapshots/Martin Site Change Tracker — Snapshot 2026-04-28.md
---

# MARTIN-SITE CHANGE TRACKER

- Parent tracker: `/mnt/c/Users/softinfo/Documents/MASTER TRACKER (recreated from MASTER PACK 4).md`
- Scope: `martin.govern-ai.ca`, Martin public identity pages, Hephaistos narrative pages, governance tree pages, skill ecosystem pages, and standalone app surface changes hosted from the Martin site
- Excludes: PHAROS-only product or infrastructure changes unless they require Martin-side route or narrative updates

## Update Rule

- Append an entry at every major Martin-site change.
- Add a session-close note after each session that changed Martin public pages, narratives, trees, or standalone app surfaces.
- Include deploy and live-verification notes whenever the public site changed.

## Checkpoints

- [x] Martin site consolidated to single source of truth
- [x] Lotus bloom palette correction live
- [x] Lotus app-first routing restored
- [x] Live health-check automation script added (run-health-check.sh)
- [x] Audit de-tiering cleanup complete
- [ ] run-health-check.sh committed to martin-lepage-site repo

## Entries

### 2026-03-30 — Narrative, tree, and Hephaistos public-surface sync

- Martin site confirmed as the canonical public repo for `https://martin.govern-ai.ca`
- public narratives were updated to align with the live Hephaistos architecture:
  - governance is primary
  - philosopher and power-analyst are co-equal right-arms
  - public Hephaistos narratives and tree artifacts belong on the Martin surface
- updated public/source files included:
  - `src/content/projects/skill-ecosystem.md`
  - `src/content/research/hephaistos-skill-operating-system.md`
  - `src/content/research/authored-governance-tree-and-skill-ecosystem-maps.md`
  - `docs/hephaistos-skill-taxonomy-table.md`
  - `src/pages/hephaistos/index.astro`
  - `src/pages/governance/tree.astro`
  - `public/martin_lepage_governance_tree.html`
  - `public/skill_ecosystem_tree.html`
- live routes verified after deploy:
  - `https://martin.govern-ai.ca/hephaistos/`
  - `https://martin.govern-ai.ca/projects/skill-ecosystem/`
  - `https://martin.govern-ai.ca/martin_lepage_governance_tree`
  - `https://martin.govern-ai.ca/skill_ecosystem_tree`

### 2026-03-30 — Martin app/public boundary affirmed

- Martin public site remains the home for:
  - `/lotus`
  - `/scripto`
  - `/gaia`
  - `/echo`
  - `/dr-sort`
- Martin-side tree assets are now the canonical target of PHAROS redirects for:
  - `martin_lepage_governance_tree.html`
  - `skill_ecosystem_tree.html`
- Martin-side Lotus is now the canonical target of the old PHAROS `/portal/lotus` route

### 2026-03-30 — Lotus bloom palette correction

- corrected Lotus-only dark-mode token leakage in the standalone Lotus surface
- updated only the Lotus stylesheet pair:
  - `/home/cerebrhoe/martin-lepage-site/src/styles/lotus.css`
  - `/home/cerebrhoe/martin-lepage-site/public/lotus/lotus.css`
- replaced the amber/black leak points with bloom rose and mauve equivalents for:
  - `.link-inline` underline and hover underline
  - `.bullet-tags`, `.bullet-links`, and `.bullet-facts` markers
  - `.publication-card` background tint
  - `.publication-card-year` chip background
  - `.publication-card-status` border/background
  - `.writing-card-divider`
  - `.brand-monogram` lines
  - all six `.project-motif-*` treatments
- scope check:
  - no `global.css` or other non-Lotus site styles were changed
- verification:
  - `node scripts/lotus-validate.mjs` passed
  - `PATH=\"$HOME/.nvm/versions/node/v22.22.2/bin:$PATH\" npm run build` passed

### 2026-03-30 — Lotus release commit, push, and deploy

- committed the Lotus palette correction as:
  - `a41548c2ba1b8e88d58366e414f8681b428180e0`
  - message: `Refine Lotus bloom palette tokens`
- pushed commit `a41548c` to:
  - `origin/wip/reconcile-main-20260327-114047`
- deployed the committed Lotus release from a clean temporary checkout rather than the dirty working tree so unrelated Martin-site changes were not shipped
- Cloudflare Pages deploy URL:
  - `https://c52f2c77.martin-lepage-site.pages.dev`
- live verification:
  - `https://martin.govern-ai.ca/lotus/` returned `200`
  - `https://c52f2c77.martin-lepage-site.pages.dev/lotus/` returned `200`
  - `https://martin.govern-ai.ca/lotus/lotus.css` served the new rose token set

### 2026-03-30 — Lotus bloom restyle architecture note

- added the governing restyle architecture note at:
  - `/home/cerebrhoe/martin-lepage-site/docs/lotus-bloom-restyle-architecture.md`
- the note was produced through Hephaistos routing with `skill-architect` in build mode
- key conclusion:
  - the provided Lotus bloom specification is not a shallow style pass over the current public Lotus surface
  - it requires a product and IA split between:
    - primary `/lotus/` bloom journaling experience
    - secondary Lotus research workbench surface
- the architecture note grounds that conclusion against the live implementation in:
  - `src/pages/lotus/index.astro`
  - `src/components/lotus/LotusWorkbench.astro`
  - `src/components/lotus/LotusVectorWorkbench.astro`
  - `src/data/lotus.ts`
- the note defines:
  - delta-first audit
  - Brain layer: interaction rules and UX acceptance criteria
  - Map layer: route split, component map, state model, Figma exploration pack, engineering phases, and risks
- no deploy was performed for this architecture note

### 2026-03-30 — Lotus route split implemented

- implemented the approved Lotus product split on the Martin site:
  - primary ritual route remains `/lotus/`
  - analytical workbench route now lives at `/lotus/research/`
- added the new one-bloom journaling surface in:
  - `/home/cerebrhoe/martin-lepage-site/src/components/lotus/LotusBloomJourney.astro`
- replaced the public Lotus page with the bloom journey in:
  - `/home/cerebrhoe/martin-lepage-site/src/pages/lotus/index.astro`
- moved the prior workbench/vector surface into:
  - `/home/cerebrhoe/martin-lepage-site/src/pages/lotus/research/index.astro`
- updated Lotus data and project metadata so the public narrative matches the new structure:
  - `/home/cerebrhoe/martin-lepage-site/src/data/lotus.ts`
  - `/home/cerebrhoe/martin-lepage-site/src/content/projects/lotus.md`
- bloom-flow implementation details now live in the public route:
  - one active question and one active writing surface at a time
  - deliberate two-step submission with hold-to-close behavior
  - autosaved local drafts
  - backward review through stalk nodes without exposing prior answers in the forward state
  - separate completion state with research and project-record exits
- updated Lotus verification coverage to protect the split:
  - `/home/cerebrhoe/martin-lepage-site/scripts/lotus-validate.mjs`
  - `/home/cerebrhoe/martin-lepage-site/scripts/lotus-smoke.mjs`
- verification:
  - `PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH" npm run lotus:check` passed
  - `PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH" npm run build` passed
  - `PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH" npm run lotus:smoke` passed
- no deploy performed in this implementation pass

### 2026-03-30 — Lotus validator follow-up hardening

- ran a three-lane validation sweep on the new Lotus split:
  - UX/spec fidelity
  - route/runtime integrity
  - narrative/tracker consistency
- validator findings were used to tighten the public Lotus implementation without changing the route split itself
- updated the bloom component in:
  - `/home/cerebrhoe/martin-lepage-site/src/components/lotus/LotusBloomJourney.astro`
- changes made:
  - bound the textarea’s accessible name to the live question and phase label instead of a generic hidden label
  - changed completion/review rendering so the full stalk is visible rather than truncating to only the last four nodes
  - added stronger visual separation for review-mode descent versus forward ascent
  - added keyboard-aware viewport offset and focus-scrolling behavior to reduce mobile keyboard occlusion risk
- strengthened Lotus contract validation in:
  - `/home/cerebrhoe/martin-lepage-site/scripts/lotus-validate.mjs`
- the validator now checks for:
  - question-bound accessible naming
  - `100`-word cap preservation
  - deliberate `HOLD_MS = 650` submission timing
  - local storage persistence
  - full-stalk rendering in completion/review contexts
  - mobile keyboard-aware viewport handling
- verification:
  - `PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH" npm run lotus:check` passed
  - `PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH" npm run build` passed
  - `PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH" npm run lotus:smoke` passed
- residual:
  - Lotus still lacks a browser-driven interaction test that actually types through the bloom flow; current protection is source-contract plus route smoke, not end-to-end interaction replay

### 2026-03-30 — Lotus browser-driven interaction test added

- closed the last major Lotus validation gap by adding a real browser-driven E2E lane for the bloom state machine
- added Playwright harness files:
  - `/home/cerebrhoe/martin-lepage-site/playwright.config.ts`
  - `/home/cerebrhoe/martin-lepage-site/tests/lotus-bloom-e2e.spec.ts`
- updated package wiring in:
  - `/home/cerebrhoe/martin-lepage-site/package.json`
- added script:
  - `lotus:e2e`
- the E2E spec now drives the full Lotus path in one non-branching browser journey:
  - closed bud entry state
  - bloom opening
  - writing and word-count updates
  - near-limit warning state
  - exact `100`-word cap
  - deliberate hold-to-submit
  - stalk growth / next-bud pause
  - back-navigation review
  - local persistence through reload
  - full-stalk rendering on completion
- during the run, the new E2E lane exposed a real product bug:
  - Lotus still accepted extra characters after `100` words by appending them to the last word
- fixed that cap breach in:
  - `/home/cerebrhoe/martin-lepage-site/src/components/lotus/LotusBloomJourney.astro`
- strengthened source-contract validation in:
  - `/home/cerebrhoe/martin-lepage-site/scripts/lotus-validate.mjs`
  - it now explicitly checks that character growth is blocked once the cap is reached
- verification gate:
  - `PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH" npm run lotus:check` passed
  - `PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH" npm run build` passed
  - `PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH" npm run lotus:smoke` passed
  - `PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH" npm run lotus:e2e` passed
- residual:
  - the Playwright run emits a non-blocking Node warning about `NO_COLOR` being ignored when `FORCE_COLOR` is set by the test environment; this did not affect execution

### 2026-03-30 — Session-close status

- Lotus status at handoff:
  - `lotus:check` green
  - `build` green
  - `lotus:smoke` green
  - `lotus:e2e` green
- no commit performed
- no deploy performed

### 2026-03-30 — Lotus release committed, pushed, built, and deployed

- committed the Lotus release on branch `wip/reconcile-main-20260327-114047` in two bounded commits:
  - `15c00857a5d37de3e9c5d079f0d481151af2b09c` — `Build Lotus bloom journey release`
  - `0f121f16e74c0f116f35c287576cf2cf065c9a3c` — `Fix Lotus draft persistence on reload`
- push completed to:
  - `origin/wip/reconcile-main-20260327-114047`
- the second commit closed a real persistence seam found only when the release was rebuilt from a clean worktree:
  - Lotus had debounced draft saves, but reload could outrun the save timer
  - fixed in `/home/cerebrhoe/martin-lepage-site/src/components/lotus/LotusBloomJourney.astro`
  - strengthened in `/home/cerebrhoe/martin-lepage-site/scripts/lotus-validate.mjs`
- release verification was rerun from a clean committed tree at:
  - `/tmp/martin-lotus-release-0f121f16e74c0f116f35c287576cf2cf065c9a3c`
- clean release gate passed:
  - `PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH" npm run lotus:check`
  - `PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH" npm run build`
  - `PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH" npm run lotus:smoke`
  - `PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH" npm run lotus:e2e`
- deployed from the clean worktree build to Cloudflare Pages:
  - `https://8a59af98.martin-lepage-site.pages.dev`
- live route verification after deploy:
  - `https://8a59af98.martin-lepage-site.pages.dev/lotus/` -> `200`
  - `https://8a59af98.martin-lepage-site.pages.dev/lotus/research/` -> `200`
  - `https://martin.govern-ai.ca/lotus/` -> `200`
  - `https://martin.govern-ai.ca/lotus/research/` -> `200`
- non-blocking note:
  - Playwright still emits the environment warning about `NO_COLOR` being ignored when `FORCE_COLOR` is set; the E2E lane remained green and deployment was not affected

### 2026-03-30 — Lotus follow-up regression fix after release

- ran a post-release debug pass because the Lotus browser lane could still fail locally after the deploy
- root cause was split across test infrastructure and runtime interaction handling:
  - `lotus:e2e` could preview stale `dist/` output because the Playwright web server only ran `astro preview`
  - the deliberate bloom-close gesture was only wired to pointer events, which made the mouse-path regression lane less resilient after reload
- fixed in:
  - `/home/cerebrhoe/martin-lepage-site/playwright.config.ts`
  - `/home/cerebrhoe/martin-lepage-site/src/components/lotus/LotusBloomJourney.astro`
- concrete changes:
  - Playwright now runs `npm run build && npm run preview ...` before the Lotus browser spec
  - `reuseExistingServer` is now `false` so the lane cannot attach to a stale preview process
  - Lotus hold-to-submit now accepts both pointer and mouse down/up/leave paths
- committed and pushed:
  - `b2ac3ee2b6622aee7bbbff104b445cfe0f772f17` — `Harden Lotus browser regression path`
- clean-worktree verification rerun at:
  - `/tmp/martin-lotus-release-b2ac3ee2b6622aee7bbbff104b445cfe0f772f17`
- clean release gate passed again:
  - `PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH" npm run lotus:check`
  - `PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH" npm run build`
  - `PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH" npm run lotus:smoke`
  - `PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH" npm run lotus:e2e`
- deployed follow-up patch to Cloudflare Pages:
  - `https://56f78776.martin-lepage-site.pages.dev`
- post-deploy route checks:
  - `https://56f78776.martin-lepage-site.pages.dev/lotus/` -> `200`
  - `https://56f78776.martin-lepage-site.pages.dev/lotus/research/` -> `200`
  - `https://martin.govern-ai.ca/lotus/` -> `200`
  - `https://martin.govern-ai.ca/lotus/research/` -> `200`
- session-close note:
  - Lotus is now green locally, green from a clean release tree, and live on the Martin surface with the follow-up regression patch

### 2026-03-30 — Lotus bloom stalk visual softening

- simplified the stalk styling inside the dormant Lotus bloom component:
  - `/home/cerebrhoe/martin-lepage-site/src/components/lotus/LotusBloomJourney.astro`
- visual adjustments:
  - shortened and slimmed the stalk line
  - reduced the spacing between closed nodes
  - made the closed buds smaller, rounder, and lighter
  - softened the node shadow and reduced the center-dot size
  - reduced review/opening/closing stalk stretch so the motion feels less heavy
- verification:
  - `PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH" npm run lotus:check`
  - `PATH="$HOME/.nvm/versions/node/v22.22.2/bin:$PATH" npm run build`
- scope note:
  - this is currently a dormant asset polish, not a live `/lotus/` route change
  - `LotusBloomJourney.astro` is not presently imported by an active public page after the `/lotus/` scorer restoration

### 2026-03-30 — Lotus scorer restoration committed and deployed

- committed the Lotus recovery and browser-test updates on:
  - branch: `wip/reconcile-main-20260327-114047`
  - commit: `6855f82ad49491bcdde078372b62abb9dd60126d`
  - message: `Restore Lotus scorer route and soften bloom stalk`
- pushed to GitHub:
  - `origin/wip/reconcile-main-20260327-114047`
- built and deployed from a clean archive of that exact commit at:
  - `/tmp/martin-lotus-release-6855f82ad49491bcdde078372b62abb9dd60126d`
- deploy result:
  - `https://61325b8a.martin-lepage-site.pages.dev`
- release verification:
  - `PATH=/home/cerebrhoe/.nvm/versions/node/v22.22.2/bin:$PATH npm run lotus:check`
  - `PATH=/home/cerebrhoe/.nvm/versions/node/v22.22.2/bin:$PATH npm run build`
  - `PATH=/home/cerebrhoe/.nvm/versions/node/v22.22.2/bin:$PATH npm run lotus:smoke`
  - `PATH=/home/cerebrhoe/.nvm/versions/node/v22.22.2/bin:$PATH npm run lotus:e2e`
- deploy verification:
  - `https://61325b8a.martin-lepage-site.pages.dev/lotus/` -> `200`
  - `https://61325b8a.martin-lepage-site.pages.dev/lotus/research/` -> `200`
  - `https://martin.govern-ai.ca/lotus/` -> `200`
  - `https://martin.govern-ai.ca/lotus/research/` -> `200`
- test hardening note:
  - the Lotus Playwright spec was narrowed to the restored vector section to avoid false duplicate-text matches on `Results` and the narrative question headings
- scope note:
  - the deployed public change is the restored Lotus scorer/workbench on `/lotus/`
  - the softened stalk remains part of the dormant `LotusBloomJourney.astro` asset and does not currently alter the live `/lotus/` surface

### 2026-03-31 — Lotus app-first corrective release after live regression review

- post-deploy live review confirmed a real regression in the public `/lotus/` presentation:
  - the scorer had been restored, but it was buried under a landing-page hero and explanatory wrapper
  - the route read like marketing copy first and app surface second
- corrected by simplifying the top of:
  - `/home/cerebrhoe/martin-lepage-site/src/pages/lotus/index.astro`
- corrective shape:
  - removed the oversized hero orbit + “Four ways” preamble
  - made the page lead with an app-first heading: `Agency scorer and reflective workbench.`
  - kept the orientation material but compressed it into a small side card
  - kept the workbench and full vector questions on the same route, closer to the top of the page
- verification rerun:
  - `PATH=/home/cerebrhoe/.nvm/versions/node/v22.22.2/bin:$PATH npm run lotus:check`
  - `PATH=/home/cerebrhoe/.nvm/versions/node/v22.22.2/bin:$PATH npm run build`
  - `PATH=/home/cerebrhoe/.nvm/versions/node/v22.22.2/bin:$PATH npm run lotus:smoke`
  - `PATH=/home/cerebrhoe/.nvm/versions/node/v22.22.2/bin:$PATH npm run lotus:e2e`
- committed and pushed:
  - branch: `wip/reconcile-main-20260327-114047`
  - commit: `c47bd465e1a670575649bbca45f0dee9f85b02ce`
  - message: `Make Lotus route app-first again`
- deployed from clean archive:
  - `/tmp/martin-lotus-release-c47bd465e1a670575649bbca45f0dee9f85b02ce`
- deployment:
  - `https://5d282bbb.martin-lepage-site.pages.dev`
- live verification:
  - `https://5d282bbb.martin-lepage-site.pages.dev/lotus/` -> app-first heading present
  - `https://martin.govern-ai.ca/lotus/` -> app-first heading present
  - both preview and custom domain returned `200`
- session-close note:
  - `/lotus/` is now live again as an app-first scorer/workbench route rather than a landing-page wrapper around the app

### 2026-03-31 — Lotus top-section contrast fix

- fixed the remaining visual polish issues in the `/lotus/` top section only:
  - `/home/cerebrhoe/martin-lepage-site/src/pages/lotus/index.astro`
- changes:
  - increased orientation-card copy contrast by switching it from pale near-white to the standard Lotus text tone
  - updated the top primary CTA styling to use dark ink on the existing rose gradient so the button clears AA contrast minimum without introducing a new color family
- required verification:
  - `PATH=/home/cerebrhoe/.nvm/versions/node/v22.22.2/bin:$PATH npm run lotus:check` -> passed
  - `PATH=/home/cerebrhoe/.nvm/versions/node/v22.22.2/bin:$PATH npm run lotus:smoke` -> passed
- committed and pushed:
  - commit: `3dd77e28c0928370f603232d12eab1f4bb6c56bb`
  - message: `Fix top-section contrast: orientation copy and button`
- deployed from clean archive:
  - `/tmp/martin-lotus-release-3dd77e28c0928370f603232d12eab1f4bb6c56bb`
- deployment:
  - `https://44aefe23.martin-lepage-site.pages.dev`
- live verification:
  - `https://44aefe23.martin-lepage-site.pages.dev/lotus/` -> `200`
  - `https://martin.govern-ai.ca/lotus/` -> `200`

### 2026-04-18 — Martin site source-of-truth consolidation and branch-control hardening

- completed the repository consolidation that makes `/home/cerebrhoe/martin-lepage-site` the single source of truth for `https://martin.govern-ai.ca`
- pre-merge comparison was run first from temporary clones only:
  - `/tmp/perso-review`
  - `/tmp/github-io`
  - raw comparison artifacts saved at:
    - `/tmp/only-github-io.txt`
    - `/tmp/only-perso-review.txt`
    - `/tmp/different-content.txt`
    - `/tmp/site-consolidation-report.md`
- merged `.github.io` source into the Martin repo on branch:
  - `merge-github-io-source-of-truth`
- preserved Martin-site identity during the merge:
  - production URL remains `https://martin.govern-ai.ca`
  - local-only app/workbench files stayed in place
  - `.github.io` source/pages/workers content was brought in without generated docs build output
- promoted `main` locally and on GitHub as the canonical branch:
  - created and pushed backup branch `backup/pre-source-of-truth-fix`
  - merged source commit `293d002` into `main`
  - pushed `main` at merge commit `c0c36ee`
  - added a `Source of Truth` section to `/home/cerebrhoe/martin-lepage-site/README.md`
- added local push protection:
  - installed `/home/cerebrhoe/martin-lepage-site/.git/hooks/pre-push`
  - hook blocks non-`main` pushes to `origin` and rejects behind/diverged local `main` states
- local branch cleanup after promotion:
  - deleted fully merged non-backup branches `merge-github-io-source-of-truth` and `wip/reconcile-main-20260327-114047`
  - preserved `main`, `origin/main`, `backup/pre-source-of-truth-fix`, `backup/main-before-reconcile-20260327-114047`, and `stash@{0}`
- verification:
  - `npm install`
  - `NODE_OPTIONS=--max-old-space-size=8192 npm run check`
  - `npm run build`
  - `npm run smoke`
- deploy note:
  - no Cloudflare action was taken during this consolidation pass

### 2026-04-18 — Automated live health-check coverage expanded for martin.govern-ai.ca

- added executable checker:
  - `/home/cerebrhoe/martin-lepage-site/run-health-check.sh`
- the checker now covers:
  - homepage reachability and TLS/header validation
  - core asset integrity
  - representative route coverage
  - same-origin internal link validation
  - mobile rendering checks on key pages
  - the mailto-based contact path
- live rerun result:
  - completed at `2026-04-18T06:42:16Z`
  - status: `HEALTHY`
  - `85` internal links checked
  - `0` broken links
  - `0` console errors
  - `0` failed requests
  - `0` mobile issues
- checker hardening note:
  - this session fixed the checker itself for `103 Early Hints` parsing and Firefox mobile-context compatibility
- independent corroboration:
  - Claude responded to the peer-channel audit request with a bounded public spot-check
  - homepage and `/lotus` both loaded without HTTP/TLS, asset, console, or rendering failures
  - no user-visible regressions or deployment risks were identified in that external pass

### 2026-04-20 — Audit de-tiering cleanup

- consolidated redundant audit-remediation files created during the HEPHAISTOS agent ecosystem audit:
  - `/home/cerebrhoe/martin-lepage-site/` — removed stale audit artifact duplicates
- de-tiered template files that had been incorrectly promoted to active status during governance reframing:
  - `/home/cerebrhoe/martin-lepage-site/src/content/` — 2 templates reset to archived/dormant status
- scope note:
  - these were internal cleanup changes; no public routes or deployed assets were modified
- no deploy performed

### 2026-04-24 — Untracked health-check automation script added

- tracker note (git hygiene):
  - `/home/cerebrhoe/martin-lepage-site/run-health-check.sh` is present but **untracked** in `martin-lepage-site` as of 2026-04-24.
  - status: UNTRACKED/NEW
  - evidence: `git status --porcelain` shows `?? run-health-check.sh`
  - This is not a deploy event; it is a staging/commit decision.
- next:
  - either commit the script as part of health-check automation coverage, or add it to ignore/drafts so the repo does not remain dirty.

## Related

- [[Research and Papers MOC]]
- [[Master Tracker — Snapshot 2026-04-28]]
