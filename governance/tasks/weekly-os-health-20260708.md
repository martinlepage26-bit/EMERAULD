---
type: governed-task
title: Governed Task — Weekly OS-Health Section (2026-07-08)
tags:
- governed-task
- emerauld-os
- stage5
status: active
domain: governance
governance_state: routed
hephaistos_scope: defined
qk_verdict: cleared
relay_id: RELAY-20260708-002
created: '2026-07-08'
updated: '2026-07-08'
vault_area: governance
canonical_path: governance/tasks/weekly-os-health-20260708.md
stamp_status: grandfathered
---

# Governed Task — Weekly OS-Health Section

> For future Claude: first task through the machine-readable governance pipeline (OS Stage 4 exit-criterion run, [[governance/tasks/README|state machine]]). The task itself is the OS build order's Stage 5 deliverable.

## Intake (Operator, 2026-07-08)

Add an OS-health section to the weekly review automation (`scripts/scheduled/weekly.sh`) per [[governance/EMERAULD-OS-BUILD-ORDER|build order]] Stage 5: the weekly review note gains a section reporting FAILURES.md entry count, orphan count, unresolved-link delta, register line counts, and contradiction flags open/closed — so the OS reports on itself and Argus audits the reports.

## Scope packet (HEPHAISTOS)

### Artifact

`scripts/scheduled/weekly.sh` gains a sixth prompt-generated section, `## OS health`, in
the note it already writes at `wiki/Weekly Review — ${TODAY}.md`. No new script file,
no new cron entry, no schema change. The artifact is a bash edit to one existing file:
a pre-computation block inserted before the existing `claude -p "..."` heredoc, and one
new bullet in the prompt's numbered synthesis list plus one new `##` section in the
output spec.

### The five metric groups, and how each is computed

1. **FAILURES.md entry count** — `wc -l < "$LOGDIR/FAILURES.md" 2>/dev/null || echo 0`.
   `Logs/scheduled/FAILURES.md` does not exist yet on this host (verified: no failures
   logged since cron monitoring closed 2026-07-08) — the count must degrade to `0` on a
   missing file, not error the script. Report as: entries this week (lines added since
   `$WEEK_START`, via `grep -c "^- $WEEK_START\|^- ${TODAY}"`-style date-prefix match
   against the FAILURES.md line format `- YYYY-MM-DD HH:MM ... FAILED ...`) alongside the
   all-time total.

2. **Orphan + unresolved counts from `.graph_store/summary.json`** — two distinct fields,
   verified present in the current file (built 2026-07-08T06:13:11Z): `zero_backlink`
   (currently 24) is the orphan count; `unresolved_links` (currently 3265) is the
   unresolved-link count. Extract with
   `python3 -c "import json;d=json.load(open('.graph_store/summary.json'));print(d['zero_backlink'],d['unresolved_links'])"`.
   Do not conflate these two fields under one label — build order Stage 5 text names
   them as separate metrics ("orphan count, unresolved-link delta").

3. **Register line counts** — `wc -l session-state.md memory/agents/*.md`, reported
   individually per file plus a combined total (verified current total: session-state.md
   100 lines + 9 files under memory/agents/ = 1,501 lines, 1,601 combined).

4. **Contradiction callouts open vs resolved** — vault-wide grep counts:
   `grep -rl '> \[!warning\] Contradiction detected' --include=*.md . | wc -l` (open,
   currently 12 files) vs
   `grep -rl '> \[!success\] Contradiction resolved' --include=*.md . | wc -l` (resolved,
   currently 4 files). Count files carrying the callout, not raw grep matches, since a
   note can carry one callout of each kind during a still-open resolution.

5. **Unresolved-link delta** — the build order specifies a *delta*, not a raw count.
   No prior-week baseline exists (only one prior weekly review note exists,
   `wiki/Weekly Review — 2026-06-26.md`, predating this section). Scope decision: on the
   first run, report the raw `unresolved_links` count and label it
   `(baseline — no prior week to diff against)`. From the second run onward, the prompt
   reads the previous dated weekly review note's `## OS health` section, extracts its
   `unresolved_links` figure, and reports `current − previous` as the delta. This needs
   no new storage: the review notes already persist weekly in `wiki/`.

### Boundary: deterministic pre-computation, not a prompt-block instruction

Two approaches were available: (a) add a prompt-block telling the headless `claude -p`
pass to compute these five metrics itself via its own tool calls, or (b) compute them
deterministically in bash before the `claude -p` invocation and interpolate the values
as literal numbers into the prompt string, the same way `$TODAY` and `$WEEK_START` are
already handled in the current script.

**Choosing (b): deterministic pre-computed values passed into the prompt.** Rationale:

- The existing script already establishes this pattern — `TODAY` and `WEEK_START` are
  computed in bash and interpolated, not left for the LLM pass to derive from context.
  Extending that pattern is lower-drift than introducing a second computation style in
  the same script.
- Line counts, grep counts, and JSON field reads are exact, mechanical operations with
  one correct answer. Delegating them to the LLM pass risks miscount or a hallucinated
  number reported with the same confidence as a correct one — unacceptable for a
  self-measurement artifact that Argus will audit against ground truth.
- It keeps the headless pass's own tool-call budget for the qualitative synthesis work
  (summary, decisions, learnings) it already does, rather than spending calls on
  arithmetic it would do less reliably than `wc -l`/`grep -c`/`python3 -c`.
- It makes the five numbers independently verifiable outside the LLM pass: any human or
  Argus audit can rerun the same four shell one-liners and get the same figures the note
  reports, without needing to trust the model's internal reasoning.

The one exception folded into the deterministic block: the second-run delta computation
(item 5) requires reading and parsing the *previous* dated weekly review note, which is
itself a markdown file with a semi-structured section — this parse still happens in bash
(grep for the `unresolved_links` line under the prior note's `## OS health` heading), not
handed to the LLM pass, to preserve the same verifiability guarantee.

### Out of scope

- No new script file. A tiny inline bash block inside `weekly.sh` is in scope; a separate
  `os-health.sh` or `.py` helper is not, unless Queen Keyport's review surfaces a
  correctness or security reason bash inlining can't satisfy (e.g., JSON parsing fragility
  — the `python3 -c` one-liner above is the acceptable minimum, not a new script).
- No changes to `scripts/scheduled/morning.sh`, `nightly.sh`, or `health-check.sh`, even
  though they touch adjacent data (contradiction flags, FAILURES.md). This task edits
  `weekly.sh` only.
- No schema changes — no new frontmatter keys, no new note type, no change to the
  13-key vault-wide frontmatter schema. The `## OS health` section is prose + numbers
  inside the existing `wiki` type review note.
- No change to the review note's existing six sections (Summary, Decisions, Projects,
  Learnings, Carry Forward, Related) beyond appending the new section after them.
- No retroactive backfill of an `## OS health` section into the one prior weekly review
  note (`2026-06-26`). The delta baseline starts at this run.

### Acceptance criteria

The next Friday 6:00 PM weekly cron run produces a review note at
`wiki/Weekly Review — <that-Friday's-date>.md` whose `## OS health` section contains, with
real numbers (not placeholders, not "N/A" unless a source file is genuinely absent and
degrades to 0 per the FAILURES.md rule above):

1. FAILURES.md entries this week and all-time total (or explicit 0 + "no failures logged"
   if the file is still absent).
2. Orphan count (`zero_backlink`) and unresolved-link count (`unresolved_links`) from
   `.graph_store/summary.json`, labeled separately.
3. Register line counts for `session-state.md` and each file under `memory/agents/*.md`,
   plus a combined total.
4. Contradiction callouts open vs resolved, as file counts (not raw grep-line counts).
5. Unresolved-link delta versus the prior week's `## OS health` section, or the explicit
   baseline label if no prior section exists yet.

Secondary acceptance check: the script still exits 0 on a normal run and still appends to
`FAILURES.md` on a non-zero `claude` exit, unchanged from current behavior — the new
pre-computation block must not introduce a new failure mode into the existing
success/failure branch at the bottom of `weekly.sh`.

## Clearance (Queen Keyport)

**Verdict: cleared (approve-with-constraints).**

Scope reviewed against the vault's binding constraints (raw-lane preserve-only, add/update-only
cron passes, `updated:`-preservation, no deletion) and the two risks HEPHAISTOS flagged.
Consequence domain: internal tooling / self-measurement, not externally exposed, not
regulated, not safety-relevant — delta-first review applies; full escalation lanes not
triggered. Diamond-Eyes: the artifact closes a genuine legibility gap (OS reporting on
itself for Argus) with no equity, oppression, or client-facing exposure — wise and caring,
not merely defensible.

Verified directly rather than taken on faith: `.graph_store/summary.json` (`zero_backlink:
24`, `unresolved_links: 3265`), the vault-wide contradiction-callout grep (12 open files, 4
resolved files, none inside any raw-lane path), `Logs/scheduled/FAILURES.md` genuinely absent,
`memory/agents/*.md` + `session-state.md` combined line count (1,601), and `weekly.sh` has no
`set -e`. I also ran the two candidate bash idioms for the FAILURES.md degrade-to-zero case
in an isolated shell to check the actual failure behavior, since "does it degrade cleanly" is
an empirical question, not a documentation question.

### CONDITIONS (binding, executor must satisfy before this task moves to `done`)

1. **Fix the missing-file stderr leak in the FAILURES.md all-time-total count.** The scope
   packet's literal idiom, `wc -l < "$LOGDIR/FAILURES.md" 2>/dev/null || echo 0`, does not
   actually suppress the "No such file or directory" message on a missing file — verified
   empirically: bash reports a failed `<` input redirection to the shell's own stderr *before*
   the trailing `2>/dev/null` is applied (redirections are set up left-to-right), so the
   message leaks to the script's unredirected stderr on every run until FAILURES.md exists.
   Fix by passing the file as a normal argument instead of via input redirection, e.g.
   `wc -l "$LOGDIR/FAILURES.md" 2>/dev/null | awk '{print $1}'` (confirmed this form suppresses
   correctly), or equivalently gate on `[ -f "$LOGDIR/FAILURES.md" ]` first. The "entries this
   week" `grep -c ...` variant in the same item is not affected (grep takes the file as an
   argument already) — audit the final script to confirm no other metric reintroduces the same
   `<`-redirection pattern.

2. **Extend explicit degrade-on-failure from item 1 to all five metric groups, not just
   FAILURES.md.** The scope packet only specifies degrade-to-zero behavior for the FAILURES.md
   count. Items 2–5 (the `.graph_store/summary.json` python3 read, the two `wc -l` register
   counts, the two contradiction-callout greps, and the prior-week-note delta parse) have no
   stated failure mode. `weekly.sh` has no `set -e`, so one failing command will not abort the
   script, but nothing currently specifies what value gets interpolated into the prompt string
   for a metric that failed to compute — leaving that implicit risks a silent empty/garbled
   number passed to the `claude -p` prompt, which then reports it as if it were real, violating
   the acceptance criterion that numbers be real, "not placeholders... unless a source file is
   genuinely absent." Each of the five metric computations must degrade to an explicit labeled
   placeholder (e.g., `"(unavailable — source missing)"`) on failure, computed in bash, not left
   to the LLM pass to paper over.

3. **Keep the second-run-onward delta computation (item 5) bash-side and deterministic, not
   LLM-parsed prose.** The scope packet's own rationale for choosing deterministic
   pre-computation over an LLM-computed pass (items 1–4) is that arithmetic/extraction done by
   the model risks miscount or confident hallucination on a self-measurement artifact Argus will
   audit against ground truth. That same rationale applies to item 5's second-run delta. This
   week's `## OS health` section must record `unresolved_links` in a fixed, single-line,
   greppable form (e.g. a literal `unresolved_links: 3265` line), not only inside free prose —
   so next week's bash pre-computation block can `grep`/extract it directly. If the extraction
   is instead left to "the prompt reads the previous note and extracts the figure," that
   reintroduces exactly the unreliability the packet rejected for the other four metrics.

4. **Contradiction-callout grep must exclude raw-lane paths, or the executor must document why
   exclusion is unneeded.** Current vault-wide scan (12 open, 4 resolved) does not intersect
   `raw/`, `raw sources/`, `PEER-REVIEW/01_RAW_MATERIALS/`, or `wiki/raw-sources/` today — verified.
   But those lanes are preserve-only and can never receive a `[!success] Contradiction resolved`
   callout by design. Any future raw-lane content that happens to contain the open-callout
   string (e.g. an ingested source quoting the format) would inflate the "open" count with an
   entry that can structurally never resolve, and the metric would misreport health. Add explicit
   path exclusions for the four raw-lane roots to both grep invocations before this ships, unless
   the executor identifies an existing mechanism that already prevents this and names it.

5. **The new pre-computation block must be its own isolated failure domain.** Do not introduce
   `set -e` (none exists today) and do not let a metric-command failure change the script's exit
   code. The exit code branch at the bottom of `weekly.sh` (the one that appends to
   `FAILURES.md`) must continue to reflect only the `claude` invocation's own success/failure,
   unchanged from current behavior — this is the packet's own secondary acceptance check, and
   condition 2 above is what makes it actually satisfiable rather than merely stated.

6. **No `updated:` bleed.** This change touches `scripts/scheduled/weekly.sh` only (a script,
   not vault-frontmatter content); the weekly review note continues to be freshly created each
   run with its own `created`/`updated` stamps. If the executor's diff touches any other vault
   note's frontmatter as a side effect, that is out of scope per HEPHAISTOS's scope packet and
   must be reverted before promotion.

7. **No new script file.** Condition 1's fix is an inline correction, not a correctness/security
   gap serious enough to trigger HEPHAISTOS's stated exception for a separate helper script.
   Inline bash remains cleared as scoped.

8. **Evidence for promotion, not assertion.** Per the Phase and Milestone Promotion Gate's
   bounded-claim standard, the actual populated `## OS health` section from the first live
   Friday cron run must be attached to or linked from the Execution record section below as the
   verification artifact. "It should work" is not sufficient to close this task; the real
   rendered numbers from the first triggered run are.

Risks accepted as residual, not requiring further condition: this is a low-consequence,
internal-only artifact (no client, regulatory, or safety exposure), so full five-lane escalation
review was not run — delta-first review, scoped to the two risks HEPHAISTOS flagged plus what I
found independently, is proportionate here.

## Execution record (Hermes-routed)

**Dispatched 2026-07-08, ledger entry `RELAY-20260708-002` written at true dispatch time (before execution). Hard gate check passed (`scripts/governance_gate.py weekly-os-health --hard` → PASS).**

Executed: `scripts/scheduled/weekly.sh` gained the OS-health pre-computation block + prompt section per the scope packet, with every QK condition addressed:

1. FAILURES.md counts gated on `[ -f ... ]` first — the `<`-redirection idiom QK refuted is not used anywhere in the block; no stderr leak (verified by standalone run).
2. All five metric groups degrade to explicit labeled fallbacks (`0` for absent FAILURES.md per scope; `unavailable` on any command failure) — nothing silent reaches the prompt.
3. Second-run delta parse is bash-side (`grep -oP` on the prior review's OS-health line), never LLM-parsed.
4. Contradiction greps exclude `raw sources/`, `raw/`, `.git`, `.trash`, `node_modules`, and count files (`grep -rl | wc -l`), not raw matches.
5. The block is an isolated failure domain: no `exit`, no `set -e`, every command has a fallback; the script's existing exit-code/FAILURES.md branch is untouched.
6. The block writes nothing — zero `updated:` bleed on any vault note.
7. No helper script created; inline bash + the sanctioned `python3 -c` JSON read only.
8. **Pending (blocks `done`):** first live Friday run (2026-07-10 18:00) must produce the populated `## OS health` section, to be attached below as verification evidence.

Standalone verification of the block (2026-07-08, matches QK's independently verified ground truth exactly): `FAIL_WEEK=0 FAIL_TOTAL=0 | ORPHANS=24 UNRESOLVED=3265 | DELTA=baseline — no prior week to diff against | SS_LINES=100 AGENT_LINES=1501 | FLAGS open=12 resolved=4`.

`governance_state` stays `routed` until condition 8's evidence lands.
