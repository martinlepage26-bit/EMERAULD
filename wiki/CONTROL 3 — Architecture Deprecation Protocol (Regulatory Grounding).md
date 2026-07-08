---
type: governance-control
title: CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding)
aliases:
- Architecture Deprecation Protocol
- CONTROL 3
- wiki/CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding)
tags:
- governance-control
- wiki
- control-3-architecture-deprecation-protocol-regulatory-grounding-md
- architecture
- deprecated
- effective
- supersession
- eight
- color-purple
status: active
created: '2026-04-26'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding).md
backlink_count: 22
backlinks:
- '[[wiki/Agatha Unified Skill System — Eight Sovereign Operators]]'
- '[[wiki/CONTROL 1 — Tool Layer Audit Protocol (Regulatory Grounding)]]'
- '[[Areas/PHAROS/Control Protocols MOC]]'
- '[[wiki/D Library — Genealogy Flags and Cleanup Leads (2026-04-26)]]'
- '[[wiki/Documents Root Intake — Hermes Action Map 2026-04-28]]'
- '[[Areas/PHAROS/Governance Controls Integration Dashboard]]'
- '[[wiki/Governance Controls and Mechanisms]]'
- '[[wiki/Governance Controls — Baseline Assessment (2026-04-26)]]'
- '[[wiki/Governance Controls — Incident Response (Control Failure Procedures)]]'
- '[[wiki/Governance Controls — Monitoring Plan & Automation Roadmap]]'
- '[[wiki/Governance Controls — Phase 1 Completion Checklist]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/NIST AI RMF 1.0 — NIST AI 100-1 (2023)]]'
- '[[wiki/OPEN RISKS — Three Governance Blindspots Requiring Recursive Control]]'
- '[[wiki/OUTLIERS — Five Notes That Break the Architecture]]'
- '[[wiki/Personal and Projects MOC]]'
- '[[wiki/Provisional Arbitration Charter — Argus Layer 9.5]]'
- '[[Resources/Regulatory Standards Reference Stack — Governance Controls Grounding]]'
- '[[wiki/Supersession Registry]]'
- '[[archive/session-state/session-state-001]]'
- '[[maps/PHAROS Method Map]]'
- '[[memory]]'
tier: critical
regulatory-anchors:
- ISO 15489
- ITIL Change Management
- NIST SP 800-53
- SOX
- HIPAA
---

# CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding)

## Summary

Governance frameworks evolve, but old architectures remain discoverable in knowledge graphs without clear deprecation, creating confusion about what is current vs. historical. [[OPEN RISKS — Three Governance Blindspots Requiring Recursive Control|Risk 3]] requires a protocol to mark superseded architectures, create migration paths, and prevent accidental re-adoption of deprecated methods. This note grounds the control in records management, change control, and compliance standards.

## Regulatory Foundation

### ISO 15489:2016 — Records Management

**Core Principle — Authenticity and Reliability:**
Records systems must demonstrate that records are what they purport to be, and that they are reliable evidence of the actions/decisions they document. This requires **clear dating and versioning of all records**.

**Applied to governance:**
- Governance frameworks are records of decision authority. When frameworks change (eight-operator → three-agent), both versions must be discoverable, but readers must know which one was operative *at the time their decision was made*.
- Example: A governance decision made on 2026-02-01 under the eight-operator architecture is not invalid, but it's *different* from a decision made on 2026-05-01 under three-agent architecture. The record must preserve this distinction.

**ISO 15489 requires:**
- **Accession date**: When each framework version was adopted
- **Effective date**: When it became operative (may differ from adoption)
- **Supersession date**: When it was replaced, and by what
- **Retention schedule**: How long to keep the deprecated version (audit trail)
- **Disposition**: Where the deprecated version is stored (archive, not active decision-making)

**Regulatory Implication:** Superseded frameworks must be archived with clear dating and versioning, not deleted or left ambiguous.

---

### ITIL Change Management (Information Technology Infrastructure Library)

**Change Advisory Board (CAB) Process:**
ITIL requires that every change to IT infrastructure (which includes governance systems) be:
1. Logged and assessed
2. Evaluated for impact (what breaks if we change?)
3. Scheduled (when is the safe window?)
4. Authorized (does a CAB approve this?)
5. Implemented with rollback plan (what if it fails?)
6. Documented for audit trail (what changed and why?)
7. Reviewed post-implementation (did it work?)

**Applied to governance:**
- Moving from eight-operator to three-agent architecture is a **change to the governance system**.
- ITIL requires documentation of:
  - What changed (operator authority model → agent co-equal model)
  - Why it changed (evidence, rationale, pressure for change)
  - Who approved it (authorization, governance decision)
  - When it takes effect (effective date, not adoption date)
  - How users migrate (migration path, training, reference docs)
  - Rollback plan (if old architecture had to be restored)
  - Post-implementation review (did the new architecture work?)

**Regulatory Implication:** Architecture changes require formal change control. Deprecation isn't just "mark old as old"; it's a documented transition with migration support.

---

### NIST SP 800-53 — Control CM-3: Access Restrictions for Change

**CM-3(a) — Change Control:**
- Organizations must define, document, and implement procedures for the authorization and implementation of changes to information systems.
- **Security-relevant changes** (governance changes affecting decision authority) require enhanced review.

**CM-3(b) — Change Impact Analysis:**
- Changes must be assessed for:
  - **Functional impact**: Does governance still produce valid decisions?
  - **Security impact**: Does new architecture introduce new security risks?
  - **Backward compatibility**: Can old decisions be re-validated under new architecture?

**Applied to governance:**
- Moving from eight-operator to three-agent impacts:
  - Authority model (who decides what? changed)
  - Binding principles (what's non-negotiable? expanded)
  - Escalation paths (who do conflicts go to? changed)
  - Each of these is security-relevant because they affect approval authority.

**Regulatory Implication:** Architecture changes must include functional and security impact analysis before adoption.

---

### SOX § 404 — Internal Control Assessment

**SOX § 404(b) — Auditor Assessment:**
- External auditors must evaluate whether management has maintained effective internal controls.
- When governance architecture changes, that's a **change to internal controls**.
- Auditors must understand:
  - What changed?
  - Why did it change?
  - Is the new architecture more effective, equally effective, or less effective than the old one?
  - Are there any transition risks (period where neither old nor new is fully in place)?

**Applied to governance:**
- If PHAROS governance architecture changes, SOX audit scope must include:
  - Effectiveness of old vs. new
  - Transition risks during changeover
  - Documentation that old decisions remain valid (audit trail doesn't break)

**Regulatory Implication:** Architecture changes must be documented with effectiveness assessment. Transition period requires dual documentation (old and new co-existing).

---

### HIPAA — Business Associate Agreements and Control Documentation

**45 CFR § 164.308(a)(7) — Business Associate Contracts:**
- Covered entities must have contracts specifying what controls the business associate will maintain.
- If a business associate changes their governance architecture, **they must notify the covered entity** (because controls changed).

**Applied to governance:**
- If governance architecture changes, all stakeholders relying on that governance (clients, regulated entities using PHAROS) must be notified.
- Notifications must document:
  - Old architecture (what they relied on)
  - New architecture (what they now rely on)
  - Effectiveness comparison (is the new one more trustworthy, or different?)
  - Timeline (when does the change take effect for their decisions?)

**Regulatory Implication:** Architecture changes are not internal refactors. They're stakeholder-facing controls changes that require disclosure.

---

## The Deeper Mechanism: Why Do Superseded Methods Remain Discoverable?

**The structural problem:** Knowledge graphs optimize for *connectivity and discoverability*. Both the eight-operator and three-agent architectures are discoverable because they're linked. But discoverability doesn't distinguish between "current" and "historical." Readers have to infer which one to use.

**Regulatory answer (ISO 15489 + ITIL + NIST CM-3):** Superseded methods must be discoverable *with their effective dates and supersession information*. The distinction is not "discoverable vs. hidden"; it's "discoverable with clear status markers."

**This means:** Governance systems need:
1. A supersession registry mapping old → new with effective dates
2. Clear status markers on each architectural note: `status: current | deprecated | archived`
3. Migration guides showing how to translate old architecture decisions to new architecture
4. Dual documentation during transition period (old and new both operative, clearly marked)

---

## Control Mechanism

### Supersession Registry

**Central record of all framework version changes:**

```yaml
Supersession Chain: Governance Authority Models

Entry 1:
  Old Architecture: Eight Sovereign Operators (Agatha, DOTTIE, MOBI v1, v2, v3, etc.)
  New Architecture: Three-Agent Stack (HEPHAISTOS, Queen Keyport, Hermes)
  Effective Date: 2026-03-01
  Adoption Date: 2026-02-15 (internal review cycle)
  Supersession Date: 2026-03-01 (effective with new decisions)
  Rationale: "Evidence showed authority conflicts between eight operators. Three-agent co-equal model reduces conflict surface."
  Impact Assessment:
    - Functional: New model resolves 4 of 8 identified decision bottlenecks
    - Security: Authority conflicts reduced; approval gates tightened
    - Backward Compatibility: Old decisions remain valid (they were made under approved framework at the time)
  Migration Path: "Translate eight-operator decisions to three-agent equivalents using [[Architecture Translation Guide]]"
  Approved By: Martin Lepage (Operator)
  ITIL CAB Sign-off: Complete
  SOX Impact: Internal control enhancement; new architecture adds co-equal checks
  Notification Status: All stakeholders notified 2026-02-20
  Search Mode: `current-only` excludes Eight-Operator architecture; `full-history` includes it with `deprecated` flag

Entry 2:
  Old Architecture: Three-Agent Stack (Linear Authority Chain)
  New Architecture: Three-Agent Stack (Co-Equal Authority)
  Effective Date: 2026-04-23
  Adoption Date: 2026-04-20
  Supersession Date: 2026-04-23
  Rationale: "Initial three-agent had embedded hierarchy. Co-equal model discovered during Diamond-Eyes audit."
  Impact Assessment:
    - Functional: Same routing, different conflict resolution (improves governance by removing false hierarchy)
    - Security: No change to authority gates; improves clarity
    - Backward Compatibility: Decisions under old hierarchy remain valid; old hierarchy was error, not intentional
  Migration Path: "No translation needed; framework name and entrypoint unchanged; only internal authority model clarified"
  Approved By: Martin Lepage (Operator), endorsed by Queen Keyport
  ITIL CAB Sign-off: Complete
  SOX Impact: Internal control clarification (no new controls added, hierarchy error corrected)
  Notification Status: All stakeholders notified 2026-04-21
  Search Mode: Both versions return same entrypoint; old linear model marked `deprecated` in historical references only
```

---

### Status Marking System

**Every framework, method, and architecture note must have a status field:**

```yaml
status: current | deprecated | archived | experimental | superseded_by
```

**Usage:**

| Status | Meaning | Discoverability | Use in Decisions | Retention |
|---|---|---|---|---|
| `current` | Active, operative framework | High (default search) | Yes, only current version | Indefinite (active) |
| `deprecated` | Superseded, but still referenced | Medium (search with flag) | No (but marked as used in old decisions) | Indefinite (audit trail) |
| `archived` | Historical reference only | Low (search full-history mode) | No (for context only) | Indefinite (audit trail) |
| `experimental` | Trial/prototype, not yet operative | Low (search requires opt-in) | No (not ready for decisions) | Until status changes |
| `superseded_by` | Points to current replacement | Redirects to current | No (links to current) | Indefinite (audit trail) |

**Example marking:**

```yaml
# Eight Sovereign Operators note
status: deprecated
superseded_by: [[HEPHAISTOS]]
effective_date: 2026-03-01
deprecation_notice: |
  This architecture was superseded by the three-agent stack 
  effective 2026-03-01. Decisions made under this architecture
  before that date remain valid. New decisions must use [[HEPHAISTOS]].
migration_guide: [[Architecture Translation Guide]]
```

---

### Migration Guide Structure

**For each supersession, create a migration guide:**

**Filename:** `Architecture Translation Guide — [Old] to [New].md`

**Contents:**

1. **Supersession summary** — what changed and why
2. **Concept translation table** — how old concepts map to new
3. **Decision re-mapping** — how old decisions should be understood under new architecture
4. **Authority re-routing** — who decides what under new vs. old
5. **Escalation path changes** — how conflicts are resolved differently
6. **Effective dates** — when old vs. new applies
7. **Transition period** — if both operate simultaneously, how to distinguish

**Example: Eight Operators → Three-Agent:**

| Concept | Old (Eight-Operator) | New (Three-Agent) | Translation |
|---|---|---|---|
| **Authority for scope** | AGATHA (Agatha decides what exists) | HEPHAISTOS (what is being built) | Same function; different agent name |
| **Authority for constraints** | DOTTIE (DOTTIE decides what's permitted) | Queen Keyport (what controls apply) | Same function; different agent name |
| **Conflict resolution** | 8-way arbitration (slow, ambiguous) | Operator arbitration with co-equal submission (faster, clear) | Process improvement |
| **Escalation** | To MOBI (meta-operator) | To Operator directly | Flatter hierarchy |

---

### Transition Period Documentation

**When old and new architectures overlap (during adoption):**

All governance decisions must note:
- **Which architecture was operative** at decision time: `_under_architecture: eight-operator` or `_under_architecture: three-agent`
- **Effective date range**: `2026-02-15 to 2026-03-01: old architecture`. `2026-03-01 onward: new architecture`
- **If retroactive changes are needed**: note what decision would be different under new architecture

---

### Integration Points

### [[HEPHAISTOS]] Scope Extension
> Governance must maintain a supersession registry and mark all superseded architectures with effective dates, migration paths, and status. Readers must be able to distinguish current from historical without ambiguity.

### [[Queen Keyport]] Approval Gate (New Criterion)
**Before approval:**
- [ ] Decision cites only `current` or `experimental` architecture
- [ ] If using experimental: decision is explicitly bounded (`ready_with_bounded_gaps` or lower)
- [ ] Deprecation notice created for any architecture being superseded
- [ ] Migration guide exists (if supersession is major)

### [[Hermes]] Routing Rule (New Validation)
Routes governance decisions only if they cite current architecture. If decision references deprecated architecture without explicit temporal scoping (old decision from old era), Hermes escalates for clarification.

### [[Argus]] Audit Layer
Audit questions:
- "Which architectures are currently operative?"
- "Are there orphaned architectures (not clearly superseded)?"
- "Can readers distinguish current from deprecated without domain expertise?"
- "Are all recent decisions using current architecture?"

---

## Success Metrics

- **Zero confusion cases** where readers can't identify current vs. deprecated architecture within 5 minutes
- **100% of superseded architectures** clearly marked with supersession date and successor
- **100% of architecture changes** documented with ITIL CAB sign-off and SOX impact assessment
- **All stakeholders notified** of architecture changes within 1 week of effective date
- **Migration guides complete** before any new decisions cite the new architecture

---

## Related

- [[OPEN RISKS — Three Governance Blindspots Requiring Recursive Control]] — source risk statement
- [[Agatha Unified Skill System — Eight Sovereign Operators]] — deprecated architecture (example)
- [[HEPHAISTOS]] — current operative architecture
- [[PHAROS Method — Technical Reference]] — governance pipeline with version history
- [[CONTROL 1 — Tool Layer Audit Protocol|Tool Layer Audit]] — parallel control mechanism
- [[ISO 15489 Records Management Standard]] — regulatory foundation
- [[ITIL Change Management Process]] — change control foundation
- [[NIST SP 800-53 CM-3 Change Control and Authorization]] — security controls foundation
- [[Provisional Arbitration Charter — Argus Layer 9.5]] — apex-conflict route if architecture supersession and current governance claims collide

---

- [[The Market Impact Question]]
- [[if-gov-ai-2027-2028]]
## Open Questions for Next Major Turn

1. Are there any orphaned or partially-superseded architectures that should have been deprecated but weren't?
2. Have all stakeholders been notified of recent architecture changes?
3. Are there any governance decisions in flight that cite deprecated architecture?
4. What should the policy be for "experimental" architectures? How long can they stay experimental before they either become current or are archived?
