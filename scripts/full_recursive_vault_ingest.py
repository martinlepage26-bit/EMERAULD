#!/usr/bin/env python3
"""
Full recursive Documents/Downloads intake for EMERAULD.

This runner is intentionally conservative around existing vault content:
- external eligible source files are verified, hash-checked, and hard-moved into raw/
- EMERAULD raw/ and raw sources/ are audited in place, not repacked
- wiki/raw-sources source notes are promoted into wiki/source-notes
- machine-readable reports and small cluster/register notes are written
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
from pathlib import Path
from typing import Any


USER_ROOT = Path(r"C:\Users\softinfo")
DOCS_ROOT = USER_ROOT / "Documents"
DOWNLOADS_ROOT = USER_ROOT / "Downloads"
VAULT_ROOT = DOCS_ROOT / "EMERAULD"
RAW_DIR = VAULT_ROOT / "raw"
RAW_SOURCES_DIR = VAULT_ROOT / "raw sources"
WIKI_DIR = VAULT_ROOT / "wiki"
WIKI_RAW_SOURCES_DIR = WIKI_DIR / "raw-sources"
SOURCE_NOTES_DIR = WIKI_DIR / "source-notes"
MANIFEST_PATH = RAW_DIR / ".intake-manifest.jsonl"
SCAN_LABEL = "c-documents-downloads-full-recursive-2026-07-14"
RUN_DATE = "2026-07-14"


ELIGIBLE_EXTS = {
    ".md",
    ".txt",
    ".pdf",
    ".doc",
    ".docx",
    ".odt",
    ".rtf",
    ".html",
    ".htm",
    ".json",
    ".csv",
    ".tsv",
    ".zip",
    ".7z",
    ".ged",
    ".svg",
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
}

UNSAFE_EXTS = {
    ".p8",
    ".der",
    ".pem",
    ".key",
    ".crt",
    ".cer",
    ".exe",
    ".msi",
    ".apk",
    ".aab",
    ".ipa",
    ".dll",
    ".bin",
    ".mp3",
    ".mp4",
    ".mov",
    ".wav",
}

SKIP_DIR_NAMES = {
    ".git",
    ".cache",
    ".venv",
    "venv",
    "env",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
    ".wrangler",
    ".smart-env",
    ".graph_store",
    ".obsidian",
    "graphify-out",
    "tmp",
}

UNSAFE_NAME_RE = re.compile(
    r"(authkey|subscriptionkey|api[_-]?key|anthropic_api_key|openai_api_key|secret|token|password|passwd|pass\.txt|certificate|cert|licensecopy)",
    re.IGNORECASE,
)

CANONICAL_DOCUMENTS_FILES = {
    "CLIENT ACCOUNTS TRACKER.md",
    "MASTER TRACKER (recreated from MASTER PACK 4).md",
    "PHAROS-AI CHANGE TRACKER.md",
    "METHOD TRACKER.md",
    "MARTIN-SITE CHANGE TRACKER.md",
}

PRESERVE_IN_PLACE_ROOTS = {
    DOCS_ROOT / "HERMES Dashboard",
    DOCS_ROOT / "GitHub",
    DOCS_ROOT / "DEV",
    DOCS_ROOT / "PowerShell",
    DOCS_ROOT / "WindowsPowerShell",
    DOCS_ROOT / "grimoire-app",
    DOWNLOADS_ROOT / "montreal-plus-mobile",
    DOWNLOADS_ROOT / "clearday-mobile",
    DOWNLOADS_ROOT / "GAIA",
    DOWNLOADS_ROOT / "Expert LINK",
}


def now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def append_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    if not records:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def load_manifest_hashes() -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    if not MANIFEST_PATH.exists():
        return out
    with MANIFEST_PATH.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            sha = rec.get("sha256")
            if isinstance(sha, str):
                out.setdefault(sha, rec)
    return out


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def rel_to_user(path: Path) -> Path:
    try:
        return path.resolve().relative_to(USER_ROOT.resolve())
    except ValueError:
        return Path(path.name)


def should_skip_dir(path: Path) -> bool:
    name = path.name.lower()
    if name in SKIP_DIR_NAMES:
        return True
    if name.endswith(".egg-info"):
        return True
    return False


def preserve_in_place_reason(path: Path) -> str | None:
    for root in PRESERVE_IN_PLACE_ROOTS:
        if is_relative_to(path, root):
            return "operational_project_audited_in_place"
    return None


def unsafe_reason(path: Path) -> str | None:
    name = path.name
    suffix = path.suffix.lower()
    if suffix in UNSAFE_EXTS:
        return f"unsafe_extension:{suffix}"
    if UNSAFE_NAME_RE.search(name):
        return "unsafe_name"
    if path.parent == DOCS_ROOT and path.name in CANONICAL_DOCUMENTS_FILES:
        return "documents_canonical_tracker_stable_path"
    return None


def eligible_reason(path: Path) -> str | None:
    suffix = path.suffix.lower()
    reason = unsafe_reason(path)
    if reason:
        return reason
    if suffix not in ELIGIBLE_EXTS:
        return f"unsupported_extension:{suffix or '[none]'}"
    try:
        if path.stat().st_size <= 0:
            return "empty_file"
    except OSError as e:
        return f"stat_error:{e}"
    return None


def iter_files(root: Path):
    for current, dirs, files in os.walk(root):
        cur = Path(current)
        dirs[:] = [d for d in dirs if not should_skip_dir(cur / d)]
        for name in files:
            yield cur / name


def unique_destination(target: Path) -> Path:
    if not target.exists():
        return target
    stem = target.stem
    suffix = target.suffix
    i = 2
    while True:
        candidate = target.with_name(f"{stem}--dup{i}{suffix}")
        if not candidate.exists():
            return candidate
        i += 1


def cluster_for(path: Path) -> str:
    text = str(path).lower()
    if any(k in text for k in ("lavoie", "client", "contrat", "facture", "progressionlive")):
        return "client-pharos-lavoie"
    if any(k in text for k in ("pharos", "governance", "ai governance", "law25", "eu ai act", "compass")):
        return "pharos-governance"
    if any(k in text for k in ("paper", "papers", "bibliograph", "journal", "publication", "article", "source pdf", "research")):
        return "research-papers"
    if any(k in text for k in ("agent", "skill", "trismegiste", "henry", "agatha", "vulcan", "phelix", "lotus")):
        return "agents-skills"
    if any(k in text for k in ("genealog", ".ged", "lepage-deschenes")):
        return "genealogy"
    if any(k in text for k in ("app", "mobile", "gaia", "kitab", "montreal-plus", "clearday", "expert link")):
        return "apps-projects"
    if any(k in text for k in ("marketplace", "production-readiness", "network-marketplace", "strategy")):
        return "business-strategy"
    if any(k in text for k in ("raw sources", "raw\\")):
        return "existing-raw-provenance"
    return "misc-operator-notes"


def build_existing_vault_hash_index() -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for root in (RAW_DIR, RAW_SOURCES_DIR):
        if not root.exists():
            continue
        for path in iter_files(root):
            reason = eligible_reason(path)
            if reason and not reason.startswith("unsupported_extension"):
                continue
            try:
                sha = sha256_file(path)
            except OSError:
                continue
            out.setdefault(sha, {"path": str(path), "lane": root.name})
    return out


def build_wiki_text_index() -> str:
    chunks: list[str] = []
    if not WIKI_DIR.exists():
        return ""
    for path in WIKI_DIR.rglob("*.md"):
        try:
            chunks.append(read_text(path).lower())
        except OSError:
            continue
    return "\n".join(chunks)


def audit_existing_raw(wiki_text: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for root in (RAW_DIR, RAW_SOURCES_DIR):
        if not root.exists():
            continue
        for path in iter_files(root):
            reason = eligible_reason(path)
            if reason and not reason.startswith("unsupported_extension"):
                status = "excluded"
            else:
                status = "eligible"
            rel = str(path.relative_to(VAULT_ROOT)).replace("\\", "/")
            stem = path.stem.lower()
            mentioned = rel.lower() in wiki_text or path.name.lower() in wiki_text or stem in wiki_text
            rows.append(
                {
                    "path": str(path),
                    "vault_relative_path": rel,
                    "cluster": cluster_for(path),
                    "status": status,
                    "coverage": "already_represented" if mentioned else "needs_review_or_note",
                    "reason": reason or "",
                    "size_bytes": path.stat().st_size if path.exists() else None,
                    "last_write_time": dt.datetime.fromtimestamp(path.stat().st_mtime).isoformat()
                    if path.exists()
                    else None,
                }
            )
    return rows


def scan_candidates(
    manifest_hashes: dict[str, dict[str, Any]], vault_hashes: dict[str, dict[str, Any]]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    candidates: list[dict[str, Any]] = []
    excluded: list[dict[str, Any]] = []
    seen_hashes = set(manifest_hashes) | set(vault_hashes)
    roots = [DOCS_ROOT, DOWNLOADS_ROOT]

    for root in roots:
        for path in iter_files(root):
            resolved = path.resolve()
            in_vault = is_relative_to(resolved, VAULT_ROOT)
            in_raw_lane = is_relative_to(resolved, RAW_DIR) or is_relative_to(resolved, RAW_SOURCES_DIR)
            in_wiki_raw_notes = is_relative_to(resolved, WIKI_RAW_SOURCES_DIR)
            if in_vault and not (in_raw_lane or in_wiki_raw_notes):
                excluded.append({"path": str(path), "reason": "existing_vault_non_raw_content"})
                continue
            if in_raw_lane:
                excluded.append({"path": str(path), "reason": "existing_raw_lane_audited_in_place"})
                continue
            if in_wiki_raw_notes:
                excluded.append({"path": str(path), "reason": "wiki_raw_source_note_promoted_separately"})
                continue
            preserve_reason = preserve_in_place_reason(resolved)
            if preserve_reason:
                excluded.append({"path": str(path), "reason": preserve_reason})
                continue

            reason = eligible_reason(path)
            if reason:
                excluded.append({"path": str(path), "reason": reason})
                continue

            try:
                sha = sha256_file(path)
                size = path.stat().st_size
            except OSError as e:
                excluded.append({"path": str(path), "reason": f"read_or_hash_error:{e}"})
                continue

            if sha in manifest_hashes:
                excluded.append(
                    {
                        "path": str(path),
                        "reason": "duplicate_hash_in_manifest",
                        "duplicate_of": manifest_hashes[sha].get("raw_path")
                        or manifest_hashes[sha].get("source_path"),
                    }
                )
                continue
            if sha in vault_hashes:
                excluded.append(
                    {
                        "path": str(path),
                        "reason": "duplicate_hash_in_existing_vault_raw_lane",
                        "duplicate_of": vault_hashes[sha]["path"],
                    }
                )
                continue
            if sha in seen_hashes:
                excluded.append({"path": str(path), "reason": "duplicate_hash_in_current_scan"})
                continue
            seen_hashes.add(sha)

            target = unique_destination(RAW_DIR / SCAN_LABEL / rel_to_user(path))
            candidates.append(
                {
                    "source_path": str(path),
                    "raw_path": str(target),
                    "file_name": path.name,
                    "source_relative_path": str(rel_to_user(path)).replace("\\", "/"),
                    "cluster": cluster_for(path),
                    "size_bytes": size,
                    "sha256": sha,
                    "source_label": SCAN_LABEL,
                    "verified_at_utc": now_utc(),
                    "verification": {
                        "exists": True,
                        "is_file": True,
                        "readable": True,
                        "non_empty": True,
                        "duplicate": False,
                    },
                }
            )
    return candidates, excluded


def move_candidates(candidates: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    moved: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    for rec in candidates:
        src = Path(rec["source_path"])
        dst = Path(rec["raw_path"])
        if not src.exists():
            bad = dict(rec)
            bad["reason"] = "missing_at_move_time"
            rejected.append(bad)
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        try:
            shutil.move(str(src), str(dst))
        except OSError as e:
            bad = dict(rec)
            bad["reason"] = f"move_error:{e}"
            rejected.append(bad)
            continue
        rec = dict(rec)
        rec["moved_at_utc"] = now_utc()
        moved.append(rec)
    return moved, rejected


def topic_for_source_note(name: str) -> str:
    lower = name.lower()
    if any(k in lower for k in ("patent", "pharos", "brain paper", "recruso", "skills as self")):
        return "pharos-ip-manuscript"
    if any(k in lower for k in ("healthcare", "recruiting", "agent operations", "agent architecture")):
        return "governance-platform-signals"
    if any(k in lower for k in ("ballad", "mia papers", "gaga", "alchimie")):
        return "cultural-lyric-corpus"
    if any(k in lower for k in ("dg", "sante-france", "stop coding", "lost-loop", "reflexive")):
        return "operator-continuity"
    return "misc-source-notes"


def add_or_update_frontmatter(text: str, old_rel: str, moved_at: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            fm = text[4:end]
            body = text[end + 5 :]
            lines = fm.splitlines()
            keys = {line.split(":", 1)[0].strip() for line in lines if ":" in line}
            if "previous_wiki_path" not in keys:
                lines.append(f'previous_wiki_path: "{old_rel}"')
            if "promoted_at" not in keys:
                lines.append(f'promoted_at: "{moved_at}"')
            if "promoted_reason" not in keys:
                lines.append('promoted_reason: "already-ingested source note moved out of raw-sources lane"')
            return "---\n" + "\n".join(lines) + "\n---\n" + body
    return (
        "---\n"
        "type: source-note\n"
        f'previous_wiki_path: "{old_rel}"\n'
        f'promoted_at: "{moved_at}"\n'
        'promoted_reason: "already-ingested source note moved out of raw-sources lane"\n'
        "---\n\n"
        + text
    )


def promote_source_notes(apply: bool) -> list[dict[str, Any]]:
    moves: list[dict[str, Any]] = []
    if not WIKI_RAW_SOURCES_DIR.exists():
        return moves
    for src in sorted(WIKI_RAW_SOURCES_DIR.rglob("*.md")):
        topic = topic_for_source_note(src.name)
        dst = unique_destination(SOURCE_NOTES_DIR / topic / src.name)
        old_rel = str(src.relative_to(WIKI_DIR)).replace("\\", "/")
        new_rel = str(dst.relative_to(WIKI_DIR)).replace("\\", "/")
        moves.append({"old_path": str(src), "new_path": str(dst), "old_wiki_path": old_rel, "new_wiki_path": new_rel, "topic": topic})
        if apply:
            text = read_text(src)
            text = add_or_update_frontmatter(text, old_rel, now_utc())
            write_text(dst, text)
            src.unlink()
    if apply and moves:
        update_wikilinks_for_moves(moves)
    return moves


def update_wikilinks_for_moves(moves: list[dict[str, Any]]) -> None:
    replacements: list[tuple[str, str]] = []
    for move in moves:
        old = move["old_wiki_path"]
        new = move["new_wiki_path"]
        old_no_ext = old[:-3] if old.endswith(".md") else old
        new_no_ext = new[:-3] if new.endswith(".md") else new
        replacements.extend(
            [
                (f"[[{old}]]", f"[[{new_no_ext}]]"),
                (f"[[{old_no_ext}]]", f"[[{new_no_ext}]]"),
            ]
        )
    for path in WIKI_DIR.rglob("*.md"):
        try:
            text = read_text(path)
        except OSError:
            continue
        new_text = text
        for old, new in replacements:
            new_text = new_text.replace(old, new)
        if new_text != text:
            write_text(path, new_text)


def summarize_counts(records: list[dict[str, Any]], key: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for rec in records:
        value = str(rec.get(key, "unknown"))
        counts[value] = counts.get(value, 0) + 1
    return dict(sorted(counts.items()))


def write_report(
    apply: bool,
    candidates: list[dict[str, Any]],
    excluded: list[dict[str, Any]],
    raw_audit: list[dict[str, Any]],
    source_note_moves: list[dict[str, Any]],
    moved: list[dict[str, Any]] | None = None,
    move_rejected: list[dict[str, Any]] | None = None,
) -> Path:
    report = {
        "run_at_utc": now_utc(),
        "source_label": SCAN_LABEL,
        "dry_run": not apply,
        "roots": [str(DOCS_ROOT), str(DOWNLOADS_ROOT)],
        "raw_dir": str(RAW_DIR / SCAN_LABEL),
        "counts": {
            "verified_external_candidates": len(candidates),
            "excluded_or_deferred": len(excluded),
            "existing_raw_lane_audited": len(raw_audit),
            "source_notes_to_promote": len(source_note_moves),
            "moved_external": len(moved or []),
            "move_rejected": len(move_rejected or []),
        },
        "external_candidate_clusters": summarize_counts(candidates, "cluster"),
        "excluded_reasons": summarize_counts(excluded, "reason"),
        "raw_lane_coverage": summarize_counts(raw_audit, "coverage"),
        "raw_lane_clusters": summarize_counts(raw_audit, "cluster"),
        "source_note_topics": summarize_counts(source_note_moves, "topic"),
        "verified_external_candidates": candidates,
        "excluded_or_deferred": excluded,
        "existing_raw_lane_audit": raw_audit,
        "source_note_moves": source_note_moves,
        "moved_external": moved or [],
        "move_rejected": move_rejected or [],
    }
    suffix = "apply" if apply else "dryrun"
    path = RAW_DIR / f"intake-report-{SCAN_LABEL}-{suffix}.json"
    write_text(path, json.dumps(report, ensure_ascii=False, indent=2))
    return path


def wiki_link_for(path: str) -> str:
    p = Path(path)
    try:
        rel = p.relative_to(WIKI_DIR)
        s = str(rel.with_suffix("")).replace("\\", "/")
        return f"[[{s}]]"
    except ValueError:
        return f"`{path}`"


def create_cluster_notes(
    report_path: Path,
    candidates: list[dict[str, Any]],
    raw_audit: list[dict[str, Any]],
    moves: list[dict[str, Any]],
    moved: list[dict[str, Any]],
) -> list[Path]:
    created: list[Path] = []
    cluster_dir = WIKI_DIR / "intake" / RUN_DATE
    report_rel = str(report_path.relative_to(VAULT_ROOT)).replace("\\", "/")

    by_cluster: dict[str, list[dict[str, Any]]] = {}
    for rec in moved or candidates:
        by_cluster.setdefault(rec["cluster"], []).append(rec)

    overview_lines = [
        "---",
        "type: intake-cluster-map",
        "status: active",
        f"created: {RUN_DATE}",
        f"source_label: {SCAN_LABEL}",
        "---",
        "",
        f"# Full Recursive Intake Cluster Map - {RUN_DATE}",
        "",
        "## Verification",
        f"- Report: `{report_rel}`",
        f"- External verified candidates: {len(candidates)}",
        f"- External moved in this run: {len(moved)}",
        f"- Existing raw/raw sources audited in place: {len(raw_audit)}",
        f"- Source notes promoted from `wiki/raw-sources/`: {len(moves)}",
        "",
        "## Cluster Registers",
    ]
    for cluster in sorted(by_cluster):
        title = f"Full Recursive Intake - {cluster} - Source Register"
        overview_lines.append(f"- [[intake/{RUN_DATE}/{title}]]")
        lines = [
            "---",
            "type: source-register",
            "status: active",
            f"created: {RUN_DATE}",
            f"source_label: {SCAN_LABEL}",
            f"cluster: {cluster}",
            "---",
            "",
            f"# {title}",
            "",
            "## Verified Sources",
        ]
        for rec in sorted(by_cluster[cluster], key=lambda r: r["source_relative_path"].lower()):
            raw_rel = str(Path(rec["raw_path"]).relative_to(VAULT_ROOT)).replace("\\", "/")
            lines.append(
                f"- `{rec['source_relative_path']}` -> `{raw_rel}` (`{rec['sha256'][:12]}`, {rec['size_bytes']} bytes)"
            )
        lines.extend(
            [
                "",
                "## Related",
                "- [[Full Recursive Intake Cluster Map - 2026-07-14]]",
                "- [[Research and Papers MOC]]",
                "- [[Governance and PHAROS MOC]]",
            ]
        )
        path = cluster_dir / f"{title}.md"
        write_text(path, "\n".join(lines) + "\n")
        created.append(path)

    raw_lines = [
        "---",
        "type: raw-lane-audit",
        "status: active",
        f"created: {RUN_DATE}",
        f"source_label: {SCAN_LABEL}",
        "---",
        "",
        f"# EMERAULD Raw Lane Coverage Audit - {RUN_DATE}",
        "",
        "## Summary",
        f"- Audited raw/raw sources files: {len(raw_audit)}",
        "- Existing raw artifacts were audited in place, not repacked.",
        "- `already_represented` means the file path, filename, or stem appears in current wiki text.",
        "",
        "## Coverage Counts",
    ]
    for key, value in summarize_counts(raw_audit, "coverage").items():
        raw_lines.append(f"- `{key}`: {value}")
    raw_lines.extend(["", "## Cluster Counts"])
    for key, value in summarize_counts(raw_audit, "cluster").items():
        raw_lines.append(f"- `{key}`: {value}")
    raw_lines.extend(["", "## Needs Review Samples"])
    for rec in [r for r in raw_audit if r["coverage"] == "needs_review_or_note"][:100]:
        raw_lines.append(f"- `{rec['vault_relative_path']}` ({rec['cluster']})")
    raw_lines.extend(["", "## Related", "- [[Full Recursive Intake Cluster Map - 2026-07-14]]"])
    raw_path = cluster_dir / "EMERAULD Raw Lane Coverage Audit - 2026-07-14.md"
    write_text(raw_path, "\n".join(raw_lines) + "\n")
    created.append(raw_path)

    overview_lines.extend(
        [
            "- [[intake/2026-07-14/EMERAULD Raw Lane Coverage Audit - 2026-07-14]]",
            "",
            "## Promoted Source Notes",
        ]
    )
    for move in sorted(moves, key=lambda m: m["new_wiki_path"]):
        overview_lines.append(f"- {wiki_link_for(move['new_path'])} (from `{move['old_wiki_path']}`)")
    overview_lines.extend(
        [
            "",
            "## Related",
            "- [[Research and Papers MOC]]",
            "- [[Governance and PHAROS MOC]]",
            "- [[VAULT ADDITIONS TRACKER]]",
        ]
    )
    overview_path = cluster_dir / "Full Recursive Intake Cluster Map - 2026-07-14.md"
    write_text(overview_path, "\n".join(overview_lines) + "\n")
    created.append(overview_path)
    return created


def append_tracker_entry(created_paths: list[Path], moved_count: int, raw_count: int, promoted_count: int) -> None:
    entry = (
        f"- {RUN_DATE} — **Full recursive Documents/Downloads + EMERAULD raw-lane intake:** "
        f"Scanned all subfolders under `C:\\Users\\softinfo\\Documents` and `C:\\Users\\softinfo\\Downloads`, "
        f"including `raw/` and `raw sources/`. Hard-moved {moved_count} verified non-duplicate external source artifacts "
        f"into `raw/{SCAN_LABEL}/`, audited {raw_count} existing raw/raw-source artifacts in place, and promoted "
        f"{promoted_count} already-ingested source notes out of `wiki/raw-sources/` into `wiki/source-notes/`. "
        f"Cluster map: [[intake/{RUN_DATE}/Full Recursive Intake Cluster Map - 2026-07-14]].\n"
    )
    for tracker in (WIKI_DIR / "VAULT ADDITIONS TRACKER.md", VAULT_ROOT / "_vault" / "VAULT ADDITIONS TRACKER.md"):
        if tracker.exists():
            text = read_text(tracker)
            if "Full recursive Documents/Downloads + EMERAULD raw-lane intake" not in text:
                if text.startswith("---\n"):
                    end = text.find("\n---\n", 4)
                    if end != -1:
                        insert_at = end + len("\n---\n")
                        text = text[:insert_at] + "\n" + entry + text[insert_at:]
                    else:
                        text = entry + text
                elif "\n---\n" in text:
                    insert_at = text.find("\n---\n") + len("\n---\n")
                    text = text[:insert_at] + "\n" + entry + text[insert_at:]
                else:
                    text = entry + text
                write_text(tracker, text)


def append_session_state(moved_count: int, raw_count: int, promoted_count: int, report_path: Path) -> None:
    path = VAULT_ROOT / "session-state.md"
    if not path.exists():
        return
    marker = "Full recursive Documents/Downloads + EMERAULD raw-lane intake"
    text = read_text(path)
    if marker in text:
        return
    report_rel = str(report_path.relative_to(VAULT_ROOT)).replace("\\", "/")
    note = (
        "\n"
        f"## {RUN_DATE} - {marker}\n\n"
        f"- Hard-moved {moved_count} verified non-duplicate external source artifacts into `raw/{SCAN_LABEL}/`.\n"
        f"- Audited {raw_count} existing files in `raw/` and `raw sources/` in place.\n"
        f"- Promoted {promoted_count} already-ingested source notes from `wiki/raw-sources/` to `wiki/source-notes/`.\n"
        f"- Report: `{report_rel}`.\n"
        f"- Cluster map: [[intake/{RUN_DATE}/Full Recursive Intake Cluster Map - 2026-07-14]].\n"
    )
    write_text(path, text.rstrip() + "\n" + note)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Perform moves and write wiki notes.")
    args = parser.parse_args()

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    manifest_hashes = load_manifest_hashes()
    vault_hashes = build_existing_vault_hash_index()
    wiki_text = build_wiki_text_index()
    raw_audit = audit_existing_raw(wiki_text)
    candidates, excluded = scan_candidates(manifest_hashes, vault_hashes)
    source_note_moves = promote_source_notes(apply=args.apply)

    moved: list[dict[str, Any]] = []
    move_rejected: list[dict[str, Any]] = []
    if args.apply:
        moved, move_rejected = move_candidates(candidates)
        append_jsonl(MANIFEST_PATH, moved)

    report_path = write_report(
        args.apply,
        candidates,
        excluded,
        raw_audit,
        source_note_moves,
        moved=moved,
        move_rejected=move_rejected,
    )

    if args.apply:
        created = create_cluster_notes(report_path, candidates, raw_audit, source_note_moves, moved)
        append_tracker_entry(created, len(moved), len(raw_audit), len(source_note_moves))
        append_session_state(len(moved), len(raw_audit), len(source_note_moves), report_path)

    print(
        json.dumps(
            {
                "dry_run": not args.apply,
                "verified_external_candidates": len(candidates),
                "excluded_or_deferred": len(excluded),
                "existing_raw_lane_audited": len(raw_audit),
                "source_notes_to_promote": len(source_note_moves),
                "moved_external": len(moved),
                "move_rejected": len(move_rejected),
                "report": str(report_path),
            },
            ensure_ascii=False,
        )
    )
    return 1 if move_rejected else 0


if __name__ == "__main__":
    raise SystemExit(main())
