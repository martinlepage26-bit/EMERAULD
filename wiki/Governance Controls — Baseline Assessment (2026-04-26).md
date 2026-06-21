---
type: governance-assessment
aliases: [GOVERNANCE CONTROLS — BASELINE ASSESSMENT (2026-04-26)]
status: active
created: 2026-04-26
updated: 2026-04-26
assessment-date: 2026-04-26
baseline-version: 1
---

# Governance Controls — Baseline Assessment (2026-04-26)

## Executive Summary

Baseline assessment of three governance controls across the EMERAULD vault and PHAROS governance system. **Current status:** Framework built, controls drafted, *baseline not yet measured against real operations*. This assessment establishes the zero-point for monitoring and creates the control testing plan.

---

## CONTROL 1 — Tool Layer Audit (Current State)

### Vector Search

**Test:** Query for "governance controls audit regulation" (high-governance relevance)

**Result:** ✓ PASS
- 4 results returned with coherent relevance scores (0.58, 0.49, 0.47, 0.47)
- Top result: RIA-CODEX System Audit Protocol (relevant)
- Second result: RECURSO Final Audit (governance context present)
- Coherence: Confirmed (search understands governance domain)
- Load time: ~2 seconds (acceptable)

**Finding:** Vector search is operational and coherent. No degradation detected.

---

### File System Integrity

**Test:** Verify all governance boundary files are accessible

**Files checked:**
- ✓ `/wiki/OPEN RISKS — Three Governance Blindspots Requiring Recursive Control.md` (present, 165 lines)
- ✓ `/wiki/CONTROL 1 — Tool Layer Audit Protocol (Regulatory Grounding).md` (present, 280 lines)
- ✓ `/wiki/CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding).md` (present, 330 lines)
- ✓ `/wiki/CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding).md` (present, 350 lines)
- ✓ `/wiki/GOVERNANCE CONTROLS INTEGRATION DASHBOARD.md` (present, 490 lines)
- ✓ `memory.md` (governance memory updated, 120 lines)

**Finding:** All governance boundary files accessible. File system integrity: PASS.

---

### Plugin Determinism

**Current governance plugins:** Obsidian Dataview, Obsidian Git, Templater (implied by Daily Notes)

**Test Plan (deferred to monitoring phase):**
- Run three identical Dataview queries (external data registry count)
- Compare results
- If identical 5/5 times: deterministic ✓
- If variance: non-deterministic ✗

**Current Status:** Not yet tested. **Action item:** Test on next major turn.

---

### Tool Dependency Chain

**Identified tool dependencies:**
1. **Vector search** (all-MiniLM-L6-v2 sentence transformer) → external data discovery
2. **File system** (NTFS mounted at `/mnt/c/...`) → policy snapshots, architecture status markers
3. **Obsidian plugins** (Dataview, Git, Daily Notes) → governance records, versioning
4. **Python environment** (`/home/cerebrhoe/.venvs/lightrag/`) → vector embedding, search execution

**Cascade risk analysis:**
- If vector search fails → external data becomes undiscoverable → Control 2 fails
- If file system fails → architecture markers lost → Control 3 fails
- If Obsidian plugins fail → governance records become unqueryable
- If Python environment fails → vector search stops working

**Current Status:** Documented, not yet mitigated. **Action item:** Add circuit breakers and fallback methods.

---

### Governance Architecture Status

**Current governance architecture:** HEPHAISTOS / Queen Keyport / Hermes (three-agent stack)

**Predecessor architecture:** Eight Sovereign Operators (Agatha, DOTTIE, MOBI variants)

**Status:** Mixed
- ✓ Current architecture clearly documented
- ✗ Predecessor not yet marked with deprecation date
- ✗ Supersession registry started but incomplete

**Finding:** Architecture status not yet fully formalized. **Action item:** Add deprecation markers to eight-operator notes (status: deprecated, effective date: 2026-03-01).

---

## CONTROL 2 — External Data Lifecycle (Current State)

### External Data Registry

**Inventory of external policy/data in vault:**
- Grep found 63 references to external data/policy/compliance frameworks
- Identified sources: GDPR, CCPA, HIPAA, FINRA, ISO standards, API terms, compliance frameworks
- **Registry entry status:** Not yet formalized

**Sample sources identified:**
- [[Reddit Data API — Access Terms and Rate Limits]] (marked "potentially stale," clipped 2026-04-20)
- [[GDPR Article 5 — Principles]] (foundational, never expires)
- [[HIPAA 45 CFR § 164 — Security and Privacy]] (regulatory, changes annually)
- [[FINRA Rule 4530 — Books and Records]] (regulatory, changes ad-hoc)
- [[ISO 15489 Records Management]] (standard, stable, 5-7 year revision cycles)
- [[ISO 27001:2022 Information Security Management]] (standard, 3-year revision cycles)

**Current Status:** External data exists but not tracked in registry. **Action item:** Create External Data Registry spreadsheet with source, clipping date, refresh schedule, status.

---

### Refresh Cadence Baseline

**Proposed refresh schedule by change frequency:**

| Source Type | Change Frequency | Proposed Check Interval | Example |
|---|---|---|---|
| API Terms | Weekly | Every 7 days | Reddit API, Cloudflare Workers |
| Regulatory Updates | Monthly/Quarterly | Every 6 weeks | FINRA, SEC guidance, CCPA updates |
| Standards | Annually | Every 2 months | ISO, NIST SP 800-53 |
| Foundational Rules | Never (reference) | Annually | GDPR foundational principles, HIPAA core rules |

**Current Status:** Schedule proposed, not yet implemented. **Action item:** Create refresh calendar with next check dates.

---

### Staleness Detection

**Test for stale external data:**

Checked: [[Reddit Data API — Access Terms and Rate Limits]]
- Clipping date: 2026-04-20
- Time elapsed: 6 days (as of 2026-04-26)
- Expected refresh: Every 7 days (API terms are volatile)
- Status: APPROACHING STALE (check date: 2026-04-27)

**Finding:** At least one external data source is approaching staleness. Refresh protocol not yet triggered (no automation in place). **Action item:** Automate staleness detection before external data affects governance decisions.

---

### External Data Quarantine Status

**Currently quarantined external data:** None

**Should be quarantined:** Potentially [[Reddit Data API — Access Terms and Rate Limits]] (approaching stale)

**Finding:** No quarantine protocol implemented. Decision-making can still use potentially stale data without warning. **Action item:** Implement quarantine flagging.

---

## CONTROL 3 — Architecture Deprecation (Current State)

### Supersession Registry

**Current entries:**

| Old Architecture | New Architecture | Effective Date | Status | Documented? |
|---|---|---|---|---|
| Eight Sovereign Operators | Three-Agent Stack (HEPHAISTOS/QK/Hermes) | 2026-03-01 | Actual supersession | Partial (need formal registry) |
| Linear Authority Chain | Co-Equal Authority Model | 2026-04-23 | Internal refinement only | Partial (documented in notes) |

**Current Status:** Two supersessions exist in practice, but not formalized in registry. **Action item:** Create Supersession Registry with effective dates, rationale, migration guides.

---

### Status Marking System

**Notes with status fields:** 1 out of 312 wiki notes

**Expected:** All architecture/framework notes should have `status: current | deprecated | archived`

**Finding:** Status marking system defined but not yet applied to existing corpus. **Action item:** Audit all architecture notes and add status fields.

---

### Migration Guides

**Current migration guides:** None created

**Needed guides:**
- Eight Sovereign Operators → Three-Agent Stack (important, multiple systems affected)
- Linear Authority → Co-Equal Authority (internal, lower priority)

**Finding:** No migration guides exist to help readers transition between architectures. **Action item:** Create guide for Eight Operators → Three-Agent translation.

---

### Current Architecture Clarity

**Can readers identify current architecture within 5 minutes?**

**Test:** Ask "What is the current governance authority model?"
- Answer in vault: [[HEPHAISTOS]], [[Queen Keyport]], [[Hermes]] (three-agent stack)
- Discoverability: Good (entrypoint files clearly named)
- Confusion risk: Low (current model is recent and well-documented)
- Historical context: Medium (old model still linked without clear deprecation)

**Finding:** Current architecture is discoverable, but historical model is accessible without clear "deprecated" markers. **Action item:** Add deprecation notice to eight-operator notes.

---

## Summary Table: Control Status

| Control | Component | Status | Finding | Action Item |
|---|---|---|---|---|
| **1 — Tool Layer** | Vector search | ✓ PASS | Coherent, operational | None (continue monitoring) |
| | File system integrity | ✓ PASS | All boundaries accessible | None (continue monitoring) |
| | Plugin determinism | ⏳ UNKNOWN | Not yet tested | Test on next turn |
| | Tool dependency chain | ⏳ DOCUMENTED | Risks identified | Add circuit breakers |
| | Governance architecture | ⚠️ PARTIAL | Current clear, predecessor not deprecated | Add deprecation markers |
| **2 — External Data** | Registry | ❌ NOT BUILT | 63 sources identified, not tracked | Create External Data Registry |
| | Refresh schedule | ⏳ PROPOSED | Schedule designed, not implemented | Build refresh calendar |
| | Staleness detection | ⚠️ MANUAL | One source approaching stale | Automate detection |
| | Quarantine protocol | ❌ NOT IMPLEMENTED | No flagging in place | Build quarantine system |
| **3 — Architecture** | Supersession registry | ❌ NOT FORMALIZED | Two supersessions exist, not registered | Create Supersession Registry |
| | Status marking | ❌ NOT APPLIED | System designed, 1/312 notes marked | Audit and mark all notes |
| | Migration guides | ❌ NOT CREATED | Eight Ops → Three Agent guide needed | Draft migration guide |
| | Current clarity | ✓ GOOD | Current architecture discoverable | None (continue monitoring) |

---

## Monitoring Plan (Phases)

### Phase 1: Baseline Infrastructure (Weeks 1-2, due ~2026-05-10)
- [x] Framework controls designed
- [ ] External Data Registry built (spreadsheet or database)
- [ ] Refresh calendar created with next check dates
- [ ] Plugin determinism test run (3 identical Dataview queries)
- [ ] Supersession Registry created with two initial entries
- [ ] Deprecation markers added to eight-operator notes
- [ ] Migration guide drafted (Eight Operators → Three Agent)

### Phase 2: Automation (Weeks 3-4, due ~2026-05-24)
- [ ] Automated staleness detection (check external data sources weekly)
- [ ] Automated quarantine flagging (flag stale data, prevent governance use)
- [ ] Automated vector search health checks (run weekly coherence test)
- [ ] Automated file system integrity check (verify governance boundary files)
- [ ] Dashboard showing control status (real-time view of all three controls)

### Phase 3: Integration (Weeks 5-6, due ~2026-06-07)
- [ ] Layer 0.5 pre-approval checklist integrated into governance workflow
- [ ] Incident response procedures (what happens if a control fails)
- [ ] Monitoring alerts configured (slack/email when control threshold breached)
- [ ] Major-turn review checklist implemented
- [ ] Quarterly audit schedule established

### Phase 4: Continuous Monitoring (Ongoing)
- [ ] Weekly tool layer health check (vector search coherence, file system, plugins)
- [ ] Quarterly external data refresh (check all sources for changes)
- [ ] Quarterly architecture audit (check for new supersessions, orphaned frameworks)

---

## Quick Wins (Can Start Immediately)

1. **Add deprecation markers to eight-operator notes** (5 min)
   - Notes: Agatha Unified Skill System, DOTTIE, MOBI
   - Add: `status: deprecated`, `effective_date: 2026-03-01`, `superseded_by: [[HEPHAISTOS]]`

2. **Create External Data Registry** (30 min)
   - Two columns: Source | Last Checked | Next Check Date | Status
   - Seed with: Reddit API, GDPR, HIPAA, FINRA, ISO standards
   - Add to memory.md for visibility

3. **Run plugin determinism test** (10 min)
   - Three Dataview queries: count external data entries in wiki
   - Compare results; document as PASS/FAIL

4. **Draft migration guide for Eight Operators → Three Agent** (20 min)
   - Concept translation table
   - Decision re-mapping
   - Effective date range

---

## Open Questions for Monitoring Phase

1. **Vector search baseline:** What is the normal response time and result quality? What counts as "drift"?
2. **External data management:** Should we use Obsidian database or external spreadsheet for registry? (Obsidian: better integration; Spreadsheet: easier auditing)
3. **Refresh automation:** How should we detect policy changes? (Automated API checks? Manual weekly review? Hybrid?)
4. **Incident response:** If a control fails mid-governance decision, what's the escalation path? (Halt approval? Quarantine decision? Escalate to Operator?)
5. **Dashboard:** Should Layer 0.5 control status be visible in real-time, or only at decision time?

---

## Related

- [[Governance and PHAROS MOC]]
- [[OPEN RISKS — Three Governance Blindspots Requiring Recursive Control]] — source risk statement
- [[CONTROL 1 — Tool Layer Audit Protocol (Regulatory Grounding)]] — full control 1
- [[CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)]] — full control 2
- [[CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding)]] — full control 3
- [[Governance Controls Integration Dashboard]] — integration points

---

## Baseline Completion Checklist

- [x] Vector search tested
- [x] File system integrity verified
- [ ] Plugin determinism tested
- [ ] Tool dependency chain documented
- [ ] External data sources inventoried
- [ ] Refresh schedule proposed
- [x] Staleness detection identified (one source approaching)
- [ ] Supersession registry created
- [ ] Status markers applied to notes
- [ ] Migration guides drafted
- [ ] Monitoring plan defined

**Estimated completion of Phase 1:** ~2026-05-10 (2 weeks)
**Next major turn:** Major-turn review should include Phase 1 completion status
