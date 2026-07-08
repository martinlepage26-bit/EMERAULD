#!/usr/bin/env python3
"""
PARA migration engine for the 2026-07-08 EMERAULD overhaul.

Executes manifest rows (CSV: source,dest,action,cluster) as `git mv` moves, then
repairs path-form wikilinks vault-wide and updates the moved files' own
canonical_path/vault_area/dir-echo tags. Bare [[Stem]] links are left alone —
Obsidian resolves them by basename and stem collisions were pre-checked at
manifest build time. Vault-wide `backlinks:` frontmatter arrays are also
rewritten where they reference moved paths, but no other frontmatter of
non-moved files is touched and `updated:` is never bumped (link repair is a
path-mechanical edit, not a content change).

Usage:
    para_migrate.py MANIFEST.csv --rows 1:20 [--dry-run]
    para_migrate.py MANIFEST.csv --verify-only   # scan for stale [[wiki/...]] links of executed rows
"""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
PROTECTED_DIRS = {"raw sources", "raw"}
SKIP_PARTS = {"node_modules"}


def is_editable_markdown(path: Path) -> bool:
    if path.suffix.lower() != ".md":
        return False
    rel_parts = path.relative_to(ROOT).parts
    if any(part.startswith(".") for part in rel_parts):
        return False
    if rel_parts[0] in PROTECTED_DIRS:
        return False
    if any(part in SKIP_PARTS for part in rel_parts):
        return False
    return True


def markdown_paths() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.md") if is_editable_markdown(path))


def load_manifest(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    for i, row in enumerate(rows, 1):
        row["_row"] = str(i)
        for key in ("source", "dest", "action"):
            if not (row.get(key) or "").strip():
                raise SystemExit(f"manifest row {i}: missing {key}")
    return rows


def rel_no_ext(rel: str) -> str:
    return rel[:-3] if rel.endswith(".md") else rel


def link_replacements(old_rel: str, new_rel: str) -> list[tuple[re.Pattern[str], str]]:
    """Patterns that rewrite path-form links [[old...]] / ![[old...]] to the new path."""
    old = re.escape(rel_no_ext(old_rel))
    new = rel_no_ext(new_rel)
    # match [[old]] [[old|alias]] [[old#heading]] [[old.md]] and embeds; keep suffix intact
    pat = re.compile(r"\[\[" + old + r"(\.md)?(?=[\]|#])")
    return [(pat, "[[" + new)]


def split_frontmatter_text(text: str) -> tuple[str | None, str]:
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    return text[: end + 4], text[end + 4 :]


def update_moved_frontmatter(path: Path, old_rel: str, new_rel: str) -> None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    fm, body = split_frontmatter_text(text)
    if fm is None:
        return
    try:
        meta = yaml.safe_load(fm[4:-4]) or {}
    except Exception:
        return
    if not isinstance(meta, dict):
        return
    old_top = old_rel.split("/", 1)[0]
    new_top = new_rel.split("/", 1)[0]
    meta["canonical_path"] = new_rel
    meta["vault_area"] = new_top
    tags = meta.get("tags")
    if isinstance(tags, list):
        meta["tags"] = [new_top.lower() if str(t) == old_top.lower() else t for t in tags]
        # dedupe preserving order
        seen: set[str] = set()
        meta["tags"] = [t for t in meta["tags"] if not (str(t) in seen or seen.add(str(t)))]
    aliases = meta.get("aliases")
    if isinstance(aliases, list):
        old_alias = rel_no_ext(old_rel)
        meta["aliases"] = [a for a in aliases if str(a) != old_alias]
        if not meta["aliases"]:
            del meta["aliases"]
    dumped = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, default_flow_style=False, width=1000)
    path.write_text(f"---\n{dumped}---{body}", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Manifest-driven PARA migration")
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--rows", help="1-based inclusive range, e.g. 1:20")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verify-only", action="store_true", help="Scan for stale links to any executed (missing-source) row")
    args = parser.parse_args()

    rows = load_manifest(args.manifest)

    if args.verify_only:
        stale = 0
        moved = [r for r in rows if not (ROOT / r["source"]).exists() and (ROOT / r["dest"]).exists()]
        texts = {p: p.read_text(encoding="utf-8", errors="ignore") for p in markdown_paths()}
        pats = {
            row["source"]: re.compile(
                r"\[\[" + re.escape(rel_no_ext(row["source"])) + r"(\.md)?(?=[\]|#])"
            )
            for row in moved
        }
        for src, pat in pats.items():
            for p, text in texts.items():
                n = len(pat.findall(text))
                if n:
                    stale += n
                    print(f"STALE: {p.relative_to(ROOT)} has {n}x [[{rel_no_ext(src)}")
        print(f"verify: {len(moved)} executed rows, {stale} stale link occurrences")
        sys.exit(1 if stale else 0)

    if not args.rows:
        raise SystemExit("--rows required (e.g. --rows 1:20)")
    start, end = (int(x) for x in args.rows.split(":"))
    batch = [r for r in rows if start <= int(r["_row"]) <= end and r["action"] in {"move", "archive"}]

    moves: list[tuple[str, str]] = []
    for row in batch:
        src = ROOT / row["source"]
        dst = ROOT / row["dest"]
        if not src.exists():
            print(f"SKIP row {row['_row']}: source missing: {row['source']}")
            continue
        if dst.exists():
            print(f"SKIP row {row['_row']}: dest exists: {row['dest']}")
            continue
        moves.append((row["source"], row["dest"]))

    print(f"batch rows {start}:{end} → {len(moves)} moves{' (dry-run)' if args.dry_run else ''}")
    if args.dry_run:
        for old, new in moves:
            print(f"  {old} -> {new}")
        return

    for old, new in moves:
        (ROOT / new).parent.mkdir(parents=True, exist_ok=True)
        subprocess.check_call(["git", "-C", str(ROOT), "mv", old, new])

    # vault-wide path-form link repair (single pass over all editable files)
    all_reps: list[tuple[re.Pattern[str], str]] = []
    for old, new in moves:
        all_reps.extend(link_replacements(old, new))
    repaired = 0
    replacements = 0
    for path in markdown_paths():
        text = path.read_text(encoding="utf-8", errors="ignore")
        new_text = text
        for pat, sub in all_reps:
            new_text = pat.sub(sub, new_text)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            repaired += 1
            replacements += sum(1 for pat, _ in all_reps for _ in pat.finditer(text))

    for old, new in moves:
        update_moved_frontmatter(ROOT / new, old, new)

    print(f"moved={len(moves)} files_link_repaired={repaired} replacements~={replacements}")


if __name__ == "__main__":
    main()
