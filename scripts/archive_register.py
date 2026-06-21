#!/usr/bin/env python3
"""
Archive EMERAULD vault registers when they exceed their line thresholds.

Registers managed:
  - session-state.md                 (threshold: 600 lines)  → archive/session-state/
  - memory/agents/Journal.md         (threshold: 300 lines)  → archive/memory-agents/
  - memory/agents/Events.md          (threshold: 300 lines)  → archive/memory-agents/
  - memory/agents/Decisions.md       (threshold: 300 lines)  → archive/memory-agents/
  - memory/agents/Learning.md        (threshold: 300 lines)  → archive/memory-agents/
  - memory/agents/Blockers.md        (threshold: 300 lines)  → archive/memory-agents/

Usage:
    python3 archive_register.py                   # check all, archive overflows
    python3 archive_register.py --register Journal # check one register by name
    python3 archive_register.py --force            # archive all regardless of size
    python3 archive_register.py --dry-run          # report what would be archived
"""

import re
import shutil
import argparse
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

VAULT_ROOT = Path(__file__).parent.parent
TZ = ZoneInfo("America/Toronto")

# ── Register definitions ──────────────────────────────────────────────────────

@dataclass
class Register:
    name: str           # short name used in --register flag
    path: Path          # path relative to VAULT_ROOT
    threshold: int      # archive when line count exceeds this
    archive_dir: Path   # archive destination relative to VAULT_ROOT
    stem: str           # archive file stem prefix (e.g. "session-state", "Journal")
    register_type: str  # frontmatter type value
    agent: str          # frontmatter agent value


REGISTERS = [
    Register(
        name="session-state",
        path=VAULT_ROOT / "session-state.md",
        threshold=600,
        archive_dir=VAULT_ROOT / "archive" / "session-state",
        stem="session-state",
        register_type="session-state",
        agent="Trismégiste",
    ),
    Register(
        name="Journal",
        path=VAULT_ROOT / "memory" / "agents" / "Journal.md",
        threshold=300,
        archive_dir=VAULT_ROOT / "archive" / "memory-agents",
        stem="Journal",
        register_type="memory-register",
        agent="Trismégiste",
    ),
    Register(
        name="Events",
        path=VAULT_ROOT / "memory" / "agents" / "Events.md",
        threshold=300,
        archive_dir=VAULT_ROOT / "archive" / "memory-agents",
        stem="Events",
        register_type="memory-register",
        agent="Trismégiste / Bowie",
    ),
    Register(
        name="Decisions",
        path=VAULT_ROOT / "memory" / "agents" / "Decisions.md",
        threshold=300,
        archive_dir=VAULT_ROOT / "archive" / "memory-agents",
        stem="Decisions",
        register_type="memory-register",
        agent="Trismégiste / Bowie",
    ),
    Register(
        name="Learning",
        path=VAULT_ROOT / "memory" / "agents" / "Learning.md",
        threshold=300,
        archive_dir=VAULT_ROOT / "archive" / "memory-agents",
        stem="Learning",
        register_type="memory-register",
        agent="Trismégiste / Bowie",
    ),
    Register(
        name="Blockers",
        path=VAULT_ROOT / "memory" / "agents" / "Blockers.md",
        threshold=300,
        archive_dir=VAULT_ROOT / "archive" / "memory-agents",
        stem="Blockers",
        register_type="memory-register",
        agent="Trismégiste / Bowie",
    ),
]

REGISTER_BY_NAME = {r.name.lower(): r for r in REGISTERS}


# ── Core logic ────────────────────────────────────────────────────────────────

def line_count(path: Path) -> int:
    try:
        with path.open(encoding="utf-8") as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        return 0


def next_archive_number(reg: Register) -> int:
    reg.archive_dir.mkdir(parents=True, exist_ok=True)
    existing = sorted(reg.archive_dir.glob(f"{reg.stem}-*.md"))
    if not existing:
        return 1
    m = re.search(r"(\d+)$", existing[-1].stem)
    return int(m.group(1)) + 1 if m else 1


def archive_index(reg: Register) -> str:
    archived = sorted(reg.archive_dir.glob(f"{reg.stem}-*.md"))
    lines = []
    for p in archived:
        m = re.search(r"(\d+)$", p.stem)
        n = int(m.group(1)) if m else 0
        date = datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d")
        lines.append(f"- [[{p.stem}]] — archive #{n:03d} ({date})")
    return "\n".join(lines) if lines else "_(none yet)_"


def fresh_content(reg: Register, archive_path: Path) -> str:
    now = datetime.now(TZ).strftime("%Y-%m-%dT%H:%M%z")
    rel_dir = reg.archive_dir.relative_to(VAULT_ROOT)
    idx = archive_index(reg)
    return (
        f"---\n"
        f"type: {reg.register_type}\n"
        f"register: {reg.name}\n"
        f"updated: {now}\n"
        f"agent: {reg.agent}\n"
        f"archive: {archive_path.stem}\n"
        f"---\n\n"
        f"## Archives\n\n"
        f"Prior entries in `{rel_dir}/`:\n\n"
        f"{idx}\n\n"
        f"---\n\n"
    )


def do_archive(reg: Register, dry_run: bool = False) -> tuple[Path, int]:
    num = next_archive_number(reg)
    dest = reg.archive_dir / f"{reg.stem}-{num:03d}.md"
    if dry_run:
        return dest, num
    shutil.copy2(reg.path, dest)
    content = fresh_content(reg, dest)
    reg.path.write_text(content, encoding="utf-8")
    return dest, num


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Archive EMERAULD vault registers")
    parser.add_argument(
        "--register", metavar="NAME",
        help=f"Target one register by name: {', '.join(r.name for r in REGISTERS)}"
    )
    parser.add_argument("--force", action="store_true", help="Archive regardless of threshold")
    parser.add_argument("--dry-run", action="store_true", help="Report only, no changes")
    args = parser.parse_args()

    targets = REGISTERS
    if args.register:
        key = args.register.lower()
        if key not in REGISTER_BY_NAME:
            print(f"Unknown register '{args.register}'. Valid: {', '.join(r.name for r in REGISTERS)}")
            raise SystemExit(1)
        targets = [REGISTER_BY_NAME[key]]

    archived = []
    skipped = []

    for reg in targets:
        if not reg.path.exists():
            print(f"  {reg.name}: not found — skip")
            continue

        lines = line_count(reg.path)
        over = lines > reg.threshold

        if not args.force and not over:
            skipped.append((reg, lines))
            print(f"  {reg.name}: {lines}/{reg.threshold} lines — OK")
            continue

        flag = "(forced)" if args.force and not over else f"({lines} > {reg.threshold})"
        if args.dry_run:
            num = next_archive_number(reg)
            dest = reg.archive_dir / f"{reg.stem}-{num:03d}.md"
            print(f"  {reg.name}: would archive → {dest.relative_to(VAULT_ROOT)} {flag}")
        else:
            dest, num = do_archive(reg, dry_run=False)
            archived.append((reg, dest, lines))
            print(f"  {reg.name}: archived → {dest.relative_to(VAULT_ROOT)} {flag}")

    if not args.dry_run and archived:
        print(f"\n{len(archived)} register(s) archived.")
        print("Write VAULT ADDITIONS TRACKER entry before closing.")
    elif not args.dry_run and not archived:
        print("\nAll registers under threshold.")


if __name__ == "__main__":
    main()
