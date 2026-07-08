---
type: governed-task
title: Governed Task — Stamp Bypass Closure (Argus Verification Criticals) (2026-07-08)
tags:
- governed-task
- argus
- stamp-bypass
status: active
domain: governance
governance_state: cleared
hephaistos_scope: defined
qk_verdict: cleared
relay_id: null
created: '2026-07-08'
updated: '2026-07-08'
vault_area: governance
canonical_path: governance/tasks/stamp-bypass-closure-20260708.md
hephaistos_scope_stamp: 306f12c3d6886c8d3c461645bef7f8d22655e3b1077588b8c4bca598f78bf5c5
hephaistos_scope_stamped_at: "2026-07-08T19:41:18Z"
hephaistos_scope_section_sha: d003e89a179f746a01562fc065efec30d10753df45b5d9d1860231394458bbd1
stamp_key_id: 8786b3fd
qk_verdict_stamp: a425fcba40c864e291caee03a2473454b04893e3dd023b3394f3b39ed94f223d
qk_verdict_stamped_at: "2026-07-08T19:41:18Z"
qk_verdict_section_sha: 024980f94d9c34c76fdff34a0a1bf90f618f63bf6a014bd0b6a2035da588acec
---

# Governed Task — Stamp Bypass Closure

> For future Claude: governed task #4. Closes the two CRITICAL findings of [[governance/ARGUS-AUDIT — Remediation Verification (2026-07-08)|the remediation-verification audit]] against the stamp mechanism built by [[governance/tasks/gate-authenticity-20260708|task #3]], plus the coupled honesty-section correction (that audit's HIGH finding 3, which exists only because of these two holes).

## Intake (Operator, 2026-07-08)

1. **Grandfather self-service bypass (CRITICAL 1):** `stamp_status: grandfathered` has no allowlist — any new note (including a wholly fabricated one) skips ALL stamp verification by adding one frontmatter line. Reproduced by Argus on a fixture. Desired outcome: exactly the two genuinely pre-mechanism tasks (`weekly-os-health-20260708`, `argus-remediations-20260708`) may carry the label; any other note claiming it is a named violation, surfaced by `--audit-all`.
2. **`governance_state` carries no tamper-evidence (CRITICAL 2):** the field the gate actually gates on can be forged (e.g. `routed`→`done`) on an otherwise fully-stamped note and produce a clean PASS. Reproduced by Argus. Desired outcome: forging `governance_state` on a stamped note becomes a detectable violation. Design consideration for HEPHAISTOS: the state legitimately transitions several times per task — the mechanism must support legitimate re-attestation at each transition without weakening the chain, and must define migration for task #3 (fully stamped but state-unstamped; a contemporaneous attestation at fix time is honest — a fabricated back-dated one is not).
3. **Honesty-section completeness (HIGH 3, coupled):** task #3's "does NOT guarantee" section and the build-order F2 wording omit these two holes and therefore violate the intake's own completeness constraint. After items 1–2 land, correct both texts to describe the actual post-fix boundary — including anything that remains open. Note: task #3's Clearance and Scope sections are HMAC-stamped; any edit to stamped section text invalidates stamps by design. The correction must respect that (e.g. corrections live in an unstamped addendum section or in this task's own record, never as silent edits to stamped text) — HEPHAISTOS decides the clean pattern.

**Out of scope (explicit):** the MEDIUM/LOW findings from the same audit — health-check.sh's broken LOGDIR branch and false "reads FAILURES.md" claim (build-order gap 7), raw-token over-blocking disclosure, duplicate-frontmatter-key parser divergence, live cron-firing evidence. These are real and remain flagged; the operator scoped this task to the two criticals.

**Standing constraints:** same as tasks #2–#3 — one-sitting rollout awareness vs the 22:00 nightly; no retro-stamps or silent backfill; honesty boundary must not be narrowed, only made complete; `updated:` preservation; the two genuinely-grandfathered notes stay grandfathered.

## Scope packet (HEPHAISTOS)

### Summary of design chosen

Three coupled fixes, all inside `scripts/gate_stamp.py` — **zero changes to
`scripts/governance_gate.py`** (its `check_note()`/`audit_all()` already call
`gate_stamp.summarize()` generically and absorb any new violation string into the
existing `if stamp_violations: ok = False` logic; this was verified by direct code
read, not assumed):

1. **A hardcoded allowlist** (`GRANDFATHERED_TASK_IDS`, a `frozenset`) closes NEW-F2a.
2. **A fourth stamped field, `governance_state_stamp`**, re-issued at every legitimate
   state transition, closes NEW-F2b.
3. **An unstamped addendum section**, appended to task #3's own note after its last
   stamped section, closes NEW-F2c (the honesty-completeness gap) — empirically
   verified safe against the actual `section_hash()` algorithm before being proposed
   here, not assumed safe from reading the code.

Everything below is precise enough to build without further design judgment calls;
where an implementation detail is left to Hermes's discretion, it is named as such.

### Fix 1 — Grandfather allowlist (closes NEW-F2a)

**Where it lives:** a hardcoded `frozenset` inside `scripts/gate_stamp.py` itself,
alongside the existing `FIELD_SECTION`/`CHAIN_PREV`/`FIELD_ORDER` module-level
constants:

```python
GRANDFATHERED_TASK_IDS = frozenset({
    "weekly-os-health-20260708",
    "argus-remediations-20260708",
})
```

**Why hardcoded-in-script, not file-based:** `scripts/gate_stamp.py` is tracked in the
vault's own git repo (confirmed: `d56a160` shows it introduced by task #3). Any
addition to this set is a diff to a script file, reviewed the same way any other code
change to the governance pipeline is reviewed — the identical tamper-evidence story
this whole mechanism already relies on for its own source. A file-based allowlist
(e.g. a `governance/tasks/GRANDFATHER-ALLOWLIST.md` note, or a JSON sidecar) would
need its **own** integrity mechanism — otherwise a drifting agent adds its own task ID
to that file exactly the way it currently adds `stamp_status: grandfathered` directly,
and the hole simply moves one file over. Stamping the allowlist file itself would
require solving a bootstrapping problem this task doesn't need to solve when a
hardcoded set, checked into the same repo as the verifier code, already carries
equivalent tamper-evidence for free. Rejected as unnecessary complexity.

**Violation class:** `GRANDFATHER_INVALID`. Fires when `stamp_status: grandfathered`
is present but `note.stem` (the task ID, matching the convention `task_id = note.stem`
already used throughout `do_stamp`/`verify_one`) is not in `GRANDFATHERED_TASK_IDS`.

**Fall-through, not short-circuit:** unlike the current code (which returns
immediately on `stamp_status == "grandfathered"`), the invalid-claim path does **not**
return early — it appends `GRANDFATHER_INVALID` to the violations list and falls
through into the normal per-field verification loop. For a wholly fabricated note with
no real `*_stamp` fields (the exact Argus fixture), this means `--audit-all` reports
both `GRANDFATHER_INVALID` and `STAMP_MISSING` for each stampable field — maximum
diagnostic honesty (what was claimed, and what is actually missing), at zero extra
design cost since it reuses the existing loop unchanged.

```python
def verify_stamps(note: Path) -> tuple[list[str], list[str]]:
    fm, text = split_note(note.read_text(encoding="utf-8"))
    fields = stampable_fields(fm)
    task_id = note.stem
    violations: list[str] = []

    if raw_field(fm, "stamp_status") == "grandfathered":
        if task_id in GRANDFATHERED_TASK_IDS:
            return ([f"grandfathered (pre-mechanism, {raw_field(fm, 'updated') or 'undated'})"], [])
        violations.append(
            f"GRANDFATHER_INVALID (stamp_status: grandfathered claimed by {task_id!r}; "
            "not in the hardcoded allowlist — claim rejected, full stamp verification enforced)"
        )

    if not fields:
        return (["no stampable fields yet (pre-clearance)"], []) if not violations else ([], violations)

    # ... existing key-load + per-field loop, unchanged, appends into `violations` ...
    # ... governance_state check (Fix 2) appended after the per-field loop ...
```

**LEDGER_XREF still runs on a listed grandfathered note — unchanged behavior.**
`summarize()` already calls `check_ledger_xref(note)` unconditionally, after
`verify_stamps()` returns, regardless of what `verify_stamps` reported (confirmed by
direct read of the current `summarize()` body). Fix 1 does not touch `summarize()` or
`check_ledger_xref()` at all — a listed grandfathered note keeps getting the same
ledger cross-reference check it gets today. Stated explicitly because it would be an
easy regression to introduce by accident while editing `verify_stamps()`.

### Fix 2 — `governance_state` attestation (closes NEW-F2b)

**Which states require attestation:** every value except the starting placeholder
`intake` — i.e. `scoped`, `cleared`, `routed`, `done`, `refused`, `abandoned` all
require a valid, current `governance_state_stamp`. Rationale: a partial rule ("only
`cleared`/`routed`/`done` need it") would itself be a second narrow-scope drift
surface to explain and defend later; "every value past the pre-work placeholder"
is the simplest rule that closes the actual exploit (advancing the headline status
string without evidence) at every point it could matter, and costs nothing extra to
implement since the check is a single field-presence test (`governance_state not in
{None, "", "intake"}`), not a per-state branch.

**Content-binding, and why no fixed section works:** `hephaistos_scope`, `qk_verdict`,
`relay_id` each bind to one fixed, named section of prose that role produces.
`governance_state` has no section of its own — it is a pure status flag, not backed
by freshly authored prose at each transition. Rather than inventing a synthetic
"N/A" section or requiring a new prose section per transition (over-engineering, and
a hard-to-satisfy requirement for the terminal states `refused`/`abandoned`, which
have no fixed canonical section today), the design **reuses the existing
`section_hash()` mechanism by anchoring `governance_state`'s stamp to whichever of the
three stage sections was most recently, actually stamped at attestation time** — this
answers the intake's own suggested design ("chain-prev = the LATEST existing stamp in
the chain") and simultaneously answers "what section-hash to use," with one rule
instead of two:

```python
def latest_companion_stamp(fm: str) -> tuple[str | None, str | None, str | None]:
    """Most-advanced FIELD_ORDER field that currently carries a stamp, or all-None."""
    latest = None
    for field in FIELD_ORDER:          # ["hephaistos_scope", "qk_verdict", "relay_id"]
        if raw_field(fm, f"{field}_stamp"):
            latest = field
    if latest is None:
        return (None, None, None)
    return (latest, raw_field(fm, f"{latest}_stamp"), FIELD_SECTION[latest])
```

**Why an explicit `governance_state_anchor` frontmatter field is required (not
re-derived at verify time):** if verify recomputed "latest companion field" fresh
every time, a benign later event (e.g. `relay_id_stamp` gets added at dispatch, a
moment before `governance_state` itself is flipped from `cleared` to `routed` and
re-stamped) would silently change which field counts as "latest" out from under an
*already-valid* `governance_state` stamp, producing a false-positive break unrelated
to any tampering. The existing `qk_verdict`/`relay_id` chain avoids exactly this
problem by embedding the **prior stamp's literal value**, not "whichever field is
currently earlier" — `governance_state` needs the same discipline: record which field
it anchored to, at stamp time, in a new key `governance_state_anchor` (value:
`hephaistos_scope` / `qk_verdict` / `relay_id` / `GENESIS`), and `verify` uses *that*
recorded field to fetch `prev` and the section heading, not a freshly recomputed
"latest." Tampering with `governance_state_anchor` itself is caught for free: pointing
it at a different field changes both `prev` and `sec_sha` inputs to the HMAC, which
were computed against the true original anchor — the recompute will not match the
stored digest. No new payload format is needed; `payload()`/`compute()` are reused
completely unchanged.

**Stamp command (reuses the existing `stamp` sub-command, field name
`governance_state`):**

```bash
python3 scripts/gate_stamp.py stamp <task-note> governance_state <value>
```

`do_stamp` branches on `field == "governance_state"` into a dedicated path (the three
existing fields' code path is otherwise untouched):

```python
def do_stamp_governance_state(note: Path, value: str) -> int:
    key = load_key()
    fm, text = split_note(note.read_text(encoding="utf-8"))
    task_id = note.stem
    current = raw_field(fm, "governance_state")
    if current != value:
        print(f"REFUSED: note has governance_state={current!r}, not {value!r}")
        return 1
    latest_field, latest_stamp, latest_heading = latest_companion_stamp(fm)
    if latest_field is None:
        anchor, prev, sec_sha = "GENESIS", "GENESIS", "GENESIS"
    else:
        ok, msg = verify_one(key, note, fm, text, latest_field)
        if not ok:
            print(f"REFUSED: anchor stamp {latest_field}_stamp does not re-verify: {msg}")
            return 1
        anchor, prev, sec_sha = latest_field, latest_stamp, section_hash(text, latest_heading)
    stamped_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    digest = compute(key, task_id, "governance_state", value, sec_sha, prev, stamped_at)
    upsert_lines(note, {
        "governance_state_stamp": digest,
        "governance_state_stamped_at": f'"{stamped_at}"',
        "governance_state_section_sha": sec_sha,
        "governance_state_anchor": anchor,
        "stamp_key_id": key_id(key),
    })
    print(f"STAMPED governance_state on {note.name} (anchor={anchor}, key_id {key_id(key)}, at {stamped_at})")
    return 0
```

**Verify path**, mirroring `verify_one`'s two-stage failure distinction (value/anchor
tamper vs. anchor-section-text tamper):

```python
def verify_governance_state(key: bytes, note: Path, fm: str, text: str) -> tuple[bool, str]:
    value = raw_field(fm, "governance_state") or ""
    stamp = raw_field(fm, "governance_state_stamp")
    stamped_at = raw_field(fm, "governance_state_stamped_at")
    stored_sha = raw_field(fm, "governance_state_section_sha")
    anchor = raw_field(fm, "governance_state_anchor")
    if not stamp or not stamped_at or not stored_sha or not anchor:
        return False, "GOVERNANCE_STATE_MISSING"
    if anchor == "GENESIS":
        prev, heading = "GENESIS", None
    elif anchor in FIELD_SECTION:
        prev, heading = raw_field(fm, f"{anchor}_stamp") or "", FIELD_SECTION[anchor]
    else:
        return False, f"GOVERNANCE_STATE_INVALID (unknown anchor {anchor!r})"
    cur_sha = section_hash(text, heading) if heading else "GENESIS"
    if compute(key, note.stem, "governance_state", value, cur_sha, prev, stamped_at) == stamp:
        return True, "valid"
    if compute(key, note.stem, "governance_state", value, stored_sha, prev, stamped_at) == stamp and cur_sha != stored_sha:
        return False, "GOVERNANCE_STATE_INVALID (anchor section text changed since stamping)"
    return False, "GOVERNANCE_STATE_INVALID (value, anchor stamp, or stamp fields altered — includes hand-edited governance_state)"
```

Wired into `verify_stamps()` after the per-field loop, gated on `governance_state not
in {None, "", "intake"}`; reuses whatever `key`/`KeyUnavailable` handling the function
already has (no second key load). New violation classes: `GOVERNANCE_STATE_MISSING`,
`GOVERNANCE_STATE_INVALID` — both flow into `summarize()`'s existing violations list
and therefore into `audit_all()`'s existing count with **zero changes to
`governance_gate.py`**.

**Migration for task #3** (`gate-authenticity-20260708.md`, currently
`governance_state: done`, no `governance_state_stamp`): at this task's rollout, run

```bash
python3 scripts/gate_stamp.py stamp governance/tasks/gate-authenticity-20260708.md governance_state done
```

This is a **contemporaneous** attestation — `governance_state_stamped_at` will carry
the true timestamp of this rollout (visibly later than the 17:5x timestamps on task
#3's three existing stamps), openly disclosing that this attestation was added after
the fact, which is the honest pattern the intake requires (not a fabricated backdate
claiming the state was attested on 2026-07-08). The anchor will resolve to
`relay_id` (task #3's most-advanced existing stamp). Task #3's `updated:` frontmatter
bumps to the real date of this rollout, per the standing no-backfill rule already
applied to the two grandfathered notes by task #3 itself.

**Tasks #1/#2:** fully exempted — the grandfather early-return in `verify_stamps()`
happens before the `governance_state` check is ever reached, so listed grandfathered
notes need no `governance_state_stamp` at all. No separate carve-out required; this
falls out of the existing control flow.

**Rollout lock-out risk (same class as task #3's QK condition 6):** if the code
changes (Fixes 1+2) land before task #3's own migration stamp is applied, the very
next `--audit-all` — including a 22:00 nightly firing mid-rollout — reports
`GOVERNANCE_STATE_MISSING` on task #3 for a reason unrelated to tampering. Steps must
land in one uninterrupted sitting exactly as task #3's own condition 6 required;
see Rollout order below.

### Fix 3 — Honesty-section correction pattern (closes NEW-F2c)

**Empirically verified, not assumed:** `## Execution record (Hermes-routed)` is task
#3's last section. `section_hash()` extracts from the line after a heading up to the
next `## `-prefixed line or EOF, then `rstrip()`s the joined body before hashing. I
ran the actual function against the real file, then simulated appending a new `##
Post-audit addendum (2026-07-08)` heading (with a blank-line separator) after the
existing content, and recomputed:

```
orig computed hash : 4474bffa21268691e95f8a7b2f4f727e5147cbab793c5366f1df30918fd4aa8a
stored section sha : 4474bffa21268691e95f8a7b2f4f727e5147cbab793c5366f1df30918fd4aa8a
match: True
new computed hash for Execution record after append: 4474bffa21268691e95f8a7b2f4f727e5147cbab793c5366f1df30918fd4aa8a
still matches stored?: True
```

The append does **not** change the Execution record section's hash — `rstrip()`
absorbs the blank-line separator identically whether the section ends at EOF or at a
newly-appended heading — so `relay_id_stamp` (and, by the same reasoning, the two
earlier sections, which are unaffected by anything appended after the file's last
section today) remain valid after the append. This confirms the pattern proposed in
the intake is safe **for this specific file's current content**, not merely
plausible from reading the algorithm.

**Pattern:** append, verbatim, after task #3's `## Execution record (Hermes-routed)`
section:

```markdown

## Post-audit addendum (2026-07-08)

> Appended by [[governance/tasks/stamp-bypass-closure-20260708|governed task #4]]
> after this note's own stamped sections. This section carries no stamp and does not
> alter any text above it — the three stamped sections' hashes were confirmed
> unchanged before and after this append (task #4 acceptance criterion 8). It exists
> solely to keep this note's own honesty boundary complete, per the binding
> constraint task #3 shipped under.

The Argus remediation-verification audit
([[governance/ARGUS-AUDIT — Remediation Verification (2026-07-08)|2026-07-08]]) found
that the "does NOT guarantee" section above, while accurate as far as it goes,
omitted two CRITICAL gaps strictly easier to exploit than the dispatch-isolation
residual it does disclose:

- **NEW-F2a:** `stamp_status: grandfathered` had no allowlist — any new note could
  self-declare it and bypass all stamp verification, with zero key-hunting required.
- **NEW-F2b:** `governance_state` itself carried no tamper-evidence — hand-editing it
  (e.g. `routed` → `done`) on an otherwise fully-stamped note produced a clean PASS.

Both are closed by [[governance/tasks/stamp-bypass-closure-20260708|governed task
#4]]: a hardcoded allowlist (`GRANDFATHERED_TASK_IDS` in `scripts/gate_stamp.py`)
restricts the grandfather flag to the two task IDs it was created for, and a new
`governance_state_stamp` (re-issued at every transition, anchored to this note's own
most-advanced stage stamp) closes NEW-F2b. This note's `governance_state` now carries
that stamp too (see frontmatter above). The dispatch-isolation residual named in the
original honesty section above remains open and is not addressed by task #4 — it is
not substrate-fixable by any signing scheme, as already stated there.
```

`updated:` on task #3 bumps to the real date this addendum lands (same rollout as the
migration stamp above — one frontmatter edit covers both).

**Why not edit the existing "does NOT guarantee" section directly:** it is inside the
stamped `## Clearance (Queen Keyport)`... no — correction: the "does NOT guarantee"
section lives inside `## Scope packet (HEPHAISTOS)`, which is the **first** stamped
section, not the last. Editing it would invalidate `hephaistos_scope_stamp`
immediately (and, via the chain, everything downstream). QK's own condition 9 on task
#3 already forbids narrowing or editing it. The addendum pattern is the only option
that adds the missing disclosure without touching stamped text anywhere in the file.

### Documentation updates (closes the coupled honesty gap in the build order + README)

**`governance/EMERAULD-OS-BUILD-ORDER.md`, gap-3 row** — replace the existing cell
text with:

> **PIPELINE LIVE 2026-07-08, closure pending** — task #1 at `routed` until its
> 2026-07-10 live-run evidence (QK condition 8); gate runs soft, invoked automatically
> by the nightly pass since task #2 (Argus F1 remediation); Argus F2 addressed by
> task #3 (HMAC-chained stage stamps, verified nightly) and task #4 (grandfather
> allowlist + `governance_state` attestation, closing NEW-F2a/NEW-F2b named by the
> 2026-07-08 remediation-verification audit): hand-edits, post-clearance section
> tampering, out-of-order sequences, unrestricted grandfather self-labeling, and
> `governance_state` forgery on an otherwise-stamped note are now tamper-EVIDENT; the
> dispatch-isolation half of F2 remains structurally open on a single-user host

Only this row's cell text changes (plus this file's `updated:`), matching the
git-diff discipline QK already required for task #3's own gap-3 edit.

**`governance/tasks/README.md` rule 1b** — replace with:

> 1b. Stage transitions are stamped with `scripts/gate_stamp.py` (task #3, extended by
> task #4): HMAC over the stage's section text, chained in order — stamp after
> writing your section, and re-stamp `governance_state` itself immediately after
> every value change (task #4; anchored to the most-advanced stage stamp at
> attestation time). Know the boundary: stamps are tamper-EVIDENCE against
> non-key-hunting drift (the RELAY-20260703-014 class) and against unrestricted
> grandfather self-labeling or state forgery (task #4's NEW-F2a/F2b closure) — not
> proof of dispatch isolation. Full honesty section:
> [[governance/tasks/gate-authenticity-20260708|task #3 scope packet]] (+ its
> post-audit addendum) + [[governance/tasks/stamp-bypass-closure-20260708|task #4
> scope packet]].

**`governance/tasks/README.md` `stamp_status` table row** — replace with:

> | `stamp_status` | executor, once | `grandfathered` = note predates the stamp
> mechanism; restricted to a hardcoded allowlist in `scripts/gate_stamp.py`
> (`GRANDFATHERED_TASK_IDS`, currently tasks #1-#2 only, task #4) — any other note
> setting this flag is rejected as a named `GRANDFATHER_INVALID` violation, never
> silently honored |

**`governance/tasks/README.md`, new table row** (add after the existing `{field}_stamp`
row):

> | `governance_state_stamp` / `_stamped_at` / `_section_sha` / `_anchor` |
> `scripts/gate_stamp.py` only | Re-attested at every `governance_state` transition
> past `intake` (task #4); anchored (`_anchor`) to whichever of the three stage
> stamps above is most-recently issued at attestation time, reusing that stage's own
> section hash — catches forged or stale state (e.g. `routed`→`done`) on an
> otherwise fully-stamped note |

### Acceptance criteria (mechanical)

1. **Fabricated-note-with-grandfather-flag → named violation.** Reproduce the
   Argus fixture (fabricated note, `stamp_status: grandfathered`, task ID not in
   `GRANDFATHERED_TASK_IDS`, no real stamps) on a scratch copy. `gate_stamp.py
   verify` and `governance_gate.py --audit-all` both report `GRANDFATHER_INVALID`
   (plus `STAMP_MISSING` per field); non-zero exit / non-zero violation count.
2. **`governance_state` forge on a stamped fixture → named violation.** On a scratch
   fixture with a valid `governance_state_stamp` for `routed`, hand-edit
   `governance_state` to `done` without re-stamping. `verify` reports
   `GOVERNANCE_STATE_INVALID`; exits 1.
3. **Legitimate state transition + re-attestation → clean PASS.** On a scratch
   fixture, advance `governance_state` through at least two real transitions (e.g.
   `scoped` → `cleared`), stamping via the real CLI at each step, including at least
   one transition where a companion field (`qk_verdict`) also gets freshly stamped in
   between. `verify` reports valid at every step; the anchor correctly reflects the
   most-advanced companion stamp at each attestation time.
4. **Task #3 migration → audit-all fully clean.** After running the migration stamp
   command and appending the addendum, `python3 scripts/governance_gate.py
   --audit-all` exits 0, 0 violations; `gate-authenticity-20260708.md` shows `STAMPS:
   valid (4/4, chain ok)`. `git diff` on that file shows only frontmatter additions
   (`governance_state_stamp`/`_stamped_at`/`_section_sha`/`_anchor`, `updated:`) plus
   the appended addendum section — the three existing stamped sections are
   byte-identical (confirmed via `gate_stamp.py verify` before and after, matching
   this packet's own empirical pre-check).
5. **Both real grandfathered notes still clean.** `weekly-os-health-20260708.md` and
   `argus-remediations-20260708.md` continue to show `STAMPS: grandfathered` with 0
   violations after Fix 1 lands (both task IDs remain in the allowlist).
6. **No regression on task #3's own five adversarial/mechanical criteria.** Re-run,
   against fresh scratch fixtures built under the modified `gate_stamp.py`: (a)
   hand-edited-frontmatter forgery → `STAMP_INVALID`; (b) post-clearance
   conditions-text edit → `STAMP_INVALID (section text changed since stamping)`; (c)
   out-of-order stamp sequence → `STAMP_ORDER_VIOLATION`; (d) `gate_stamp.py verify`
   independently runnable, correct exit codes, no dependency on `governance_gate.py`;
   (e) enrichment normalize+`safe_dump` round-trip on a fully-stamped fixture (now
   including `governance_state_stamp`) → still valid; (f) renamed/missing key file →
   every stampable note (including `governance_state`) reports `KEY_UNAVAILABLE`, not
   `STAMP_INVALID`/`GOVERNANCE_STATE_INVALID`.
7. **This task's own note passes through the live mechanism.** As
   `stamp-bypass-closure-20260708.md` moves through `scoped → cleared → routed →
   done`, each transition is stamped contemporaneously (`hephaistos_scope`,
   `qk_verdict`, `relay_id`, and `governance_state` at every state change) —
   demonstrating the extended mechanism on live, current-day use, not only fixtures.
8. **Addendum safety re-confirmed at execution time.** Immediately before and after
   appending the addendum to the real `gate-authenticity-20260708.md` file (not the
   scratch copy used to design this packet), `gate_stamp.py verify` shows all
   existing stamps valid in both runs.
9. **Documentation lands as specified.** `git diff` on
   `governance/EMERAULD-OS-BUILD-ORDER.md` touches only the gap-3 cell (+
   `updated:`); `git diff` on `governance/tasks/README.md` touches only rule 1b, the
   `stamp_status` row, and the one new table row (+ `updated:`).
10. **Scope boundary held.** `git diff` overall touches only: `scripts/gate_stamp.py`
    (Fixes 1+2); `governance/tasks/gate-authenticity-20260708.md` (frontmatter
    additions + addendum + `updated:`); this note (frontmatter + all four sections +
    `updated:`); `governance/EMERAULD-OS-BUILD-ORDER.md` (gap-3 cell + `updated:`);
    `governance/tasks/README.md` (rule 1b + two table changes + `updated:`).
    **`scripts/governance_gate.py` is untouched** (verified: no code path there needs
    to change for either fix). No other governed-task note, no cron/systemd surface,
    no MCP server, no `vault_ops.py` change.

### Artifact list / scope boundary

**Modified:** `scripts/gate_stamp.py` (new module-level `GRANDFATHERED_TASK_IDS`
constant; `verify_stamps()` gains the allowlist check + governance_state check;
new functions `latest_companion_stamp`, `do_stamp_governance_state`,
`verify_governance_state`; `do_stamp`/`main` branch on `field == "governance_state"`);
`governance/tasks/gate-authenticity-20260708.md` (frontmatter: new
`governance_state_stamp`/`_stamped_at`/`_section_sha`/`_anchor` keys,
`updated:` bump; body: one appended, unstamped addendum section — the three existing
stamped sections are untouched); this note (all sections, frontmatter stamps applied
live at each transition); `governance/EMERAULD-OS-BUILD-ORDER.md` (gap-3 cell,
`updated:`); `governance/tasks/README.md` (rule 1b, `stamp_status` row, one new
table row, `updated:`).

**Explicitly untouched:** `scripts/governance_gate.py`; `scripts/scheduled/nightly.sh`;
`scripts/scheduled/weekly.sh`; the MCP server; `vault_ops.py`; both real grandfathered
notes' bodies (frontmatter untouched — they never receive `governance_state_stamp`,
by design); any cron/systemd surface; no new daemon.

**Out of scope (reaffirmed from the intake):** the MEDIUM/LOW findings from the same
Argus audit — `health-check.sh`'s broken `LOGDIR` branch and false "reads
FAILURES.md" claim (build-order gap 7, NEW-F1b/NEW-F4a), the `raw` token
over-blocking disclosure (NEW-F3a), the duplicate-frontmatter-key parser divergence
(NEW-F2d — this task does not touch `raw_field()`'s or `yaml.safe_load`'s duplicate-key
semantics, and the new `governance_state`/`GRANDFATHER_INVALID` code inherits whatever
`raw_field()` already does there, unchanged), the stale `PIPESTATUS[0]` acceptance
criterion in task #2 (NEW-F5a), live cron-firing evidence (NEW-F1a).

### Rollout order (must land as one ordered execution burst — same lock-out class as task #3's QK condition 6)

1. Add `GRANDFATHERED_TASK_IDS` + the `GRANDFATHER_INVALID` check to
   `verify_stamps()`. Build a scratch fixture reproducing Argus's exact fake-new-task
   fixture; confirm `GRANDFATHER_INVALID` fires; confirm both real grandfathered
   notes still verify clean.
2. Add `governance_state` support (`latest_companion_stamp`,
   `do_stamp_governance_state`, `verify_governance_state`, wiring into
   `verify_stamps()`). Build scratch fixtures for: legitimate roundtrip across two
   transitions, hand-edit-without-restamp forgery, and an anchor-pointing-at-wrong-
   field tamper. Confirm all three behave as designed.
3. Re-run task #3's original adversarial fixture suite (acceptance criterion 6 above)
   against the modified `gate_stamp.py` — zero regression, before touching any real
   task note.
4. Migrate `gate-authenticity-20260708.md`: stamp `governance_state: done` for real
   (contemporaneous); append the addendum section; bump `updated:`. Re-verify all 4
   stamps clean immediately (acceptance criterion 8).
5. Update `governance/EMERAULD-OS-BUILD-ORDER.md` and `governance/tasks/README.md` to
   the post-fix wording.
6. Run `python3 scripts/governance_gate.py --audit-all` — must show 0 violations, all
   three real governed-task notes clean.
7. Stamp this task's own transitions (`hephaistos_scope`, `qk_verdict`, `relay_id`,
   and `governance_state` at each of `scoped`/`cleared`/`routed`/`done`) live, using
   the real tool, mirroring task #3's own bootstrap precedent — this packet does not
   self-stamp for the same reason task #3's packet did not: the code implementing
   `governance_state` stamping does not exist at the moment this packet is written.

**Why one sitting, concretely:** once step 2's code is live, any governed-task note
whose `governance_state` is not `intake` and lacks a `governance_state_stamp` reports
`GOVERNANCE_STATE_MISSING`. Task #3 sits at `governance_state: done` with no such
stamp until step 4 completes. If step 2 lands and a 22:00 nightly `--audit-all` fires
before step 4, that run produces a real (not hypothetical) `FAILURES.md` entry for a
reason unrelated to actual tampering — identical in kind to the risk task #3's QK
condition 6 named for its own rollout. If the rollout cannot complete in one sitting,
steps must land in an order where step 2 (governance_state code) is never the last
thing committed before a pause without step 4 (task #3's migration stamp) already
having landed alongside it.

## Clearance (Queen Keyport)

**Verdict: CLEARED (approve-with-constraints), 10 binding conditions.** The three-fix
design (hardcoded grandfather allowlist; a fourth anchored `governance_state` stamp;
an unstamped honesty addendum) is not refused. Two of the packet's own load-bearing
empirical claims were independently reproduced against the real code and the real
file (not accepted from prose); both held. Two further gaps were found by direct
execution/tracing that the packet itself did not surface — one is a design residual
that must be disclosed, not solved, in this rollout; one is a rollout-sequencing bug
that must be corrected before execution. Neither requires re-opening the chosen
design.

**Governance domain:** internal governance-tooling integrity (same domain as task
#3) — a script extension, a hardcoded allowlist, a new stamped field, and a
documentation-only addendum. No external-facing surface, no client data, no
regulatory exposure. Consequence domain is the auditability/tamper-evidence of the
governance pipeline's own self-attestation, and — because this task is itself the
first non-grandfathered note to live through the new `governance_state` requirement
— the pipeline's own rollout-correctness. Delta-first review applies; none of the
escalation triggers in `QUEEN-KEYPORT_OPERATIONS.md` (client-facing, regulatory,
safety, "exhaustive" framing) are met.

**Evidence threshold applied — verified by direct execution against a scratch copy
of the real file and the real code, not accepted from the packet's prose:**

- **(a) Addendum-append safety — CONFIRMED, independently.** `gate_stamp.section_hash()`
  was imported and run directly (not re-implemented) against a scratch copy of the
  real `gate-authenticity-20260708.md` (identical filename, scratch directory, no
  real key needed — this check has no HMAC dependency). Computed hash for
  `## Execution record (Hermes-routed)` against the file as-is matched the stored
  `relay_id_section_sha` exactly
  (`4474bffa21268691e95f8a7b2f4f727e5147cbab793c5366f1df30918fd4aa8a`). After
  appending a `## Post-audit addendum (2026-07-08)` heading with a blank-line
  separator, the recomputed hash for the same section was byte-identical. The
  packet's claim holds under independent reproduction, not just the packet's own
  self-check — `rstrip()` on the joined body genuinely absorbs the trailing
  blank line whether the section ends at EOF or at a new heading. No condition
  needed beyond re-running this exact check against the real file immediately
  before and after the real append (already acceptance criterion 8 — reaffirmed
  as binding, condition 1 below).

- **(b) Grandfather fall-through — CONFIRMED, no evasion found.** Traced the sketch's
  exact control flow for the Argus fixture (fabricated `stamp_status: grandfathered`,
  task ID not in the allowlist, content-bearing `hephaistos_scope`/`qk_verdict`/
  `relay_id` values but zero real `*_stamp` fields): `stampable_fields()` returns all
  three field names (it keys off content values, not stamp presence), so `fields` is
  non-empty and the `if not fields:` branch is never reached — the invalid claim
  falls through into the unchanged per-field loop, producing `GRANDFATHER_INVALID`
  plus three `STAMP_MISSING` entries. Separately traced the **degenerate case the
  packet did not walk through explicitly** — an invalid grandfather claim on a note
  with genuinely zero stampable content (no field is "defined"/non-pending/non-empty):
  `violations` is non-empty when the `if not fields:` line is reached, so the ternary
  `return (["no stampable fields yet (pre-clearance)"], []) if not violations else
  ([], violations)` evaluates its `else` branch — `([], violations)` — not the
  pre-clearance message. `summarize()` then sees a non-empty `violations` list and
  returns `STAMPS: GRANDFATHER_INVALID (...)`, never a silent pass. No evasion path
  found in either branch of this design for a false grandfather claim.

- **(c) `governance_state` chain-anchor — NOT fully closed as designed; a residual,
  not a blocker.** `verify_governance_state()` recomputes the HMAC over the note's
  *currently stored* `governance_state` value, current anchor-section hash, and the
  anchor's *currently stored* companion stamp — so a **partial** hand-edit (state
  changed, stamp left alone) is correctly caught (`GOVERNANCE_STATE_INVALID`), exactly
  as intended. But the mechanism has no freshness or monotonicity check: `stamped_at`
  is an opaque string bound into the HMAC, not compared against the note's own prior
  attestation time. Traced concretely: if `governance_state`, `governance_state_stamp`,
  `governance_state_stamped_at`, `governance_state_section_sha`, and
  `governance_state_anchor` are **together** reverted to a byte-consistent earlier
  state (recoverable from this file's own git history, since `governance/tasks/` is
  git-tracked — or from any external copy), `verify_governance_state()` recomputes the
  same digest and reports `valid` — because internal self-consistency, not
  current-and-only-ever-true status, is what the HMAC actually proves. This is a
  structural property of the whole stamp design (the same replay is theoretically
  possible against `hephaistos_scope`/`qk_verdict`/`relay_id`, which are also plain
  upserted scalars with no monotonic anchor), but it applies with materially more
  force to `governance_state` specifically, because — unlike the other three fields,
  which are stamped exactly once each in normal operation — `governance_state` is
  explicitly designed to be re-stamped at every transition, so multiple genuinely-valid
  past digests will exist across this task's own git history for the *same field, at
  different values*, all individually replayable. This is exactly the class of
  undisclosed-residual pattern NEW-F2c itself exists to close — shipping this closure
  without naming it would reopen the identical honesty gap one layer down. Bound
  below (condition 3): it must be named in the Fix 3 addendum, not solved by this
  task.

- **(d) Rollout-sequencing gap — found, must-fix, not a residual.** Traced the
  packet's own rollout order against this task's own current frontmatter
  (`governance_state: scoped`, set at Intake, before Fix 2's code exists). Once step 2
  lands, `verify_stamps()` requires a valid `governance_state_stamp` on **any**
  governed-task note whose `governance_state` is not `intake`/empty — including this
  very note, which is already sitting at `scoped`. The packet's step 7 (stamping this
  note's own transitions) runs **after** step 6's `--audit-all` check. As literally
  ordered, step 6 would report at least one violation
  (`GOVERNANCE_STATE_MISSING` on `stamp-bypass-closure-20260708.md` itself) — directly
  contradicting the packet's own stated bar for that step ("must show 0 violations,
  all three real governed-task notes clean" — by execution time there are four,
  not three, real governed-task notes, and the fourth is this one). This is a
  sequencing bug in the packet as written, not a disclosed-and-accepted risk. Bound
  below (condition 4): must-fix before rollout begins.

- **(e) Time-margin check.** Current time at review: `Wed Jul 8 19:35:01 UTC 2026`
  (confirmed via `date`) — approximately 2h25m before the 22:00 nightly
  `--audit-all` fire. Task #3's own precedent for a **smaller** change (one new
  allowlist check, no migration of an already-`done` note, no live governance_state
  walk) required and used roughly 4h margin. This rollout is larger: two new checks,
  a real migration of task #3's frontmatter and body, doc edits across two files,
  and — per binding condition 4 — an additional live stamp of this note's own
  `hephaistos_scope` and `governance_state:scoped` before the audit-all gate. 2h25m
  is a materially tighter margin than the precedent this exact class of risk was
  named against. Bound below (condition 5).

**Right-arm synthesis (Philosopher / Power-Analyst):** no divergence; both concur
clearance-with-conditions is correct. Philosopher's finding: the packet is candid
about what it closes and reuses task #3's own honesty-boundary discipline
correctly — the one place candor must extend further is precisely where polish is
highest, per Argus's own capture-signal rule applied recursively: the packet's most
elegant claim (the `governance_state` anchor design, argued at length against
inventing a synthetic section) is also the one place a residual risk was found
underneath, echoing exactly how NEW-F2a/F2b were found underneath task #3's own
polish. Power-Analyst's finding: the real leverage point in this rollout is
ordering, not cryptography — the two new checks are correctly engineered against the
threats they name, but their *activation moment* (step 2 landing) redistributes risk
onto every governed-task note that already exists at that instant, including the one
authoring this very clearance. A design can be sound and still lock out its own
author if the rollout order does not account for its own existence as a live,
in-flight governed-task note.

**Diamond-Eyes:** wise and caring, not merely defensible, with one caveat: naming
the replay residual (condition 3) and fixing the sequencing gap (condition 4) are
what keep this task from repeating, one layer down, the exact overclaiming pattern
it was created to close. Shipping without both would be procedurally clean and
substantively unfaithful to the task's own purpose. With both bound, the design is
proportionate to the two CRITICAL findings it targets, adds no speculative
complexity, and the honesty addendum becomes genuinely complete rather than merely
longer.

### Binding conditions (executor must satisfy before this task moves to `done`)

1. **Re-confirm addendum safety at execution time, on the real file.** Immediately
   before and after appending the addendum to the real `gate-authenticity-20260708.md`
   (not a scratch copy), run `gate_stamp.py verify` and confirm all three existing
   stamps remain valid in both runs (packet's own acceptance criterion 8 — reaffirmed
   as binding, not optional, given this review's independent reproduction used a
   scratch copy and the real file must still be checked at the moment of the real
   edit).
2. **Preserve the fall-through ternary exactly as sketched.** The line
   `return (["no stampable fields yet (pre-clearance)"], []) if not violations else
   ([], violations)` must ship with this precedence unchanged — do not "simplify" it
   into an early return during implementation; this review confirmed it is the reason
   a false grandfather claim on a content-empty fabricated note still surfaces as a
   violation rather than a silent pre-clearance pass.
3. **Name the replay/rollback residual in the Fix 3 addendum, as a fourth disclosed
   gap.** Alongside dispatch isolation and the key-hunting-adversary boundary already
   carried forward from task #3, the addendum must state in substance: stamps
   (including `governance_state` and the three original stage stamps) are HMAC
   self-consistency checks over currently-stored frontmatter values, not proof against
   replaying a stale-but-internally-consistent frontmatter block reconstructed from
   this file's own git history or any external copy; the mechanism does not bind
   `stamped_at` to a monotonic clock or an append-only ledger. This is not optional
   polish — shipping the addendum without it reopens the same honesty gap this task
   exists to close, one layer down.
4. **Fix the rollout order before execution begins.** Fold stamping this note's own
   `hephaistos_scope` (chain: GENESIS) and `governance_state: scoped` into the
   migration step (packet's step 4, alongside task #3's migration), immediately after
   the regression suite (step 3) and before docs/audit-all (steps 5-6) — not deferred
   to step 7. Step 6's `--audit-all` check must show 0 violations across **all four**
   real governed-task notes that exist at that point in time, including this one, not
   three. As `qk_verdict` and `relay_id` become available on this note (this
   clearance, then Hermes's dispatch), their own `governance_state` transitions
   (`cleared`, `routed`, `done`) get stamped live at each transition per the packet's
   step 7, using the real tool, in the order the transitions actually occur — this
   condition only moves the *first* transition (`scoped`) earlier, it does not change
   the live-stamping requirement for the rest.
5. **Time-margin gate.** Do not begin step 1 (code changes to `gate_stamp.py`) unless
   the executing session can commit to reaching a safe pause point — every currently
   existing governed-task note, including this one, holding a fully valid,
   non-violating stamp state — with comparable margin to task #3's own ~4h precedent.
   If reviewed margin to 22:00 UTC is under approximately 3h at the moment execution
   would begin, defer code-landing steps 1-2 to a session with sufficient runway
   rather than start and risk a real (not hypothetical) `FAILURES.md` entry from a
   mid-rollout nightly firing for a reason unrelated to actual tampering.
6. **`scripts/governance_gate.py` remains untouched — confirmed, not merely assumed.**
   Direct read confirms `check_note()` computes its `ok` boolean before even calling
   `gate_stamp.summarize()`, and discards `_stamp_violations` entirely — new violation
   strings never touch `--hard`'s exit behavior there, by existing design.
   `audit_all()` already has a generic `if stamp_violations: ok = False` that absorbs
   any new violation string, including `GRANDFATHER_INVALID`,
   `GOVERNANCE_STATE_MISSING`, and `GOVERNANCE_STATE_INVALID`, with zero code changes.
   Any diff touching this file is a scope-boundary failure.
7. **No retro-stamps, no backdating.** Task #3's migration stamp and this note's own
   `governance_state:scoped` stamp (condition 4) must carry true, contemporaneous
   `_stamped_at` timestamps from the actual rollout moment, openly later than the
   original 17:5x-era stamps — matching the honest-disclosure pattern already applied
   to the two grandfathered notes and required by the standing intake constraint.
8. **Documentation edits land exactly as scoped.** `git diff` on
   `governance/EMERAULD-OS-BUILD-ORDER.md` touches only the gap-3 cell plus
   `updated:`; `git diff` on `governance/tasks/README.md` touches only rule 1b, the
   `stamp_status` row, and the one new table row, plus `updated:` — matching the
   packet's own acceptance criterion 9.
9. **Scope boundary held.** Only the artifacts named in the packet's "Artifact list /
   scope boundary" section may change. No changes to `scripts/scheduled/nightly.sh`,
   `scripts/scheduled/weekly.sh`, the MCP server, `vault_ops.py`, or either
   grandfathered note's body. The two grandfathered task IDs
   (`weekly-os-health-20260708`, `argus-remediations-20260708`) remain the only
   entries in `GRANDFATHERED_TASK_IDS`.
10. **All ten of the packet's own acceptance criteria must pass, plus an eleventh:**
    at the moment step 6's `--audit-all` is run, all four real governed-task notes
    (tasks #1-#4) show 0 violations — not three, per condition 4 above.

**Honesty boundary carried forward, not narrowed:** task #3's original boundary
statement (does not prove dispatch isolation; does not defend against a
key-hunting same-substrate adversary) ships unedited, inside the addendum's
framing, per task #3's own condition 9. This task adds the replay/rollback
residual (condition 3) as a genuinely new disclosure, not a restatement.

## Execution record (Hermes-routed)

*(pending)*
