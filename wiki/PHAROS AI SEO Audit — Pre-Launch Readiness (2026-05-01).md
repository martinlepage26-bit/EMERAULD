---
type: wiki
aliases:
  - PHAROS SEO Readiness
  - Pre-Launch Technical Audit
tags: [pharos, seo, technical, audit, deployment, blockers, 2026-05-01]
status: active
created: 2026-05-01T18:15
updated: 2026-05-01T18:15
---

# PHAROS AI SEO Audit — Pre-Launch Readiness (2026-05-01)

> **Cluster connections:** Technical companion to the 2026-05-01 PHAROS commercial launch. Part of the launch artifact set with [[PHAROS AI Commercial Launch — 8-Stream Deploy (2026-05-01)]], [[Agent Orchestration — PHAROS Launch as Governed Multi-Agent Execution]], and [[PHAROS Launch — Fluency, Evidence, and Mid-Funnel Trust (Synthesis)]]. Indexed in [[PHAROS Commercial Strategy]] under launch operations.

## Summary

Static SEO audit of deployed PHAROS AI pages (6 HTML files at `pharos-ai.ca`) identified **3 critical blockers** and **2 secondary issues** requiring remediation before [[PHAROS Procurement-Unblock Sprint|outreach Day 0]]. All are fixable within current session. Operational artifact under [[PHAROS Commercial Strategy]] (pre-launch readiness audit) and the 2026-05-01 launch trace [[PHAROS AI Commercial Launch — 8-Stream Deploy (2026-05-01)]].

## Deployed Pages (6 Total)

| Page | Status | Blockers |
|---|---|---|
| Landing Page (`/ai-act-diagnostic`) | ✓ live | CF token, 93→90 days (×2), hreflang |
| Article: Digital Omnibus Failed | ✓ live | CF token |
| Article: EU AI Act Applies | ✓ live | CF token, 93 days (×1), title oversized |
| Article: High-Risk Explained | ✓ live | CF token |
| Article: Law 25 + EU AI Act Overlap | ✓ live | CF token, 93 days (×2) |
| Commercial Brief | ✓ live | CF token, 93 days (×2) |

## Critical Blockers (Must Fix Before Outreach)

### 1. CF Analytics Token — 6/6 Pages

**Issue:** All 6 pages contain placeholder comment `REPLACE_WITH_CF_TOKEN`.

**Impact:** Zero traffic measurement. Analytics beacon inert.

**Fix:** 
1. Retrieve actual CF Analytics token from CF Dashboard (Analytics & Logs → Web Analytics → `pharos-ai.ca` → copy token)
2. Replace `REPLACE_WITH_CF_TOKEN` in all 6 pages
3. Test: wait 60s, verify page load registers in CF Analytics dashboard
4. Rebuild + redeploy: `pnpm build && wrangler deploy`

**Effort:** 5 min setup + 2 min rebuild/deploy

**Status:** ❌ BLOCKER — Analytics is operational dependency for outreach tracking

---

### 2. Messaging Currency: "93 days" → "90 days" — 5/6 Pages

**Issue:** Messaging shift decided (2026-05-01) but not yet applied. 5 pages still reference "93 days."

**Locations:**
- Landing page: 2 instances (hero section, meta description)
- Brief: 2 instances (header, regulatory section)
- Article "Law 25 + EU AI Act": 2 instances
- Article "EU AI Act Applies": 1 instance

**Impact:** Outreach copy will reference inconsistent timelines (90 days in cold email, 93 days on landing page = credibility erosion).

**Fix:**
```bash
# Landing page
sed -i 's/93 days/90 days/g' /home/cerebrhoe/PHAROS-SUITE/PHAROS-NEWLOOK/client/public/ai-act-diagnostic/index.html

# Brief
sed -i 's/93 days/90 days/g; s/93-day/90-day/g' /home/cerebrhoe/PHAROS-SUITE/PHAROS-NEWLOOK/client/public/pharos-ai-commercial-brief.html

# Articles
sed -i 's/93 days/90 days/g; s/93-day/90-day/g' /home/cerebrhoe/PHAROS-SUITE/PHAROS-NEWLOOK/client/public/articles/*/index.html
```

**Verify:** `grep -r "93 days" /home/cerebrhoe/PHAROS-SUITE/PHAROS-NEWLOOK/client/public/` should return 0 results

**Effort:** 2 min sed replacement + 2 min rebuild/deploy

**Status:** ❌ BLOCKER — messaging coherence is critical for outreach credibility

---

### 3. hreflang to Nonexistent French Page

**Issue:** Landing page contains `<link rel="alternate" hreflang="fr">` pointing to `/fr/ai-act-diagnostic`, which does not exist. Crawlers receive 404.

**Impact:** SEO noise, potential indexing confusion, broken language alternate signal.

**Fix:** Remove hreflang tag until HENRY completes French page draft.

```bash
# Landing page only (keep hreflang on other pages if needed)
sed -i '/<link rel="alternate" hreflang="fr"/d' /home/cerebrhoe/PHAROS-SUITE/PHAROS-NEWLOOK/client/public/ai-act-diagnostic/index.html
```

**Restore:** After French page deployed, restore with:
```html
<link rel="alternate" hreflang="fr" href="https://pharos-ai.ca/fr/ai-act-diagnostic">
```

**Effort:** 1 min edit + 2 min rebuild/deploy

**Status:** ❌ BLOCKER — prevents outreach until fixed (Argus flagged this in initial audit)

---

## Secondary Issues (Fix Before Design Review Completion)

### 4. Article Title Length Oversized

**Issue:** `articles/digital-omnibus-failed/index.html` title is 83 characters (optimal: 50–60, max: 60 for desktop SERPs).

**Current:** "The Digital Omnibus Failed. What That Means for Your August 2 Deadline. | PHAROS AI"

**Optimal:** "Digital Omnibus Failed: What It Means for Your Aug 2 Deadline"

**Impact:** Title truncation in SERPs, loss of brand visibility.

**Fix:** Shorten to ~55 chars. Recommendation:

```html
<title>Digital Omnibus Failed: Your August 2 Deadline Stands | PHAROS AI</title>
```

**Effort:** 2 min edit

---

### 5. Article Description Length Oversized

**Issue:** Same article has 200-char description (optimal: 150–160, max: 160 for display).

**Current:** "The Digital Omnibus proposal would have delayed high-risk AI Act compliance to December 2027. The trilogue failed on April 28, 2026. Your August 2 deadline stands. Here's what that means for Canadian companies with EU exposure."

**Optimal:** Condense to ~155 chars.

**Fix:**
```html
<meta name="description" content="The Digital Omnibus delay failed April 28. Your August 2 deadline is real. 90 days for compliance. What this means for Canadian AI vendors.">
```

**Effort:** 2 min edit

---

## Missing Opportunities (Post-Launch Optimization)

### Schema.org Structured Data

**Status:** None deployed.

**Impact:** Lost opportunity for rich snippets, FAQ snippets, author/byline attribution.

**Recommendation:** Add after outreach starts (post-priority work). Suggested:
- **Landing page:** Organization schema + LocalBusiness
- **Articles:** Article schema (author, datePublished, dateModified) + FAQPage schema on FAQ section
- **Brief:** BreadcrumbList schema

---

## SEO Readiness Summary

| Category | Status | Notes |
|---|---|---|
| **Core Meta Tags** | ⚠️ Partial | Titles/descriptions mostly good; 1 oversized title/desc |
| **Canonical URLs** | ✓ Pass | All pages have rel=canonical |
| **Mobile Responsive** | ✓ Pass | Viewport meta tag present |
| **Character Encoding** | ✓ Pass | UTF-8 declared |
| **Analytics** | ❌ Fail | Placeholder token (blocker) |
| **Messaging Coherence** | ❌ Fail | 93→90 day update incomplete (blocker) |
| **Internationalization** | ❌ Fail | hreflang to 404 (blocker) |
| **Structured Data** | ❌ Fail | None deployed (optimization gap) |
| **Internal Linking** | ✓ Pass | Clean link structure, no broken links detected |

---

## Fix Priority and Timeline

### Priority 1 — MUST FIX BEFORE OUTREACH DAY 0 (Blockers)

**Time budget:** ~15 min setup + rebuild/deploy

1. **CF Analytics token** (5 min)
   - Retrieve from CF Dashboard
   - Replace in all 6 pages
   - Rebuild + deploy
   - Test: wait 60s for first event

2. **93→90 days messaging** (5 min)
   - Sed replace across landing page + brief + articles
   - Rebuild + deploy
   - Verify: `grep "93 days"` returns 0

3. **hreflang removal** (3 min)
   - Remove `<link rel="alternate" hreflang="fr">` from landing page
   - Rebuild + deploy

4. **Rebuild and deploy** (2 min)
   - `pnpm build`
   - `wrangler deploy`
   - Verify: Check `pharos-ai.ca` pages load (test from outside WSL if possible)

---

### Priority 2 — SHOULD FIX BEFORE CODEX DESIGN REVIEW RETURN

**Time budget:** ~5 min

1. Article title/description length (digital-omnibus-failed)
   - Shorten title to 55 chars
   - Shorten description to 155 chars
   - Rebuild + deploy

---

### Priority 3 — POST-LAUNCH OPTIMIZATION

1. Add Schema.org structured data (FAQ, Article, Organization)
2. Monitor analytics for traffic patterns
3. A/B test CTA wording in landing page hero

---

## Related

- [[Governance and PHAROS MOC]]
- [[PHAROS AI Commercial Launch — 8-Stream Deploy (2026-05-01)]] — Technical deployment spec
- [[Codex Handoff — PHAROS AI Design Review (2026-05-01)]] — Design review in progress
- [[PHAROS Procurement-Unblock Sprint]] — Outreach execution
- [[Regulatory Arbitrage — EU AI Act + Law 25 + 93-Day Window (Synthesis)]] — 90-day messaging context
