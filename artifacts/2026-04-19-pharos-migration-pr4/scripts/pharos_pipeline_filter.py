#!/usr/bin/env python3
"""
pharos_pipeline_filter.py
─────────────────────────
PHAROS Archive — Pipeline Contamination Filter

Purpose
-------
Reads 00_ARCHIVE_METADATA_MANIFEST.csv and produces a clean evidence manifest
that excludes files that must not enter a fresh evidence scan:
  - revision_status == redistributed_copy   (43 files — the baseline-loop source)
  - revision_status == superseded_but_important  (3 files — AI interpretive, unlabelled)
  - action         == REVISE_AND_STRENGTHEN  (5 files — Grok/Codex derivatives)

Also raises hard errors if high-risk files are in the MERGE queue without a human
gate recorded (specifically: ai-anxiety manuscript).

Usage
-----
  python pharos_pipeline_filter.py \
    --manifest 00_ARCHIVE_METADATA_MANIFEST.csv \
    --inventory 00_archive_inventory.csv \
    --output    pharos_clean_manifest.csv \
    --dry-run

  Drop --dry-run to write the output file.

Outputs
-------
  pharos_clean_manifest.csv    — files safe to include in a pipeline run
  pharos_excluded.csv          — excluded files with reason codes
  pharos_filter_report.txt     — human-readable summary

Exit codes
----------
  0  — clean run
  1  — hard stop: protected file in auto-merge queue (human gate required)
  2  — CSV parse error
"""

import argparse
import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

# ── Exclusion rules ──────────────────────────────────────────────────────────

# revision_status values that must NEVER enter a fresh evidence scan
EXCLUDED_REVISION_STATUSES = {
    "redistributed_copy",
    "superseded_but_important",
}

# action values that must NEVER enter a fresh evidence scan
EXCLUDED_ACTIONS = {
    "REVISE_AND_STRENGTHEN",
    "DEPRECATED",
}

# Files that require a human gate before any automated merge.
# If these appear in an auto-merge queue this script exits with code 1.
HUMAN_GATE_REQUIRED = {
    "ai-anxiety-recursive-governance-ai-society-aligned-2026-03-11.md",
}

# The action that would trigger the human gate check
MERGE_ACTIONS = {"MERGE_WITH_RELATED_FILE", "MERGE"}

# Evidence statuses that carry primary evidentiary weight
PRIMARY_EVIDENCE_STATUSES = {"source_bearing_artifact"}

# ── Reason codes for exclusion report ────────────────────────────────────────
REASON_REDISTRIBUTED   = "redistributed_copy: excluded — baseline-loop contamination source"
REASON_SUPERSEDED      = "superseded_but_important: excluded — AI interpretive derivative, not primary evidence"
REASON_REVISE          = "REVISE_AND_STRENGTHEN: excluded — AI-output artifact not yet aligned to PHAROS v5/v6 method"
REASON_DEPRECATED      = "DEPRECATED action: excluded — marked for deprecation"


def load_csv(path: Path) -> list[dict]:
    try:
        with open(path, newline="", encoding="utf-8-sig") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print(f"ERROR: File not found: {path}", file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(f"ERROR: Could not parse {path}: {e}", file=sys.stderr)
        sys.exit(2)


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def check_human_gates(manifest_rows: list[dict]) -> None:
    """
    Exit with code 1 if a protected file is in an automated merge queue
    without a recorded human_gate_cleared flag.
    """
    violations = []
    for row in manifest_rows:
        filename = row.get("filename", row.get("file_name", row.get("File", "")))
        action   = row.get("action", "").strip()
        human_gate = row.get("human_gate_cleared", "").strip().lower()

        if any(name in filename for name in HUMAN_GATE_REQUIRED):
            if action in MERGE_ACTIONS and human_gate not in ("true", "yes", "1"):
                violations.append(
                    f"  HARD STOP — {filename!r}\n"
                    f"  action={action!r} but human_gate_cleared={human_gate!r}\n"
                    f"  This is a source-bearing, high-confidence manuscript submitted to "
                    f"AI & Society.\n"
                    f"  It must not be merged automatically. Record human_gate_cleared=true\n"
                    f"  in the manifest after a conscious, documented review decision."
                )

    if violations:
        print("\n" + "═" * 72, file=sys.stderr)
        print("PHAROS PIPELINE FILTER — HUMAN GATE REQUIRED", file=sys.stderr)
        print("═" * 72, file=sys.stderr)
        for v in violations:
            print(v, file=sys.stderr)
        print("═" * 72 + "\n", file=sys.stderr)
        sys.exit(1)


def classify_row(row: dict) -> tuple[bool, str]:
    """
    Returns (include: bool, reason: str).
    include=True  → file is safe for pipeline inclusion.
    include=False → file is excluded; reason explains why.
    """
    revision_status = row.get("revision_status", "").strip()
    action          = row.get("action", "").strip()

    if revision_status == "redistributed_copy":
        return False, REASON_REDISTRIBUTED

    if revision_status == "superseded_but_important":
        return False, REASON_SUPERSEDED

    if action == "REVISE_AND_STRENGTHEN":
        return False, REASON_REVISE

    if action in EXCLUDED_ACTIONS - {"REVISE_AND_STRENGTHEN"}:
        return False, REASON_DEPRECATED

    return True, ""


def generate_report(
    total: int,
    clean: list[dict],
    excluded: list[dict],
    dry_run: bool,
    output_path: Path,
) -> str:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    mode = "DRY RUN — no files written" if dry_run else f"Output written to {output_path}"

    # Exclusion breakdown by reason
    reason_counts: dict[str, int] = {}
    for row in excluded:
        r = row.get("_exclusion_reason", "unknown")
        reason_counts[r] = reason_counts.get(r, 0) + 1

    source_bearing_clean = sum(
        1 for r in clean
        if r.get("evidence_status", "") == "source_bearing_artifact"
    )

    lines = [
        "═" * 72,
        "PHAROS PIPELINE FILTER — RUN REPORT",
        f"Generated: {ts}",
        f"Mode: {mode}",
        "═" * 72,
        "",
        f"Total files in manifest  : {total}",
        f"Included (clean)         : {len(clean)}",
        f"Excluded (contaminated)  : {len(excluded)}",
        f"  of which source-bearing: {source_bearing_clean} (in clean set)",
        "",
        "Exclusion breakdown:",
    ]
    for reason, count in sorted(reason_counts.items(), key=lambda x: -x[1]):
        lines.append(f"  {count:>3}  {reason}")

    lines += [
        "",
        "Excluded files:",
    ]
    for row in excluded:
        filename = row.get("filename", row.get("file_name", row.get("File", "unknown")))
        reason   = row.get("_exclusion_reason", "")
        lines.append(f"  [{row.get('confidence', '?'):>12}]  {filename}")
        lines.append(f"               → {reason}")

    lines += [
        "",
        "─" * 72,
        "WARNING: The following files are excluded but carry notes worth reviewing:",
        "  moving parts.txt         — MERGE flagged; sole CompassAI/AurorAI keyword carrier.",
        "                             Run compassai_aurorai_extractor.py BEFORE any merge.",
        "  ai-anxiety-recursive-... — Source-bearing, high-confidence, AI&Society submission.",
        "                             Human gate required before merge (see HUMAN_GATE_REQUIRED).",
        "─" * 72,
    ]

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="PHAROS archive pipeline contamination filter"
    )
    parser.add_argument(
        "--manifest",
        required=True,
        type=Path,
        help="Path to 00_ARCHIVE_METADATA_MANIFEST.csv",
    )
    parser.add_argument(
        "--inventory",
        type=Path,
        default=None,
        help="Path to 00_archive_inventory.csv (optional; used for cross-validation only)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("pharos_clean_manifest.csv"),
        help="Output path for the clean manifest CSV",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would be excluded without writing output files",
    )
    args = parser.parse_args()

    manifest_rows = load_csv(args.manifest)

    # Human gate check runs before anything else — hard exit if triggered
    check_human_gates(manifest_rows)

    clean: list[dict]    = []
    excluded: list[dict] = []

    for row in manifest_rows:
        include, reason = classify_row(row)
        if include:
            clean.append(row)
        else:
            row["_exclusion_reason"] = reason
            excluded.append(row)

    report = generate_report(
        total=len(manifest_rows),
        clean=clean,
        excluded=excluded,
        dry_run=args.dry_run,
        output_path=args.output,
    )

    print(report)

    if not args.dry_run:
        fieldnames = list(manifest_rows[0].keys()) if manifest_rows else []

        write_csv(args.output, clean, fieldnames)
        print(f"\nClean manifest written: {args.output} ({len(clean)} files)")

        excluded_path = args.output.with_name(args.output.stem + "_excluded.csv")
        write_csv(excluded_path, excluded, fieldnames + ["_exclusion_reason"])
        print(f"Exclusion log written:  {excluded_path} ({len(excluded)} files)")

        report_path = args.output.with_name("pharos_filter_report.txt")
        report_path.write_text(report, encoding="utf-8")
        print(f"Report written:         {report_path}")
    else:
        print("\n[DRY RUN] No files written. Remove --dry-run to produce output.")


if __name__ == "__main__":
    main()
