#!/usr/bin/env python3
"""
Vault verification harness for the 2026-07-08 overhaul (and reusable afterward).

Checks, against the same editable-file scope as enrich_frontmatter_backlinks.py:
- YAML parse failures + files with no frontmatter
- type histogram + Bases filter simulation (no Obsidian GUI on this host)
- tag pollution (color-*, filename-echo, blocklist words)
- created > updated impossible orderings
- updated-date histogram (stale-scan saturation check)
- graph store summary deltas vs a baseline JSON (--baseline)

Usage:
    audit_vault.py [--baseline _vault/overhaul-baseline-2026-07-08.json] [--json]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PROTECTED_DIRS = {"raw sources", "raw"}
SKIP_PARTS = {"node_modules"}
BLOCKLIST_PATH = ROOT / "scripts" / "tag_blocklist.txt"


def sanitize_tag(value: str) -> str:
    value = value.lower().strip().replace("_", "-").replace(" ", "-")
    value = re.sub(r"[^a-z0-9/-]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-/")
    return value


def editable_md():
    for p in sorted(ROOT.rglob("*.md")):
        rel_parts = p.relative_to(ROOT).parts
        if any(part.startswith(".") for part in rel_parts):
            continue
        if rel_parts[0] in PROTECTED_DIRS:
            continue
        if any(part in SKIP_PARTS for part in rel_parts):
            continue
        yield p


def main() -> None:
    parser = argparse.ArgumentParser(description="EMERAULD vault audit")
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    blocklist = set()
    if BLOCKLIST_PATH.exists():
        blocklist = {
            l.strip().lower()
            for l in BLOCKLIST_PATH.read_text(encoding="utf-8").splitlines()
            if l.strip() and not l.startswith("#")
        }

    total = 0
    no_fm: list[str] = []
    parse_fail: list[tuple[str, str]] = []
    type_hist: Counter[str] = Counter()
    updated_hist: Counter[str] = Counter()
    color_tags = echo_tags = block_tags = 0
    created_gt_updated: list[str] = []

    daily_total = daily_typed = 0
    projects_top_total = projects_top_project = 0
    projects_nested_project = 0
    wiki_person = 0

    for p in editable_md():
        rel = p.relative_to(ROOT).as_posix()
        total += 1
        text = p.read_text(encoding="utf-8", errors="ignore")
        if not text.startswith("---\n") or text.find("\n---", 4) == -1:
            no_fm.append(rel)
            continue
        end = text.find("\n---", 4)
        try:
            meta = yaml.safe_load(text[4:end]) or {}
            if not isinstance(meta, dict):
                raise ValueError("non-dict frontmatter")
        except Exception as e:
            parse_fail.append((rel, str(e).splitlines()[0][:120]))
            continue

        t = str(meta.get("type"))
        type_hist[t] += 1
        u = str(meta.get("updated") or "")[:10]
        if u:
            updated_hist[u] += 1
        c = str(meta.get("created") or "")[:10]
        if c and u and len(c) == 10 and len(u) == 10 and c > u:
            created_gt_updated.append(rel)

        tags = meta.get("tags") or []
        if isinstance(tags, list):
            echo = {sanitize_tag(p.stem), sanitize_tag(p.name)}
            for tag in tags:
                tag = str(tag)
                if tag.startswith("color-"):
                    color_tags += 1
                if tag in echo:
                    echo_tags += 1
                if tag in blocklist:
                    block_tags += 1

        parts = p.relative_to(ROOT).parts
        if parts[0] == "memory" and len(parts) > 2 and parts[1] == "daily":
            daily_total += 1
            if t == "daily-log":
                daily_typed += 1
        if parts[0] == "projects":
            if len(parts) == 2:
                projects_top_total += 1
                if t == "project":
                    projects_top_project += 1
            elif t == "project":
                projects_nested_project += 1
        if parts[0] == "wiki" and t == "person":
            wiki_person += 1

    graph = {}
    summary_path = ROOT / ".graph_store" / "summary.json"
    if summary_path.exists():
        s = json.loads(summary_path.read_text(encoding="utf-8"))
        graph = {
            "built_at_utc": s.get("built_at_utc"),
            "nodes": s.get("nodes"),
            "edges": s.get("edges"),
            "unresolved_links": s.get("unresolved_links"),
            "components": s.get("components"),
            "zero_backlink": s.get("zero_backlink"),
        }

    result = {
        "total_editable_md": total,
        "no_frontmatter": len(no_fm),
        "no_frontmatter_files": no_fm,
        "yaml_parse_failures": parse_fail,
        "created_gt_updated": len(created_gt_updated),
        "created_gt_updated_files": created_gt_updated,
        "tag_pollution": {"color": color_tags, "filename_echo": echo_tags, "blocklist": block_tags},
        "type_histogram_top": type_hist.most_common(20),
        "updated_histogram_top": updated_hist.most_common(10),
        "bases_simulation": {
            "Daily.base: memory/daily typed daily-log": f"{daily_typed}/{daily_total}",
            "Projects.base: projects/ top-level typed project": f"{projects_top_project}/{projects_top_total}",
            "projects/ nested files still typed project (should be 0)": projects_nested_project,
            "People.base: wiki type=person": wiki_person,
        },
        "graph_store": graph,
    }

    if args.baseline and args.baseline.exists():
        base = json.loads(args.baseline.read_text(encoding="utf-8"))
        result["baseline_deltas"] = {
            "no_frontmatter": f"{base.get('no_frontmatter_count')} -> {len(no_fm)}",
            "color_tags": f"{base.get('color_tag_occurrences')} -> {color_tags}",
            "echo_tags": f"{base.get('filename_echo_tag_occurrences')} -> {echo_tags}",
            "created_gt_updated": f"{base.get('created_gt_updated_count')} -> {len(created_gt_updated)}",
        }

    if args.json:
        json.dump(result, sys.stdout, indent=1, ensure_ascii=False)
        return

    print(f"editable_md={total}")
    print(f"no_frontmatter={len(no_fm)}")
    for f in no_fm[:20]:
        print(f"  no-fm: {f}")
    print(f"yaml_parse_failures={len(parse_fail)}")
    for f, err in parse_fail:
        print(f"  parse: {f}: {err}")
    print(f"created_gt_updated={len(created_gt_updated)}")
    print(f"tag_pollution color={color_tags} echo={echo_tags} blocklist={block_tags}")
    print("updated_histogram_top:", ", ".join(f"{d}:{n}" for d, n in updated_hist.most_common(6)))
    print("type_top:", ", ".join(f"{t}:{n}" for t, n in type_hist.most_common(12)))
    for k, v in result["bases_simulation"].items():
        print(f"bases: {k} = {v}")
    if graph:
        print("graph:", json.dumps(graph))
    if "baseline_deltas" in result:
        for k, v in result["baseline_deltas"].items():
            print(f"delta {k}: {v}")


if __name__ == "__main__":
    main()
