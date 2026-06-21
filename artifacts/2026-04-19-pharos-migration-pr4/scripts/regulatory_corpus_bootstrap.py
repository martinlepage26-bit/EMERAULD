#!/usr/bin/env python3
"""
regulatory_corpus_bootstrap.py
──────────────────────────────
PHAROS Archive — Regulatory Document Corpus Bootstrap

The diagnostic found ai_governance_regulatory_docs.csv is EMPTY.
If PHAROS makes regulatory compliance claims, those claims need
a traceable corpus backing them.

This script:
  1. Creates a structured regulatory_docs.csv with the 5 core documents
     that PHAROS positions against
  2. Maps each document to specific PHAROS method components
  3. Generates a keyword extraction config for the next pipeline pass
  4. Produces a compliance claim audit checklist

The actual regulatory PDFs must be obtained and ingested separately.
This script creates the index and mapping layer — the evidence
architecture, not the evidence itself.

Usage:
  python regulatory_corpus_bootstrap.py --output-dir ./regulatory_corpus
"""

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path

# ── Core regulatory documents PHAROS positions against ───────────────────────

REGULATORY_DOCS = [
    {
        "doc_id": "REG-001",
        "title": "EU AI Act",
        "jurisdiction": "EU",
        "year": 2024,
        "status": "enacted",
        "key_articles": "Article 6 (classification), Article 9 (risk management), Article 11 (technical documentation), Article 13 (transparency), Article 14 (human oversight), Article 15 (accuracy/robustness)",
        "pharos_mapping": "Recursive audit (Art. 9), evidence receipts (Art. 11), voice control/authorship boundary (Art. 13), human gate protocol (Art. 14), topology layer integrity (Art. 15)",
        "claim_type": "structural_alignment",
        "ingestion_status": "not_ingested",
        "source_url": "https://eur-lex.europa.eu/eli/reg/2024/1689/oj",
        "notes": "Full text available. Priority ingestion target.",
    },
    {
        "doc_id": "REG-002",
        "title": "NIST AI Risk Management Framework (AI RMF 1.0)",
        "jurisdiction": "US",
        "year": 2023,
        "status": "published",
        "key_articles": "Govern function (roles, policies, accountability), Map function (context, risk identification), Measure function (metrics, evaluation), Manage function (risk response, monitoring)",
        "pharos_mapping": "Govern → recursive governance stack (Layers 1-5), Map → topology layer (Theseus), Measure → evidence receipts + keyword extraction, Manage → consequence binding layer (v6.0)",
        "claim_type": "framework_mapping",
        "ingestion_status": "not_ingested",
        "source_url": "https://www.nist.gov/artificial-intelligence/ai-risk-management-framework",
        "notes": "Free PDF. Four core functions map directly to PHAROS method layers.",
    },
    {
        "doc_id": "REG-003",
        "title": "ISO/IEC 42001:2023 — AI Management System",
        "jurisdiction": "International",
        "year": 2023,
        "status": "published",
        "key_articles": "Section 4 (context), Section 5 (leadership), Section 6 (planning/risk), Section 7 (support/competence), Section 8 (operation), Section 9 (evaluation), Section 10 (improvement)",
        "pharos_mapping": "Section 6 → recursive risk assessment, Section 8 → pipeline filter + evidence scan, Section 9 → topology audit + self-correcting review, Section 10 → method versioning (v5 → v6)",
        "claim_type": "management_system_alignment",
        "ingestion_status": "not_ingested",
        "source_url": "https://www.iso.org/standard/81230.html",
        "notes": "Paid standard. Map PHAROS components to ISO clauses for certification pathway.",
    },
    {
        "doc_id": "REG-004",
        "title": "Canadian Artificial Intelligence and Data Act (AIDA)",
        "jurisdiction": "Canada",
        "year": 2022,
        "status": "proposed",
        "key_articles": "Part 1 (regulated activities), Part 2 (high-impact AI classification), Part 3 (transparency obligations), Part 4 (compliance measures)",
        "pharos_mapping": "High-impact classification → PHAROS risk tier assessment, transparency → evidence receipts + authorship boundary protocol, compliance → pipeline filter + human gate",
        "claim_type": "regulatory_readiness",
        "ingestion_status": "not_ingested",
        "source_url": "https://www.parl.ca/DocumentViewer/en/44-1/bill/C-27/first-reading",
        "notes": "Bill C-27. Quebec jurisdiction relevance for PHAROS registration.",
    },
    {
        "doc_id": "REG-005",
        "title": "Canada Voluntary Code of Conduct on Responsible AI",
        "jurisdiction": "Canada",
        "year": 2023,
        "status": "published",
        "key_articles": "Accountability measures, risk assessment, transparency, human oversight, safety monitoring, valid/reliable AI",
        "pharos_mapping": "Accountability → recursive governance with named decision rights, Risk assessment → topology audit + consequence binding, Transparency → evidence receipts + voice spec, Human oversight → human gate protocol",
        "claim_type": "voluntary_compliance",
        "ingestion_status": "not_ingested",
        "source_url": "https://ised-isde.canada.ca/site/ised/en/voluntary-code-conduct-responsible-development-and-management-advanced-generative-ai-systems",
        "notes": "Voluntary. Low barrier to claim. Good for early positioning.",
    },
]

# ── Keyword extraction config for regulatory corpus ──────────────────────────

REGULATORY_KEYWORDS = {
    "eu_ai_act": [
        "high-risk AI",
        "risk management system",
        "technical documentation",
        "transparency",
        "human oversight",
        "accuracy",
        "robustness",
        "conformity assessment",
        "AI system",
        "deployer",
        "provider",
    ],
    "nist_ai_rmf": [
        "govern",
        "map",
        "measure",
        "manage",
        "trustworthy AI",
        "risk management",
        "AI lifecycle",
        "socio-technical",
        "AI actor",
        "impact assessment",
    ],
    "iso_42001": [
        "AI management system",
        "interested parties",
        "risk treatment",
        "AI policy",
        "competence",
        "documented information",
        "performance evaluation",
        "continual improvement",
        "internal audit",
        "management review",
    ],
    "canadian_aida": [
        "high-impact",
        "artificial intelligence system",
        "biased output",
        "general-purpose",
        "regulated activity",
        "responsible person",
        "significant harm",
    ],
}


def write_regulatory_csv(output_dir: Path) -> Path:
    path = output_dir / "ai_governance_regulatory_docs.csv"
    fieldnames = list(REGULATORY_DOCS[0].keys())
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(REGULATORY_DOCS)
    return path


def write_keyword_config(output_dir: Path) -> Path:
    path = output_dir / "regulatory_keyword_extraction_config.json"
    config = {
        "description": "Keyword extraction configuration for regulatory corpus documents",
        "generated": datetime.now(timezone.utc).isoformat(),
        "keyword_tiers": REGULATORY_KEYWORDS,
        "usage": (
            "Add these keyword sets to the ai_governance_text_hits extraction pass. "
            "Run against ingested regulatory PDFs to map PHAROS claims to specific "
            "regulatory language."
        ),
    }
    path.write_text(json.dumps(config, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def write_compliance_checklist(output_dir: Path) -> str:
    lines = [
        "# PHAROS Regulatory Compliance Claim Audit",
        f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "## Purpose",
        "",
        "This checklist maps every regulatory compliance claim PHAROS makes (or will make)",
        "to the specific evidence required to support it. A claim without traceable evidence",
        "is an assertion — defensible in marketing, flaggable in patent examination or peer review.",
        "",
        "## Compliance claim matrix",
        "",
        "| # | Claim | Regulatory source | PHAROS component | Evidence status | Action |",
        "|---|-------|-------------------|------------------|-----------------|--------|",
    ]

    claims = [
        ("1", "Recursive risk assessment satisfies AI Act Art. 9", "EU AI Act Art. 9", "Recursive governance stack (Layers 1-5)", "UNVERIFIED", "Ingest Art. 9; map to specific layer outputs"),
        ("2", "Evidence receipts satisfy AI Act Art. 11 documentation", "EU AI Act Art. 11", "Evidence receipts pipeline + keyword extraction", "UNVERIFIED", "Ingest Art. 11; demonstrate receipt format compliance"),
        ("3", "Human gate protocol satisfies AI Act Art. 14 oversight", "EU AI Act Art. 14", "Human gate in pipeline filter", "PARTIAL — code exists, no regulatory mapping", "Map gate triggers to Art. 14 requirements"),
        ("4", "Method maps to NIST Govern function", "NIST AI RMF Govern", "Recursive governance stack", "UNVERIFIED", "Ingest NIST Govern; map to Layers 1-5"),
        ("5", "Topology layer maps to NIST Map function", "NIST AI RMF Map", "Topology (Theseus/Auryn/Hopf)", "UNVERIFIED — topology docs have zero keyword hits", "Resolve topology gap first; then map"),
        ("6", "Evidence receipts map to NIST Measure function", "NIST AI RMF Measure", "Evidence receipts + MASTER_PROJECT_TRACKER", "PARTIAL — tracker has 54 empty outcomes", "Archive tracker, create V2; then map"),
        ("7", "ISO 42001 Section 9 alignment", "ISO 42001 S.9", "Topology audit + self-correcting review", "UNVERIFIED", "Paid standard; obtain and map"),
        ("8", "AIDA high-impact readiness", "Canadian AIDA Part 2", "Risk tier assessment", "NOT STARTED", "Monitor bill status; pre-map if enacted"),
        ("9", "Voluntary Code accountability compliance", "CA Voluntary Code", "Recursive governance with named decision rights", "UNVERIFIED", "Low barrier; map and claim early"),
    ]

    for c in claims:
        lines.append(f"| {c[0]} | {c[1]} | {c[2]} | {c[3]} | {c[4]} | {c[5]} |")

    lines += [
        "",
        "## Ingestion priority order",
        "",
        "1. **NIST AI RMF** — free PDF, strongest structural alignment, most credible US reference",
        "2. **EU AI Act** — enacted law, highest regulatory weight, full text available",
        "3. **CA Voluntary Code** — free, low barrier, Quebec jurisdictional relevance",
        "4. **ISO 42001** — paid, but required for any enterprise certification pathway",
        "5. **AIDA** — proposed only; monitor, do not invest heavily until enacted",
        "",
        "## Required actions",
        "",
        "| Priority | Action | Owner |",
        "|----------|--------|-------|",
        "| **P1** | Download NIST AI RMF PDF and ingest into archive inventory | Codex |",
        "| **P1** | Download EU AI Act full text and ingest | Codex |",
        "| **P2** | Map PHAROS components to NIST four functions (Govern/Map/Measure/Manage) | Martin + Codex |",
        "| **P2** | Map PHAROS components to AI Act articles (9, 11, 13, 14, 15) | Martin + Codex |",
        "| **P3** | Obtain ISO 42001 and map Section 6/8/9/10 | Martin |",
        "| **P3** | Download CA Voluntary Code and map | Codex |",
    ]

    content = "\n".join(lines)
    path = output_dir / "regulatory_compliance_audit_checklist.md"
    path.write_text(content, encoding="utf-8")
    return content


def main():
    parser = argparse.ArgumentParser(
        description="Bootstrap the regulatory document corpus for PHAROS"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("regulatory_corpus"),
        help="Directory for output artifacts",
    )
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    print("═" * 60)
    print("PHAROS REGULATORY CORPUS BOOTSTRAP")
    print(f"Generated: {ts}")
    print("═" * 60)

    csv_path = write_regulatory_csv(args.output_dir)
    print(f"\n  ✓ Regulatory docs CSV: {csv_path} ({len(REGULATORY_DOCS)} documents)")

    kw_path = write_keyword_config(args.output_dir)
    print(f"  ✓ Keyword config:      {kw_path}")

    write_compliance_checklist(args.output_dir)
    checklist_path = args.output_dir / "regulatory_compliance_audit_checklist.md"
    print(f"  ✓ Compliance checklist: {checklist_path}")

    print(f"\n  Regulatory corpus bootstrapped at {args.output_dir}/")
    print("  Next: download the actual PDFs and run the keyword extraction pass.")
    print("  Priority order: NIST AI RMF → EU AI Act → CA Voluntary Code → ISO 42001 → AIDA")


if __name__ == "__main__":
    main()
