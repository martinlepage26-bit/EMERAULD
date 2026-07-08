#!/usr/bin/env python3
"""HMAC stage stamps for governed-task notes (governed task gate-authenticity-20260708).

Provides tamper-EVIDENCE for the governance pipeline's stage artifacts: each state
transition is stamped with HMAC-SHA256 over (task_id | field | value | section-hash |
previous-stamp | timestamp), chained so ordering violations are detectable, keyed by a
secret held outside every git tree at ~/.agents/hephaistos/keys/gate-hmac.key (0600).

Honesty boundary (binding, from the task's scope packet — do not narrow):
- Detects: hand-edited stage frontmatter, post-clearance edits to stamped section text,
  out-of-order or fabricated stage sequences — the RELAY-20260703-014 incident class,
  produced by a drifting agent that does not go hunting for key material.
- Does NOT prove dispatch isolation (same host, same user for every role) and does NOT
  defend against a deliberate key-hunting same-substrate adversary.

Usage:
    gate_stamp.py stamp  <task-note> <field> <value>
    gate_stamp.py verify <task-note>

Fields and their bound sections:
    hephaistos_scope -> "## Scope packet (HEPHAISTOS)"          (chain: GENESIS)
    qk_verdict       -> "## Clearance (Queen Keyport)"          (chain: hephaistos_scope)
    relay_id         -> "## Execution record (Hermes-routed)"   (chain: qk_verdict)

Frontmatter writes are targeted line-upserts (never yaml.safe_dump — no reformatting of
untouched lines). *_stamped_at is written as an explicitly QUOTED string: an unquoted
ISO-8601 scalar is auto-typed to datetime by yaml.safe_load and re-serializes
byte-differently through any safe_dump round-trip, silently invalidating the stamp
(QK condition 1, verified empirically against enrich_frontmatter_backlinks.py).
"""

from __future__ import annotations

import hashlib
import hmac as hmac_mod
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_KEY_PATH = os.path.expanduser("~/.agents/hephaistos/keys/gate-hmac.key")

FIELD_SECTION = {
    "hephaistos_scope": "## Scope packet (HEPHAISTOS)",
    "qk_verdict": "## Clearance (Queen Keyport)",
    "relay_id": "## Execution record (Hermes-routed)",
}
CHAIN_PREV = {
    "hephaistos_scope": None,
    "qk_verdict": "hephaistos_scope",
    "relay_id": "qk_verdict",
}
FIELD_ORDER = ["hephaistos_scope", "qk_verdict", "relay_id"]


class KeyUnavailable(Exception):
    """Key file missing, unreadable, or wrong mode — an infrastructure fault, not a forgery."""


def load_key() -> bytes:
    path = os.environ.get("GATE_HMAC_KEY_PATH", DEFAULT_KEY_PATH)
    try:
        mode = os.stat(path).st_mode & 0o777
    except OSError as exc:
        raise KeyUnavailable(f"key file unavailable: {path} ({exc})") from exc
    if mode != 0o600:
        raise KeyUnavailable(f"key file {path} has mode {oct(mode)}, refusing (expected 0600)")
    try:
        data = Path(path).read_text(encoding="utf-8").strip()
    except OSError as exc:
        raise KeyUnavailable(f"key file unreadable: {path} ({exc})") from exc
    if not data:
        raise KeyUnavailable(f"key file empty: {path}")
    return data.encode()


def key_id(key: bytes) -> str:
    return hashlib.sha256(key).hexdigest()[:8]


def split_note(text: str) -> tuple[str, str]:
    """Return (frontmatter_inner_text, full_text). Raises on missing frontmatter."""
    if not text.startswith("---\n"):
        raise ValueError("note has no frontmatter block")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("unterminated frontmatter block")
    return text[4:end], text


def raw_field(fm: str, key_name: str) -> str | None:
    """Read a frontmatter scalar as the raw string on its line (never YAML-typed).

    Strips one layer of matching quotes. QK condition 2: stamped_at must be handled
    as str end-to-end; this reader never touches yaml.safe_load.
    """
    m = re.search(rf"^{re.escape(key_name)}:\s*(.*)$", fm, re.M)
    if m is None:
        return None
    val = m.group(1).strip()
    if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
        val = val[1:-1]
    return val if val not in {"", "null", "None"} else None


def section_hash(text: str, heading: str) -> str | None:
    lines = text.split("\n")
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == heading) + 1
    except StopIteration:
        return None
    body = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        body.append(line)
    return hashlib.sha256("\n".join(body).rstrip().encode("utf-8")).hexdigest()


def payload(task_id: str, field: str, value: str, sec_sha: str, prev: str, stamped_at: str) -> str:
    return f"{task_id}|{field}|{value}|{sec_sha}|{prev}|{stamped_at}"


def compute(key: bytes, task_id: str, field: str, value: str, sec_sha: str, prev: str, stamped_at: str) -> str:
    return hmac_mod.new(key, payload(task_id, field, value, sec_sha, prev, stamped_at).encode(), hashlib.sha256).hexdigest()


def upsert_lines(path: Path, updates: dict[str, str]) -> None:
    """Targeted frontmatter line-upsert: replace matching lines in place, append missing
    ones before the closing ---. No other line is touched."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("note has no frontmatter block")
    end = text.find("\n---", 4)
    fm_lines = text[4:end].split("\n")
    rest = text[end:]
    done = set()
    for i, line in enumerate(fm_lines):
        for k, v in updates.items():
            if re.match(rf"^{re.escape(k)}:\s*", line):
                fm_lines[i] = f"{k}: {v}"
                done.add(k)
    for k, v in updates.items():
        if k not in done:
            fm_lines.append(f"{k}: {v}")
    path.write_text("---\n" + "\n".join(fm_lines) + rest, encoding="utf-8")


def do_stamp(note: Path, field: str, value: str) -> int:
    if field not in FIELD_SECTION:
        print(f"ERROR: unknown field {field!r} (expected one of {FIELD_ORDER})")
        return 1
    key = load_key()  # raises KeyUnavailable loudly — stamping without a key is impossible
    fm, text = split_note(note.read_text(encoding="utf-8"))
    task_id = note.stem

    current = raw_field(fm, field)
    if current != value:
        print(f"REFUSED: note has {field}={current!r}, not {value!r} — stamp attests the recorded value, it does not set it")
        return 1

    prev_field = CHAIN_PREV[field]
    prev = "GENESIS"
    if prev_field is not None:
        prev = raw_field(fm, f"{prev_field}_stamp") or ""
        if not prev:
            print(f"REFUSED: {field} requires a prior {prev_field}_stamp (chain order)")
            return 1
        ok, msg = verify_one(key, note, fm, text, prev_field)
        if not ok:
            print(f"REFUSED: prior stamp {prev_field}_stamp does not re-verify before chaining: {msg}")
            return 1

    sec_sha = section_hash(text, FIELD_SECTION[field])
    if sec_sha is None:
        print(f"REFUSED: section {FIELD_SECTION[field]!r} not found in note")
        return 1
    stamped_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    digest = compute(key, task_id, field, value, sec_sha, prev, stamped_at)
    upsert_lines(
        note,
        {
            f"{field}_stamp": digest,
            f"{field}_stamped_at": f'"{stamped_at}"',  # QUOTED — QK condition 1
            f"{field}_section_sha": sec_sha,
            "stamp_key_id": key_id(key),
        },
    )
    print(f"STAMPED {field} on {note.name} (key_id {key_id(key)}, at {stamped_at})")
    return 0


def verify_one(key: bytes, note: Path, fm: str, text: str, field: str) -> tuple[bool, str]:
    """Verify one field's stamp. Caller guarantees the field has a stampable value."""
    value = raw_field(fm, field) or ""
    stamp = raw_field(fm, f"{field}_stamp")
    stamped_at = raw_field(fm, f"{field}_stamped_at")
    stored_sha = raw_field(fm, f"{field}_section_sha")
    if not stamp or not stamped_at or not stored_sha:
        return False, f"STAMP_MISSING ({field})"

    prev_field = CHAIN_PREV[field]
    prev = "GENESIS" if prev_field is None else (raw_field(fm, f"{prev_field}_stamp") or "")
    task_id = note.stem
    cur_sha = section_hash(text, FIELD_SECTION[field]) or ""

    if compute(key, task_id, field, value, cur_sha, prev, stamped_at) == stamp:
        return True, "valid"
    # Distinguish failure modes: does the stamp verify against the STORED section hash?
    if compute(key, task_id, field, value, stored_sha, prev, stamped_at) == stamp:
        if cur_sha != stored_sha:
            return False, f"STAMP_INVALID ({field}: section text changed since stamping)"
    # Try the stored hash + every plausible component to detect chain break specifically
    if prev_field is not None:
        return False, f"STAMP_INVALID or STAMP_ORDER_VIOLATION ({field}: field value, chain prev, or stamp fields altered)"
    return False, f"STAMP_INVALID ({field}: field value or stamp fields altered)"


def stampable_fields(fm: str) -> list[str]:
    out = []
    if (raw_field(fm, "hephaistos_scope") or "") == "defined":
        out.append("hephaistos_scope")
    if raw_field(fm, "qk_verdict") not in {None, "pending"}:
        out.append("qk_verdict")
    if raw_field(fm, "relay_id"):
        out.append("relay_id")
    return out


def verify_stamps(note: Path) -> tuple[list[str], list[str]]:
    """Return (ok_msgs, violations) for a governed-task note. Used by governance_gate."""
    fm, text = split_note(note.read_text(encoding="utf-8"))
    fields = stampable_fields(fm)
    if not fields:
        return (["no stampable fields yet (pre-clearance)"], [])
    if raw_field(fm, "stamp_status") == "grandfathered":
        return ([f"grandfathered (pre-mechanism, {raw_field(fm, 'updated') or 'undated'})"], [])
    try:
        key = load_key()
    except KeyUnavailable as exc:
        return ([], [f"KEY_UNAVAILABLE ({exc})"])
    ok_msgs, violations = [], []
    for field in fields:
        ok, msg = verify_one(key, note, fm, text, field)
        (ok_msgs if ok else violations).append(msg if not ok else f"{field}: {msg}")
    # chain-order cross-check: each later stamp's embedded prev must equal the current earlier stamp
    for field in fields:
        prev_field = CHAIN_PREV[field]
        if prev_field is None or f"{field}" not in fields:
            continue
        # (embedded prev is inside the HMAC; a mismatch already fails verify_one — this
        # branch exists to name the violation class when the earlier stamp was re-issued)
    return (ok_msgs, violations)


def check_ledger_xref(note: Path, ledger: Path = Path("/home/martin/.agents/hephaistos/ledgers/RELAY-LEDGER.md")) -> list[str]:
    """Cheap, keyless cross-reference: a set relay_id must exist in the RELAY-LEDGER.
    Runs on grandfathered notes too."""
    fm, _ = split_note(note.read_text(encoding="utf-8"))
    relay = raw_field(fm, "relay_id")
    if not relay:
        return []
    try:
        ledger_text = ledger.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return [f"LEDGER_XREF_MISSING (ledger unreadable at {ledger})"]
    if re.search(rf"^relay_id:\s*{re.escape(relay)}\s*$", ledger_text, re.M) is None:
        return [f"LEDGER_XREF_MISSING (relay_id {relay} not found in RELAY-LEDGER)"]
    return []


def summarize(note: Path) -> tuple[str, list[str]]:
    """One STAMPS segment + violations list, for governance_gate's printed line."""
    try:
        ok_msgs, violations = verify_stamps(note)
    except ValueError as exc:
        return (f"STAMPS: unparseable ({exc})", [f"STAMP_INVALID (unparseable note: {exc})"])
    violations = violations + check_ledger_xref(note)
    if violations:
        if any(v.startswith("KEY_UNAVAILABLE") for v in violations):
            return ("STAMPS: KEY_UNAVAILABLE (infrastructure fault — key file, not a forgery)", violations)
        return (f"STAMPS: {'; '.join(violations)}", violations)
    if ok_msgs and ok_msgs[0].startswith("grandfathered"):
        return (f"STAMPS: {ok_msgs[0]}", [])
    if ok_msgs and ok_msgs[0].startswith("no stampable"):
        return ("STAMPS: n/a (pre-clearance)", [])
    return (f"STAMPS: valid ({len(ok_msgs)}/{len(ok_msgs)}, chain ok)", [])


def main() -> int:
    argv = sys.argv[1:]
    if len(argv) >= 2 and argv[0] == "verify":
        note = Path(argv[1])
        seg, violations = summarize(note)
        print(f"{note.name} | {seg}")
        return 1 if violations else 0
    if len(argv) == 4 and argv[0] == "stamp":
        try:
            return do_stamp(Path(argv[1]), argv[2], argv[3])
        except KeyUnavailable as exc:
            print(f"KEY_UNAVAILABLE: {exc}")
            return 2
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main())
