---
type: governance-risk
title: OPEN RISKS — Three Governance Blindspots Requiring Recursive Control
aliases:
- OPEN RISKS
- Open Risks
- Open Risks — Three Governance Blindspots Requiring Recursive Control
- wiki/OPEN RISKS — Three Governance Blindspots Requiring Recursive Control
tags:
- governance-risk
- wiki
- open-risks-three-governance-blindspots-requiring-recursive-control-md
- deprecation
- control
- tool
- external
- supersession
- color-purple
status: active
created: '2026-04-26'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/OPEN RISKS — Three Governance Blindspots Requiring Recursive
  Control.md
backlink_count: 17
backlinks:
- '[[.trash/Building Your First AI Agent with OpenAI__________]]'
- '[[Areas/PHAROS/CONTROL 1 — Tool Layer Audit Protocol (Regulatory Grounding)]]'
- '[[Areas/PHAROS/CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)]]'
- '[[Areas/PHAROS/CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding)]]'
- '[[Areas/PHAROS/Control Protocols MOC]]'
- '[[archive/wiki-2026-07-08/Documents Root Intake — Hermes Action Map 2026-04-28]]'
- '[[Areas/PHAROS/Governance Controls Integration Dashboard]]'
- '[[wiki/Governance Controls and Mechanisms]]'
- '[[archive/wiki-2026-07-08/Governance Controls — Baseline Assessment (2026-04-26)]]'
- '[[wiki/Governance Controls — Incident Response (Control Failure Procedures)]]'
- '[[archive/wiki-2026-07-08/Governance Controls — Phase 1 Progress Checkpoint (2026-04-26)]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/OUTLIERS — Five Notes That Break the Architecture]]'
- '[[wiki/Provisional Arbitration Charter — Argus Layer 9.5]]'
- '[[Resources/Regulatory Standards Reference Stack — Governance Controls Grounding]]'
- '[[archive/session-state/session-state-001]]'
- '[[maps/PHAROS Method Map]]'
risk-level: high
review-cycle: major-turn
---

# OPEN RISKS — Three Governance Blindspots Requiring Recursive Control

## The Three Critical Gaps

Identified from [[OUTLIERS — Five Notes That Break the Architecture]]. These are not design flaws; they are **structural blindspots in how governance audits itself**. Each requires continuous monitoring, loop-based analysis, and active control implementation.

---

## RISK 1: Tool Layer Transparency

**What it is:** Governance frameworks depend on infrastructure (vector search, plugins, linking discipline, file systems) that the governance layer cannot audit.

**Evidence:** [[Plugin Recommendations]] — isolated utility note with no governance links. PHAROS can audit content, but not the tools that make content discoverable.

**Why it matters:** If tools fail silently, the entire governance system operates on corrupted inputs without knowing it. A broken vector search returns wrong answers; governance audits them as coherent. The system becomes self-validating fiction.

**Control needed:**
- [ ] Quarterly audit: "What layers support governance but aren't governed?"
- [ ] Dependency map: Tool failures → governance failures (cascade analysis)
- [ ] Tool health checks: Vector store coherence, plugin stability, file system integrity
- [ ] Escalation trigger: If any tool layer shows drift, halt governance promotion until tool is re-audited

**Loop process:**
1. Identify tool dependencies (what governs governance?)
2. Test tool assumptions (does vector search still work as expected?)
3. Detect silent failures (are there undetected tool drifts?)
4. Implement controls (add tool health checks to governance gates)
5. Reassess at next major turn (did controls catch the next failure?)

**Review trigger:** Every major code/infrastructure change, every 6 months minimum

---

## RISK 2: External Data Rot Without Refresh Protocol

**What it is:** Governance systems ingest external policy/data (Reddit API terms, compliance frameworks, vendor specs) with expiry dates, but have no mechanism to refresh, expire, or detect staleness.

**Evidence:** [[Reddit Data API — Access Terms and Rate Limits]] — policy snapshot marked "potentially stale," clipped 2026-04-20, supporting a product that doesn't exist. Once external data lands in the vault, "the vault itself is regulated storage"—but there's no protocol to keep it current.

**Why it matters:** Stale external policy can be used to make governance decisions (recommend data collection under old GDPR rules, advise on API access under outdated terms). The governance system can be internally coherent while being externally illegal.

**Control needed:**
- [ ] External data registry: Every ingested policy/spec labeled with authoritative source, clipping date, expected expiry
- [ ] Refresh triggers: Scheduled checks (quarterly for fast-moving policy like Reddit, annually for stable frameworks)
- [ ] Staleness detection: Automated checks against live sources; flag if source document has changed
- [ ] Quarantine protocol: If external data is out of date, flag it as "not for decision-making" in governance
- [ ] Deprecation marking: Stale external data marked as historical/reference-only, not operative

**Loop process:**
1. Inventory external data (what external policy have we ingested?)
2. Establish refresh cadence (how often does each policy actually change?)
3. Check against live source (is our snapshot still accurate?)
4. Detect drift (what changed that we need to know about?)
5. Update governance decisions if needed (do we need to revise recommendations?)
6. Reassess at major turn (did we catch policy changes that would have affected decisions?)

**Review trigger:** Quarterly for fast-moving policy (API, regulatory), annually for stable frameworks, immediately on known policy change

---

## RISK 3: Supersession Without Deprecation

**What it is:** Governance frameworks evolve, but old architectures remain discoverable in the knowledge graph without clear deprecation, creating confusion about what is current vs. historical.

**Evidence:** [[Agatha Unified Skill System — Eight Sovereign Operators]] coexists with [[HEPHAISTOS]] without clear marking that one supersedes the other. Two authority models compete in the graph; future readers won't know which to follow.

**Why it matters:** Governance decisions made using superseded architectures will be wrong. A client following eight-operator logic in a three-agent system creates authority conflicts. The vault contains both methods as if they're equivalent choices.

**Control needed:**
- [ ] Supersession registry: Track which methods/frameworks supersede which others, with effective dates
- [ ] Deprecation marking: All superseded architectures tagged as "deprecated as of [date], use X instead"
- [ ] Canonical current version: Every domain (agents, methods, frameworks) has a single "current" entry; others are historical
- [ ] Migration guide: If old method is referenced, automatically surface migration path to current method
- [ ] Search filtering: Vector search optionally excludes deprecated architectures (search mode: current-only vs. full-history)

**Loop process:**
1. Identify architectural changes (when does a method get superseded?)
2. Map supersession chain (what replaced what, and when?)
3. Mark all predecessors (tag old architectures with deprecation date and successor)
4. Test for confusion (can readers clearly see what's current?)
5. Update references (do all new decisions cite current architecture?)
6. Reassess at major turn (did we catch supersessions that created confusion?)

**Review trigger:** Every major methodological revision, every 6 months minimum, before any governance decision that relies on historical context

---

## Implementation Roadmap

### Phase 1: Risk Documentation (Complete)
- [x] Identify the three critical gaps
- [x] Document evidence from outliers
- [x] Articulate control requirements
- [x] Define loop processes

### Phase 2: Control Infrastructure (Complete)
- [x] **Tool Layer Transparency:** [[CONTROL 1 — Tool Layer Audit Protocol (Regulatory Grounding)|Control 1 - Tool Layer Audit Protocol]] — Layer 0.5 pre-gate; cascade failure analysis; grounded in COBIT, SOC 2, ISO 27001, NIST
- [x] **External Data Rot:** [[CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)|Control 2 - External Data Lifecycle Protocol]] — External data registry; refresh triggers; staleness detection; grounded in GDPR, CCPA, HIPAA, FINRA, SOX
- [x] **Supersession Clarity:** [[CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding)|Control 3 - Architecture Deprecation Protocol]] — Supersession registry; status marking; migration guides; grounded in ISO 15489, ITIL, NIST CM-3

### Phase 3: Integration into Governance Loop (In Progress)
- [x] Add three risks to [[HEPHAISTOS]] scope: "governance must audit its own infrastructure, policy boundaries, and deprecation chains"
- [x] Integrate tool health checks into [[Queen Keyport]] approval gates via Layer 0.5 pre-gate
- [x] Add external data freshness check to [[Hermes]] routing via quarantine protocol
- [ ] Create supersession audit as part of [[Argus]] seven-layer review (Layer 0.5 integration)
- [ ] Add all three controls to session-state and major-turn reassessment checklist
- [ ] Build dashboard showing control status (tool health, external policy versions, deprecation chain)

### Phase 4: Continuous Reassessment (Ongoing)
- Every major turn: Have the three gaps shifted? Have controls caught new instances?
- Quarterly minimum: Check tool layer, external policy, supersession chain
- Incident post-mortems: When governance failures occur, trace back through these three blindspots

---

## Integration Points

**[[HEPHAISTOS]] scope addition:**
> Governance must audit governance itself across three critical blindspots: the tool layers that make governance possible, the external policy boundaries that constrain governance, and the supersession chains that make old governance discoverable.

**[[Queen Keyport]] approval gate (Layer 0.5 pre-approval):**
> Before approving any governance decision:
> - Tool layer passed [[CONTROL 1 — Tool Layer Audit Protocol (Regulatory Grounding)|Control 1]] checks (vector search, file system, plugins, external policy audit, governance architecture)
> - External policy cited in decision is current per [[CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)|Control 2]] (not quarantined, not stale)
> - Decision uses only `current` or `experimental` architecture per [[CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding)|Control 3]] (not deprecated)
> - If any check fails: decision cannot be approved until preconditions are cleared

**[[Hermes]] routing rule:**
> Routes governance decisions only after all [[Queen Keyport]] approvals pass [[CONTROL 1 — Tool Layer Audit Protocol (Regulatory Grounding)|Control 1]], [[CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)|Control 2]], and [[CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding)|Control 3]] checks. If post-approval tool layer degrades, external policy changes, or architecture is deprecated, Hermes halts routing and escalates to Operator.

**[[Argus]] audit layer (Layer 0.5 audit):**
> New layer inserted before L1 (claims and boundary):
> - **Layer 0.5 — Meta-governance coherence:** Is governance auditing its own blindspots?
>   - Does [[CONTROL 1 — Tool Layer Audit Protocol (Regulatory Grounding)|Control 1]] catch tool layer failures?
>   - Does [[CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)|Control 2]] catch policy staleness?
>   - Does [[CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding)|Control 3]] prevent deprecated architecture reuse?
>   - Failure to audit meta-governance = Layer 0.5 blocker; all downstream layers fail

---

## Success Metrics

- **Tool Layer:** Zero silent tool failures go undetected beyond one review cycle
- **External Data:** Zero governance decisions made using stale external policy
- **Supersession:** Zero confusion cases where readers can't identify current vs. deprecated architecture within 5 minutes of reading

---

## Related

- [[OUTLIERS — Five Notes That Break the Architecture]] — source evidence
- [[DEEPER CONNECTIONS — The Triple Synthesis and the Governance Architecture]] — unified framework these risks test
- [[PHAROS Method — Recursive Governance]] — governance that must now govern itself
- [[Governance by Denial — Legibility, Capacity, Classification (Draft)]] — how systems fail to recognize their own blindspots
- [[HEPHAISTOS]] — primary agent responsible for managing these risks
- [[Queen Keyport]] — approval authority for control implementation
- [[Argus]] — audit responsibility for detecting risk slippage
- [[Provisional Arbitration Charter — Argus Layer 9.5]] — provisional apex-authority response when recursive controls conflict

---

- [[Building Your First AI Agent with OpenAI__________]]
- [[CONTROL ID MON-CORE-01]]
- [[2026 - CORE-01]]
- [[MartinLepage_AttackClassificationReport]]
## Open Questions for Next Major Turn

1. **Tool layer:** What infrastructure changes happened since last review? Did any tool fail silently?
2. **External policy:** Which external policies changed since last review? Are we still current?
3. **Supersession:** Did we introduce new architectures without clear deprecation of old ones? Are there orphaned frameworks?
