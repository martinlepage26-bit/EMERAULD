#!/usr/bin/env python3
"""
compassai_aurorai_extractor.py
──────────────────────────────
PHAROS Archive — CompassAI / AurorAI Implementation Reference Extractor

Purpose
-------
`moving parts.txt` is the ONLY file in the 116-file archive with meaningful
keyword density for CompassAI and AurorAI (8 hits for impl_pharos_govern_ai,
1 hit each for impl_compassai and impl_aurorai per the diagnostic report).

Before this file is merged into any other document, its implementation
references must be extracted, attributed, and re-homed as a standalone
evidence artifact. If the merge happens first, the archive loses its only
keyword-traceable implementation evidence for both tools.

This script:
  1. Reads `moving parts.txt` (or any target file)
  2. Extracts all paragraphs containing CompassAI, AurorAI, and PHAROS
     implementation keywords
  3. Writes a provenance-stamped extraction artifact
  4. Writes a keyword hit log (matches the ai_governance_text_hits.csv format)
  5. Prints a merge-safety clearance report

Run this BEFORE any merge operation on moving parts.txt.

Usage
-----
  python compassai_aurorai_extractor.py \
    --source "moving parts.txt" \
    --output-dir ./extracted_evidence

Outputs
-------
  extracted_evidence/
    compassai_aurorai_implementation_references.md   ← the provenance artifact
    compassai_aurorai_keyword_hits.csv               ← hits in text-hits format
    moving_parts_merge_clearance.txt                 ← merge-safe confirmation
"""

import argparse
import csv
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# ── Keyword sets ─────────────────────────────────────────────────────────────

# Primary implementation keywords (from the diagnostic: impl_* category)
IMPLEMENTATION_KEYWORDS = [
    "compassai",
    "compass ai",
    "compass-ai",
    "aurorai",
    "aurora ai",
    "aurora-ai",
    "impl_compassai",
    "impl_aurorai",
    "impl_pharos_govern_ai",
]

# Secondary PHAROS governance implementation terms
PHAROS_IMPL_KEYWORDS = [
    "pharos",
    "govern-ai",
    "govern_ai",
    "governai",
    "governance suite",
    "governance shell",
    "compass",          # broad — will produce false positives; marked in output
    "aurora",           # broad — same
]

# Topology terms (P1 gap — check here too while we have the corpus open)
TOPOLOGY_KEYWORDS = [
    "topology_theseus",
    "topology_auryn",
    "topology_hopf",
    "theseus",
    "auryn",
    "hopf",
]

KEYWORD_TIERS = {
    "primary_implementation": IMPLEMENTATION_KEYWORDS,
    "pharos_governance":      PHAROS_IMPL_KEYWORDS,
    "topology_audit":         TOPOLOGY_KEYWORDS,
}


def compile_patterns(keywords: list[str]) -> list[re.Pattern]:
    return [re.compile(re.escape(kw), re.IGNORECASE) for kw in keywords]


def split_paragraphs(text: str) -> list[tuple[int, str]]:
    """Split text into (line_number, paragraph) pairs."""
    paragraphs: list[tuple[int, str]] = []
    current_lines: list[str] = []
    current_start = 1

    for i, line in enumerate(text.splitlines(), start=1):
        if line.strip() == "":
            if current_lines:
                paragraphs.append((current_start, "\n".join(current_lines)))
                current_lines = []
                current_start = i + 1
        else:
            if not current_lines:
                current_start = i
            current_lines.append(line)

    if current_lines:
        paragraphs.append((current_start, "\n".join(current_lines)))

    return paragraphs


def scan_paragraph(
    para: str, tier_patterns: dict[str, list[re.Pattern]]
) -> dict[str, list[str]]:
    """Return {tier: [matched_keywords]} for a paragraph."""
    hits: dict[str, list[str]] = {}
    for tier, patterns in tier_patterns.items():
        matched = [p.pattern for p in patterns if p.search(para)]
        if matched:
            hits[tier] = matched
    return hits


def format_extraction_doc(
    source_path: Path,
    extractions: list[dict],
    topology_hits: list[dict],
    ts: str,
) -> str:
    lines = [
        "# CompassAI / AurorAI Implementation References",
        f"**Extracted from:** `{source_path.name}`",
        f"**Extraction timestamp:** {ts}",
        f"**Extractor:** compassai_aurorai_extractor.py",
        f"**Provenance status:** source_bearing_implementation_trace",
        f"**Action:** PRESERVE — this document must not be merged or deleted.",
        "",
        "---",
        "",
        "## Extraction rationale",
        "",
        f"`{source_path.name}` is the sole file in the PHAROS archive with keyword",
        "evidence for CompassAI and AurorAI implementation (8 hits for",
        "`impl_pharos_govern_ai`, 1 each for `impl_compassai` and `impl_aurorai`).",
        "This extraction preserves those references as a standalone provenance artifact",
        "so that the source file can be merged without destroying the implementation trace.",
        "",
        "---",
        "",
        "## Extracted paragraphs",
        "",
    ]

    if not extractions:
        lines += [
            "> **WARNING:** No paragraphs matched primary implementation keywords.",
            "> Either the keyword extraction pass used different search strings,",
            "> or the file content does not contain these terms in their expected form.",
            "> This is itself a finding — flag for manual review of the source file.",
        ]
    else:
        for i, ex in enumerate(extractions, start=1):
            tier_summary = ", ".join(
                f"{tier}: {', '.join(kws)}"
                for tier, kws in ex["hits"].items()
            )
            lines += [
                f"### Paragraph {i} (source line {ex['line_number']})",
                f"**Keyword tiers matched:** {tier_summary}",
                "",
                ex["text"],
                "",
                "---",
                "",
            ]

    if topology_hits:
        lines += [
            "## Topology keyword audit (P1 gap check)",
            "",
            "The following topology terms — flagged as having ZERO archive hits in the",
            "diagnostic — were found in this file. This resolves or partially resolves",
            "the topology gap for this source document.",
            "",
        ]
        for h in topology_hits:
            lines.append(f"- Line {h['line_number']}: `{h['keyword']}` in: {h['context'][:120]!r}")
    else:
        lines += [
            "## Topology keyword audit (P1 gap check)",
            "",
            "> `topology_theseus`, `topology_auryn`, `topology_hopf` — ZERO hits in this file.",
            "> Topology gap confirmed for this source. Check `03_TOPOLOGY_*` documents directly.",
        ]

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract CompassAI/AurorAI references from moving parts.txt before merge"
    )
    parser.add_argument(
        "--source",
        required=True,
        type=Path,
        help="Path to the source file (e.g. 'moving parts.txt')",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("extracted_evidence"),
        help="Directory to write extraction artifacts",
    )
    args = parser.parse_args()

    if not args.source.exists():
        print(f"ERROR: Source file not found: {args.source}", file=sys.stderr)
        sys.exit(1)

    text = args.source.read_text(encoding="utf-8", errors="replace")
    paragraphs = split_paragraphs(text)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # Compile patterns
    tier_patterns: dict[str, list[re.Pattern]] = {
        tier: compile_patterns(kws) for tier, kws in KEYWORD_TIERS.items()
    }

    extractions: list[dict]   = []
    keyword_hits: list[dict]  = []
    topology_hits: list[dict] = []

    for line_num, para in paragraphs:
        hits = scan_paragraph(para, tier_patterns)
        if not hits:
            continue

        # Separate topology hits for the gap audit
        topo_hit = hits.pop("topology_audit", None)
        if topo_hit:
            topology_hits.append({
                "line_number": line_num,
                "keyword": ", ".join(topo_hit),
                "context": para[:200],
            })

        if hits:
            extractions.append({"line_number": line_num, "text": para, "hits": hits})
            for tier, kws in hits.items():
                for kw in kws:
                    keyword_hits.append({
                        "Path":     str(args.source),
                        "Line":     line_num,
                        "Tier":     tier,
                        "Keyword":  kw,
                        "Context":  para[:300].replace("\n", " "),
                    })

    # Write outputs
    args.output_dir.mkdir(parents=True, exist_ok=True)

    # 1 — Provenance extraction document
    doc_path = args.output_dir / "compassai_aurorai_implementation_references.md"
    doc_path.write_text(
        format_extraction_doc(args.source, extractions, topology_hits, ts),
        encoding="utf-8",
    )

    # 2 — Keyword hit log (matches ai_governance_text_hits.csv format)
    hits_path = args.output_dir / "compassai_aurorai_keyword_hits.csv"
    if keyword_hits:
        with open(hits_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Path", "Line", "Tier", "Keyword", "Context"])
            writer.writeheader()
            writer.writerows(keyword_hits)

    # 3 — Merge clearance report
    clearance_lines = [
        "PHAROS MERGE CLEARANCE REPORT",
        f"Source file: {args.source}",
        f"Generated:   {ts}",
        "─" * 60,
        "",
        f"Implementation references extracted: {len(extractions)} paragraphs",
        f"Keyword hits logged:                 {len(keyword_hits)} rows",
        f"Topology gap hits:                   {len(topology_hits)} (expected 0 per diagnostic)",
        "",
    ]

    if extractions:
        clearance_lines += [
            "✓ CompassAI/AurorAI references have been extracted and preserved.",
            f"  Provenance artifact: {doc_path}",
            f"  Keyword hit log:     {hits_path}",
            "",
            "MERGE CLEARANCE: GRANTED",
            f"  {args.source.name} may now be merged.",
            "  Condition: the provenance artifact above must be committed to the",
            "  archive as a standalone PRESERVE_AS_IS file before the merge commit.",
        ]
    else:
        clearance_lines += [
            "⚠ WARNING: No implementation references found in this file.",
            "  Either the keywords were not present in the expected form,",
            "  or this is the wrong file.",
            "",
            "MERGE CLEARANCE: BLOCKED — manual review required.",
            "  Do not merge until the keyword gap is resolved.",
            "  Verify you are running this against the correct source file.",
        ]

    clearance_path = args.output_dir / "moving_parts_merge_clearance.txt"
    clearance_path.write_text("\n".join(clearance_lines), encoding="utf-8")

    # Console summary
    print("\n" + "═" * 60)
    print("COMPASSAI / AURORAI EXTRACTOR — COMPLETE")
    print("═" * 60)
    print(f"Source:      {args.source}")
    print(f"Paragraphs:  {len(paragraphs)} scanned, {len(extractions)} extracted")
    print(f"Keyword hits: {len(keyword_hits)}")
    print(f"Topology gap: {len(topology_hits)} hits (expected 0)")
    print(f"\nOutputs written to: {args.output_dir}/")
    print(f"  {doc_path.name}")
    print(f"  {hits_path.name}")
    print(f"  {clearance_path.name}")

    status = "GRANTED" if extractions else "BLOCKED"
    print(f"\nMERGE CLEARANCE: {status}")


if __name__ == "__main__":
    main()
