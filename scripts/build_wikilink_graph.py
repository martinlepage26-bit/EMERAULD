#!/usr/bin/env python3
"""
Build a deterministic Obsidian wikilink graph for the EMERAULD wiki corpus.

The graph is built from the same corpus as scripts/embed.py by default:
wiki/**/*.md, or .vector_store/paths.json when present. It does not call an LLM.

Outputs:
    .graph_store/nodes.json
    .graph_store/edges.json
    .graph_store/unresolved_links.json
    .graph_store/components.json
    .graph_store/summary.json
    .graph_store/graph_report.md
"""

from __future__ import annotations

import argparse
import json
import re
import time
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Any

from lightrag_config import VAULT_ROOT

STORE_DIR = VAULT_ROOT / ".graph_store"
VECTOR_PATHS_FILE = VAULT_ROOT / ".vector_store" / "paths.json"
CORPUS_DIRS = ["wiki", "maps", "projects"]
WIKILINK_RE = re.compile(r"(?<!!)\[\[([^\]\n]+)\]\]")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def strip_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text

    end = text.find("\n---", 4)
    if end == -1:
        return {}, text

    raw = text[4:end].strip()
    body = text[end + 4 :].lstrip("\n")
    meta: dict[str, Any] = {}
    current_key: str | None = None

    for line in raw.splitlines():
        if not line.strip():
            continue
        if line.startswith(("  - ", "- ")) and current_key:
            meta.setdefault(current_key, []).append(line.split("-", 1)[1].strip().strip("\"'"))
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        current_key = key
        if value == "[]":
            meta[key] = []
        elif value.startswith("[") and value.endswith("]"):
            items = [i.strip().strip("\"'") for i in value[1:-1].split(",") if i.strip()]
            meta[key] = items
        elif value:
            meta[key] = value.strip("\"'")
        else:
            meta[key] = []

    return meta, body


def load_corpus(use_vector_paths: bool = True) -> list[Path]:
    if use_vector_paths and VECTOR_PATHS_FILE.exists():
        paths = json.loads(VECTOR_PATHS_FILE.read_text(encoding="utf-8"))
        return sorted(
            VAULT_ROOT / p for p in paths
            if any(p.startswith(d + "/") for d in CORPUS_DIRS) and p.endswith(".md")
        )
    return sorted(
        p
        for d in CORPUS_DIRS
        for p in (VAULT_ROOT / d).rglob("*.md")
        if (VAULT_ROOT / d).exists()
    )


def normalize_target(target: str) -> str:
    target = target.split("|", 1)[0].split("#", 1)[0].strip()
    if target.endswith(".md"):
        target = target[:-3]
    return target.strip("/")


def extract_links(text: str) -> list[str]:
    links = []
    for match in WIKILINK_RE.finditer(text):
        target = normalize_target(match.group(1))
        if target:
            links.append(target)
    return links


def title_for(path: Path) -> str:
    rel = path.relative_to(VAULT_ROOT).with_suffix("").as_posix()
    if rel.startswith("wiki/"):
        return rel[len("wiki/"):]
    return rel


def build_alias_index(paths: list[Path]) -> tuple[dict[str, str], dict[str, dict[str, Any]]]:
    alias_to_id: dict[str, str] = {}
    metadata: dict[str, dict[str, Any]] = {}

    for path in paths:
        node_id = title_for(path)
        meta, body = strip_frontmatter(read_text(path))
        first_heading = next((line[2:].strip() for line in body.splitlines() if line.startswith("# ")), "")
        aliases = meta.get("aliases", [])
        if isinstance(aliases, str):
            aliases = [aliases]

        keys = {node_id, Path(node_id).name, path.stem}
        if first_heading:
            keys.add(first_heading)
        keys.update(a for a in aliases if a)

        for key in keys:
            alias_to_id.setdefault(key, node_id)

        metadata[node_id] = {
            "id": node_id,
            "title": Path(node_id).name,
            "path": str(path.relative_to(VAULT_ROOT)),
            "type": meta.get("type", "unknown"),
            "status": meta.get("status", "unknown"),
            "aliases": sorted(set(aliases)),
        }

    return alias_to_id, metadata


def connected_components(nodes: set[str], edges: list[dict[str, Any]]) -> list[list[str]]:
    adj: dict[str, set[str]] = {node: set() for node in nodes}
    for edge in edges:
        source = edge["source"]
        target = edge["target"]
        adj[source].add(target)
        adj[target].add(source)

    seen: set[str] = set()
    components: list[list[str]] = []
    for node in sorted(nodes):
        if node in seen:
            continue
        queue = deque([node])
        seen.add(node)
        comp = []
        while queue:
            cur = queue.popleft()
            comp.append(cur)
            for nxt in sorted(adj[cur]):
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        components.append(sorted(comp))

    return sorted(components, key=lambda c: (-len(c), c[0]))


def bucket_backlinks(count: int) -> str:
    if count <= 2:
        return str(count)
    if count <= 4:
        return "3-4"
    if count <= 6:
        return "5-6"
    if count <= 10:
        return "7-10"
    if count <= 20:
        return "11-20"
    if count <= 50:
        return "21-50"
    if count <= 100:
        return "51-100"
    return "101+"


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build_graph(use_vector_paths: bool = True) -> dict[str, Any]:
    paths = load_corpus(use_vector_paths)
    alias_to_id, nodes = build_alias_index(paths)

    edge_counts: Counter[tuple[str, str]] = Counter()
    outbound: dict[str, Counter[str]] = {}
    unresolved: list[dict[str, str]] = []

    for path in paths:
        node_id = title_for(path)
        _, body = strip_frontmatter(read_text(path))
        targets = extract_links(body)
        counts: Counter[str] = Counter()
        for raw_target in targets:
            resolved = alias_to_id.get(raw_target)
            if not resolved:
                unresolved.append({
                    "source": node_id,
                    "target": raw_target,
                    "source_path": str(path.relative_to(VAULT_ROOT)),
                })
                continue
            if resolved == node_id:
                continue
            counts[resolved] += 1
            edge_counts[(node_id, resolved)] += 1
        outbound[node_id] = counts

    edges = [
        {"source": source, "target": target, "count": count}
        for (source, target), count in sorted(edge_counts.items())
    ]

    inbound_counts: Counter[str] = Counter()
    for (_, target), count in edge_counts.items():
        inbound_counts[target] += count

    for node_id, node in nodes.items():
        node["outlinks"] = int(sum(outbound.get(node_id, Counter()).values()))
        node["unique_outlinks"] = len(outbound.get(node_id, Counter()))
        node["backlinks"] = int(inbound_counts[node_id])

    components = connected_components(set(nodes), edges)
    backlink_hist = Counter(bucket_backlinks(node["backlinks"]) for node in nodes.values())
    type_counts = Counter(node["type"] for node in nodes.values())

    zero = sorted(node_id for node_id, node in nodes.items() if node["backlinks"] == 0)
    one = sorted(node_id for node_id, node in nodes.items() if node["backlinks"] == 1)
    two = sorted(node_id for node_id, node in nodes.items() if node["backlinks"] == 2)

    summary = {
        "built_at": time.time(),
        "built_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "corpus": "vector_store paths.json wiki entries" if use_vector_paths and VECTOR_PATHS_FILE.exists() else "wiki/**/*.md",
        "nodes": len(nodes),
        "edges": len(edges),
        "edge_mentions": int(sum(edge_counts.values())),
        "unresolved_links": len(unresolved),
        "components": len(components),
        "largest_component": len(components[0]) if components else 0,
        "zero_backlink": len(zero),
        "one_backlink": len(one),
        "two_backlink": len(two),
        "backlink_histogram": dict(sorted(backlink_hist.items())),
        "type_counts": dict(type_counts.most_common()),
    }

    STORE_DIR.mkdir(exist_ok=True)
    write_json(STORE_DIR / "nodes.json", sorted(nodes.values(), key=lambda n: n["id"]))
    write_json(STORE_DIR / "edges.json", edges)
    write_json(STORE_DIR / "unresolved_links.json", unresolved)
    write_json(STORE_DIR / "components.json", components)
    write_json(STORE_DIR / "summary.json", summary)

    report = render_report(summary, zero, one, two, components, unresolved)
    (STORE_DIR / "graph_report.md").write_text(report, encoding="utf-8")
    return summary


def render_report(
    summary: dict[str, Any],
    zero: list[str],
    one: list[str],
    two: list[str],
    components: list[list[str]],
    unresolved: list[dict[str, str]],
) -> str:
    lines = [
        "# EMERAULD Wikilink Graph Report",
        "",
        f"Built: {summary['built_at_utc']}",
        f"Corpus: {summary['corpus']}",
        "",
        "## Summary",
        "",
        f"- Nodes: {summary['nodes']}",
        f"- Directed edges: {summary['edges']}",
        f"- Link mentions: {summary['edge_mentions']}",
        f"- Unresolved wikilinks: {summary['unresolved_links']}",
        f"- Connected components: {summary['components']}",
        f"- Largest component: {summary['largest_component']}",
        f"- Zero-backlink notes: {summary['zero_backlink']}",
        f"- One-backlink notes: {summary['one_backlink']}",
        f"- Two-backlink notes: {summary['two_backlink']}",
        "",
        "## Backlink Histogram",
        "",
    ]
    for bucket, count in summary["backlink_histogram"].items():
        lines.append(f"- {bucket}: {count}")

    lines.extend(["", "## Low-Backlink Notes", ""])
    for label, items in (("Zero", zero), ("One", one), ("Two", two)):
        lines.append(f"### {label} backlink ({len(items)})")
        if not items:
            lines.append("")
            lines.append("_None._")
        else:
            for item in items[:100]:
                lines.append(f"- [[{item}]]")
            if len(items) > 100:
                lines.append(f"- ... {len(items) - 100} more")
        lines.append("")

    lines.extend(["## Components", ""])
    for idx, comp in enumerate(components[:20], 1):
        lines.append(f"- Component {idx}: {len(comp)} notes; seed [[{comp[0]}]]")

    lines.extend(["", "## Top Unresolved Targets", ""])
    unresolved_counts = Counter(item["target"] for item in unresolved)
    for target, count in unresolved_counts.most_common(50):
        lines.append(f"- `{target}`: {count}")

    return "\n".join(lines).rstrip() + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--no-vector-paths",
        action="store_true",
        help="Ignore .vector_store/paths.json and scan wiki/**/*.md directly",
    )
    args = parser.parse_args()

    result = build_graph(use_vector_paths=not args.no_vector_paths)
    print(
        "Graph built: "
        f"{result['nodes']} nodes, {result['edges']} edges, "
        f"{result['components']} components, {result['unresolved_links']} unresolved links"
    )
