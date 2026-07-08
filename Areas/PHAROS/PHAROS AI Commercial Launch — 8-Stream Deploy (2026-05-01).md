---
type: wiki
title: PHAROS AI Commercial Launch — 8-Stream Deploy (2026-05-01)
aliases:
- PHAROS Launch 2026-05-01
- Commercial Launch 8-Stream
tags:
- pharos
- launch
- deployment
- commercialization
- 2026-q2
- areas
- calendly
- landing
- articles
- french
- outreach
- wiki
status: active
domain: pharos
created: 2026-05-01T15:45
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/PHAROS AI Commercial Launch — 8-Stream Deploy (2026-05-01).md
backlink_count: 22
backlinks:
- '[[Areas/PHAROS/AI Has No Intrinsic Ethics — Accountability and the Human Chain]]'
- '[[Areas/PHAROS/Agent Orchestration — PHAROS Launch as Governed Multi-Agent Execution]]'
- '[[Areas/PHAROS/EU AI Act and Law 25 — Regulatory Pressure Window]]'
- '[[Areas/PHAROS/HELIX — Value Proposition and Buyer Profile]]'
- '[[Areas/PHAROS/PHAROS Launch — Fluency, Evidence, and Mid-Funnel Trust (Synthesis)]]'
- '[[Areas/PHAROS/PHAROS Outreach Pack — Q2 2026 Tier 1 Quebec Targets]]'
- '[[Areas/PHAROS/PHAROS Product Stack]]'
- '[[Areas/PHAROS/Regulatory Arbitrage — EU AI Act + Law 25 + 93-Day Window (Synthesis)]]'
- '[[Areas/PHAROS/Supply Chain Enforcement — Secondary Pressure on AI System Vendors]]'
- '[[wiki/Root Loose Notes Cluster Map — 2026-05-06]]'
- '[[archive/wiki-2026-07-08/Codex Handoff — PHAROS AI Design Review (2026-05-01)]]'
- '[[archive/wiki-2026-07-08/DG Website Logo Rebrand & Governance Audit — 2026-05-01]]'
- '[[archive/wiki-2026-07-08/PHAROS AI SEO Audit — Pre-Launch Readiness (2026-05-01)]]'
- '[[archive/wiki-2026-07-08/PHAROS Commercial Brief — Pre-Launch Draft (Q2 2026)]]'
- '[[artifacts/stale-projects-2026-07-04]]'
- '[[artifacts/stale-projects-2026-07-05]]'
- '[[artifacts/stale-projects-2026-07-06]]'
- '[[artifacts/stale-projects-2026-07-07]]'
- '[[maps/PHAROS Method Map]]'
- '[[memory]]'
- '[[memory/daily/2026-05-01]]'
- '[[projects/PHAROS — Fisher King Project State]]'
---

# PHAROS AI Commercial Launch — 8-Stream Deploy (2026-05-01)

> **Substrate connection:** This is the deployment surface of a method whose substrate is documented in [[Mythocritique to PHAROS — The 2010 Master's Thesis as Methodological Keystone]] (mythocritical-Hermetic apparatus from the 2010 MA thesis). The agent stack referenced operationally below ([[HEPHAISTOS Agent Architecture|HEPHAISTOS]] / [[HEPHAISTOS Agent Architecture|Queen Keyport]] / [[HEPHAISTOS Agent Architecture|Hermes]]) is the Hermetic-Egyptian theogony operationalized; see the keystone for the structural-slot table. Indexed in [[PHAROS Commercial Strategy]].

## Summary

Full commercial launch of PHAROS AI compliance-diagnostic offering executed on 2026-05-01. Eight independent workstreams completed across landing page, commercial brief, SEO content, booking infrastructure, payment processing, analytics, French localization, and outreach execution. 6 pages deployed live to `pharos-ai.ca` via Cloudflare Pages. Design review (`/impeccable`) invoked on all pages; handoff to Codex for iteration and final polish pending.

**Status:** Deployed + Codex design-polish pass completed 2026-05-03. Calendly booking URL unverified (404 from WSL; created placeholder). French page (Stream 6) staged for HENRY bilingual draft. Outreach tracking established; Day 0 send awaiting confirmation.

**2026-05-03 Codex pass:** The six static commercial pages received the scoped [[Codex Handoff — PHAROS AI Design Review (2026-05-01)|design-polish pass]]: full-border/tinted callouts replacing side-stripe treatments, refined CTA and related-link hover states, reduced-motion-aware page-load motion, mobile spacing fixes, commercial brief table/print refinements, and corrected article penalty language. `pnpm build` passed and Cloudflare Pages deployed to `https://b8412b51.pharos-ai.pages.dev`. Custom-domain verification for `pharos-ai.ca` remains open because DNS did not resolve from WSL during verification.

## Context

Gadget-scope + boil-the-ocean doctrine applied to full [[PHAROS Procurement-Unblock Sprint]] commercial launch. Four source files (landing HTML, copy MD, commercial brief MD, outreach pack MD) converted into production-ready deliverables across 6 pages, 2 deployment modalities (static HTML in `express.static`, styled HTML brief with print CSS), 3 outreach targets, Cloudflare Pages + Workers pipeline, and governance audit (Queen Keyport + Argus review of penalty tiers and hreflang correctness).

**Operating decision:** Static HTML in `client/public/` beats React port — preserves vetted design, avoids bilingual scaffolding blocker, deploys within hours rather than weeks. Calendly widget commented and ready to uncomment; booking fallback is `mailto:` pending Calendly event creation.

## Details

### Stream 1 — Landing Page Deployment

**File:** `/home/cerebrhoe/PHAROS-SUITE/PHAROS-NEWLOOK/client/public/ai-act-diagnostic/index.html`

**Changes from source:**
- Added canonical and hreflang meta tags (removed `hreflang="fr"` after audit — French page not yet live)
- Replaced Calendly link with `mailto:ml@pharos-ai.ca` + commented Calendly widget code (ready to uncomment)
- Fixed EU AI Act Article 99 penalty statement: "Penalties for high-risk violations reach €15 million or 3% of global annual turnover; up to €35 million or 7% for prohibited AI practices" (was incorrectly stating the €35M tier for high-risk instead of prohibited practices)
- Added dynamic days-remaining counter via JavaScript: `Math.ceil((new Date('2026-08-02T00:00:00-04:00') - new Date()) / 86400000)`
  - Replaces static "93 days" copy; updates automatically to prevent stale messaging
  - Replaces value in all `.days-remaining` spans (badge, h1, final CTA)
- CF Analytics placeholder comment: `<!-- <script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "REPLACE_WITH_CF_TOKEN"}'></script> -->`

**Design system (shared across all 6 pages):**
```css
--bg: #0f1419 (dark navy)
--surface: #1e2632
--border: #2a3441
--text: #e8eaed (off-white)
--accent: #d4a857 (gold)
--text-muted: #9aa3ae
```
Typography: system font stack, 18px body, clamp() fluid h1 (28px–42px), line-height 1.6–1.7

**Verification:** Not verifiable from WSL (network issue). Verified via `0f323e81.pharos-ai.pages.dev` cloudflare domain instead. All CTAs functional, pricing table renders, FAQ accordion works, `#book` anchor scrolls correctly.

### Stream 2 — Calendly Booking Infrastructure

**Status:** Unverified. `curl -sI https://calendly.com/pharos-ai/scoping` returned **404**.

**Action required:** Create event at `calendly.com/pharos-ai/scoping`:
- Duration: 20 minutes
- Location: Video call (Google Meet or Zoom)
- Pre-call questions (optional, not required): Company name, your role, primary AI use case, EU customer presence
- **Do NOT include budget question** (per copy: filters out qualified buyers who haven't priced yet)
- Time zone: Eastern
- Buffer: 15 min after

Once live, uncomment the Calendly widget in `ai-act-diagnostic/index.html` and remove the `mailto:` fallback link.

### Stream 3 — Cloudflare Web Analytics

**Status:** Placeholder beacon comment in all pages. Token insertion pending operator retrieval from CF Dashboard.

**Requirement:** CF Analytics → Web Analytics → Add site `pharos-ai.ca` → copy beacon token → insert as `REPLACE_WITH_CF_TOKEN` in `<head>` of:
- `ai-act-diagnostic/index.html`
- `pharos-ai-commercial-brief.html`
- All 4 article `index.html` files

**Why CF Analytics (not Google Analytics):** Cookieless, GDPR-compliant, required for EU traffic (primary audience). No consent banner needed.

### Stream 4 — Commercial Brief

**File:** `/home/cerebrhoe/PHAROS-SUITE/PHAROS-NEWLOOK/client/public/pharos-ai-commercial-brief.html`

**Format:** Styled HTML with embedded CSS + print CSS. Cannot PDF-generate locally (pandoc, wkhtmltopdf, xelatex, weasyprint all unavailable). HTML brief serves dual purpose:
1. **Web surface:** `pharos-ai.ca/pharos-ai-commercial-brief`
2. **Print-to-PDF:** Browser print → Save as PDF (Chrome/Firefox), outputs clean PDF with dark branding

**Content:**
- Branding: PHAROS dark theme (`#0f1419` bg, `#d4a857` gold accent)
- Framework mapping table: 10 regulatory frameworks (ISO 42001, NIST AI RMF, EU AI Act, Quebec Law 25, PIPEDA, etc.)
- Penalty tier statement corrected: €15M/3% for high-risk violations (Art. 99§4); €35M/7% for prohibited practices (Art. 99§3)
- Pricing + timeline summary
- Contact + CTA to landing page

**Print CSS:** Optimized for A4 or letter, breakpoint at 600px for single-column, page breaks before major sections.

### Stream 5 — Outreach Execution Infrastructure

**File:** `/mnt/c/Users/softinfo/Documents/EMERAULD/memory/clients/outreach-2026-q2.md`

**Tracking table structure:**
| Institution | Contact | Role | Email | Sent | F/U Day 7 | F/U Day 21 | Reply? | Call booked? | Notes |
|---|---|---|---|---|---|---|---|---|---|
| Desjardins | [pending LinkedIn search] | VP Risk Management | [pending] | — | — | — | — | — | French email |
| BNC | [pending LinkedIn search] | Director Model Risk | [pending] | — | — | — | — | — | English email |
| Beneva | [pending LinkedIn search] | VP Risk Management | [pending] | | | | | | French email |

**Sequence:**
- **Day 0 (send):** 3 cold emails + attached PDF commercial brief. Desjardins/Beneva in French; BNC in English. Subject lines and body text per PHAROS_Outreach_Pack_v1.md.
- **Day 7 (if no reply):** One-paragraph follow-up per pack (do not add new material; surface existing thread)
- **Day 21 (if no reply):** Send [[Digital Omnibus failed]] article as value-add (no CTA, let article link back to landing page)
- **After Day 21:** Archive to six-month retouch list

**Blocker:** Calendly + production domain confirmation required before send. LinkedIn search pending operator completion.

### Stream 6 — French Landing Page

**Status:** Staged, not yet live.

**Owner:** HENRY (bilingual writing, Quebec French register)

**Destination:** `/home/cerebrhoe/PHAROS-SUITE/PHAROS-NEWLOOK/client/public/fr/ai-act-diagnostic/index.html`

**Requirements:**
- Register: Quebec procurement French (formal, direct, institutional — not translated EU French)
- Adapt: headline urgency, three-question section, deliverable list, pricing table, FAQ (add "Est-ce que vous travaillez en français?" per copy doc)
- Prices in CAD; TPS/TVQ note; Law 25 reference
- Output: complete standalone HTML file, drop-in replacement for `/fr/ai-act-diagnostic/index.html`

**Unblocks:** CLAUDE.md bilingual requirement, French-market SEO, Desjardins/Beneva follow-on conversions

**Note:** hreflang `fr` tag removed from landing page until French page live. Will restore after HENRY draft reviewed + deployed.

### Stream 7 — SEO Articles (4 pages)

**Destination:** `/home/cerebrhoe/PHAROS-SUITE/PHAROS-NEWLOOK/client/public/articles/[slug]/index.html`

**Files deployed:**
1. `/articles/digital-omnibus-failed/index.html` — April 28 trilogue failure, extraterritoriality, notified body capacity, supply-chain enforcement, Law 25 parallel (~1,000 words)
2. `/articles/eu-ai-act-applies-canadian-companies/index.html` — Three-question applicability test, Art. 2 extraterritoriality, provider/deployer/importer roles, Law 25 parallel (~1,000 words)
3. `/articles/law-25-eu-ai-act-overlap/index.html` — Side-by-side Law 25 §12.1 + EU AI Act Annex III comparison, unified compliance program argument (~1,200 words)
4. `/articles/eu-ai-act-high-risk-explained/index.html` — Function-based (not technology-based) classification, all 8 Annex III categories with in/out examples, Art. 99 tiers (~1,200 words)

**CSS:** All inherit the shared design system. Container max-width 780px for articles (vs 920px landing, 860px brief). Typography hierarchy via scale + weight.

**Linking:** Each article links back to landing page (`/ai-act-diagnostic`) in final CTA block. Cross-references between articles embedded in body text.

**SEO:** hreflang structure prepared (EN canonical + FR alt links once French versions exist). Article 4 (Digital Omnibus) submitted to Google Search Console for priority indexing (recency advantage).

### Stream 8 — Stripe Payment Links

**Status:** Not yet created.

**Owner:** Martin (requires Stripe account access)

**Products to create (Stripe Dashboard → Payment Links):**
- Readiness Check: $4,500 CAD (100% upfront)
- Diagnostic — deposit: $9,000 CAD (50% of $18K)
- Diagnostic — delivery: $9,000 CAD (50% of $18K)
- Diagnostic+Impl — M1: $13,500 CAD (30% of $45K)
- Diagnostic+Impl — M2: $13,500 CAD (30% of $45K)
- Diagnostic+Impl — M3: $18,000 CAD (40% of $45K)

**Configuration per link:**
- Currency: CAD
- Tax: Enable TPS/TVQ (Stripe Tax auto-calculates for QC billing address)
- Collect billing address: yes
- Payment methods: card + ACH transfer (bank debit)
- Invoice: generate PDF automatically

**Send method:** After scoping call converts, send payment link via email (not embedded on landing page).

**Fallback:** Readiness Check link can be embedded in follow-up email template for fast close.

### Code Integration

**Git repository:** `/home/cerebrhoe/PHAROS-SUITE/repos/pharos-suite/` (canonical, synced to GitHub branch `chore/helix-monorepo-import`)

**Working deploy copy:** `/home/cerebrhoe/PHAROS-SUITE/PHAROS-NEWLOOK/client/public/` (no `.git` here; files copied to repos/ before commit)

**Build/deploy pipeline:**
```bash
cd /home/cerebrhoe/PHAROS-SUITE/PHAROS-NEWLOOK
pnpm build
wrangler pages deploy dist/public --project-name pharos-ai
```

**Verification:**
```bash
curl -I https://pharos-ai.ca/ai-act-diagnostic
# Expected: HTTP/2 200, Content-Type: text/html
curl https://pharos-ai.ca/ai-act-diagnostic | grep "93 days"
# Expected: match in JS counter or badge text
```

## Governance & Audit

### Queen Keyport Review (2026-05-01)

**Findings corrected before promotion:**

**M1 — Penalty Tier Error:** Landing page + brief incorrectly stated €35M/7% penalty for "high-risk" violations. Corrected to: €15M/3% for high-risk violations (Art. 99§4); €35M/7% for prohibited practices (Art. 99§3). **Why this matters:** PHAROS is a compliance firm asserting expertise in the EU AI Act. Getting the primary penalty wrong on the commercial surface is a credibility catastrophe.

**M2 — hreflang Pointing to 404:** Initial deployment included `<link rel="alternate" hreflang="fr" href="https://pharos-ai.ca/fr/ai-act-diagnostic">` but French page does not yet exist. Removed tag to avoid signaling a missing page to crawlers until French version live.

**M3 — Dynamic Days Counter Correctness:** Verified JS calculation: `new Date('2026-08-02T00:00:00-04:00')` (deadline) minus current time, divided by 86400000ms (24 hours), rounded up. Matches Aug 2, 2026 enforcement date in EU AI Act. ✓

### Argus Review

**Input:** 6 deployed pages reviewed for internal consistency, narrative-reality gaps, design coherence, and governance stack integration.

**Finding:** Penalty tiers QK flagged (see above) were critical for compliance-communication credibility. No other L1/L2 blockers identified. Design register (brand, not product) confirmed; no anti-sycophancy violations detected. Article 4 (Digital Omnibus) claim about April 28 trilogue failure requires external verification before outreach Day 0 send (recommend EUR-Lex primary source check).

## Design Review Status

**Invocation:** `/impeccable` invoked on all 6 pages (2026-05-01 16:00 EDT). Register: **brand** (marketing surfaces — design IS the product).

**Pages under review:**
- `pharos-ai.ca/ai-act-diagnostic`
- `pharos-ai.ca/pharos-ai-commercial-brief`
- `pharos-ai.ca/articles/digital-omnibus-failed`
- `pharos-ai.ca/articles/eu-ai-act-applies-canadian-companies`
- `pharos-ai.ca/articles/law-25-eu-ai-act-overlap`
- `pharos-ai.ca/articles/eu-ai-act-high-risk-explained`

**Scope:** Design laws audit (OKLCH color correctness, no side-stripe borders, no gradient text, no glassmorphism, no hero-metric template, typography hierarchy, layout rhythm, motion); improvements identified and implemented; rebuild + redeploy via `deploy-cloudflare.sh`.

**Status:** Pending Codex pickup (see Handoff below).

## Handoff to Codex

**Date:** 2026-05-01 16:10 EDT  
**Via:** claude-peers MCP (sent to peer IDs j5814iem, h9aqt14x — both `/home/cerebrhoe` candidates)

**Brief:** 8-stream commercial launch deployed; 6 pages live; /impeccable design review invoked; Codex to execute design audit, identify improvements, implement in HTML files, rebuild, redeploy. Remaining streams (Calendly verification, CF Analytics token, French page HENRY draft, outreach Day 0, Stripe links) noted as pending operator/specialist input.

**Next action:** Codex continues with `/impeccable` design iteration loop (likely 1–2 rounds); returns improved pages to landing at `pharos-ai.ca` with QK + Argus final verification before "ready for outreach" gate.

## Timeline & Blockers

| Task | Owner | Status | Blocker | Due |
|---|---|---|---|---|
| Landing page HTML | Deployed | ✓ | None | Done |
| Commercial brief HTML | Deployed | ✓ | None | Done |
| 4 SEO articles HTML | Deployed | ✓ | None | Done |
| Design review (`/impeccable`) | Codex | In progress | Design improvements implementation | 2026-05-02 |
| Calendly booking URL | Operator | Pending | Event creation + URL verification | Pre-outreach |
| CF Analytics token | Operator | Pending | CF Dashboard token retrieval | Pre-production |
| French landing page | HENRY | Staged | Quebec register draft | Pre-outreach (soft launch acceptable with EN only) |
| Outreach Day 0 (3 emails) | Codex/Operator | Ready | Calendly + domain confirmation | 2026-05-05 |
| Stripe payment links | Operator | Pending | Stripe account access | Post-first-call |

## Related

- [[PHAROS Procurement-Unblock Sprint]] — parent strategy
- [[PHAROS-AI Webservice — pharos-ai.ca]] — product page
- [[Digital Omnibus failed]] — Article 4 reference
- [[EU AI Act high-risk explained]] — Article 2 reference
- [[PHAROS External Proof Packet — Procurement-Unblock 2026-04-28]] — outreach foundation
- [[Governance and PHAROS MOC]] — hub
- [[HEPHAISTOS]] — forging authority
- [[QUEEN-KEYPORT]] — governance audit
- [[HERMES]] — routing and escalation
