---
type: index
tags: [publications, graph-repair, progress, martin-lepage]
status: active
created: 2026-07-10
---

# Publication ↔ Reference Linking — Progress

**Goal:** link the 985 reference notes to the papers/chapters that cite them, bidirectionally; build a vault node per canonical publication; cross-link drafts to published versions.

**Scope chosen (2026-07-10):** Both — canonical CV publication notes as primary nodes + full-text draft matching + draft↔published cross-links.

## Phases
- [x] **A — Canonical publication notes** — DONE: 16 notes created in `Publications/Papers and Chapters/` (frontmatter type: publication + author/year/doi/tags; body: Summary, References cited [Phase C placeholder], Related draft, Corpus link).
- [x] **B — Full-text draft matching** — DONE: 13 papers matched, 265 citations, 145 matched (54%).: parse each full-text paper's bibliography, match to `references/` notes. Papers: 5 in-vault + ~12 unique `PHAROS_PAPERS_DB` drafts.
- [x] **C — Bidirectional links** — DONE: 8 working-paper notes created; 13 papers got '## References cited'; 85 reference notes got '## Cited in'. All 92 paper→ref + 124 ref→paper links verified resolving (0 broken).: `## Cited in` on each reference note (→ paper); `## References cited` on each paper (→ ref notes); draft ↔ canonical cross-links.

## Match baseline (5 vault papers)
109 citations, 64 matched (58%). Rivard paper 18/18. Media-studies papers (Buffy/Shadows) low — they cite works not in the reference library (Bhabha, Creed, Dyer, Buffy episodes) → correctly no note to link.

## Notes
- References library was built from AI-governance + Pagan/queer bibliographies; media-studies citations largely absent → expected low match there.
- Matcher: `scratchpad/match_refs.py` (surname+year, title-overlap disambiguation). Match map: `scratchpad/ref_matches.json`.
- Draft→published known links: "For Her Alone to Wield — HENRY Draft" → 2025 Slayage "Every Hair a Battle Scar".

## Log
- 2026-07-10: Scoped. Baseline matcher run. Starting Phase A.
- 2026-07-10: Phase A complete (16 canonical publication notes). Next: Phase B — dedupe full-text paper set (5 vault + PHAROS_PAPERS_DB drafts), run matcher across all, map paper→refs.

## Library widening (2026-07-10)
- Added **59 new reference notes** (media-studies: Bhabha, Creed, Dyer, Chow, Muñoz, Wilcox, Jenkins, Jowett, Pender, Taylor, Shohat & Stam, Negra & Tasker, Berlant & Stewart, Star & Ruhleder, Fraser; AI-governance/methods: Floridi, Doshi-Velez, Dryzek, Crenshaw 1991, Barocas-Hardt-Narayanan, SHAP, LIME, chain-of-thought, Argyris & Schön, Schön, Scott, Sculley, Mittelstadt, Hagendorff, Mökander×2, Chalmers, Nagel, Nisbett & Wilson, Toulmin, Orseau & Armstrong, Lincoln & Guba, Creswell & Poth, Lorde, Dominelli, Ramsden, Roberts, etc.; cultural: Mauss (Eng), Weber (Eng), Huysmans, Constant, Mellet, Richardson et al., Borges, Cao). Also ingested to SAFE master (985->1044) + HENRY annotations + rebuild.
- Self-citations (Lepage — La Déesse, Religiosités) linked to the canonical publication notes.
- **Re-match (true, auto-sections excluded): 214/256 (83%), up from 145/265 (54%).** Re-linked (merge-aware/idempotent): 13 papers "References cited"; **144 reference notes "Cited in"**; 194 paper-ref links; all 183 paper->ref + 198 ref->paper links verified resolving (0 broken). Reference library now 1044 notes.
