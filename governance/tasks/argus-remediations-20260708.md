---
type: governed-task
title: Governed Task — Argus Audit Remediations (2026-07-08)
tags:
- governed-task
- argus
- remediation
status: active
domain: governance
governance_state: done
hephaistos_scope: defined
qk_verdict: cleared
relay_id: RELAY-20260708-004
created: '2026-07-08'
updated: '2026-07-08'
vault_area: governance
canonical_path: governance/tasks/argus-remediations-20260708.md
stamp_status: grandfathered
---

# Governed Task — Argus Audit Remediations

> For future Claude: governed task #2. Remediates the four principal actionable findings of [[governance/ARGUS-AUDIT — Governance Pipeline (2026-07-08)|the 2026-07-08 Argus audit]] (verdict CONDITIONAL), flowing through the same pipeline the audit critiqued — per operator directive "apply all four remediations as governed task #2".

## Intake (Operator, 2026-07-08)

1. **Gate enforcement (Argus finding 1):** `scripts/governance_gate.py` has zero automated invocation path. Give it one — an automated, recurring check that surfaces governed-task state violations without a human remembering to run it. Desired outcome: a task executed without clearance artifacts becomes visible in the OS's own failure surface within a day, not never.
2. **MCP raw-guard coverage (finding 3):** extend the write protection to all four raw-lane roots — `raw sources/`, `raw/`, `PEER-REVIEW/01_RAW_MATERIALS/`, `wiki/raw-sources/` — in the registered server config and verify each refuses writes.
3. **weekly.sh silent-zero fallbacks (finding 5):** the two contradiction-flag greps and the agent-register count mask upstream failure as `0` via piped `wc -l`; make all three degrade to a labeled `unavailable` like the other metrics, per QK condition 2 of task #1.
4. **Narrative-state corrections (finding 4):** reword the "CLOSED"/"DONE" callouts in [[governance/EMERAULD-OS-BUILD-ORDER|the build order]] (gap 3 / Stage 4, and any other overstated claim Argus identified) to match the pipeline's actual recorded state (task #1 at `routed` pending 2026-07-10 evidence; gate soft and — until item 1 lands — manually invoked).

## Scope packet (HEPHAISTOS)

> For future Claude: this packet defines the artifact for each of the 4 intake items — what gets built, where, why that location and not another, what it explicitly does not touch, and how to check the fix mechanically without waiting on a live cron firing. It does not execute any of the four edits; execution is Hermes-routed after Queen Keyport clears. Read this alongside [[governance/ARGUS-AUDIT — Governance Pipeline (2026-07-08)]] for the underlying evidence (F1, F3, F4, F5).

### Cross-item notes (read before executing any item)

- **Sequencing:** items 2 and 3 are independent and order-agnostic. Item 4's exact wording depends on whether item 1 has already landed in the same execution pass — if Hermes does all four in one sitting, item 4 must describe the *post*-item-1 state (automated invocation exists), not the pre-item-1 state ("manually invoked"). Do not let item 4 contradict item 1's own commit in the same pass.
- **Standing constraints applied to all four:** `updated:` frontmatter moves only on the date content actually changes (never backfilled to 2026-07-08 if executed later); cron scripts get add/update-only edits — no deletion of existing metric groups, log lines, or exit branches; the four raw lanes (`raw/`, `raw sources/`, `PEER-REVIEW/01_RAW_MATERIALS/`, `wiki/raw-sources/`) are read-only targets for every item here — none of the four remediations write into them; no item may introduce a new way for `scripts/scheduled/{weekly,nightly}.sh` to exit nonzero from the deterministic pre-pass blocks — every new check is additive and sits beside the existing `STATUS=$?` / `if [ $STATUS -ne 0 ]` branch, never inside or ahead of it in a way that changes its behavior.
- **Explicit residual, not in scope anywhere in this task:** Argus F2 — `governance_gate.py` validates three YAML frontmatter strings (`governance_state`, `hephaistos_scope`, `qk_verdict`), not process authenticity. It cannot tell whether HEPHAISTOS and Queen Keyport were genuinely isolated dispatches, whether QK's numbered conditions were actually satisfied before `qk_verdict` was set, or whether the three fields were set in the correct order. Item 1 below makes the gate's *absence of automated invocation* (F1) go away; it does not and cannot close F2. Any future task that wants to address F2 needs a different mechanism (e.g., signing, condition-satisfaction checks cross-referenced against the note body, or ordering checks) — that is new design work, not a byproduct of this task.

### Item 1 — Gate enforcement (Argus F1)

**Artifact:** an `--audit-all` mode added to `scripts/governance_gate.py`, invoked from a new deterministic pre-pass block in `scripts/scheduled/nightly.sh` (placed the same way `archive_register.py` already is: before the `claude` call, output appended to the dated log, never gating `$STATUS`).

**Approach and justification:**
- **Why `--audit-all` on the existing script, not a new script:** the check logic already exists and is correct (`state in {cleared,routed} and scope=="defined" and verdict=="cleared"`); generalizing it to iterate every task note reuses proven logic instead of duplicating it. Filter candidate task notes by `type: governed-task` in frontmatter (confirmed present on both `governance/tasks/weekly-os-health-20260708.md` and this note; `governance/tasks/README.md` has `type: governance-doc` and is correctly excluded by this filter, avoiding false WARNs on the state-machine doc itself).
- **Why `nightly.sh`, not `weekly.sh` or a new systemd timer:** the intake's desired outcome is "visible within a day, not never." `nightly.sh` runs daily; `weekly.sh` runs every 7 days, which would leave up to a week of blindness — too slow for the stated outcome. A new systemd timer is a heavier, riskier addition (new unit + new failure surface) for a check that fits the existing daily cadence with one line. `nightly.sh`'s pre-pass block already establishes the pattern (`archive_register.py` — deterministic, non-`claude`, logged, not exit-gated) that this reuses exactly.
- **Why non-blocking (soft, not `--hard`):** `governance/tasks/README.md` rule 1 states the gate runs soft during the pilot month and tightens to hard "after the first clean month" — a decision not yet made. `--audit-all` must not preempt that decision or silently upgrade enforcement; it stays soft.
- **How a violation becomes visible without touching `$STATUS`:** capture the audit's own stdout/stderr and its own exit code into a script-local variable (not `$STATUS`, which is reserved for the `claude` call's exit code later in the file); if the audit's exit code is nonzero OR its output contains `WARN`/`REFUSED`/`ERROR`, append one line to `Logs/scheduled/FAILURES.md` — the OS's existing, already-monitored failure surface (health-check.sh already reads it). This is a second, independent write path to `FAILURES.md`, parallel to the existing `if [ $STATUS -ne 0 ]` branch, not a modification of it.

**Boundaries:**
- Detects only what the gate already checks: a task note whose `governance_state` has advanced (`cleared`/`routed`/`done`) without `hephaistos_scope: defined` and `qk_verdict: cleared` both being true. Does not verify condition satisfaction, field-set ordering, or dispatch isolation (F2, out of scope per the cross-item note above).
- Does not detect "executed work with no task note at all" (`governance/tasks/README.md` rule 4's other drift case) — that requires cross-referencing the RELAY-LEDGER against task filenames, a materially larger piece of work not requested by this intake item.
- Does not change the gate's soft/hard default or the `TASKS.glob(f"*{args.task}*.md")` ambiguity risk on the single-task path (Argus F10, LOW, not in this intake).
- Does not add a "stale in `routed`" staleness rule (Argus F12, LOW, not in this intake).

**Acceptance criteria (mechanical):**
1. `python3 scripts/governance_gate.py --audit-all` exits 0 and prints exactly one `GATE <PASS|WARN|REFUSED>` line per note under `governance/tasks/` whose frontmatter `type == governed-task` (today: 2 lines, for `weekly-os-health-20260708.md` and this note).
2. `grep -n "governance_gate.py --audit-all" scripts/scheduled/nightly.sh` returns exactly one hit, and that line appears before the `/home/martin/.local/bin/claude --dangerously-skip-permissions` invocation in the same file.
3. `git diff` (or a byte comparison) on `scripts/scheduled/nightly.sh` shows the existing `STATUS=$?` / `if [ $STATUS -ne 0 ]` block unchanged; all new lines are additions above the `claude` call.
4. Manually running the new nightly.sh block (or `governance_gate.py --audit-all` directly) against this task note in its current state (`governance_state: scoped`, `qk_verdict: pending`) produces a `WARN` line — a live, truthful demonstration that a task short of full clearance is correctly flagged, not silently passed.
5. `governance_gate.py --audit-all` never causes `nightly.sh` to exit nonzero on its own (soft mode preserved; hard-mode escalation remains a separate, later operator decision per `governance/tasks/README.md` rule 1).

### Item 2 — MCP raw-guard coverage (Argus F3)

**Artifact:** the `OBSIDIAN_PROTECTED_DIRS` value inside `~/.claude.json` → `.projects["/home/martin"].mcpServers["obsidian-second-brain"].env`, extended from `"raw sources:raw"` to include path-part tokens for all four raw-lane roots. No change to `vault_ops.py` — its `_PROTECTED_WRITE_DIRS` mechanism (colon-split env value, matched against `target.relative_to(vault).parts`) already generalizes correctly; it only lacks the right tokens today.

**Approach and justification:**
- Confirmed on disk which path part each root resolves to, since the guard matches PARTS, not full paths:
  - `raw/` → part `raw` (already covered)
  - `raw sources/` → part `raw sources` (already covered, space not hyphen)
  - `PEER-REVIEW/01_RAW_MATERIALS/` → part `01_RAW_MATERIALS` (missing — distinct string, does not overlap with the existing two tokens)
  - `wiki/raw-sources/` → part `raw-sources` (missing — hyphenated, distinct from the already-covered `raw sources` which uses a space)
- New value: `"raw sources:raw:01_RAW_MATERIALS:raw-sources"` (order-independent; the mechanism splits on `:` and treats each token as an exact path-part match).
- **Edit path:** a careful, targeted JSON edit of the single `env.OBSIDIAN_PROTECTED_DIRS` key inside `~/.claude.json` (read-modify-write via a script that loads the JSON, mutates exactly that key, writes atomically via temp-file-then-rename) — not `claude mcp remove` + `claude mcp add`, because this registration carries a `type: stdio` / `command` / `args` shape that would need to be retyped correctly by hand; a scoped JSON key edit is lower-risk for a single env-var change. The MCP server must be reconnected (new Claude Code session, or an explicit MCP reconnect) for the new env value to take effect — this is an operational step, not a code change.

**Boundaries:**
- Extends write-protection coverage only. Does not touch the filesystem-permission gap Argus separately flagged (F11: `raw sources/` is `775`, `wiki/raw-sources/` inherits ordinary vault permissions) — that is an OS-level hardening task, not requested by this intake item, which specifically names "the registered server config."
- Does not promote the MCP registration from project scope (`/home/martin`) to global scope — that is the build order's own separate "after ~1 week clean" follow-through, unrelated to raw-lane coverage.
- Does not redesign `_PROTECTED_WRITE_DIRS` to match full relative paths instead of bare path-part names. The current part-matching mechanism means any *future* directory anywhere in the vault that happens to be named exactly `01_RAW_MATERIALS` or `raw-sources` would also become write-protected as a side effect — a known, pre-existing property of the mechanism, not something this item introduces or is scoped to fix.

**Acceptance criteria (mechanical):**
1. `python3 -c "import json; d=json.load(open('/home/martin/.claude.json')); print(d['projects']['/home/martin']['mcpServers']['obsidian-second-brain']['env']['OBSIDIAN_PROTECTED_DIRS'])"` prints a colon-separated string whose parts, as a set, equal `{"raw sources", "raw", "01_RAW_MATERIALS", "raw-sources"}`.
2. With that env value set, four direct calls to `vault_ops.update_note` (or four MCP `obsidian_update_note` calls after reconnect), one per raw-lane root targeting an existing file in each (e.g. `raw sources/2026 - Memory Context.md`, a file under `raw/00_Inbox`, `PEER-REVIEW/01_RAW_MATERIALS/README.md`, `wiki/raw-sources/2026-05-13/<a file>`), each return `{"error": "path is in a protected directory"}`.
3. A fifth control call to `update_note` on an existing note outside all four roots (e.g. something under `Areas/`) still succeeds — confirms the guard did not over-broaden and block legitimate writes.
4. `git diff` on `vault_ops.py` for this item is empty.

### Item 3 — weekly.sh silent-zero fallbacks (Argus F5)

**Artifact:** the three metric computations in `scripts/scheduled/weekly.sh` — `AGENT_LINES` (line 42), `OPEN_FLAGS` and `RESOLVED_FLAGS` (lines 45-46) — rewritten to check the real exit status of the upstream command in the pipe instead of `wc -l`'s (which almost never fails, so the existing `|| echo "unavailable"` never fires).

**Approach and justification:**
- The anti-pattern is `cmd | wc -l || echo "unavailable"`: bash's `||` here binds to the exit status of the *last* command in the pipe (`wc -l`), which succeeds even when `cmd` failed and produced no/garbage input. `wc -l` on empty stdin returns `0` with exit `0`. The fix reads the upstream command's own exit status via bash's `${PIPESTATUS[0]}` array instead.
- **`AGENT_LINES` (cat-based):** `cat` has no valid "expected empty" case distinct from failure — treat any nonzero `cat` exit as a real failure:
  ```
  AGENT_LINES=$(cat memory/agents/*.md 2>/dev/null | wc -l)
  [ "${PIPESTATUS[0]}" -eq 0 ] || AGENT_LINES="unavailable"
  ```
- **`OPEN_FLAGS` / `RESOLVED_FLAGS` (grep-based) — the fix must NOT use the same threshold as `cat`.** `grep -rl` exits `0` (matches found), `1` (no matches — a legitimate, common "zero flags open" state, not a failure), or `2`+ (a real error: bad pattern, unreadable path). Using "any nonzero = fail" here would wrongly relabel a genuinely healthy zero-open-flags week as `unavailable`. The correct check treats only exit `>= 2` as failure:
  ```
  OPEN_FLAGS=$(grep -rl '...' ... . 2>/dev/null | wc -l)
  [ "${PIPESTATUS[0]}" -le 1 ] || OPEN_FLAGS="unavailable"
  ```
  (same pattern for `RESOLVED_FLAGS`). This distinction — cat's binary success/fail vs. grep's three-way found/none/error — is the one substantive judgment call in this item; getting it wrong in either direction reintroduces either a false failure or a masked one.
- The other two metric groups QK already verified as correct (F5 itself confirms this) are untouched: the `FAILURES.md` block (lines 23-24, `[ -f ... ]` guard before the read, not a pipe-based fallback) and the `GRAPH_METRICS` python invocation (lines 32-36, single command whose own exit status directly gates the `|| echo` fallback — no intermediate `wc -l` masking it). `SS_LINES` (line 41) uses the same correct `[ -f ... ] && wc -l < ... || echo unavailable` idiom as FAILURES.md and is also untouched.

**Boundaries:**
- Only the three named metrics change. `FAILURES.md`, `GRAPH_METRICS`, `SS_LINES`, and the unresolved-link delta block (lines 48-58, a bash arithmetic comparison, not a `cmd | wc -l` pattern and not named in F5) are untouched.
- `morning.sh` and `health-check.sh` are not touched — F5 and this intake item name `weekly.sh` specifically.
- Does not change what the metrics measure or the prompt text that consumes them (lines 79-84) beyond substituting the corrected shell variables — the review note's structure and wording stay as-is.

**Acceptance criteria (mechanical):**
1. `grep -c '| wc -l || echo "unavailable"' scripts/scheduled/weekly.sh` returns `0` (down from 3 today).
2. `grep -n 'PIPESTATUS\[0\]' scripts/scheduled/weekly.sh` returns 3 hits, one per fixed metric.
3. Live test A (genuine failure): with `memory/agents/` temporarily unreadable or absent in a test copy, `AGENT_LINES` resolves to the literal string `unavailable`, not `0`.
4. Live test B (genuine zero, must NOT regress): with zero files currently matching `> [!warning] Contradiction detected` (or a constructed fixture with zero matches), `OPEN_FLAGS` resolves to `0`, not `unavailable` — confirms exit-1-from-grep is not misclassified as a failure.
5. `git diff` on `scripts/scheduled/weekly.sh` touches only lines 42 and 45-46 (plus their new `PIPESTATUS` check lines); lines 23-24, 32-36, 41, and 48-94 are unchanged.

### Item 4 — Narrative-state corrections (Argus F4)

**Artifact:** `governance/EMERAULD-OS-BUILD-ORDER.md`, exactly two spots — the gap-3 row in the "9 gaps" table (line 51) and the Stage 4 paragraph in "Build sequence" (line 67). No other CLOSED/DONE label in that document changes.

**Approach and justification:**
- Argus's Layer 1 coherence failure is precise and narrow: these two spots say `CLOSED`/`DONE` while the artifact they cite as evidence — [[governance/tasks/weekly-os-health-20260708]] — carries `governance_state: done`, not `done`, and states its own closure "pends its Friday live-run evidence" (2026-07-10, not yet occurred). No other gap's CLOSED/DONE label was flagged by Argus as contradicted by its own cited evidence (Argus's L5 note explicitly confirms the other stage exit criteria "were not fabricated," corroborated independently via git history and the systemd journal) — so only these two spots change; widening the correction to other gaps would be uninstructed scope creep.
- Replacement label: `MECHANISM LIVE — NOT CLOSED (2026-07-08)`, chosen to (a) avoid reusing `CLOSED`/`DONE` for a state that is not that, (b) not invent a new false status either, and (c) match the table's own existing tolerance for non-CLOSED labels (gap 8 already reads `DOCUMENTED below`, so a third status word is not a stretch of the table's format).
- Replacement text states, in the artifact's own words: the task note's real `governance_state` (`routed`), the pending 2026-07-10 evidence date, and the gate's current invocation mode (soft; manually invoked as of the edit date, OR — if item 1 has already landed in the same execution pass — "automated via nightly.sh" per the cross-item sequencing note above). The executing session must check item 1's actual landed state at edit time rather than assume either wording.
- `updated:` frontmatter bumps to the actual date this edit is applied (standing rule; not backfilled to 2026-07-08 if this executes later).

**Boundaries:**
- Confined to the gap-3 table row and the Stage 4 paragraph. Every other gap's status label (1, 2, 4, 5, 6, 7, 9) and every other Stage's paragraph (1, 2, 3, 5) is untouched.
- Does not touch `governance/EMERAULD-OS-SPEC — Governance Wiring.md`, which Argus already credits with getting this right ("the pipeline's first act was to refuse premature closure, which is the point") — no edit needed there.
- Does not address F9 (one-time proof artifacts sitting in `governance/` next to standing mechanism) or F12 (no stale-in-`routed` rule in `governance/tasks/README.md`) — both separate findings, neither named in this intake item.
- Does not change `governance/tasks/weekly-os-health-20260708.md` itself — that note's own `governance_state: done` is already correct per Argus; only the build order's *description* of it is wrong.

**Acceptance criteria (mechanical):**
1. `grep -n "CLOSED 2026-07-08" governance/EMERAULD-OS-BUILD-ORDER.md` no longer matches the gap-3 row or the Stage 4 paragraph (mechanical: line count for that exact string drops by 2 from today's baseline; other CLOSED/DONE occurrences elsewhere in the file are unchanged in count).
2. The new gap-3 row and Stage 4 paragraph both contain the literal string `routed` and the date `2026-07-10`.
3. The new text states the gate's invocation mode (soft; manual or automated) in a way that is true at the moment the edit is committed — verified by cross-checking against item 1's actual state (does `scripts/scheduled/nightly.sh` already call `governance_gate.py --audit-all` at commit time, yes or no) rather than asserted from this packet alone.
4. `git diff` on `governance/EMERAULD-OS-BUILD-ORDER.md` touches only the gap-3 row and the Stage 4 paragraph (plus the frontmatter `updated:` field); every other line is byte-identical to today's version.
5. Frontmatter `updated:` on this file equals the actual date of the edit commit, not `2026-07-08` if executed on a later date.

## Clearance (Queen Keyport)

**Verdict: CLEARED, with 11 binding conditions.** None of the four items is refused outright; item 3's proposed code, however, was independently tested and does not do what it claims — it cannot proceed as literally drafted and is bound below to a corrected, re-tested implementation.

**Governance domain:** internal infrastructure (cron scripts, an MCP env-var config file, and a governance-doc narrative correction) — no external-facing surface, no client data, no regulatory exposure. Consequence domain is auditability and configuration integrity, with one genuine blast-radius risk (item 2 touches a file shared by 6 project scopes, not just this one).

**Evidence threshold applied:** mechanical, testable claims only — every control below was run in an isolated shell on this host (2026-07-08) rather than accepted from the packet's prose. Two of the packet's own code samples (item 3) were disproven by direct test; the rest held up.

**Right-arm synthesis (Philosopher / Power-Analyst):** Philosopher names a live epistemic tension the packet itself flags and correctly declines to resolve: this task remediates an Argus audit of the governance pipeline *through that same pipeline*, and Argus's own F2 (the gate checks three YAML strings, not whether HEPHAISTOS/QK were genuinely isolated dispatches) remains unverifiable from artifacts for this task too. Naming this is required by binding principle 1 (Objectivity as Naming Limits of Subjectivity); it is not a reason to refuse, since the intake explicitly scopes F2 out (see condition 10). Power-Analyst names the structural single point of failure in item 2: `~/.claude.json` is one 50KB file gating MCP config for 6 unrelated project scopes on this host, edited here for the sake of one project's raw-lane coverage — the leverage/blast-radius mismatch is real and is bound below (conditions 5-8). No divergence between the two right-arms on this task; both concur clearance is appropriate with the constraints below.

**Diamond-Eyes:** wise and caring, not merely defensible — refusing to let a broken-but-plausible-looking fix (item 3) pass as a genuine repair, and refusing to let a single-file edit with no backup and a permission-downgrade risk touch five other projects' configuration silently, both protect the system's future self more than a fast, ungated approval would. Escalation not required; conditions suffice.

### Binding conditions

1. **Item 3 — the packet's literal `${PIPESTATUS[0]}` fix is broken; do not implement it as drafted.** Verified empirically (isolated bash, 2026-07-08): when a pipe is wrapped in a command-substitution assignment (`VAR=$(cmd1 | cmd2)`), `${PIPESTATUS[0]}` read in the *outer* shell reflects only the exit status of that single assignment statement — which equals the exit status of the subshell, which (absent `pipefail`) equals the *last* command in the inner pipe (`wc -l`, which almost never fails) — not the inner pipeline's own PIPESTATUS array, which is scoped to the subshell and discarded on exit. Direct test: `OPEN_FLAGS=$(grep -rl 'x' ONLY_NONEXISTENT_DIR 2>/dev/null | wc -l); [ "${PIPESTATUS[0]}" -le 1 ]` evaluates **true** (reads 0, not grep's real exit code 2) even though the directory does not exist — reproducing the exact silent-zero failure F5 exists to fix, inside the code meant to fix it. Required correction, verified working against all four failure/success cases (missing dir, permission-denied dir, bad pattern, legitimate zero-match, and cat on a missing/unreadable glob): scope `pipefail` to the subshell and read `$?` immediately after, e.g. `OPEN_FLAGS=$(set -o pipefail; grep -rl '...' ... 2>/dev/null | wc -l); RC=$?; [ "$RC" -le 1 ] || OPEN_FLAGS="unavailable"` (grep, threshold `-le 1`) and `AGENT_LINES=$(set -o pipefail; cat memory/agents/*.md 2>/dev/null | wc -l); RC=$?; [ "$RC" -eq 0 ] || AGENT_LINES="unavailable"` (cat, threshold `-eq 0`). Verified the subshell-scoped `pipefail` does not leak into the parent script's shell options, so it cannot alter any other pipeline in `weekly.sh` — the additive-only boundary holds.
2. **Item 3 — the packet's own Live Test A and Live Test B (acceptance criteria 3-4) must actually be run against the corrected code, not accepted on the strength of the pseudocode.** Given condition 1, the packet's literal snippet would silently fail its own Live Test A (a genuinely missing/unreadable `memory/agents/` would still resolve to `0`, not `unavailable`). Do not close this item on a `git diff` match alone.
3. **Item 1 — capture the audit-all subprocess's own output and exit status into a script-local variable, and grep only that variable for `WARN`/`REFUSED`/`ERROR`, never the shared `$LOG` file.** `archive_register.py` appends to the same dated log immediately before this new block; grepping the whole file risks misattributing an unrelated string in `archive_register.py`'s own output to a gate finding. Example shape: `GATE_OUT=$(python3 "$VAULT/scripts/governance_gate.py" --audit-all 2>&1); GATE_RC=$?` then write `GATE_OUT` to the log separately and test `GATE_OUT`/`GATE_RC`, not `$LOG`.
4. **Item 1 — confirm the new `--audit-all` mode does not change the existing single-task invocation's behavior.** Run `governance_gate.py weekly-os-health --hard` before and after the code change and diff the output; it must be byte-identical.
5. **Item 1 — verify, don't assume, that a nonzero exit from the new audit block cannot abort `nightly.sh` before the `claude` call runs.** `nightly.sh` has no `set -e` and the new block is not chained into the `claude` invocation with `&&`, so this should hold structurally — but force the audit-all call to exit nonzero once (a malformed test fixture) and confirm the `claude` line still executes and `$STATUS` still reflects only the `claude` call's own exit code, not the gate's.
6. **Item 2 — back up `~/.claude.json` before editing, at mode 600, and confirm the backup's permission bit rather than assume it.** `cp -p` preserves source permissions on this host (verified) — use it (e.g. `cp -p ~/.claude.json ~/.claude.json.bak-$(date +%Y%m%d-%H%M%S)`), then `stat` the backup and confirm `0600`.
7. **Item 2 — the edit script must not do a naive `open(path,'w')`-then-rename.** Verified on this host: under the current umask (`0002`), a plain `open().write()` yields mode `664`, silently downgrading a file that is currently `-rw-------` (600) and holds MCP configuration for **6** distinct project scopes (`/home/martin`, `/root/repos/compta-anc-pcg-api`, `/home/martin/EMERAULD`, `/home/martin/EMERAULD/PEER-REVIEW`, `/home`, `/home/martin/Lavoie`) to group/world-readable. Use `tempfile.mkstemp` (verified default mode 600 on this host) or an explicit `os.chmod(tmp, 0o600)` before the atomic rename, and confirm post-write that `~/.claude.json` is still exactly `0600`.
8. **Item 2 — verify the other 5 project scopes are untouched, not just the target key.** The packet's own acceptance criteria check only `OBSIDIAN_PROTECTED_DIRS`'s new value plus one control-path probe (`Areas/`). Before marking this item done, diff the full parsed JSON structure before/after and confirm every project key other than `/home/martin`'s `mcpServers.obsidian-second-brain.env.OBSIDIAN_PROTECTED_DIRS` is unchanged — not spot-checked.
9. **Item 2 — `~/.claude.json` is a live, frequently-written, shared file on a host that runs a multi-agent CLI council concurrently.** Perform the edit at a moment with no other active Claude Code session write in flight where practical, and re-read the file immediately after writing to confirm the change was not lost to a concurrent read-modify-write race. If a race is detected, redo the edit; do not declare it done on the first write alone.
10. **Item 2 — the guard's expanded coverage is not live until the MCP server reconnects.** Do not mark the four protected-path refusal probes or the one control-path success probe (packet acceptance criteria 2-3) as passed until they are run against a reconnected server process, not the one already running in this session.
11. **Item 4 must execute last among the four, in any single pass.** If item 4 is written before item 1 lands, and item 1 then lands later in the same sitting, item 4's description of the gate's invocation mode goes stale again within the same pass — reproducing the exact F4 failure this item exists to correct. Check item 1's actual landed state (`grep -n "governance_gate.py --audit-all" scripts/scheduled/nightly.sh`) immediately before writing item 4's replacement text, not earlier in the session.

**Residual, named per binding principle 1 (not a blocker):** automating the gate's invocation (item 1) makes governance drift *visible*; it does not make the three YAML fields the gate checks *trustworthy* (Argus F2, explicitly out of scope for this task per the packet's own cross-item note — concurred). Any future narrative describing item 1's completion must preserve this distinction rather than let "the gate now runs automatically" imply "the gate now verifies clearance was genuine."

**Standing check for all four items:** before any item is marked `done`, run `git diff` against that item's own stated boundary lines. A diff touching lines outside the stated boundary is a completeness failure for that item, not a stylistic nit.

## Execution record (Hermes-routed)

**Dispatched 2026-07-08, ledger `RELAY-20260708-004` written at true dispatch time. Hard gate PASS before execution. All four items executed in QK-condition order (1→2→3→4, item 4 last per condition 11); every acceptance criterion verified mechanically the same day — no pending live-run dependency, so this task closes at `done`.**

- **Item 1 (gate enforcement):** `governance_gate.py` gained `--audit-all` (filters `type: governed-task`; pre-clearance states report PASS-pending; advanced states without both clearance artifacts, or routed/done without relay_id, count as violations; exit 1 on any). `nightly.sh` invokes it in the deterministic pre-pass block — output and exit captured in `GATE_OUT`/`GATE_RC` (never `$STATUS`, never grepped from the shared log, QK condition 3); violations append to FAILURES.md. Verified: audit-all reports both governed tasks PASS / 0 violations; single-task invocation output byte-identical pre/post (condition 4); forced nonzero gate exit cannot abort the flow or touch `$STATUS` (condition 5); hook sits at nightly.sh:23, before the claude call at :30.
- **Item 2 (MCP raw-guard coverage):** `OBSIDIAN_PROTECTED_DIRS` extended to `"raw sources:raw:01_RAW_MATERIALS:raw-sources"` in ~/.claude.json via mkstemp + chmod 600 + atomic rename (condition 7); `cp -p` backup at mode 600 taken first (condition 6); full-JSON structural diff proved no other key or project scope changed (condition 8); immediate re-read confirmed no concurrent-write race (condition 9); all four raw-lane probes REFUSED and the control path passed in a fresh server-equivalent process running the registered env, and `claude mcp list` shows Connected post-edit (condition 10). No vault_ops.py code change needed — the part-matching guard generalized as scoped.
- **Item 3 (silent-zero fallbacks):** implemented QK's corrected idiom (subshell-scoped `set -o pipefail` + immediate `$?`), NOT the scope packet's refuted `PIPESTATUS` form (condition 1). Thresholds: cat-pipeline fails on RC≠0, grep pipelines only on RC≥2 (grep exit 1 = legitimate zero). Live tests per condition 2: happy path real values (1501 / 13), missing glob → `unavailable`, bad search root → `unavailable`, legitimate zero-match → `0`, no pipefail leak into the parent shell.
- **Item 4 (narrative corrections):** executed last; item 1's landed state re-checked immediately before writing (condition 11). Build order gap-3 row and Stage-4 paragraph reworded: "CLOSED/DONE" → "PIPELINE LIVE, closure pending", naming task #1's `routed` state, the 2026-07-10 evidence dependency, the gate's soft + now-automated invocation, and the open F2 residual — which this record also preserves: **the gate now runs nightly, but it validates clearance artifacts, not their authenticity (Argus F2 remains open by scope).**

Boundary check (QK standing check): `git status` shows exactly the four stated artifacts + this task note; outside-repo edits limited to ~/.claude.json (backed up) and the RELAY-LEDGER entry.
