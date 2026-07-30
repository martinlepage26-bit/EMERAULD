---
type: index
tags: [themes, graph-repair, progress]
status: active
created: 2026-07-10
---

# Thematic Linking — Progress

**Goal:** make research themes first-class vault nodes; link papers + references to their themes bidirectionally (frontmatter tags + backlinks).

## Theme taxonomy (8 canonical, = SAFE theme labels; references already tagged)
1. AI Governance, Policy & Regulation — `ai_governance`
2. Governance & Institutions — `governance`
3. Power, Security & Political Control — `power_security`
4. Ritual, Religion & Spirituality — `ritual_spirituality`
5. Gender, Queer & Embodiment Studies — `gender_queer`
6. Media & Cultural Analysis — `media_culture`
7. Research Methods — `methods`
8. Posthumanism, Ecology & the Anthropocene — `posthuman_ecology`

Fine-grained paper/new-ref tags map into these (pagan-studies/wicca/magic→ritual; queer-studies/transgender/masculinities→gender_queer; cultural-studies/buffy/film→media_culture; ai/interpretability/auditing/fairness→ai_governance; etc.).

## Phases
- [x] A — Create 8 theme hub notes in `themes/` (description + Papers list + Reference-library pointer + related MOC).
- [x] B — Backlink the ~29 papers to their theme notes (`## Themes` section) + theme→paper links.
- [x] C — Add `## Themes` to each of 1044 reference notes (from its existing tags → theme note[s]). Batched.

## Log
- 2026-07-10: Taxonomy derived from existing tags + MOCs. Starting Phase A.

## Result (2026-07-10)
- 8 theme hub notes + [[Research Themes]] index (linked from Home).
- 25/30 papers backlinked to themes.
- References themed: 725 by existing tag + 291 by content-inference (thematic reading) = **1000/1043** (~96%); 43 left un-themed (OCR fragments/too-short). Theme tags written to frontmatter for inferred ones.
- All **1392 `## Themes` links verified resolving (0 broken)**. Base renamed Untitled.base -> Source Library.base.

## Tightening + base views (2026-07-10)
- (a) Re-classified the 291 content-inferred notes with a **precise lexicon** (dropped broad noise: bare power/analysis/narrative/control/media). Fixed mis-files (Bourdieu/Graeber/Foucault no longer in Power/Security; Huysmans correctly retained). Coverage 951/1043 themed (down from 1000, precision up); ~92 un-themed (OCR fragments + a few hard cases). All theme links resolve (0 broken).
- (b) Added **8 per-theme live views** to `Source Library.base` (filtered by theme tag) + the base is linked from the theme notes and [[Research Themes]].

## Second thematic reading — 5 new themes + full coverage (2026-07-10)
Prompt: *"read the ~92 un-themed notes and theme them, find more themes and re-read and link the vault."*
- **Read all 92 un-themed notes** (citation + annotation) — clear clusters emerged that the 8-tag SAFE system never had labels for.
- **5 new themes created** (hubs in `themes/`, added to [[Research Themes]] → now **13 themes**):
  9. [[Social Theory]] — `social_theory` (Durkheim, Weber, Giddens, Bourdieu, Lévi-Strauss, recognition/agency, deviance) — **157 refs**
  10. [[Social Psychology and Interaction]] — `social_psychology` (mimicry/chameleon effect, ostracism, self-presentation, flow) — **23 refs**
  11. [[Health, Medicine and Clinical Practice]] — `health_medicine` (telemedicine, nursing, drugs/devices, physiology) — **74 refs**
  12. [[Literature and Narrative Theory]] — `literature` (novels, narratology, authorship, fairy tales, Rivard corpus) — **50 refs**
  13. [[Art and Aesthetics]] — `art_aesthetics` (participatory/relational art, theatre, dance notation) — **23 refs**
- **All 92 un-themed notes hand-mapped** (read individually, not keyword-guessed) into old+new themes.
- **Whole corpus re-scanned** to cross-list the new themes onto already-themed notes → **320 reference notes updated** (Social Theory +157, Health +74, Literature +50, Social Psychology +23, Art +23, plus old-theme corrections).
- Coverage now **1043/1043 references themed (100%)**; **1610 `## Themes` links, 0 broken**. Papers 25/30 (Rivard paper now carries Literature).
- Added **5 new per-theme views** to `Source Library.base` (13 theme views total). Base YAML validated.
