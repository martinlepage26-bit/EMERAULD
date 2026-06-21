---
type: governance-procedures
aliases: [GOVERNANCE CONTROLS — Incident Response (Control Failure Procedures)]
status: active
created: 2026-04-26
updated: 2026-04-26
tier: critical
---

# Governance Controls — Incident Response (Control Failure Procedures)

## Summary

When a governance control fails (Layer 0.5 check does not pass), the governance system must have clear escalation and remediation procedures. This document defines: (1) failure classification (severity levels), (2) escalation paths, (3) hold/release criteria, and (4) remediation procedures for each control.

---

## Failure Severity Classification

### P0 — Governance System Offline (Complete Control Failure)

**Definition:** A control fails such that governance decisions cannot be issued safely.

**Examples:**
- Vector search completely unavailable (Control 1)
- File system corruption affects governance boundary files (Control 1)
- All external data quarantined (Control 2)
- Governance architecture unclear / contradictory (Control 3)

**Immediate Action:**
1. Escalate to Operator immediately
2. Halt all governance approvals
3. Do NOT route any governance decisions
4. Begin remediation (see procedures below)

**Timeline:**
- Resolution must begin within 1 hour
- Full governance resumption within 4 hours (or escalate again)

---

### P1 — Critical Control Failure (Partial Degradation)

**Definition:** A control fails for a significant portion of governance work, but workarounds exist.

**Examples:**
- Vector search returns degraded results but is still operational (Control 1)
- One plugin non-deterministic; others work (Control 1)
- One external data source stale; others current (Control 2)
- One deprecated architecture referenced; others current (Control 3)

**Immediate Action:**
1. Flag the specific degradation to Operator
2. Do not approve new governance decisions that rely on the failed component
3. Existing approvals remain valid if they don't depend on the failed component
4. Begin remediation within 2 hours

**Timeline:**
- Workaround in place within 2 hours
- Full remediation within 24 hours

---

### P2 — Minor Control Failure (Degraded Performance)

**Definition:** A control shows warning signs but does not block governance operations.

**Examples:**
- Vector search performance slow (>5 sec response) but accurate (Control 1)
- External data refresh schedule approaching (not yet missed) (Control 2)
- One architecture note missing status field (not yet causing confusion) (Control 3)

**Immediate Action:**
1. Log the degradation
2. Governance approvals may continue
3. Schedule remediation within 1 week

**Timeline:**
- Remediation planned within 24 hours
- Fix deployed within 1 week

---

## CONTROL 1 — Tool Layer Failure Procedures

### Failure: Vector Search Degraded

**Symptom:** Vector search returns incoherent results, wrong relevance scores, or slow responses (>5 sec)

**Diagnosis:**
```
1. Verify sentence-transformer model load (check for CUDA/memory issues)
2. Test query against known good examples
3. Check if vault has grown past model capacity
4. Verify Elasticsearch/FAISS index not corrupted
```

**Severity:**
- Incoherent results (P0) → governance can't find relevant policies
- Slow but accurate (P2) → governance works, performance poor
- Partially degraded (P1) → some queries work, others fail

**Remediation:**
- **P0:** Rebuild vector index from scratch; revert to manual search (git grep) as fallback
- **P1:** Rebuild vector index; implement query caching to speed up common governance queries
- **P2:** Increase refresh frequency for vector index; monitor model performance

**Hold/Release Criteria:**
- Vector search may resume once: (1) queries against known governance concepts return coherent top-5 results, (2) response time < 3 sec, (3) five test queries pass

---

### Failure: File System Integrity Loss

**Symptom:** Governance boundary files inaccessible, corrupted, or lost (Control 2 registry, Control 3 deprecation marks, approval records)

**Diagnosis:**
```
1. Check file existence: ls /mnt/c/Users/softinfo/Documents/EMERAULD/wiki/CONTROL* GOVERNANCE*
2. Check corruption: file integrity hashes against backup
3. Check permissions: stat -c %a (must be readable)
4. Check mount status: mount | grep /mnt/c (WSL2 NTFS mount)
```

**Severity:**
- Governance approval records lost (P0) → audit trail broken
- Control registries inaccessible (P0) → Layer 0.5 cannot run
- Single policy snapshot missing (P1) → workaround to decision without that policy

**Remediation:**
- **P0:** Restore from git history; rebuild governance records from last known good state
- **P1:** Restore missing file from backup; restart governance process using checkpoint

**Hold/Release Criteria:**
- All governance boundary files restored, readable, and checksummed matching backup
- Git commit history shows no loss between last approved decision and recovery point

---

### Failure: Plugin Non-Determinism

**Symptom:** Same Dataview query returns different results on repeated runs

**Diagnosis:**
```
1. Run query 5 times in sequence
2. Compare outputs (row counts, column order, values)
3. Check for caching/stale-cache behavior
4. Verify Obsidian plugin version stability
```

**Severity:**
- One query non-deterministic (P1) → governance uses plugin output, output varies
- All Dataview results non-deterministic (P0) → governance records unreliable

**Remediation:**
- **P0:** Disable Dataview plugin; revert to manual counting/verification; fix plugin before re-enabling
- **P1:** Quarantine non-deterministic query; rebuild it without Dataview

**Hold/Release Criteria:**
- Plugin query passed determinism test: 5 identical runs with identical output

---

## CONTROL 2 — External Data Failure Procedures

### Failure: External Policy Stale (Beyond Refresh Date)

**Symptom:** Policy snapshot date is past its expected refresh date; live source may have changed

**Diagnosis:**
```
1. Check snapshot clipping date vs. next refresh date
2. Fetch live authoritative source (Reddit API docs, GDPR text, etc.)
3. Compute hash of live source
4. Compare to snapshot hash
5. If hash differs: policy changed
```

**Severity:**
- Policy changed and decision relies on old version (P1) → decision may be invalid
- Policy changed but decision doesn't rely on it (P2) → flag for record, no action required
- Multiple policies stale (P0) → governance based on unknown current rules

**Remediation:**
- **P1:** Quarantine old policy snapshot; ingest new version; re-assess governance decisions made under old policy
- **P2:** Ingest new version; update registry; mark old as archived
- **P0:** Halt governance approvals; refresh all external policy; re-approve decisions under new policy

**Hold/Release Criteria:**
- All external policy current (not past refresh date)
- Live sources re-verified as matching snapshots (or snapshots updated to current)
- Governance decisions re-assessed under current policy if policy change would affect outcome

---

### Failure: Policy Quarantine Blocks Governance

**Symptom:** All available versions of an external policy are quarantined; governance decision cannot proceed

**Diagnosis:**
```
1. Which policies are quarantined? Why?
2. Is there a previous known-good version available?
3. How long until new version can be obtained?
```

**Severity:**
- Can route around quarantine (use different policy or defer decision) (P2)
- Cannot proceed without this policy; decision must be deferred (P1)
- Multiple policies quarantined; governance halted (P0)

**Remediation:**
- **P2:** Document why decision deferred; schedule for next refresh cycle
- **P1:** Escalate to Operator; make manual judgment on whether to use previous version or defer
- **P0:** Halt governance; prioritize policy refresh

**Hold/Release Criteria:**
- Fresh version of external policy obtained and verified current
- Or Operator explicitly authorizes governance decision under previous (stale) version with bounded justification

---

## CONTROL 3 — Architecture Failure Procedures

### Failure: Deprecated Architecture Used

**Symptom:** Governance decision cites or relies on an architecture marked as deprecated

**Diagnosis:**
```
1. Which architecture was cited in the decision?
2. What is its status? (current | deprecated | archived)
3. When was it deprecated? (effective_date field)
4. What architecture superseded it?
5. Would the decision change under current architecture?
```

**Severity:**
- Decision made before deprecation date (P2) → valid at the time, mark for historical record
- Decision made after deprecation date (P1) → invalid, decision needs revision
- Deprecated method actively re-adopted (P0) → governance process broken

**Remediation:**
- **P2:** Add temporal scope note to decision record: "Made under [old architecture] on [date], before deprecation on [date]"
- **P1:** Re-assess decision under current architecture; revise if outcome changes
- **P0:** Halt new governance; audit all recent decisions for deprecated architecture usage; revise as needed

**Hold/Release Criteria:**
- Decision explicitly scoped to architecture version and date
- If decision made after deprecation: decision re-assessed and revised under current architecture
- No new decisions citing deprecated architecture without explicit temporal justification

---

### Failure: Architecture Status Unclear

**Symptom:** Readers cannot determine within 5 minutes whether an architecture is current or historical

**Diagnosis:**
```
1. Find the architecture note
2. Does it have a status field? (current | deprecated | archived)
3. Does it point to successor? (superseded_by field)
4. Is it linked from current governance documents?
5. How long does it take a reader to figure out status?
```

**Severity:**
- One note status unclear (P2) → mark with deprecation notice, low impact
- Multiple notes status unclear (P1) → audit creates confusion, readers may cite wrong version
- All architecture status unclear (P0) → governance authority is ambiguous

**Remediation:**
- **P2:** Add deprecation/status notices to unclear notes
- **P1:** Complete status audit; mark all notes with current | deprecated | archived
- **P0:** Halt governance decisions that depend on architecture clarity; do full audit

**Hold/Release Criteria:**
- Every architecture note has a status field
- Readers can determine current vs. historical within 2 minutes (not 5)
- All supersessions have migration guides

---

### Failure: Supersession Chain Broken

**Symptom:** Architecture A was superseded by B, which was superseded by C, but the chain is broken or ambiguous

**Diagnosis:**
```
1. Map the known supersessions (A→B, B→C, etc.)
2. Are there any orphaned architectures? (A references B, but B doesn't acknowledge it)
3. Are there branches? (A→B and A→C both claimed)
4. Is the chain linear or complex?
```

**Severity:**
- One orphaned architecture (P2) → low impact, mark as deprecated
- Complex/branching chain (P1) → readers can't follow history
- Chain completely unclear (P0) → governance authority is unknown

**Remediation:**
- **P2:** Mark orphan with deprecation notice pointing to known successor
- **P1:** Complete supersession registry; document all transitions with effective dates
- **P0:** Establish canonical succession history; resolve all ambiguities before approving new decisions

**Hold/Release Criteria:**
- Supersession registry complete with all known transitions
- Each old architecture marked with effective date and successor
- Reader can follow chain from current back to oldest without ambiguity

---

## Escalation Path (All Controls)

```
Control Failure Detected
    ↓
1. Classify severity (P0/P1/P2)
    ↓
2. P0: Escalate to Operator immediately
   P1: Escalate to Operator within 2 hours
   P2: Log incident, schedule remediation within 1 week
    ↓
3. Operator Decision:
   - Can governance continue with workaround? (P1/P2)
   - Must governance halt pending remediation? (P0, or P1/P2 if no workaround)
    ↓
4. Remediation begins (procedures per control above)
    ↓
5. Hold/Release criteria verified
    ↓
6. Control Passed: Resume governance
   OR
7. Remediation Failed: Escalate to higher authority / manual intervention
```

---

## Example Incident: Control 2 Failure

**Incident:** Reddit Data API terms snapshot is 10 days old; refresh date was 2026-04-27; governance decision depends on rate limit specifications

**Severity Assessment:** P1 (policy may have changed; decision blocks)

**Escalation:**
1. Fetch live Reddit API documentation
2. Compute hash of live source
3. Compare to snapshot hash
4. Hash differs: policy changed

**Remediation:**
1. Ingest new API terms (2026-04-26 or later)
2. Identify what changed (rate limits: 100/min → 50/min? OAuth: same?)
3. Re-assess governance decision:
   - If rate limit critical to decision: revise decision under new limits
   - If rate limit not critical: note decision was made under old policy, approve under current policy with caveat
4. Update External Data Registry: new snapshot date, next check date (2026-05-04)

**Hold/Release Criteria:**
- Live Reddit API snapshot current (< 1 day old)
- Governance decision explicitly references which API version was used
- If outcome changed under new terms: decision revised and re-approved

**Timeline:**
- Discovery to escalation: < 15 min
- Policy refresh: < 1 hour
- Decision revision: < 2 hours
- Full remediation: < 4 hours

---

## Monthly Incident Review (Major-Turn Checklist)

**Every major turn, review:**

1. **Tool Layer (Control 1):**
   - How many P1/P2 tool incidents this month?
   - Did any incident require manual workaround?
   - Do we need to add redundancy or monitoring?

2. **External Data (Control 2):**
   - Did any external policy change catch us by surprise?
   - How quickly did we detect the change?
   - Are refresh schedules adequate?

3. **Architecture (Control 3):**
   - Did any decision cite deprecated architecture?
   - Were readers confused about current vs. historical?
   - Do migration guides need updating?

4. **System Integration:**
   - Did one control failure cascade to others?
   - Were escalation procedures followed?
   - Did Operator have enough context to make decisions?

---

## Related

- [[Governance and PHAROS MOC]]
- [[OPEN RISKS — Three Governance Blindspots Requiring Recursive Control]] — source risks
- [[Governance Controls Integration Dashboard]] — normal operation procedures
- [[CONTROL 1 — Tool Layer Audit Protocol (Regulatory Grounding)]] — tool layer monitoring
- [[CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)]] — external data management
- [[CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding)]] — architecture versioning

---

## Open Questions

1. **Incident severity thresholds:** Are P0/P1/P2 definitions right? Should we add P3 (informational)?
2. **Remediation timelines:** Are 1-hour, 2-hour, 4-hour timelines realistic? Should they be adjusted?
3. **Manual workarounds:** When is it OK to bypass a failed control? (Never? With Operator approval? With Queen Keyport sign-off?)
4. **Incident communication:** Who should be notified when a control fails? (Operator? Stakeholders? Board?)
5. **Post-incident review:** Should we do blameless postmortems when controls fail?
