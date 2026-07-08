---
type: wiki
title: Chat Node Instructions — 16-Node Scholarly Paper Pipeline
aliases:
- Chat Node Instructions
- 16-Node Paper Pipeline
- Paper Node Protocol
tags:
- areas
- chat
- instruction
- literature
- wiki
- writing
status: active
domain: writing
created: '2026-05-31'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/Writing/Chat Node Instructions — 16-Node Scholarly Paper Pipeline.md
backlink_count: 9
backlinks:
- '[[Areas/Writing/Academic Paper Pipeline]]'
- '[[Areas/Writing/HENRY — Research Paper Writing System]]'
- '[[Areas/Writing/Per-Paper Project Structure — Folder and File Architecture]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[archive/session-state/session-state-003]]'
- '[[artifacts/stale-projects-2026-07-04]]'
- '[[artifacts/stale-projects-2026-07-05]]'
- '[[artifacts/stale-projects-2026-07-06]]'
- '[[artifacts/stale-projects-2026-07-07]]'
---

# Chat Node Instructions — 16-Node Scholarly Paper Pipeline

## Summary

A complete node-by-node instruction set for producing a peer-reviewable scholarly article across 16 dedicated chat sessions. Each node receives a specific instruction, operates on defined inputs, and produces required output files. The pipeline prevents any single chat from controlling the whole paper, preserving argument continuity and citation discipline across sessions. Companion to [[Per-Paper Project Structure — Folder and File Architecture]].

## Context

This is the operating protocol for the [[Academic Paper Pipeline]] and integrates with [[HENRY — Research Paper Writing System]] for the operator's scholarly publication track. Each node maps onto a stage in the [[Manuscript Pipeline MOC]]. The pipeline enforces the principle that scholarly papers must not be generated in one pass — corpus formation, evidence discipline, and argument structure each require separate review cycles. Author name used in defaults: Martin Le Lepage.

## The 16 Nodes

**NODE 00 — PROJECT INTAKE**
Chat name: `00 — Intake and Corpus Formation`
Purpose: Gather everything that exists. Build the project map. Do not write the paper.
Instruction: Inspect uploaded materials, identify what kind of paper this can become, produce PROJECT_BRIEF.md. Do not draft. Do not invent. Separate raw ideas, sources, drafts, theoretical fragments, method notes, and journal requirements.
Required output: `PROJECT_BRIEF.md`, `MATERIALS_INVENTORY.md`, `UNCERTAINTY_REGISTER.md`

---

**NODE 01 — REFERENCE TREE**
Chat name: `01 — Reference Tree and Field Mapping`
Purpose: Map the scholarly field before drafting.
Instruction: Identify citation tree, canonical works, adjacent literatures, missing sources, and peer-review expectations. Separate direct source support / theoretical background / method support / contextual support / critique / counterargument. Mark unverified sources `[SOURCE TO VERIFY]`, missing pages `[PAGE NEEDED]`.
Required output: `REFERENCE_TREE.md`, `CANONICAL_WORKS.md`, `ADJACENT_LITERATURES.md`, `SOURCE_GAPS.md`, `SOURCE_MATRIX.md`

---

**NODE 02 — OUTLINE ARCHITECT**
Chat name: `02 — Outline Architect`
Purpose: Turn corpus and field map into a diagnostic paper structure.
Instruction: Build scholarly article outline from project brief, field map, source matrix. Expose argument architecture: object → problem → gap → method → literature → framework → analysis → findings → discussion → conclusion. Default: 8,000 words. Default section targets: lit review ~1,000w, conceptual framework ~1,200w, analysis ~1,500w, discussion 800–1,000w, conclusion 800–1,200w.
Required output: `OUTLINE_V1.md`, `SECTION_PLAN.md`, `CLAIM_REGISTER_INITIAL.md`

---

**NODE 03 — OUTLINE REVIEW AND CITATION ASSESSMENT**
Chat name: `03 — Outline Review and Citation Assessment`
Purpose: Test the outline before abstracting.
Instruction: Stress-test outline against source base. Identify weak claims, missing literatures, citation gaps, theoretical overreach, unsupported transitions, reviewer objections. Do not invent sources. Mark plausible-but-unverified as `[SOURCE TO VERIFY]`. Revise only where evidence requires it.
Required output: `OUTLINE_REVIEW.md`, `REVISED_SECTION_PLAN.md`, `CITATION_ASSESSMENT.md`, `PEER_REVIEW_RISK_REGISTER.md`

---

**NODE 04 — ABSTRACT**
Chat name: `04 — Abstract V1`
Purpose: Create the first compact version of the paper.
Instruction: Write 150–250 word scholarly abstract stating object, problem, approach/method, corpus, main finding, contribution. Do not overclaim. If method/corpus/findings are unstable, mark instability clearly after the abstract.
Required output: `ABSTRACT_V1.md`, `ABSTRACT_RISK_NOTE.md`

---

**NODE 05 — DEEP RESEARCH BUNDLE**
Chat name: `05 — Deep Research Bundle`
Purpose: Create the research file that feeds the literature review and later sections.
Instruction: Organize sources by function: definition / field terrain / theory / method / empirical support / historical context / critique / counterargument / stakes. Map each major claim to source support. Mark missing citations and pages. Identify which sources must be read more closely before drafting.
Required output: `DEEP_RESEARCH.md`, `CLAIM_TO_SOURCE_MAP.md`, `CITATION_CANDIDATES.md`, `PAGE_NUMBER_TRACKER.md`

---

**NODE 06 — LITERATURE REVIEW BUILDER**
Chat name: `06 — Literature Review Builder`
Purpose: Draft the literature review from the research bundle.
Instruction: Write scholarly literature review ~1,000 words. Organize around problems, debates, concepts, and gaps — not source-by-source summaries. Use only sources in the research bundle. Citation format: journal style if uploaded, else `(Author, Year:Page)`. End with validation note identifying unsupported claims, missing citations, missing pages.
Required output: `02_LITERATURE_REVIEW.md`, `LIT_REVIEW_VALIDATION_NOTE.md`

---

**NODE 07 — LITERATURE REVIEW VALIDATION**
Chat name: `07 — Literature Review Validation`
Purpose: Harden the literature review before theory writing.
Instruction: Audit for citation accuracy, source relevance, missing canonical works, unsupported claims, inflated contribution, weak transitions, unused references, unclear field positioning. Audit structure first, then revise. Mark uncertain sources and pages. Remove or flag any reference that does not perform a clear function.
Required output: `LIT_REVIEW_AUDIT.md`, `02_LITERATURE_REVIEW_REVISED.md`, `REFERENCE_REMOVAL_CANDIDATES.md`

---

**NODE 08 — CONCEPTUAL FRAMEWORK**
Chat name: `08 — Conceptual Framework and Theoretical Background`
Purpose: Build the conceptual apparatus that governs the analysis.
Instruction: Write ~1,200 words. Name frameworks, define core constructs, explain relationships, justify fit to research question, show how they guide analysis. Before drafting, harden works cited list from literature review and source matrix. Every concept must perform analytic work. No decorative theory.
Required output: `03_CONCEPTUAL_FRAMEWORK.md`, `CONCEPT_SOURCE_MAP.md`, `WORKS_CITED_HARDENING_NOTE.md`

---

**NODE 09 — WORKS CITED HARDENING**
Chat name: `09 — Works Cited Hardening`
Purpose: Remove citation noise before analysis.
Instruction: Compare literature review, conceptual framework, source matrix, and current works cited. Remove unused references. Identify missing references required by claims already made. Identify sources cited in prose but absent from reference list, and vice versa. Mark uncertain bibliographic details `[DETAIL TO VERIFY]`.
Required output: `REFERENCE_LIST_AUDIT.md`, `WORKS_CITED_REVISED.md`, `MISSING_CITATIONS_LIST.md`

---

**NODE 10 — ANALYSIS AND FINDINGS**
Chat name: `10 — Analysis and Findings`
Purpose: Write the evidentiary core of the paper.
Instruction: Write ~1,500 words. Use conceptual framework to analyze material — do not simply repeat theory. Each major finding must have: claim, mechanism, implication. Identify implication type: scholarly / institutional / legal / clinical / labor / epistemic / cultural / political. Separate direct evidence from supported inference. Mark `[CITATION NEEDED]` and `[PAGE NEEDED]`.
Required output: `04_ANALYSIS_FINDINGS.md`, `FINDINGS_CLAIM_MAP.md`, `ANALYSIS_VALIDATION_NOTE.md`

---

**NODE 11 — DISCUSSION**
Chat name: `11 — Discussion`
Purpose: Explain the significance of the findings.
Instruction: Write 800–1,000 words. Explain what the findings change, clarify, complicate, or make newly visible in the field. Do not summarize findings. Do not introduce new literature review. Connect back to literature review and conceptual framework. Name consequence domain of each implication. Keep separate from conclusion.
Required output: `05_DISCUSSION.md`, `DISCUSSION_CLAIM_MAP.md`

---

**NODE 12 — CONCLUSION**
Chat name: `12 — Conclusion`
Purpose: Close the article without collapsing into repetition.
Instruction: Write 800–1,200 words. Restate contribution, clarify limits, identify what analysis has shown, explain what future research or practice must address. Do not introduce new arguments the paper has not earned. Do not merge with discussion unless journal requires it.
Required output: `06_CONCLUSION.md`, `LIMITATIONS_AND_FUTURE_WORK_NOTE.md`

---

**NODE 13 — ABSTRACT REVISION**
Chat name: `13 — Abstract Revision After Body`
Purpose: Make the abstract match the finished paper.
Instruction: Revise 150–250 word abstract to match completed body. Remove claims final paper does not support. Add findings or limits that became central during drafting. Do not preserve first abstract out of loyalty. Abstract must describe the paper that now exists.
Required output: `08_ABSTRACT_FINAL.md`, `ABSTRACT_ALIGNMENT_NOTE.md`

---

**NODE 14 — INTRODUCTION**
Chat name: `14 — Introduction`
Purpose: Write the introduction last.
Instruction: Write after body has stabilized. Define object, problem, scholarly gap, method/approach, central claim, contribution, article structure. Do not use generic openings. Do not begin with "In recent years" unless topic requires historical opening. Introduce the final article, not the earlier plan.
Required output: `07_INTRODUCTION.md`, `INTRODUCTION_ALIGNMENT_NOTE.md`

---

**NODE 15 — FINAL JOURNAL CONFORMITY**
Chat name: `15 — Final Journal Conformity and Submission Audit`
Purpose: Prepare the paper for submission.
Instruction: Audit full article against uploaded journal submission guidelines — journal guidelines override all house defaults. Check: word count, title page, abstract length, keywords, headings, citation style, reference list, anonymization, file format, spacing, font, margins, figures/tables, ethics statements, conflict of interest, acknowledgments, submission metadata. House defaults if no guidelines: Times New Roman 12pt, single spacing, one space after each paragraph, title page with paper title and author Martin Le Lepage, in-text citations `(Author, Year:Page)`.
Required output: `JOURNAL_CONFORMITY_AUDIT.md`, `PAPER_FINAL_READY.md`, `SUBMISSION_CHECKLIST.md`, `FINAL_RISK_REGISTER.md`

---

## Master Pipeline Instruction

> "This project produces one peer-reviewable scholarly article. Do not generate the article in one pass. Work through the established paper pipeline: corpus formation, reference tree, outline, citation assessment, abstract, deep research bundle, literature review, validation, conceptual framework, works cited hardening, analysis and findings, discussion, conclusion, abstract revision, introduction, and final journal conformity. Use uploaded journal submission guidelines as the highest formatting and citation authority. If no journal guidelines are provided, use the house default: Times New Roman 12pt, single spacing, one space after each paragraph, title page with paper title and author Martin Le Lepage, in-text citations `(Author, Year:Page)`. Assume 8,000 words unless journal requires otherwise. Keep discussion and conclusion separate unless journal requires combined format. Do not invent sources, page numbers, publication details, quotations, or journal requirements. Mark uncertain sources `[SOURCE TO VERIFY]`, missing pages `[PAGE NEEDED]`, unsupported claims `[CITATION NEEDED]`. At end of every response, provide a handoff note."

## Related

- [[Per-Paper Project Structure — Folder and File Architecture]]
- [[Academic Paper Pipeline]]
- [[HENRY — Research Paper Writing System]]
- [[Manuscript Pipeline MOC]]
- [[Martin Lepage Publications — Annotated Bibliography and Verification Leads]]
- [[PHAROS Scholarly Publication Track]]
