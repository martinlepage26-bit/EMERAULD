---
type: wiki
aliases:
  - PAPER BUILDER Source Bundle
  - HENRY Origin Bundle
  - ubuntu disk bundle
tags: [henry, paper-builder, voice-spec, genealogy, build-artifact, writing-system, version-genealogy]
status: active
created: 2026-05-03
updated: 2026-07-30
---

# PAPER BUILDER — Source Bundle and HENRY Origin

## Summary
The canonical source bundle from which [[HENRY — Research Paper Writing System|HENRY]] was built. Located at `C:\Users\softinfo\Desktop\ubuntu disk\` (WSL: `/mnt/c/Users/softinfo/Desktop/ubuntu disk/`). The bundle contains the Martin-named originals; `/home/cerebrhoe/HENRY/` contains the renamed output. The transformation is explicit and scriptable: `rebuild_henry_bundle.py` converts all `PAPER BUILDER → HENRY` and `Martin Voice Spec → HENRY Voice Spec` across files. This is the missing upstream node in the [[Martin Voice Spec — Version Genealogy|voice spec genealogy]] and the [[HENRY — Research Paper Writing System|HENRY writing system]] provenance chain.

## Context
Discovered 2026-05-03. [[SYSTEM CHECK]] (item 10) had previously flagged `paper.builder` and `HENRY` under "MODELS folder on Desktop — no git, no documented relationship to main projects" — the existence was noted but the relationship was not traced. This note completes that trace. The "ubuntu disk" folder name does not match the "MODELS folder" reference in SYSTEM CHECK; possible rename or separate folder. Two gaps closed: (1) HENRY's design origin (the paper builder app spec and social studies workbook), and (2) Martin's voice CODE provenance (the JSON operator spec was Martin-named in the source, HENRY-named in the output). Relevant to [[Version Genealogy System]], [[HEPHAISTOS Agent Architecture]], and [[Martin Lepage Professional Identity]].

Raw source capture at: `raw sources/paper-builder-origin-bundle/`

## Bundle Contents

| File | Purpose | Status |
|---|---|---|
| `Martin Voice Spec v3 OFFICIAL (2).pdf` | Official v3 voice spec PDF — source of `HENRY Voice Spec v3 OFFICIAL (2).pdf` | Present; not copied (binary, already in HENRY/) |
| `Martin's voice CODE.txt` | Machine-readable JSON operator spec — 11 operators, paragraph contract, lexicon EN/FR | Captured in raw sources |
| `PAPER BUILDER APP.txt` | 6-phase inspectable workflow spec (Lock → Spine → Coupling → Passes → Verify → Release) | Captured |
| `PAPER BUILDER APP WF.txt` | Same workflow in form-fillable tokenized format | Captured |
| `PAPER BUILDER APP VOCAB.txt` | Vocabulary reference — **0 bytes; empty file; open gap** | Captured (empty) |
| `PAPER BUILDER WF Sum.txt` | Plain-language workflow summary | Captured |
| `PAPER BUILDER WK SocialStudies.txt` | Social studies / humanities variant with **relational coupling** replacing three-arm coupling | Captured |
| `paper builder.txt` | Operational runbook v3 ("Write notes → peer-reviewed paper") | Captured |
| `martin_voice_optimizer.py` | Voice profiler tool: detects CLAIM-EARLY, ANCHOR-INJECTION, HEDGE-CALIBRATION flags | Captured |
| `bib_rebuild.py` | Bibliography rebuilder (Crossref + OpenAlex lookups, Harvard-ish output) | Captured |
| `rebuild_henry_bundle.py` | **Build script**: copies bundle and renames Martin → HENRY throughout | Captured |

## Key Genealogical Finding: rebuild_henry_bundle.py

The script is the explicit transform:
- `PAPER BUILDER` → `HENRY` (file names and content)
- `Martin Voice Spec` → `HENRY Voice Spec`
- `Martin's voice CODE` → `HENRY voice CODE`
- `martin_voice_optimizer.py` → `henry_voice_optimizer.py`

This means every `HENRY/` file at `/home/cerebrhoe/HENRY/` is a renamed copy of a file from this bundle. The source bundle is Martin-named; the HENRY bundle is the deployed output.

2026-07-30 metadata resolution: the recovered filesystem and archive hashes confirm `Martin's voice CODE.txt` as the Martin-named source and `HENRY voice CODE.txt` as the later machine-readable HENRY output. See [[genealogy/Voice Operator Lineage - Metadata Resolution 2026-07-30]].

## Architectural Evolution: Relational Coupling

`PAPER BUILDER WK SocialStudies.txt` contains an important refinement: the "three-arm coupling" model (academic arm / artistic arm / ritual arm) was replaced with a **relational coupling** model using three registers:

| Original (three-arm) | Evolved (relational) |
|---|---|
| Academic arm | Artifact register |
| Artistic arm | Procedure register |
| Ritual arm | Proof regime register |

The evolution distinguishes between *having anchors* in each arm and *making the relation between anchors explicit* — a stricter test that the three-arm model did not enforce. This is the more current form of the paper-writing method.

## Open Gaps

- `PAPER BUILDER APP VOCAB.txt` is empty (0 bytes) — vocabulary reference was never populated or was deleted
- `martin_voice_optimizer.py` is a standalone tool (note header: "AGATHA, DO NOT RUN") — it predates the HENRY rename; its operational status is unclear
- The PDF (`Martin Voice Spec v3 OFFICIAL (2).pdf`) is not yet directly accessible in the vault via semantic search

## Related

- [[HENRY — Research Paper Writing System]] — the deployed output of this source bundle
- [[Martin Voice Spec — Version Genealogy]] — the version lineage now updated to include ubuntu disk origin
- [[genealogy/Voice Operator Lineage - Metadata Resolution 2026-07-30]] — 2026-07-30 metadata resolution for HENRY voice code and operator chronology
- [[Martin Voice Spec — Stage Map]] — functional stage map for runtime use
- [[Version Genealogy System]] — hub for all version genealogy work
- [[Martin Lepage Professional Identity]] — authorial identity the voice spec produces
- [[HEPHAISTOS Agent Architecture]] — architecture in which HENRY operates
- [[AI Personas — Agatha, DOTTIE, and MOBI]] — the "AGATHA, DO NOT RUN" header on martin_voice_optimizer.py links to this persona genealogy
