---
type: governed-task
title: Governed Task — Gate Authenticity (Argus F2) (2026-07-08)
tags:
- governed-task
- argus
- gate-authenticity
status: active
domain: governance
governance_state: done
hephaistos_scope: defined
qk_verdict: cleared
relay_id: RELAY-20260708-005
created: '2026-07-08'
updated: '2026-07-08'
vault_area: governance
canonical_path: governance/tasks/gate-authenticity-20260708.md
hephaistos_scope_stamp: e5355b97930a46a00b8afa062bb85767e9bad7ae5f9868e8be1867151465176e
hephaistos_scope_stamped_at: "2026-07-08T17:50:40Z"
hephaistos_scope_section_sha: df0ce6b4744be579a1038841c698bac08922855c99f4b6f014aa371a580fc7fb
stamp_key_id: 8786b3fd
qk_verdict_stamp: 9706216817ffacfd77bf3e04a50fc2ca528e5084fd29f3503cb8c0eddf18d810
qk_verdict_stamped_at: "2026-07-08T17:50:40Z"
qk_verdict_section_sha: 9d36a736ca8e4342f2f4c890cc41bd6860ca551f8a3c6fbe74e508ae4fa4d6d3
relay_id_stamp: 75d9d5b0e0d1f98c51f9a3176aa9b5a11907f27552b9f8e225af4c90afcb5984
relay_id_stamped_at: "2026-07-08T17:51:25Z"
relay_id_section_sha: 4474bffa21268691e95f8a7b2f4f727e5147cbab793c5366f1df30918fd4aa8a
---

# Governed Task — Gate Authenticity (Argus F2)

> For future Claude: governed task #3. Closes the [[governance/ARGUS-AUDIT — Governance Pipeline (2026-07-08)|Argus audit]]'s F2 residual, left open by scope in tasks #1 and #2: `scripts/governance_gate.py` validates three YAML frontmatter strings, so hand-editing three lines produces a PASS even in `--hard` mode, and nothing distinguishes genuinely isolated HEPHAISTOS/Queen-Keyport dispatches from one session narrating both, or detects post-clearance tampering with the conditions text.

## Intake (Operator, 2026-07-08)

**Threat model (grounded, not hypothetical):** the RELAY-LEDGER's own history records a real incident of this class — RELAY-20260703-014, where a council agent wrote a fabricated "Queen Keyport Second Ruling" directly into canonical ADR-0001 and cited a circularly self-referencing handoff as evidence. The primary adversary is not a root-level attacker; it is a capable-but-drifting agent on this host writing false governance state into canonical files with full confidence. Protection sought: tamper-EVIDENCE strong enough that the nightly `--audit-all` catches fabricated or tampered clearance state within a day.

**Desired outcome:** the gate can distinguish (a) clearance artifacts produced through the pipeline in the correct order from (b) hand-edited or fabricated frontmatter, and (c) detect post-clearance modification of the clearance conditions text. Candidate mechanisms named by Queen Keyport in task #2's residual: signing, condition-satisfaction checks cross-referenced against the note body, ordering checks — HEPHAISTOS designs; this intake does not prescribe.

**Honesty constraint (binding on all artifacts):** every role in this pipeline runs on the same host as the same user. Whatever mechanism is chosen MUST document its actual guarantee boundary explicitly — what it detects (careless/fabricated/tampered state from agents that don't go hunting for the mechanism's key material) versus what it cannot prevent (a deliberate same-substrate adversary with full host access regenerating any artifact). Overclaiming cryptographic identity isolation that does not exist would itself be an F4-class narrative failure.

**Grandfathering:** tasks #1 and #2 predate the mechanism. Whatever is built must handle them honestly (explicitly-labeled retro-stamps or an explicit grandfather rule in the verifier) — silent backfill that fakes contemporaneous stamps is prohibited (the ledger's off-protocol-backfill admission is the cautionary precedent).

## Scope packet (HEPHAISTOS)

### Design chosen

**HMAC-SHA256 stamps over per-section content hashes, chained by embedding the prior
stage's stamp value in the next stage's HMAC input, keyed by a secret held outside the
vault's git tree.** Three stages, one stamp each: `hephaistos_stamp` (binds
`hephaistos_scope: defined` to the exact text of `## Scope packet (HEPHAISTOS)`),
`qk_stamp` (binds `qk_verdict` to the exact text of `## Clearance (Queen Keyport)`,
chained to `hephaistos_stamp`), `relay_stamp` (binds `relay_id` to the exact text of
`## Execution record (Hermes-routed)`, chained to `qk_stamp`).

**Why this design and not the alternatives named in the intake:**
- **Git-history cross-checks alone** would show *that* the frontmatter changed and
  *when*, but not whether the change was a legitimate stage transition or a hand-edit
  of the same three lines Argus F2 already showed pass trivially — git diff cannot
  distinguish "HEPHAISTOS wrote this" from "someone typed `hephaistos_scope: defined`."
  Folded in anyway as a **secondary, non-cryptographic layer**: the ledger cross-reference
  check below is exactly this kind of check, cheap and worth keeping alongside signing,
  not instead of it.
- **Signing wins over ordering-only checks** because F2's actual named gap is a
  hand-editable string with no authentication at all; an order-only check (e.g. "field A
  timestamp before field B timestamp") is itself hand-editable the same way. Signing is
  the only candidate that makes the individual field values themselves resistant to a
  drifting agent that doesn't go looking for key material.
- **Content-hash binding (not just field-value signing)** is required because F2 names a
  second, distinct gap: post-clearance edits to the conditions text. Signing only
  `qk_verdict: cleared` (the string) would not catch someone leaving that string alone
  while rewording condition 3 afterward. Hashing the entire `## Clearance (Queen
  Keyport)` section into the HMAC input closes that gap directly — any byte change to
  that section after stamping invalidates the stamp.
- **Chaining (not three independent stamps)** is required because independent stamps
  would each individually verify even if qk_stamp was produced before hephaistos_stamp
  ever existed (e.g. a session fast-tracks "clearance" text into the note, stamps it,
  and only writes the scope section afterward to backfill a plausible-looking history).
  Embedding the prior stamp's actual value inside the next stamp's HMAC input makes that
  reordering detectable: a valid qk_stamp can only exist if it was computed after a
  specific hephaistos_stamp value existed to embed.

### Threat model fit (what this buys, stated against the grounded incident)

RELAY-20260703-014: Kimi wrote a fabricated "Queen Keyport Second Ruling" directly into
canonical ADR-0001 prose, with no corresponding stamp of any kind, and cited a circularly
self-referencing handoff as evidence. Under this mechanism, any governed-task note whose
`qk_verdict` (or the equivalent state-advancing claim) lacks a valid, chain-consistent
`qk_stamp` is flagged by `--audit-all` the same night — mechanically, not by a human or
Argus happening to re-read the file and notice the contradiction, which is what actually
had to happen in the real incident. That is the concrete improvement this design targets:
turning "someone eventually notices" into "the nightly job notices."

### Key: location, generation, permissions

- Path: `/home/martin/.agents/hephaistos/keys/gate-hmac.key` — outside
  `/home/martin/EMERAULD` (the vault's git tree) entirely, and outside the vault's normal
  MCP/tool read surface (the obsidian-second-brain MCP server, and any session whose job
  is to read/write vault *notes*, has no operational reason to open this path).
- **`/home/martin/.agents/hephaistos` is itself a git repo pushed to
  `github.com/martinlepage26-bit/hephaistos`** (confirmed via `git remote -v`) — the key
  must never be committed there either. Add `keys/` to
  `/home/martin/.agents/hephaistos/.gitignore` (currently contains only
  `.claude/settings.local.json`) as the literal first line of implementation, before the
  key file is created.
- Generation (stdlib only, no new dependency): 32 random bytes, base64-encoded, written
  with `os.open(..., os.O_CREAT | os.O_EXCL, 0o600)` (create-exclusive, not
  write-then-chmod, to avoid the umask-0002-window `governance/tasks/argus-remediations-20260708.md`
  Item 2 condition 7 already had to correct for on this exact host) so the file is never
  briefly group/world-readable. `keys/` directory itself: mode 700.
- Single global key, not per-task. Rotation is a manual future operation (generate new
  key, re-stamp live tasks, retire old key); not built now — no rotation need exists yet
  and building it speculatively would violate "keep it buildable in one session."
- `stamp_key_id` (first 8 hex chars of `sha256(key_bytes)`) is written alongside every
  stamp so a future rotation is legible in the note itself (`stamp_key_id: 4f9a2b1c`) —
  distinguishes "never stamped" from "stamped with a since-rotated key" during a
  verification failure, rather than reporting both as the same generic `STAMP_INVALID`.

### What gets stamped, at each transition, by what command

New CLI: `scripts/gate_stamp.py` (vault repo, alongside `governance_gate.py`).

```
python3 scripts/gate_stamp.py stamp <task-note> hephaistos_scope defined
python3 scripts/gate_stamp.py stamp <task-note> qk_verdict cleared
python3 scripts/gate_stamp.py stamp <task-note> relay_id RELAY-20260708-00X
python3 scripts/gate_stamp.py verify <task-note>
```

`stamp <note> <field> <value>` behavior:
1. Loads the key (path overridable via `GATE_HMAC_KEY_PATH` for test fixtures); refuses
   with a clear error if the key file is missing or not mode `0600`.
2. For `qk_verdict` and `relay_id`: refuses to proceed unless the corresponding prior
   stamp (`hephaistos_stamp` for qk; `qk_stamp` for relay) is already present *and*
   independently re-verifies against current content — this is the CLI-side half of
   ordering enforcement (the verifier below is the other half, for stamps written by
   hand or by a modified tool).
3. Computes the section hash for the field's bound section (`## Scope packet
   (HEPHAISTOS)` for `hephaistos_scope`; `## Clearance (Queen Keyport)` for
   `qk_verdict`; `## Execution record (Hermes-routed)` for `relay_id`) — see algorithm
   below.
4. Computes `HMAC-SHA256(key, payload)`, hex digest.
5. Writes `{field}_stamp`, `{field}_stamped_at` (ISO-8601 UTC), and `stamp_key_id` into
   frontmatter via the **targeted line-upsert** described below (never
   `yaml.safe_dump`).

`verify <note>` recomputes every present stamp from current content, checks chain
linkage, honors `stamp_status: grandfathered`, prints one line per field, exits 0 only
if every required stamp is valid and chain-consistent (or the note is grandfathered).

### Canonical payload and section-hash algorithm (must match exactly between `stamp` and `verify`)

Section extraction: given heading string `H` (e.g. `## Scope packet (HEPHAISTOS)`),
take everything from the line after `H` up to (excluding) the next line starting with
`## ` or end-of-file; strip trailing whitespace; normalize line endings to `\n`;
`sha256(...).hexdigest()`.

Payload: `f"{task_id}|{field_name}|{field_value}|{section_sha256_hex}|{prev_or_GENESIS}|{stamped_at_iso8601}"`
— `task_id` = note filename stem; `prev_or_GENESIS` = literal `GENESIS` for
`hephaistos_stamp`, else the current value of the immediately-prior stamp field at
stamping time. Stamp value = `hmac.new(key, payload.encode(), hashlib.sha256).hexdigest()`.

### Frontmatter write discipline — the trap to avoid

`governance_gate.py`'s existing `load_meta()` parses frontmatter with `yaml.safe_load`
but never writes it back. `gate_stamp.py` must **not** round-trip through
`yaml.safe_dump` to add a key — `safe_dump` can reorder keys, change quote style, or
reformat a value, producing a large unwanted diff on a governance-tracked file (and
ironically undermining the "detect tampering" goal with a tool that itself mutates
untouched fields). Use a targeted line-level upsert instead: locate the frontmatter
block exactly as `load_meta` does (`text[4:text.find("\n---", 4)]`), scan its lines for
an existing `^{key}:\s*.*$` match and replace only that line in place, or append the new
`key: value` line just before the closing `---` if absent. Every other line, including
key order and quoting elsewhere in the block, is untouched.

### Verification integration: `check_note` / `audit_all`, new violation classes

`governance_gate.py` gains `from gate_stamp import verify_stamps, check_ledger_xref`
(same-directory sibling import, matching the existing `sys.path.insert(0,
str(Path(__file__).parent))` pattern already used by `scripts/embed.py`). Both
`check_note()` and `audit_all()` call `verify_stamps(path, meta, text)` and append its
returned violation strings to the existing violation handling — **the existing
three-string PASS/WARN logic (`state in {...} and scope=="defined" and
verdict=="cleared"`) is unmodified**; stamp checks are strictly additive so a note can
pass the old check and fail the new one (surfaced, not silently absorbed).

New violation classes (each only checked when the corresponding field has actually
reached a stampable value — mirrors the existing pre-clearance exemption, so a task
still at `intake`/`scoped` is not flagged for a stamp it isn't due to have yet):
- `STAMP_MISSING` — field has a stampable value (`hephaistos_scope: defined`,
  `qk_verdict` set, or `relay_id` set) but its `*_stamp` key is absent.
- `STAMP_INVALID` — stamp present but recomputation (current content + key) doesn't
  match — covers both hand-edited-field forgery and post-clearance section-text edits
  (the section hash is inside the HMAC input, so either failure mode fails the same
  check; the printed message distinguishes them by separately recomputing the section
  hash first and reporting "conditions text changed since stamping" when only that
  component differs).
- `STAMP_ORDER_VIOLATION` — a later stamp's embedded `prev` value doesn't match the
  actual current value of the earlier stamp it should have chained to.
- `LEDGER_XREF_MISSING` — `relay_id` is set but no `relay_id: <value>` line exists
  anywhere in `/home/martin/.agents/hephaistos/ledgers/RELAY-LEDGER.md` (plain grep,
  needs no key — this is the "ledger cross-reference" candidate from the intake,
  cheap and independent of the signing mechanism, so it still runs even on grandfathered
  notes).

Printed line grows one segment, e.g.:
`GATE PASS: gate-authenticity-20260708.md | governance_state=routed hephaistos_scope=defined qk_verdict=cleared relay_id=RELAY-20260708-005 | STAMPS: valid (3/3, chain ok)`
or
`GATE WARN (soft gate): <name> | ... | STAMPS: INVALID (qk_stamp: conditions text changed since stamping)`

**Rollout enforcement level (avoiding a second F1):** stamp violations count toward
`audit_all`'s violation total and appear in every printed line (visible immediately),
but do **not** change `--hard`'s exit-1 boolean in this rollout — `--hard` continues to
gate on the pre-existing three-string check only. This mirrors the precedent already
set in `governance/tasks/README.md` rule 1 (soft-then-hard tightening) and is a Queen
Keyport decision to make later, not something this packet presumes.

### Grandfathering tasks #1 and #2

Both predate the mechanism. Per the intake's binding honesty constraint, no retro-stamp
is written — a stamp computed today over content authored days ago would be
byte-indistinguishable in the file from a genuine same-day stamp, which is exactly the
kind of "off-protocol backfill" the RELAY-LEDGER's own admitted precedent warns against.

Instead: add one new frontmatter key, `stamp_status: grandfathered`, to
`governance/tasks/weekly-os-health-20260708.md` and
`governance/tasks/argus-remediations-20260708.md` (bump `updated:` to the actual edit
date, per the standing no-backfill rule — not left at `2026-07-08` if this executes
later). `verify_stamps()` checks this flag first: if set, it skips
`STAMP_MISSING`/`STAMP_INVALID`/`STAMP_ORDER_VIOLATION` entirely and reports `STAMPS:
grandfathered (pre-mechanism, <date>)` — visibly labeled, not silently passed, and not a
counted violation. `LEDGER_XREF_MISSING` still runs on grandfathered notes (it needs no
stamp and both notes' real `relay_id` values are already confirmed present in
RELAY-LEDGER.md by direct grep during this scoping pass), so grandfathering narrows
exactly to the checks the old notes structurally cannot satisfy, nothing broader.

### Rollout order (must land as one ordered execution burst — this is what prevents lock-out)

1. Add `keys/` to `~/.agents/hephaistos/.gitignore`; generate the key at
   `~/.agents/hephaistos/keys/gate-hmac.key` (0600); build and standalone-test
   `scripts/gate_stamp.py` (stamp + verify) against scratch fixture notes — **before**
   `governance_gate.py` changes at all.
2. Add `stamp_status: grandfathered` to task #1 and task #2 (bump their `updated:`).
   Must land before step 3, or the very first `--audit-all` run after step 3 flags both
   as `STAMP_MISSING`.
3. Wire `verify_stamps`/`check_ledger_xref` into `governance_gate.py`'s `check_note()`
   and `audit_all()`, additive-only per the enforcement-level note above.
4. Stamp this task's own `## Scope packet (HEPHAISTOS)` section now, using the real
   tool — the first live, contemporaneous use of the mechanism, on the task that
   commissioned it.
5. When Queen Keyport clears this task, she stamps her own `## Clearance` section the
   same way; the CLI will refuse if step 4's `hephaistos_stamp` doesn't itself
   re-verify — proving the ordering guarantee end-to-end, live, on this task.

Steps 1-4 land together so no `--audit-all` run ever observes `verify_stamps()` logic
active against this task's own scope-defined-but-unstamped state.

**Note on this packet's own stamp:** this section does not carry a `hephaistos_stamp`
field right now, because `scripts/gate_stamp.py` does not exist yet at the moment this
packet is written — HEPHAISTOS's lane is scope design, not execution. Hand-writing a
placeholder or fabricated stamp value here would itself be the exact failure class this
task exists to prevent. The real stamp is applied at rollout Step 4, by Hermes, using
the real key and the real tool, immediately after Step 1 lands.

### What this mechanism explicitly does NOT guarantee (same-substrate honesty section, binding per intake)

- **Does not prove dispatch isolation.** It cannot distinguish "HEPHAISTOS and Queen
  Keyport were genuinely separate Agent-tool dispatches with independent context" from
  "one session, holding the same key material any `martin`-owned process on this host
  can read, wrote both sections in sequence and ran the stamp CLI twice while narrating
  both personas." Both produce an identical, fully valid, chain-consistent stamp
  sequence. **This is Argus F2's core residual and it is not closable by any
  same-substrate signing scheme** — it would require a genuinely separate credential,
  process boundary, or human-witnessed action per role, none of which exist on this
  host today. Stated plainly so no future reading of "F2 closed" overclaims this.
- **Does not defend against a deliberate, key-hunting same-substrate adversary.** Any
  process running as `martin` can in principle read
  `~/.agents/hephaistos/keys/gate-hmac.key` and forge a fully valid, internally
  consistent chain, including a fabricated ordering. The key's location and mode 600
  raise the bar against a *careless or non-hunting* drifting agent — one that edits
  frontmatter directly the way the actual ADR-0001 incident happened, without first
  going and discovering a signing key it had no reason to suspect existed — not against
  someone who reads this scope packet (itself vault-readable) and therefore knows
  exactly where the key lives and what payload format to sign.
- **Does not verify that Queen Keyport's numbered conditions were actually satisfied in
  reality** — e.g., that a claimed empirical test was genuinely run. It proves only that
  the conditions *text* has not silently changed since it was stamped: tamper-evidence
  over the note's own content, not truth-verification of claims made in that content.
- **Does not detect "executed work with no task note at all"** (`governance/tasks/README.md`
  rule 4's other named drift case) — that needs cross-referencing the full RELAY-LEDGER
  against all executed work, a materially larger undertaking than one relay_id
  cross-reference, and out of scope here exactly as it was out of scope for task #2 item 1.
- **Does not protect the key file itself** from host compromise, a misconfigured backup
  that copies `~/.agents/` somewhere more permissive, or a future MCP server
  misconfiguration that broadens its filesystem read scope to include
  `~/.agents/hephaistos/keys/`.
- **What it does provide, stated positively:** tamper-*evidence* (not tamper-*proof*)
  against the specific, grounded threat class named in the intake — a drifting-but-not-
  key-hunting agent that hand-edits governance frontmatter or narrates a fabricated
  ruling directly into canonical files with full confidence, the way RELAY-20260703-014
  actually happened, surfaced mechanically within a day via the nightly
  `--audit-all` pass already wired in by task #2, with zero new cron/systemd surface.

### Acceptance criteria (mechanical)

1. **Hand-edited-frontmatter forgery detected:** on a stamped, cleared note, hand-edit
   `qk_verdict` (or `hephaistos_scope`) directly, leaving `*_stamp` untouched. Both
   `python3 scripts/gate_stamp.py verify <note>` and
   `python3 scripts/governance_gate.py <note> --hard` (via `--audit-all`'s violation
   count) report `STAMP_INVALID`; `gate_stamp.py verify` exits 1.
2. **Post-clearance conditions-text edit detected:** on a stamped, cleared note, edit
   one word inside `## Clearance (Queen Keyport)` without re-stamping. `verify` reports
   `STAMP_INVALID (qk_stamp: conditions text changed since stamping)`; exits 1.
3. **Out-of-order stamp sequence detected:** construct a fixture where `qk_stamp`'s
   embedded `prev` does not match the note's actual current `hephaistos_stamp` (e.g.
   `hephaistos_scope` was legitimately re-stamped after `qk_stamp` already existed,
   changing the value `qk_stamp` should have chained to). `verify` reports
   `STAMP_ORDER_VIOLATION`; exits 1.
4. **Both grandfathered tasks audit clean:** after adding `stamp_status: grandfathered`
   to task #1 and #2, `python3 scripts/governance_gate.py --audit-all` exits 0, 0
   violations, both lines show `STAMPS: grandfathered`.
5. **Happy path (this task itself):** once this task is fully stamped through Steps 4-5
   and reaches `relay_stamp` at dispatch, `--audit-all` shows `STAMPS: valid (3/3, chain
   ok)` for `gate-authenticity-20260708.md` — proving the real pipeline, not only the
   adversarial fixtures, produces a clean result.
6. `python3 scripts/gate_stamp.py verify <note>` is independently runnable and exits
   0/1 correctly for all five cases above without depending on `governance_gate.py`.
7. `git diff` on `scripts/scheduled/nightly.sh` is empty — `--audit-all` is already
   wired in from task #2; this task changes only `governance_gate.py`,
   `gate_stamp.py` (new), the two grandfather frontmatter edits, this note's own
   stamps, and (documentation only) `governance/tasks/README.md`'s state-machine table
   gaining rows for the new frontmatter keys plus a one-line pointer to this honesty
   section.

### Artifact list / scope boundary

**New:** `~/.agents/hephaistos/keys/gate-hmac.key` (0600); `keys/` added to
`~/.agents/hephaistos/.gitignore`; `scripts/gate_stamp.py`.
**Modified:** `scripts/governance_gate.py` (additive `verify_stamps`/
`check_ledger_xref` calls only); `governance/tasks/weekly-os-health-20260708.md` and
`governance/tasks/argus-remediations-20260708.md` (one frontmatter key + `updated:`
bump each); this note (real stamps at Steps 4-5); `governance/tasks/README.md`
(state-machine table + honesty-section pointer).
**Explicitly untouched:** the MCP server and `vault_ops.py`; `scripts/scheduled/nightly.sh`
(already wired from task #2 — zero changes needed); `scripts/scheduled/weekly.sh`; any
cron/systemd surface; no new daemon.

## Clearance (Queen Keyport)

**Verdict: CLEARED (approve-with-constraints), 9 binding conditions.** The design
(HMAC-SHA256 stamps, chained, over per-section content hashes) is not refused. Two
gaps were found by direct execution of code on this host, not by reading the packet's
prose — both are fixable without changing the chosen design, and are bound below.

**Governance domain:** internal governance tooling (a new script, a key file, and
additive changes to an existing gate script). No external-facing surface, no client
data, no regulatory exposure. Consequence domain is auditability/integrity of the
governance pipeline's own tamper-evidence, plus one adjacent risk this review
surfaced: silent interaction with an already-existing, uncoordinated vault tool.
Delta-first review applies; the escalation triggers in `QUEEN-KEYPORT_OPERATIONS.md`
(client-facing, regulatory, safety, "full/exhaustive" framing) are not met.

**Evidence threshold applied — verified by direct execution, not accepted from the
packet's prose:**
- `os.open(path, os.O_CREAT | os.O_EXCL, 0o600)` under this host's actual umask
  (`0002`, confirmed via `umask`) produces file mode `0600` exactly, and
  `os.mkdir(path, 0o700)` produces dir mode `0700` exactly — both empirically
  confirmed in an isolated Python process. The packet's claim about avoiding the
  umask-0002 window holds for the create-exclusive idiom; **it does not, by itself,
  protect any value written into frontmatter later by a different code path** (see
  condition 1).
- `scripts/enrich_frontmatter_backlinks.py` (an existing, already-built, currently
  **dormant** vault-wide tool — confirmed via `grep -rn "enrich_frontmatter_backlinks"
  scripts/scheduled/ crontab`, zero hits, so no scheduled job calls it today) rewrites
  the *entire* frontmatter block of every editable Markdown file via `yaml.safe_dump`,
  and its exclusion set (`PROTECTED_DIRS = {"raw sources", "raw"}`) does **not**
  exclude `governance/` or `governance/tasks/` — confirmed directly against this
  task note's own path parts. This task's own body/section text is untouched by that
  tool (it only rewrites frontmatter for non-index files; body is passed through
  `body.lstrip()` unchanged) — so the **section-hash mechanism itself survives**
  enrichment. Confirmed by direct code read of the write loop in `main()`.
- **The load-bearing failure found:** PyYAML's `safe_load`/`safe_dump` auto-types an
  unquoted ISO-8601-looking scalar (`2026-07-08T16:40:47Z`) as `datetime.datetime` on
  load, and `enrich_frontmatter_backlinks.py`'s own `normalize_yaml_value()` converts
  it back to a string via `.isoformat()` on dump — which renders as
  `'2026-07-08T16:40:47+00:00'`, byte-different from the original. Reproduced live in
  an isolated Python process: round-tripping an unquoted `*_stamped_at` value through
  this exact normalize+dump pipeline changes the string that is embedded in the HMAC
  payload, which would silently invalidate every non-grandfathered stamp on this vault
  the next time this dormant tool is ever run (manually or, per this vault's own
  history — `governance_gate.py --audit-all` itself went from standalone script to
  wired-in cron job within one day — once it too gets wired into a scheduled pass).
  Also confirmed: **quoting the value at write time closes this** — a frontmatter line
  written as `hephaistos_stamped_at: "2026-07-08T16:40:47Z"` round-trips byte-for-byte
  as a string through the same normalize+dump pipeline (verified live). This is a real,
  previously undetected collision between two independently-evolved vault mechanisms —
  exactly the kind of cross-system leverage a structural read is supposed to surface,
  not something HEPHAISTOS could have found without executing the enrichment tool's
  actual code, which is why it wasn't in the scope packet.

**Right-arm synthesis (Philosopher / Power-Analyst):** no divergence; both concur
clearance is appropriate with conditions. Philosopher's finding: the packet is
unusually honest about its own limits (same-substrate, no dispatch-isolation proof,
explicit "does NOT guarantee" section) — the one place language should tighten is
rollout Step 5 ("Queen Keyport stamps her own Clearance section the same way"), which
reads as if a governance verdict includes personally executing a CLI tool. That
collapses governance and execution scope exactly as the architecture prohibits
("do not collapse all three roles into one undifferentiated assistant pass" —
`CLAUDE.md`, `.agents/hephaistos/`). Bound below (condition 7): the physical stamp
of this Clearance section is an execution act performed by Hermes (or whoever
executes the rollout), after this verdict is written, using the real tool — not
something Queen Keyport does as part of issuing the verdict, since `gate_stamp.py`
does not exist at the time this verdict is written. Power-Analyst's finding: the
real structural leverage point is the shared key/shared host/shared user assumption,
which the packet already names correctly and does not overclaim past. The *additional*
structural risk this review found (the enrichment-tool collision) is the same family
of risk — an unexamined dependency between two subsystems built at different times by
different sessions — just surfaced empirically rather than by inspection.

**Diamond-Eyes:** wise and caring, not merely defensible. The design is proportionate
to the grounded incident (RELAY-20260703-014) it targets, does not add speculative
complexity (no premature key rotation, no new daemon), and the conditions below close
real, testable gaps rather than adding governance theater. Escalation not required.

### Binding conditions (executor must satisfy before this task moves to `done`)

1. **All `*_stamped_at` values must be written as explicitly quoted YAML strings**
   (e.g. `hephaistos_stamped_at: "2026-07-08T16:40:47Z"`, not a bare unquoted scalar).
   This is not cosmetic: an unquoted ISO-8601 value is auto-typed to
   `datetime.datetime` by `yaml.safe_load` and re-serializes to a different string
   (`+00:00` instead of `Z`) through any tool that round-trips frontmatter via
   `yaml.safe_dump` — verified empirically against `enrich_frontmatter_backlinks.py`'s
   actual `normalize_yaml_value()` + `safe_dump` pipeline. `gate_stamp.py`'s own
   targeted line-upsert must write the quoted form on first creation, not just avoid
   full-document round-tripping.
2. **`gate_stamp.py verify()` must reconstruct the payload from the raw quoted string
   value, not from whatever Python type `yaml.safe_load` happens to return.** If
   `verify()` calls the same `load_meta()`-style YAML parse used elsewhere and reads
   `meta.get("hephaistos_stamped_at")` directly, condition 1's quoting is necessary
   but verify must still treat the field as `str` throughout — do not let any
   intermediate code path re-normalize it through `datetime`. Add an explicit unit
   test: stamp a fixture note, then run `verify` in a fresh process, confirming PASS.
3. **Exclude `governance/` (or at minimum `governance/tasks/`) from
   `scripts/enrich_frontmatter_backlinks.py`'s `PROTECTED_DIRS`,** in addition to
   condition 1's quoting fix — defense in depth, since condition 1 protects the
   specific field this task introduces, but the enrichment tool rewrites the *entire*
   frontmatter block of governed-task notes for no operational reason (governed-task
   notes are not the kind of note that tool exists to enrich) and any future field
   added to this pipeline inherits the same risk class if not independently quoted.
   Acceptance check: `python3 scripts/enrich_frontmatter_backlinks.py --dry-run`
   reports zero planned changes for any file under `governance/tasks/`.
4. **Add a regression test to the acceptance criteria:** stamp a fixture note fully
   (all 3 fields), run `scripts/enrich_frontmatter_backlinks.py` (or a scoped
   reproduction of its normalize+dump pipeline if a full vault-wide dry run is
   impractical to sandbox) against a copy of it, then run
   `python3 scripts/gate_stamp.py verify <copy>` and confirm it still exits 0. This is
   acceptance criterion **8** (extends HEPHAISTOS's 7 mechanical criteria); do not
   mark this task `done` without it passing.
5. **Add a distinct violation class for an unavailable/unreadable key file,
   `KEY_UNAVAILABLE`, separate from `STAMP_INVALID`.** A missing, unreadable, or
   wrong-mode key file causes every non-grandfathered stampable note to fail
   verification simultaneously on the next `--audit-all` run — this fail-loud
   behavior is correct and desired (losing the key is itself a governance emergency,
   not a transient blip), but it must not be reported identically to a genuine
   per-note forgery. `STAMP_INVALID` should mean "this specific stamp does not
   recompute against a working key" and `KEY_UNAVAILABLE` should mean "no stamp on
   this host could be checked right now, for an infrastructure reason" — conflating
   them would misdirect whoever reads `FAILURES.md` toward hunting a forger when the
   actual fault is a broken key path. Acceptance check (criterion **9**): temporarily
   rename the key file, run `--audit-all`, confirm every stampable note reports
   `KEY_UNAVAILABLE` (not `STAMP_INVALID`), and confirm the printed summary makes it
   legible as one infrastructure fault, not N independent-looking forgeries.
6. **Rollout steps 1-5 (per HEPHAISTOS's own ordering) must execute as one
   uninterrupted session, not spanning a scheduled cron boundary.** HEPHAISTOS's own
   packet already names the specific lock-out this guards against (step 2 must land
   before step 3, or the first `--audit-all` after step 3 flags both grandfathered
   tasks; steps 1-4 must land together or this task's own unstamped
   `hephaistos_scope: defined` gets flagged the same way). This review adds the
   concrete trigger: `nightly.sh` fires unconditionally at 22:00 daily regardless of
   whether this rollout is mid-execution. If step 3 (wiring `verify_stamps` into
   `governance_gate.py`) has landed but step 2 (grandfather flags) or step 4 (this
   task's own stamp) has not, and 22:00 arrives before the session resumes, that
   night's `--audit-all` will produce real (not hypothetical) `FAILURES.md` noise for
   reasons unrelated to any actual tampering. If the rollout cannot complete in one
   sitting, land steps in an order where the gate wiring (step 3) is never the last
   thing committed before a pause.
7. **Step 5's "Queen Keyport stamps her own Clearance section" is an execution act,
   performed by Hermes (or the executing agent) after this verdict is written, using
   the real tool** — not something Queen Keyport does as part of issuing this
   governance decision. `scripts/gate_stamp.py` does not exist at the time this
   clearance is written (per HEPHAISTOS's own note under "this packet's own stamp").
   The CLI's own ordering enforcement (refusing `qk_verdict` stamping unless
   `hephaistos_stamp` already re-verifies) is what proves the ordering guarantee —
   Queen Keyport's role here is the verdict text above; the stamp is applied
   afterward, mechanically, by the tool.
8. **`keys/` directory mode `0700` and key file mode `0600` must be confirmed by
   `stat` immediately after creation, not assumed from the `os.open`/`os.mkdir` call
   succeeding.** Both were verified reproducible on this host's actual umask (`0002`)
   in this review's own test, but the build step should still assert this
   mechanically (e.g. `stat -c %a` check in the same script or a one-line
   post-creation assertion) rather than rely on this review's isolated test as a
   permanent guarantee across host/umask changes.
9. **The honesty section's scope is correct and must not be narrowed during
   implementation.** No change requested to the packet's "What this mechanism
   explicitly does NOT guarantee" section — it is accurate, appropriately bounded,
   and must ship unedited. Any future narrative describing this task's completion
   must preserve it verbatim in substance (dispatch isolation is not provable by this
   mechanism; a key-hunting same-substrate adversary is not defended against).

**Gaps declared (not blockers, named per Argus's L99 audit criterion):** this review
verified the YAML-coercion and umask claims by direct execution; it did not build or
execute `scripts/gate_stamp.py` itself (it does not exist yet — that is Hermes's
execution step). Whether the MCP server's filesystem access is structurally incapable
of reading `~/.agents/hephaistos/keys/gate-hmac.key` was not independently re-verified
in this pass; it relies on the 2026-07-08 Argus audit's existing characterization of
MCP scope as vault-rooted. If that characterization is ever wrong, the key's location
does not protect it from that surface.

**Standing check:** before this task is marked `done`, `git diff` must show only the
artifacts named in HEPHAISTOS's scope packet's "Artifact list" plus this note's own
stamps — any diff outside that boundary is a completeness failure, not a stylistic nit.

## Execution record (Hermes-routed)

**Dispatched 2026-07-08, ledger `RELAY-20260708-005` at true dispatch time. Hard gate PASS before execution. Rollout steps 1-5 executed in one uninterrupted sitting with ~4h margin before the 22:00 nightly (QK condition 6).**

- **Step 1:** `keys/` gitignored in ~/.agents/hephaistos (before key creation); key generated create-exclusive; dir 0700 + file 0600 stat-asserted, not assumed (QK condition 8); key invisible to the hephaistos repo's git. `scripts/gate_stamp.py` built and standalone-tested against scratch fixtures with a scratch key before any gate change.
- **Step 2:** `stamp_status: grandfathered` upserted on tasks #1 and #2 — no retro-stamps (intake constraint).
- **Step 3:** `governance_gate.py` wired additively — check_note and audit_all gain a STAMPS segment; stamp violations count in audit-all but never alter --hard's boolean (rollout enforcement level per scope); KEY_UNAVAILABLE reported as one legible infrastructure fault, never as N forgeries (QK condition 5). `enrich_frontmatter_backlinks.py` excludes `governance/tasks/` (QK condition 3; dry-run plans zero changes there — the tool's stats line counting inbound links to excluded task notes as unresolved is cosmetic and accepted).
- **Steps 4-5:** scope and clearance sections stamped on this note with the real key, in chain order, by the executing session as an execution act (QK condition 7); the CLI verified the scope stamp before permitting the clearance stamp — the ordering guarantee exercised live. The relay stamp below binds this execution record's final text.

**Acceptance criteria — all verified 2026-07-08:**
1. Hand-edited `qk_verdict` → STAMP_INVALID, exit 1. ✓
2. One-word edit inside a stamped Clearance section → `STAMP_INVALID (section text changed since stamping)`, exit 1. ✓
3. Re-stamped scope after qk stamped (chain break) → violation, exit 1. ✓ (Bonus finding: the stamp binds task_id, so a stamped note copied under a different filename also fails — accidental but useful anti-cloning property.)
4. Both grandfathered tasks audit clean with visible `STAMPS: grandfathered` labels. ✓ (final audit-all run below)
5. This task 3/3 chain-ok after relay stamp. ✓ (final audit-all run below)
6. `gate_stamp.py verify` independently runnable, correct exits for all cases. ✓
7. `git diff scripts/scheduled/nightly.sh` empty — zero cron changes. ✓
8. Enrichment normalize+safe_dump round-trip on a fully-stamped fixture → still valid 3/3 (QK conditions 1+2+4: quoted stamped_at written at creation, verify reads raw strings, never yaml-typed). ✓
9. Renamed key file → every stampable note reports KEY_UNAVAILABLE, distinct from STAMP_INVALID, summarized as one infrastructure fault. ✓

**Honesty boundary, preserved verbatim in substance per QK condition 9:** this mechanism provides tamper-EVIDENCE against the grounded threat (a drifting, non-key-hunting agent hand-editing governance state — the RELAY-20260703-014 class), surfaced nightly. It does NOT prove dispatch isolation and does NOT defend against a deliberate same-substrate key-hunting adversary. Argus F2 is closed to the extent closable on one host as one user; the dispatch-isolation residual remains structurally open.
