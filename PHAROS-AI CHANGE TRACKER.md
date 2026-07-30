---
type: note
title: PHAROS-AI Change Tracker
tags:
- note
status: active
created: '2026-07-08'
updated: '2026-07-08'
vault_area: PHAROS-AI CHANGE TRACKER.md
canonical_path: PHAROS-AI CHANGE TRACKER.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

# PHAROS-AI Change Tracker

## 2026-06-17

- Deployed updated PHAROS homepage hero wordmark and nav logo assets for `pharos-ai.ca`.
- Replaced the hero `PHAROS` text treatment with the gold custom wordmark image and trimmed the asset so the mark aligns evenly.
- Swapped the navigation lockup to the new `PHAROS AI Governance` logo and accepted the corresponding `site.css` size update in `frontend/style-lock.json`.

## 2026-06-17 Deploy

- Committed and pushed the hero/header alignment update.
- Rebuilt the frontend and redeployed the current `main` branch to Cloudflare Pages.
- Kept the tracker gate satisfied so the next deploy can verify this release boundary.

## 2026-06-30 — Middleware deployment fix

- Fixed Cloudflare Pages Functions middleware not being deployed.
- `functions/_middleware.js` (basic auth for `/normalized-results`) was never reaching Cloudflare because `wrangler pages deploy build` only deploys the `build/` directory and CRA does not copy `frontend/functions/` into it.
- Updated `cf:deploy` script to run `cp -r functions build/` before the wrangler deploy, ensuring the middleware ships with every deploy.
- No React source changes — JS bundle remains `main.3537dadf.js`.

## 2026-06-30 — SEO corrections

- Fixed `og:image` and `twitter:image`: switched from SVG to PNG (`pharos-social-card.png`) — Twitter/X cards were broken with SVG.
- Added `og:image:width="1200"` and `og:image:height="630"` to all pages.
- Fixed `hreflang` on all 24 pre-rendered routes: inner pages now point to their own URL and French counterpart (`/fr/{path}`) instead of the root.
- Added `<lastmod>2026-06-30</lastmod>` and `<changefreq>monthly</changefreq>` to all 40 sitemap entries.
- SEO changes live in `public/index.html`, `public/sitemap.xml`, and `scripts/generate-static-route-pages.cjs`.
- Rebuild produces `main.3537dadf.js` — same hash as current production, no JS regression.

## 2026-07-01 — Fixed broken /connect contact form

- Root cause: `Connect.js` (and every other content page — About, Services, FAQ, Library, ServiceMenu, Research, Assurance, Cases, ConceptualMethod, Terms) referenced a design-system class vocabulary (`form-shell`, `input-field`, `input-grid`, `hero-grid`, `hero-panel`, `section-shell`, `section-tight`, `surface`, `surface-muted`, `check-list`, `badge-chip`, `badge-row`, `icon-pill`, `kicker`, `hero-badge`, `body-lead`, `form-status`, `reveal-up`) with zero CSS backing anywhere in `App.css`/`site.css`/`tailwind.generated.css`. Traced via git history to the 2026-05-14 "C-drive migration" commit that imported these page components without their matching stylesheet.
- Added the missing classes to `App.css`/`site.css`, reusing the currently-shipped dark-navy/gold token system (`--color-*`, `--radius-*`, `--shadow-*`) and extending the existing `.card` shared ruleset rather than inventing a new visual language.
- Fixed two secondary bugs found during visual QA: missing `.section-tight` (was leaving a large blank gap between stacked sections) and no `.btn-primary:disabled` styling (submit button gave no visual feedback when disabled).
- Minor copy tightening in `Connect.js` (EN only): "Submit preferred date and time" → "Share preferred date and time"; "No request slots remain" → "No slots remain."
- Verified via local dev server + Playwright screenshots: desktop, mobile, French locale, filled/focus states, error state, disabled/enabled button.
- Added `frontend/PRODUCT.md` (impeccable skill project context: brand register, personality, anti-references).
- `frontend/style-lock.json` password was unrecoverable; hashes were regenerated directly (not via the password-gated `style:lock:update` path) with explicit owner sign-off to unblock this deploy.

## 2026-07-15 — French hero brought to parity with the English redesign

- Updated `frontend/src/pages/Home.js` (`HOME_COPY.fr.hero` + `HeroSection`) so the French homepage hero matches the English promise treatment.
- New headline: "Voir la revue venir de loin" (mirrors EN "See the review come from afar"), with the calligraphic flourish span on "venir de loin".
- Added the FR `wordmark` line and the `pharosHeroWordmark` gold image (`contextImage`/`contextImageAlt`) so the FR block carries the same lockup as EN.
- Rewrote the FR hero body to the "missing answer" framing, and strengthened the third proof point label to "Une chaîne de preuve reconstructible" with a reconstructible-evidence value line.
- Change originated from an Antigravity pair-programming session; verified locally (localhost render) before shipping.
- Build passed style-lock (7 CSS files) and the hero aesthetic contract; no CSS or lock changes were required.
- Deployed as uncommitted working-tree state via direct upload (`wrangler pages deploy build --commit-dirty=true`) from the migrated mtl-03 working copy. Not yet committed or pushed to GitHub `main` (SSH push was unavailable this session); the source change still needs a follow-up commit + push to reconcile the Git-connected Pages project.

## 2026-07-30 — Search indexing and canonical-host corrections

- Added self-canonical static HTML, route-specific French titles and
  descriptions, reciprocal `hreflang`, localized Open Graph metadata, and
  language-aware structured data for the bilingual public routes.
- Removed the soft-404 SPA catch-all. Unknown URLs now return a real HTTP 404
  with noindex, while `/$` permanently redirects to the canonical root.
- Kept the public transparency JSON and Martin-site RSS feed available while
  marking both machine resources non-indexable.
- Normalized the governed-decisions article to its extensionless canonical URL
  across the page, sitemap, and internal link.
- Added and deployed the `pharos-www-redirect` Cloudflare Worker custom domain
  so `www.pharos-ai.ca` permanently redirects to the apex while preserving
  paths and query strings.
- Pinned the Pages deployment to the verified `pharos-suite` owner account
  after Wrangler correctly refused an ambiguous non-interactive account choice.
- Verified 102 frontend tests, 9 edge-runtime tests, 50 generated bilingual
  pages, all 42 sitemap routes, a successful production build, and local
  Cloudflare Pages response semantics before deployment.
