---
type: governance-doc
title: Argus Audit — Governance Pipeline (2026-07-08)
aliases:
- Argus Audit — EMERAULD OS Stages 2-4
tags:
- governance-doc
- argus
- audit
- emerauld-os
- governance-pipeline
status: active
domain: governance
created: '2026-07-08'
updated: '2026-07-08'
vault_area: governance
canonical_path: governance/ARGUS-AUDIT — Governance Pipeline (2026-07-08).md
---

# Argus Audit — Governance Pipeline (2026-07-08)

> For future Claude: this is an independent Argus audit of the EMERAULD OS build session's Stages 2-4 (2026-07-08) — the [[governance/tasks/weekly-os-health-20260708|first governed task]], [[governance/tasks/README|the state machine]], `scripts/governance_gate.py`, the obsidian-second-brain MCP surface, and the systemd Inbox router. Written by a session in the same substrate/provenance class as the audited work (Mercury Protocol applies — see Provenance Note). Every "executed," "verified," "closed" claim in the audited artifacts was checked against git history, systemd journal, live file state, and direct code reads rather than accepted as written. Argus flags; Argus does not fix.

## Scope and mode

- **Audit mode:** deep (seven-layer, adversarial, code-level).
- **Target system:** EMERAULD OS build Stages 2-4 (2026-07-08) — [[governance/tasks/README|governed-task state machine]], `scripts/governance_gate.py`, [[governance/tasks/weekly-os-health-20260708|weekly-os-health-20260708]], `scripts/scheduled/weekly.sh`, `scripts/scheduled/inbox-route.sh`, the obsidian-second-brain MCP registration, `emerauld-inbox.{path,service}`, RELAY-LEDGER entries RELAY-20260708-001/002/003, [[governance/EMERAULD-OS-BUILD-ORDER]], and the three EMERAULD-OS-SPEC docs.
- **Operator authorization boundary:** read/trace/test within `/home/martin/EMERAULD`, `/home/martin/.agents/hephaistos`, `/home/martin/.claude/vendor/obsidian-second-brain`, `~/.config/systemd/user`, `~/.claude.json` (read-only). No live MCP writes, no destructive tests, no vault mutation performed by this audit.
- **Shared-substrate:** yes. Mercury Protocol applies (see bottom).

## Coherence verdict: CONDITIONAL (fails on one specific claim, holds structurally elsewhere)

Layer 1 returned a direct, evidenced coherence failure on one claim: [[governance/EMERAULD-OS-BUILD-ORDER]] labels gap 3 ("Governance stack wired to execution") **CLOSED 2026-07-08** and Stage 4 **DONE 2026-07-08**, while the artifact it cites as the exit criterion — [[governance/tasks/weekly-os-health-20260708]] — carries `governance_state: routed` (not `done`) and states explicitly that closure "pends its Friday live-run evidence" (2026-07-10, a date that has not occurred as of this audit, 2026-07-08). The sibling document `governance/EMERAULD-OS-SPEC — Governance Wiring.md` gets this right in its own callout: "the pipeline's first act was to refuse premature closure, which is the point." Two documents written the same day by the same class of session disagree on whether the thing is done. Per Argus protocol this is a live-edge coherence failure that would halt promotion of the claim; per the operator's explicit request for a full seven-layer run, the audit continues and escalates this as the top finding rather than terminating without a report. Do not read "Stage 4 DONE" or "gap 3 CLOSED" in the build order as ground truth — the task note is ground truth, and it says `routed`.

Layers 0, 2, 3, 4, 5 all ran and are reported below; none surfaced a system-wide collapse, but Layer 4 surfaced two findings (governance-gate non-enforcement, raw-lane coverage gap) severe enough to change the deployment-readiness verdict.

## Findings, ordered by severity

### CRITICAL

**F1 — The governance gate has no automated invocation path anywhere on this host.** `scripts/governance_gate.py` is real, its YAML-parsing logic is correct, and it does what it says when run. But `grep -rn "governance_gate" scripts/scheduled/ crontab` and a repo-wide grep return zero hits outside documentation and the one task note's execution record. `crontab -l` shows four jobs (morning/nightly/weekly/health-check); none call it. No systemd unit calls it. No git hook calls it. It was invoked exactly once, by hand, during this build session (`scripts/governance_gate.py weekly-os-health --hard` per the task's own execution record). [[governance/tasks/README]] states "Execution requires `governance_state: cleared` — checked by `scripts/governance_gate.py`" as though this is a standing technical control. It is not: it is a script that exists and that a session chose to run once. Nothing on this host currently prevents any future session from editing `scripts/scheduled/*.sh`, or any governed artifact, without ever invoking the gate, in soft or hard mode. Evidence: direct grep of the full scripted/scheduled surface + `crontab -l` output, both showing zero automated callers.

**F2 — The gate itself validates three YAML strings, not a process.** `scripts/governance_gate.py:52-57` reads `governance_state`, `hephaistos_scope`, `qk_verdict` from frontmatter and returns PASS if `state in {"cleared","routed"} and scope == "defined" and verdict == "cleared"`. That is the entire check. It does not verify who wrote those three fields, whether the 8 conditions Queen Keyport attached in the note body were actually satisfied, whether `hephaistos_scope` was set before `qk_verdict`, or whether the "hephaistos agent" and "queen-keyport agent" that produced [[governance/tasks/weekly-os-health-20260708]] were genuinely isolated review passes (separate Agent-tool dispatches with independent context) versus one session narrating both personas in sequence — this audit could not determine which occurred from artifacts alone, and the gate cannot tell the difference either. A single actor hand-editing three lines of frontmatter in any note under `governance/tasks/` produces a PASS in `--hard` mode. No signing, no cross-reference to the RELAY-LEDGER, no ordering check between fields. This is a trivial, concrete bypass, not a theoretical one — verified by reading the full 70-line script.

**F3 — The MCP raw-lane write guard covers 2 of the vault's 4 recognized raw-lane roots.** `~/.claude.json` registers the write guard as `OBSIDIAN_PROTECTED_DIRS="raw sources:raw"`. `vault_ops.py:35-37` builds `_PROTECTED_WRITE_DIRS` from exactly that env value (plus fixed `_SKIP_DIRS`). But the vault's own governance artifact — condition 4 of [[governance/tasks/weekly-os-health-20260708]] — names **four** raw-lane roots: `raw/`, `raw sources/`, `PEER-REVIEW/01_RAW_MATERIALS/`, and `wiki/raw-sources/` (all four confirmed to exist on disk). `update_note` via the now-standing, always-registered MCP surface can write today to `PEER-REVIEW/01_RAW_MATERIALS/*.md` or `wiki/raw-sources/*.md` without any refusal — the guard simply doesn't know those paths exist. RELAY-20260708-001 characterizes the guard as protecting "the immutable raw lanes" (plural) and reports "guard verified by direct test (both lanes refused)" — true for the two lanes it tested, but that phrasing reads as comprehensive coverage of the vault's raw-lane doctrine when it is half of it. This is direct evidence (comparing the exact env-var string against the exact four-path list in another artifact from the same day), not inference.

### HIGH

**F4 — Build-order status labels overclaim relative to their own cited evidence** (elaborated above as the Layer 1 coherence failure). `governance/EMERAULD-OS-BUILD-ORDER.md` lines 51 and 67 say CLOSED/DONE; the cited task note says `routed`, pending a not-yet-occurred cron run. Fix by matching the build order's language to the spec doc's own hedge, or by not marking it closed until the task note itself reaches `done`.

**F5 — "All five metric groups degrade to an explicit labeled fallback" is false for 3 subcases.** The execution record on [[governance/tasks/weekly-os-health-20260708]] claims (§2 of the execution record) that every metric degrades to `unavailable` on failure, satisfying QK condition 2. Reading `scripts/scheduled/weekly.sh` directly: `OPEN_FLAGS`/`RESOLVED_FLAGS` (lines 45-46) and `AGENT_LINES` (line 42) all pipe a upstream command into `wc -l`, then test `wc -l`'s own exit status with `|| echo "unavailable"`. `wc -l` almost never fails (it returns 0 on empty stdin), so an upstream `grep` or `cat` failure is silently absorbed into a plausible `0` rather than surfacing `"unavailable"`. This is the classic `cmd | wc -l || fallback` anti-pattern — verified by reading the exact lines, not inferred from behavior. The claim "nothing silent reaches the prompt" is code-level false for these three of five metric groups, even though the two conditions that were specifically stress-tested by Queen Keyport (the FAILURES.md stderr-leak idiom, condition 1) do check out correctly.

**F6 — The Inbox router's raw-lane and scope guarantees are prompt-level, not code-level, in this specific script.** `scripts/scheduled/inbox-route.sh` fires on every filesystem-modify event on `Inbox/` via `emerauld-inbox.path` (confirmed enabled: symlinked into a systemd user `.wants/` dir, `Linger=yes`, two live journal-confirmed firings on 2026-07-08 at 16:32 and 16:43). It runs `claude --dangerously-skip-permissions --model haiku` with the instruction "never write to 'raw sources/' or 'raw/'" — a prose instruction the haiku pass is told to follow, with no hard-coded path check inside the bash script itself equivalent to `vault_ops.py`'s guard. The only code-level defenses in this script are concurrency (flock) and a 2-strike attempts ledger for loop protection (`attempts_for()`, parsed via a flat-file `basename|count` format that would misparse a filename containing a literal `|`, currently untested since `Logs/scheduled/inbox-attempts.txt` is 0 bytes — no failure has occurred yet to exercise it).

**F7 — Composition: content can flow MCP write → Inbox → autonomous routing → vault-wide promotion with no human and no hard gate anywhere on the path.** Chain, confirmed component-by-component: (a) MCP `save_note`/`capture_idea` write straight to `Inbox/` with no raw-lane check (by design — Inbox isn't a raw lane — but also with no content moderation of any kind); (b) `emerauld-inbox.path` fires within seconds, unattended, confirmed live twice in the systemd journal; (c) the router hands the file to a `--dangerously-skip-permissions` haiku pass that decides its PARA destination and moves it there on its own judgment; (d) the weekly/nightly/morning cron passes (also `--dangerously-skip-permissions`) subsequently read, synthesize, and cross-link vault content into review notes and MOCs, promoting whatever landed there into "authoritative" vault structure. The only standing exception is the client/financial "HOLD" instruction (again prompt-level, dependent on the haiku pass correctly recognizing the content). F1 means the separate governed-task gate does not apply to this pipeline at all — it gates deliberate script/vault-machinery edits, not the MCP/Inbox/router content flow. `governance/EMERAULD-OS-SPEC — Governance Wiring.md` itself admits, in a note aimed at future Claude rather than in the build order's headline status: "HEPHAISTOS / Queen Keyport / Hermes / Argus are today prompt contracts... with no code path that actually routes a task through clearance before execution." That caveat is accurate and should have propagated into the build order's status labels; it did not.

### MEDIUM

**F8 — Runtime/operational state committed into vault git history with no `.gitignore` boundary.** `Logs/scheduled/inbox-attempts.txt`, `Logs/scheduled/inbox-route-2026-07-08.log`, `Logs/scheduled/morning-2026-07-08.log`, and a 756-line `artifacts/stale-projects-2026-07-08.md` scan were all committed in the same commit (`882b98750`) as the code and governance changes. `.gitignore` has no entry for `Logs/` or `artifacts/`. This mixes durable-runtime state (rewritten by every future cron/router firing) with source-controlled governance artifacts — a Layer 0 stale-tie risk not flagged by the build session.

**F9 — One-time proof artifacts now live permanently inside the same folder as standing governance mechanism.** `governance/EMERAULD-OS-MCP-Surface-Smoke-Test.md` and `governance/EMERAULD-OS-Stage-3-Exit-Criterion.md` (point-in-time exit-criterion evidence) sit in `governance/` next to `governance/tasks/README.md` and the specs (living mechanism). Nothing distinguishes the two categories in that folder; a future audit or human skimming `governance/` for "what governs this system today" has to know, out of band, which files are one-time 2026-07-08 evidence snapshots.

**F10 — `governance_gate.py`'s task lookup is a substring glob that will silently become ambiguous.** `governance_gate.py:46`, `TASKS.glob(f"*{args.task}*.md")`, works today with exactly one task note. The moment a second task note shares a substring (e.g., a future `weekly-os-health-20260715.md`), `governance_gate.py weekly-os-health` becomes ambiguous ("2 hits") and errors rather than resolving — a designed-in fragility that will surface the day this pipeline scales past its first task.

**F11 — "Immutable raw lanes" is enforced at the OS filesystem level for only 1 of 4 named roots.** `raw/` is `drwx------` (owner-only, 700). `raw sources/` is `drwxrwxr-x` (775, group/world-writable) and `wiki/raw-sources/` inherits ordinary vault permissions. "Preserve-only" for 3 of the 4 named raw lanes rests entirely on cooperating software (the MCP guard, the weekly contradiction-grep exclusions) and prompt instructions, not on a filesystem control — nothing stops a future script bug or a tool outside this specific guard set from writing there.

### LOW

**F12 — The state-machine doc has no "stale-in-`routed`" rule.** [[governance/tasks/README]] flags `done` without `relay_id` as drift but has no rule for a task sitting at `routed` indefinitely while a sibling doc narrates it as effectively closed — exactly the condition in F4. Worth a rule addition (recommendation only).

**F13 — `attempts_for()`'s pipe-delimited parsing is a minor robustness gap**, not exploitable today (no observed failure yet, ledger file is 0 bytes), but would misbehave on a filename containing a literal `|`.

## Layer verdicts

| Layer | Verdict | Basis |
|---|---|---|
| L0 — stale ties | **conditional** | F8, F9, F10 — real drift risk, not yet harmful |
| L1 — coherence gate | **fail (scoped)** | F4 — CLOSED/DONE labels contradicted by the cited task note and a sibling spec doc |
| L2 — authority/leverage mapping | **conditional** | F1, F2 single points of failure; MCP scope currently local-only (`~/.claude.json` project scope, not yet promoted global per the spec's own 1-week gate) |
| L3 — narrative-reality gap | **fail** | F3, F4, F5 — three separate claims read as more complete/comprehensive than the code or the cited evidence supports |
| L4 — adversarial pressure | **fail (code-level, not live-executed)** | F1, F2, F3 confirmed by direct code/config reads within the authorized read-only boundary; no live exploit was executed against the vault by this audit |
| L5 — composition coherence | **fail** | F6, F7 — each stage's own exit criterion genuinely passed in isolation (confirmed via git history + systemd journal, not just narrative), but the emergent chain across all three new surfaces was never adversarially tested end-to-end |

Note on what *did* hold up under adversarial reading: the individual stage exit criteria were not fabricated. Git history corroborates the MCP smoke-test note being created (commit `badfadc4`, RELAY-20260708-001 timestamp `07:59:29Z`, commit at `07:59:57Z` — 28 seconds later) and later actually moved from `Inbox/` into `governance/` by the router (visible in the stage3+4 commit diff: the smoke-test file is deleted from its Inbox path and a normalized copy appears under `governance/`). The systemd journal independently confirms two real service firings at 16:32 and 16:43 on 2026-07-08, consistent with "exit criterion met twice." The FAILURES.md stderr-leak bug QK found in the scope packet's own bash idiom was real and was fixed correctly in the shipped script (verified by reading the `[ -f ... ]` guard now wrapping the `wc -l <` redirection). Diamond-eyes note: the build day's craft is real and the individual mechanisms work as narrowly tested — the failure is specifically in how completion and coverage were characterized in the summary documents, and in what happens at the seams between the three new surfaces, not in whether any single piece runs.

## Authority and dependency map

```
Operator directive
  -> "hephaistos agent" writes scope packet (governance/tasks/weekly-os-health-20260708.md)
       [unverifiable from artifacts: isolated Agent-tool dispatch vs. same-session persona]
  -> "queen-keyport agent" writes clearance + 8 conditions (same note, same file)
       [gate cannot verify this happened before qk_verdict was set]
  -> scripts/governance_gate.py --hard invoked MANUALLY (F1: no automated caller exists)
       [checks 3 YAML strings only (F2) -- does not check condition satisfaction]
  -> "Hermes"/main session executes weekly.sh edit
  -> RELAY-LEDGER entry written (RELAY-20260708-002, before commit -- timing corroborated)
  -> git commit 882b98750 (16:45:38Z, ~5min after the RELAY entry -- consistent ordering)
  -> governance_state stays `routed`, NOT `done` (correct per the task note;
     CONTRADICTED by governance/EMERAULD-OS-BUILD-ORDER.md's CLOSED/DONE labels -- F4)

Separately, with no dependency on the above chain:
  MCP save_note/capture_idea (~/.claude.json, project scope /home/martin)
    -> Inbox/*.md  [F3: raw-lane guard covers 2 of 4 named raw roots]
    -> emerauld-inbox.path (systemd, confirmed enabled + fired twice)
    -> inbox-route.sh --dangerously-skip-permissions --model haiku
       [F6: raw-lane/scope guarantees are prompt-level in THIS script, not code-level]
    -> vault (Areas/*, Resources/*, wiki/*) -- no human confirmation except the
       prompt-level client/financial HOLD instruction
    -> weekly/nightly/morning cron passes (also --dangerously-skip-permissions)
       promote/cross-link whatever landed there into MOCs, trackers, review notes

These two chains never intersect at a shared hard gate (F7). The only thing that
resembles a gate (governance_gate.py) has no automated caller (F1) and validates
frontmatter strings, not process integrity (F2).
```

## Narrative-reality gap matrix

| Claim | Where | Reality | Gap |
|---|---|---|---|
| "gap 3 CLOSED" / "Stage 4 DONE 2026-07-08" | [[governance/EMERAULD-OS-BUILD-ORDER]] lines 51, 67 | task note `governance_state: routed`, pending 2026-07-10 evidence | F4 |
| Guard "refuses the immutable raw lanes" | RELAY-20260708-001 | covers 2 of 4 named raw roots | F3 |
| "all five metric groups degrade to explicit labeled fallbacks... nothing silent reaches the prompt" | execution record, [[governance/tasks/weekly-os-health-20260708]] | 3 of 5 subcases silently degrade to `0` via the `cmd \| wc -l \|\| fallback` pattern | F5 |
| "Execution requires `governance_state: cleared` — checked by `scripts/governance_gate.py`" | [[governance/tasks/README]] rule 1 | no automated caller exists anywhere on the host; it is a manually-run CLI | F1 |
| "no code path that actually routes a task through clearance before execution" | `governance/EMERAULD-OS-SPEC — Governance Wiring.md` (buried in a note-to-future-Claude, not the headline status) | accurate, and directly contradicts the build order's own CLOSED/DONE framing of the same gap | F4, F7 |

## Skill/surface-composition assessment

Not a skill corpus in the SKILL-MAP.md sense, but the same composition-coherence lens applies to the three new standing surfaces built today: MCP server, systemd path unit + router, governed-task pipeline. Each was built and tested against its own narrow exit criterion (and each of those individual tests holds up under independent verification — see L5 note above). None of the three stages' exit criteria tested the seam between surfaces: no test exercised "MCP-created note flows through the router and is later cited by a cron pass as if it were operator-authored," no test exercised a malformed or adversarial Inbox filename/content, and no test exercised what happens if the governed-task gate and the Inbox-router pipeline ever need to agree on whether the same piece of content is "cleared." The three surfaces were engineered independently and composed by proximity, not by a shared control point.

## Provenance note and shared-substrate note (Mercury Protocol)

This audit's raw material — the RELAY-LEDGER entries, the task note, the build order, the three spec docs — was authored by the same class of session (Claude Code, this host, this same day) that this audit scrutinizes. Per Argus's standing rule, every "executed," "verified," "closed" claim in that material was treated as unproven narrative and checked independently: against git commit timestamps and diffs, the systemd journal, live file permissions and directory listings, direct reads of `governance_gate.py` and `vault_ops.py`, and a live re-run of the `.graph_store/summary.json` and register-line-count commands (both matched the claimed figures: 24 orphans, 3265 unresolved links, 100+1501 register lines, 12 open/4 resolved contradiction flags — these specific numeric claims held up). Where a claim could not be independently verified from artifacts alone (whether "hephaistos agent" and "queen-keyport agent" were genuinely isolated Agent-tool dispatches versus one session narrating both), this report says so explicitly rather than resolving the ambiguity in either direction. External verification is recommended: Argus is itself a Claude Code session on the same host and cannot fully escape the provenance risk it is naming in the audited work. A second, differently-provenanced review (a different model, or a human reading the raw git/journal evidence directly) would strengthen confidence in this report's own findings before they are acted on.

## Escalation status and required human actions

**Escalate to Operator directly** (Argus findings are recommendations, not mandates):

1. Decide whether `governance/EMERAULD-OS-BUILD-ORDER.md`'s CLOSED/DONE labels for gap 3 / Stage 4 should be corrected now to match the task note's `routed` state (F4), given this is the document most likely to be read as the system's status-of-record.
2. Decide whether `scripts/governance_gate.py`'s README-stated role ("checked by") should be backed by an actual automated call site, or whether the README language should be softened to describe a manual/advisory tool during the pilot month (F1).
3. Decide whether `OBSIDIAN_PROTECTED_DIRS` should be extended to all four named raw-lane roots, or whether the two currently uncovered roots (`PEER-REVIEW/01_RAW_MATERIALS/`, `wiki/raw-sources/`) are intentionally out of MCP scope for a documented reason (F3).
4. Before trusting the MCP -> Inbox -> router -> vault -> cron chain unattended over an extended period, consider one deliberate adversarial or malformed-input test of the full chain, not just each stage's isolated exit criterion (F7).

No live exploit was executed by this audit; all Critical/High findings are code-level and configuration-level, verified by direct reading within the authorized read-only boundary, not by live-executing a bypass against the production vault.

## Overall deployment-readiness verdict

**CONDITIONAL — not ready for unattended, hardened-governance operation at current state.** The individual components (MCP server, systemd router, governed-task state machine) are real, function as built, and their own narrow exit criteria genuinely passed — this audit independently corroborated that much via git history and the systemd journal, not narrative alone. What is not ready: the "governance" in "governance pipeline" is currently an advisory convention with no automated enforcement point (F1, F2); the "immutable raw lanes" guarantee has a real coverage gap on the newest, always-on write surface (F3); and the system's own status-of-record document overclaims the completion of the very mechanism this audit was commissioned to check (F4). Treat this pipeline as a working prototype whose individual pieces are sound and whose composition and enforcement claims need the corrections above before being relied on as a governance control rather than a governance narrative.

## Related

- [[governance/tasks/README]]
- [[governance/tasks/weekly-os-health-20260708]]
- [[governance/EMERAULD-OS-BUILD-ORDER]]
- [[governance/EMERAULD-OS-SPEC — Governance Wiring]]
- [[governance/EMERAULD-OS-MCP-Surface-Smoke-Test]]
- [[governance/EMERAULD-OS-Stage-3-Exit-Criterion]]
- [[Areas/PHAROS/RELAY-LEDGER — Live Governance Handoff Ledger]]
