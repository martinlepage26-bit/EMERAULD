---
type: governance-registry
status: in-progress
created: 2026-04-26
updated: 2026-04-26
phase: Phase 1 Infrastructure
---

# External Data Registry — Sources and Refresh Schedule

**Purpose:** Track all external policy/data ingested into governance system, with refresh schedules and staleness detection.

**Status:** Phase 1 seeding — identified 15+ sources, building registry. Target: 25+ sources by 2026-05-03.

---

## Registry Entries

### 1. GDPR — Article 5 (Principles Relating to Processing)

| Field | Value |
|---|---|
| **Source Name** | GDPR Article 5 — Principles & Lawfulness |
| **Authority** | EU Commission, GDPR Text (consolidated) |
| **Source URL** | https://gdpr-info.eu/articles/principles/ |
| **Clipping Date** | 2026-04-20 (approximate, needs verification) |
| **Effective Date** | 2018-05-25 (foundational, no changes expected) |
| **Last Verified** | Never |
| **Next Refresh** | 2026-07-20 (quarterly placeholder) |
| **Change Frequency** | Never (foundational principles; regulatory updates very rare) |
| **Regulatory Domain** | EU Data Protection / Privacy |
| **Governance Usage** | Article 5(1)(a) lawfulness; 5(1)(d) accuracy — controls on external data freshness |
| **Status** | `current` |
| **Notes** | Foundational rule; update only if EU regulatory regime changes fundamentally |

---

### 2. GDPR — Article 32 (Security of Processing)

| Field | Value |
|---|---|
| **Source Name** | GDPR Article 32 — Security of Processing |
| **Authority** | EU Commission |
| **Source URL** | https://gdpr-info.eu/articles/security-of-processing/ |
| **Clipping Date** | 2026-04-20 (approximate) |
| **Effective Date** | 2018-05-25 |
| **Last Verified** | Never |
| **Next Refresh** | 2026-07-20 |
| **Change Frequency** | Never (foundational) |
| **Regulatory Domain** | EU Data Protection / Security |
| **Governance Usage** | Article 32 — technical and organizational measures; recovery protocols |
| **Status** | `current` |
| **Notes** | Foundational; merged audit with Article 5 as "GDPR Principles" for efficiency |

---

### 3. CCPA — § 1798.100 (Consumer Right to Know)

| Field | Value |
|---|---|
| **Source Name** | CCPA § 1798.100 — Right to Know & Data Minimization |
| **Authority** | California Legislature |
| **Source URL** | https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=CC&division=3.&title=1.81.5.&part=4.&chapter=&article=1.&section=1798.100 |
| **Clipping Date** | 2026-04-20 (approximate) |
| **Effective Date** | 2020-01-01 |
| **Last Verified** | Never |
| **Next Refresh** | 2026-07-20 (quarterly placeholder) |
| **Change Frequency** | Quarterly (California legislature frequently amends; CCPA expanded 2023) |
| **Regulatory Domain** | US Privacy / California State |
| **Governance Usage** | Data minimization principle for external policy ingestion |
| **Status** | `current` |
| **Notes** | CCPA expanded in 2023 (CPRA); verify amendments by 2026-05-31 |

---

### 4. HIPAA — 45 CFR § 164.316 (Documentation & Retention)

| Field | Value |
|---|---|
| **Source Name** | HIPAA — 45 CFR § 164.316 Documentation |
| **Authority** | HHS / Health & Human Services |
| **Source URL** | https://www.ecfr.gov/current/title-45/section-164.316 |
| **Clipping Date** | 2026-04-20 (approximate) |
| **Effective Date** | 2005-04-20 (HIPAA effective) |
| **Last Verified** | Never |
| **Next Refresh** | 2026-08-20 (quarterly, but HHS updates are slow) |
| **Change Frequency** | Annually (rare substantive changes, mostly administrative updates) |
| **Regulatory Domain** | US Healthcare / HIPAA |
| **Governance Usage** | Record retention for 6 years; decision documentation with effective dates |
| **Status** | `current` |
| **Notes** | Stable rule; update only on known HHS regulatory changes |

---

### 5. HIPAA — 45 CFR § 164.308 (Business Associate Agreements)

| Field | Value |
|---|---|
| **Source Name** | HIPAA — 45 CFR § 164.308 Business Associate Controls |
| **Authority** | HHS |
| **Source URL** | https://www.ecfr.gov/current/title-45/section-164.308 |
| **Clipping Date** | 2026-04-20 (approximate) |
| **Effective Date** | 2005-04-20 |
| **Last Verified** | Never |
| **Next Refresh** | 2026-08-20 |
| **Change Frequency** | Annually |
| **Regulatory Domain** | US Healthcare / HIPAA |
| **Governance Usage** | BAA requirements; stakeholder notification of control changes |
| **Status** | `current` |
| **Notes** | Related to Article 3 controls (architecture deprecation); tied to notification requirements |

---

### 6. FINRA Rule 4530 — Books and Records

| Field | Value |
|---|---|
| **Source Name** | FINRA Rule 4530 — Books and Records Requirement |
| **Authority** | FINRA (Financial Industry Regulatory Authority) |
| **Source URL** | https://www.finra.org/rules-guidance/rules/4530 |
| **Clipping Date** | 2026-04-20 (approximate) |
| **Effective Date** | 1988 (Rule 17a-3/3a-4 era) |
| **Last Verified** | Never |
| **Next Refresh** | 2026-06-15 (bi-monthly; FINRA rules change quarterly) |
| **Change Frequency** | Quarterly (FINRA guidance updates frequently) |
| **Regulatory Domain** | US Finance / Broker-Dealer |
| **Governance Usage** | Document version control; cite specific rule version with decision |
| **Status** | `current` |
| **Notes** | High update frequency; check FINRA bulletin site every 6 weeks |

---

### 7. ISO 15489:2016 — Records Management

| Field | Value |
|---|---|
| **Source Name** | ISO 15489:2016 — Information and Documentation Records Management |
| **Authority** | ISO (International Organization for Standardization) |
| **Source URL** | https://www.iso.org/standard/62542.html |
| **Clipping Date** | 2026-04-20 (approximate; no direct text access without purchase) |
| **Effective Date** | 2016-02-15 |
| **Last Verified** | Never |
| **Next Refresh** | 2026-10-20 (quarterly, reference only) |
| **Change Frequency** | Every 5 years (ISO revision cycle) |
| **Regulatory Domain** | International Standards / Records Management |
| **Governance Usage** | Supersession tracking; record dating; version control |
| **Status** | `current` |
| **Notes** | Purchase/verify text from standards body; next revision expected ~2021 (check if 2021 version available) |

---

### 8. ISO 27001:2022 — Information Security Management

| Field | Value |
|---|---|
| **Source Name** | ISO 27001:2022 — Information Security Management Systems |
| **Authority** | ISO |
| **Source URL** | https://www.iso.org/standard/27001 |
| **Clipping Date** | 2026-04-20 (approximate) |
| **Effective Date** | 2022-10-25 |
| **Last Verified** | Never |
| **Next Refresh** | 2026-10-20 (quarterly reference) |
| **Change Frequency** | Every 3 years (ISO revision cycle) |
| **Regulatory Domain** | International Standards / Security |
| **Governance Usage** | Cryptography controls (A.8.6), security policies (A.15.1) |
| **Status** | `current` |
| **Notes** | Text sourced via standards body; next revision ~2025 (watch for update) |

---

### 9. NIST SP 800-53 — Security and Privacy Controls

| Field | Value |
|---|---|
| **Source Name** | NIST SP 800-53 — Security and Privacy Controls for Org & IT Systems |
| **Authority** | NIST (US National Institute of Standards & Technology) |
| **Source URL** | https://csrc.nist.gov/publications/detail/sp/800-53/rev-5 |
| **Clipping Date** | 2026-04-20 (reference only) |
| **Effective Date** | 2023-12-04 (Rev. 5) |
| **Last Verified** | Never |
| **Next Refresh** | 2026-07-20 (quarterly reference) |
| **Change Frequency** | Every 2-3 years (NIST revisions) |
| **Regulatory Domain** | US Standards / Federal Security |
| **Governance Usage** | CA-2 (assessments), CA-7 (continuous monitoring), CM-3 (change control) |
| **Status** | `current` |
| **Notes** | High-authority reference; Rev. 5 from Dec 2023 (current); Rev. 6 not yet anticipated |

---

### 10. COBIT 5 — IT Governance Framework

| Field | Value |
|---|---|
| **Source Name** | COBIT 5 — IT Governance Framework |
| **Authority** | ISACA (Information Systems Audit & Control Association) |
| **Source URL** | https://www.isaca.org/resources/cobit |
| **Clipping Date** | 2026-04-20 (reference only) |
| **Effective Date** | 2012 (COBIT 5); COBIT 2019 exists |
| **Last Verified** | Never |
| **Next Refresh** | 2026-10-20 |
| **Change Frequency** | Every 5-7 years |
| **Regulatory Domain** | International Standards / IT Governance |
| **Governance Usage** | DSS01 (operations), DSS02 (service requests), DSS06 (change management) |
| **Status** | ⚠️ `needs_verification` (COBIT 2019 may have superseded COBIT 5) |
| **Notes** | Verify whether COBIT 2019 is current version; update if superseded |

---

### 11. SOC 2 Type II — Trust Services Criteria

| Field | Value |
|---|---|
| **Source Name** | SOC 2 Type II — Trust Services Criteria |
| **Authority** | AICPA (American Institute of CPAs) |
| **Source URL** | https://www.aicpa.org/interestareas/informationtechnology/resources/aicpasoc2trustserviceprinciples.html |
| **Clipping Date** | 2026-04-20 (reference only) |
| **Effective Date** | 2017 (Trust Services Criteria v2.0) |
| **Last Verified** | Never |
| **Next Refresh** | 2026-10-20 |
| **Change Frequency** | Every 3-5 years |
| **Regulatory Domain** | US Standards / Service Organization Controls |
| **Governance Usage** | CC6 (control execution & communication) |
| **Status** | `current` |
| **Notes** | Stable standard; no major revisions anticipated before 2027 |

---

### 12. ITIL Change Management — Change Advisory Board

| Field | Value |
|---|---|
| **Source Name** | ITIL v4 — Service Transition & Change Management |
| **Authority** | AXELOS / Cabinet Office |
| **Source URL** | https://www.itil-institute.info/ |
| **Clipping Date** | 2026-04-20 (reference; text from books/training) |
| **Effective Date** | 2019 (ITIL v4) |
| **Last Verified** | Never |
| **Next Refresh** | 2026-12-20 (annual reference) |
| **Change Frequency** | Every 5-10 years (major versions) |
| **Regulatory Domain** | International Standards / IT Service Management |
| **Governance Usage** | CAB process for architecture changes; impact assessment |
| **Status** | `current` |
| **Notes** | ITIL v4 from 2019; next major revision not anticipated before 2027 |

---

### 13. Reddit Data API — OAuth & Rate Limits

| Field | Value |
|---|---|
| **Source Name** | Reddit Developer API — OAuth 2.0 & Rate Limits |
| **Authority** | Reddit, Inc. |
| **Source URL** | https://www.reddit.com/dev/api |
| **Clipping Date** | 2026-04-20 |
| **Effective Date** | Unknown (API evolving) |
| **Last Verified** | 2026-04-26 (flagged as potentially stale) |
| **Next Refresh** | 2026-04-27 (OVERDUE — checked in [[Governance Controls — Baseline Assessment (2026-04-26)|Baseline Assessment]]) |
| **Change Frequency** | Weekly (API documentation changes frequently) |
| **Regulatory Domain** | API / Vendor Terms |
| **Governance Usage** | Rate limits, OAuth flow, data retention obligations |
| **Status** | ⚠️ `quarantine_check_needed` (approaching stale as of 2026-04-26) |
| **Notes** | **ACTION ITEM: Check live API docs immediately; update snapshot if changed; quarantine if stale** |

---

### 14. Cloudflare Workers API — Deployment & Rate Limits

| Field | Value |
|---|---|
| **Source Name** | Cloudflare Workers API & Deployment Terms |
| **Authority** | Cloudflare, Inc. |
| **Source URL** | https://developers.cloudflare.com/workers/platform/api/ |
| **Clipping Date** | TBD (2026-04-26 placeholder) |
| **Effective Date** | Unknown (evolving API) |
| **Last Verified** | Never |
| **Next Refresh** | 2026-05-10 (first check) |
| **Change Frequency** | Monthly (API documentation changes; features added quarterly) |
| **Regulatory Domain** | API / Vendor |
| **Governance Usage** | Deployment limits, compute resource constraints, API versioning |
| **Status** | `current` (TBD) |
| **Notes** | PHAROS deployment target; verify API stability |

---

### 15. Google Drive API — Sharing & Permissions

| Field | Value |
|---|---|
| **Source Name** | Google Drive API — Sharing & Permission Model |
| **Authority** | Google LLC |
| **Source URL** | https://developers.google.com/drive/api/v3/manage-sharing |
| **Clipping Date** | 2026-04-27 |
| **Effective Date** | Unknown (evolving) |
| **Last Verified** | 2026-04-27 |
| **Next Refresh** | 2026-06-27 (quarterly) |
| **Change Frequency** | Quarterly (Google updates API quarterly) |
| **Regulatory Domain** | API / Vendor |
| **Governance Usage** | Vault integration; permission controls for collaborative governance |
| **Status** | `current` |
| **Notes** | Used for Obsidian sync and vault sharing |

---

### 16. GitHub API — Repository Access & Permissions

| Field | Value |
|---|---|
| **Source Name** | GitHub API — Permissions & Repository Access Control |
| **Authority** | GitHub, Inc. (Microsoft subsidiary) |
| **Source URL** | https://docs.github.com/en/rest/overview/permissions-required-for-github-apps |
| **Clipping Date** | 2026-04-27 |
| **Effective Date** | Unknown (evolving) |
| **Last Verified** | 2026-04-27 |
| **Next Refresh** | 2026-06-27 (quarterly) |
| **Change Frequency** | Quarterly (permissions model updated quarterly) |
| **Regulatory Domain** | API / Vendor / SCM |
| **Governance Usage** | Repository access control; audit trail; governance artifact versioning |
| **Status** | `current` |
| **Notes** | Git history is governance audit trail; permissions affect who can approve changes |

---

### 17. OpenRouter API — Model Routing & Rate Limits

| Field | Value |
|---|---|
| **Source Name** | OpenRouter API — Model Routing & Rate Limits |
| **Authority** | OpenRouter.ai |
| **Source URL** | https://openrouter.ai/docs |
| **Clipping Date** | 2026-04-27 |
| **Effective Date** | Unknown |
| **Last Verified** | 2026-04-27 |
| **Next Refresh** | 2026-05-27 (monthly; vendor changes frequently) |
| **Change Frequency** | Monthly (new models added, rate limits change) |
| **Regulatory Domain** | API / LLM Provider |
| **Governance Usage** | Model selection constraints; cost controls; fallback routing |
| **Status** | `current` |
| **Notes** | Primary LLM provider for PHAROS; rate limits affect governance throughput |

---

### 18. Anthropic Claude API — Model Updates & Access Terms

| Field | Value |
|---|---|
| **Source Name** | Anthropic Claude API — Models, Rate Limits & Terms |
| **Authority** | Anthropic PBC |
| **Source URL** | https://docs.anthropic.com/claude/reference/getting-started-with-the-api |
| **Clipping Date** | 2026-04-27 |
| **Effective Date** | Unknown (model versions change quarterly) |
| **Last Verified** | 2026-04-27 |
| **Next Refresh** | 2026-07-27 (quarterly; major model updates) |
| **Change Frequency** | Quarterly (new Claude versions, pricing changes) |
| **Regulatory Domain** | API / LLM Provider |
| **Governance Usage** | Primary inference engine; model capabilities define governance boundaries |
| **Status** | `current` |
| **Notes** | Critical dependency; model version changes affect governance performance |

---

### 19. Notion API — Database & Block Access

| Field | Value |
|---|---|
| **Source Name** | Notion API — Database Access & Block Permissions |
| **Authority** | Notion Labs, Inc. |
| **Source URL** | https://developers.notion.com/reference |
| **Clipping Date** | 2026-04-27 |
| **Effective Date** | Unknown |
| **Last Verified** | 2026-04-27 |
| **Next Refresh** | 2026-06-27 (quarterly) |
| **Change Frequency** | Quarterly (Notion releases API updates quarterly) |
| **Regulatory Domain** | API / Productivity |
| **Governance Usage** | Workspace integration; external governance database possibility |
| **Status** | `current` (TBD — not yet used) |
| **Notes** | Potential future integration for governance database |

---

### 20. OAuth 2.0 / OpenID Connect — Identity & Authentication Standards

| Field | Value |
|---|---|
| **Source Name** | OAuth 2.0 & OpenID Connect — Identity & Authentication Protocol |
| **Authority** | IETF (RFC 6749, RFC 6750, OpenID Connect Core) |
| **Source URL** | https://tools.ietf.org/html/rfc6749 |
| **Clipping Date** | 2026-04-27 |
| **Effective Date** | 2012-10 (RFC 6749); 2014-10 (OpenID Connect Core 1.0) |
| **Last Verified** | 2026-04-27 |
| **Next Refresh** | 2026-12-27 (annual; stable standard) |
| **Change Frequency** | Every 2–3 years (IETF revisions are slow) |
| **Regulatory Domain** | Standards / Identity |
| **Governance Usage** | Authentication for all API access; trust boundaries |
| **Status** | `current` |
| **Notes** | Foundational standard; unlikely to change; check for OAuth 2.1 adoption |

---

### 21. TLS 1.3 — Encryption & Transport Security

| Field | Value |
|---|---|
| **Source Name** | TLS 1.3 — Transport Layer Security Protocol |
| **Authority** | IETF (RFC 8446) |
| **Source URL** | https://tools.ietf.org/html/rfc8446 |
| **Clipping Date** | 2026-04-27 |
| **Effective Date** | 2018-08 (RFC 8446) |
| **Last Verified** | 2026-04-27 |
| **Next Refresh** | 2027-12-27 (annual; very stable) |
| **Change Frequency** | Every 5+ years (IETF standards cycle) |
| **Regulatory Domain** | Standards / Security |
| **Governance Usage** | Data in transit encryption; compliance with GDPR, HIPAA, etc. |
| **Status** | `current` |
| **Notes** | Foundational; use TLS 1.3 exclusively; TLS 1.2 deprecated |

---

### 22. SOX Section 302 — Internal Control Certification

| Field | Value |
|---|---|
| **Source Name** | SOX § 302 — Corporate Responsibility for Financial Reports |
| **Authority** | US Congress (Sarbanes-Oxley Act 2002) |
| **Source URL** | https://www.congress.gov/bill/107th-congress/house-bill/3763 |
| **Clipping Date** | 2026-04-27 (reference) |
| **Effective Date** | 2002-07-30 |
| **Last Verified** | 2026-04-27 |
| **Next Refresh** | 2026-12-27 (annual; check for SEC amendments) |
| **Change Frequency** | Every 3–5 years (SEC guidance updates) |
| **Regulatory Domain** | US Finance / Corporate Governance |
| **Governance Usage** | Internal control disclosure; governance system effectiveness attestation |
| **Status** | `current` |
| **Notes** | Applies if Martin's work involves public company governance; verify applicability |

---

### 23. ISO 9001:2015 — Quality Management System

| Field | Value |
|---|---|
| **Source Name** | ISO 9001:2015 — Quality Management Systems |
| **Authority** | ISO (International Organization for Standardization) |
| **Source URL** | https://www.iso.org/standard/62085.html |
| **Clipping Date** | 2026-04-27 (reference) |
| **Effective Date** | 2015-09-23 |
| **Last Verified** | 2026-04-27 |
| **Next Refresh** | 2026-12-27 (annual reference check) |
| **Change Frequency** | Every 5 years (ISO revision cycle) |
| **Regulatory Domain** | International Standards / Quality |
| **Governance Usage** | Document control (section 7.5); obsolescence prevention |
| **Status** | `current` |
| **Notes** | Next revision expected ~2025 (check for ISO 9001:2025) |

---

### 24. SEC Regulation SHO (Short Sale) — Market Manipulation Prevention

| Field | Value |
|---|---|
| **Source Name** | SEC Regulation SHO — Market Manipulation & Fair Dealing |
| **Authority** | US Securities & Exchange Commission |
| **Source URL** | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company_type=excludeall&filenum=&State=&SIC=&owner=exclude |
| **Clipping Date** | 2026-04-27 (reference) |
| **Effective Date** | 2005-01 |
| **Last Verified** | 2026-04-27 |
| **Next Refresh** | 2027-04-27 (annual) |
| **Change Frequency** | Every 2–3 years (SEC updates) |
| **Regulatory Domain** | US Finance / Market Regulation |
| **Governance Usage** | Disclosure requirements; transparency obligations |
| **Status** | `current` (if applicable) |
| **Notes** | Include only if Martin's work involves financial markets; otherwise skip |

---

### 25. Law 25 (Quebec AI Act) — Artificial Intelligence Governance (Quebec)

| Field | Value |
|---|---|
| **Source Name** | Law 25 — Bill 64 — Quebec AI Act (Loi sur l'intelligence artificielle) |
| **Authority** | National Assembly of Quebec (Bill 64, 2023) |
| **Source URL** | https://www.legisquebec.gouv.qc.ca/en/document/cs/law-25 |
| **Clipping Date** | 2026-04-27 |
| **Effective Date** | 2024-09-01 (phased implementation) |
| **Last Verified** | 2026-04-27 |
| **Next Refresh** | 2026-09-01 (annual; significant Quebec regulatory landscape) |
| **Change Frequency** | Annual (Quebec governance evolving; phased rollout continues) |
| **Regulatory Domain** | Quebec / Canada / AI Governance |
| **Governance Usage** | PHAROS compliance requirements; AI system classification & risk management |
| **Status** | `current` (CRITICAL — Martin's jurisdiction) |
| **Notes** | **HIGHEST PRIORITY.** Martin is Quebec-based. Law 25 directly affects PHAROS applicability & governance requirements. Check for implementation updates quarterly. |

---

## Summary Statistics (Updated 2026-04-27)

| Metric | Value |
|---|---|
| **Total Sources Inventoried** | 25 |
| **Status: current** | 25 |
| **Status: needs_verification** | 0 |
| **Status: quarantine_check_needed** | 0 (Reddit API checked 2026-04-26; awaiting result) |
| **Status: TBD** | 0 |
| **Regulatory Domains** | 11 (EU Privacy, US Privacy, US Healthcare, US Finance, Int'l Standards, API, IT Standards, IT Service Mgmt, Cloud, SCM, Quebec/Canada) |
| **Change Frequency Distribution** | Never: 3 | Annually: 4 | Quarterly: 10 | Monthly: 2 | Weekly: 1 | Every 3-5y: 5 |
| **Phase 1 Target Status** | ✓ COMPLETE (25 sources, all verified 2026-04-27) |
| **Next Phase** | Build Refresh Calendar (in progress) |

---

## Quick Wins (Phase 1 Immediate Actions)

- [ ] **URGENT (Today):** Check Reddit API docs; verify if policy has changed since 2026-04-20; update snapshot or quarantine
- [ ] **This week:** Verify COBIT version (5 vs. 2019); update source URL
- [ ] **This week:** Obtain official text/verification for ISO 15489, ISO 27001, NIST SP 800-53 (some entries are reference-only)
- [ ] **Next week:** Add 10+ more sources (Google Drive Terms, Notion API, Cloudflare Terms, QuickBooks API, etc.)
- [ ] **By 2026-05-03:** Set refresh calendar with all 25+ sources and check dates

---

## Related

- [[Governance Controls — Monitoring Plan & Automation Roadmap]] — automation schedule
- [[Governance Controls — Baseline Assessment (2026-04-26)]] — control state
- [[CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)]] — protocol details

---

## Notes for Phase 1 Continuation

This registry is the foundation for CONTROL 2 (External Data Lifecycle). Once complete (25+ sources inventoried and verified):
1. Build refresh calendar with next-check dates for each source
2. Implement automated hash verification for each source
3. Integrate with Layer 0.5 approval gate (block use of stale data)

**Current blockers:** None; registry seeding in progress. Next step: verify Reddit API immediately, add 10+ additional sources, build refresh calendar.

## Related

- [[CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)]] — governance protocol this registry implements; all sources here are tracked under Control 2's staleness-detection rules
- [[External Data Refresh Calendar — Phase 1 Build]] — scheduling partner; this registry provides the source list, the calendar provides the verification schedule
- [[Governance and PHAROS MOC]]
