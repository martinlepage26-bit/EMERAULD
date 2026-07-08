#!/usr/bin/env python3
"""QK-Gate for governed tasks (OS build Stage 4).

Checks a governed task note in governance/tasks/ before execution:
    governance_gate.py <task-note-path-or-task-id> [--hard]

Soft mode (default): prints PASS/WARN and always exits 0 — the warning is the
enforcement during the pilot month. Hard mode (--hard): exits 1 unless
governance_state is `cleared` (or `routed` for a resumed execution).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
import gate_stamp  # HMAC stage-stamp verification (governed task gate-authenticity-20260708)

ROOT = Path(__file__).resolve().parents[1]
TASKS = ROOT / "governance" / "tasks"


def load_meta(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    try:
        meta = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError:
        return {}
    return meta if isinstance(meta, dict) else {}


def check_note(path: Path, hard: bool) -> bool:
    """Print one GATE line for a task note; return True if it passes.

    The pass/fail boolean (and --hard's exit) gates on the original three-field
    check only; stamp verification is ADDITIVE — surfaced on the printed line and
    in audit-all's violation count, never absorbed into --hard's boolean in this
    rollout (soft-then-hard precedent, governance/tasks/README.md rule 1).
    """
    meta = load_meta(path)
    state = str(meta.get("governance_state", "")).strip()
    scope = str(meta.get("hephaistos_scope", "")).strip()
    verdict = str(meta.get("qk_verdict", "")).strip()

    ok = state in {"cleared", "routed"} and scope == "defined" and verdict == "cleared"
    label = "PASS" if ok else ("REFUSED (hard gate)" if hard else "WARN (soft gate)")
    stamp_seg, _stamp_violations = gate_stamp.summarize(path)
    print(
        f"GATE {label}: {path.name} | governance_state={state or '∅'} "
        f"hephaistos_scope={scope or '∅'} qk_verdict={verdict or '∅'} | {stamp_seg}"
    )
    return ok


def audit_all() -> int:
    """Daily drift audit (invoked by nightly.sh): check every governed-task note.

    A note is audited only if frontmatter type == governed-task (the README and
    other governance docs are excluded). Notes legitimately pre-clearance
    (intake/scoped states) are reported as PASS-pending, not WARN — the drift
    signal is a task whose state ADVANCED without both clearance artifacts.
    Exit 1 if any violation is found (soft: caller surfaces, never blocks).
    """
    violations = 0
    key_unavailable = False
    for path in sorted(TASKS.glob("*.md")):
        meta = load_meta(path)
        if str(meta.get("type", "")).strip() != "governed-task":
            continue
        state = str(meta.get("governance_state", "")).strip()
        scope = str(meta.get("hephaistos_scope", "")).strip()
        verdict = str(meta.get("qk_verdict", "")).strip()
        relay = str(meta.get("relay_id", "")).strip()
        if state in {"cleared", "routed", "done"}:
            ok = scope == "defined" and verdict == "cleared"
            if state in {"routed", "done"} and relay in {"", "None", "null"}:
                ok = False
        else:
            ok = True
        stamp_seg, stamp_violations = gate_stamp.summarize(path)
        if stamp_violations:
            ok = False
            if any(v.startswith("KEY_UNAVAILABLE") for v in stamp_violations):
                key_unavailable = True
        if state in {"cleared", "routed", "done"}:
            label = "PASS" if ok else "WARN (soft gate)"
        else:
            label = "PASS (pre-clearance state)" if ok else "WARN (soft gate)"
        if not ok:
            violations += 1
        print(
            f"GATE {label}: {path.name} | governance_state={state or '∅'} "
            f"hephaistos_scope={scope or '∅'} qk_verdict={verdict or '∅'} relay_id={relay or '∅'} | {stamp_seg}"
        )
    if key_unavailable:
        print(
            "audit-all: KEY_UNAVAILABLE — one infrastructure fault (stamp key file missing/"
            "unreadable/wrong-mode), NOT independent forgeries; restore "
            "~/.agents/hephaistos/keys/gate-hmac.key before hunting a forger"
        )
    print(f"audit-all: {violations} violation(s)")
    return 1 if violations else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Governance gate for governed tasks")
    parser.add_argument(
        "task",
        nargs="?",
        help="task note path, or task id to find under governance/tasks/",
    )
    parser.add_argument("--hard", action="store_true", help="refuse (exit 1) instead of warning")
    parser.add_argument(
        "--audit-all",
        action="store_true",
        help="audit every governed-task note under governance/tasks/ (daily drift check)",
    )
    args = parser.parse_args()

    if args.audit_all:
        return audit_all()
    if not args.task:
        parser.error("task is required unless --audit-all is given")

    path = Path(args.task)
    if not path.exists():
        hits = sorted(TASKS.glob(f"*{args.task}*.md"))
        if len(hits) != 1:
            print(f"GATE ERROR: task not found (or ambiguous, {len(hits)} hits): {args.task}")
            return 1
        path = hits[0]

    meta = load_meta(path)
    state = str(meta.get("governance_state", "")).strip()
    scope = str(meta.get("hephaistos_scope", "")).strip()
    verdict = str(meta.get("qk_verdict", "")).strip()

    ok = state in {"cleared", "routed"} and scope == "defined" and verdict == "cleared"
    label = "PASS" if ok else ("REFUSED (hard gate)" if args.hard else "WARN (soft gate)")
    print(
        f"GATE {label}: {path.name} | governance_state={state or '∅'} "
        f"hephaistos_scope={scope or '∅'} qk_verdict={verdict or '∅'}"
    )
    if not ok and args.hard:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
