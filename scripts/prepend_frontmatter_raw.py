#!/usr/bin/env python3
"""
Byte-safe frontmatter prepend for the protected raw lanes (`raw sources/`, `raw/`).

Operator override 2026-07-08: raw files MAY receive a YAML frontmatter block, but the
original body must remain byte-identical after the block. This script is the only
sanctioned writer for those lanes. It:

1. targets only .md files whose bytes do not already start with a frontmatter fence;
2. records sha256 of the original bytes;
3. writes header_bytes + original_bytes with no decode/encode round-trip of the body,
   no lstrip, no newline normalization;
4. re-reads and asserts sha256(new_bytes[len(header):]) == original hash;
5. emits a manifest at _vault/RAW-FRONTMATTER-MANIFEST-2026-07-08.md.

Frontmatter is deliberately minimal (no updated/backlink fields) so these files stay
out of all future enrichment churn.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LANES = {"raw sources": "raw-source", "raw": "raw-intake"}
MANIFEST = ROOT / "_vault" / f"RAW-FRONTMATTER-MANIFEST-{date.today().isoformat()}.md"
DATE_RE = re.compile(r"(20\d{2})[-_ ](0[1-9]|1[0-2])[-_ ]([0-3]\d)")


def git_created(rel: str) -> str:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(ROOT), "log", "--follow", "--format=%ad", "--date=short", "--", rel],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        out = ""
    return out.splitlines()[-1].strip() if out else ""


def header_for(path: Path, lane_type: str) -> bytes:
    rel = path.relative_to(ROOT).as_posix()
    created = ""
    m = DATE_RE.search(path.name)
    if m:
        created = f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    if not created:
        created = git_created(rel) or date.today().isoformat()
    meta = {
        "type": lane_type,
        "title": path.stem,
        "tags": [lane_type],
        "status": "preserved",
        "created": created,
        "vault_area": path.relative_to(ROOT).parts[0],
        "canonical_path": rel,
    }
    dumped = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, default_flow_style=False, width=1000)
    return f"---\n{dumped}---\n\n".encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepend frontmatter to raw-lane files, byte-safe")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    rows: list[tuple[str, str, str]] = []  # rel, sha256, status
    skipped_existing = 0
    failures: list[str] = []

    for lane, lane_type in LANES.items():
        lane_dir = ROOT / lane
        if not lane_dir.exists():
            continue
        for path in sorted(lane_dir.rglob("*.md")):
            original = path.read_bytes()
            if original.startswith(b"---\n") or original.startswith(b"---\r\n"):
                skipped_existing += 1
                continue
            digest = hashlib.sha256(original).hexdigest()
            if args.dry_run:
                rows.append((path.relative_to(ROOT).as_posix(), digest, "would-prepend"))
                continue
            header = header_for(path, lane_type)
            path.write_bytes(header + original)
            reread = path.read_bytes()
            ok = hashlib.sha256(reread[len(header):]).hexdigest() == digest
            if not ok:
                # restore original immediately on any mismatch
                path.write_bytes(original)
                failures.append(path.relative_to(ROOT).as_posix())
                rows.append((path.relative_to(ROOT).as_posix(), digest, "FAILED-RESTORED"))
            else:
                rows.append((path.relative_to(ROOT).as_posix(), digest, "verified"))

    print(f"prepended={sum(1 for r in rows if r[2] == 'verified')}")
    print(f"would_prepend={sum(1 for r in rows if r[2] == 'would-prepend')}")
    print(f"skipped_existing_frontmatter={skipped_existing}")
    print(f"failures={len(failures)}")
    for f in failures:
        print(f"  FAILED: {f}")

    if not args.dry_run and rows:
        lines = [
            "---",
            "type: register",
            f"title: RAW-FRONTMATTER-MANIFEST-{date.today().isoformat()}",
            "tags:",
            "- register",
            "- raw-override",
            "status: active",
            f"created: '{date.today().isoformat()}'",
            "vault_area: _vault",
            f"canonical_path: _vault/{MANIFEST.name}",
            "---",
            "",
            f"# Raw-Lane Frontmatter Manifest — {date.today().isoformat()}",
            "",
            "Operator-approved override: YAML frontmatter prepended to raw-lane files;",
            "bodies verified byte-identical via sha256. See [[OVERHAUL-BASELINE-2026-07-08]]",
            "and the [[EMERAULD]] provenance rule.",
            "",
            "| File | sha256(original body) | Status |",
            "|---|---|---|",
        ]
        for rel, digest, status in rows:
            lines.append(f"| {rel} | `{digest[:16]}…` | {status} |")
        MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"manifest={MANIFEST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
