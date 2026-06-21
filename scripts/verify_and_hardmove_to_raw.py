#!/usr/bin/env python3
"""
Fail-closed verifier + hard-move intake for EMERAULD knowledge scans.

Protocol:
1) Verify existence, type, readability, size, and duplicate hash state.
2) Hard-move verified, non-duplicate files to /raw.
3) Emit a JSON report with verified vs rejected artifacts.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import shutil
import sys
from pathlib import Path
from typing import Any

VAULT_ROOT = Path("/mnt/c/users/softinfo/documents/emerauld")
DEFAULT_RAW_DIR = VAULT_ROOT / "raw"
MANIFEST_PATH = DEFAULT_RAW_DIR / ".intake-manifest.jsonl"


def utc_now() -> str:
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


def load_manifest_hash_index(manifest_path: Path) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    if not manifest_path.exists():
        return index
    with manifest_path.open("r", encoding="utf-8") as f:
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
                index.setdefault(sha, rec)
    return index


def ensure_unique_destination(target: Path) -> Path:
    if not target.exists():
        return target
    stem = target.stem
    suffix = target.suffix
    counter = 2
    while True:
        candidate = target.with_name(f"{stem}--dup{counter}{suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def destination_for(src: Path, raw_dir: Path, source_root: Path | None) -> Path:
    if source_root is None:
        return ensure_unique_destination(raw_dir / src.name)
    try:
        rel = src.relative_to(source_root)
    except ValueError:
        rel = Path(src.name)
    return ensure_unique_destination(raw_dir / rel)


def quick_readability_check(path: Path) -> tuple[bool, str]:
    # Binary-safe: just verify file can be opened/read.
    try:
        with path.open("rb") as f:
            f.read(4096)
        return True, ""
    except Exception as e:  # noqa: BLE001
        return False, str(e)


def verify_candidate(path: Path) -> dict[str, Any]:
    result: dict[str, Any] = {
        "path": str(path),
        "verified": False,
        "reason": "",
        "size_bytes": None,
        "sha256": None,
    }
    if not path.exists():
        result["reason"] = "missing_file"
        return result
    if not path.is_file():
        result["reason"] = "not_a_file"
        return result
    try:
        size = path.stat().st_size
    except Exception as e:  # noqa: BLE001
        result["reason"] = f"stat_error:{e}"
        return result
    result["size_bytes"] = size
    if size <= 0:
        result["reason"] = "empty_file"
        return result
    ok, err = quick_readability_check(path)
    if not ok:
        result["reason"] = f"unreadable:{err}"
        return result
    try:
        result["sha256"] = sha256_file(path)
    except Exception as e:  # noqa: BLE001
        result["reason"] = f"hash_error:{e}"
        return result
    result["verified"] = True
    return result


def append_manifest_records(manifest_path: Path, records: list[dict[str, Any]]) -> None:
    with manifest_path.open("a", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Verify and hard-move source artifacts into EMERAULD /raw."
    )
    p.add_argument(
        "--raw-dir",
        default=str(DEFAULT_RAW_DIR),
        help=f"Raw intake directory (default: {DEFAULT_RAW_DIR})",
    )
    p.add_argument(
        "--manifest",
        default=str(MANIFEST_PATH),
        help=f"Global intake manifest path (default: {MANIFEST_PATH})",
    )
    p.add_argument(
        "--source",
        required=True,
        help="Source label for provenance (example: d-drive-scan-2026-05-12).",
    )
    p.add_argument(
        "--preserve-relative-to",
        default="",
        help="Preserve paths relative to this source root under --raw-dir.",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Verify and report intended moves without moving files or updating the manifest.",
    )
    p.add_argument(
        "--report",
        default="",
        help="Optional output report path. Defaults to /raw/intake-report-<ts>.json",
    )
    p.add_argument("files", nargs="+", help="Candidate files to verify and move.")
    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    raw_dir = Path(args.raw_dir).resolve()
    raw_dir.mkdir(parents=True, exist_ok=True)

    manifest_path = Path(args.manifest).expanduser().resolve()
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_index = load_manifest_hash_index(manifest_path)
    hash_index = dict(manifest_index)
    source_root = (
        Path(args.preserve_relative_to).expanduser().resolve()
        if args.preserve_relative_to
        else None
    )

    verified: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    manifest_new: list[dict[str, Any]] = []

    for item in args.files:
        src = Path(item).expanduser().resolve()
        v = verify_candidate(src)
        if not v["verified"]:
            rejected.append(v)
            continue

        sha = str(v["sha256"])
        prev = hash_index.get(sha)
        if prev is not None:
            v["verified"] = False
            v["reason"] = "duplicate_hash_in_manifest"
            v["duplicate_of"] = prev.get("raw_path", prev.get("source_path", "unknown"))
            rejected.append(v)
            continue

        target = destination_for(src, raw_dir, source_root)
        if not args.dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            try:
                shutil.move(str(src), str(target))
            except Exception as e:  # noqa: BLE001
                v["verified"] = False
                v["reason"] = f"move_error:{e}"
                rejected.append(v)
                continue

        moved = {
            "source_path": str(src),
            "raw_path": str(target),
            "file_name": target.name,
            "size_bytes": v["size_bytes"],
            "sha256": sha,
            "source_label": args.source,
            "verified_at_utc": utc_now(),
            "verification": {
                "exists": True,
                "is_file": True,
                "readable": True,
                "non_empty": True,
                "duplicate": False,
            },
        }
        if args.dry_run:
            moved["dry_run"] = True
        verified.append(moved)
        if not args.dry_run:
            manifest_new.append(moved)
        hash_index[sha] = moved

    if manifest_new and not args.dry_run:
        append_manifest_records(manifest_path, manifest_new)

    report = {
        "run_at_utc": utc_now(),
        "source_label": args.source,
        "raw_dir": str(raw_dir),
        "manifest_path": str(manifest_path),
        "dry_run": bool(args.dry_run),
        "counts": {
            "input": len(args.files),
            "verified": len(verified),
            "rejected": len(rejected),
        },
        "verified": verified,
        "rejected": rejected,
    }

    if args.report:
        report_path = Path(args.report).expanduser().resolve()
    else:
        stamp = dt.datetime.now().strftime("%Y%m%dT%H%M%S")
        report_path = DEFAULT_RAW_DIR / f"intake-report-{stamp}.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(report["counts"]))
    print(f"report: {report_path}")
    return 0 if len(verified) > 0 else 2


if __name__ == "__main__":
    sys.exit(main())
