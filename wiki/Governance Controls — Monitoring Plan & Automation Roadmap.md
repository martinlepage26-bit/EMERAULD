---
type: governance-procedures
title: Governance Controls — Monitoring Plan & Automation Roadmap
aliases:
- GOVERNANCE CONTROLS — Monitoring Plan & Automation Roadmap
- wiki/Governance Controls — Monitoring Plan & Automation Roadmap
tags:
- governance-procedures
- wiki
- governance-controls-monitoring-plan-automation-roadmap-md
- manual
- automation
- check
- alert
- hash
- color-purple
status: active
created: '2026-04-26'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Governance Controls — Monitoring Plan & Automation Roadmap.md
backlink_count: 7
backlinks:
- '[[Areas/PHAROS/Control Protocols MOC]]'
- '[[wiki/External Data Registry — Phase 1 Build]]'
- '[[wiki/Governance Controls and Mechanisms]]'
- '[[wiki/Governance Controls — Phase 1 Completion Checklist]]'
- '[[wiki/Governance Controls — Phase 1 Progress Checkpoint (2026-04-26)]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/Regulatory Standards Reference Stack — Governance Controls Grounding]]'
tier: critical
phase: Phase 2 (Automation)
---

# Governance Controls — Monitoring Plan & Automation Roadmap

## Summary

Transition from manual control checks to automated, continuous monitoring. This document defines: (1) what to monitor, (2) how often, (3) alert thresholds, (4) automation implementation timeline, and (5) dashboard design.

---

## Monitoring Matrix (What × How Often × Threshold)

### CONTROL 1 — Tool Layer Monitoring

| Component | Metric | Check Frequency | Alert Threshold | Who Monitors |
|---|---|---|---|---|
| Vector Search | Coherence (top-5 relevance for known queries) | Weekly | Any query < 0.4 score | Automation + Weekly manual test |
| Vector Search | Response time | Real-time | > 5 seconds | Automation (log, trend) |
| Vector Search | Index age | Daily | Index > 7 days old | Automation (trigger rebuild) |
| File System | Governance boundary files accessibility | Daily | Any file unreadable | Automation (trigger alert) |
| File System | Vault size vs. capacity | Weekly | Vault > 80% of capacity | Automation (trend warning) |
| Plugins | Dataview determinism | Monthly | Any query variance > 1 result | Manual test (3 runs) |
| Plugins | Obsidian Git sync status | Daily | Any commit pending > 1 day | Automation (trigger sync) |
| Dependencies | Python environment health | Weekly | Any import fails | Automation (test sentence-transformers) |
| Dependencies | Disk space in `/home/cerebrhoe` | Daily | < 5GB free | Automation (alert) |

**Implementation Level:** Real-time automation for continuous metrics; weekly manual for spot checks

---

### CONTROL 2 — External Data Monitoring

| Component | Metric | Check Frequency | Alert Threshold | Who Monitors |
|---|---|---|---|---|
| External Data Registry | Sources tracked | Monthly | Any ingested policy not in registry | Manual audit |
| External Data Registry | Refresh dates documented | Monthly | Any source missing next-check-date | Manual audit |
| Policy Freshness | Reddit API terms | Weekly (volatile) | Live source hash differs from snapshot | Automation (hash check) |
| Policy Freshness | GDPR Article 5 | Annually (stable) | Live source differs | Automation (annual check) |
| Policy Freshness | ISO standards | Every 2 months | Version number changes | Automation (version check) |
| Policy Freshness | HIPAA/FINRA rules | Every 6 weeks | Regulatory updates announced | Automation (RSS feed check) |
| Staleness Detection | Days past refresh date | Daily | Any source > 0 days past due | Automation (flag) |
| Quarantine Status | Quarantined external data | Daily | Any governance decision uses quarantined data | Automation (block before approval) |
| Decision Impact | Decisions affected by stale data | After each policy change | Any recent decision using old version | Manual review (triggered by staleness) |

**Implementation Level:** Real-time automation for time-based checks; daily for staleness; weekly for policy hash verification

---

### CONTROL 3 — Architecture Monitoring

| Component | Metric | Check Frequency | Alert Threshold | Who Monitors |
|---|---|---|---|---|
| Status Marking | % of architecture notes with status field | Monthly | < 95% | Manual audit |
| Status Clarity | Readers can identify current within 5 min | Quarterly | Spot check fails for any note | Manual testing (5 readers) |
| Supersession Registry | Completeness (all known transitions documented) | Quarterly | Any orphaned architecture found | Manual audit |
| Deprecation Notices | All deprecated notes linked to successors | Quarterly | Any deprecated note points nowhere | Manual audit |
| Migration Guides | Existence for major supersessions | Quarterly | No guide for Eight Ops → Three Agent | Manual (track as backlog) |
| Current Architecture Confusion | Decisions citing wrong architecture | After each major methodological change | Any decision uses deprecated without temporal scope | Manual review (triggered by change) |

**Implementation Level:** Quarterly manual audits; real-time flagging for deprecated architecture in governance approvals

---

## Automation Timeline (Phases)

### Phase 1: Infrastructure (Weeks 1-2, due ~2026-05-10)

**Goal:** Set up the monitoring data structures and initial automated checks.

**Tasks:**

1. **Build External Data Registry** (spreadsheet or Obsidian database)
   - Columns: Source | Clipping Date | Effective Date | Next Refresh Date | Status (current|stale|archived) | Hash
   - Seed with: Reddit API, GDPR, HIPAA, FINRA, ISO 15489, ISO 27001, COBIT, SOC 2, NIST
   - Owner: Manual entry (will automate hashing in Phase 2)
   - Due: 2026-05-03

2. **Create Refresh Calendar** (Obsidian Daily Notes or shared calendar)
   - View: All external data sources with next-check date
   - Trigger: Daily reminder of what to check today
   - Owner: Manual checks (will automate detection in Phase 2)
   - Due: 2026-05-03

3. **Apply Status Markers to All Notes** (audit all 312 wiki notes)
   - Add `status: current` to all active architecture/framework notes
   - Add `status: deprecated` to eight-operator notes (effective date: 2026-03-01)
   - Owner: Automated script? Or manual audit?
   - Due: 2026-05-10

4. **Create Supersession Registry** (document or database)
   - Entries: [Old → New], Effective Date, Rationale, Migration Guide Status
   - Populate: Eight Operators → Three-Agent, Linear Authority → Co-Equal
   - Owner: Manual entry
   - Due: 2026-05-03

5. **Draft Migration Guide** (Eight Operators → Three-Agent)
   - Concept translation table
   - Decision re-mapping
   - Effective date: 2026-03-01
   - Owner: Manual draft
   - Due: 2026-05-10

6. **Run Plugin Determinism Test** (Control 1)
   - Test: Run same Dataview query 3 times
   - Expected: Identical results each time
   - Owner: Manual test, document results
   - Due: 2026-05-01

**Success Criteria for Phase 1:**
- [ ] External Data Registry with 10+ sources tracked
- [ ] Refresh calendar with check dates set
- [ ] 95%+ of architecture notes have status field
- [ ] Supersession registry with 2+ entries
- [ ] Migration guide drafted
- [ ] Plugin determinism test passed

---

### Phase 2: Automation (Weeks 3-4, due ~2026-05-24)

**Goal:** Automate recurring checks; integrate with Layer 0.5 gate.

**Tasks:**

1. **Automated Staleness Detection** (script)
   - Input: External Data Registry
   - Check: For each source, is today > next-refresh-date?
   - Output: Alert list (which sources are stale)
   - Schedule: Daily (cron job)
   - Integration: Flag to Layer 0.5 gate (block approval if stale data cited)
   - Due: 2026-05-17

2. **Automated Policy Hash Verification** (script)
   - Input: External Data Registry (source URL, hash)
   - Check: Fetch live source, compute hash, compare to snapshot
   - Output: Hash match | Hash mismatch (policy changed!)
   - If mismatch: Log alert, flag for manual review, quarantine old version
   - Schedule: Per-source (weekly for volatile, annually for stable)
   - Due: 2026-05-17

3. **Automated Vector Search Health Check** (script)
   - Input: Known governance queries + expected results
   - Test: Run queries, check top-5 coherence scores
   - Output: Pass/Fail, scores, response time
   - Schedule: Weekly
   - Due: 2026-05-10

4. **Automated File System Integrity Check** (script)
   - Input: Governance boundary file list
   - Test: Stat each file, verify readable, compute checksums
   - Output: All accessible | Missing file | Corrupted file (checksum mismatch)
   - Schedule: Daily
   - Due: 2026-05-10

5. **Layer 0.5 Control Status Dashboard** (Obsidian note or static page)
   - Display: Real-time status of all three controls
   - Data sources: Output from scripts above
   - Auto-update: Hourly (or event-triggered)
   - Content: Green ✓ | Yellow ⚠️ | Red ✗ with last check time
   - Due: 2026-05-24

6. **Layer 0.5 Pre-Approval Integration** (governance workflow)
   - Before approval: Check dashboard for any control failure
   - If P0 failure: Block approval, escalate to Operator
   - If P1 failure: Approve with warning, document in decision record
   - If P2 failure: Approve, log incident for future remediation
   - Due: 2026-05-24

**Success Criteria for Phase 2:**
- [ ] Staleness detection running daily
- [ ] Policy hash verification running per-source schedule
- [ ] Vector search health check running weekly
- [ ] File system integrity check running daily
- [ ] Dashboard updated hourly
- [ ] Layer 0.5 checks blocking/warning approvals as designed

---

### Phase 3: Integration (Weeks 5-6, due ~2026-06-07)

**Goal:** Integrate controls into governance decision workflow; establish monitoring baseline.

**Tasks:**

1. **Incident Response Playbook** (documented procedures)
   - Owner: Operator
   - Content: Severity classification, escalation paths, remediation procedures
   - Reference: [[Governance Controls — Incident Response (Control Failure Procedures)]]
   - Due: 2026-06-07 (already drafted, just needs operational integration)

2. **Monitoring Alerts** (email/Slack/notifications)
   - Tool: Email, Slack, or Obsidian plugin
   - Triggers: Control failure, staleness detected, degradation warning
   - Recipients: Operator, (optional: team Slack channel for visibility)
   - Due: 2026-05-31

3. **Major-Turn Review Checklist** (integrated into session workflow)
   - Content: Review all control metrics from last session
   - Questions: Tool health? External policy changes? Architecture clarity?
   - Owner: Session-state documentation
   - Due: 2026-06-07

4. **Monthly Incident Report** (trend analysis)
   - Content: P0/P1/P2 incidents this month, remediation time, root causes
   - Schedule: First Monday of each month
   - Owner: Automated (with manual review)
   - Due: 2026-06-07

5. **Quarterly Architecture Audit** (formal review)
   - Content: Status markers, deprecation markers, migration guides, confusion risk
   - Owner: Manual audit (1-2 hours per quarter)
   - Schedule: Every 13 weeks starting 2026-06-30
   - Due: 2026-06-07 (first audit scheduled)

**Success Criteria for Phase 3:**
- [ ] Incident response procedures operational (tested with mock incident)
- [ ] Alerts configured and tested
- [ ] Major-turn checklist integrated into session routine
- [ ] Monthly incident reports being generated
- [ ] Quarterly audits scheduled and tracked

---

### Phase 4: Continuous Monitoring (Ongoing, after 2026-06-07)

**Recurring Checks:**
- Daily: File system integrity, staleness detection, Obsidian Git sync
- Weekly: Vector search health, external policy hash verification (volatile sources)
- Monthly: External data registry completeness, status marker audit
- Quarterly: Architecture clarity assessment, supersession registry review
- Annually: Baseline refresh (all external data verified current)

**Escalation Protocol:**
- P0: Operator escalated immediately
- P1: Escalated within 2 hours
- P2: Logged for weekly review

---

## Dashboard Design

### Layer 0.5 Control Status Dashboard

```
╔═══════════════════════════════════════════════════════════════╗
║            GOVERNANCE CONTROLS STATUS (Layer 0.5)             ║
║                  As of [timestamp]                            ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  CONTROL 1: Tool Layer Audit Protocol                        ║
║  ┌─────────────────────────────────────────────────────────┐ ║
║  │ ✓ Vector Search         [Last check: 2026-04-26 14:32]  │ ║
║  │   Coherence: 0.57 (avg of known queries)  Time: 2.3s    │ ║
║  │                                                          │ ║
║  │ ✓ File System Integrity [Last check: 2026-04-26 08:00]  │ ║
║  │   All boundary files accessible and readable            │ ║
║  │                                                          │ ║
║  │ ⏳ Plugin Determinism   [Last test: Never - SCHEDULE]    │ ║
║  │   Dataview tests not yet automated                      │ ║
║  │                                                          │ ║
║  │ ⚠️  Dependencies         [Last check: 2026-04-26 14:30]  │ ║
║  │   Warning: /home/cerebrhoe/ disk 78% full (>80%)        │ ║
║  │                                                          │ ║
║  │ Status: PASS (1 warning, monitor disk space)            │ ║
║  └─────────────────────────────────────────────────────────┘ ║
║                                                               ║
║  CONTROL 2: External Data Lifecycle Protocol                 ║
║  ┌─────────────────────────────────────────────────────────┐ ║
║  │ ⚠️  External Data Registry  [Last audit: 2026-04-26]     │ ║
║  │   Sources tracked: 7/11 (missing: Google Drive, Notion) │ ║
║  │   Next check due: Redis API (2026-04-27)                │ ║
║  │                                                          │ ║
║  │ ✓ Policy Freshness [Last check: 2026-04-26 daily]       │ ║
║  │   GDPR: current (hashes match)                           │ ║
║  │   Reddit API: APPROACHING STALE (check today)           │ ║
║  │   HIPAA: current (annual check in progress)             │ ║
║  │                                                          │ ║
║  │ ✗ Quarantine Status     [Last check: 2026-04-26]        │ ║
║  │   CRITICAL: Reddit API data marked stale; should be     │ ║
║  │   quarantined but no quarantine protocol yet            │ ║
║  │                                                          │ ║
║  │ Status: P1 FAILURE (policy approaching stale)           │ ║
║  │ Action: Check Reddit API today; update if needed        │ ║
║  └─────────────────────────────────────────────────────────┘ ║
║                                                               ║
║  CONTROL 3: Architecture Deprecation Protocol                ║
║  ┌─────────────────────────────────────────────────────────┐ ║
║  │ ⚠️  Status Marking       [Last audit: 2026-04-26]        │ ║
║  │   Marked notes: 1/312 (need to mark 311 more)           │ ║
║  │   Target: 95% marked by 2026-05-10                      │ ║
║  │                                                          │ ║
║  │ ⚠️  Supersession Registry [Last update: 2026-04-26]      │ ║
║  │   Documented transitions: 2 (need 5+)                   │ ║
║  │   Missing migration guides: Eight Ops → Three Agent     │ ║
║  │                                                          │ ║
║  │ ✓ Current Architecture Clarity [Last test: 2026-04-26]  │ ║
║  │   Three-Agent Stack discoverable (< 2 min)             │ ║
║  │                                                          │ ║
║  │ Status: P2 WARNING (audit not complete, but current     │ ║
║  │ architecture clear)                                     │ ║
║  │ Action: Complete Phase 1 infrastructure by 2026-05-10   │ ║
║  └─────────────────────────────────────────────────────────┘ ║
║                                                               ║
║  OVERALL STATUS: ⚠️  PARTIAL (Framework built, monitoring    ║
║  Phase 1 in progress. Controls operational but not fully     ║
║  automated. Layer 0.5 gate ready for deployment when Phase 1 ║
║  infrastructure complete.)                                   ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## Implementation Sequence (Detailed)

**Week 1 (2026-04-29–05-03):**
- Build External Data Registry
- Create Refresh Calendar
- Create Supersession Registry
- Draft Migration Guide
- Run plugin determinism test

**Week 2 (2026-05-04–05-10):**
- Apply status markers to 95%+ of notes
- Implement automated vector search health check
- Implement automated file system integrity check
- Integration testing of Phase 1 infrastructure

**Week 3 (2026-05-11–05-17):**
- Implement automated staleness detection
- Implement automated policy hash verification
- Deploy Phase 2 automation
- Test error cases and incident responses

**Week 4 (2026-05-18–05-24):**
- Build Layer 0.5 control status dashboard
- Integrate dashboard with Layer 0.5 approval gate
- Test full governance approval workflow with controls
- Document any issues and refinements

**Week 5-6 (2026-05-25–06-07):**
- Incident response procedures operational
- Monitoring alerts configured
- Major-turn review checklist integrated
- Quarterly audit schedule established
- System ready for continuous operations

---

## Risk Mitigation

**Risk:** Automation introduces new failure modes (scripts fail, dashboard stale, alerts missed)

**Mitigation:**
1. Keep manual fallback procedures documented
2. Test automation weekly
3. Alerting on alerts (if dashboard hasn't updated in 24 hours, alert Operator)
4. Redundant monitoring (two systems checking same thing)

---

## Success Criteria (Overall)

By 2026-06-07:
- [ ] All three controls fully automated and integrated
- [ ] Layer 0.5 gate preventing P0/P1 failures from reaching governance approvals
- [ ] Incident response procedures tested (at least one mock incident)
- [ ] Dashboard showing real-time control status
- [ ] Monitoring baseline established (can measure improvement)
- [ ] Quarterly/monthly review schedules in place
- [ ] Operator confident controls are catching failures

---

## Related

- [[Governance and PHAROS MOC]]
- [[Governance Controls — Baseline Assessment (2026-04-26)]] — current state
- [[Governance Controls — Incident Response (Control Failure Procedures)]] — failure handling
- [[Governance Controls Integration Dashboard]] — normal operation procedures
- [[CONTROL 1 — Tool Layer Audit Protocol (Regulatory Grounding)]] — tool layer specs
- [[CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)]] — external data specs
- [[CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding)]] — architecture specs

---

## Next Review Point

**Next Major Turn (~2026-05-10):**
- [ ] Phase 1 infrastructure 95% complete?
- [ ] Registry populated with 10+ sources?
- [ ] Status markers applied to 95%+ of notes?
- [ ] Plugin determinism test passed?
- [ ] Supersession registry and migration guide drafted?
- [ ] Any blockers or scope changes needed?

If Phase 1 on track: proceed to Phase 2 automation.
If Phase 1 blocked: escalate to Operator, adjust timeline.
