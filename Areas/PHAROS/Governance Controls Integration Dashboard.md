---
type: governance-dashboard
title: Governance Controls Integration Dashboard
aliases:
- GOVERNANCE CONTROLS INTEGRATION DASHBOARD
tags:
- governance-dashboard
- areas
- governance-controls-integration-dashboard-md
- control
- external
- approval
- controls
- tool
- color-purple
status: active
created: '2026-04-26'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/Governance Controls Integration Dashboard.md
backlink_count: 21
backlinks:
- '[[wiki/Agatha Unified Skill System — Eight Sovereign Operators]]'
- '[[Areas/PHAROS/Architecture Translation Guide — Eight Operators to Three-Agent Stack]]'
- '[[Areas/PHAROS/Control Protocols MOC]]'
- '[[wiki/Documents Root Intake — Hermes Action Map 2026-04-28]]'
- '[[wiki/External Data Refresh Calendar — Phase 1 Build]]'
- '[[wiki/Governance Controls and Mechanisms]]'
- '[[wiki/Governance Controls — Baseline Assessment (2026-04-26)]]'
- '[[wiki/Governance Controls — Incident Response (Control Failure Procedures)]]'
- '[[wiki/Governance Controls — Monitoring Plan & Automation Roadmap]]'
- '[[wiki/Governance Controls — Phase 1 Progress Checkpoint (2026-04-26)]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Areas/PHAROS/MCP and Runtime Integration MOC]]'
- '[[wiki/OUTLIERS — Five Notes That Break the Architecture]]'
- '[[wiki/Plugin Recommendations]]'
- '[[wiki/Provisional Arbitration Charter — Argus Layer 9.5]]'
- '[[wiki/Regulatory Standards Reference Stack — Governance Controls Grounding]]'
- '[[wiki/Root Loose Notes Cluster Map — 2026-05-06]]'
- '[[wiki/Supersession Registry]]'
- '[[archive/session-state/session-state-001]]'
- '[[maps/PHAROS Method Map]]'
- '[[memory]]'
tier: critical
---

# Governance Controls Integration Dashboard

## Summary

Three regulatory-grounded controls now integrate into the [[PHAROS Method — Technical Reference|PHAROS governance pipeline]] to audit governance itself. The three controls — [[CONTROL 1 — Tool Layer Audit Protocol (Regulatory Grounding)|Control 1 (Tool Layer)]], [[CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)|Control 2 (External Data)]], and [[CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding)|Control 3 (Architecture Deprecation)]] — close three of the five gaps identified in [[OUTLIERS — Five Notes That Break the Architecture]] and address the risk statement in [[OPEN RISKS — Three Governance Blindspots Requiring Recursive Control]]. This dashboard shows: (1) how the three controls work together, (2) integration points in the [[HEPHAISTOS|Hephaistos]] / [[Queen Keyport|Queen Keyport]] / [[Hermes|Hermes]] three-agent stack, (3) regulatory anchors, (4) success metrics, and (5) major-turn review checklist.

## The Three Controls (Integrated System)

```
┌─────────────────────────────────────────────────────────────────┐
│                    GOVERNANCE DECISION PIPELINE                 │
│  (PHAROS Stages 1-10: Corpus → Promotion)                      │
└─────────────────────────────────────────────────────────────────┘
                              ↑
                              │ approval required
                              │
┌─────────────────────────────────────────────────────────────────┐
│                 LAYER 0.5 PRE-APPROVAL GATE                     │
│             (Three Controls Operate in Parallel)                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  CONTROL 1: Tool Layer         CONTROL 2: External Data        │  CONTROL 3: Architecture
│  Audit Protocol                Lifecycle Protocol              │  Deprecation Protocol
│  ─────────────────────────────────────────────────────────────│
│  ✓ Vector search coherent?     ✓ All external data current?   │  ✓ Using current/experimental
│  ✓ File system intact?         ✓ Nothing quarantined?         │    architecture only?
│  ✓ Plugins deterministic?      ✓ Policy versions documented?  │  ✓ No deprecated methods?
│  ✓ Tool dependencies valid?    ✓ Refresh schedule maintained? │  ✓ Supersession clear?
│  ✓ Governance arch current?    ✓ Staleness detected early?    │  ✓ Migration path available?
│                                                                 │
│  Grounded in:                  Grounded in:                    │  Grounded in:
│  - COBIT 5 (DSS01, DSS02)      - GDPR Article 5               │  - ISO 15489
│  - SOC 2 Type II (CC6.1-6.2)   - CCPA (data minimization)    │  - ITIL Change Management
│  - ISO 27001 (A.8.6, A.15.1)   - HIPAA (45 CFR 164.316)     │  - NIST SP 800-53 (CM-3)
│  - NIST SP 800-53 (CA-7)       - FINRA Rule 4530              │  - SOX § 404
│                                - ISO 9001 (Doc Control)       │  - HIPAA (BAA)
│                                - SOX § 302                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              ↓ all pass
                    ✓ LAYER 0.5 CLEARED
                              ↓
            HEPHAISTOS & QUEEN KEYPORT PROCEED
                              ↓
                    GOVERNANCE APPROVAL ISSUED
                              ↓
            HERMES ROUTES (if post-approval conditions stable)
```

---

## How the Controls Reinforce Each Other

### Sequence: Dependency Chain

**Control 1 → Control 2 → Control 3 → Back to Control 1**

```
Control 1 validates: Are the tools that discover external data (vector search, file system) valid?
    ↓
Control 2 depends on valid tools: External data registry must be discoverable via vector search,
                                  file system integrity ensures policy snapshots aren't corrupted.
    ↓
Control 3 validates: Are the tools that distinguish current vs. deprecated architectures valid?
                     (Deprecation markers in file system, discoverable via vector search)
    ↓
Back to Control 1: If deprecation chain can't be validated, tool layer is at risk.
```

**If any control fails, the chain breaks:**
- Tool failure → external data becomes undiscoverable or corrupted → architecture changes can't be tracked
- External data failure → governance decisions made on stale policy → old architectures appear valid
- Deprecation failure → readers can't tell what's current → old tools/policies re-adopted by accident

---

## Integration into the Three-Agent Stack

### HEPHAISTOS (Scope & Forging)

**New Scope Boundaries:**
- Governance must define and audit its own infrastructure dependencies (tools, external data, architecture versions)
- Forging phase includes documenting:
  - What tools are required? (vector search, file system, plugins)
  - What external policy governs the artifact? (GDPR, API terms, compliance frameworks)
  - What architecture is this artifact being built under? (current, experimental, or deprecated)

**Hephaistos Questions:**
- What is the artifact being forged? → requires valid tools (Control 1) + current policy (Control 2) + current architecture (Control 3)

---

### Queen Keyport (Governance & Controls)

**New Approval Gate — Layer 0.5:**

**Before Queen Keyport issues any approval:**

```yaml
Approval Checklist:

CONTROL 1 — Tool Layer (REQUIRED)
  - [ ] Vector search returns coherent results for governance-relevant queries
  - [ ] File system integrity verified (all governance boundary files accessible)
  - [ ] All plugins used in governance path tested for determinism
  - [ ] Tool dependency chain documented (what breaks if tool X fails?)
  - [ ] Tool changes logged (what changed since last review?)
  Decision: ☐ Pass ☐ Fail (halt approval)

CONTROL 2 — External Data (REQUIRED)
  - [ ] All external policy cited in decision is in registry (source, clipping date, expiry)
  - [ ] No cited external data is quarantined (all are "current" status)
  - [ ] Policy versions match governance record (haven't drifted since snapshot)
  - [ ] Refresh schedule maintained (next check date set)
  - [ ] If policy near expiry, governance bounded accordingly
  Decision: ☐ Pass ☐ Fail (halt approval)

CONTROL 3 — Architecture (REQUIRED)
  - [ ] Supersession registry confirms all cited frameworks are current or experimental
  - [ ] No deprecated architecture used without explicit temporal scoping
  - [ ] If new architecture, migration guides exist for any deprecation
  - [ ] Architecture status clearly marked (current | deprecated | archived)
  Decision: ☐ Pass ☐ Fail (halt approval)

FINAL DECISION:
  ☐ Approve (all three controls passed)
  ☐ Approve with bounded gaps (name which gaps, which controls triggered)
  ☐ Block (name which control failed, why, what must be fixed)
```

**Queen Keyport Authority:**
- Layer 0.5 gate is non-exceptionable. Even if governance logic is sound, if Layer 0.5 fails, approval is blocked.
- No compensating control can bypass Layer 0.5 pre-approval.

---

### Hermes (Routing & Escalation)

**New Routing Rule:**

```yaml
Condition 1: All Layer 0.5 controls passed at approval time?
  └─ No: Escalate to Operator (can't route)
  └─ Yes: Continue to Condition 2

Condition 2: Since approval, have any Layer 0.5 conditions changed?
  └─ Tool layer degraded? (vector search drift, file loss)
  └─ External policy changed? (refresh cycle triggered staleness)
  └─ Architecture changed? (new deprecation introduced)
  └─ Any Yes: Escalate to Operator (halt routing pending re-approval)
  └─ All No: Route governance decision

Post-Route Monitoring:
  Monitor tool layer, external policy, architecture status continuously.
  If drift detected post-routing, halt execution and escalate.
```

---

### Argus (Meta-Governance Audit)

**New Layer — Layer 0.5 Audit:**

Layer 0.5 inserted before L1 (claims and boundary) audit:

```yaml
Layer 0.5 — Meta-Governance Coherence (NEW)

Questions:
1. Is Control 1 (Tool Layer) working?
   - Are tool failures detected before governance approval?
   - Are cascade analyses complete (tool X fails → what governance breaks)?
   - Failure finding: Tool layer audit is inadequate
   
2. Is Control 2 (External Data) working?
   - Are external policy changes detected on schedule?
   - Are stale policies caught before they affect decisions?
   - Are all external data dependencies inventoried?
   - Failure finding: External data is not actively managed
   
3. Is Control 3 (Architecture) working?
   - Are superseded architectures clearly marked?
   - Are migration paths available?
   - Are readers confused about current vs. deprecated?
   - Failure finding: Deprecation protocol is not working

4. Are the three controls working together?
   - If Control 1 fails (tool), do Controls 2 and 3 also fail? (dependency chain test)
   - If Control 2 fails (external data), is Control 1 aware? (integration test)
   - If Control 3 fails (architecture), do 1 and 2 correct?  (feedback test)
   - Failure finding: Controls are isolated, not integrated

Finding Escalation:
  - Any Layer 0.5 failure = all downstream layers (L1-L5) halted
  - Layer 0.5 findings escalate directly to Operator (not reviewed at L1-L5)
  - Before any promotion, Layer 0.5 must be cleared
```

---

## Regulatory Mapping

### Control 1 Regulatory Anchors

| Standard | Section | Implication |
|---|---|---|
| COBIT 5 | DSS01.02 | All IT operations executed in controlled manner; failures detected and corrected |
| SOC 2 Type II | CC6.1-6.2 | Quality information about control execution; roles/responsibilities explicit |
| ISO 27001 | A.8.6, A.15.1 | Crypto changes invalidate prior decisions; tool security must be verified continuously |
| NIST SP 800-53 | CA-7 | Continuous monitoring of control implementation; organizational-defined metrics required |

**Compliance Test:** "Is governance auditing the infrastructure that makes governance possible?"

---

### Control 2 Regulatory Anchors

| Standard | Section | Implication |
|---|---|---|
| GDPR | Article 5(1)(a), (d) | Data must be processed under current rules; accuracy maintained with reasonable steps |
| CCPA | § 1798.100(d) | Data minimization: retain external policy only while actively needed |
| HIPAA | 45 CFR § 164.316(b) | Document retention for 6 years; governance rules must cite effective date |
| FINRA | Rule 4530 | Maintain records of specific regulatory standard applied to each decision |
| ISO 9001 | § 7.5 | Documented information controlled; obsolete documents prevented from unintended use |
| SOX | § 302, § 404 | Internal controls effectiveness must be disclosed; significant changes must be recorded |

**Compliance Test:** "Is governance using current external policy, or has policy changed?"

---

### Control 3 Regulatory Anchors

| Standard | Section | Implication |
|---|---|---|
| ISO 15489 | Records Management | Clear dating and versioning of all records; supersession tracked with effective dates |
| ITIL | Change Advisory Board | All system changes logged, assessed, authorized, scheduled, implemented, documented, reviewed |
| NIST SP 800-53 | CM-3 | Change control procedures required; impact analysis for security-relevant changes |
| SOX | § 404 | Internal control effectiveness assessed; significant control changes must be disclosed |
| HIPAA | 45 CFR § 164.308 | Business associate agreements specify controls; control changes require stakeholder notification |

**Compliance Test:** "Is governance tracking which architecture version was operative at decision time?"

---

## Success Metrics

### Control 1 Metrics
- **Zero silent tool failures** beyond one review cycle (detect before 2+ governance decisions made)
- **100% of tool assumptions documented** in governance approval record
- **Tool audit time < 10% of governance decision time** (must not become a bottleneck)
- **Cascade analysis complete** for all tools used in governance path

### Control 2 Metrics
- **Zero governance decisions made using stale external policy** within one review cycle of policy change
- **100% of external data tracked** in registry with source, clipping date, refresh schedule
- **Staleness detection** catches all policy changes before they affect 3+ downstream decisions
- **External data audit time < 5% of governance decision time**

### Control 3 Metrics
- **Zero confusion cases** where readers can't identify current vs. deprecated within 5 min of reading
- **100% of superseded architectures** clearly marked with supersession date and successor
- **100% of architecture changes** documented with ITIL CAB sign-off and SOX impact assessment
- **All stakeholders notified** of architecture changes within 1 week of effective date

### System-Level Metric
- **Layer 0.5 approval time < 15 minutes** (all three controls run in parallel; 5 min per control is target)

---

## Major-Turn Review Checklist

**Every major governance decision or session close, review:**

### Tool Layer (Control 1)
- [ ] What infrastructure changes happened since last review? (updates, migrations, new tools)
- [ ] Did any tool fail silently? (vector search drift, file loss, plugin non-determinism)
- [ ] Are tool dependencies documented and cascade-analyzed?
- [ ] Is tool health being monitored continuously?

### External Data (Control 2)
- [ ] Which external policies changed since last review? (check refresh calendar)
- [ ] Are we still operating under current versions of all cited policies?
- [ ] Did any governance decision use stale policy without knowing it?
- [ ] Are external data dependencies inventoried and versioned?

### Architecture (Control 3)
- [ ] Did we introduce new architectures without clear deprecation of old ones?
- [ ] Are there orphaned frameworks (not clearly superseded)?
- [ ] Can readers distinguish current vs. deprecated within 5 minutes?
- [ ] Have all stakeholders been notified of recent architecture changes?

### System Integration
- [ ] Do all three controls work together as expected?
- [ ] If one control failed, did the others catch the breakdown?
- [ ] Are there new dependencies between controls?
- [ ] Do we need to update integration points?

---

## Next Major-Turn Actions

1. **Run Layer 0.5 on current state:** Test all three controls against current governance corpus
2. **Document baseline:** What is the state of tool layer, external data, architecture as of 2026-04-26?
3. **Set refresh calendar:** Schedule all Control 2 (external data) refresh checks
4. **Create monitoring dashboard:** Track control status in real time
5. **Notify stakeholders:** Announce Layer 0.5 gate and new approval requirements

---

## Related

- [[OPEN RISKS — Three Governance Blindspots Requiring Recursive Control]] — risk statement
- [[CONTROL 1 — Tool Layer Audit Protocol (Regulatory Grounding)]] — full control 1
- [[CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)]] — full control 2
- [[CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding)]] — full control 3
- [[PHAROS Method — Technical Reference]] — governance pipeline these controls protect
- [[HEPHAISTOS]] — scope agent; defines what governance controls apply
- [[Queen Keyport]] — governance authority; issues approvals at Layer 0.5
- [[Hermes]] — routing; validates controls before promoting decisions
- [[Argus]] — audit; audits whether controls are working
- [[Provisional Arbitration Charter — Argus Layer 9.5]] — provisional rule for authority conflicts not resolved cleanly by existing controls

---

- [[Plugin Recommendations]]
## Open Questions for Next Major Turn

1. **Baseline state:** What is the current state of each control? (all passing? any failing?)
2. **Automation:** Which control checks can be automated vs. which require manual review?
3. **Monitoring:** What's the right cadence for checking each control? (real-time? daily? weekly?)
4. **Stakeholder communication:** Who needs to know about Layer 0.5? (clients, team, board?)
5. **Incident response:** If Layer 0.5 fails, what's the escalation path and incident response?
