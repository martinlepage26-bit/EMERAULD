#!/usr/bin/env python3
"""
topology_audit.py
─────────────────
PHAROS Archive — Topology Keyword Coverage Audit

Purpose
-------
The diagnostic reports that `topology_theseus`, `topology_auryn`, and
`topology_hopf` have ZERO keyword hits across all 116 archive files.
This is a hard gap. The topology layer is architectural — these terms
define the formal method structure and are central to any patent claim
on the method architecture.

There are exactly two explanations for zero hits:
  A. The topology documents were never ingested into the keyword extraction pass.
  B. They were ingested, but the extractor used different search strings
     than what the diagnostic checked for.

This script determines which explanation is correct by:
  1. Scanning the archive inventory for topology-named files
  2. Scanning all ingested files for topology-adjacent terms (broader net)
  3. Reporting which files, if any, contain topology content under any label
  4. Producing a verified keyword list for the next extraction pass

Usage
-----
  # Check just the inventory CSVs (no raw file access needed):
  python topology_audit.py \
    --inventory 00_archive_inventory.csv \
    --manifest  00_ARCHIVE_METADATA_MANIFEST.csv

  # Full scan — also reads raw files from an archive directory:
  python topology_audit.py \
    --inventory 00_archive_inventory.csv \
    --manifest  00_ARCHIVE_METADATA_MANIFEST.csv \
    --archive-dir /path/to/archive/files \
    --output topology_audit_report.md

Outputs
-------
  topology_audit_report.md   — findings and recommended keyword strings
  topology_keyword_hits.csv  — all hits found, if any
"""

import argparse
import csv
import re
import sys
from pathlib import Path
from datetime import datetime, timezone

# ── Keyword tiers ─────────────────────────────────────────────────────────────

# Tier 1: exact terms that should have been in the extraction pass
TIER1_EXACT = [
    "topology_theseus",
    "topology_auryn",
    "topology_hopf",
]

# Tier 2: component names without the topology_ prefix
TIER2_NAMES = [
    "theseus",
    "auryn",
    "hopf",
    "hopf fibration",
    "hopf bundle",
]

# Tier 3: topology-adjacent structural terms used in PHAROS architecture
TIER3_STRUCTURAL = [
    "topolog",        # catches topology, topological, topologies
    "fibration",
    "manifold",
    "recursive shell",
    "topology layer",
    "formal topology",
    "method topology",
    "governance topology",
    "phase topology",
    "recursion structure",
    "structural layer",
]

# Tier 4: filename patterns that suggest topology documents
TOPOLOGY_FILENAME_PATTERNS = [
    r"03_TOPOLOGY",
    r"topology",
    r"theseus",
    r"auryn",
    r"hopf",
    r"TOPOLOGY",
]

ALL_KEYWORD_TIERS = {
    "tier1_exact":       TIER1_EXACT,
    "tier2_names":       TIER2_NAMES,
    "tier3_structural":  TIER3_STRUCTURAL,
}


def load_csv(path: Path) -> list[dict]:
    try:
        with open(path, newline="", encoding="utf-8-sig") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        print(f"ERROR: File not found: {path}", file=sys.stderr)
        sys.exit(2)


def find_topology_files_in_inventory(inventory: list[dict]) -> list[dict]:
    """Find files whose names suggest topology content."""
    filename_patterns = [re.compile(p, re.IGNORECASE) for p in TOPOLOGY_FILENAME_PATTERNS]
    results = []
    for row in inventory:
        filename = row.get("filename", row.get("file_name", row.get("File", "")))
        if any(p.search(filename) for p in filename_patterns):
            results.append(row)
    return results


def scan_file_for_keywords(
    file_path: Path,
    tier_kws: dict[str, list[str]],
) -> dict[str, list[dict]]:
    """Scan a single file for topology keywords. Returns {tier: [hit_records]}."""
    try:
        text = file_path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return {"_error": [{"error": str(e)}]}

    results: dict[str, list[dict]] = {}
    for tier, keywords in tier_kws.items():
        hits = []
        for kw in keywords:
            pattern = re.compile(re.escape(kw), re.IGNORECASE)
            for i, line in enumerate(text.splitlines(), start=1):
                if pattern.search(line):
                    hits.append({
                        "keyword": kw,
                        "line":    i,
                        "context": line.strip()[:200],
                    })
        if hits:
            results[tier] = hits
    return results


def generate_report(
    inventory_topology_files: list[dict],
    manifest_topology_files: list[dict],
    archive_scan_results: dict[str, dict],  # filename → {tier: [hits]}
    ts: str,
) -> str:
    lines = [
        "# PHAROS Topology Keyword Audit Report",
        f"**Generated:** {ts}",
        "",
        "## Finding summary",
        "",
        "The diagnostic identified `topology_theseus`, `topology_auryn`, and",
        "`topology_hopf` as having ZERO keyword hits across 116 archive files.",
        "This report determines whether that gap is due to missing ingestion (A)",
        "or mismatched keyword strings (B).",
        "",
        "---",
        "",
        "## 1. Topology files found in inventory by filename pattern",
        "",
    ]

    if inventory_topology_files:
        lines.append(f"**{len(inventory_topology_files)} file(s) matched topology filename patterns:**")
        lines.append("")
        for row in inventory_topology_files:
            fn = row.get("filename", row.get("file_name", row.get("File", "unknown")))
            ps = row.get("parse_status", "?")
            lines.append(f"- `{fn}` (parse_status: {ps})")
        lines += [
            "",
            "**Finding:** Topology-named files exist in the inventory.",
            "If these files have zero keyword hits in the extraction pass, the likely",
            "cause is **Explanation B** — keyword mismatch, not missing ingestion.",
        ]
    else:
        lines += [
            "**Zero files matched topology filename patterns in the inventory.**",
            "",
            "**Finding:** No `03_TOPOLOGY_*` or equivalent files appear in the inventory.",
            "This strongly supports **Explanation A** — the topology documents were",
            "never ingested. They exist on the filesystem but were not included in",
            "the `00_archive_inventory.csv` scan.",
            "",
            "**Action required:** Locate the topology documents (likely under a",
            "`03_TOPOLOGY_*` or `topology/` directory) and run a fresh inventory",
            "scan that includes them, then re-run the keyword extraction pass.",
        ]

    lines += [
        "",
        "---",
        "",
        "## 2. Topology files found in manifest by filename pattern",
        "",
    ]

    if manifest_topology_files:
        lines.append(f"**{len(manifest_topology_files)} file(s) matched topology filename patterns in manifest:**")
        for row in manifest_topology_files:
            fn = row.get("filename", row.get("file_name", row.get("File", "unknown")))
            ev = row.get("evidence_status", "?")
            lines.append(f"- `{fn}` (evidence_status: {ev})")
    else:
        lines += [
            "**Zero topology-named files in the manifest.**",
            "Consistent with Explanation A (not ingested).",
        ]

    lines += [
        "",
        "---",
        "",
        "## 3. Full-archive keyword scan results",
        "",
    ]

    if archive_scan_results:
        any_hits = any(
            any(tier != "_error" for tier in tiers)
            for tiers in archive_scan_results.values()
        )
        if any_hits:
            lines.append("**Topology keywords FOUND in archive scan:**")
            lines.append("")
            for filename, tier_hits in archive_scan_results.items():
                if tier_hits and "_error" not in tier_hits:
                    lines.append(f"### `{filename}`")
                    for tier, hits in tier_hits.items():
                        lines.append(f"**{tier}:** {len(hits)} hit(s)")
                        for hit in hits[:5]:  # show first 5
                            lines.append(f"  - Line {hit['line']}: `{hit['keyword']}` → {hit['context'][:100]!r}")
                    lines.append("")
        else:
            lines += [
                "**Zero topology keywords found across all scanned files.**",
                "",
                "Both Tier 1 (exact: `topology_theseus`, etc.) and Tier 2 (component names)",
                "returned zero hits. This confirms the gap is not a keyword string mismatch.",
                "**Explanation A is confirmed: topology documents were not ingested.**",
            ]
    else:
        lines += [
            "No `--archive-dir` provided — raw file scan skipped.",
            "Run with `--archive-dir` pointing to the archive root for a full content scan.",
        ]

    lines += [
        "",
        "---",
        "",
        "## 4. Recommended keyword strings for next extraction pass",
        "",
        "Add the following to your keyword extraction configuration:",
        "",
        "```yaml",
        "# Tier 1 — topology exact terms (these should have been present from v5)",
        "- topology_theseus",
        "- topology_auryn",
        "- topology_hopf",
        "",
        "# Tier 2 — component names (catch documents using names without prefix)",
        "- theseus",
        "- auryn",
        "- hopf",
        "- hopf fibration",
        "",
        "# Tier 3 — structural terms (broaden coverage for topology-adjacent content)",
        "- topolog",      # prefix match: topology, topological
        "- fibration",
        "- method topology",
        "- governance topology",
        "- recursive shell",
        "```",
        "",
        "---",
        "",
        "## 5. Required actions",
        "",
        "| Priority | Action | Owner |",
        "|----------|--------|-------|",
        "| **P1** | Locate topology documents (03_TOPOLOGY_* or equivalent) | Martin |",
        "| **P1** | Confirm whether they were excluded from the inventory scan, and why | Martin |",
        "| **P1** | If excluded: re-run inventory including topology directory | Codex |",
        "| **P1** | Re-run keyword extraction with Tier 1+2 strings above | Codex |",
        "| **P2** | Add Tier 3 structural terms to extraction config going forward | Codex |",
        "| **P2** | Verify topology terms appear in any patent claim draft | Martin |",
    ]

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="PHAROS topology keyword coverage audit"
    )
    parser.add_argument(
        "--inventory",
        required=True,
        type=Path,
        help="Path to 00_archive_inventory.csv",
    )
    parser.add_argument(
        "--manifest",
        required=True,
        type=Path,
        help="Path to 00_ARCHIVE_METADATA_MANIFEST.csv",
    )
    parser.add_argument(
        "--archive-dir",
        type=Path,
        default=None,
        help="Root directory of archive files for full content scan (optional)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("topology_audit_report.md"),
        help="Output path for the audit report",
    )
    args = parser.parse_args()

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    inventory = load_csv(args.inventory)
    manifest  = load_csv(args.manifest)

    inventory_topo = find_topology_files_in_inventory(inventory)
    manifest_topo  = find_topology_files_in_inventory(manifest)

    archive_scan_results: dict[str, dict] = {}

    if args.archive_dir:
        if not args.archive_dir.is_dir():
            print(f"ERROR: --archive-dir is not a directory: {args.archive_dir}", file=sys.stderr)
            sys.exit(1)

        # Scan all files in archive dir for topology keywords
        # Focus on text-readable formats
        text_extensions = {".md", ".txt", ".py", ".yaml", ".html", ".css", ".odt", ".docx"}
        files_to_scan = [
            f for f in args.archive_dir.rglob("*")
            if f.is_file() and f.suffix.lower() in text_extensions
        ]

        print(f"Scanning {len(files_to_scan)} files in {args.archive_dir}...")
        for file_path in files_to_scan:
            hits = scan_file_for_keywords(file_path, ALL_KEYWORD_TIERS)
            if hits:
                archive_scan_results[file_path.name] = hits

    report = generate_report(
        inventory_topology_files=inventory_topo,
        manifest_topology_files=manifest_topo,
        archive_scan_results=archive_scan_results,
        ts=ts,
    )

    args.output.write_text(report, encoding="utf-8")
    print(f"Topology audit report written: {args.output}")

    # CSV hit log
    all_hits = []
    for filename, tier_hits in archive_scan_results.items():
        for tier, hits in tier_hits.items():
            if tier == "_error":
                continue
            for hit in hits:
                all_hits.append({
                    "File":    filename,
                    "Tier":    tier,
                    "Keyword": hit["keyword"],
                    "Line":    hit["line"],
                    "Context": hit["context"],
                })

    if all_hits:
        hits_path = args.output.with_name("topology_keyword_hits.csv")
        with open(hits_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["File", "Tier", "Keyword", "Line", "Context"])
            writer.writeheader()
            writer.writerows(all_hits)
        print(f"Keyword hit log written:      {hits_path} ({len(all_hits)} hits)")
    else:
        print("No keyword hits found — topology gap confirmed.")

    # Summary
    print("\n" + "─" * 60)
    if not inventory_topo and not manifest_topo and not any(
        any(t != "_error" for t in hits)
        for hits in archive_scan_results.values()
    ):
        print("CONCLUSION: Explanation A confirmed — topology docs NOT ingested.")
        print("Action: Locate 03_TOPOLOGY_* files and add to inventory scan.")
    elif archive_scan_results and any(
        any(t != "_error" for t in hits)
        for hits in archive_scan_results.values()
    ):
        print("CONCLUSION: Topology content found — keyword mismatch (Explanation B).")
        print("Action: Update extraction strings per report Section 4.")
    else:
        print("CONCLUSION: Inconclusive — run with --archive-dir for full content scan.")


if __name__ == "__main__":
    main()
