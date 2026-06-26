---
type: wiki
aliases: []
tags: [library, docsort, triage, cleanup, reference]
status: active
created: 2026-05-05
updated: 2026-05-05
---

# D Library — Review Unreadable Cleanup (2026-05-04)

## Summary

Three-phase cleanup of the 641 files that [[DocSort — Dr. Sort Automation Project|DocSort]] had routed to `D:\LIBRARY\Review\Unreadable` because it could not extract text from them. All three phases completed in a single [[CLAUDEX]] session on 2026-05-04. The folder is now empty; all files are filed. The [[MASTER REFERENCE SAFE — Canonical Bibliography System]] grew from 990 → 998 entries as a byproduct.

## Context

The Unreadable subfolder was a residual from the [[D Library — LIBRARY Intake Index (2026-04-26)|2026-04-26 D:\LIBRARY ingest]] — DocSort had classified and renamed files but could not read the content of 641 of them (image-based PDFs, encrypted files, malformed DOCX). A prior OCR pass (also 2026-04-26) had already extracted text from 110 of them and produced converted markdown for all 641 via [[Library Master Reference Intake (2026-04-26)|Henry's intake pipeline]]. This session used those artifacts to finish the job.

Two structural problems were present going in: DocSort had triple-repeated every filename (a re-rename bug producing names like `1971 - tax.pdf - 1971 - tax.pdf.pdf.pdf`), and the files had never been triaged into the LIBRARY folder hierarchy.

## Details

### Phase 1 — Filename Cleanup

631 of 641 files renamed. The repair rule: truncate at the first occurrence of the file's own extension in the filename. 10 files were already clean. 0 naming conflicts. Produced clean names like `1971 - tax_or_finance [2].pdf`.

### Phase 2 — Synthesis (MASTER REFERENCE SAFE)

The prior OCR pass had extracted DOIs and ISBNs into a Henry candidates CSV (100 entries, 91 DOIs, 20 ISBNs). Cross-referenced against the [[MASTER REFERENCE SAFE — Canonical Bibliography System|MASTER REFERENCE LIST]] (990 entries at the time).

- 274 DOI matches already present
- 41 raw new DOIs → deduplicated to 23 unique valid → 3 added after content inspection:
  - Attwood, A. (2018). Jurassic ethics: Using film in bioethics education. *Medical Humanities*, 44(1). https://doi.org/10.1136/medhum-2017-011255
  - Baril, A. (2020). Confessing society and epistemic injustice: Toward a queer crip analytic of knowledge production. *Hypatia*, 35(1), 33–56. https://doi.org/10.1017/hyp.2019.31
  - Price, M. (2011). *Mad at School: Rhetorics of Mental Disability and Academic Life*. Ann Arbor: University of Michigan Press. https://doi.org/10.3998/dcbooks.9439946.0001.001
- 20 skipped: already in list under different DOI form, truncated OCR artifacts, or malformed hyphenation

MASTER REFERENCE LIST: **990 → 998 entries**.

### Phase 3 — Triage

Files moved into LIBRARY structure using a two-pass approach:

**Pass 1 (filename rules):** 641 files sorted by DocSort category in filename and presence of "Martin Lepage."

**Pass 2 (content rules):** 177 files that could not be classified by filename alone were re-read via their converted markdown and reclassified.

Final destinations across both passes:

| Destination | Count |
|---|---|
| `Mine/policy/` | ~255 (Martin's personal and admin docs) |
| `Not_Mine/notes/` | ~189 (journal articles, academic papers) |
| `Review/Low_Confidence/` → emptied | 0 |
| `Not_Mine/report/` | ~71 (institutional reports) |
| `Not_Mine/policy/` | 34 (government/policy docs) |
| `Not_Mine/book/` | ~33 |
| `Not_Mine/thesis/` | 37 |
| `Not_Mine/book_chapter/` | ~16 |
| `Review/Uncategorized/` | 5 (blank OCR — genuinely unreadable) |
| **Deleted** | 7 (raw PDF binary blobs — `%PDF-1.x.txt` artifacts) |

Content in `Mine/policy/` includes: UQAM/Laval transcripts, RAMQ health card, PhD diploma (2018), Fonds Gérard-Dion and Andrew W. Mellon fellowship files, CRA tax docs, manuscript chapters (Buffy book prospectus, Willow Rosenberg chapter), COMPASSai test reports.

Notable papers now in `Not_Mine/notes/`: Brown & Michael (2003) "A Sociology of Expectations," Amiraux & Araya-Moreno "Pluralism and Radicalization," Hedström/Ylikoski causal mechanisms, Sara Ahmed *Cultural Politics of Emotion*, Orientalism (Said).

5 genuinely unreadable files (blank OCR even after repair) remain in `Review/Uncategorized/`: 2016 and 2024–2025 `ocr_needed` PDFs with no extractable content.

## Related

- [[Governance and PHAROS MOC]]
- [[Bridge - Dr. Sort Filename Normalization 2026-05-06]]
- [[Research and Papers MOC]]
- [[Writing and Novels MOC]]
- [[D Library — LIBRARY Intake Index (2026-04-26)]] — original ingest session
- [[Library Master Reference Intake (2026-04-26)]] — OCR/markdown artifacts used in Phase 2–3
- [[D Library — Genealogy Flags and Cleanup Leads (2026-04-26)]] — parallel cleanup track
- [[MASTER REFERENCE SAFE — Canonical Bibliography System]] — bibliography system updated in Phase 2
- [[Personal and Projects MOC]] — this note indexed here
- [[2015 - book_or_monograph_1.pdf - 2015 - book_or_monograph_1.pdf.pdf - 2015 - book_or_monograph_1.pdf]]
- [[2023 - ocr_needed.pdf - 2023 - ocr_needed.pdf.pdf - 2023 - ocr_needed.pdf - 2023 - ocr_needed.pdf.pd]]
- [[2026 - Martin Lepage - J an 28 , 2026 [2]]]
- [[2026 - Martin Lepage - J an 28 , 2026]]
- [[2026 - Martin Lepage - J an 29, 2026]]
- [[Andrew W. Mellon Postdoctoral Fellowshi... How to Apply Penn Humanities Forum]]
- [[Andrew W. Mellon Postdoctoral Fellowship in the Humanities Vitae]]
- [[Digitalisation, artificial intelligence... workplace_ Shaping the future of work]]
- [[How gay, bisexual and other men who have sex with men living with HIV experience sexual dysfunction]]
- [[Mail iCloud - your chapter for edited volume]]
- [[Review_2020_white_Correspondences.pdf - Review_2020_white_Correspondences.pdf.pdf - Review_2020_whit]]
- [[The Cultural Politics of Emotion]]
- [[DocSort — Setup & Reference]]
