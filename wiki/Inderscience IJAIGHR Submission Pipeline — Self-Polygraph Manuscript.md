---
type: wiki
title: Inderscience IJAIGHR Submission Pipeline — Self-Polygraph Manuscript
aliases:
- IJAIGHR submission
- Inderscience submission pipeline
- Self-Polygraph submission checklist
- wiki/Inderscience IJAIGHR Submission Pipeline — Self-Polygraph Manuscript
tags:
- workflow
- deliverable
- submission
- inderscience
- ijaighr
- paper-pipeline
- runbook
- manuscript
- wiki
- inderscience-ijaighr-submission-pipeline-self-polygraph-manuscript-md
- polygraph
- pipeline
- color-blue
status: active
created: '2026-04-30'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Inderscience IJAIGHR Submission Pipeline — Self-Polygraph Manuscript.md
backlink_count: 5
backlinks:
- '[[Areas/Writing/Academic Paper Pipeline]]'
- '[[Areas/Writing/Manuscript Pipeline MOC]]'
- '[[Areas/Writing/Research and Papers MOC]]'
- '[[wiki/Self-Polygraph Manuscript — Inderscience Rewrite (2026-04-30)]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
---

# Inderscience IJAIGHR Submission Pipeline — Self-Polygraph Manuscript

> **Cluster:** Submission pipeline for [[Self-Polygraph Manuscript — Inderscience Rewrite (2026-04-30)|the manuscript]]; sister of [[Self-Polygraph Protocol and Suprametacognition|the protocol synthesis]] and [[Möbius Protocol — AI Self-Polygraph Template|the template]]. The same theoretical apparatus is targeted at IJAIGHR per [[Recursive Deterministic AI Governance — Method and Paper]]. Indexed in [[Evidence Discipline and Epistemics]] and [[Academic Paper Pipeline]].

## Summary
End-to-end submission workflow for [[Self-Polygraph Manuscript — Inderscience Rewrite (2026-04-30)]] to the **International Journal of Artificial Intelligence Governance and Human Rights (IJAIGHR)**. Captures journal fit, the manuscript's already-satisfied requirements, the six remaining submission tasks, and the operator-side gates a paper-pipeline runbook should enforce. Plugs into [[Academic Paper Pipeline]] alongside the [[PHAROS AI Ethics Submission — Springer Draft]] track. Source: `/home/cerebrhoe/inderscience_submission_notes.md`. Raw capture: `raw sources/2026-04-30_inderscience-ijaighr-submission-pipeline.md`.

## Context
This pipeline is the deliverable-execution counterpart to the manuscript itself. It is a workflow note in the same family as [[PHAROS Runbook SOP]] and [[HELIX Production Shipping Runbook — Web, iOS, Android (2026-04-19)]]: a checklist that converts a finished artifact into a shipped artifact through a publisher's own gating system. The runbook deliberately separates *what is in the manuscript* from *what the submission system needs around it* — because conflating the two has been a recurring submission-blocker in past pipeline runs (see [[Academic Paper Pipeline]]).

## Details

### Journal fit
**International Journal of Artificial Intelligence Governance and Human Rights (IJAIGHR)** publishes on the issues, challenges, and governance of AI within the context of human rights and human welfare. In-scope topics include: ethics, governance and legal issues of AI; social, political, regulatory and economic issues; individual rights and personhood; impacts on human rights; algorithmic impact assessments; lawfulness, fairness, transparency. Journal page: `https://www.inderscience.com/jhome.php?jcode=ijaighr`.

The manuscript's bounded claim — that AI self-description should be treated as a contestable evidentiary artifact, not self-authenticating testimony — sits cleanly inside the AIA/transparency band of the journal's scope.

### Already in the manuscript

- Factual abstract under 150 words.
- Keywords.
- Conflicts of interest declaration.
- Blinded main file (no author names, affiliations, biographies, or acknowledgements).
- Harvard-style in-text citation and references.
- Protocol appendix / source note.

### Six outstanding submission tasks

1. **PDF main file.** Inderscience requires the submission as PDF. The current `.md` working file must be rendered to PDF with the journal's preferred typography (UK spelling, Harvard refs).
2. **Four expert reviewer names.** Constraints — none on any Inderscience editorial board; none from any author institution; at least two from a country different from the authors. This is the most constraint-laden task; build the candidate list early.
3. **AI-use disclosure.** Inderscience asks for AI-use disclosure in **Acknowledgements**. Because the journal is double-blind, the disclosure cannot live in the blinded main file as identifying metadata; carry it as a separate editorial note or attach to the unblinded version on acceptance. Two suggested texts are given in the source notes (general + stronger specificity).
4. **Informed consent declaration.** Required *only* if research involved human participants. The Self-Polygraph paper analyses a researcher-maintained transcript with Claude; if no non-author humans were recruited, no declaration is required. **Do not add a false declaration.**
5. **Length risk.** Inderscience's preparing-articles page sets a 5,000–7,000-word soft cap on original articles, with longer pieces accepted on quality grounds. The current manuscript is ~10,000 words. Two options: trim to band, or plan to defend length on quality. Decide before the PDF render to avoid two formatting passes.
6. **UK spelling pass.** Inderscience requests UK spelling and terminology. The manuscript still contains some US spellings; run a spelling pass before PDF render. Tools: `aspell --lang=en_GB`, or LibreOffice with British dictionary, or a manual sweep.

### Operator-side gates not in the source notes

These belong in any paper-pipeline runbook even though Inderscience does not require them:

- **[[Diamond-Eyes — Aesthetic Refinement Skill|Diamond-Eyes pass]]** before PDF render — wisdom + care, not just technical correctness.
- **Citation cross-check** against [[AI Governance Reference Stack — Annotated Library (Operational 2026-03-11)]] — every cited author/year resolves to a verified entry, not a model-generated approximation. This is the [[Evidence Discipline and Epistemics]] gate.
- **Companion paper de-duplication** — the rewrite must not silently duplicate findings already published in [[Self-Polygraph Protocol and Suprametacognition]] or staged in [[The Wheel and the Watcher]]. Cross-reference openly to avoid self-plagiarism flags.
- **Decision: Paper B vs. this paper as second venue.** [[Recursive Deterministic AI Governance — Method and Paper]] is also in the pipeline; if both target Inderscience the order matters. Operator decides; record the decision in [[Complete Paper List — Martin Lepage Corpus]].

### Reference URLs (verified at source-capture time)

- Author Guidelines: `https://www.inderscience.com/mobile/inauthors/index.php?pid=70`
- Preparing Articles: `https://www.inderscience.com/mobile/inauthors/index.php?pid=71`
- Submissions Checklist: `https://www.inderscience.com/mobile/inauthors/index.php?pid=72`
- IJAIGHR journal page: `https://www.inderscience.com/jhome.php?jcode=ijaighr`

## Related

- [[Self-Polygraph Manuscript — Inderscience Rewrite (2026-04-30)]]
- [[Self-Polygraph Protocol and Suprametacognition]]
- [[PHAROS AI Ethics Submission — Springer Draft]]
- [[Complete Paper List — Martin Lepage Corpus]]
- [[Academic Paper Pipeline]]
- [[Evidence Discipline and Epistemics]]
- [[Diamond-Eyes — Aesthetic Refinement Skill]]
- [[AI Governance Reference Stack — Annotated Library (Operational 2026-03-11)]]
- [[PHAROS Runbook SOP]]
- [[2026-04-30_inderscience-ijaighr-submission-pipeline]]
- [[2026 - ISSN 2666-6596 ScienceDirect.com b]]
- [[Submission guidelines SYNTHESE]]
