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


def main() -> int:
    parser = argparse.ArgumentParser(description="Governance gate for governed tasks")
    parser.add_argument("task", help="task note path, or task id to find under governance/tasks/")
    parser.add_argument("--hard", action="store_true", help="refuse (exit 1) instead of warning")
    args = parser.parse_args()

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
