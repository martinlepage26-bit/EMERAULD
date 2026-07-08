---
type: governance-control
title: CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)
aliases:
- CONTROL 2 — External Data Lifecycle Protocol
- CONTROL 2
tags:
- governance-control
- areas
- control-2-external-data-lifecycle-protocol-regulatory-grounding-md
- policy
- external
- stale
- effective
- gdpr
- color-purple
status: active
created: '2026-04-26'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding).md
backlink_count: 22
backlinks:
- '[[Areas/PHAROS/CONTROL 1 — Tool Layer Audit Protocol (Regulatory Grounding)]]'
- '[[Areas/PHAROS/Control Protocols MOC]]'
- '[[archive/wiki-2026-07-08/Documents Root Intake — Hermes Action Map 2026-04-28]]'
- '[[Areas/PHAROS/External Data Refresh Calendar — Phase 1 Build]]'
- '[[Areas/PHAROS/External Data Registry — Phase 1 Build]]'
- '[[Areas/PHAROS/Governance Controls Integration Dashboard]]'
- '[[wiki/Governance Controls and Mechanisms]]'
- '[[archive/wiki-2026-07-08/Governance Controls — Baseline Assessment (2026-04-26)]]'
- '[[Areas/PHAROS/Governance Controls — Incident Response (Control Failure Procedures)]]'
- '[[Areas/PHAROS/Governance Controls — Monitoring Plan & Automation Roadmap]]'
- '[[archive/wiki-2026-07-08/Governance Controls — Phase 1 Completion Checklist]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Areas/PHAROS/OPEN RISKS — Three Governance Blindspots Requiring Recursive Control]]'
- '[[wiki/OUTLIERS — Five Notes That Break the Architecture]]'
- '[[Resources/Privacy as Contextual Integrity — Nissenbaum 2004 (Public Surveillance)]]'
- '[[Areas/PHAROS/Provisional Arbitration Charter — Argus Layer 9.5]]'
- '[[wiki/Reddit Data API — Access Terms and Rate Limits]]'
- '[[Resources/Regulatory Standards Reference Stack — Governance Controls Grounding]]'
- '[[archive/session-state/session-state-001]]'
- '[[maps/PHAROS Method Map]]'
- '[[memory]]'
- '[[memory/clients/helix-prospects/HELIX-hermes-assisted-prospect-extension-2026-05-06/2026-05-05_aurascribe-ai-medical-scribe-for-quebec]]'
tier: critical
regulatory-anchors:
- GDPR Article 5
- CCPA
- HIPAA
- FINRA
- ISO 9001
- SOX
---

# CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)

## Summary

Governance systems ingest external policy (GDPR text, API terms, compliance frameworks, vendor specifications) with expiry dates and change frequencies. [[OPEN RISKS — Three Governance Blindspots Requiring Recursive Control|Risk 2]] requires a protocol to track, refresh, and detect staleness of external data before it's used to make governance decisions. This note grounds the control in data governance and regulatory compliance standards.

## Regulatory Foundation

### GDPR Article 5 (Principles Relating to Processing of Personal Data)

**Article 5(1)(a) — Lawfulness, fairness, transparency:**
- Personal data must be processed lawfully and transparently according to the **rules in effect at the time of processing**.
- **If governance relies on a stale GDPR interpretation**, the governance decision is not GDPR-compliant, even if the interpretation was once valid.

**Article 5(1)(d) — Accuracy:**
- Personal data must be accurate and kept up to date. **Organizations must take reasonable steps to erase or rectify inaccurate data.**
- Applied to governance: If external policy snapshots in a governance system become inaccurate (policy changed, regulation updated), governance decisions made using stale policy are materially inaccurate.

**Article 32 — Security of Processing:**
- Organizations must implement technical and organizational measures to ensure a level of security appropriate to the risk, **including recovery from policy changes**.

**Regulatory Implication:** Stale external data in a governance system is non-compliant with GDPR Article 5(1)(d). Governance systems must refresh external data on a defined schedule or be non-compliant.

---

### CCPA (California Consumer Privacy Act) — Data Minimization

**CCPA § 1798.100(d) — Right to Know / Minimum Justifiable Purpose:**
- Governance systems cannot retain external policy data beyond the time it is **actively needed for the stated purpose**.
- Once external policy data becomes stale (new version is live), keeping the old version in governance violates minimization.

**Applied to governance:**
- External policy must be versioned. Old versions must be explicitly marked as historical.
- Active governance decisions must cite only current versions.
- Historical versions are retained for audit trail, not decision-making.

**Regulatory Implication:** Data minimization requires active versioning and deprecation of stale external data.

---

### HIPAA (Health Insurance Portability and Accountability Act) — Data Retention

**45 CFR § 164.316(b) — Documentation:**
- Organizations must maintain written documentation of policies and procedures for 6 years.
- When HIPAA rules change, the **old rule documentation must not be discarded** (audit trail), but **governance decisions must cite the new rule**.

**Applied to governance:**
- External health/compliance data (HIPAA rules, breach notification timelines, consent requirements) must be versioned with effective dates.
- Governance decisions cite effective date of rule used.
- If rule changes post-decision, old decision remains valid (under old rule), but new decisions use new rule.

**Regulatory Implication:** Effective-date tracking is mandatory. Governance must record which version of external policy each decision used.

---

### FINRA (Financial Industry Regulatory Authority) — Data Retention and Change Notification

**FINRA Rule 4530 — Books and Records:**
- Firms must maintain records of the **specific regulatory standard** applied to each decision, including the effective date of that standard.
- When regulations change (FINRA publishes new guidance, SEC rules change), firms must be able to demonstrate that new decisions use new rules.

**Applied to governance:**
- External policy snapshots must include: source, clipping date, effective date, expected expiry date, and link to live authoritative source.
- Governance records must cite which snapshot version (identified by effective date, not just "the FINRA rules") was used.

**Regulatory Implication:** Snapshot versioning with effective dates is mandatory audit trail requirement.

---

### ISO 9001:2015 — Quality Management — Document Control

**Section 7.5 — Documented Information (Control):**
- Documented information must be controlled (captured, reviewed, approved, distributed, accessed, secured, prevented from obsolescence, retrieved, stored, protected, controlled, deleted, retained).
- **Obsolete documents must be prevented from unintended use.**

**Applied to governance:**
- External policy snapshots are "documented information" in the governance system.
- Obsolete snapshots (newer version available) must be prevented from unintended use.
- Active governance use (decision-making) must be restricted to current versions.
- Obsolete versions are retained in archive for historical audit trail, not for active decisions.

**Regulatory Implication:** Version control and "current" marking is mandatory to prevent unintended use of stale data.

---

### SOX (Sarbanes-Oxley) — Effective Internal Control Over Financial Reporting

**SOX § 302 — Corporate Responsibility:**
- CIOs and CFOs must certify that internal controls are effective and that significant changes have been disclosed.
- If external policy (regulation, accounting standard) changes and governance doesn't refresh, that's a change to internal controls that must be disclosed.

**Applied to governance:**
- When external policy changes, governance control effectiveness may change.
- Changes to external policy constraints require re-documentation of control effectiveness.
- Failure to refresh external policy = failure to disclose material control changes.

**Regulatory Implication:** External policy changes cascade into internal control audit scope. Governance systems must track and flag policy changes.

---

## The Deeper Mechanism: When Does External Policy Change Trigger Re-Decision?

**The structural problem:** External policies (GDPR, API terms, compliance frameworks) change at different rates. Some change weekly (API rate limits), others annually (tax code), others never (foundational principles). Governance systems have no protocol for detecting which changes matter and forcing re-decision.

**Regulatory answer (GDPR + FINRA + SOX):** When external policy changes, governance decisions made under the old policy are not automatically invalidated — but they must be *known to be* based on old policy. Decisions made after policy change must use new policy. Decisions made *despite knowledge of policy change* are non-compliant.

**This means:** Governance systems must:
1. Know what external policy they depend on
2. Know when that policy is expected to change
3. Detect when it has changed
4. Flag decisions that were made under old policy vs. new policy
5. Force re-assessment of decisions if policy change would affect outcome

---

## Control Mechanism

### External Data Registry

**Every external policy/data ingested into governance must be recorded in a registry:**

| Field | Example | Purpose |
|---|---|---|
| **Source Name** | "GDPR Article 5" | What policy is this? |
| **Source URL** | https://gdpr-info.eu/articles/principles/ | Where is the authoritative live version? |
| **Clipping Date** | 2026-04-20 | When was this snapshot taken? |
| **Content Hash** | `sha256:a1b2c3...` | What changed? Detect drift. |
| **Effective Date** | 2018-05-25 | When did this version become operative? |
| **Expected Expiry** | None (foundational rule) | When will this change? |
| **Change Frequency** | Never | How often does this policy typically change? |
| **Regulatory Domain** | GDPR (EU) | What jurisdiction/framework governs this? |
| **Governance Usage** | "Consent requirement for personal data processing" | How does governance rely on this policy? |
| **Status** | `current` | Is this the operative version? |
| **Next Review Date** | 2026-07-26 (quarterly) | When must we check if it's still current? |
| **Quarantine Flag** | `false` | Should governance decisions use this? |

**Example entry:**

```
Source: Reddit Data API — OAuth and Rate Limits
URL: https://www.reddit.com/dev/api
Clipping Date: 2026-04-20
Content Hash: sha256:f47ac10b58cc4efa1a4cc8b0e6da3c5d61dc0c75
Effective Date: 2026-02-01
Expected Expiry: 2026-05-01 (API terms change quarterly)
Change Frequency: Quarterly
Regulatory Domain: API/Data Vendor (US)
Governance Usage: Rate limit planning, data retention requirements
Status: current
Next Review: 2026-05-15
Quarantine Flag: false
```

---

### Refresh and Staleness Detection Protocol

**Automated checks (run on schedule defined by "Change Frequency"):**

For each external data entry:

1. **Fetch live source** — retrieve the current version of the policy
2. **Compute hash** — `sha256(live_policy)`
3. **Compare to stored hash** — if hashes match, policy hasn't changed
4. **If hashes differ:**
   - Mark stored version as `status: stale_outdated`
   - Quarantine stored version: `quarantine_flag: true`
   - Ingest new version: new hash, new clipping date, new effective date (usually now)
   - Flag all recent governance decisions that used the old version
   - Create alert: "External policy changed; decisions using [old policy] may need re-assessment"

**Check frequency by change rate:**

| Change Frequency | Check Interval | Reason |
|---|---|---|
| Weekly (e.g., Reddit API) | Every 7 days | Catch changes before 2+ decisions made on stale data |
| Monthly | Every 2 weeks | Catch changes early |
| Quarterly | Every 6 weeks | Catch changes within one review cycle |
| Annually | Every 2 months | Catch changes before annual re-audit |
| Never | Annually (reference-only) | Foundational principles; check for out-of-band changes |

---

### Quarantine and Decision Flagging

**When external data becomes stale:**

1. **Quarantine the stale version:** Flag `quarantine_flag: true`, status: `stale_outdated`
2. **Halt new governance decisions** using stale data: Layer 0.5 gate rejects any governance claim citing quarantined external data
3. **Flag recent decisions**: Any governance decision made in last [refresh interval] using stale data is flagged for re-assessment
4. **Create re-assessment trigger**: If re-assessment shows policy change would have affected decision outcome, that decision is "needs revision"

**Re-assessment decision tree:**

```
Did external policy change?
  ├─ No → Continue using current decision
  └─ Yes → Did policy change affect governance outcome?
      ├─ No → Decision stands; note policy change in record
      └─ Yes → Decision needs revision under new policy
          ├─ Auto-revise if automated rule applies
          └─ Escalate to Queen Keyport if manual judgment required
```

---

### Integration Points

### [[HEPHAISTOS]] Scope Extension
> Governance must maintain an inventory of external dependencies and refresh external policy on a defined schedule. Stale external policy invalidates governance coherence claims.

### [[Queen Keyport]] Approval Gate (New Criterion)
**Before approval:**
- [ ] All cited external policy is current (not quarantined)
- [ ] Clipping date, effective date, and expected expiry are documented
- [ ] If policy is known to be changing soon, governance decision is bounded to current policy version
- [ ] External data registry entry created/updated

### [[Hermes]] Routing Rule (New Validation)
Routes governance decisions only if all external data is current. If external policy becomes stale post-routing, Hermes escalates to Operator for re-assessment decision.

### [[Argus]] Audit Layer
Audit questions:
- "Which external policies is this governance system dependent on?"
- "When did each policy last change, and did we detect that change?"
- "Are any governance decisions using stale external data?"

---

## Success Metrics

- **Zero governance decisions made using stale external policy** within one review cycle after policy change
- **100% of external data tracked** in registry with source, clipping date, and refresh schedule
- **Staleness detection catches all policy changes** before they affect 3+ downstream decisions
- **External data audit time** < 5% of governance decision time

---

## Related

- [[OPEN RISKS — Three Governance Blindspots Requiring Recursive Control]] — source risk statement
- [[Reddit Data API — Access Terms and Rate Limits]] — example of stale external data
- [[PHAROS Method — Technical Reference]] — governance pipeline that depends on accurate external constraints
- [[CONTROL 1 — Tool Layer Audit Protocol|Tool Layer Audit]] — parallel control mechanism
- [[GDPR Article 5 — Accuracy Principle Explained]] — regulatory foundation
- [[ISO 9001 Document Control and Obsolescence Prevention]] — quality management foundation
- [[Provisional Arbitration Charter — Argus Layer 9.5]] — apex-conflict route if external-policy currency and internal authority conflict
- [[External Data Registry — Phase 1 Build]] — live registry of all 25+ external policy/data sources with refresh schedules and staleness detection; Phase 1 implementation of this control
- [[External Data Refresh Calendar — Phase 1 Build]] — 90-day scheduling calendar for verifying external policy/data sources; operational scheduling arm of this control

---

- [[2026-05-05_aurascribe-ai-medical-scribe-for-quebec]]
## Open Questions for Next Major Turn

1. Which external policies changed since last refresh cycle?
2. Were any governance decisions made using now-stale external data?
3. Are there external data dependencies we haven't yet inventoried?
4. What is the actual change frequency for each external data source? (Are we checking too often, or not often enough?)
