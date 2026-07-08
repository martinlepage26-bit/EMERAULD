---
type: governance-doc
title: Argus Audit — Remediation Verification (2026-07-08)
aliases:
- Argus Remediation Verification — F1-F5
tags:
- governance-doc
- argus
- audit
- emerauld-os
- governance-pipeline
- remediation-verification
status: active
domain: governance
created: '2026-07-08'
updated: '2026-07-08'
vault_area: governance
canonical_path: governance/ARGUS-AUDIT — Remediation Verification (2026-07-08).md
---

# Argus Audit — Remediation Verification (2026-07-08)

> For future Claude: this is a follow-up Argus audit re-verifying the five findings (F1-F5) of [[governance/ARGUS-AUDIT — Governance Pipeline (2026-07-08)|the 2026-07-08 baseline Argus audit]] (verdict CONDITIONAL) against the two governed tasks that claim to have remediated them: [[governance/tasks/argus-remediations-20260708|governed task #2 (F1/F3/F4/F5)]] and [[governance/tasks/gate-authenticity-20260708|governed task #3 (F2)]]. Every "done," "verified," "closed," and "all N acceptance criteria pass" claim in those two notes was treated as unproven narrative and reproduced independently — direct code reads, a live re-run of `governance_gate.py --audit-all`, a scratch-copy adversarial attack suite against `gate_stamp.py` (never touching the real key, the real task notes, or the real ledger), a fresh-process test of the MCP raw-guard against all four named lanes plus a control path, and an isolated reproduction of every `weekly.sh` failure/success case named in the operator's brief. Argus flags; Argus does not fix.

## Scope and mode

- **Audit mode:** standard, adversarial (Layer 4 pressure applied on scratch copies only; no live exploit against production files).
- **Target system:** the two remediation task notes and the artifacts they touched — `scripts/scheduled/nightly.sh`, `scripts/governance_gate.py`, `scripts/gate_stamp.py`, `~/.agents/hephaistos/keys/gate-hmac.key`, `~/.claude.json` (`OBSIDIAN_PROTECTED_DIRS`), `vault_ops.py`, `scripts/scheduled/weekly.sh`, `governance/EMERAULD-OS-BUILD-ORDER.md`, `governance/tasks/README.md`.
- **Operator authorization boundary:** read/trace/test within `/home/martin/EMERAULD`, `/home/martin/.agents/hephaistos` (read-only on the real key; all attacks run against a scratch key at `/tmp/.../f2-attack/scratch.key`), `~/.claude.json` (read env only, no writes), scratch fixtures under `/tmp/claude-1001/.../scratchpad/`. No mutation of `governance/tasks/`, the real HMAC key, or `~/.agents/hephaistos/ledgers/RELAY-LEDGER.md` was performed.
- **Shared-substrate:** yes. Mercury Protocol applies. Both remediation task notes were authored by the same class of session (Claude Code, this host, same day) that this audit scrutinizes, and both are unusually elaborate, self-aware, and well-documented — eleven and nine binding QK conditions respectively, an explicit "honesty boundary" section, empirically-caught bugs in their own drafts. Per Argus's standing rule, elegance and self-awareness are treated as a capture signal, not a reason to relax scrutiny: the more polished the artifact, the harder this audit pushed on it, and the critical finding below (NEW-F2a/b) was found precisely underneath that polish.

## Per-finding verdicts

### F1 (gate never invoked) — **REMEDIATED**

Direct evidence: `scripts/scheduled/nightly.sh:23-28` calls `governance_gate.py --audit-all`, captures `GATE_OUT`/`GATE_RC` into script-local variables (never `$STATUS`, never grepped from the shared `$LOG` — QK condition 3 held), and appends to `Logs/scheduled/FAILURES.md` on nonzero exit or a `WARN|REFUSED|ERROR` match, before the `claude` call at line 30. `crontab -l` confirms `nightly.sh` fires daily at 22:00. A live run of `python3 scripts/governance_gate.py --audit-all` today returns `0 violation(s)` (all three governed-task notes PASS). A synthetic-WARN reproduction of the exact capture/grep logic in `/tmp/.../f1-synth/` confirmed a WARN-producing gate output correctly reaches a `FAILURES.md`-shaped file with the same conditional (`[ $GATE_RC -ne 0 ] || grep -qE 'WARN|REFUSED|ERROR'`). The core F1 ask — an automated, non-blocking invocation path that surfaces violations without a human remembering to run the gate — is real and functionally correct.

Caveats (do not change the verdict, but qualify "verified"):
- `nightly.sh` was last modified 2026-07-08 17:27 UTC; the audit was run at 19:12 UTC, before the 22:00 cron fire. No `Logs/scheduled/nightly-*.log` exists yet. **Every "verified" claim in task #2's execution record is a manual invocation, not an observed live-cron firing** — that is consistent with the task's own acceptance criteria (which do not require waiting on a cron cycle) but should not be read as "operationally proven," only "code-proven."
- Task #2's own justification for choosing `nightly.sh` over `weekly.sh` cadence states the failure surface is "already-monitored (`health-check.sh` already reads it)." This is false: `health-check.sh` contains zero references to reading `FAILURES.md` anywhere in its ~55 lines, and its own write branch (`echo ... >> "$LOGDIR/FAILURES.md"`) is itself broken — `LOGDIR` is never defined in `health-check.sh` (confirmed by `grep -n "LOGDIR=" scripts/scheduled/health-check.sh` returning zero hits), so that line would resolve to `/FAILURES.md` and fail with a permission error, silently swallowed. This bug pre-dates and is untouched by either remediation task (out of scope by their own stated boundaries), but it means the actual human-visible surfacing cadence for a nightly-recorded violation is the next Friday `weekly.sh` run (which does correctly read and count `FAILURES.md`, lines 23-29) — up to six days, not "within a day" as the intake's desired outcome framed it. The record lands within a day; human visibility does not. See NEW-F1a/F1b below.

### F2 (gate authenticity) — **PARTIALLY REMEDIATED**

The HMAC-SHA256 chained-stamp mechanism in `scripts/gate_stamp.py` is real, correctly engineered for what it explicitly claims, and every attack named in its own acceptance criteria was independently reproduced against scratch fixtures (never the real key or real notes):

| Attack (scratch copies only, `GATE_HMAC_KEY_PATH` pointed at a scratch key) | Result |
|---|---|
| Hand-edit a stamped field (`qk_verdict`), leave stamp untouched | Correctly `STAMP_INVALID`, exit 1 |
| Edit stamped section text (`## Clearance`) without re-stamping | Correctly `STAMP_INVALID (section text changed since stamping)`, exit 1 |
| Edit upstream section text (`## Scope packet`) | Correctly `STAMP_INVALID (hephaistos_scope: section text changed since stamping)`, exit 1 — and correctly does NOT cascade to downstream stamps (chain binds to stamp *value*, not upstream section text — as designed) |
| Re-stamp an earlier stage after later stages exist (order/backfill attempt) | CLI *permits* the re-stamp write (exit 0 — only ordering-on-write for qk_verdict/relay_id is checked, not "does a later stage already exist"), but `verify` correctly flags the resulting chain break as `STAMP_INVALID or STAMP_ORDER_VIOLATION`, exit 1 — matches QK's own acceptance criterion 3 exactly |
| Swap `qk_verdict_stamp` and `relay_id_stamp` values between fields | Both correctly flagged invalid |
| Stamp-like field placed in the note body instead of frontmatter | `raw_field()` only scans the frontmatter substring; body text is never read as a stamp field — no confusion found |
| Duplicate frontmatter key (`qk_verdict:` twice, different values) | Confirmed a **real parsing divergence**: `governance_gate.py`'s `yaml.safe_load` resolves duplicate keys to the LAST occurrence; `gate_stamp.py`'s regex-based `raw_field()` resolves to the FIRST. In the direction tested, this happened to fail safe (the 3-string check saw the forged last value and correctly REFUSED). Not exploited further within this audit's time budget, but the two parsers reading the same frontmatter block with opposite duplicate-key semantics is a structural landmine — see NEW-F2d. |

Two findings that are **not exploits of a designed defense but of what the design leaves out entirely**, both reproduced empirically against scratch fixtures:

- **NEW-F2a (CRITICAL): `stamp_status: grandfathered` can be self-declared on any brand-new, entirely fabricated governed-task note, with zero stamps, and completely bypasses all verification.** A fixture note (`fake-new-task.md`) was constructed from scratch — fabricated `governance_state: done`, `hephaistos_scope: defined`, `qk_verdict: cleared`, `relay_id: RELAY-FAKE-999`, and `stamp_status: grandfathered` — with no `*_stamp` fields at all and body sections stating outright "Never actually reviewed by anyone" / "Never actually cleared by anyone." Run through `governance_gate.audit_all()` (scratch `TASKS` dir, scratch ledger with a matching fabricated `relay_id` line added), it reports **`GATE PASS`, `STAMPS: grandfathered (pre-mechanism, 2026-07-08)`, `audit-all: 0 violation(s)`.** The code (`gate_stamp.verify_stamps()`, lines ~231-238) checks `stamp_status == "grandfathered"` first and returns immediately with no allowlist, no restriction to the two originally-named legacy tasks, no date-boundary check. `governance/tasks/README.md` line 32 *describes* the flag as meaning "note predates the stamp mechanism (tasks #1-#2)" — a narrative claim the code does not enforce at all. This is a materially bigger hole than the disclosed dispatch-isolation residual: it requires **no key-hunting whatsoever**, only reading the vault-readable scope packet that documents the exact flag name and semantics — precisely the "drifting, non-key-hunting agent" threat class (RELAY-20260703-014) the mechanism was commissioned to catch.
- **NEW-F2b (CRITICAL): `governance_state` itself is not a stamped, content-bound field.** Only `hephaistos_scope`, `qk_verdict`, and `relay_id` are in `FIELD_SECTION`. On an otherwise-validly-stamped scratch note, hand-editing `governance_state` from `routed` to `done` (with the ledger-xref noise isolated out via a scratch ledger) produced **`GATE PASS`, `STAMPS: valid (3/3, chain ok)`, `0 violations`** — the exact field that carries the "is this task actually done" narrative claim (the claim F4 exists to police) has zero tamper-evidence. An attacker, or a drifting agent, can advance a task's headline status without touching any stamped field.
- **NEW-F2c (binding-constraint violation): the honesty section omits both gaps above.** The intake's binding constraint states the mechanism "MUST document its actual guarantee boundary explicitly." The shipped honesty section in `gate-authenticity-20260708.md` (lines 265-296) lists five specific non-guarantees (dispatch isolation, key-hunting adversary, condition-satisfaction truth, no-task-note detection, key-file OS protection) but never names NEW-F2a or NEW-F2b — both of which require zero key-hunting and are strictly easier to exploit than anything the honesty section discloses.

The phrase in the execution record — "**Argus F2 is closed to the extent closable on one host as one user; the dispatch-isolation residual remains structurally open**" — overclaims. It frames the only remaining gap as a *substrate-level, physically unfixable* one. NEW-F2a and NEW-F2b are not substrate-limited; they are ordinary, fixable implementation gaps (add an allowlist; bind `governance_state` into an existing stamp's payload) that were simply not built or disclosed.

### F3 (raw-guard coverage) — **REMEDIATED**

`~/.claude.json`'s registered `OBSIDIAN_PROTECTED_DIRS` reads `raw sources:raw:01_RAW_MATERIALS:raw-sources` — matches the claim exactly. A fresh Python process importing `vault_ops` with that exact env confirmed `update_note()` returns `{"error": "path is in a protected directory"}` for a real existing file in all four named lanes (`raw sources/`, `raw/`, `PEER-REVIEW/01_RAW_MATERIALS/`, `wiki/raw-sources/2026-05-13/`), and a control file under `Areas/` is correctly NOT blocked (checked via the guard's own set-intersection logic without executing a real write, to avoid mutating vault content).

New finding, MEDIUM: **NEW-F3a — the "raw" token already over-blocks two unrelated, pre-existing directories elsewhere in the vault.** `find . -type d -name raw` returns three hits, not one: the intended `./raw`, plus `./hephaistos/personal-assistant-agents/trismegiste/vault/raw` and `./artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/raw`. Both were confirmed to also refuse writes under the live guard test. This is not introduced by this remediation (the bare `raw` token predates it) and fails safe rather than under-protecting, but the task's boundary section only spoke abstractly about *future* collisions ("any future directory... named exactly `01_RAW_MATERIALS` or `raw-sources`") without checking whether the pre-existing `raw` token *already* collides today. `01_RAW_MATERIALS` and `raw-sources` were each confirmed unique (one match apiece) — only `raw` has this property today.

### F4 (narrative overstatement) — **REMEDIATED (narrow scope), with an adjacent unaddressed overstatement in the same document**

`grep -n "CLOSED 2026-07-08"` on `governance/EMERAULD-OS-BUILD-ORDER.md` now returns exactly 7 hits (gaps 1, 2, 4, 5, 6, 7, 9) — the gap-3 row and the Stage 4 paragraph no longer carry that label, matching acceptance criterion 1 exactly (9 minus 2 = 7). Both now read `PIPELINE LIVE 2026-07-08, closure pending`, contain the literal string `routed` and the date `2026-07-10`, and correctly state the gate is now "invoked automatically by the nightly pass" (true, per F1 above) — item 4's own instruction to check item 1's landed state before writing was followed correctly.

Two findings:
- **NEW-F4a (adjacent, not in this task's scope, MEDIUM):** gap 7's row in the *same table* — "Cron monitoring/alerting — **CLOSED 2026-07-08** (durable logs + FAILURES.md + **health-check reads it**)" — repeats the same false claim named in F1's caveat above. This was correctly out of item 4's stated boundary (only the gap-3 row and Stage 4 paragraph were licensed to change), so it is not a remediation failure, but it is a live overstatement in the exact document this task exists to make honest, and the operator's brief specifically asked to scrutinize "any remaining claim that overstates reality" in this file.
- **NEW-F4b (LOW, self-referential narrowing):** the new gap-3 text names the residual as "the dispatch-isolation half of F2 remains structurally open" — accurate as far as it goes, but (written the same day, by the same pipeline) it does not know about NEW-F2a/F2b because task #3's own honesty section never surfaced them. This is not a fabrication — it is downstream of NEW-F2c — but it means the build order's own "what's still open" framing is narrower than what this audit found underneath.

### F5 (silent-zero fallbacks) — **REMEDIATED**

Full reproduction of every case named in the operator's brief, using the exact code from `scripts/scheduled/weekly.sh` lines 45-46 and 50-53:

| Case | Reproduced result |
|---|---|
| `memory/agents/` glob matches nothing (empty dir) | `AGENT_LINES=unavailable` (RC 1) — correct |
| `memory/agents/` directory missing entirely | `AGENT_LINES=unavailable` (RC 1) — correct |
| Happy path (real files) | `AGENT_LINES=3` (RC 0) — correct |
| Legitimate zero-match grep (real dir, zero matches) | `OPEN_FLAGS=0` (RC 1, `-le 1` holds) — correct, does NOT regress to `unavailable` |
| Bad/nonexistent grep root (real error, RC 2) | `OPEN_FLAGS=unavailable` — correct |
| `set -o pipefail` scoped inside `$(...)` | Confirmed does not leak: parent shell's own `pipefail` option is unaffected after the subshell runs |

`grep -c '| wc -l || echo "unavailable"' scripts/scheduled/weekly.sh` returns `0` (down from 3) — the anti-pattern is gone. The QK-corrected `set -o pipefail; ...; RC=$?` idiom (not the packet's originally-drafted `PIPESTATUS[0]` form, which QK's own binding condition 1 empirically refuted before it shipped) is what is actually live, and it works exactly as claimed. This is the most cleanly and completely verified of the five remediations.

New finding, LOW: **NEW-F5a — `argus-remediations-20260708.md`'s own Item 3 acceptance criterion 2 is now stale.** The packet section still literally reads `grep -n 'PIPESTATUS\[0\]' scripts/scheduled/weekly.sh` returns 3 hits" but the shipped code contains zero `PIPESTATUS` occurrences (it uses `RC=$?` per QK's correction). Mechanically running that exact acceptance-criterion command today returns 0 hits, not 3 — a self-contradicting criterion inside the task note, harmless in practice (the execution record correctly narrates the real, corrected implementation, and the functional fix independently verified above is genuinely sound) but a stale-tie inside the governance artifact itself.

## New findings, ordered by severity

**CRITICAL**
1. **NEW-F2a** — `stamp_status: grandfathered` is a blanket, unrestricted self-service bypass for any new note, requiring no key-hunting. Reproduced empirically.
2. **NEW-F2b** — `governance_state` carries zero tamper-evidence; only three companion fields are stamped. Reproduced empirically.

**HIGH**
3. **NEW-F2c** — the mechanism's honesty section omits both critical gaps above, in direct tension with the intake's binding "must document its actual guarantee boundary explicitly" constraint.
4. **NEW-F1b** — the "already-monitored" justification for F1's cadence choice rests on a false claim (`health-check.sh` does not read `FAILURES.md`, and its own write path to that file is broken via an undefined `LOGDIR`). Real human-visible surfacing cadence is up to ~6 days (next Friday), not "within a day."

**MEDIUM**
5. **NEW-F3a** — the raw-lane guard's `raw` token already over-blocks two unrelated pre-existing directories (a trismegiste sample vault, a marketplace demo artifact); undisclosed, fails safe.
6. **NEW-F4a** — gap 7 in the build order repeats the same false "health-check reads it" claim; out of this task's scope but still live in the document.
7. **NEW-F2d** — `governance_gate.py` (yaml.safe_load, last-duplicate-key-wins) and `gate_stamp.py` (regex `raw_field`, first-duplicate-key-wins) resolve duplicate frontmatter keys with opposite semantics. One direction was tested and failed safe; the reverse direction was not exhaustively tested within this audit's scope and should be treated as an open structural risk, not a cleared one.

**LOW**
8. **NEW-F4b** — the build order's new gap-3 text names only the dispatch-isolation residual, narrower than what this audit found (downstream of NEW-F2c, not an independent fabrication).
9. **NEW-F5a** — `argus-remediations-20260708.md`'s own Item 3 acceptance criterion 2 (`PIPESTATUS[0]`, 3 hits) is stale against the actually-shipped `RC=$?` implementation.
10. **NEW-F1a** — no live cron firing has occurred yet against the new nightly.sh code (code committed 17:27 UTC, cron fires 22:00 UTC, audit run at 19:12 UTC); all "verified" claims in the execution record are manual, not operationally observed.

## Composition re-check

The baseline audit's core composition critique was that three surfaces (MCP, systemd router, governed-task gate) were "engineered independently and composed by proximity, not by a shared control point," with no automated enforcement and a documented, trivial bypass (original F2). That has genuinely changed: F1 wired a real, tested, non-blocking automated caller; F5 fixed real silent-failure code; F3 closed a real coverage gap; F4 corrected the one contradicted claim it was scoped to fix. **The system's overall posture is better than the baseline, not merely re-narrated as better.**

But the composition-level risk did not disappear — it moved. The soft-gate-to-hard-gate promotion plan (`governance/tasks/README.md` rule 1: tighten "after the first clean month," target roughly 2026-08-08) now depends on `audit-all: 0 violation(s)` as its evidentiary basis for "clean." NEW-F2a means that evidentiary basis can be produced by any drifting or bad-faith session — without any cryptographic sophistication, without hunting for the key — simply by adding one frontmatter line to any new note. The exact incident class the entire task-#3 mechanism exists to catch (RELAY-20260703-014: a session narrating a fabricated governance ruling directly into canonical files) could recur, self-label `grandfathered`, and produce a perfectly clean `audit-all` for the whole pilot month. **The soft-gate window until ~2026-08-08 is not yet safe to treat as a clean-month proof under the stamps as currently built** — the stamps materially raise the bar against careless hand-edits (verified, real improvement) but do not raise it at all against a session that reads the vault-readable scope packet naming the exact bypass flag. Recommend (flag only, not implemented here): restrict `stamp_status: grandfathered` to an explicit, code-level allowlist of the two task IDs it was created for, and bind `governance_state` into the existing chain, before the "first clean month" clock is trusted as evidence for the hard-gate promotion decision.

## New stale ties from the remediation work itself

- **NEW-F5a** (above): stale `PIPESTATUS[0]` acceptance criterion inside `argus-remediations-20260708.md` against the shipped `RC=$?` code.
- The README's `stamp_status` row (line 32) describes grandfathering as scoped to "tasks #1-#2" — a narrative claim with no code enforcement (this is the documentation half of NEW-F2a, not a separate tie, but worth naming as exactly the kind of narrative-implies-more-than-code-enforces pattern the baseline audit's F3/F4 were built around).
- No new dangling wikilinks, no new circular citations, and no new orphaned one-time-evidence files were found among the artifacts this audit read (git history for both task commits — `70ecf60` at 17:30:21 UTC and `d56a160` at 17:52:04 UTC — and RELAY-LEDGER entries `RELAY-20260708-004`/`-005` were cross-checked and are present and consistent, corroborating the timing narrative in both execution records).

## Provenance note and shared-substrate note (Mercury Protocol)

Both remediation task notes were authored by the same class of session, on the same host, the same day, that this audit scrutinizes — the identical provenance condition the baseline audit flagged. Per Argus's standing rule, every claim was checked independently rather than accepted: git commit timestamps and diffs, RELAY-LEDGER cross-references, a live `governance_gate.py --audit-all` run, and a full scratch-copy adversarial attack suite against `gate_stamp.py` (nine distinct attacks, all reproduced with commands shown above, none touching the real key/notes/ledger). Where a claim held up (F1's wiring, F3's coverage, F4's two named spots, F5's entire fix), it held up under direct execution, not narrative. Where a claim did not hold up (F2's "closed to the extent closable" framing), the gap was found by treating the artifact's own unusual polish and self-awareness as a reason for *more* scrutiny, per Argus's capture-signal rule — the eleven and nine QK binding conditions, the honesty sections, and the empirically-caught drafting bugs in both task notes made this the kind of "elegant" artifact that specifically warranted an adversarial pass rather than trust. External verification is recommended: a second, differently-provenanced review (different model or a human reading the scratch-attack transcripts directly) would strengthen confidence in NEW-F2a/F2b before the operator decides how to weight them against the soft-gate timeline.

## Escalation status and required human actions

**Escalate to Operator directly** (findings are recommendations, not mandates):

1. Decide whether `stamp_status: grandfathered` needs an explicit allowlist restriction (or equivalent) before relying on `audit-all: 0 violations` as evidence toward the ~2026-08-08 hard-gate promotion decision (NEW-F2a).
2. Decide whether `governance_state` should be folded into the existing stamp chain, given it currently carries the task's headline "done/routed" claim with zero tamper-evidence (NEW-F2b).
3. Decide whether the honesty section in `gate-authenticity-20260708.md` needs an addendum naming NEW-F2a/F2b explicitly, given the intake's own binding completeness constraint (NEW-F2c).
4. Decide whether gap 7 in `EMERAULD-OS-BUILD-ORDER.md` should be corrected alongside gap 3, given it repeats the same false "health-check reads it" claim (NEW-F4a), and whether `health-check.sh`'s undefined-`LOGDIR` bug should be fixed as its own small task (NEW-F1b).
5. No live exploit was executed against production files; all Critical/High findings above are reproduced against scratch copies within the authorized boundary.

## Overall verdict

**CONDITIONAL — genuinely improved from the baseline, not yet safe to treat as fully closed.** Three of five original findings (F1, F3, F5) are cleanly and completely remediated, verified by direct reproduction rather than accepted narrative. F4 is remediated for its exact, narrow scope. F2 built a real, well-tested tamper-evidence mechanism that correctly catches every attack it explicitly claims to defend against — but it ships with two undisclosed, non-substrate-limited bypasses (a blanket self-service grandfather flag and an entirely unstamped state field) that are easier to exploit than the one gap it does disclose, in direct tension with its own binding honesty-completeness requirement. Until NEW-F2a and NEW-F2b are addressed or explicitly accepted as residual risk by the Operator, the pipeline's headline claim — "Argus F2 is closed to the extent closable on one host as one user" — should be read as overclaiming, and the soft-gate-to-hard-gate promotion clock should not be started on the strength of a clean `audit-all` alone.

## Related

- [[governance/ARGUS-AUDIT — Governance Pipeline (2026-07-08)]]
- [[governance/tasks/argus-remediations-20260708]]
- [[governance/tasks/gate-authenticity-20260708]]
- [[governance/tasks/README]]
- [[governance/EMERAULD-OS-BUILD-ORDER]]
- [[Areas/PHAROS/RELAY-LEDGER — Live Governance Handoff Ledger]]
