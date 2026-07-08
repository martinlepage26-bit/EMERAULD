---
type: wiki
title: LOTUS Premium Spec
aliases:
- LOTUS Premium Spec
- Dr. Sort Premium Vision
- LOTUS application spec
- LOTUS Dr. Sort product roadmap
- wiki/LOTUS Premium Spec
tags:
- lotus
- dr-sort
- product-spec
- application-layer
- desktop-app
- content-aware-classification
- premium-feature-set
- wiki
- lotus-premium-spec-md
- sort
- spec
- ownership
- march
- color-red
status: active
created: '2026-05-03'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/LOTUS Premium Spec.md
backlink_count: 11
backlinks:
- '[[archive/wiki-2026-07-08/CODEX HANDOFF — 2026-05-03 Trismégiste Keystone Cycle]]'
- '[[Areas/Writing/Dr. Sort Codebase Version Genealogy — Three Iterations of Failed Automation]]'
- '[[wiki/Dr. Sort Corpus Map — March 2026]]'
- '[[wiki/Dr. Sort and LOTUS Ownership Decision — March 2026]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/LOTUS Agency Scoring App GPT — ChatGPT Product Specification]]'
- '[[wiki/LOTUS Model and Agency]]'
- '[[wiki/LOTUS Model — Agency and Social Positioning]]'
- '[[wiki/Mythocritique to PHAROS — The 2010 Master''s Thesis as Methodological Keystone]]'
- '[[projects/Dr. Sort — Fisher King Project State]]'
- '[[projects/LOTUS — Fisher King Project State]]'
---

# LOTUS Premium Spec

> **CORRECTION NOTICE (2026-05-03):** This note describes the **vision layer**, not realized engineering. The spec was authored alongside the `pdf_sorter_v1` Python prototype — one of three coexisting Dr. Sort codebases. The actually-realized engineering is documented in the **Milestone 1 and Milestone 2 design documents** at `/home/cerebrhoe/dr-sort/docs/milestone1-design.md` and `/home/cerebrhoe/dr-sort/docs/milestone2-design.md`, which describe a third Dr. Sort codebase: Electron + React + TypeScript + Python service + SQLite at `/home/cerebrhoe/dr-sort/apps/desktop/` and `/home/cerebrhoe/dr-sort/backend/`. That third codebase is a complete rewrite, not an evolution. The "currently implemented" claims in this spec describe the prototype, which was abandoned and superseded. Per the [[Dr. Sort and LOTUS Ownership Decision — March 2026|ownership decision]], canonical Dr. Sort lives at `Agency/scriptorium_v3` (a fourth, older codebase). The version genealogy across all four (Agency tkinter / pdf_sorter_v1 prototype / Premium Spec vision / M1+M2 milestone-driven rewrite) is itself evidence of failure-as-method per [[Dr. Sort Corpus Map — March 2026]] and the [[Mythocritique to PHAROS — The 2010 Master's Thesis as Methodological Keystone|keystone]].

## Summary

Product **vision specification** for `LOTUS | Dr. Sort-Academic Helper` as a local-first, content-aware archive application — describing the *intended* application layer that would operationalize the [[LOTUS Model — Agency and Social Positioning|LOTUS theoretical framework]] as a desktop tool. **This is the vision, not the realized engineering.** Distinct from the [[LOTUS Model — Agency and Social Positioning|formal vector model]] (mathematics) and [[Bonded Intelligence Under Constraint — The LOTUS Processor Framework|the theoretical paper]] (philosophical grounding). Realized engineering documented separately in M1/M2 milestone design docs (Electron+React+Python service+SQLite). Closely tied to [[Dr. Sort and LOTUS Ownership Decision — March 2026]] for file-level ownership and [[Dr. Sort Corpus Map — March 2026]] for operational evidence of the prototype run. Related to [[LOTUS Model and Agency]] and [[Governance and PHAROS MOC]].

## Context

Raw source: `raw sources/LOTUS_PREMIUM_SPEC.md`. Recovered 2026-05-03 from `/home/cerebrhoe/dr-sort/pdf_sorter_v1/`. The spec sits inside the canonical Dr. Sort source tree per the [[Dr. Sort and LOTUS Ownership Decision — March 2026|ownership decision]] (canonical at `Agency/scriptorium_v3`; the `pdf_sorter_v1` location is a working development directory).

The spec describes LOTUS/Dr. Sort as **evolving from a safe document sorter into a high-end, local-first, content-aware archive application** — meaning the product trajectory is from minimal-viable to premium tooling, not from research demo to production.

## Core Product Direction

The spec defines five product commitments:

1. **Intelligent AI-assisted classification** based on file content, metadata, structure, and naming patterns
2. **Contextual renaming** into standardized descriptive filenames
3. **Automatic folder hierarchy generation** by category, type, date, and custom schemas (project, client)
4. **Local-first operation** for privacy-sensitive archives — no cloud dependency required
5. **Review-before-apply workflow with undo** — non-destructive by default

These commitments map directly to the [[LOTUS Model — Agency and Social Positioning|LOTUS dimensions]]:
- Local-first → coherence (C) and access (A) preserved against external constraint
- Review-before-apply → perceptual latitude (P) and regulatory bandwidth (R) preserved against automation override
- Content-aware classification → social legibility (S) — making documents readable to systems and to the operator

## Premium Feature Set

### Intelligent AI-Powered Automation

Implemented in foundation form:
- Content-aware analysis for `PDF`, `DOCX`, `DOC`, `TXT`
- Metadata extraction for title, author, date, DOI, ISBN, language, file type
- Intelligent tagging for retrieval and downstream automation
- Rules-assisted classification overrides and filename templating
- Contextual renaming into richer descriptive filenames
- Duplicate-aware planning before files are moved or copied

### Deep Integration and Customization

Implemented:
- Plain-English rules file
- Cross-reference reporting against `MASTER BIBLIOGRAPHY.txt` (see [[MASTER BIBLIOGRAPHY — Theoretical Genealogy of LOTUS]])
- Real-time monitoring scaffold for watched folders
- Sort-view controls for proposed actions and review order
- Folder hierarchy generation by category, document type, author, date cues
- Windows launcher + PowerShell wrapper for the same engine

### Advanced Search and Security

Implemented:
- Local semantic-style search over title, authors, tags, metadata, extracted content
- Exact and probable duplicate detection
- Local-only processing by default
- Privacy-first behavior

### User Experience

Implemented:
- Pre-move review table
- Cross Reference report viewer
- Render Masterlist export (see [[Dr. Sort Corpus Map — March 2026]] for an output example)
- Undo last sort action
- Search, monitor, rules, and sort controls in one desktop hub

## Implementation Status (per spec)

### Currently Implemented

The spec lists 13 confirmed-implemented capabilities (verbatim):
- content-aware scan and classification
- duplicate detection
- cross-reference reports
- masterlist rendering
- sort-by review control
- intelligent tag generation
- semantic local search foundation
- plain-English rules foundation
- real-time folder monitoring scaffold
- undo-last-sort support
- contextual renaming templates through rules
- local-first privacy-preserving workflow
- PowerShell access to rules via `-RulesFile`

### Premium Roadmap (Not Yet Shipped)

The spec lists 7 explicit roadmap items:
- cloud sync connectors (OneDrive, Dropbox, Google Drive)
- richer rule grammar
- project/client-specific folder schemas
- image/video understanding
- stronger semantic ranking models
- plain-English rule builder inside the GUI
- explicit client/project lenses and saved views

## How This Spec Maps to LOTUS

The spec uses LOTUS-vocabulary in its product framing:

| Spec language | LOTUS framework correspondence |
|---|---|
| "review-before-apply workflow with undo" | preserves regulatory bandwidth (R) — the operator's capacity to self-regulate against system action |
| "local-first ... no cloud dependency required" | preserves access (A) and reduces institutional constraint (K_institutional) |
| "content-aware classification" | operationalizes social legibility (S) — making documents legible to the operator's classification scheme |
| "duplicate-aware planning" | reduces noise in coherence (C) — preventing duplicate self-representation in the archive |
| "plain-English rules file" | preserves perceptual latitude (P) — operator can read and revise the classification logic |
| "cross-reference reporting" | operationalizes the recognition function (Honneth/Butler) — checking new material against established canon |

This is not coincidental. The spec is written in the same conceptual vocabulary that grounds LOTUS as a measurement framework. See [[MASTER BIBLIOGRAPHY — Theoretical Genealogy of LOTUS]] for the theoretical lineage.

## Operational Evidence

The 2026-03-07 / 2026-03-08 production runs documented in [[Dr. Sort Corpus Map — March 2026]] confirm that the spec's "currently implemented" claims are operational. Dr. Sort produced:
- 9 cross-reference run reports
- 8 masterlist exports (CSV + Markdown)
- 16 manifest exports
- A duplicate-quarantine layer that correctly caught two duplicates (Alchemy of the Wound; Dawes 2025-07-29 cover letter)

The premium roadmap items (cloud sync, image/video understanding, semantic ranking, GUI rule builder) are not yet evidenced in operational outputs.

## Ownership and Constraints

Per [[Dr. Sort and LOTUS Ownership Decision — March 2026]]:
- Canonical LOTUS / Dr. Sort lives in `Agency/scriptorium_v3`
- The PHAROS `lotus_dr_sort` residue carries unreplicated delta around structured-note authoring, scoring studio, and sorted-viewer features
- This spec describes the product vision; the file-level ownership and migration constraints are independent and binding

## What This Spec Does Not Describe

- Mathematical specification of the LOTUS vector — see [[LOTUS Model — Agency and Social Positioning]]
- Philosophical/theoretical grounding — see [[Bonded Intelligence Under Constraint — The LOTUS Processor Framework]]
- The bibliography Dr. Sort cross-references against — see [[MASTER BIBLIOGRAPHY — Theoretical Genealogy of LOTUS]]
- Operational corpus evidence — see [[Dr. Sort Corpus Map — March 2026]]
- File-level ownership and migration constraints — see [[Dr. Sort and LOTUS Ownership Decision — March 2026]]

This spec is the **product layer**. The other notes in this cluster handle theory, framework, evidence, and ownership.

## Related

- [[LOTUS Model — Agency and Social Positioning]] — formal vector model
- [[Bonded Intelligence Under Constraint — The LOTUS Processor Framework]] — theoretical paper
- [[MASTER BIBLIOGRAPHY — Theoretical Genealogy of LOTUS]] — theoretical lineage
- [[Dr. Sort Corpus Map — March 2026]] — operational evidence
- [[Dr. Sort and LOTUS Ownership Decision — March 2026]] — ownership decision record
- [[LOTUS Model and Agency]] — primary index
- [[Governance and PHAROS MOC]] — secondary index
- [[Dr_Sort_milestone1-design]]
- [[LOTUS_PREMIUM_SPEC]]
