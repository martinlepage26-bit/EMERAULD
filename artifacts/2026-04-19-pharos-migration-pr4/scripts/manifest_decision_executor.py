#!/usr/bin/env python3
"""
manifest_decision_executor.py
─────────────────────────────
Applies manifest-level decisions from the Decision Brief directly to
00_ARCHIVE_METADATA_MANIFEST.csv. Auditable, reversible, logged.

Decisions implemented:
  1. ai-anxiety manuscript → PRESERVE_AND_LIGHTLY_CLEAN, human_gate_cleared=true
  2. Optionally archives MASTER_PROJECT_TRACKER.csv as historical run log

Usage:
  python manifest_decision_executor.py \
    --manifest 00_ARCHIVE_METADATA_MANIFEST.csv \
    --decision 1 \
    --dry-run

  python manifest_decision_executor.py \
    --manifest 00_ARCHIVE_METADATA_MANIFEST.csv \
    --decision all \
    --apply

Exit codes:
  0  clean run
  1  manifest not found or parse error
  2  target file not found in manifest
"""

import argparse
import csv
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

# ── Decision definitions ──────────────────────────────────────────────────────

DECISIONS = {
    1: {
        "name": "Preserve AI & Society manuscript",
        "target_filename": "ai-anxiety-recursive-governance-ai-society-aligned-2026-03-11.md",
        "field_updates": {
            "action": "PRESERVE_AND_LIGHTLY_CLEAN",
            "human_gate_cleared": "true",
            "notes": "Decision 1 applied: standalone submission document — merge prohibited until DOI assigned. Decision recorded {timestamp}.",
        },
        "rationale": (
            "Source-bearing, high-confidence, near-final manuscript submitted to AI & Society. "
            "Merging destroys standalone provenance and DOI-citability."
        ),
    },
    2: {
        "name": "Archive Master Tracker as historical run log",
        "target_filename": "MASTER_PROJECT_TRACKER.csv",
        "field_updates": {
            "action": "DEPRECATED_BUT_RETAINED",
            "notes": "Decision 2 applied: archived as append-only historical run log. Active tracking moved to PHAROS_TRACKER_V2.csv. Decision recorded {timestamp}.",
        },
        "rationale": (
            "54 rows with no outcome, 10 slugs repeating 6x at DEFER. "
            "Tracker is accurate as history but not functional as active decision surface."
        ),
    },
}


def load_manifest(path: Path) -> tuple[list[dict], list[str]]:
    try:
        with open(path, newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            fieldnames = list(reader.fieldnames or [])
            rows = list(reader)
        return rows, fieldnames
    except FileNotFoundError:
        print(f"ERROR: Manifest not found: {path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Cannot parse manifest: {e}", file=sys.stderr)
        sys.exit(1)


def apply_decision(
    rows: list[dict],
    fieldnames: list[str],
    decision_id: int,
    timestamp: str,
) -> tuple[list[dict], bool]:
    """Apply a single decision. Returns (updated_rows, was_applied)."""
    decision = DECISIONS[decision_id]
    target = decision["target_filename"]
    updates = decision["field_updates"]

    found = False
    for row in rows:
        fn = row.get("filename", row.get("file_name", row.get("File", "")))
        if target in fn:
            found = True
            before = {k: row.get(k, "") for k in updates}
            for field, value in updates.items():
                value = value.replace("{timestamp}", timestamp)
                row[field] = value
                if field not in fieldnames:
                    fieldnames.append(field)
            after = {k: row.get(k, "") for k in updates}
            print(f"\n  Decision {decision_id}: {decision['name']}")
            print(f"  Target: {fn}")
            print(f"  Rationale: {decision['rationale']}")
            for field in updates:
                print(f"    {field}: {before[field]!r} → {after[field]!r}")
            break

    if not found:
        print(f"\n  WARNING: Target file {target!r} not found in manifest.", file=sys.stderr)
        print(f"  Decision {decision_id} NOT applied.", file=sys.stderr)

    return rows, found


def main():
    parser = argparse.ArgumentParser(
        description="Apply Decision Brief decisions to the archive manifest"
    )
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument(
        "--decision",
        required=True,
        help="Decision number (1, 2) or 'all'",
    )
    parser.add_argument("--dry-run", action="store_true", help="Show changes without writing")
    parser.add_argument("--apply", action="store_true", help="Write changes to manifest")
    args = parser.parse_args()

    if not args.dry_run and not args.apply:
        print("Specify --dry-run or --apply.", file=sys.stderr)
        sys.exit(1)

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    rows, fieldnames = load_manifest(args.manifest)

    # Determine which decisions to apply
    if args.decision == "all":
        decision_ids = sorted(DECISIONS.keys())
    else:
        try:
            decision_ids = [int(args.decision)]
        except ValueError:
            print(f"ERROR: Invalid decision: {args.decision!r}. Use 1, 2, or 'all'.", file=sys.stderr)
            sys.exit(1)

    print("═" * 60)
    print("MANIFEST DECISION EXECUTOR")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'APPLY'}")
    print(f"Timestamp: {ts}")
    print("═" * 60)

    results = {}
    for did in decision_ids:
        if did not in DECISIONS:
            print(f"\n  ERROR: Unknown decision {did}. Available: {list(DECISIONS.keys())}")
            continue
        rows, applied = apply_decision(rows, fieldnames, did, ts)
        results[did] = applied

    # Summary
    print("\n" + "─" * 60)
    for did, applied in results.items():
        status = "✓ APPLIED" if applied else "✗ NOT FOUND"
        print(f"  Decision {did}: {status}")

    if args.apply and any(results.values()):
        # Backup first
        backup_path = args.manifest.with_suffix(f".backup-{ts.replace(' ', '_').replace(':', '')}.csv")
        shutil.copy2(args.manifest, backup_path)
        print(f"\n  Backup: {backup_path}")

        # Write updated manifest
        with open(args.manifest, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)
        print(f"  Updated: {args.manifest}")
    elif args.dry_run:
        print("\n  [DRY RUN] No files written.")


if __name__ == "__main__":
    main()
