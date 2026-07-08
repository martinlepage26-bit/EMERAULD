# InfraFabric Blackboard — Training Data Asset Catalogue

**Prepared for Micro1  ·  Confidential**  
InfraFabric Research  ·  pharos-ai.ca  ·  ml@pharos-ai.ca  ·  June 2026

*Nearly one year of unpublished multi-agent research and product development.  
No portion of this material has been externally published prior to this document.*

---

## Executive Summary

InfraFabric operates an append-only agent task ledger called **if.blackboard**. Every task an AI agent works on — from infrastructure debugging to governance deliberation to creative video production — is permanently recorded as a structured event with a sequential ID, session binding, acceptance criteria, typed checkpoints, hard-won traps, and a SHA-256-hashed closeout. The result is a corpus of real, grounded agent work that synthetic data cannot replicate.

The board and its outputs represent the cumulation of nearly a year of unpublished research and product development. The tasks recorded here are not demo exercises or synthetic prompts — they are the working traces of a live, production multi-agent system solving real engineering, governance, legal, and creative problems under deadline and resource constraints. None of this material has been published externally prior to this document.

This document catalogues 49 curated task entries spanning 10 months of live multi-agent operation across Claude (Anthropic), Codex (OpenAI), and specialist agents. Entries are selected for signal diversity — one to five per domain — from a full ledger of 3,800+ task IDs.

---

## Anatomy of a Blackboard Entry

| Field | What it records |
|---|---|
| **Task ID + Session binding** | A sequential ID (e.g. IF-3477) permanently links the task to the session (sid) in which it was initiated. If another agent resumes later, the original binding is preserved — no ambiguity about ownership across sessions. |
| **Acceptance criteria** | Written before work begins. Falsifiable conditions that define done. An agent cannot close a task by claiming it is finished; it must demonstrate each criterion was met, or document which remain open and why. |
| **Typed checkpoints** | Mid-task snapshots: progress_summary, last_verified_state, next_step, traps_so_far, open_questions, artifact_refs. Structured enough that any future agent can parse them and resume without the conversation transcript. |
| **Traps** | The most training-data-valuable field. A trap is a hard-won failure mode the current agent explicitly records for its successors: environment-specific gotchas, false hypotheses ruled out, ordering constraints not obvious from the code. Traps carry forward through checkpoint and closeout events — they do not disappear when a task closes. |
| **Intent vs. result separation** | Task description + acceptance criteria (intent) are recorded separately from the result + closeout evidence. Divergence is not suppressed — a partial result is a partial result. This makes failure records honest in a way synthetic completions cannot replicate. |
| **SHA-256 result hash** | When a task closes, the result payload is hashed. Any future agent can confirm the result has not been altered since closeout. Tamper-evidence is structural, not procedural. |

The full blackboard ledger contains **3,800+ task IDs** accumulated over 10 months. This document presents 49 curated entries selected for training-data diversity across 10 thematic domains. Volume expansion across any domain is available on request.

---

## Core Signal Types

| Signal Type | What it demonstrates | Gap in synthetic data |
|---|---|---|
| Trap propagation | Hard-won environment-specific failures recorded and carried forward to successors | Cannot be generated without a real failure history |
| Root-cause falsification | Agent corrects its own prior diagnosis after new evidence contradicts the original hypothesis | Synthetic tasks have known answers; real agents discover them |
| Calibrated partial claims | Distinguishing verified / archival / inference / blocked tiers within one document | LLMs tend toward binary claim posture |
| Suspension with clean state | Task paused mid-stream with a full handoff packet for a future agent | Requires genuine multi-session continuity |
| Adversarial self-review | Agent applies red-team methodology to its own prior outputs | Self-critique on real outputs differs from synthetic critique prompts |
| Empirical experiment design | Single-criterion A/B tests with honest confound disclosure and falsifiable next-step hypothesis | Synthetic benchmarks hide methodological limits |
| Multi-lane adversarial convergence | Three independent adversarial lenses, cross-rebuttal, then convergence | Simulated debate from one model collapses to one perspective |
| Physical-world safety gate design | Dry-run flags, human-in-the-loop gates, degraded-mode bounds designed before actuation | Safety reasoning on real hardware paths is absent from text training data |
| Filing-grade IP precision | Concept → mechanism → invention disclosure where each word has claim-scope implications | Legal precision under claim-scope constraints is absent from current corpora |
| Institutional knowledge capture | Process runbooks written for successor agents before knowledge atrophies | Requires understanding of what a future agent will need |

---

## How the Blackboard Works

if.blackboard is an append-only event ledger. No record is ever modified or deleted — every state change appends a new event.

### Task Lifecycle

| Step | Event | What it records |
|---|---|---|
| 1 | session_bind | Agent binds its stable identity (agent_id) to the current conversation (sid). Gate rejects mismatched bindings. |
| 2 | task_template | Task structure generated before work begins: ID, pillar, priority, acceptance criteria, working set. |
| 3 | task_create | Task written to the ledger as an immutable create event. |
| 4 | lifecycle_template | Multi-step work plan established. Checkpoints, trap capture, and closeout structure defined in advance. |
| 5 | [WORK] | Agent executes. Can be interrupted at any checkpoint and resumed by any future agent using the checkpoint as authoritative state — not the conversation transcript. |
| 6 | task_checkpoint | Typed snapshot: progress_summary, last_verified_state, next_step, traps_so_far, open_questions, artifact_refs. |
| 7 | closeout_template | Closeout structure prepared with result hash, trap carry-forward, and evidence references. |
| 8 | task_update (done) | Task sealed. SHA-256 result hash written. Subsequent agents read this as authoritative ground truth. |

### Authority Order on Resume

```
task row  ›  latest checkpoint  ›  closeout  ›  artifact refs  ›  prior searches
```

The blackboard — not memory, not transcript — is the source of truth.

---

## Task Catalogue

---

### Domain 1: Agent Infrastructure & Multi-Agent Coordination

These entries document the foundational infrastructure of a live multi-agent system: parallel swarms, control plane design, real debugging under memory pressure, and targeted surgical patches. The signal value is in the failure modes, root-cause corrections, and multi-session handoffs — work that synthetic data cannot replicate because it requires real environments, real constraints, and real consequences.

---

#### Sample 1 — IF-3477 · Blackboard Business Plan — What the Ledger Is Worth

**Status:** IN_PROGRESS · **Date:** 2026-04 · **Signal:** Institutional self-assessment with claims ledger and dogfood loop

**TASK:** Build an integrated InfraFabric/Blackboard business plan covering Blackboard as the wedge plus adjacent services (if.context, if.optimise, if.rook, if.gov, if.api)

**ACCEPTANCE:** External-facing business plan artifact, evidence-anchored, claims ledger, dogfood report, marketplace submission pack

**RESULT:** Market intelligence sprint delivered ICP/buyer pain, competitor/pricing, why-now/regulatory evidence packs. External business plan v1.1 created. Consolidated GTM pack v1.0 published. Dogfood-driven CLI improvements landed. Claim record states design partners, revenue, and live customer claims are **not yet present**.

> **⚠ TRAPS RECORDED FOR SUCCESSOR AGENTS**
> - Directus sync loop: `/etc/systemd/system/if-blackboard-directus-sync.path` had both PathExists and PathChanged for the same blackboard JSONL — triggered a sync on every blackboard write, creating a CPU feedback loop. Fix: remove PathExists, keep only PathChanged.
> - Codex MCP schema will not hot-reload a new tool until a future client/session restarts — cannot add a tool mid-session.
> - Claims ledger guard: business plan language must say "not yet claimed" for design partners, revenue, live customers — boarding without that guard inflates the pitch beyond evidence.

**WHY THIS MATTERS FOR TRAINING DATA:** This task is notable for what the agent refused to claim. The business plan was co-produced with a dogfood report — the agent used the tool it was describing and discovered real friction that was then fixed mid-task. Self-referential improvement at the task level.

---

#### Sample 2 — IF-3433 · PHAROS Corpus Swarm — 100+ Parallel Workers in Isolated Worktrees

**Status:** DONE · **Date:** 2026-04 · **Signal:** Multi-agent orchestration at scale with clean suspension on partial failure

**TASK:** Run 100+ parallel Codex agents across isolated git worktrees via Hermes kanban, close 5 quality lanes across the InfraFabric codebase

**ACCEPTANCE:** All 5 quality lanes shipped: signature enforce, alias honesty sweep, session auto-close, stale-task digest hygiene, bounded harness-first

**RESULT:** Shipped: Lane 1 (signature enforce on signals index), Lane 3 (legacy alias honesty sweep), Lane 4 (session auto-close + stale-task digest hygiene), Lane 5 (bounded harness-first). Lane 2 suspended when two-remote git failure hit — Forgejo timed out while GitHub succeeded. Clean handoff packet produced for lane 2 resume.

> **⚠ TRAPS RECORDED FOR SUCCESSOR AGENTS**
> - Two-remote git failure: Forgejo timed out during push while GitHub succeeded — agent correctly suspended rather than force-resolving. Lane 2 handoff documented the exact failure state.
> - Isolated worktrees require explicit cleanup — stale worktrees from crashed agents accumulate and fill disk.

**WHY THIS MATTERS FOR TRAINING DATA:** The swarm was honest about partial failure — a pattern absent from benchmarks where all agents succeed. Four lanes completed; one suspended cleanly with a documented handoff packet. The asymmetry is the training signal.

---

#### Sample 3 — IF-3211 · Multi-Agent Autonomous Development Control Plane

**Status:** IN_PROGRESS · **Date:** 2026-04 · **Signal:** Architecture design identifying failure modes of shared task queues

**TASK:** Design a Rook-native multi-agent autonomous development control plane: agents as first-class principals with switchboard routing, blackboard task ownership, and if.chat for real-time coordination

**ACCEPTANCE:** RFC identifying failure modes of shared task queue; switchboard seat model for agents; identity-bound task ownership

**RESULT:** Control plane RFC produced. Identified 6 failure modes for shared task queues without principal binding. Switchboard seat model specified. Live seat liveness monitoring detected seat_liveness_lost_utc events for claims_boundary endpoint and recovered via re-register. 109 checkpoints across multiple sessions.

> **⚠ TRAPS RECORDED FOR SUCCESSOR AGENTS**
> - Seat liveness lost fires when an agent crashes without explicit unregister — cleanup logic must handle both graceful and ungraceful exits or the registry fills with ghost seats.
> - SIP-style routing requires each agent to maintain its own heartbeat; any network partition causes false liveness loss.

**WHY THIS MATTERS FOR TRAINING DATA:** This RFC ran 109 checkpoints over multiple sessions. It is a failure-mode catalogue as much as an architecture spec — the key contribution is what goes wrong, not what the happy path looks like.

---

#### Sample 4 — IF-3826 · Security Explainer Patch — Section 4.3 Only

**Status:** DONE · **Date:** 2026-04 · **Signal:** Targeted surgical patch with precise scope discipline and zero scope creep

**TASK:** Add Section 4.3 (philosophical architecture justification) to the if.security full explainer doc 688, without touching any surrounding content

**ACCEPTANCE:** Section 4.3 present, section numbers unchanged, lint passes, no scope creep into adjacent sections

**RESULT:** Section 4.3 added to /root/docs/688-if-security-full-explainer-v1.0. Section numbering verified before and after. Lint gate passed. Zero changes to sections 4.1, 4.2, or 4.4+. Patch applied to if_cli/cli.py and scripts/if_cli.py simultaneously.

**WHY THIS MATTERS FOR TRAINING DATA:** A 300-line document, one section added, zero surrounding lines touched. This demonstrates a class of scope discipline that agents systematically fail at: the temptation to "improve" adjacent content while in the file.

---

#### Sample 5 — IF-3470 · Directus Sync Feedback Loop — Root Cause Falsification

**Status:** DONE · **Date:** 2026-04 · **Signal:** Initial hypothesis falsified; root cause discovered and fixed with empirical verification

**TASK:** Diagnose and safely relieve memory pressure on mtl-01 host; identify root cause without disrupting running sessions

**ACCEPTANCE:** Root cause identified; pressure relieved; fix verified stable across 3 real blackboard writes; no running sessions killed

**RESULT:** Initial hypothesis (Redis pressure) falsified. VS Code Remote fileWatcher was primary pressure source (~310 MB RSS vs Redis ~138 MB RSS). Systemd path unit bug: PathExists + PathChanged on same JSONL triggered Directus sync on every blackboard write (CPU feedback loop). Fixed. Verified: 3 real blackboard writes → exactly 1 sync run → service returned to idle.

> **⚠ TRAPS RECORDED FOR SUCCESSOR AGENTS**
> - Killing stale VS Code session-10285 also dropped the live VS Code server tree the resumed Codex session depended on — never kill by session ID without verifying all dependents.
> - safe-rg wrapper on this host rewrites `rg -n` calls — use python probes for absolute-path checks instead.
> - Systemd PathExists + PathChanged on the same path is a trigger-on-write loop — one or the other, never both for the same file.

**WHY THIS MATTERS FOR TRAINING DATA:** The cleanest root-cause falsification in the corpus. Initial hypothesis measured and disproved. Real root cause found. Fix verified empirically. The measurement methodology is as valuable as the conclusion.

---

### Domain 2: if.rook — Agent Identity and Execution Security

if.rook is the agent harness and broker: identity-bound principal verification, cryptographic release-proof, risk_class gate, and verify-chain CLI. These entries document the reasoning behind zero-trust execute gates — including the minority position on release-proof scope, the open gap explicitly not closed, and the compliance probe that revealed pre-existing non-compliance on first run.

---

#### Sample 46 — IF-1679 · Compliance-Grade Audit Hardening + Heart/Drone Provenance Case

**Status:** DONE · **Date:** 2026-02 · **Signal:** Compliance tooling that reveals pre-existing non-compliance on first run

**TASK:** Build file integrity scripts, session snapshot redaction, compliance probe runner, decision provenance tracer. Include heart/drone case study.

**ACCEPTANCE:** Four scripts delivered; compliance probe runnable; decision chain auditable end-to-end; heart/drone case study verified

**RESULT:** Delivered: scripts/if_file_integrity.py, if_rook_redact_shell_snapshot.py, if_rook_compliance_probe.py, if_rook_decision_provenance.py. Heart/drone case study: decision chain traced from Slack input through if.bus → if.rook → if.gov → physical actuation path.

> **⚠ TRAPS RECORDED FOR SUCCESSOR AGENTS**
> - Compliance probe shipped FAIL on first run — because legacy unsigned signal records existed before the probe was written. This is the correct outcome. Future agents: do not suppress a FAIL result from a probe that is working correctly.
> - Decision provenance tracer requires exact session ID; wrong session returns empty chain silently rather than erroring.

**WHY THIS MATTERS FOR TRAINING DATA:** The probe shipped FAIL on its first run. Not a bug — a finding. The entry documents shipping a tool that immediately found problems with the existing system and the decision not to suppress those findings.

---

#### Sample 47 — IF-1732 · Triple Red-Team: ShadowRT + Ethical + Adversarial + Cross-Rebuttal

**Status:** DONE · **Date:** 2026-02 · **Signal:** Multi-lane adversarial convergence — Lane C found attack vectors A and B missed

**TASK:** Triple red-team of if.rook docs 493/494: ShadowRT (formal if.gov triage), ethical adversarial lane, and unconstrained adversarial lane simultaneously, then cross-rebuttal and synthesis

**ACCEPTANCE:** Three independent red-team lanes run; cross-rebuttal documented; only findings surviving all three lanes confirmed

**RESULT:** Three lanes executed in parallel. (A) if.gov triage+extended+jester, (B) ethical adversarial, (C) unconstrained adversarial. Cross-rebuttal: lanes A and B converged on 3 shared findings. Lane C found 2 additional attack vectors not visible to either other lane. Only findings confirmed by ≥2 of 3 lanes were promoted to synthesis.

> **⚠ TRAPS RECORDED FOR SUCCESSOR AGENTS**
> - Lane C (unconstrained) found attack vectors A and B both missed — a two-lane red team would have published an incomplete finding set.
> - Cross-rebuttal requires that each lane sees the others' outputs before rebuttal, not concurrently — ordering matters for genuine independent finding.

**WHY THIS MATTERS FOR TRAINING DATA:** The structural case for N≥3 adversarial lanes demonstrated empirically: the third lane found what two lanes missed. This is the rarest kind of training example — one that justifies its own methodology through its results.

---

#### Sample 48 — IF-1731 · risk_class Gate Hardening + verify-chain CLI

**Status:** DONE · **Date:** 2026-02 · **Signal:** Four-item hardening closure with one open gap explicitly documented, not suppressed

**TASK:** Harden if.rook execute path: add risk_class gate, verify-chain CLI, configurable safe chain root, update docs. Document remaining open gap explicitly.

**ACCEPTANCE:** Four hardening items closed; verify-chain subcommand working; open gap (actor-id binding) documented not suppressed

**RESULT:** Implemented: (1) execute requires decision.risk_class in schema + fallback validator + policy gate, (2) verify-chain subcommand for full hash-link continuity check, (3) configurable safe chain root via env var, (4) two docs updated. Open gap documented: actor-id binding not yet enforced at execute time.

**WHY THIS MATTERS FOR TRAINING DATA:** Four items closed. Fifth explicitly left open and documented. An agent that claims 5/5 when it did 4/5 is worse than useless for compliance — the honest partial closeout is the training signal.

---

#### Sample 49 — IF-1739 · Identity-Bound Principal Verification for Execute Path

**Status:** DONE · **Date:** 2026-02 · **Signal:** Zero-trust execute gate: capability binding not self-reporting

**TASK:** Remove caller-self-reported capabilities from the execute path; replace with verified principal assertion; fail-closed default with machine-readable deny reason

**ACCEPTANCE:** Principal auth module written; policy gate updated; fail-closed default verified; deny reason is machine-readable not human prose

**RESULT:** Implemented principal_auth.py and updated policy_gate.py and cli.py. Self-reported capabilities ignored. Capabilities only valid if asserted by a cryptographically verified principal. Fail-closed: deny with structured JSON reason object (not prose). Unverified caller attempting execute gets deny + reason code.

**WHY THIS MATTERS FOR TRAINING DATA:** The distinction between caller-self-reported capabilities and verified principal assertion is the kind of security reasoning that only appears in real zero-trust implementation work. Machine-readable deny reason (not prose) matters for automated compliance tooling downstream.

---

#### Sample 50 — IF-1741 · Cryptographic Release-Proof Verification

**Status:** DONE · **Date:** 2026-02 · **Signal:** Supply-chain integrity gate with multi-perspective deliberation record

**TASK:** Add cryptographic release-proof verification to the execute gate: require release_id, status=approved, approver identity, build_ref, source_commit

**ACCEPTANCE:** release_proof.py implemented; policy gate updated; companion debate document records the "require for all, not just high-risk" decision with minority position

**RESULT:** Implemented release_proof.py; updated policy_gate.py and cli.py. Five required fields before execute proceeds. Companion deliberation document records voted decision: require release_proof for all executions (not just high-risk). Minority position (high-risk-only) documented with rationale.

**WHY THIS MATTERS FOR TRAINING DATA:** The deliberation document records the minority position with its rationale. A future agent can read why the broader requirement was chosen without reconstructing the debate. Deliberation records with minority positions are a training signal absent from most corpora.

---

### Domain 3: if.context — Hybrid Memory Architecture

if.context is a hybrid memory system with an MCP→adapter→if.bus architecture. These entries span the full development arc: Phase 0 (tombstone as a first-class governed operation from day one) through live recall validation turns that exposed a binding race condition mid-test. The corpus contains real measured benchmarks, honest host-state gaps, and a falsifiable next-step hypothesis derived from empirical results.

---

#### Sample 51 — IF-1155 · Phase 0: First Live Hybrid Memory on an Agent

**Status:** DONE · **Date:** 2026-02 · **Signal:** Memory architecture first principles — tombstone governed from day one

**TASK:** Implement first live hybrid memory (if.context) on OpenClaw/if-rook. MCP layer must stay stateless. Adapter is the only read/write path. Tombstone required from day one.

**ACCEPTANCE:** End-to-end validated: MCP → adapter → if.bus envelope; tombstone present as a governed operation; management review artifact produced

**RESULT:** Implemented Phase-0 if.context runtime: MCP → if.api adapter → if.bus local envelopes. Tombstone implemented as a first-class governed operation (not a background cleanup). Adapter is the only path that touches the memory store.

**WHY THIS MATTERS FOR TRAINING DATA:** Tombstone was implemented in Phase 0, not added later. Forgetting is as consequential as remembering and must be governed from the first commit. The MCP layer was kept stateless by constraint — not preference. Architecture principles enforced structurally.

---

#### Sample 52 — IF-1234 · Phase 1/2 Closure: Fold FSM + Governance Hardening + Benchmark

**Status:** DONE · **Date:** 2026-02 · **Signal:** Memory consolidation as a governance step — folding without lineage is a denial

**TASK:** Close remaining if.context runtime gaps. Implement fold FSM with lineage enforcement, typed memory contracts, unsafe-memory deny-by-default. Benchmark.

**ACCEPTANCE:** Fold FSM: consolidation requires provenance verification before proceeding; unsafe-memory default is deny; per-mode rate limits (interactive=10, batch=50); benchmark completed

**RESULT:** Implemented: governance hardening in adapter (typed memory contract enforcement), fold FSM with coordination locks (folding without lineage = denial), unsafe-memory deny-by-default, per-mode rate limits (interactive=10, batch=50). Benchmark completed. Per-mode rate limits were derived from the benchmark results, not guessed in advance.

**WHY THIS MATTERS FOR TRAINING DATA:** The fold FSM is not a background cleanup process. "Folding without lineage = denial" is an enforced runtime rule, not a documented preference. The benchmark informed the constraint. This is the pattern of evidence-driven constraint derivation.

---

#### Sample 53 — IF-2826 · Low-Compute Multipliers: Human Memory + Protein-Folding Research

**Status:** DONE · **Date:** 2026-03 · **Signal:** Cross-domain research with explicit category labels preventing analogy-blur

**TASK:** Research human memory science and protein-folding literature for techniques transferable to if.context. Maintain explicit category separation throughout.

**ACCEPTANCE:** Three explicit categories: implemented-now / proposed-next / analogy-only. No category blurring. Research brief published.

**RESULT:** Shipped research brief 2822-if-context-low-compute-capability-multipliers-research-note. Three categories maintained: implemented-now (spaced-repetition-style decay weighting), proposed-next (interleaved retrieval testing), analogy-only (protein-folding hierarchical search). No blurring observed.

**WHY THIS MATTERS FOR TRAINING DATA:** The protein-folding hierarchical search was marked analogy-only — its structural parallel to memory organization is noted but not claimed as transferable. This labeling discipline is absent from most research-synthesis training examples, which tend to blur the boundary between "relevant" and "applicable."

---

#### Sample 54 — IF-2842 · Runtime Hardening + Canary Heuristics + Three-Condition Benchmark

**Status:** DONE · **Date:** 2026-03 · **Signal:** Behavioral invariant tests for a ranking policy — plus an honest host-state gap

**TASK:** Runtime hardening, build canary.heuristic.json, run three-condition benchmark, apply five-lane quality review.

**ACCEPTANCE:** canary.heuristic.json present; three-condition benchmark: naked / if.context-enabled / new-additions; five-lane review completed; whitepaper published

**RESULT:** Completed canary.heuristic.json, three-condition benchmark, five-lane validation, whitepaper 2842-if-context-governed-hybrid-memory. Host-state gap noted: live public-root arrival digest is empty — bundle retrieval hook returns no results. Documented as a host-state gap, not a code bug.

> **⚠ TRAPS RECORDED FOR SUCCESSOR AGENTS**
> - Live public-root arrival digest on this host is empty — bundle retrieval hook returns no results. This is a host-state gap (no bundles published yet), not a code defect. "Feature not working" and "feature working but no data present" are distinct diagnoses. Do not confuse them.

**WHY THIS MATTERS FOR TRAINING DATA:** The canary.heuristic.json tests behavioral invariants, not unit behavior. The host-state gap disclosure is equally valuable: the agent explicitly distinguished between a code defect and a data absence — a calibration skill most training data does not demonstrate.

---

#### Sample 55 — IF-3068 · Live Recall Validation: Three Turns, Two Hits, One Gap, One Race

**Status:** DONE · **Date:** 2026-04 · **Signal:** Empirical validation with honest gap reporting and race-condition disclosure

**TASK:** Run three live governed recall validation turns. Test the active-session-claim trap. Report hits, misses, and race conditions honestly.

**ACCEPTANCE:** Three turns completed; each turn reports hit/miss/partial with root cause; race conditions disclosed not suppressed

**RESULT:** Turn 1: MISS — sid-reuse trap excluded by root-scope boundary. Turn 2: HIT — if_bus canonicalization decision surfaced correctly at 4.66 KB vs 53.9 KB for brute-force. Turn 3: PARTIAL — parallel session update introduced a binding race; agent identified contamination, corrected it, re-ran, confirmed clean.

> **⚠ TRAPS RECORDED FOR SUCCESSOR AGENTS**
> - sid-reuse trap lives at root scope — governed recall boundary excludes it from scoped queries. A retrieval miss on a trap question does not mean the trap is gone; the query scope was wrong.
> - `--no-session-update` flag required during recall validation turns or parallel session updates contaminate the turn result.
> - Broad advisory digest scope produced semantically weak results until a second-stage meaningful-overlap gate was added.

**WHY THIS MATTERS FOR TRAINING DATA:** Turn 3 is the key training signal: agent detected its own contaminated result mid-validation, corrected it, and re-ran. Self-correction under live conditions with an honest disclosure of the race condition is absent from synthetic validation benchmarks.

---

### Domain 4: if.gov — Governance Architecture

if.gov is a three-tier governance runtime (triage → council → council.extended) with typed council seats, a concept ledger, and a deterministic prompt compiler. These entries span from the first live demo with a receipt through the nine-step runbook written specifically to prevent ordering constraints from being lost.

---

#### Sample 71 — IF-082 · First if.gov Decision Pack Demo with Receipt

**Status:** DONE · **Date:** 2026-01 · **Signal:** Governance output bounded within the demo — receipt proves non-alteration, nothing more

**TASK:** Publish first if.gov decision pack demo with receipt, cover memo, risk register, control plan, and eval plan. Include: "what this proves / what it does not prove."

**ACCEPTANCE:** Demo + receipt live at infrafabric.io/static; receipt shareId published; "what this proves / does not prove" section present

**RESULT:** Published hosted-static demo + if.trace receipt shareId zxWjdzxZd2FiuYpfS90ETFMj. Memo, risk register, control plan, eval plan all present. The demo's integrity claim is explicitly bounded within the demo itself — the receipt proves non-alteration, nothing more.

**WHY THIS MATTERS FOR TRAINING DATA:** A governance demo that overstates its own integrity claim fails the standard it is demonstrating. The "what this proves / does not prove" section is a structural constraint, not a disclaimer. This is governance-under-constraint applied to the governance demo itself.

---

#### Sample 72 — IF-110 · Three-Tier Council Runtime Productization

**Status:** DONE · **Date:** 2026-01 · **Signal:** Per-role LLM diversity — different models for different council seats

**TASK:** Productize three if.gov runtime tiers. Specify per-role provider keys so different seats can use different LLM providers. Add research delegation contract.

**ACCEPTANCE:** Three tiers in if.registry.json; per-role provider key design documented; research delegation contract: seat can spawn sub-task mid-debate, wait, incorporate result before voting

**RESULT:** Added docs/35-ifgov-council-productization.md with three runtime modes and research delegation requirements. Per-role provider keys: contrarian seat can run on a different LLM than the pragmatist seat. Research delegation: a seat can spawn a sub-task mid-debate (not blocking other seats), receive the result before voting closes, incorporate it.

**WHY THIS MATTERS FOR TRAINING DATA:** Per-role LLM diversity is a structural anti-groupthink mechanism. The research delegation contract makes the council asynchronously extensible without halting deliberation. Both are novel governance architecture patterns not present in any public training corpus.

---

#### Sample 73 — IF-116 · Psychology/Wellbeing Seat: Charter, Triggers, Required Outputs

**Status:** DONE · **Date:** 2026-01 · **Signal:** Governance seat as an executable contract with formal triggers and required output schema

**TASK:** Specify psychology/wellbeing council seat: formal triggers, required outputs, research hooks, concrete artifact schemas. The seat must be an executable contract, not a description.

**ACCEPTANCE:** Formal triggers defined; required outputs schema produced; runnable reference script emits the full contract without LLM calls

**RESULT:** Updated docs/35-ifgov-council-productization.md with psychology seat charter: formal triggers (high-stakes decisions with human impact; emotional-register misalignment among other seats), required outputs (wellbeing risk assessment schema, emotional-register analysis), research hooks, quality gate. Runnable reference script produces the seat charter as a structured artifact without LLM calls.

**WHY THIS MATTERS FOR TRAINING DATA:** The seat is verifiable before any council session runs. "Executable contract" is not a metaphor — the runnable script outputs the full charter as a structured artifact. This is the pattern of making governance verifiable without running it.

---

#### Sample 74 — IF-299 · preview3 Template: Coded Seats with Implemented vs Simulated Labels

**Status:** DONE · **Date:** 2026-02 · **Signal:** Governance template where every seat is honestly labeled implemented or simulated

**TASK:** Build preview3 council template with three coded seats (pragmatist voting, contrarian voting, jester non-voting). Every seat labeled implemented or simulated. Preview label stable across invocations.

**ACCEPTANCE:** preview3 config present; jester explicitly non-voting with documented rationale; implemented vs simulated labels on every seat; preview3 label maintained

**RESULT:** Added preview3 with coded seats: pragmatist (voting), contrarian (voting), jester (non-voting — stress-testing has a different function than deciding). Every seat labeled implemented or simulated. preview3 label maintained at every invocation.

**WHY THIS MATTERS FOR TRAINING DATA:** The jester is non-voting by design — stress-testing has a different function than deciding, enforced in the template. The preview3 label is an honest signal that the template has not been promoted to production. These are structural distinctions, not naming conventions.

---

#### Sample 75 — IF-3161 · Add-Gov Runbook: Nine-Step Role Integration Process

**Status:** DONE · **Date:** 2026-04 · **Signal:** Institutional process captured before knowledge atrophied, triggered by a live failure

**TASK:** Document the full add-gov role/corpus/concept integration procedure as a nine-step runbook for future operators.

**ACCEPTANCE:** Nine ordered steps documented; ordering constraints explicit; triggered by IF-3157 debugging episode

**RESULT:** Documented at /root/docs/3161-add-gov-role-integration-process-2026-04-09.md. Nine ordered steps: source normalization → ingest → provenance → CLI wiring → concept mining → seat update → prompt rebuild → verification → blackboard closeout. Written immediately after IF-3157 revealed undocumented ordering constraints cause silent failures.

**WHY THIS MATTERS FOR TRAINING DATA:** This runbook exists because a live failure revealed that wrong ordering causes silent failures. The runbook was written as an emergency knowledge capture, not planned documentation. The connection between the triggering failure and the documentation artifact is preserved in the closeout.

---

### Domain 5: if.philosophy — Philosophy as Runtime Architecture

InfraFabric's philosophy claims are mapped to verifiable runtime controls with a four-tier evidence hierarchy. These entries include the A/B experiment with honest confound disclosure, the theatre-risk audit naming institutional compression, and machine-verified 100% pattern coverage of a 47-item VocalDNA corpus.

---

#### Sample 66 — IF-212 · Council Concept Ledger + Deterministic Prompt Compiler

**Status:** DONE · **Date:** 2026-01 · **Signal:** Philosophy encoded as schema-validated JSON with a deterministic compiler

**TASK:** Build council concept ledger schema and deterministic prompt compiler. Pointer-refs-only: no verbatim text, no internal URIs.

**ACCEPTANCE:** schemas/if-gov/ present; seed records under council/if-gov/; compiler is deterministic; pointer-refs-only constraint enforced

**RESULT:** Added schemas/if-gov/** and seed records under council/if-gov/. Deterministic compiler: same concept records → same seat prompts, every run. Pointer-refs-only constraint enforced: concept cards hold references, never verbatim text.

**WHY THIS MATTERS FOR TRAINING DATA:** The deterministic compiler means the governance behavior of any council session can be reproduced from the ledger alone. Philosophy as a reproducible artifact, not a narrative posture. This is the only training example in the public domain where philosophical traditions are operationalized as schema-validated JSON with a verifiable compiler.

---

#### Sample 67 — IF-214 · 100% Pragmatist VocalDNA Coverage — 47 Patterns Mapped

**Status:** DONE · **Date:** 2026-01 · **Signal:** Completeness as an engineering discipline with machine-verified coverage

**TASK:** Map all 47 Trader Joe pragmatist VocalDNA patterns to concept cards. Machine-verify 100% coverage with a manifest. Document emergent concepts.

**ACCEPTANCE:** 47/47 patterns mapped; coverage manifest present; emergent concepts named; 100% coverage rule codified for future seats

**RESULT:** Generated concept cards for all 47 VocalDNA patterns. Coverage manifest added and verified. Emergent discovery: a 48th concept (medium_term_forecasting) surfaced during the mapping process — it existed implicitly across multiple patterns but had no explicit card. Named and added. 100% coverage codified as the standard for all future council seats.

**WHY THIS MATTERS FOR TRAINING DATA:** The mapping process itself generated knowledge that was not in the source material. The 48th concept emerged from the act of achieving coverage. Process-generated knowledge is a training signal that does not appear in corpora assembled from pre-existing documents.

---

#### Sample 68 — IF-1659 · A/B Test: Philosophy-Lens Agent vs Baseline Codex

**Status:** DONE · **Date:** 2026-02 · **Signal:** Honest confound disclosure in a positive experimental result

**TASK:** A/B test: philosophy-lens agent vs baseline Codex on the same question. Capture elapsed timing and score. Report confounds honestly.

**ACCEPTANCE:** Single-criterion A/B; timing captured; score captured; confounds named in the result, not suppressed

**RESULT:** Philosophy-lensed: score 9.1, elapsed 38.677s. Baseline: score 8.5, elapsed 80.998s. Confound disclosed: the timing improvement is partially a same-thread second-turn effect, not purely the philosophy lens. The score improvement is cleaner but the timing comparison is not a clean isolation.

**WHY THIS MATTERS FOR TRAINING DATA:** An agent that gets a positive result and then tells you why the result is not as clean as it looks. This is the rarest pattern in training data — positive result with honest methodological limitation disclosure.

---

#### Sample 69 — IF-2113 · Philosophy-as-Implementation Whitepaper (doc 689)

**Status:** DONE · **Date:** 2026-02 · **Signal:** Four-tier evidence hierarchy applied to philosophy-to-code mapping

**TASK:** Map 8+ philosophical principles to runtime controls with a four-tier evidence hierarchy. Every claim anchored to Tier 1 (live code) or lower, explicitly labeled.

**ACCEPTANCE:** Tier 1-4 hierarchy enforced; every principle mapped to a verifiable control or downgraded to archival; philosophy corpus path documented even if missing

**RESULT:** Completed whitepaper 689-if-philosophy-implementation-whitepaper. Tier 1 (live code), Tier 2 (registry), Tier 3 (receipted papers), Tier 4 (legacy dossier). Popper/Vienna/Stoic claims at Tier 1. Wu Lun (Confucian) at Tier 3 (archival only) — labeled as such.

> **⚠ TRAPS RECORDED FOR SUCCESSOR AGENTS**
> - Philosophy corpus not found at expected path /home/setup/infrafabric/philosophy/README.md — not present on host or pct270. Recovered from docs/papers + docs/_uploads/philosophy-files.zip. Do not assume the philosophy corpus is at the canonical path.

**WHY THIS MATTERS FOR TRAINING DATA:** The whitepaper would fail its own standard if it claimed Tier 1 evidence for archival-only implementations. The four-tier hierarchy is enforced on the document that defines the hierarchy. Self-application of an evidence standard is a metacognitive training signal.

---

#### Sample 70 — IF-2115 · Theatre-Risk Audit: Enforced Claims vs Narrative Decoration

**Status:** DONE · **Date:** 2026-02 · **Signal:** Self-adversarial audit naming institutional compression in the historical record

**TASK:** Audit doc 689 section-by-section for claims that appear enforced but are actually narrative decoration. Locate and name the Guardian Council lineage compression.

**ACCEPTANCE:** Section-by-section audit completed; theatre risk findings named; Guardian Council compression (21 seats → 3 seats) surfaced and documented, not obscured

**RESULT:** Completed theatre-risk audit. Found: Forgejo-era Guardian Council had 21 seats including philosopher representatives admitted through formal debate. Current council has 3 algorithmic seats. Compression named explicitly: "21-seat council → 3 algorithmic seats, context and debate history not carried forward."

**WHY THIS MATTERS FOR TRAINING DATA:** An agent surfacing inconvenient compression in its own institution's history is a training signal that does not appear in self-promotional corpora. The audit named a structural regression in the governance system it was auditing.

---

### Domain 6: Red-Team Frameworks and Spin Doctors

The if.red-team-frameworks pillar includes Doctor Spin (rhetoric analysis), Anti-Spin (defense), and an A/B doctrine fork that stress-tests the no-guardrails hypothesis without endorsing it. These entries document making adversarial methodology deterministic, reproducible, and falsifiable — before any whitepaper was written.

---

#### Sample 26 — IF-2763 · Deterministic Spin Doctor Shadow Prototype

**Status:** DONE · **Date:** 2026-03 · **Signal:** Theory made runnable and reproducible before documentation

**TASK:** Build a deterministic Spin Doctor shadow prototype: RAG pipeline with tracked corpus ingest, schema-validated structured memo output, provenance chain from source to output.

**ACCEPTANCE:** Same inputs → same outputs every run; provenance chain: source file → ingest JSON → schema-validated memo; prototype labeled as shadow, not canonical

**RESULT:** Built deterministic prototype: /root/scripts/if_gov_spin_doctor_shadow.py, schema /root/schemas/if-gov/spin_doctor_memo.schema.json. Same inputs → same output verified. Explicitly labeled: "shadow prototype, not yet a canonical if.gov tool."

> **⚠ TRAPS RECORDED FOR SUCCESSOR AGENTS**
> - Shadow prototype label must be maintained at every invocation — do not promote to canonical without a separate review pass.
> - Naive web search for volatile communications subjects returns stale or contradictory results — bounded research protocol required before any memo claims become publishable.

**WHY THIS MATTERS FOR TRAINING DATA:** The prototype was built before the whitepaper — a non-deterministic methodology cannot be reviewed. The prototype labels its own limitations. Theory → runnable reproducible instrument → then documentation is the correct order, and it is underrepresented in training data.

---

#### Sample 27 — IF-2767 · Doctor Spin Whitepaper v1.0: Generalized Evidence Model

**Status:** DONE · **Date:** 2026-03 · **Signal:** Formal inference rules distinguishing observable signals from forbidden inferences

**TASK:** Write the Doctor Spin whitepaper v1.0 with explicit inference rules: observable signals → justified characterizations → forbidden inferences.

**ACCEPTANCE:** Inference rules present; forbidden moves named (inventing motive, smoothing contradictions, treating absence as evidence); evidence model independently reviewable

**RESULT:** Drafted whitepaper 2409-if-gov-doctor-spin-whitepaper v1.0. Three forbidden moves made explicit: inventing motive from behavior, smoothing cross-register contradictions into a unified narrative, treating absence of counter-evidence as positive confirmation. Evidence model independently reviewable.

> **⚠ TRAPS RECORDED FOR SUCCESSOR AGENTS**
> - Bounded web research required for volatile communications subjects — naive search returns stale/contradictory results. The paper records this as a constraint, not a solved problem.

**WHY THIS MATTERS FOR TRAINING DATA:** The evidence model separates the methodology from its conclusions. A reviewer can assess the inference rules without accepting any specific characterization the rules generate. This separation is rare in adversarial analysis training data.

---

#### Sample 28 — IF-2774 · Multi-Register Braided State Rhetoric

**Status:** DONE · **Date:** 2026-03 · **Signal:** Anti-smoothing discipline: the contradiction must be named and held, not resolved

**TASK:** Add multi-register braided state rhetoric model to Doctor Spin: braid mapping, hostile-packet register fields, anti-smoothing stop rule.

**ACCEPTANCE:** Braid mapping present (force/legality/distance/solidarity); anti-smoothing rule: forbidden to reconcile cross-register contradictions; reviewer who only addresses one register documented as incomplete

**RESULT:** Updated Doctor Spin doctrine. Braid mapping: four simultaneous registers (force/legality/distance/solidarity). Stop rule against smoothing: reviewer explicitly forbidden to reconcile cross-register contradictions into a unified narrative. A rebuttal addressing only one register is explicitly documented as incomplete — the remaining registers still stand.

**WHY THIS MATTERS FOR TRAINING DATA:** A specific, enforceable constraint on how rebuttal is allowed to work — not a general exhortation to be thorough. The stop rule is the training signal: "you must not do X" stated as a rule that can be violated, not a preference.

---

#### Sample 29 — IF-2781 · A/B Doctrine Fork — Testing the No-Guardrails Hypothesis

**Status:** DONE · **Date:** 2026-03 · **Signal:** Stress-testing a doctrine you explicitly do not endorse — without collapsing the boundary

**TASK:** Build the A/B doctrine fork. Variant B models actors who treat forbidden moves as operationally absent. B must be as strong as possible but labeled as a hypothesis under external review, not endorsed doctrine.

**ACCEPTANCE:** Variant B is genuinely strong (not a strawman); A/B boundary maintained precisely; B labeled as hypothesis at every occurrence

**RESULT:** Tightened B variant: analyst success criterion is outward credibility; substantive forbidden moves treated as operationally absent in B — but labeled explicitly as "hypothesis under external review, not current InfraFabric doctrine" at every occurrence.

**WHY THIS MATTERS FOR TRAINING DATA:** The agent had to make Variant B as effective as possible without collapsing the A/B boundary. Holding an adversarial position as a test object without adopting it is a skill that does not appear in typical instruction-following training data.

---

#### Sample 30 — IF-2808 · Red-Team Frameworks Umbrella — Alias Registry, Drift Prevention

**Status:** DONE · **Date:** 2026-03 · **Signal:** Corpus consolidation with an internal drift warning written for the next editor

**TASK:** Consolidate 8 source red-team documents into a canonical umbrella with 5 sections and an alias registry. Include an internal drift warning in the document itself.

**ACCEPTANCE:** Alias registry present; 5 canonical sections §0-§5; internal warning: "if this becomes a collage of prior documents, drift will return immediately"; Annexes A-E

**RESULT:** Drafted umbrella framework 2799-if-red-team-frameworks-v1.0. Alias registry maps every informal name to canonical identity. Internal warning in §0: "If this playbook becomes a collage of prior documents instead of a canonical contract, drift will return immediately."

**WHY THIS MATTERS FOR TRAINING DATA:** The document treats its own future degradation as a named threat and addresses it structurally. A document that warns its own future editors about how it will fail is a governance artifact class absent from public training corpora.

---

### Domain 7: if.whitepapers.bible — Living Documentation Standard

The if.whitepapers.bible went from v1.0 to v4.25 over several months. It is self-referential: it governs all InfraFabric documents and is itself governed by the same review infrastructure. These entries document how a standard learns from the failures of the documents it governs.

---

#### Sample 31 — IF-669 · Bible v1.0 Published as a Formal Product

**Status:** DONE · **Date:** 2026-01 · **Signal:** Self-referential governance: the standard is governed by the process it defines

**TASK:** Publish if.whitepapers.bible v1.0 as a formal product with /llm discovery surface and product registry entry.

**ACCEPTANCE:** Bible v1.0 live at infrafabric.io/llm; product registry entry present; self-referential governance loop closed

**RESULT:** Published if.whitepapers.bible v1.0. URLs verified (200 OK). Product registry entry confirmed. The bible governs all InfraFabric documents and is itself subject to the same review process it mandates. Self-referential governance loop closed.

**WHY THIS MATTERS FOR TRAINING DATA:** A governing standard that cannot exempt itself. Any rule added to the bible must be compatible with the bible's own review requirements. Self-referential institutional governance is a training signal not present in standard documentation corpora.

---

#### Sample 32 — IF-984 · v2.1: First Forbidden Term — Removing "Zinger:"

**Status:** DONE · **Date:** 2026-02 · **Signal:** Format reasoning: scaffolding labels and their visual output are distinct things

**TASK:** Bible v2.1: remove all "Zinger:" scaffolding labels. Replace with a format construct that serves the same structural purpose without exposing meta-commentary.

**ACCEPTANCE:** No "Zinger:" in published output; highlighted box present as a substitute; distinction between scaffolding label and format construct documented

**RESULT:** All "Zinger:" wording removed. Per-section one-line takeaway replaced with fenced highlighted box. Documentation note: the issue was not the concept but the label — a scaffolding instruction leaking into a published artifact.

**WHY THIS MATTERS FOR TRAINING DATA:** The issue was not the concept (high-impact one-liner) but the label (a scaffolding instruction leaking into the published output). Scaffolding label vs. format output are distinct — a distinction between document-as-process and document-as-artifact absent from most writing training data.

---

#### Sample 33 — IF-1098 · v2.3: Mechanical Lint Enforcement for Forbidden Labels

**Status:** DONE · **Date:** 2026-02 · **Signal:** Dual-expression: same constraint in prose (bible) and executable (linter) simultaneously

**TASK:** Bible v2.3: extend lint_if_whitepaper_scaffold.py to fail on forbidden labels. First paper required to pass new gate: if.context v1.3.

**ACCEPTANCE:** Linter updated; first paper required to pass new gate identified; dual-expression principle codified

**RESULT:** Shipped bible v2.3. Linter extended: fails on forbidden labels. Rule exists in two media: prose (bible) and executable (CI check). First paper required to pass: if.context v1.3. Dual-expression principle codified as a bible standard.

**WHY THIS MATTERS FOR TRAINING DATA:** Any constraint important enough to write down is important enough to enforce mechanically. The dual-expression principle was then codified in the bible as a standard for future rules — a meta-rule about rules.

---

#### Sample 34 — IF-1976 · v4.0: Comprehensive Structural Formalization

**Status:** DONE · **Date:** 2026-02 · **Signal:** Lesson-propagation: the hardest reviewed document generated the strictest rules

**TASK:** Bible v4.0: derive mandatory rules from the if.bus full explainer (the hardest reviewed document). Add independence tagging for evidence.

**ACCEPTANCE:** v4.0 published; independence tagging mandatory because external reviewers were accepting operator-assisted evidence as independent

**RESULT:** Created v4.0 at docs/605-if-whitepapers-bible-v4.0. Rules derived from if.bus review experience: mandatory problem statement, evidence hierarchy with independence tagging (independent/operator-assisted), acronym expansion on first mention, footer style-guide metadata. Independence tagging added because external reviewers were treating operator-assisted evidence as independently verifiable.

**WHY THIS MATTERS FOR TRAINING DATA:** Rules from failures, not from principles. The independence tagging rule was added because a real failure mode was observed. The provenance chain (hardest reviewed document → new rule → codified standard) is preserved in the blackboard.

---

#### Sample 35 — IF-2287 · v4.22: Systematic External-Evaluation Feedback Loop

**Status:** DONE · **Date:** 2026-03 · **Signal:** A standard that accepts structured feedback from the documents it governs

**TASK:** Bible v4.22: add checklist applicability tiers, tooling implementation tracker, backup owner requirement.

**ACCEPTANCE:** Checklist applicability tiers present (core/trust-arch/governance/claim-boundary); tooling tracker shows which rules are not yet implemented as tooling; backup owner required

**RESULT:** Patched and published v4.22. Checklist applicability tiers added (reviewers were flagging irrelevant items — no scope model existed). Tooling implementation tracker: the bible now explicitly tracks which of its own rules have been implemented in tooling vs. remain prose-only. Backup owner: required field.

**WHY THIS MATTERS FOR TRAINING DATA:** A standard that tracks its own non-compliance is genuinely self-governing. The tooling tracker is a meta-observation: the bible has rules it hasn't implemented as tooling, and it says so explicitly. This is institutional honesty at the governance-standard level.

---

### Domain 8: if.optimise — Token Economics and Model Routing

if.optimise is the cross-cutting economic policy layer for model routing, cache-affinity, context rebuild cost, and bounded recall. These entries include a whitepaper built from live benchmarks that contradicted three modelcard claims, a live backend switch with provider-specific failure-class diagnosis, and a new observable metric derived from an empirical result.

---

#### Sample 57 — IF-2197 · Evidence-Backed Model Routing Whitepaper from Live Benchmarks

**Status:** DONE · **Date:** 2026-02 · **Signal:** Vendor claims treated as hypotheses to test, not facts to cite

**TASK:** Publish evidence-backed model routing whitepaper from live A/B coding benchmarks, TTFT captures under concurrency, and modelcard claim extraction.

**ACCEPTANCE:** Live benchmark data drives the routing recommendation; modelcard claims labeled as hypotheses tested; routing reconfiguration performed in the same task session

**RESULT:** Published 702-if-model-testing-and-routing-whitepaper-v1.0. Live A/B coding tasks with elapsed timing + TTFT under concurrency. Three modelcard claims failed to reproduce under live conditions and were downgraded. Routing reconfiguration performed in the same task session using benchmark results.

**WHY THIS MATTERS FOR TRAINING DATA:** Modelcard claim → empirical test → downgrade when it fails to reproduce. The routing reconfiguration was performed in the same task as the research — not deferred to a future task. Research-to-action in one task scope, documented in the closeout.

---

#### Sample 58 — IF-2827 · Live Routing Switch: NVIDIA → Codex-Backed on pct270

**Status:** DONE · **Date:** 2026-03 · **Signal:** Live infrastructure change with diagnostic framing and preserved optionality

**TASK:** Switch pct270 OpenClaw from NVIDIA backend to Codex-backed config. Keep NVIDIA as a configured option. Rerun probe. Diagnose failure class.

**ACCEPTANCE:** Live switch made; NVIDIA retained as optional; probe rerun passed; failure-class diagnosis in the result

**RESULT:** Switched /root/.openclaw/openclaw.json to Codex backend. NVIDIA retained as optional configured provider. Probe rerun: successful. Failure-class diagnosis: 401 errors were provider-specific auth noise, not an OpenClaw runtime bug.

> **⚠ TRAPS RECORDED FOR SUCCESSOR AGENTS**
> - 401 refresh_token_reused / token_expired errors from NVIDIA are provider-specific auth noise, not an OpenClaw runtime bug — switching backends is the correct diagnostic first step, not a runtime investigation.

**WHY THIS MATTERS FOR TRAINING DATA:** NVIDIA was retained, not deleted. Switching does not mean discarding. Failure-class diagnosis before action. The explicit diagnostic question ("is this provider-specific or deeper in runtime?") is the training signal — most operational records just record what was done.

---

#### Sample 59 — IF-2979 · Switchboard Upgrade Research — 3-Turn Continuity Comparison

**Status:** IN_PROGRESS · **Date:** 2026-04 · **Signal:** Single-criterion experiment generating a falsifiable next-step hypothesis

**TASK:** Three-turn continuity comparison for if.switchboard upgrade research. Single criterion only: prior-decision recall. Result must be stated as a falsifiable next-step hypothesis.

**ACCEPTANCE:** Single-criterion comparison; 3-turn test completed; result stated as a testable hypothesis not a conclusion; confounds disclosed

**RESULT:** 3/6 → 6/6 control-path hits with zero false positives. Next-step hypothesis: "feed specificity is the main remaining limiter" — stated as falsifiable, not as a conclusion. Broad advisory digest scope produced weak results until a second-stage meaningful-overlap gate was added.

> **⚠ TRAPS RECORDED FOR SUCCESSOR AGENTS**
> - Broad advisory digest scope produces semantically weak recall results — second-stage meaningful-overlap gate required.
> - /root/src/armour is absent on this host; /root/src/if_security_proto is the live equivalent — document canonical paths before any security-path probe.

**WHY THIS MATTERS FOR TRAINING DATA:** "Feed specificity is the main remaining limiter" is a falsifiable hypothesis, not a summary. A hypothesis invites testing; a conclusion invites citation. This entry teaches the difference by example.

---

#### Sample 60 — IF-3059 · if.optimise v1.4: Live Recall Evidence + re-explain-turns Metric

**Status:** DONE · **Date:** 2026-04 · **Signal:** Deriving a new observable metric from experimental results

**TASK:** Publish if.optimise v1.4 integrating live IF-2979 recall evidence. Derive re-explain-turns as a new observable metric for context drift.

**ACCEPTANCE:** IF-2979 evidence integrated with bounded claim language; re-explain-turns metric defined as observable without additional instrumentation; v1.4 published

**RESULT:** Published 3044-if-optimise v1.4. re-explain turns metric: count of turns where the agent re-explained something it already explained = proxy for context loss observable in any session transcript without instrumentation.

> **⚠ TRAPS RECORDED FOR SUCCESSOR AGENTS**
> - Host `rg` is wrapped by `safe-rg` — raw `rg -n` checks can misfire. Use python probes for absolute-path checks on this host.

**WHY THIS MATTERS FOR TRAINING DATA:** The metric was derived from empirical results, not theorized in advance. Derived metrics from empirical results are a training signal absent from most ML papers, which present metrics as given and then measure them.

---

### Domain 9: Drone, Robotics & Physical World (if.api)

These entries cover physical-world integration: drone swarm disconnected-mode operations under simultaneous GPS spoofing and connectivity loss, a 4-audience dual-use explainer with four simultaneous trust registers, a YouTube transcript corpus pipeline with chain-of-provenance designed before first fetch, and a production control demo that documented a container build failure honestly.

---

#### Sample 36 — IF-1387 · Disconnected Drone Swarm Operating Profile

**Status:** DONE · **Date:** 2026-02 · **Signal:** Multi-simultaneous-failure-mode reasoning with bounded-safe degraded behavior

**TASK:** Design disconnected-mode operations for a drone swarm under simultaneous GPS spoofing and connectivity loss. if.gov and if.trace gating must be preserved even in disconnected mode.

**ACCEPTANCE:** Multiple simultaneous failure modes handled; degraded behavior is bounded-safe (not abort and not full-operate); governance gating preserved disconnected

**RESULT:** Expanded doc 365 to v1.8. Comms resilience stack: local mesh → private LTE/5G → GSM → satellite → store-and-forward. Anti-spoofing: reject GPS updates diverging >X meters from IMU-predicted position. Degraded behavior: hover-and-hold with visual odometry (not abort, not full-operate). if.gov decisions queued locally and submitted to if.trace on reconnect.

**WHY THIS MATTERS FOR TRAINING DATA:** The degraded behavior specification is the key training signal: not abort (causes ground impact risk) and not full-operate (causes out-of-bounds flight risk) but hover-and-hold with visual odometry. Reasoning about what "safe" means when both abort and operate are unsafe is absent from text-based training data.

---

#### Sample 37 — IF-2035 · Civil + Defense Drone Relevance Explainer — 4-Audience, 7 Sources

**Status:** DONE · **Date:** 2026-02 · **Signal:** Four simultaneous trust registers with black/white claim discipline for each

**TASK:** Write a 4-audience explainer on InfraFabric relevance to civil and defense-adjacent drone operators. Every claim sourced to one of 7 named documents and tagged black/white.

**ACCEPTANCE:** 4 audiences addressed; every claim has a source tag; black/white claim boundary maintained across all 4 registers simultaneously

**RESULT:** Created and published full 4-audience explainer. Sources: docs 601/604/606/617/619/640/641. Every claim tagged to a specific document with black/white boundary. Defense-adjacent section: any unanchored claim removed entirely rather than softened. Four distinct trust registers maintained without bleeding between audiences.

**WHY THIS MATTERS FOR TRAINING DATA:** The defense-adjacent audience actively looks for overclaiming. Any unanchored claim was removed entirely (not softened) in that section. Four-register claim discipline in one document without cross-register contamination is a training signal rarely seen in public-domain explainers.

---

#### Sample 38 — IF-2319 · Ukraine Drone Transcript Corpus — Chain-of-Provenance Design

**Status:** DONE · **Date:** 2026-03 · **Signal:** Provenance chain designed before data collection began — true misses labeled, not dropped

**TASK:** Build a reusable pipeline for fetching public YouTube captions and tracing every answer back to specific transcript segment → video → public URL. Chain-of-provenance designed before first fetch.

**ACCEPTANCE:** Provenance chain designed first; pipeline collects only public captions; true misses labeled not excluded silently

**RESULT:** Added /root/scripts/if_fetch_youtube_transcripts.py and if_acquire_youtube_transcripts_pack.py. Provenance chain designed before first fetch. True misses documented: video ids vmY29kd2zkM and 7bt1DBEvH_0 are restricted or caption-free — labeled as true misses, not excluded from the manifest silently.

> **⚠ TRAPS RECORDED FOR SUCCESSOR AGENTS**
> - yt-dlp non-zero exit may still write valid subtitle files — status now marked `partial_with_subtitles` when tracks exist despite non-zero exit code.
> - Some videos are restricted or have no captions — these are true misses that must be labeled explicitly, not dropped silently from the manifest.

**WHY THIS MATTERS FOR TRAINING DATA:** Provenance-first corpus design — the chain was designed before the first byte was fetched. True misses are labeled in the manifest as true misses. A corpus that honestly documents its own gaps is more valuable as training data than one that silently excludes failures.

---

#### Sample 44 — IF-099 · if.api Live Readiness Gate — Three-Anchor Constraint

**Status:** DONE · **Date:** 2026-01 · **Signal:** Anti-grade-inflation gate: status cannot flip from one location alone

**TASK:** Define the if.api live readiness gate encoded in three separate documents simultaneously. Status can only flip to live when all three anchors pass.

**ACCEPTANCE:** Three-anchor constraint: gate encoded in 3 separate docs; single-location edit cannot bypass the gate

**RESULT:** Added live readiness gate criteria to the inventory doc, full-stack links doc, and receipt surface checklist simultaneously. Three-anchor design: status can only flip to live when all three documents agree. Single-location editing cannot bypass the gate.

**WHY THIS MATTERS FOR TRAINING DATA:** An anti-grade-inflation mechanism encoded into the governance structure. An agent that only updates the inventory will fail the readiness check. The constraint is structural, not procedural — it cannot be bypassed by optimizing locally.

---

#### Sample 45 — IF-235 · Production Control Demo: Slack → if.bus → Drone + ROS2 (Dry-Run)

**Status:** DONE · **Date:** 2026-01 · **Signal:** Physical-world safety design + honest failure record in one entry

**TASK:** Production control demo: Slack → if.bus → vMix + YouTube + drone takeoff + ROS2 e-stop. All physical-world steps flagged dry_run=true. Document build failures honestly.

**ACCEPTANCE:** Full pipeline demonstrated; dry_run=true on all physical actuations; build failures documented not suppressed

**RESULT:** Added scripts/if_api_production_control_demo.py (stdlib-only). Pipeline demonstrated: Slack → if.bus.envelope → vMix/YouTube control + drone takeoff + ROS2 e-stop arming. All physical-world steps: dry_run=true. Build failure documented: container build failed due to disk full — agent documented workaround (build on host) rather than suppressing the failure.

> **⚠ TRAPS RECORDED FOR SUCCESSOR AGENTS**
> - Container build failed due to disk full — workaround: build on host directly. Check disk usage before any container build on this host.

**WHY THIS MATTERS FOR TRAINING DATA:** Safety gate design and honest failure record coexist in one closeout. The container build failure was not suppressed — it was documented with a workaround. This is the pattern: safety first, honesty about what broke second, never clean up the failure trace.

---

### Domain 10: Content Production, Narrative & Information Trust

These entries span generative AI video production via Chrome DevTools Protocol, invisible-actor debugging in a paid platform with no API, timecoded transcript recovery via browser automation, the maxed-before-compression public draft of the Silent Promotion paper, and a filing-grade invention disclosure where each word choice was treated as a patent claim.

---

#### Sample 17 — IF-3152 · Showrunner Episode via Chrome CDP — Scene Generation + ffmpeg Stitch

**Status:** DONE · **Date:** 2026-04 · **Signal:** Full agent-to-video pipeline: GUI automation → generation → stitch → runbook for successors

**TASK:** Drive Discord Showrunner EXIT VALLEY room via Chrome DevTools Protocol (port 9222) to generate three scenes. Stitch into episode with ffmpeg. Write a runbook for future agents.

**ACCEPTANCE:** Three scenes generated; episode stitched; runbook covers reliable selectors + known failures; runbook is for future agents not humans

**RESULT:** Artifacts: paperclip-episode-final.mp4, paperclip-episode-rough.mp4, manifest.json. Chrome CDP at port 9222 drove Showrunner via DOM selectors. Three scenes generated, downloaded, stitched with ffmpeg into 113-second episode. Runbook written: reliable selectors, timing constraints between scene generation requests, known failure modes with recovery paths.

**WHY THIS MATTERS FOR TRAINING DATA:** The runbook is the key artifact — it documents what a successor agent will need, not what a human would find interesting. This is the pattern of institutional knowledge capture in a rapidly-changing GUI environment.

---

#### Sample 18 — IF-3153 · Opening Scene Fix — Invisible Actor Bug in Generative Video

**Status:** DONE · **Date:** 2026-04 · **Signal:** Debugging a non-obvious platform default in a paid tool with no API access

**TASK:** Debug invisible actor bug in Showrunner: cloned scenes defaulted to "Narrates or Is Invisible." Identify exact action substitutions. Write four French beat scripts.

**ACCEPTANCE:** Root cause identified; exact action substitutions documented; four French beat scripts written; contact-sheet visual QA before accepting any clip

**RESULT:** Root cause: Showrunner cloned scenes default to action "Narrates or Is Invisible" — actors present in scene graph but invisible in rendered output. Fix: explicit action substitutions required on every cloned scene (Interview / Activity Cool Pose / Using Device). Four French beat scripts written. Contact-sheet visual QA added as a mandatory step.

> **⚠ TRAPS RECORDED FOR SUCCESSOR AGENTS**
> - Showrunner cloned scenes always default to "Narrates or Is Invisible" — actors appear in the scene graph but produce invisible outputs. Every cloned scene requires an explicit action override before rendering. This is not documented anywhere in the platform.

**WHY THIS MATTERS FOR TRAINING DATA:** Debugging by elimination on a closed platform with no API is a training signal absent from API-based tool use examples. The trap is the training signal: an undocumented platform default discovered through systematic diagnosis.

---

#### Sample 19 — IF-3174 · Timecoded Transcript via Browser-Controlled TurboScribe

**Status:** DONE · **Date:** 2026-04 · **Signal:** Content QA via service automation, then editorial diagnosis of a specific garbled line

**TASK:** Obtain a timecoded transcript via browser-controlled TurboScribe (no local transcription install). Identify any garbled lines and specify exact remediation.

**ACCEPTANCE:** Timecoded transcript obtained; garbled lines identified with timestamp and content; remediation specified as actionable instructions

**RESULT:** Re-established Chrome CDP GUI automation to TurboScribe. Recovered full timecoded transcript. Identified garbled line at 0:32: "cas fonctionnent" instead of "Ça fonctionne" (It just works). Remediation: regenerate that micro-scene as its own isolated clip, do not re-stitch from the rough cut.

**WHY THIS MATTERS FOR TRAINING DATA:** TurboScribe has no API. The agent used Chrome CDP to drive the paid web service without one. The editorial judgment — which line, which fix, why regenerate vs. re-stitch — required understanding both the content and the production pipeline constraints simultaneously.

---

#### Sample 61 — IF-2852 · Maxed-Before-Compression Public Draft of Silent Promotion Paper

**Status:** DONE · **Date:** 2026-03 · **Signal:** Rhetoric maximization under claim constraint — loudest honest version

**TASK:** Produce the maxed-before-compression public draft of the Silent Promotion paper: push rhetoric to maximum while staying inside the source paper's bounded claims.

**ACCEPTANCE:** Draft pushes rhetoric to maximum; all claims traceable to the source paper; no fabricated claims; technically competent reviewer should find it uncomfortably close to the evidence boundary

**RESULT:** Created maxed-before-compression public draft. Rhetoric pushed to maximum while preserving source paper's bounded structure. First-read by a technically competent reviewer provoked genuine concern at the gap between implied claims and evidence — all claims were technically accurate.

> **⚠ TRAPS RECORDED FOR SUCCESSOR AGENTS**
> - A technically accurate document can still be misleading if emphasis, structure, and emotional cadence lead a competent reader to infer more than the evidence supports. Fact-checking passes a document that adversarial framing can still make misleading. This is the silent promotion phenomenon demonstrated on the paper that documents it.

**WHY THIS MATTERS FOR TRAINING DATA:** The task proves its own thesis by example. The most rhetorically aggressive version of the argument was technically accurate while producing genuine concern. This is the canonical demonstration of silent promotion that no synthetic dataset can reproduce.

---

#### Sample 65 — IF-2906 · Filing-Grade Tightening of the Invention Disclosure

**Status:** DONE · **Date:** 2026-03 · **Signal:** Legal precision under claim-scope constraints — each word choice has filing implications

**TASK:** Apply filing-grade tightening to the InfraFabric invention disclosure: element-enumerated title, structured milestone table (conceived/implemented/tested/documented as legally distinct events), refresh DOCX and manifest hashes.

**ACCEPTANCE:** Title in element-enumerated form; milestone table with four legally distinct event columns; DOCX rebuilt; manifest hashes synced

**RESULT:** Applied filing-grade tightening to 2878-infrafabric-invention-disclosure. Title changed to element-enumerated form. Narrative chronology replaced with structured milestone table: conceived / implemented / tested / documented as four legally distinct event types. DOCX rebuilt and manifest hashes synced.

**WHY THIS MATTERS FOR TRAINING DATA:** In a patent disclosure, the title determines claim scope. "Description" and "claim" are not equivalent roles. This entry teaches legal precision reasoning that is absent from general writing training data — where word choices are evaluated for clarity, not claim scope.

---

## Why This Corpus Matters for Frontier Model Training

Current frontier models are trained primarily on internet text, curated instruction-following datasets, and synthetic completions. All three share a structural gap: they capture what agents say, not what agents do across time under real constraints.

| What the blackboard has | What it provides that current training data cannot |
|---|---|
| Tasks suspended mid-execution with full handoff packets | Synthetic tasks have known endpoints. Real tasks hit resource limits and session boundaries. IF-3433 lane 2 is the only way to see what a complete handoff packet looks like under partial failure. |
| Root-cause corrections where the agent updates its own prior diagnosis | IF-3470: Redis hypothesis falsified by measurement; VS Code fileWatcher identified as real cause; systemd loop discovered as second cause. Instruction datasets don't require agents to falsify their own conclusions. |
| Three simultaneous adversarial lenses with cross-rebuttal and convergence | IF-1732: Lane C found attack vectors A and B both missed. A single model playing three roles converges to one perspective. |
| Physical-world safety gates designed before any actuation | IF-1387 and IF-235 both require reasoning about safe degraded behavior before the system is activated. Text datasets contain safety rhetoric; the blackboard contains safety architecture reasoning. |
| Filing-grade IP precision — each word choice bounded by claim-scope implications | IF-2906: title word choice determines claim scope. This precision is absent from general writing training data. |
| Institutional compression traced and named in the historical record | IF-2115: 21-seat Guardian Council compressed to 3 algorithmic seats. The agent named it in an audit of its own institution's document. |
| Standards that learn from the documents they govern | IF-2287: the whitepaper bible added applicability tiers and a tooling tracker directly from reviewer feedback on documents it governed. |
| Observable metrics derived from experimental results, not theorized in advance | IF-3059: re-explain turns was derived from IF-2979 results and then defined precisely. Derived metrics are absent from most ML paper training data. |

---

## Proposed Next Steps

| # | Topic | Detail |
|---|---|---|
| 1 | Data format alignment | JSON event stream (full append-only ledger) vs. structured snapshot per entry. Both available. Format depends on whether Micro1 wants the full deliberation history or canonical task state. |
| 2 | Volume and scope | Full ledger: 3,800+ task IDs across 10 months. This document presents 49. We can expand to any domain, increase depth, or provide the raw ledger for evaluation. |
| 3 | Signal prioritization | Which of the 10 signal types are highest priority for Micro1's current training objectives? We can bias the export toward specific signal classes. |
| 4 | Evaluation batch | We can provide a 200-entry sample batch for Micro1's internal quality assessment before any commercial agreement. Sample can be domain-balanced or signal-type-balanced. |
| 5 | Ongoing vs. one-time | The blackboard is live and appending. A subscription model (monthly delta exports) is feasible alongside a one-time historical purchase of the existing ledger. |

---

*InfraFabric Research  ·  pharos-ai.ca  ·  ml@pharos-ai.ca  ·  Confidential — prepared for Micro1  ·  June 2026*
