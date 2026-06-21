---
type: wiki
aliases:
  - MASTER REFERENCE SAFE
  - canonical reference list
  - reference manager
tags: [bibliography, tools, reference, knowledge-infrastructure, research]
status: active
created: 2026-05-04
updated: 2026-05-04
---

# MASTER REFERENCE SAFE — Canonical Bibliography System

## Summary

The MASTER REFERENCE SAFE is the canonical bibliography management system for [[Martin Lepage — Professional Profile|Martin Lepage]]'s full research corpus. It lives at `D:\MASTER REFERENCE SAFE` and maintains a single alphabetically-sorted master citation list, automated annotation builds, and a structured intake pipeline. As of 2026-05-04 it holds **998 citations** spanning AI governance, queer theory, religious studies, disability studies, media studies, social theory, and healthcare.

## Context

This system sits at the centre of all research production in [[Governance and PHAROS MOC]], [[Research and Papers MOC]], and [[Writing and Novels MOC]]. It is the authoritative source that feeds:
- [[Master Bibliography — Références bibliographiques 2025]] — the paper-corpus bibliography
- [[MASTER BIBLIOGRAPHY — Theoretical Genealogy of LOTUS]] — the LOTUS theoretical spine
- [[AI Governance Reference Stack — Annotated Library (Operational 2026-03-11)]] — the governance standards routing list
- All [[PHAROS Method — Technical Reference]] and academic writing output

The system was designed to replace ad-hoc per-paper citation lists with a single maintained library. It supports the long-term goal of [[Legitimacy Machines — Book Skeleton and Architecture]] and all ongoing research.

## Details

**Location:** `D:\MASTER REFERENCE SAFE` (WSL: `/mnt/d/MASTER REFERENCE SAFE`)

**Canonical file:** `canonical/MASTER REFERENCE LIST.txt` — alphabetical by author, single source of truth

**Current state (2026-05-04):**
- 998 entries (grew from 773 on 2026-05-04 via D:\LIBRARY DOI ingest; baseline before Unreadable cleanup synthesis was 995, +3 confirmed entries = 998)
- Annotated views auto-built by `reference_manager.py rebuild`: themes, alphabetical, publication date, compact MD, CSV
- AI Governance derived list maintained separately: `canonical/AI Governance MASTER REFERENCE LIST.txt`

**Intake workflow:**
1. Drop Bibcitation exports, PubMed `.nbib`, or `.ris` files into `exports/bibcitation/inbox/`
2. Run `process-inbox` (or let watcher run continuously)
3. Or: `ingest-file` for direct single-file ingestion
4. Rebuild triggers automatically after each ingest

**Key commands (run from WSL with `python3`):**
```bash
# Ingest from inbox
python3 "/mnt/d/MASTER REFERENCE SAFE/reference_manager.py" process-inbox

# Rebuild all annotated views
python3 "/mnt/d/MASTER REFERENCE SAFE/reference_manager.py" rebuild

# Search the library
python3 "/mnt/d/MASTER REFERENCE SAFE/reference_manager.py" search "your query"
```

**Build history:**
- Pre-2026-05-04: 773 entries (base corpus built March–April 2026)
- 2026-05-04: +233 entries from `D_LIBRARY_ingest_2026-04-26` DOI scan
  - 218 via CrossRef
  - 5 arXiv (Datasheets for Datasets, Model Cards, AI Incident Database, Generative AI vs. AGI, AI Authors survey)
  - 10 via repair pass (DOI content negotiation + OpenAlex)
  - 25 unresolvable (15 truncated OCR fragments; 10 valid-format DOIs unregistered — log: `exports/bibcitation/failed-dois-2026-05-04.txt`)

**Unprocessed gaps (institutional access needed):**
The 10 valid-format unresolvable DOIs include works from Cambridge (Politics & Gender, Hypatia), BMJ Medical Humanities, Brill, Sage Big Data & Society, Transformative Works and Cultures, JSTOR, SSRN, and Pomegranate. These require institutional access to identify and add manually.

**Relationship to EMERAULD vault:**
The MASTER REFERENCE SAFE is infrastructure, not a synthesis layer. The vault synthesises works into linked wiki notes; the SAFE maintains the raw citation list that those notes draw on. The two are complementary, not redundant.

**Candidate intake pipeline:**
Raw source candidates from the [[Library Master Reference Intake (2026-04-26)]] session are at:
`raw sources/D_LIBRARY_ingest_2026-04-26/henry/MASTER_REFERENCE_CANDIDATES_ALL.csv`

## Related
- [[Master Bibliography — Références bibliographiques 2025]]
- [[Master Reference Bridge Atlas — 2026-05-06]]
- [[MASTER BIBLIOGRAPHY — Theoretical Genealogy of LOTUS]]
- [[AI Governance Reference Stack — Annotated Library (Operational 2026-03-11)]]
- [[Library Master Reference Intake (2026-04-26)]]
- [[D Library — LIBRARY Intake Index (2026-04-26)]]
- [[Research and Papers MOC]]
- [[Personal and Projects MOC]]
