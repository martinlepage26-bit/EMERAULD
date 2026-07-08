#!/usr/bin/env python3
"""
Enrich EMERAULD Markdown frontmatter with deterministic backlink metadata.

Scope:
- all Markdown files in the vault except protected raw lanes (`raw sources/`, `raw/`),
  dot-directories (.git, .trash, .planning, .github, .agent_bus, .graph_store, ...),
  and node_modules.

Behavior (revised 2026-07-08 overhaul):
- `updated:` is PRESERVED. It is never re-stamped on unchanged content. Missing values
  are backfilled from git last-commit date, then `created`, then today. The 2026-06-26
  run stamped a hardcoded date vault-wide and blinded the stale scanner — never again.
- `created > updated` impossible orderings are repaired (updated raised to created).
- `--strip-noise-tags` removes color-* tags, filename-echo tags, and blocklisted
  body-word tags (scripts/tag_blocklist.txt).
- Path-variant aliases are no longer injected and existing ones are stripped
  (canonical_path/vault_area already encode location; Obsidian resolves filenames natively).
- Type values are normalized so Bases filters work (daily-log canonical; only top-level
  projects/*.md are `project`, nested working-dir mirrors are `project-mirror`).
- `domain` and `priority` are inferred add-only (never overwrite existing values).
- `--dry-run` reports planned changes, including every file whose `updated` would move.

The script strips frontmatter before extracting wikilinks so generated metadata does
not recursively become graph evidence. It updates the existing vault-level orphan
index with real body links for files that had no inbound links before this pass.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import date, datetime
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
PROTECTED_DIRS = {"raw sources", "raw"}
SKIP_PARTS = {"node_modules"}
INDEX_NAME = "Orphan Index — Vault-Level Graph Repair 2026-05-06.md"
TAG_BLOCKLIST_PATH = ROOT / "scripts" / "tag_blocklist.txt"
TODAY = date.today().isoformat()

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
    "domain",
    "priority",
    "created",
    "updated",
    "vault_area",
    "canonical_path",
    "backlink_count",
    "backlinks",
]

# Normalize drifted type values to the canonical vocabulary Bases filter on.
TYPE_NORMALIZE = {
    "memory-daily": "daily-log",
    "daily": "daily-log",
    "daily-note": "daily-log",
}

# Add-only domain inference by location (post-PARA layout).
DOMAIN_BY_PREFIX = [
    ("Areas/PHAROS/", "pharos"),
    ("Areas/Writing/", "writing"),
    ("Areas/Personal/", "personal"),
    ("Areas/Lavoie/", "lavoie"),
    ("Resources/", "reference"),
    ("governance/", "governance"),
    ("hephaistos/", "governance"),
]


def load_tag_blocklist() -> set[str]:
    if not TAG_BLOCKLIST_PATH.exists():
        return set()
    return {
        line.strip().lower()
        for line in TAG_BLOCKLIST_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    }


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


def index_path(paths: list[Path]) -> Path | None:
    default = ROOT / "wiki" / INDEX_NAME
    if default in paths:
        return default
    for path in paths:
        if path.name == INDEX_NAME:
            return path
    return None


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 4 :].lstrip("\n")
    try:
        meta = yaml.safe_load(raw) or {}
    except yaml.YAMLError as exc:
        raise ValueError(f"unparseable frontmatter: {exc}") from exc
    if not isinstance(meta, dict):
        meta = {}
    return meta, body


def strip_generated_index(body: str) -> str:
    start = body.find(START_MARKER)
    end = body.find(END_MARKER)
    if start == -1 or end == -1 or end < start:
        return body
    return body[:start] + body[end + len(END_MARKER) :]


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
    if isinstance(value, (list, tuple)):
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
    rel_parts = path.relative_to(ROOT).parts
    top = rel_parts[0] if rel_parts else path.name
    rel = path.relative_to(ROOT).as_posix()

    current_text = str(current or "").strip()
    if current_text in TYPE_NORMALIZE:
        current_text = TYPE_NORMALIZE[current_text]
    if current_text and current_text != "unknown":
        # Nested working-dir mirrors must not masquerade as project index notes.
        if top == "projects" and len(rel_parts) > 2 and current_text == "project":
            return "project-mirror"
        return current_text

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
        return "project" if len(rel_parts) == 2 else "project-mirror"
    if top == "templates":
        return "template"
    if top == "archive":
        return "archive"
    if top == "artifacts":
        return "artifact"
    if top == "assets":
        return "asset"
    if top in {"governance", "hephaistos"}:
        return "governance"
    if top == "memory":
        if len(rel_parts) > 1 and rel_parts[1] == "daily":
            return "daily-log"
        if len(rel_parts) > 1 and rel_parts[1] == "agents":
            return "agent-register"
        return "memory"
    if top == "Areas":
        return "area-note"
    if top == "Resources":
        return "resource"
    if top == "Inbox":
        return "inbox"
    if top == "Logs":
        return "log"
    if top == "PEER-REVIEW":
        return "peer-review-workspace"
    if top == "Publications":
        return "publication"
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
    if top == "archive" or inferred_type in {"archive", "archive-note"}:
        return "archived"
    if inferred_type == "generated-report":
        return "generated"
    if inferred_type in {"template", "peer-review-workspace"}:
        return "draft"
    return "active"


def infer_domain(path: Path, current: Any) -> str | None:
    current_text = str(current or "").strip()
    if current_text:
        return current_text
    rel = path.relative_to(ROOT).as_posix()
    for prefix, domain in DOMAIN_BY_PREFIX:
        if rel.startswith(prefix):
            return domain
    return None


def infer_priority(current: Any, inferred_type: str, status: str) -> str | None:
    current_text = str(current or "").strip()
    if current_text:
        return current_text
    if inferred_type == "moc":
        return "high"
    if inferred_type == "project" and status == "in-progress":
        return "high"
    if status == "archived":
        return "low"
    return None


def sanitize_tag(value: str) -> str:
    value = value.lower().strip().replace("_", "-").replace(" ", "-")
    value = re.sub(r"[^a-z0-9/-]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-/")
    return value


def enrich_tags(
    path: Path,
    meta: dict[str, Any],
    inferred_type: str,
    strip_noise: bool,
    blocklist: set[str],
) -> list[str]:
    rel_parts = path.relative_to(ROOT).parts
    top = rel_parts[0] if rel_parts else "root"
    tags = string_list(meta.get("tags"))
    additions = [sanitize_tag(inferred_type), sanitize_tag(top)]
    if len(rel_parts) > 2 and not rel_parts[1].startswith("."):
        additions.append(sanitize_tag(rel_parts[1]))

    echo_tags = {sanitize_tag(path.stem), sanitize_tag(path.name)}
    seen: set[str] = set()
    merged = []
    for tag in tags + additions:
        clean = sanitize_tag(tag)
        if not clean or clean in seen:
            continue
        if strip_noise:
            if clean.startswith("color-"):
                continue
            if clean in echo_tags:
                continue
            if clean in blocklist:
                continue
        seen.add(clean)
        merged.append(clean)
    return merged


def clean_aliases(path: Path, meta: dict[str, Any]) -> list[str]:
    aliases = string_list(meta.get("aliases"))
    cleaned = []
    for alias in aliases:
        if alias == path.stem:
            continue  # Obsidian resolves filenames natively
        if "/" in alias and alias.split("/")[-1] in {path.stem, path.name}:
            continue  # path-variant of canonical_path (current or former)
        if alias not in cleaned:
            cleaned.append(alias)
    return cleaned


def git_last_modified(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    try:
        output = subprocess.check_output(
            ["git", "-C", str(ROOT), "log", "-1", "--format=%ad", "--date=short", "--", rel],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        output = ""
    return output


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


def resolve_updated(path: Path, current: Any, created: str, body_changed: bool) -> str:
    """Preserve `updated` unless the body actually changed; backfill when absent."""
    existing = scalar_to_string(current)
    if body_changed:
        updated = TODAY
    elif existing:
        updated = existing
    else:
        updated = git_last_modified(path) or created or TODAY
    if created and updated and created[:10] > updated[:10]:
        updated = created[:10]
    return updated


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
    if isinstance(value, (list, tuple)):
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
    idx_path: Path | None,
    exact: dict[str, Path],
    stem_map: dict[str, list[Path]],
    alias_map: dict[str, list[Path]],
) -> tuple[dict[Path, set[Path]], Counter[str]]:
    inbound = {path: set() for path in paths}
    unresolved: Counter[str] = Counter()

    for source in paths:
        body = bodies[source]
        if idx_path is not None and source == idx_path:
            body = strip_generated_index(body)
        for match in WIKILINK_RE.finditer(body):
            target = normalize_target(match.group(1))
            dest = resolve_target(target, exact, stem_map, alias_map)
            if dest is None:
                unresolved[target] += 1
                continue
            if dest != source:
                inbound[dest].add(source)

    return inbound, unresolved


def generated_index_section(paths: list[Path], zero_inbound: list[Path]) -> str:
    groups: dict[str, list[Path]] = defaultdict(list)
    for path in zero_inbound:
        top = path.relative_to(ROOT).parts[0]
        groups[top].append(path)

    lines = [
        START_MARKER,
        "",
        f"## Editable Markdown backlink sweep — {TODAY}",
        "",
        "Generated index links for editable Markdown files that had no inbound wikilinks before this pass.",
        "`raw sources/` and `raw/` are excluded by vault provenance rule; those files were not modified.",
        "",
        f"- Editable Markdown files scanned: **{len(paths)}**",
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


def update_generated_index(body: str, paths: list[Path], zero_inbound: list[Path]) -> str:
    section = generated_index_section(paths, zero_inbound)
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


def render_markdown(meta: dict[str, Any], body: str) -> str:
    dumped = yaml.safe_dump(
        ordered_meta(meta),
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
        width=1000,
    )
    return f"---\n{dumped}---\n\n{body.lstrip()}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Enrich EMERAULD frontmatter + backlink metadata")
    parser.add_argument("--dry-run", action="store_true", help="Report planned changes, write nothing")
    parser.add_argument(
        "--strip-noise-tags",
        action="store_true",
        help="Strip color-* tags, filename-echo tags, and scripts/tag_blocklist.txt entries",
    )
    args = parser.parse_args()

    blocklist = load_tag_blocklist()
    paths = markdown_paths()
    idx_path = index_path(paths)
    metas: dict[Path, dict[str, Any]] = {}
    bodies: dict[Path, str] = {}
    original_bodies: dict[Path, str] = {}

    skipped_unparseable: list[str] = []
    for path in paths:
        try:
            meta, body = split_frontmatter(path.read_text(encoding="utf-8", errors="ignore"))
        except ValueError as exc:
            print(f"SKIP unparseable frontmatter: {path.relative_to(ROOT)} ({exc})", file=sys.stderr)
            skipped_unparseable.append(path.relative_to(ROOT).as_posix())
            continue
        metas[path] = meta
        bodies[path] = body
        original_bodies[path] = body
    if skipped_unparseable:
        paths = [p for p in paths if p.relative_to(ROOT).as_posix() not in set(skipped_unparseable)]

    exact, stem_map, alias_map = build_link_indexes(paths, metas, bodies)
    inbound, unresolved = build_inbound(paths, bodies, idx_path, exact, stem_map, alias_map)
    zero_inbound = sorted([path for path, sources in inbound.items() if not sources])

    final_inbound = {path: set(sources) for path, sources in inbound.items()}
    if idx_path is not None:
        for path in zero_inbound:
            if path != idx_path:
                final_inbound[path].add(idx_path)
        bodies[idx_path] = update_generated_index(bodies[idx_path], paths, zero_inbound)

    changed = 0
    updated_bumped: list[str] = []
    type_changes: Counter[str] = Counter()
    tags_stripped = 0

    for path in paths:
        meta = dict(metas[path])
        title = title_for(path, meta, bodies[path])
        old_type = str(meta.get("type") or "").strip()
        inferred_type = infer_type(path, meta.get("type"))
        if old_type and old_type != inferred_type:
            type_changes[f"{old_type}->{inferred_type}"] += 1

        aliases = clean_aliases(path, meta)

        sources = sorted(final_inbound[path], key=lambda p: link_id(p))
        backlinks = [wikilink(source) for source in sources]

        old_tags = string_list(meta.get("tags"))
        new_tags = enrich_tags(path, meta, inferred_type, args.strip_noise_tags, blocklist)
        tags_stripped += max(0, len(old_tags) - len([t for t in new_tags if t in {sanitize_tag(x) for x in old_tags}]))

        body_changed = bodies[path] != original_bodies[path]
        status = infer_status(path, meta.get("status"), inferred_type)
        created = infer_created(path, meta.get("created"))
        updated = resolve_updated(path, meta.get("updated"), created, body_changed)
        if scalar_to_string(meta.get("updated")) != updated:
            updated_bumped.append(path.relative_to(ROOT).as_posix())

        meta["type"] = inferred_type
        meta["title"] = title
        if aliases:
            meta["aliases"] = aliases
        elif "aliases" in meta:
            del meta["aliases"]
        meta["tags"] = new_tags
        meta["status"] = status
        domain = infer_domain(path, meta.get("domain"))
        if domain:
            meta["domain"] = domain
        priority = infer_priority(meta.get("priority"), inferred_type, status)
        if priority:
            meta["priority"] = priority
        meta["created"] = created
        meta["updated"] = updated
        meta["vault_area"] = path.relative_to(ROOT).parts[0]
        meta["canonical_path"] = path.relative_to(ROOT).as_posix()
        meta["backlink_count"] = len(backlinks)
        meta["backlinks"] = backlinks

        new_text = render_markdown(meta, bodies[path])
        old_text = path.read_text(encoding="utf-8", errors="ignore")
        if new_text != old_text:
            changed += 1
            if not args.dry_run:
                path.write_text(new_text, encoding="utf-8")

    mode = "DRY-RUN " if args.dry_run else ""
    print(f"{mode}editable_md={len(paths)}")
    print(f"{mode}changed={changed}")
    print(f"{mode}zero_inbound_before_generated_index={len(zero_inbound)}")
    print(f"{mode}unresolved_wikilink_targets={sum(unresolved.values())}")
    print(f"{mode}updated_field_moved={len(updated_bumped)}")
    for rel in updated_bumped:
        print(f"  updated-moved: {rel}")
    if type_changes:
        print("type_normalizations=" + ", ".join(f"{k}:{v}" for k, v in type_changes.most_common(20)))
    if unresolved:
        print("top_unresolved=" + ", ".join(f"{target}:{count}" for target, count in unresolved.most_common(10)))


if __name__ == "__main__":
    main()
