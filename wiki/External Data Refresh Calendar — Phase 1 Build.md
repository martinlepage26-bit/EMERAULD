---
type: governance-procedures
title: External Data Refresh Calendar (Phase 1 Build)
aliases:
- External Data Refresh Calendar — Phase 1 Build
- wiki/External Data Refresh Calendar — Phase 1 Build
tags:
- governance-procedures
- wiki
- external-data-refresh-calendar-phase-1-build-md
- quarterly
- manual
- annual
- check
- weekly
- color-purple
status: active
created: '2026-04-27'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/External Data Refresh Calendar — Phase 1 Build.md
backlink_count: 5
backlinks:
- '[[wiki/CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)]]'
- '[[wiki/External Data Registry — Phase 1 Build]]'
- '[[wiki/Governance and PHAROS MOC]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[session-state]]'
phase: Phase 1 Infrastructure
---

# External Data Refresh Calendar (Phase 1 Build)

**Purpose:** Central scheduling for verifying all external policy/data sources. Prevents stale data from affecting governance decisions. Integrated with [[CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)|Control 2 External Data Lifecycle]].

**Status:** Calendar built 2026-04-27. All 25 sources have scheduled refresh dates.

---

## Quick Reference — Next 90 Days

### URGENT (Check This Week — 2026-04-27 to 05-03)

| Source | Last Checked | Next Check | Frequency | Owner |
|---|---|---|---|---|
| **Law 25 (Quebec AI Act)** | 2026-04-27 | 2026-05-03 | Weekly (first cycle) | Manual |
| **Reddit Data API** | 2026-04-26 | 2026-04-27 | Weekly | Automation (Phase 2) |
| **OpenRouter API** | 2026-04-27 | 2026-05-27 | Monthly | Automation (Phase 2) |

### May 2026 — Full Refresh Schedule

| Date | Day | Sources to Check | Owner | Status |
|---|---|---|---|---|
| **2026-04-27 (Today)** | Sun | Reddit API (next: daily until stable) | Manual | Starting |
| **2026-05-03** | Sat | Law 25, GDPR Article 5, CCPA | Manual | Quarterly baseline |
| **2026-05-10** | Sat | Cloudflare, Google Drive, GitHub, Notion | Manual | First verify |
| **2026-05-17** | Sat | OpenRouter (monthly check) | Manual | Monthly cycle |
| **2026-05-24** | Sat | Cloudflare, Google Drive, GitHub, Notion | Manual | Re-verify |
| **2026-05-27** | Tue | OpenRouter API | Manual | Monthly refresh |
| **2026-05-31** | Sat | FINRA Rule 4530, Anthropic Claude API | Manual | Quarterly |

### June 2026

| Date | Day | Sources to Check | Owner |
|---|---|---|---|
| **2026-06-15** | Sun | FINRA Rule 4530, Anthropic API (verify) | Manual |
| **2026-06-27** | Fri | Google Drive, GitHub, Cloudflare, Notion | Manual |

### July 2026

| Date | Day | Sources to Check | Owner |
|---|---|---|---|
| **2026-07-20** | Mon | GDPR Articles 5 & 32, HIPAA, ISO 15489, ISO 27001, NIST | Manual |
| **2026-07-27** | Mon | Anthropic Claude API | Manual |

---

## Full Registry with Refresh Dates

### Never (Foundational — Annual Spot-Check Only)

| Source | Next Check | Notes |
|---|---|---|
| GDPR Article 5 — Principles | 2026-07-20 | Foundational; no changes expected |
| GDPR Article 32 — Security | 2026-07-20 | Foundational; no changes expected |
| OAuth 2.0 / OpenID Connect | 2026-12-27 | Annual check for OAuth 2.1 adoption |
| TLS 1.3 | 2027-12-27 | Annual check; very stable |

### Annually (Slow-Moving Standards & Regulations)

| Source | Next Check | Frequency |
|---|---|---|
| HIPAA 45 CFR § 164.316 | 2026-08-20 | Annual |
| HIPAA 45 CFR § 164.308 | 2026-08-20 | Annual |
| ISO 15489 | 2026-10-20 | Annual (next revision ~2025) |
| COBIT 5 | 2026-10-20 | Annual (verify if 2019 is current) |
| SOX § 302 | 2026-12-27 | Annual |
| ISO 9001:2015 | 2026-12-27 | Annual (next revision ~2025) |

### Quarterly (Fast-Moving Policies & Standards)

| Source | Next Check | Frequency | Notes |
|---|---|---|---|
| GDPR (combined audit) | 2026-07-20 | Quarterly | Both Articles 5 & 32 together |
| CCPA | 2026-07-20 | Quarterly | Expanded 2023 (CPRA); monitor amendments |
| FINRA Rule 4530 | 2026-05-31, 2026-08-20, 2026-11-20 | Quarterly | High update frequency |
| NIST SP 800-53 | 2026-07-20 | Quarterly | Stable but government updates |
| ITIL v4 | 2026-12-20 | Annual reference | Minimal change frequency |
| SOC 2 Type II | 2026-10-20 | Quarterly | Stable standard |
| Cloudflare Workers API | 2026-06-27, 2026-09-27 | Quarterly | Monthly changes, quarterly formal reviews |
| Google Drive API | 2026-06-27, 2026-09-27 | Quarterly | Google updates quarterly |
| GitHub API | 2026-06-27, 2026-09-27 | Quarterly | Permissions model updates |
| Notion API | 2026-06-27, 2026-09-27 | Quarterly | Notion releases quarterly |

### Monthly (Volatile APIs & Vendor Terms)

| Source | Next Check | Frequency | Notes |
|---|---|---|---|
| OpenRouter API | 2026-05-27, 2026-06-27, 2026-07-27 | Monthly | New models added; rate limits change |
| Anthropic Claude API | 2026-07-27 | Quarterly (initially); upgrade to monthly if model changes | Quarterly model releases; watch for Claude v4.7 release |

### Weekly (Highly Volatile — Initially Daily Due to Baseline)

| Source | Next Check | Frequency | Notes |
|---|---|---|---|
| Reddit Data API | Daily until stable, then weekly | Weekly (after baseline) | API documentation changes weekly; rate limits volatile |
| **Law 25 (Quebec AI Act)** | **2026-05-03** | **Weekly first cycle, then quarterly** | **HIGHEST PRIORITY. Implementation phased; regulatory updates frequent.** Check Quebec National Assembly for amendments. |

---

## Automated vs. Manual Checks

### Phase 1 (Now): Manual Checks Only
- All sources checked by human operator (Trismégiste)
- Calendar above shows manual check schedule
- Estimated time: 30 min per week

### Phase 2 (2026-05-10 onward): Automated Checks
- Hash verification: Fetch live source, compute hash, compare to snapshot
- Automated weekly for volatile (Reddit, OpenRouter), quarterly for stable (GDPR, NIST)
- Slack/email alerts when policy changes detected
- Reduces manual overhead to ~15 min per week

---

## What to Check (Procedure)

### For Each Source on Scheduled Date:

1. **Fetch live authoritative source** (use source URL)
2. **Compute hash** of live content (SHA-256)
3. **Compare to registry hash** (stored in External Data Registry)
4. **If hashes match:** Policy unchanged; update "Last Verified" date in registry
5. **If hashes differ:** Policy changed!
   - [ ] Document what changed (2-3 bullet points)
   - [ ] Update registry with new hash and clipping date
   - [ ] Flag to governance team: "Policy X changed; decision Y may need re-assessment"
   - [ ] Quarantine old version in registry (mark `status: stale_outdated`)
   - [ ] Ingest new version (create new registry entry)

### Tools Needed (Phase 1):
- Web browser (fetch policy text)
- `sha256sum` or online hash tool (compute hash)
- Markdown editor (update registry)
- Email/Slack (notify governance team of changes)

### Tools Available (Phase 2):
- Python script: automated hash verification
- GitHub Actions / Zapier: automatic weekly checks
- Slack bot: notifications
- Dashboard: real-time control status

---

## Calendar View by Responsibility

### Governance Operator (Martin / Trismégiste)

**Weekly Cadence (30 min):**
- Monday: Reddit API (check for changes, rate limit updates)
- Friday: OpenRouter API (monthly cycle, first Friday of month)

**Monthly Cadence (15 min):**
- First Monday: FINRA Rule 4530, Law 25 (Quebec AI Act)

**Quarterly Cadence (45 min):**
- Calendar weeks: 2, 6, 10, 14 of each quarter
- Check: GDPR, CCPA, HIPAA, FINRA, NIST, ISO, Cloudflare, Google Drive, GitHub, Notion, Anthropic, SOC 2

**Annual Cadence (15 min):**
- June: OAuth 2.0, TLS 1.3, SOX, ISO 9001, COBIT, ITIL

---

## Integration with Governance Workflow

**Before any governance decision:**
1. Check if today's date coincides with a scheduled refresh (calendar above)
2. If yes, perform refresh check before approving decision
3. If policy changed, governance decision may need re-assessment

**After any external policy change:**
1. Governance team is alerted (automated in Phase 2, manual in Phase 1)
2. Recently approved decisions are flagged for re-assessment
3. Impact analysis: Does the change affect governance outcomes?

**Quarterly governance review:**
1. Review External Data Registry
2. Verify all refreshes happened on schedule
3. Identify any missed checks or stale data
4. Update refresh calendar if change frequencies need adjustment

---

## Phase 1 to Phase 2 Transition

**Target: 2026-05-10**

When Phase 2 automation launches:
1. All 25 sources have been checked at least once
2. Refresh schedule validated (are frequencies correct?)
3. Automated scripts ready to take over
4. Manual operator overhead drops from 30 min/week to ~5 min/week (exception handling only)

---

## Monitoring Metrics

**Track each week:**
- [ ] Scheduled refreshes completed on time (yes/no)
- [ ] Policy changes detected (count)
- [ ] Days to governance impact after policy change (goal: < 1 day)
- [ ] False positives in hash verification (should be zero)

**Track each quarter:**
- [ ] % of external data sources current (goal: 100%)
- [ ] Average policy freshness (days old) (goal: < 30 days)
- [ ] Governance decisions impacted by stale data (goal: zero)

---

## Related

- [[EXTERNAL DATA REGISTRY (Phase 1 Build)]] — full source details
- [[CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)]] — protocol specifications
- [[Governance Controls — Phase 1 Completion Checklist]] — execution roadmap
- [[Governance Controls Integration Dashboard]] — control status overview

---

## Notes & Open Questions

1. **Reddit API priority:** Currently daily checks due to baseline. Can reduce to weekly after 1–2 weeks of stability?
2. **Law 25 monitoring:** Should we monitor Quebec National Assembly website for amendments in addition to API checks?
3. **Anthropic API versioning:** When Claude v4.7 releases (expected ~2026-06), does that trigger governance re-assessment?
4. **Phase 2 threshold:** What's the minimum policy change rate to trigger daily vs. weekly checks?

---

## Quick Links for Refresh Days

**Reddit API check:** https://www.reddit.com/dev/api
**GDPR text:** https://gdpr-info.eu/articles/principles/
**Law 25 (Quebec):** https://www.legisquebec.gouv.qc.ca/en/document/cs/law-25
**CCPA:** https://leginfo.legislature.ca.gov/
**FINRA Rule 4530:** https://www.finra.org/rules-guidance/rules/4530
**NIST SP 800-53:** https://csrc.nist.gov/publications/detail/sp/800-53/rev-5
**HIPAA:** https://www.ecfr.gov/current/title-45/section-164.316
**Cloudflare API:** https://developers.cloudflare.com/workers/platform/api/
**OpenRouter:** https://openrouter.ai/docs
**Anthropic:** https://docs.anthropic.com/claude/reference/getting-started-with-the-api

## Related

- [[CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)]] — governance protocol this calendar operationalizes; scheduling decisions enforce Control 2's staleness-detection rules
- [[External Data Registry — Phase 1 Build]] — source registry partner; the registry tracks what to verify, this calendar tracks when to verify it
- [[Governance and PHAROS MOC]]
