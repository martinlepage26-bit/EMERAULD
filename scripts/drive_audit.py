#!/usr/bin/env python3
"""
Catalogue Google Drive-for-Desktop roots and compare topical documents against
local C: and WSL content.

Outputs are written to:
    tmp/drive-audit-YYYY-MM-DD/

This script is intentionally conservative:
- it inventories Drive via PowerShell so streamed Drive letters remain readable
- it avoids hashing streamed Drive content
- it uses heuristic duplicate and paper-gap detection, not destructive actions
"""

from __future__ import annotations

import argparse
import base64
import csv
import json
import os
import re
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_ROOT = REPO_ROOT / "tmp" / f"drive-audit-{datetime.now().strftime('%Y-%m-%d')}"
POWERSHELL = Path("/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe")

DRIVE_ROOTS = {
    "drive_g_martinlepage26_me_com": r"G:\Mon disque",
    "drive_f_secondary": r"F:\Mon disque",
}

C_SCAN_ROOTS = [
    Path("/mnt/c/Users/softinfo/Documents"),
    Path("/mnt/c/Users/softinfo/Desktop"),
    Path("/mnt/c/Users/softinfo/Downloads"),
]

WSL_SCAN_ROOTS = [
    Path("/home/cerebrhoe/manuscripts"),
    Path("/home/cerebrhoe/governance-project"),
    Path("/home/cerebrhoe/PHAROS-SUITE"),
    Path("/home/cerebrhoe/obsidian-agent-vault"),
    Path("/home/cerebrhoe/output"),
    Path("/home/cerebrhoe/Downloads"),
    Path("/home/cerebrhoe/Desktop/CODEX"),
]

LOCAL_SKIP_DIRS = {
    ".git",
    ".claude",
    ".codex",
    ".cache",
    ".npm",
    ".cargo",
    ".venv",
    "node_modules",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    ".smart-env",
    ".vector_store",
    ".lightrag",
    ".obsidian",
    ".progress",
    ".local",
    ".config",
    "AppData",
    ".vscode",
    ".azure",
    ".bun",
    "snap",
}

DOC_EXTS = {
    ".gdoc",
    ".gsheet",
    ".gslides",
    ".doc",
    ".docx",
    ".pdf",
    ".md",
    ".txt",
    ".odt",
    ".rtf",
    ".html",
    ".htm",
    ".ppt",
    ".pptx",
}

TOPIC_KEYWORDS = {
    "pharos": ["pharos", "hermes", "argus", "queen keyport", "hephaistos", "govern-ai"],
    "ai_governance": [
        "ai governance",
        "governance",
        "audit",
        "model card",
        "responsible ai",
        "ethics",
        "transparency",
        "ex libris",
        "diagnostic",
    ],
    "cv_resume": ["cv", "resume", "resumes", "bio", "cover", "letter", "cisco", "hireable"],
    "research_paper": [
        "paper",
        "article",
        "chapter",
        "reviewer",
        "bibliography",
        "submission",
        "abstract",
        "journal",
        "manuscript",
        "proposal",
        "dissertation",
        "sociologie",
        "social compass",
        "astrology",
        "governance by denial",
        "sealed card",
    ],
}

PAPER_MANUSCRIPT_HINTS = {
    "paper",
    "article",
    "chapter",
    "manuscript",
    "submission",
    "journal",
    "draft",
    "rev",
    "revised",
    "final",
    "reviewer",
    "bibliography",
    "response",
    "proposal",
    "abstract",
}

OFFICIAL_PAPER_COMPANIONS = {
    "manuscript": ["paper", "article", "chapter", "manuscript", "draft", "submission"],
    "abstract_or_proposal": ["abstract", "proposal", "summary"],
    "references": ["bibliography", "reference", "references", "citations"],
    "review_cycle": ["reviewer", "response", "comments", "evaluateur", "tracked", "highlighted"],
    "final_delivery": ["final", "clean", "pdf", "submission", "journal"],
    "cover_letter": ["cover", "lettre", "letter"],
}

OFFICIAL_PAPER_EXCLUDE_NAMES = {
    "desktop.ini",
    ".ds_store",
    "readme",
    "skill",
    "skill md",
    "requirements",
    "release checklist",
    "template",
    "redraft",
}

OFFICIAL_PAPER_ALLOWED_EXTS = {".doc", ".docx", ".gdoc", ".pdf", ".odt", ".md", ".txt"}


@dataclass
class FileRecord:
    source: str
    root: str
    path: str
    name: str
    ext: str
    is_dir: bool
    size: int
    modified: str
    topic: str = "other"
    normalized_stem: str = ""


def ensure_output_root() -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)


def run_powershell_json(script: str) -> list[dict]:
    cmd = [str(POWERSHELL), "-NoProfile", "-Command", script]
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if proc.returncode != 0:
        raise RuntimeError(f"PowerShell failed:\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}")
    text = proc.stdout.strip()
    if not text:
        return []
    return json.loads(text)


def run_powershell_text(script: str) -> str:
    cmd = [str(POWERSHELL), "-NoProfile", "-Command", script]
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if proc.returncode != 0:
        raise RuntimeError(f"PowerShell failed:\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}")
    return proc.stdout


def inventory_windows_root(label: str, root: str) -> list[FileRecord]:
    ps_script = rf"""
$items = Get-ChildItem '{root}' -Recurse -Force -ErrorAction SilentlyContinue
foreach ($item in $items) {{
  $safePath = [regex]::Replace($item.FullName, '[\x00-\x1F]', '')
  $safeName = [regex]::Replace($item.Name, '[\x00-\x1F]', '')
  $ext = if ($item.PSIsContainer) {{ '' }} else {{ $item.Extension }}
  $modified = try {{ $item.LastWriteTime.ToString('o') }} catch {{ '' }}
  $fields = @(
    [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($safePath)),
    [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($safeName)),
    [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($ext)),
    $(if ($item.PSIsContainer) {{ '1' }} else {{ '0' }}),
    $(if ($item.PSIsContainer) {{ '0' }} else {{ [string][int64]$item.Length }}),
    [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($modified))
  )
  [Console]::Out.WriteLine(($fields -join "`t"))
}}
"""
    text = run_powershell_text(ps_script)
    records: list[FileRecord] = []
    for line in text.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) != 6:
            continue
        path_b64, name_b64, ext_b64, is_dir_raw, size_raw, modified_b64 = parts
        path = base64.b64decode(path_b64).decode("utf-8", errors="replace")
        name = base64.b64decode(name_b64).decode("utf-8", errors="replace")
        ext = base64.b64decode(ext_b64).decode("utf-8", errors="replace")
        modified = base64.b64decode(modified_b64).decode("utf-8", errors="replace")
        records.append(
            FileRecord(
                source="drive",
                root=root,
                path=path,
                name=name,
                ext=(ext or "").lower(),
                is_dir=is_dir_raw == "1",
                size=int(size_raw or 0),
                modified=modified,
            )
        )
    for rec in records:
        enrich_record(rec)
    write_csv(OUTPUT_ROOT / f"{label}.csv", records)
    return records


def inventory_local_root(label: str, root: Path) -> list[FileRecord]:
    records: list[FileRecord] = []
    if not root.exists():
        return records
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in LOCAL_SKIP_DIRS]
        current = Path(dirpath)
        for dirname in dirnames:
            path = current / dirname
            records.append(
                FileRecord(
                    source="local",
                    root=str(root),
                    path=str(path),
                    name=dirname,
                    ext="",
                    is_dir=True,
                    size=0,
                    modified=iso_from_stat(path),
                )
            )
        for filename in filenames:
            path = current / filename
            ext = path.suffix.lower()
            if ext not in DOC_EXTS:
                continue
            try:
                stat = path.stat()
            except OSError:
                continue
            records.append(
                FileRecord(
                    source="local",
                    root=str(root),
                    path=str(path),
                    name=filename,
                    ext=ext,
                    is_dir=False,
                    size=int(stat.st_size),
                    modified=iso_from_timestamp(stat.st_mtime),
                )
            )
    for rec in records:
        enrich_record(rec)
    write_csv(OUTPUT_ROOT / f"{label}.csv", records)
    return records


def iso_from_stat(path: Path) -> str:
    try:
        return iso_from_timestamp(path.stat().st_mtime)
    except OSError:
        return ""


def iso_from_timestamp(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).astimezone().isoformat()


def strip_accents(text: str) -> str:
    norm = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in norm if not unicodedata.combining(ch))


def normalize_search_text(text: str) -> str:
    text = strip_accents(text).lower()
    text = text.replace("&", " and ")
    text = re.sub(r"[_\-]+", " ", text)
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def normalize_stem(name: str) -> str:
    stem = normalize_search_text(Path(name).stem)
    stem = re.sub(r"\b(copie de|copy of|copy)\b", " ", stem)
    stem = re.sub(r"\(\d+\)", " ", stem)
    stem = re.sub(r"\b(v\d+|rev\d*|revised|tracked|clean|highlighted|final|draft|submission|reviewed)\b", " ", stem)
    stem = re.sub(r"\s+", " ", stem).strip()
    return stem


def classify_topic(path: str, name: str) -> str:
    hay = normalize_search_text(f"{path} {name}")
    for topic, keywords in TOPIC_KEYWORDS.items():
        for keyword in keywords:
            needle = normalize_search_text(keyword)
            if re.search(rf"(?<!\w){re.escape(needle)}(?!\w)", hay):
                return topic
    return "other"


def enrich_record(record: FileRecord) -> None:
    record.topic = classify_topic(record.path, record.name)
    record.normalized_stem = normalize_stem(record.name)


def write_csv(path: Path, records: Iterable[FileRecord | dict]) -> None:
    rows: list[dict] = []
    for rec in records:
        if isinstance(rec, FileRecord):
            rows.append(
                {
                    "source": rec.source,
                    "root": rec.root,
                    "path": rec.path,
                    "name": rec.name,
                    "ext": rec.ext,
                    "is_dir": rec.is_dir,
                    "size": rec.size,
                    "modified": rec.modified,
                    "topic": rec.topic,
                    "normalized_stem": rec.normalized_stem,
                }
            )
        else:
            rows.append(rec)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def read_records_csv(path: Path) -> list[FileRecord]:
    records: list[FileRecord] = []
    if not path.exists():
        return records
    with path.open(encoding="utf-8", errors="replace", newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            records.append(
                FileRecord(
                    source=row["source"],
                    root=row["root"],
                    path=row["path"],
                    name=row["name"],
                    ext=(row.get("ext") or "").lower(),
                    is_dir=str(row.get("is_dir", "")).lower() in {"1", "true", "yes"},
                    size=int(row.get("size") or 0),
                    modified=row.get("modified") or "",
                    topic=row.get("topic") or "other",
                    normalized_stem=row.get("normalized_stem") or "",
                )
            )
    return records


def top_level_rollup(records: list[FileRecord]) -> list[dict]:
    files = [r for r in records if not r.is_dir]
    buckets: dict[str, list[FileRecord]] = defaultdict(list)
    for rec in files:
        relative = rec.path.replace(rec.root, "", 1).lstrip("\\/")
        top = relative.split("\\")[0].split("/")[0] if relative else "[root]"
        buckets[top].append(rec)
    rows = []
    for top, items in buckets.items():
        rows.append(
            {
                "folder": top,
                "files": len(items),
                "bytes": sum(r.size for r in items),
                "latest_modified": max((r.modified for r in items), default=""),
            }
        )
    rows.sort(key=lambda row: row["bytes"], reverse=True)
    return rows


def extension_rollup(records: list[FileRecord]) -> list[dict]:
    files = [r for r in records if not r.is_dir]
    counter = Counter(r.ext or "[none]" for r in files)
    return [{"extension": ext, "count": count} for ext, count in counter.most_common()]


def large_file_candidates(records: list[FileRecord], min_bytes: int = 100 * 1024 * 1024) -> list[dict]:
    rows = []
    for rec in records:
        if rec.is_dir or rec.size < min_bytes:
            continue
        reason = "large_file"
        if rec.ext in {".avi", ".mkv", ".mov"}:
            reason = "large_media"
        rows.append(
            {
                "source": rec.source,
                "path": rec.path,
                "size_bytes": rec.size,
                "size_mb": round(rec.size / (1024 * 1024), 1),
                "modified": rec.modified,
                "reason": reason,
                "topic": rec.topic,
            }
        )
    rows.sort(key=lambda row: row["size_bytes"], reverse=True)
    return rows


def duplicate_candidates(records: list[FileRecord]) -> list[dict]:
    files = [r for r in records if not r.is_dir]
    rows: list[dict] = []

    by_name: dict[tuple[str, int, str], list[FileRecord]] = defaultdict(list)
    by_norm: dict[tuple[str, str], list[FileRecord]] = defaultdict(list)
    for rec in files:
        by_name[(rec.name.lower(), rec.size, rec.ext)].append(rec)
        by_norm[(rec.normalized_stem, rec.ext)].append(rec)

    seen = set()
    for key, items in by_name.items():
        if len(items) < 2:
            continue
        group_id = ("exact_name_size",) + key
        if group_id in seen:
            continue
        seen.add(group_id)
        rows.append(
            {
                "candidate_type": "exact_name_size",
                "key": f"{key[0]} | {key[1]} | {key[2]}",
                "count": len(items),
                "paths": " || ".join(r.path for r in items),
                "reason": "Same filename, size, and extension in multiple locations.",
            }
        )

    for key, items in by_norm.items():
        if len(items) < 2 or not key[0]:
            continue
        copyish = [r for r in items if re.search(r"\(\d+\)|copy|copie de", r.name, re.IGNORECASE)]
        if not copyish:
            continue
        rows.append(
            {
                "candidate_type": "copy_variant",
                "key": f"{key[0]} | {key[1]}",
                "count": len(items),
                "paths": " || ".join(r.path for r in items),
                "reason": "Copy-number or copy-of naming suggests redundant versions to review.",
            }
        )

    junk = [r for r in files if r.name.lower() in {"desktop.ini", ".ds_store"} or r.ext in {".télécharger", ".download"}]
    for rec in junk:
        rows.append(
            {
                "candidate_type": "cleanup_artifact",
                "key": rec.name,
                "count": 1,
                "paths": rec.path,
                "reason": "System or partial-download artifact; usually safe to review for deletion.",
            }
        )

    rows.sort(key=lambda row: (row["candidate_type"], -row["count"], row["key"]))
    return rows


def collect_topic_records(records: list[FileRecord]) -> list[FileRecord]:
    return [r for r in records if not r.is_dir and r.topic != "other" and r.ext in DOC_EXTS]


def topic_comparison(drive_records: list[FileRecord], local_records: list[FileRecord]) -> tuple[list[dict], list[dict]]:
    drive_topics = collect_topic_records(drive_records)
    local_topics = collect_topic_records(local_records)

    drive_keys = defaultdict(list)
    local_keys = defaultdict(list)
    for rec in drive_topics:
        drive_keys[(rec.topic, rec.normalized_stem)].append(rec)
    for rec in local_topics:
        local_keys[(rec.topic, rec.normalized_stem)].append(rec)

    missing_on_drive = []
    drive_only = []

    for key, items in local_keys.items():
        if key not in drive_keys and key[1]:
            sample = items[0]
            missing_on_drive.append(
                {
                    "topic": key[0],
                    "normalized_stem": key[1],
                    "local_paths": " || ".join(r.path for r in items[:5]),
                    "drive_match": "",
                    "reason": "Topical local file has no matching normalized stem on scanned Drive roots.",
                }
            )

    for key, items in drive_keys.items():
        if key not in local_keys and key[1]:
            sample = items[0]
            drive_only.append(
                {
                    "topic": key[0],
                    "normalized_stem": key[1],
                    "drive_paths": " || ".join(r.path for r in items[:5]),
                    "local_match": "",
                    "reason": "Topical Drive file has no matching normalized stem in scanned local paths.",
                }
            )

    missing_on_drive.sort(key=lambda row: (row["topic"], row["normalized_stem"]))
    drive_only.sort(key=lambda row: (row["topic"], row["normalized_stem"]))
    return missing_on_drive, drive_only


def likely_official_paper(record: FileRecord) -> bool:
    if record.is_dir:
        return False
    if record.ext not in OFFICIAL_PAPER_ALLOWED_EXTS:
        return False
    if record.topic not in {"research_paper", "ai_governance", "pharos"}:
        return False
    hay = strip_accents(f"{record.path} {record.name}").lower()
    stem = record.normalized_stem
    if stem in OFFICIAL_PAPER_EXCLUDE_NAMES:
        return False
    if any(part in hay for part in ["/skills/", "\\skills\\", "desktop.ini", "requirements.txt"]):
        return False
    if record.ext in {".md", ".txt"} and not any(part in hay for part in ["paper", "article", "chapter", "manuscript", "submission", "journal", "reviewer", "bibliography", "governance by denial", "sealed card", "voodoo", "socialcompass", "pharos_invention_disclosure", "ai anxiety"]):
        return False
    return any(hint in hay for hint in PAPER_MANUSCRIPT_HINTS)


def paper_cluster_key(record: FileRecord) -> str:
    stem = record.normalized_stem
    stem = re.sub(
        r"\b(abstract|proposal|bibliography|references?|reviewer|response|comments|cover|letter|tracked|clean|highlighted|final|submission|journal|pdf)\b",
        " ",
        stem,
    )
    stem = re.sub(r"\s+", " ", stem).strip()
    return stem or record.normalized_stem


def official_paper_gaps(records: list[FileRecord]) -> list[dict]:
    candidates = [r for r in records if likely_official_paper(r)]
    clusters: dict[str, list[FileRecord]] = defaultdict(list)
    for rec in candidates:
        clusters[paper_cluster_key(rec)].append(rec)

    rows = []
    for cluster, items in clusters.items():
        if not cluster or len(items) < 2:
            continue
        haystack = " ".join(strip_accents(f"{r.path} {r.name}").lower() for r in items)
        present = {}
        missing = []
        for bucket, hints in OFFICIAL_PAPER_COMPANIONS.items():
            has_bucket = any(hint in haystack for hint in hints)
            present[bucket] = has_bucket
            if not has_bucket and bucket != "manuscript":
                missing.append(bucket)
        if not present["manuscript"]:
            continue
        if not missing:
            continue
        rows.append(
            {
                "cluster": cluster,
                "files_in_cluster": len(items),
                "sample_files": " || ".join(r.name for r in items[:6]),
                "missing_companions": ", ".join(missing),
                "reason": "Cluster looks like an official-paper package but lacks common companion artifacts.",
            }
        )
    rows.sort(key=lambda row: (-row["files_in_cluster"], row["cluster"]))
    return rows


def bytes_to_gb(value: int) -> str:
    return f"{value / (1024 ** 3):.2f} GB"


def write_summary(
    drive_g: list[FileRecord],
    drive_f: list[FileRecord],
    local_records: list[FileRecord],
    duplicates: list[dict],
    large_files: list[dict],
    missing_on_drive: list[dict],
    drive_only: list[dict],
    paper_gaps: list[dict],
) -> None:
    g_files = [r for r in drive_g if not r.is_dir]
    f_files = [r for r in drive_f if not r.is_dir]
    local_files = [r for r in local_records if not r.is_dir]
    g_topics = Counter(r.topic for r in g_files if r.topic != "other")
    local_topics = Counter(r.topic for r in local_files if r.topic != "other")

    lines = [
        "# Drive Audit Summary",
        "",
        f"Generated: {datetime.now().isoformat()}",
        "",
        "## What was already completed",
        "- Confirmed `G:\\Mon disque` as the Drive for `martinlepage26@me.com`.",
        "- Confirmed the smaller secondary Drive root at `F:\\Mon disque`.",
        "- Completed a first-pass manual scan of sizes, extensions, and large folders before this scripted export.",
        "",
        "## Next concrete step that was resumed here",
        "- Export full inventories, derive cleanup candidates, and compare topical files against local C:/WSL sources.",
        "",
        "## Inventory",
        f"- Drive G files: {len(g_files)} across {bytes_to_gb(sum(r.size for r in g_files))}",
        f"- Drive F files: {len(f_files)} across {bytes_to_gb(sum(r.size for r in f_files))}",
        f"- Local topical files scanned: {len(local_files)}",
        "",
        "### Drive G top-level by size",
    ]
    for row in top_level_rollup(drive_g)[:12]:
        lines.append(f"- `{row['folder']}`: {row['files']} files, {bytes_to_gb(row['bytes'])}")
    lines.extend(
        [
            "",
            "### Drive G topical counts",
        ]
    )
    for topic, count in g_topics.most_common():
        lines.append(f"- `{topic}`: {count}")
    lines.extend(
        [
            "",
            "### Local topical counts",
        ]
    )
    for topic, count in local_topics.most_common():
        lines.append(f"- `{topic}`: {count}")
    lines.extend(
        [
            "",
            "## Deletion / cleanup candidates",
            f"- Duplicate candidate groups: {len([r for r in duplicates if r['candidate_type'] != 'cleanup_artifact'])}",
            f"- Cleanup artifacts: {len([r for r in duplicates if r['candidate_type'] == 'cleanup_artifact'])}",
            f"- Large files over 100 MB: {len(large_files)}",
            "",
            "### Highest-signal cleanup suggestions",
        ]
    )
    for row in large_files[:10]:
        lines.append(f"- `{row['path']}` ({row['size_mb']} MB, {row['reason']})")
    lines.extend(
        [
            "",
            "## Topic comparison",
            f"- Topical local files missing a Drive match: {len(missing_on_drive)}",
            f"- Topical Drive files missing a local match: {len(drive_only)}",
            "",
            "### Likely missing from Drive / official paper set",
        ]
    )
    for row in missing_on_drive[:15]:
        lines.append(f"- `{row['topic']}` -> `{row['normalized_stem']}`")
    lines.extend(
        [
            "",
            "## Official paper package gaps",
            f"- Clusters with likely missing companion artifacts: {len(paper_gaps)}",
        ]
    )
    for row in paper_gaps[:15]:
        lines.append(f"- `{row['cluster']}` missing `{row['missing_companions']}`")
    lines.extend(
        [
            "",
            "## Assumptions",
            "- Because the Google Drive API connector was not available, this uses Drive-for-Desktop mounted roots instead of the cloud API.",
            "- Local comparison focuses on user-relevant C: paths plus the WSL home tree, excluding system/cache folders.",
            "- \"Official papers\" is inferred heuristically from filenames and companion-document patterns, so suggestions are review prompts, not absolute truth.",
        ]
    )

    (OUTPUT_ROOT / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(reuse_inventory: bool = False) -> int:
    ensure_output_root()

    if reuse_inventory:
        drive_g = read_records_csv(OUTPUT_ROOT / "inventory_drive_g_martinlepage26_me_com.csv")
        drive_f = read_records_csv(OUTPUT_ROOT / "inventory_drive_f_secondary.csv")
        local_records: list[FileRecord] = []
        for idx, _ in enumerate(C_SCAN_ROOTS, start=1):
            local_records.extend(read_records_csv(OUTPUT_ROOT / f"inventory_local_c_{idx}.csv"))
        for idx, _ in enumerate(WSL_SCAN_ROOTS, start=1):
            local_records.extend(read_records_csv(OUTPUT_ROOT / f"inventory_local_wsl_{idx}.csv"))
        if not drive_g or not drive_f:
            raise SystemExit("Missing existing inventory CSVs required for --reuse-inventory.")
    else:
        drive_g = inventory_windows_root("inventory_drive_g_martinlepage26_me_com", DRIVE_ROOTS["drive_g_martinlepage26_me_com"])
        drive_f = inventory_windows_root("inventory_drive_f_secondary", DRIVE_ROOTS["drive_f_secondary"])

        local_records = []
        for idx, root in enumerate(C_SCAN_ROOTS, start=1):
            local_records.extend(inventory_local_root(f"inventory_local_c_{idx}", root))
        for idx, root in enumerate(WSL_SCAN_ROOTS, start=1):
            local_records.extend(inventory_local_root(f"inventory_local_wsl_{idx}", root))

    drive_all = drive_g + drive_f
    duplicates = duplicate_candidates(drive_all)
    large_files = large_file_candidates(drive_all)
    missing_on_drive, drive_only = topic_comparison(drive_all, local_records)
    paper_gaps = official_paper_gaps(drive_all + local_records)

    write_csv(OUTPUT_ROOT / "drive_top_level_g.csv", top_level_rollup(drive_g))
    write_csv(OUTPUT_ROOT / "drive_top_level_f.csv", top_level_rollup(drive_f))
    write_csv(OUTPUT_ROOT / "drive_extensions_g.csv", extension_rollup(drive_g))
    write_csv(OUTPUT_ROOT / "drive_extensions_f.csv", extension_rollup(drive_f))
    write_csv(OUTPUT_ROOT / "duplicate_candidates.csv", duplicates)
    write_csv(OUTPUT_ROOT / "large_file_candidates.csv", large_files)
    write_csv(OUTPUT_ROOT / "topic_missing_on_drive.csv", missing_on_drive)
    write_csv(OUTPUT_ROOT / "topic_drive_only.csv", drive_only)
    write_csv(OUTPUT_ROOT / "official_paper_gaps.csv", paper_gaps)

    write_summary(
        drive_g=drive_g,
        drive_f=drive_f,
        local_records=local_records,
        duplicates=duplicates,
        large_files=large_files,
        missing_on_drive=missing_on_drive,
        drive_only=drive_only,
        paper_gaps=paper_gaps,
    )

    print(str(OUTPUT_ROOT))
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--reuse-inventory",
        action="store_true",
        help="Reuse existing inventory CSVs in the output directory instead of rescanning disks.",
    )
    args = parser.parse_args()
    raise SystemExit(main(reuse_inventory=args.reuse_inventory))
