---
type: raw-source
aliases: [orphan-raw-2026-05-06-009]
graph_repair: 2026-05-06
---

# IF-2086 - Debate Structure and Triple Red-Team Optimization Whitepaper (v1.2)

Danny Stocker | ds@infrafabric.io | InfraFabric Research | 2026-02-22

## Quick TOC

- Section 0: Executive Decision
- Section 1: Dataset, Method, and Evidence Hierarchy
- Section 2: Current Debate Structure (as implemented)
- Section 3: Empirical Outcomes and Calibration Notes
- Section 4: Thin Areas and Token/Effort Waste
- Section 5: Missing Controls (Process Gaps)
- Section 6: Optimization Blueprint (v2 runtime)
- Section 7: Implementation Plan and Acceptance Gates
- Section 8: Reviewer Conclusions
- Section 9: Minimal External Verification (offline)
- Section 10: Risk and Mitigation
- Section 11: Applied Plan Status
- Section 12: Scheduled Follow-Up Tasks

## Document Navigation by Audience

- Executives / Business Leaders (standardize or constrain this operating model): Sections `0`, `3`, `4`, `6`, `8`, `11`
- Power Users / Operators (run cycles with less waste and fewer false motions): Sections `1`, `2`, `4`, `6`, `7`, `9`, `10`
- Engineers / Implementers (instrumentation, gate logic, rollback safety): Sections `2`, `5`, `6`, `7`, `9`, `10`, `12`
- LLM Runtime Developers (token economy, lane quality, policy enforcement; LLM = Large Language Model): Sections `3`, `4`, `5`, `6`, `7`, `9`, `10`
- Compliance / External Reviewers (claim boundary, reproducibility, and process control sufficiency): Sections `1`, `3`, `5`, `8`, `9`, `10`

**Who|Why|What|Where|When|How**

- **Who:** InfraFabric operators, Rook lane owners, external reviewers validating governance discipline.
- **Why:** debate cycles find real issues, but avoidable token/effort waste and partial quality coverage reduce operating efficiency.
- **What:** evidence-backed optimization plan for the 5-lane + triple-red-team process, including hard gates, stop conditions, and verification discipline.
- **Where:** `if_rook_five_lane` bundles, blackboard task history, and debate runbooks in this workspace.
- **When:** dataset as-of `2026-02-22T10:48:00Z`; optimization windows in `30/60/90 minutes` and `3/6/9 hours`; standardization decision checkpoints on day-scale dates.
- **How:** quantified corpus analysis + cross-session task conversion review + explicit control-gap design + reproducible verification commands.

**Problem statement:** we run many high-value adversarial debate cycles, but template-like lanes, missing quality summaries, and missing lane token telemetry still create measurable spend without proportional decision value.

**Execution-time model:** drafting/patching/review in `30/60/90 minutes` and `3/6/9 hours`; user-facing confidence and production-readiness decisions remain day-scale.

**Research-not-shipped:** this paper evaluates debate-process quality and optimization. It does not claim outbound commercial uplift.

**Not-for:** this paper is not legal advice and does not authorize autonomous execution.

## 0) Executive Decision

Decision: keep the 5-lane + triple-red-team structure as the architectural ceiling, but make runtime execution conditional via preflight admission, delta-first scheduling, and explicit return-on-investment (ROI) stop gates.

- Keep: multi-lens adversarial pressure and strict arbitration.
- Change: do not run full-lane cycles by default; run admissible delta-first lanes, then expand only when gates demand it.
- Add: lane token telemetry, template-lane hard fail, and automatic finding-to-task write-through for high-severity findings.

Target impact (pilot/stretch targets; re-baseline after IF-2089/IF-2090/IF-2091 telemetry lands):

- Template-like lane rate: reduce from `25%` to `<10%`.
- Quality summary coverage for `publish_target=true`: increase from `63.64%` to `>=95%`.
- P0/P1 follow-up task write-through: `100%` conversion within same cycle.

Black/white:

- Verified: current structure repeatedly surfaces high-severity issues.
- Verified: current process still spends material effort on non-publishable/low-yield cycles.
- Not yet verified: true per-lane token economics (current ROI is proxy-weighted, not token-normalized).

*If every metric improves except decision latency, you optimized the dashboard, not the business.*

## 1) Dataset, Method, and Evidence Hierarchy

Primary evidence sources used in this analysis:

- Debate orchestration runbook: `docs/2256_debates_and_redteams_orchestration_runbook_v1.2_2026-02-27.md`
- Prior triple-red-team reference: `docs/495-rook-v1.3-triple-redteam-final-report-v1.0-2026-02-15T173138Z.md`
- Bundle corpus root: `tmp/if_rook_five_lane/`
- Blackboard history: `.if_tasks/blackboard/tasks.events.jsonl`

Generated analysis artifacts (this run):

- `tmp/if2056/debate_redteam_dataset_2026-02-22T1048Z.json`
- `tmp/if2056/debate_redteam_task_conversion_2026-02-22T1050Z.json`
- `tmp/if2056/debate_redteam_meta_2026-02-22T1040Z.json`
- `tmp/if2056/debate_redteam_roi_2026-02-22T1041Z.json`
- `tmp/if2056/debate_redteam_timing_2026-02-22T1043Z.json`

Path note (`if2056` vs `IF-2086`): artifact paths retain `if2056` prefix because they were produced in the existing analytics workspace originally created for IF-2056 pipeline tooling. This paper (`IF-2086`) consumes those generated artifacts; no claim is made that the path prefix equals task scope.

Method summary:

1. Enumerate `IF-*` lane bundles and detect completeness (`manifest`, `arbitration`, `quality_gate_summary`, lane files).
2. Aggregate lane verdicts, severity, and `no_finding_reason` codes.
3. Compute quality coverage and quality latency (`manifest.created_utc` -> `quality_gate_summary.checked_utc`).
4. Detect low-return patterns (template-like lanes, duplicate reruns, quality-missing bundles).
5. Correlate debate outputs to blackboard follow-up conversion state.

Exclusions and limits:

- No direct per-lane prompt/completion token counters in baseline artifacts.
- No independent inter-rater severity calibration experiment in this dataset window.
- Triple-red-team overlay outputs are represented in bundle corpus behavior, but overlay-level independence metrics are not yet instrumented.

### 1.1 Evidence Hierarchy Used in This Paper

| Tier | Evidence class | Used for | Limitation |
|---|---|---|---|
| Tier 1 | Generated corpus artifacts (`dataset/task_conversion/meta/roi/timing`) | Quantitative claims and rates | No direct token counters yet |
| Tier 2 | Runbook contracts and gate scripts | Process-structure claims | May lag runtime drift if not revalidated |
| Tier 3 | Taskboard/blackboard status snapshots | Conversion/closure claims | Snapshot bias if tasks update after extraction |
| Tier 4 | Reviewer critiques (Opus/GPT/Gemini) | Gap detection and improvement agenda | Advisory signal, not runtime telemetry |

### 1.2 Operational Definitions (for reproducibility)

- **Template-like lane:** lane with `verdict=no_finding`, empty `agent`, empty `findings`, and `no_finding_reason=redteam.model_abstain` OR semantic similarity >= `0.90` to bootstrap lane template after removing timestamps/IDs.
- **Quality summary present:** `quality_gate_summary.json` exists and includes explicit pass/fail verdict fields.
- **Publish-target bundle:** bundle with `manifest.publish_target=true` (new field in v2 plan).
- **Duplicate rerun:** multiple bundles for same `task_id` within same phase window without explicit source-change rationale recorded.

*If the evidence ladder is blurry, every conclusion becomes an opinion with better typography.*

## 2) Current Debate Structure (As Implemented)

Reference operating model:

- 3-session ownership split:
  - Session-1 control owner (arbitration + publish/no-publish)
  - Session-2 quorum/recovery owner
  - Session-3 debate accelerator
- Debate modes:
  - Product debate
  - Red-team debate
  - Recovery debate
  - External reviewer debate
- 5-lane contract (mandatory):
  - `L1` Claims+Boundary
  - `L2` Runtime+Code
  - `L3` Adversarial+Abuse
  - `L4` Ops+Recovery
  - `L5` External Reviewer Lens

Triple red-team overlays (parallel lenses):

- Narrative stress lens
- Compliance/ethical abuse lens
- Technical replay/bypass lens

Control flow (current runtime path):

```text
Task claim -> bundle bootstrap -> lane generation (L1..L5 + overlays)
-> arbitration -> patch/no-patch decision -> quality validate -> publish-ready gate
-> task update + artifact ledger
```

Consistency statement: Section 3 measures practical adherence and highlights where this ideal flow is not consistently completed.

*If the loop exists only in diagrams, production will eventually route around it.*

## 3) Empirical Outcomes and Calibration Notes (As-of 2026-02-22T10:48Z)

Dataset coverage:

- Bundle count: `22`
- Distinct task IDs: `19`
- Lane artifacts analyzed: `100`
- Findings captured: `149`

Lane verdict distribution:

- `pass_with_risk`: `62`
- `no_finding`: `26`
- `fail`: `12`
- `pass`: `0`

Severity distribution:

- `P0`: `4`
- `P1`: `71`
- `P2`: `68`
- `P3`: `6`

Derived process metrics:

- Lane findings rate: `0.74`
- Lane no-finding rate: `0.26`
- Template-like lane rate: `0.25`
- Average findings per lane: `1.49`
- Quality summary coverage: `14/22` (`63.64%`)
- Quality latency (minutes): p50 `10.85`, p90 `23.88`, mean `11.93`

Metric formulas used:

- `lane_findings_rate = lanes_with_findings / lane_total`
- `lane_no_finding_rate = lanes_no_finding / lane_total`
- `template_like_rate = template_like_lanes / lane_total`
- `avg_findings_per_lane = findings_total / lane_total`
- `quality_coverage_rate = quality_summary_present / bundle_count`

Task conversion snapshot (`IF-2056..IF-2089` cohort):

- Total tasks: `30`
- Status split: `18 done`, `5 in_progress`, `7 todo`
- Debate/red-team tagged: `7` (`5 done`, `2 in_progress`)

Interpretation of `pass=0` (explicit):

- Plausible explanation A: lanes are correctly tuned toward risk discovery under adversarial framing.
- Plausible explanation B: lane prompts/criteria may be biased toward non-pass outcomes.
- Therefore: `pass=0` is a signal requiring calibration follow-up, not proof of superior rigor by itself.

Severity calibration caveat:

- `P1/P2` clustering (`139/149`) may indicate true mid-high risk density, severity anchoring bias, or both.
- This paper cannot conclude calibration quality without independent rater or replay calibration data.

*Zero passes can mean strong detection or strong confusion; calibration decides which story is true.*

## 4) Thin Areas and Token/Effort Waste

### 4.1 Thin areas

1. No direct lane token telemetry.
- ROI is proxy-based today.

2. Incomplete quality coverage.
- `8/22` bundles lack quality summary.

3. Partial semantic verification dependence.
- Human reviewer quality still non-uniform across cycles.

4. Overlay independence is under-measured.
- We do not yet score whether red-team overlays produce independent findings or lane echoes.

5. Severity calibration is under-specified.
- No adjudication rubric confidence score attached to each severity call.

### 4.2 Waste classes

1. Non-publishable cycle waste.
- Quality-missing bundles represent lane effort with unclear promotion value.

2. Template/no-output waste.
- `25` lanes match template-like behavior and consume cycles without new evidence.

3. Duplicate rerun waste.
- `3` tasks had duplicate bundle runs; useful for patch verification only when source-change rationale is explicit.

4. Drift-induced patch churn.
- Environment/path/dependency assumptions caused avoidable reruns and repatching.

### 4.3 ROI formulas and guardrails

Current proxy (heuristic):

- `ROI_proxy = (P0*8 + P1*5 + P2*2 + P3*1) / lane_count`

Heuristic status:

- Weights are provisional and must be calibrated against closure cost and remediation impact after telemetry lands.

Target formula (post-telemetry):

- `ROI_token = weighted_findings / (prompt_tokens + completion_tokens + arbitration_minutes*k)`

Interpretation rule (v2):

- Trigger collapse when yield falls below `50%` of rolling five-cycle baseline for two consecutive cycles, OR no `P0/P1` across two cycles.

Duplicate rerun policy (explicit):

- Allowed: rerun after code/doc/source delta with rationale in manifest.
- Blocked: rerun without delta rationale for same task/phase window.

*If reruns feel productive without new inputs, you are paying for motion, not learning.*

## 5) Missing Controls (Process Gaps)

1. Lane-level token accounting missing.
- Add `prompt_tokens` and `completion_tokens` per lane.

2. Template-lane hard fail not universal.
- Enforce semantic template detection before arbitration.

3. Finding-to-task conversion still manual.
- Auto-generate `triage` task stubs for `P0/P1` immediately.

4. Publish intent too late.
- Require `publish_target=true|false` at bootstrap.

5. Replay/attestation fixtures not mandatory in all cycles.
- Enforce L3 fixture suite (`replay`, `stale`, `unsigned`, composed bypass case).

6. Lane retirement/collapse logic missing.
- Add bounded policy for temporarily collapsing repeatedly low-yield lanes.

## 6) Optimization Blueprint (v2 Runtime)

### 6.1 Gate sequence

Gate A: Preflight admission (hard stop)

- Task ID exists and owner is normalized.
- Scope and artifact target declared.
- `publish_target` explicit.
- `manifest.schema_version`, `source_hash`, `dependency_digest`, and `policy_digest` present.

Gate B: Lane generation admission (delta-first with drift safety)

- Require source hash + dependency digest + policy version digest check.
- Skip unchanged lanes only if prior quality is green and staleness window not exceeded.
- Force periodic full sweep every `Nth` cycle (default `N=3`) or after policy/tool digest change.

Gate C: Arbitration readiness

- Reject template-like lanes.
- Reject findings lacking evidence ref and concrete next action.
- Apply severity down-check for all `P1` findings (prevent inflation drift).

Gate D: Publish readiness

- Require quality summary pass.
- Require contradiction resolution record.
- Require residual-risk mapping to follow-up tasks.

### 6.2 Stop conditions (token protection)

S1: low-yield loop

- Trigger: yield < `50%` of rolling five-cycle baseline for two consecutive cycles OR no `P0/P1` in both cycles.
- Action: collapse to rapid mode (`L1`,`L3`) + owner review.

S2: template recursion

- Trigger: template-like lane appears in two consecutive cycles for same task.
- Action: halt auto-lane execution and require prompt-pack correction.

S3: publish drift

- Trigger: publish-target bundle lacks quality summary by end of operator window (default 30 minutes unless explicitly extended).
- Action: downgrade bundle to exploratory and exclude from promotion metrics.

S4: hard budget ceiling

- Trigger: bundle crosses configured token or effort cap before Gate D.
- Action: stop generation, escalate to owner, require explicit continuation decision.

### 6.3 Conflict resolution hierarchy

- L3 abuse evidence outranks narrative convenience claims.
- L1 claim-boundary violations block external promotion regardless of other lane passes.
- L4 can request rollback readiness gating even when arbitration is otherwise green.
- L5 can only promote wording/clarity changes; it cannot downgrade hard control failures.

### 6.4 Highest-return improvements

1. Delta-first + periodic full sweep scheduler.
2. Deterministic prompt packs by failure class.
3. Automated ROI dashboard from lane + quality artifacts.
4. Enforced finding-to-task write-through with dedupe and triage state.

### 6.5 Minimal manifest contract (v2)

Required fields for gate admission:

- `task_id` (string)
- `publish_target` (boolean)
- `mode` (`exploratory|publish`)
- `schema_version` (string)
- `source_hash` (sha256)
- `dependency_digest` (sha256)
- `policy_digest` (sha256)
- `created_utc` (RFC3339)
- `owner_sid` (string)

*If the manifest cannot explain the run, the run cannot justify the claim.*

## 7) Implementation Plan and Acceptance Gates

Schedule interpretation: all windows below are pilot planning checkpoints (not fixed contractual delivery promises) and are contingent on listed dependencies.

### 7.1 Immediate windows (30/60/90 minutes)

- 30 minutes:
  - Add `publish_target` + `mode` fields to manifest.
  - Add template-like detector hook.
  - Acceptance: new bundles include fields; detector flags known template fixtures.

- 60 minutes:
  - Add lane token fields.
  - Add ROI summary emitter.
  - Acceptance: `debate_roi_summary.json` exists for new bundles.

- 90 minutes:
  - Add `P0/P1 -> triage task stub` generation.
  - Add severity down-check field in arbitration record.
  - Acceptance: high-severity findings create deduped triage stubs with owner prompts.

Dependencies:

- 60-minute items depend on 30-minute schema updates.
- 90-minute items depend on 30-minute and 60-minute outputs.

Rollback criteria:

- If false-positive template blocks exceed `10%` in pilot, revert detector to advisory mode and tune similarity thresholds.

### 7.2 Extended windows (3/6/9 hours)

- 3 hours:
  - Implement delta-first scheduler with digest map.

- 6 hours:
  - Add mandatory L3 fixture pack + composed abuse telemetry.

- 9 hours:
  - Enforce `publish_target=true` closure block unless Gate D is green.

Acceptance:

- New bundles include digest map and fixture outcomes.
- Publish-target closure fails closed when quality/arbitration artifacts are missing.
- Stop-gate telemetry emitted (`S1`..`S4` trigger state + inputs) for operator dashboards.

### 7.3 Day-scale milestones (30/60/90 days)

- Day 30 (`2026-03-24` window start):
  - First calibrated ROI report with token telemetry.
  - First severity calibration replay sample.

- Day 60:
  - Overlay independence scoring published.
  - Duplicate-rerun suppression policy validated.

- Day 90:
  - Standardization decision memo with measured before/after deltas.
  - Explicit decision: keep v2 as default, revise, or rollback.

*Milestones without gates are calendar art.*

## 8) Reviewer Conclusions

### Can conclude now

- Debate architecture is structurally strong and repeatedly surfaces non-trivial risk.
- Process waste is measurable and material (`25%` template-like lanes + `36.36%` quality-missing bundles), which is sufficient to justify runtime optimization.
- Optimization controls are concrete and implementable without architecture rewrite.

### Cannot conclude now

- True token-normalized ROI (telemetry pending).
- Severity calibration reliability (independent rater data pending).
- Commercial/outbound impact from debate quality alone.

### Should not conclude

- High finding volume does not prove economic efficiency.
- Exploratory bundles without quality summary are not production-grade evidence.
- `pass=0` is not automatically proof of superior rigor; it may also indicate prompt-calibration bias.

*When "cannot conclude" is ignored, risk is just being deferred in formal language.*

## 9) Minimal External Verification (Offline)

Artifact hashes (sha256):

- `47884f63728c4e849275fb1f63e2a9775bb4b80b4a52771dccbb058b9b3aea4a` -> `tmp/if2056/debate_redteam_dataset_2026-02-22T1048Z.json`
- `1b4d178e10e1d6b2ccfb2b4ba5b372bdd5875a2ed43a017d81206d8e59497a62` -> `tmp/if2056/debate_redteam_task_conversion_2026-02-22T1050Z.json`
- `d6daf800128f3c66699c09d19ba04598ad088acdc98b4c17dae4174b26989fd2` -> `tmp/if2056/debate_redteam_meta_2026-02-22T1040Z.json`
- `5b7d2ea6a03e2024252659d630ec3b169729aea94e2918594dce388837d79f34` -> `tmp/if2056/debate_redteam_roi_2026-02-22T1041Z.json`
- `0de69c1063661318617e453208b97a9adce5418e6845c96ef5747f8546f0685f` -> `tmp/if2056/debate_redteam_timing_2026-02-22T1043Z.json`

Commands:

```bash
jq '{bundle_count,task_count,quality_summary_present,quality_summary_missing,lane_verdict_counts,derived}' tmp/if2056/debate_redteam_dataset_2026-02-22T1048Z.json
jq '{duplicate_task_count,duplicate_tasks,quality_missing_bundles}' tmp/if2056/debate_redteam_dataset_2026-02-22T1048Z.json
jq '{cohort_count,status_counts,debate_task_count,debate_status_counts,followup_todo_count}' tmp/if2056/debate_redteam_task_conversion_2026-02-22T1050Z.json
jq '.top_finding_tokens[0:15]' tmp/if2056/debate_redteam_dataset_2026-02-22T1048Z.json
jq '.metrics | {lane_total,findings_total,template_like_lanes}' tmp/if2056/debate_redteam_dataset_2026-02-22T1048Z.json
jq '.derived' tmp/if2056/debate_redteam_dataset_2026-02-22T1048Z.json
jq '{task_id,publish_target,mode,schema_version,source_hash,dependency_digest,policy_digest}' tmp/if_rook_five_lane/IF-2092_2026-02-22T115111Z/manifest.json
rg -n "^## " docs/2256_debates_and_redteams_orchestration_runbook_v1.2_2026-02-27.md
```

Expected shape checks:

- `bundle_count` should read `22` for this dataset snapshot.
- `lane_verdict_counts` should include `pass_with_risk`, `no_finding`, `fail`, `pass`.
- `cohort_count` should read `30` in the conversion snapshot.
- Manifest digest fields are a v2 requirement; if missing in current bundles, treat as a pending-control gap (not a false pass).

Current boundary:

- Verification commands above are repo-local/offline against hashed artifacts in `tmp/if2056/`.
- Promotion to external immutable/signed verifier links is pending follow-up implementation.

*If outsiders cannot replay it, insiders should not overclaim it.*

## 10) Risk and Mitigation

1. Risk: speed optimization degrades adversarial depth.
- Mitigation: mandatory L3 fixture pack + periodic full sweeps.

2. Risk: ROI metric gaming (Goodhart pressure).
- Mitigation: severity down-check, evidence minimums, and qualitative audits on high-ROI bundles.

3. Risk: backlog flood from auto-generated stubs.
- Mitigation: `P0/P1` only auto-create; `P2+` grouped by theme; default `triage` state with dedupe.

4. Risk: token instrumentation overhead.
- Mitigation: lane-boundary counters only; no per-token payload copies.

5. Risk: cross-session ownership conflict.
- Mitigation: strict sid hygiene, owner normalization, and explicit session/task mapping.

6. Risk: delta-first false negatives from dependency/context drift.
- Mitigation: digest checks + periodic full sweeps + forced rerun on policy/tool version change.

7. Risk: citation hallucination in downstream summaries.
- Mitigation: evidence refs required for promoted findings and hash-linked artifact checks.

8. Risk: ambiguous pilot results stall decision.
- Mitigation: define standardization decision protocol before pilot close (keep/revise/rollback criteria).

9. Risk: repo-local verification artifacts are mutable paths for external reviewers.
- Mitigation: publish immutable, signed verification mirrors before external compliance-facing reviews.

10. Risk: runtime compliance probe hard-fail (`chat_healthz_ok=false`) blocks compliance-grade claims.
- Mitigation: restore chat surface health and require green compliance probe before making compliance-grade runtime assertions.

*The unmonitored risk is usually the one that writes the postmortem.*

## 11) Applied Plan Status (v1.2)

| Recommendation | Status | Evidence |
|---|---|---|
| quantify outcomes from real bundle corpus | implemented-once | Section 3 + dataset artifacts |
| classify waste with measurable proxies | implemented-once | Section 4 |
| define adaptive stop conditions | documented-only | Section 6.2 |
| define gate-based optimization runtime | documented-only | Section 6 |
| add reviewer-verifiable commands + hashes | implemented-once | Section 9 |
| lane token telemetry | pending (operationalize) | IF-2089 |
| template hard-fail gate | pending (operationalize) | IF-2090 |
| auto finding-to-task conversion | pending (operationalize) | IF-2091 |

*"Documented-only" is useful, but it does not survive contact with auditors.*

## 12) Scheduled Follow-Up Tasks

- `IF-2089` (P1): lane token telemetry + ROI summary emitter.
  - depends on: manifest/schema field updates.
  - target: `2026-02-24` pilot-ready.

- `IF-2090` (P1): template-lane hard fail pre-arbitration.
  - depends on: template detection rule + fixture set.
  - target: `2026-02-24` pilot-ready.

- `IF-2091` (P1): auto-convert `P0/P1` findings into `triage` task stubs.
  - depends on: severity parse + owner mapping + dedupe key.
  - target: `2026-02-24` pilot-ready.

- `IF-2092` (P1): integrate external reviewer critiques into v1.2 and run multi-agent/triple-red-team review.
  - depends on: v1.2 draft + lane bundle validation.
  - target: same-day completion.

*Scheduled work is not closed risk; it is a dated promise.*

## Footer

Style Guide: Whitepaper v4.17

## Related

- [[Governance and PHAROS MOC]]
- [[PROTOCOLS — Debate and Red-Team Runbook]]
- [[Santé-France — Critical Full Explainer (v2.0, dependency-gated rebuild)]]
