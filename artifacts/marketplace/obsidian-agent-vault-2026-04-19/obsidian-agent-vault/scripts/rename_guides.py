#!/usr/bin/env python3
"""Rename the buyer-facing guide names in this vault.

Run from the vault root:

    python scripts/rename_guides.py --context "North" --synthesis "Weaver"

The script changes visible guide names only. File names stay stable so prompts
and links keep working.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROLES = ("context", "synthesis", "link", "archive")
DEFAULT_NAMES = {
    "context": "Caelir",
    "synthesis": "Ilyris",
    "link": "Ariun",
    "archive": "Mnara",
}
TARGET_FILES = (
    "CLAUDE.md",
    "README.md",
    "START_HERE.md",
    "Home.md",
    "skills/README.md",
    "skills/synthesis_prompt.md",
    "skills/link_guide.md",
    "skills/archive_guide.md",
    "scripts/README.md",
)
BAD_CHARS = set("\n\r\t/\\<>|`[]{}")


def vault_root() -> Path:
    return Path(__file__).resolve().parents[1]


def config_path(root: Path) -> Path:
    return root / "scripts" / "guide_names.json"


def load_names(root: Path) -> dict[str, str]:
    path = config_path(root)
    if not path.exists():
        return DEFAULT_NAMES.copy()

    data = json.loads(path.read_text(encoding="utf-8"))
    names = data.get("names", {})
    return {role: str(names.get(role, DEFAULT_NAMES[role])) for role in ROLES}


def save_names(root: Path, names: dict[str, str]) -> None:
    path = config_path(root)
    path.write_text(
        json.dumps({"names": names}, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )


def clean_name(value: str, role: str) -> str:
    name = value.strip()
    if not name:
        raise SystemExit(f"{role} name cannot be empty.")
    if len(name) > 40:
        raise SystemExit(f"{role} name is too long; use 40 characters or fewer.")
    if any(char in BAD_CHARS for char in name):
        raise SystemExit(
            f"{role} name contains a character that could break Markdown or paths."
        )
    return name


def build_new_names(args: argparse.Namespace, current: dict[str, str]) -> dict[str, str]:
    updated = current.copy()
    for role in ROLES:
        value = getattr(args, role)
        if value is not None:
            updated[role] = clean_name(value, role)
    if len(set(updated.values())) != len(updated):
        raise SystemExit("Guide names must be unique so future renames stay reliable.")
    return updated


def replacement_pattern(current: dict[str, str]) -> re.Pattern[str]:
    terms = sorted(set(current.values()), key=len, reverse=True)
    return re.compile("|".join(re.escape(term) for term in terms))


def rename_text(text: str, current: dict[str, str], updated: dict[str, str]) -> str:
    reverse = {name: role for role, name in current.items()}
    pattern = replacement_pattern(current)

    def replace(match: re.Match[str]) -> str:
        role = reverse[match.group(0)]
        return updated[role]

    return pattern.sub(replace, text)


def show_names(names: dict[str, str]) -> None:
    print("Current guide names:")
    print(f"  context:   {names['context']}")
    print(f"  synthesis: {names['synthesis']}")
    print(f"  link:      {names['link']}")
    print(f"  archive:   {names['archive']}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Rename the buyer-facing guide names in this Obsidian vault."
    )
    parser.add_argument("--context", help="New name for the context guide.")
    parser.add_argument("--synthesis", help="New name for the synthesis guide.")
    parser.add_argument("--link", help="New name for the link guide.")
    parser.add_argument("--archive", help="New name for the archive guide.")
    parser.add_argument("--show", action="store_true", help="Show current guide names.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = vault_root()
    current = load_names(root)

    if args.show:
        show_names(current)
        return 0

    updated = build_new_names(args, current)
    if updated == current:
        print("No new names provided. Use --show to see current names.")
        return 0

    changed: list[str] = []
    for relative in TARGET_FILES:
        path = root / relative
        if not path.exists():
            continue
        original = path.read_text(encoding="utf-8")
        renamed = rename_text(original, current, updated)
        if renamed != original:
            changed.append(relative)
            if not args.dry_run:
                path.write_text(renamed, encoding="utf-8")

    if args.dry_run:
        print("Dry run. Files that would change:")
    else:
        save_names(root, updated)
        print("Guide names updated.")

    for relative in changed:
        print(f"  - {relative}")

    if not changed:
        print("No visible name references were found to update.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
