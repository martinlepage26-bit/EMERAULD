---
type: wiki
title: Per-Paper Project Structure — Folder and File Architecture
aliases:
- Per-Paper Project Structure
- Paper Project Folders
- Scholarly Article Folder Structure
- wiki/Per-Paper Project Structure — Folder and File Architecture
tags:
- wiki
- per-paper-project-structure-folder-and-file-architecture-md
- journal
- abstract
- citation
- outline
- paper
- color-violet
status: active
created: '2026-05-31'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Per-Paper Project Structure — Folder and File Architecture.md
backlink_count: 5
backlinks:
- '[[wiki/Academic Paper Pipeline]]'
- '[[wiki/Chat Node Instructions — 16-Node Scholarly Paper Pipeline]]'
- '[[wiki/HENRY — Research Paper Writing System]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[session-state]]'
---

# Per-Paper Project Structure — Folder and File Architecture

## Summary

The canonical folder and file structure for each individual scholarly article project. Seven folders organize all materials from raw intake through final submission, with required files specified for each. Designed to preserve argument continuity across multiple model sessions without allowing any single chat to rewrite the project's purpose, evidence base, or citation rules. Companion to [[Chat Node Instructions — 16-Node Scholarly Paper Pipeline]].

## Context

This structure implements the [[Academic Paper Pipeline]] at the project level. Each paper gets its own project — named `[PAPER TITLE SHORT NAME] — Scholarly Article Project` (e.g., `Recursive AI Governance — Scholarly Article Project`). Integrates with [[HENRY — Research Paper Writing System]] and the [[Manuscript Pipeline MOC]].

## Folder Structure

### `00_PROJECT_CONTROL` — Governing documents

The highest-authority folder. No node may override documents here without explicit operator sign-off.

Required files:
- `PROJECT_BRIEF.md` — paper title, author (Martin Le Lepage), target journal, article length, central claim, object of analysis, method/approach, corpus, core literatures, current status
- `JOURNAL_GUIDELINES.pdf` or `JOURNAL_GUIDELINES.md` — if available; overrides all house defaults
- `STYLE_RULES.md` — formatting requirements, citation style, section word targets, journal overrides
- `CLAIM_REGISTER.md` — main claim, subclaims, source support, evidence status, unresolved risks
- `SECTION_PLAN.md` — section-by-section plan with word targets
- `MODEL_HANDOFF_LOG.md` — preserves output of every node; prevents later chats from restarting the project from scratch

---

### `01_RAW_MATERIALS` — Unsorted intake

Contains all raw and lightly sorted materials before inspection. No final claims should be drawn from this folder until materials have been inspected and moved into a structured research file.

Possible contents: raw notes, voice transcripts, earlier drafts, model outputs, source PDFs, screenshots, bibliographies, journal calls for papers, reviewer comments, loose theoretical fragments.

---

### `02_SOURCE_FIELD` — Inspected scholarly terrain

Required files:
- `REFERENCE_TREE.md` — citation lineages and works discovered through references
- `CANONICAL_WORKS.md` — major works the paper probably cannot ignore
- `ADJACENT_LITERATURES.md` — nearby fields that may matter but should not dominate without justification
- `SOURCE_MATRIX.md` — maps sources to functions: definition / method / historical context / theoretical support / empirical finding / critique / counterargument / background
- `SOURCE_GAPS.md` — missing or weak sources

---

### `03_OUTLINE_AND_ABSTRACT` — First stabilized architecture

Required files:
- `OUTLINE_V1.md` — diagnostic outline, not final structure
- `OUTLINE_REVIEW.md` — what the outline gets right, inflates, misses, and which sources need adding
- `ABSTRACT_V1.md` — first 150–250 word abstract
- `ABSTRACT_REVISED_AFTER_BODY.md` — produced after full paper body stabilizes

---

### `04_RESEARCH_BUNDLE` — Deep research material for drafting

Required files:
- `DEEP_RESEARCH.md` — main markdown research bundle
- `CLAIM_TO_SOURCE_MAP.md` — each major claim linked to sources
- `CITATION_CANDIDATES.md` — sources that may be used but require verification
- `PAGE_NUMBER_TRACKER.md` — exact pages, page gaps, unresolved page needs
- `METHOD_AND_CORPUS_NOTES.md` — what material is being analyzed and how

---

### `05_SECTION_DRAFTS` — Section-level drafts

Required files (in writing order):
1. `01_BACKGROUND_CONTEXT.md` — may begin early but remains author-governed
2. `02_LITERATURE_REVIEW.md`
3. `03_CONCEPTUAL_FRAMEWORK.md`
4. `04_ANALYSIS_FINDINGS.md`
5. `05_DISCUSSION.md`
6. `06_CONCLUSION.md`
7. `07_INTRODUCTION.md` — written last
8. `08_ABSTRACT_FINAL.md` — revised after body stabilizes

**Default writing order:** Literature Review → Conceptual Framework → Analysis and Findings → Discussion → Conclusion → Revised Abstract → Introduction.

---

### `06_VALIDATION` — Audits

Required files:
- `CITATION_AUDIT.md` — checks whether each citation supports the claim attached to it
- `REFERENCE_LIST_AUDIT.md` — removes unused sources, checks final bibliography consistency
- `CLAIM_AUDIT.md` — checks overstatement, vague claims, unsupported inference, missing limits
- `JOURNAL_CONFORMITY_AUDIT.md` — article length, formatting, citation style, headings, abstract format, keywords, anonymization, submission requirements
- `PEER_REVIEW_STRESS_TEST.md` — predicts likely reviewer objections and required revisions

---

### `07_FINAL_OUTPUTS` — Submission materials

Required files:
- `PAPER_FINAL.docx`
- `PAPER_FINAL.pdf` (if needed)
- `ABSTRACT_FINAL.md`
- `KEYWORDS.md`
- `COVER_LETTER.md` (if needed)
- `AUTHOR_BIO.md` (if needed)
- `SUBMISSION_CHECKLIST.md`

---

## Master Project Instruction

> "This project produces one peer-reviewable scholarly article. Do not generate the article in one pass. Work through the established paper pipeline: corpus formation, reference tree, outline, citation assessment, abstract, deep research bundle, literature review, validation, conceptual framework, works cited hardening, analysis and findings, discussion, conclusion, abstract revision, introduction, and final journal conformity. Use the uploaded journal submission guidelines as the highest formatting and citation authority. If no journal guidelines are provided, use the house default: Times New Roman 12pt, single spacing, one space after each paragraph, title page with paper title and author Martin Le Lepage, in-text citations `(Author, Year:Page)`. Assume 8,000 words unless journal requires otherwise. Keep discussion and conclusion separate unless journal requires combined format. Do not invent sources, page numbers, publication details, quotations, or journal requirements. Mark uncertain sources `[SOURCE TO VERIFY]`, missing pages `[PAGE NEEDED]`, unsupported claims `[CITATION NEEDED]`. Use only verified sources in final prose. Preserve the author's argument and voice. Strengthen structure, evidence, precision, and scholarly positioning without flattening prose into generic academic language. At the end of every response, provide a handoff note stating what was produced, which sources were used, what remains uncertain, which citations require verification, and what the next node should do."

## Related

- [[Chat Node Instructions — 16-Node Scholarly Paper Pipeline]]
- [[Academic Paper Pipeline]]
- [[HENRY — Research Paper Writing System]]
- [[Manuscript Pipeline MOC]]
- [[PHAROS Scholarly Publication Track]]
- [[Martin Lepage Publications — Annotated Bibliography and Verification Leads]]
