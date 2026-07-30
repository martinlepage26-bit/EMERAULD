---
type: wiki
aliases:
  - Master Annotated Reference List
  - annotated bibliography hub
  - reference corpus hub
tags: [bibliography, reference, hub, research, knowledge-infrastructure]
status: active
created: 2026-07-14
updated: 2026-07-14
---

# Master Annotated Reference List

## Summary

This is the hub for the vault's annotated reference corpus: **1,124 reference notes** in `references/`, each carrying a citation, a scholarly annotation, and a theme assignment. Every one of those notes links back here. The corpus is generated from the [[MASTER REFERENCE SAFE — Canonical Bibliography System]], whose canonical list now holds **1,194 entries**, and it is bridged into the vault's thematic layer via [[Research Themes]].

## Context

The reference corpus is infrastructure, not synthesis. The [[MASTER REFERENCE SAFE — Canonical Bibliography System]] maintains the raw citation list and its annotations; this vault turns each entry into a linked note so citations become navigable alongside the notes that actually use them. It feeds [[Research and Papers MOC]], [[Governance and PHAROS MOC]], and the writing tracked in [[Writing and Novels MOC]].

For the theme-level bridge between citations and vault surfaces, see [[Master Reference Bridge Atlas — 2026-05-06]]. For the working bibliography of the paper corpus, see [[Master Bibliography — Références bibliographiques 2025]].

## Details

**Location:** `references/` — one note per entry
**Source of truth:** `E:\MASTER REFERENCE SAFE\canonical\MASTER REFERENCE LIST.txt`
**Annotated views:** `E:\MASTER REFERENCE SAFE\annotated\` (themes, alphabetical, publication date, CSV)
**Durable annotations:** `annotated/henry_annotations.json` — keyed by exact citation line, preserved across rebuilds

### Themes

Each reference note is assigned to one or more themes. The theme notes live in `themes/`:

- [[AI Governance, Policy and Regulation]]
- [[Governance and Institutions]]
- [[Power, Security and Political Control]]
- [[Research Methods]]
- [[Gender, Queer and Embodiment Studies]]
- [[Ritual, Religion and Spirituality]]
- [[Media and Cultural Analysis]]
- [[Posthumanism, Ecology and the Anthropocene]]
- [[Social Theory]]
- [[Social Psychology and Interaction]]
- [[Health, Medicine and Clinical Practice]]
- [[Literature and Narrative Theory]]
- [[Art and Aesthetics]]

### State (2026-07-14)

| | count |
|---|---|
| Canonical entries in the SAFE | 1,194 |
| Reference notes in `references/` | 1,124 |
| Entries withheld (corrupted source lines) | 71 |

**Coverage gap is deliberate.** 71 canonical lines are not citations — they are OCR fragments, page-number scraps, or two references merged into a single line by a bad reference-section scrape. They are logged in the intake report rather than turned into notes, because a note built on a corrupted line would put a garbage node into the graph. See the *Known data quality issues* section below.

### Known data quality issues

Roughly **7% of the canonical list (86 of 1,194 entries) is damaged**, inherited from PDF reference-section scraping:

- **~32 entries are not citations at all** — URL fragments, bare page ranges, stray sentences.
- **~54 entries have two references merged into one line**, so the parsed title carries a second author, a page range, or a second year.

These are source-level defects in `MASTER REFERENCE LIST.txt`, not vault defects. Cleaning them at source and re-exporting would raise `references/` coverage to the full corpus.

## Related

- [[MASTER REFERENCE SAFE — Canonical Bibliography System]]
- [[Master Reference Bridge Atlas — 2026-05-06]]
- [[Master Bibliography — Références bibliographiques 2025]]
- [[Research Themes]]
- [[Research and Papers MOC]]
- [[Governance and PHAROS MOC]]
