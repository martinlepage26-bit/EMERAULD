#!/usr/bin/env python3
"""
Enrich EMERAULD Markdown frontmatter with deterministic backlink metadata.

Scope:
- all Markdown files in the vault except protected `raw sources/`
- `.git` internals are ignored

The script strips frontmatter before extracting wikilinks so generated metadata does
not recursively become graph evidence. It updates the existing vault-level orphan
index with real body links for files that had no inbound links before this pass.
"""

from __future__ import annotations

import re
import subprocess
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
PROTECTED_RAW_SOURCES = ROOT / "raw sources"
INDEX_PATH = ROOT / "wiki" / "Orphan Index — Vault-Level Graph Repair 2026-05-06.md"
TODAY = "2026-06-26"

WIKILINK_RE = re.compile(r"(?<!!)\[\[([^\]\n]+)\]\]")
DATE_RE = re.compile(r"(20\d{2})[-_ ](0[1-9]|1[0-2])[-_ ]([0-3]\d)")
START_MARKER = "<!-- BEGIN GENERATED EDITABLE MD BACKLINK INDEX 2026-06-26 -->"
END_MARKER = "<!-- END GENERATED EDITABLE MD BACKLINK INDEX 2026-06-26 -->"

PREFERRED_KEYS = [
    "type",
    "title",
    "aliases",
    "tags",
    "status",
    "created",
    "updated",
    "vault_area",
    "canonical_path",
    "backlink_count",
    "backlinks",
]


def is_editable_markdown(path: Path) -> bool:
    if path.suffix.lower() != ".md":
        return False
    rel_parts = path.relative_to(ROOT).parts
    if ".git" in rel_parts:
        return False
    if path == PROTECTED_RAW_SOURCES or PROTECTED_RAW_SOURCES in path.parents:
        return False
    return True


def markdown_paths() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.md") if is_editable_markdown(path))


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 4 :].lstrip("\n")
    meta = yaml.safe_load(raw) or {}
    if not isinstance(meta, dict):
        meta = {}
    return meta, body


def strip_generated_index(body: str) -> str:
    start = body.find(START_MARKER)
    end = body.find(END_MARKER)
    if start == -1 or end == -1 or end < start:
        return body
    return body[:start] + body[end + len(END_MARKER) :]


def body_for_link_scan(path: Path, body: str) -> str:
    if path == INDEX_PATH:
        return strip_generated_index(body)
    return body


def normalize_target(target: str) -> str:
    target = target.split("|", 1)[0].split("#", 1)[0].strip()
    if target.endswith(".md"):
        target = target[:-3]
    return target.strip("/")


def rel_no_ext(path: Path) -> str:
    return path.relative_to(ROOT).with_suffix("").as_posix()


def link_id(path: Path) -> str:
    rel = rel_no_ext(path)
    if rel.startswith("wiki/"):
        return rel[len("wiki/") :]
    return rel


def wikilink(path: Path) -> str:
    return f"[[{rel_no_ext(path)}]]"


def first_heading(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def string_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, tuple):
        return [str(item).strip() for item in value if str(item).strip()]
    text = str(value).strip()
    return [text] if text else []


def title_for(path: Path, meta: dict[str, Any], body: str) -> str:
    existing = str(meta.get("title", "")).strip()
    if existing:
        return existing
    heading = first_heading(body)
    if heading and not heading.startswith("{{"):
        return heading
    return path.stem.strip() or path.name


def infer_type(path: Path, current: Any) -> str:
    current_text = str(current or "").strip()
    if current_text and current_text != "unknown":
        return current_text

    rel_parts = path.relative_to(ROOT).parts
    top = rel_parts[0] if rel_parts else path.name
    rel = path.relative_to(ROOT).as_posix()

    if top == "wiki":
        if "/bridges/" in rel:
            return "bridge-note"
        if "/archive/" in rel:
            return "archive-note"
        if "/skills/" in rel:
            return "skill"
        if path.name.endswith("MOC.md"):
            return "moc"
        return "wiki"
    if top == "maps":
        return "map"
    if top == "projects":
        return "project"
    if top == "templates":
        return "template"
    if top in {"archive", ".trash"}:
        return "archive"
    if top == "artifacts":
        return "artifact"
    if top == "assets":
        return "asset"
    if top == "governance" or top == "hephaistos":
        return "governance"
    if top == "memory":
        if len(rel_parts) > 1 and rel_parts[1] == "daily":
            return "daily-note"
        if len(rel_parts) > 1 and rel_parts[1] == "agents":
            return "agent-register"
        return "memory"
    if top == "personal-assistant-agents":
        return "agent-spec"
    if top == "PEER-REVIEW":
        return "peer-review-workspace"
    if top == "Publications":
        return "publication"
    if top == "raw":
        return "raw-intake"
    if top == ".github":
        return "agent-spec"
    if top == ".planning":
        return "planning-doc"
    if top == ".agent_bus":
        return "agent-bus-doc"
    if top == ".graph_store":
        return "generated-report"
    if top == "cloudflare":
        return "integration-doc"
    if top == "resources":
        return "resource"
    if top == "_vault":
        return "vault-doc"
    return "note"


def infer_status(path: Path, current: Any, inferred_type: str) -> str:
    current_text = str(current or "").strip()
    if current_text and current_text != "unknown":
        return current_text
    rel_parts = path.relative_to(ROOT).parts
    top = rel_parts[0] if rel_parts else ""
    if top in {"archive", ".trash"} or inferred_type in {"archive", "archive-note"}:
        return "archived"
    if inferred_type == "generated-report":
        return "generated"
    if inferred_type in {"template", "peer-review-workspace"}:
        return "draft"
    return "active"


def sanitize_tag(value: str) -> str:
    value = value.lower().strip().replace("_", "-").replace(" ", "-")
    value = re.sub(r"[^a-z0-9/-]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-/")
    return value


def enrich_tags(path: Path, meta: dict[str, Any], inferred_type: str) -> list[str]:
    rel_parts = path.relative_to(ROOT).parts
    top = rel_parts[0] if rel_parts else "root"
    tags = string_list(meta.get("tags"))
    additions = [sanitize_tag(inferred_type), sanitize_tag(top)]
    if len(rel_parts) > 1 and not rel_parts[1].startswith("."):
        additions.append(sanitize_tag(rel_parts[1]))
    seen: set[str] = set()
    merged = []
    for tag in tags + additions:
        clean = sanitize_tag(tag)
        if clean and clean not in seen:
            seen.add(clean)
            merged.append(clean)
    return merged


def infer_created(path: Path, current: Any) -> str:
    current_text = scalar_to_string(current)
    if current_text:
        return current_text
    match = DATE_RE.search(path.as_posix())
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    rel = path.relative_to(ROOT).as_posix()
    try:
        output = subprocess.check_output(
            ["git", "-C", str(ROOT), "log", "--follow", "--format=%ad", "--date=short", "--", rel],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        output = ""
    if output:
        return output.splitlines()[-1].strip()
    return TODAY


def scalar_to_string(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    return str(value).strip()


def normalize_yaml_value(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(k): normalize_yaml_value(v) for k, v in value.items()}
    if isinstance(value, list):
        return [normalize_yaml_value(item) for item in value]
    if isinstance(value, tuple):
        return [normalize_yaml_value(item) for item in value]
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    return value


def build_link_indexes(
    paths: list[Path],
    metas: dict[Path, dict[str, Any]],
    bodies: dict[Path, str],
) -> tuple[dict[str, Path], dict[str, list[Path]], dict[str, list[Path]]]:
    exact: dict[str, Path] = {}
    stem_map: dict[str, list[Path]] = defaultdict(list)
    alias_seen: dict[str, set[Path]] = defaultdict(set)

    for path in paths:
        for key in {rel_no_ext(path), link_id(path), path.stem}:
            exact.setdefault(key, path)
        stem_map[path.stem].append(path)

        title = title_for(path, metas[path], bodies[path])
        aliases = string_list(metas[path].get("aliases"))
        for key in [title, first_heading(bodies[path]), *aliases]:
            if key:
                alias_seen[key].add(path)

    alias_map = {key: sorted(value) for key, value in alias_seen.items()}
    return exact, stem_map, alias_map


def resolve_target(
    target: str,
    exact: dict[str, Path],
    stem_map: dict[str, list[Path]],
    alias_map: dict[str, list[Path]],
) -> Path | None:
    normalized = normalize_target(target)
    if not normalized:
        return None
    if normalized in exact:
        return exact[normalized]
    if len(stem_map.get(normalized, [])) == 1:
        return stem_map[normalized][0]
    if len(alias_map.get(normalized, [])) == 1:
        return alias_map[normalized][0]
    return None


def build_inbound(
    paths: list[Path],
    bodies: dict[Path, str],
    exact: dict[str, Path],
    stem_map: dict[str, list[Path]],
    alias_map: dict[str, list[Path]],
) -> tuple[dict[Path, set[Path]], Counter[str]]:
    inbound = {path: set() for path in paths}
    unresolved: Counter[str] = Counter()

    for source in paths:
        body = body_for_link_scan(source, bodies[source])
        for match in WIKILINK_RE.finditer(body):
            target = normalize_target(match.group(1))
            dest = resolve_target(target, exact, stem_map, alias_map)
            if dest is None:
                unresolved[target] += 1
                continue
            if dest != source:
                inbound[dest].add(source)

    return inbound, unresolved


def generated_index_section(zero_inbound: list[Path]) -> str:
    groups: dict[str, list[Path]] = defaultdict(list)
    for path in zero_inbound:
        top = path.relative_to(ROOT).parts[0]
        groups[top].append(path)

    lines = [
        START_MARKER,
        "",
        "## Editable Markdown backlink sweep — 2026-06-26",
        "",
        "Generated index links for editable Markdown files that had no inbound wikilinks before this pass.",
        "`raw sources/` is excluded by vault provenance rule; those files were not modified.",
        "",
        f"- Editable Markdown files scanned: **{len(markdown_paths())}**",
        f"- Files given generated inbound links: **{len(zero_inbound)}**",
        "",
    ]

    for group in sorted(groups):
        lines.append(f"### {group}")
        for path in sorted(groups[group], key=lambda p: p.relative_to(ROOT).as_posix()):
            lines.append(f"- {wikilink(path)}")
        lines.append("")

    lines.extend([END_MARKER, ""])
    return "\n".join(lines)


def update_generated_index(body: str, zero_inbound: list[Path]) -> str:
    section = generated_index_section(zero_inbound)
    start = body.find(START_MARKER)
    end = body.find(END_MARKER)
    if start != -1 and end != -1 and end > start:
        return body[:start].rstrip() + "\n\n" + section + body[end + len(END_MARKER) :].lstrip("\n")
    return body.rstrip() + "\n\n" + section


def ordered_meta(meta: dict[str, Any]) -> dict[str, Any]:
    normalized = {str(k): normalize_yaml_value(v) for k, v in meta.items()}
    ordered: dict[str, Any] = {}
    for key in PREFERRED_KEYS:
        if key in normalized:
            ordered[key] = normalized.pop(key)
    for key, value in normalized.items():
        ordered[key] = value
    return ordered


def write_markdown(path: Path, meta: dict[str, Any], body: str) -> bool:
    dumped = yaml.safe_dump(
        ordered_meta(meta),
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
        width=1000,
    )
    new_text = f"---\n{dumped}---\n\n{body.lstrip()}"
    old_text = path.read_text(encoding="utf-8", errors="ignore")
    if new_text == old_text:
        return False
    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> None:
    paths = markdown_paths()
    metas: dict[Path, dict[str, Any]] = {}
    bodies: dict[Path, str] = {}

    for path in paths:
        meta, body = split_frontmatter(path.read_text(encoding="utf-8", errors="ignore"))
        metas[path] = meta
        bodies[path] = body

    exact, stem_map, alias_map = build_link_indexes(paths, metas, bodies)
    inbound, unresolved = build_inbound(paths, bodies, exact, stem_map, alias_map)
    zero_inbound = sorted([path for path, sources in inbound.items() if not sources])

    final_inbound = {path: set(sources) for path, sources in inbound.items()}
    for path in zero_inbound:
        if path != INDEX_PATH:
            final_inbound[path].add(INDEX_PATH)

    if INDEX_PATH in bodies:
        bodies[INDEX_PATH] = update_generated_index(bodies[INDEX_PATH], zero_inbound)

    changed = 0
    for path in paths:
        meta = dict(metas[path])
        title = title_for(path, meta, bodies[path])
        inferred_type = infer_type(path, meta.get("type"))

        aliases = string_list(meta.get("aliases"))
        unique_alias = rel_no_ext(path)
        if not aliases:
            aliases = [unique_alias]
        elif unique_alias not in aliases:
            aliases.append(unique_alias)

        sources = sorted(final_inbound[path], key=lambda p: link_id(p))
        backlinks = [wikilink(source) for source in sources]

        meta["type"] = inferred_type
        meta["title"] = title
        meta["aliases"] = aliases
        meta["tags"] = enrich_tags(path, meta, inferred_type)
        meta["status"] = infer_status(path, meta.get("status"), inferred_type)
        meta["created"] = infer_created(path, meta.get("created"))
        meta["updated"] = TODAY
        meta["vault_area"] = path.relative_to(ROOT).parts[0]
        meta["canonical_path"] = path.relative_to(ROOT).as_posix()
        meta["backlink_count"] = len(backlinks)
        meta["backlinks"] = backlinks

        if write_markdown(path, meta, bodies[path]):
            changed += 1

    print(f"editable_md={len(paths)}")
    print(f"changed={changed}")
    print(f"zero_inbound_before_generated_index={len(zero_inbound)}")
    print(f"unresolved_wikilink_targets={sum(unresolved.values())}")
    if unresolved:
        print("top_unresolved=" + ", ".join(f"{target}:{count}" for target, count in unresolved.most_common(10)))


if __name__ == "__main__":
    main()
