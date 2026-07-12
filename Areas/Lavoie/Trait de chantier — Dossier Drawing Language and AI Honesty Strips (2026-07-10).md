---
type: wiki
title: Trait de chantier — Dossier Drawing Language and AI Honesty Strips (2026-07-10)
aliases:
- Trait de chantier
- Dossier drawing law
- AI strips
tags:
- lavoie
- client-doc
- design
- diamond-eyes
- brand
- pharos
- writing-rules
- areas
- wiki
status: active
domain: lavoie
created: '2026-07-12'
updated: '2026-07-12'
vault_area: Areas
canonical_path: Areas/Lavoie/Trait de chantier — Dossier Drawing Language and AI Honesty Strips (2026-07-10).md
---

# Trait de chantier — Dossier Drawing Language and AI Honesty Strips (2026-07-10)

> For future Claude: the visual and rhetorical canon adopted for the [[Areas/Lavoie/AREA|Groupe Lavoie]] client binder across versions v0.09 → v0.13 (directories 5152 → 5156 under `~/Lavoie/dossiers-client/`). Three durable rules came out of it: one drawing language, an AI-transparency strip on every module page, and an explicit **"SANS IA, par choix"** state for pages where AI does not help. Load this before drawing anything client-facing or writing any AI claim into a deliverable. Canons on disk: `dossiers-client/DESIGN.md` and `PRODUCT.md` (treat external edits there as authoritative).

## Summary

Martin's correction was that the binder was becoming "a patchwork of different styles" with arrowheads in the middle of lines. The fix was a single drawing law, named **trait de chantier**, applied to every sheet: one gold 5px main flow per page, slate support lines, numbered detail bubbles carrying direction instead of arrowheads, junction dots, white tech-boxes with module-coloured outlines. On top of it sits an AI-transparency strip and, where honesty demands it, the absence of one. The binder then took the PHAROS livery (teal `#0a3d4f`, champagne `#b8962e`) under an endorsement architecture: PHAROS is the issuing engineer in the cartouche, the product stays [[Areas/Lavoie/Contremaître — Groupe Lavoie Field-Operations Platform|Contremaître]].

## Context

The audience is a builder, not a software buyer, so the document had to read like a plan set rather than a deck. Version lineage: v0.09 (mobile terrain elevated to a first-class module with a voice-assistant subsection and guardrails), v0.10 (P-112 customer journey, « comptant », channel pills), v0.11 (AI strips, unified drawing language, footer progress bar), v0.12 (PHAROS livery), v0.13 (multi-tenancy sheet F-216 and the [[Areas/Lavoie/Marketplace de débordement — Job Overflow and Payments Architecture (2026-07-10)|marketplace money-flow sheet F-217]]). The editorial rules and build-time scan enforcement live in the [[Areas/Lavoie/Dossiers Client Plan-Set — Chaîne de gouvernance éditoriale 5156–5165 (2026-07-08)|dossier chain note]]; this note holds the drawing and AI-claim side.

## Details

### The drawing law

- **One gold 5px main flow per page.** Support lines are slate `#8a9a90` at 2.5px.
- **Numbered detail bubbles carry direction.** No arrowheads on spines. No mid-line chevrons, ever. Small drafting-tick terminals appear only where the numbering does not already tell you which way to read.
- Junction dots at branches. White tech-boxes, `rx=4`, with 2.5px outlines in the module's colour. Dark green is **reserved** for the Contremaître core. Panel corner ticks.
- Helpers in the generator: `svg_spine`, `_tech_box`, `_arrow` (rewritten with `math.atan2` for a fine line plus tick), `_panel_ticks`, and `_fit` for auto-sizing text that would otherwise overflow a box.

### AI transparency strips

Every module page carries a dark `.ai-strip` band — chip **IA AU TRAVAIL**, three columns: *Ce que l'IA fait* / *Ce que vous gardez* / *Temps gagné*. No invented metrics: every claim has to trace to a real endpoint or a real work package, which is why the [[Areas/Lavoie/Contremaître Integrations — Verified API Capability Map (2026-07-10)|verified capability map]] is upstream of this design and not decoration.

### The honesty state

Martin: « we should also be honest when AI doesn't add ». So there is a green `.ai-strip.none` variant reading **SANS IA, PAR CHOIX**. A page that does not benefit from AI says so. This is the single most defensible thing in the binder for a governance consultancy selling constraint-first AI, and it should survive into every future PHAROS deliverable.

### Livery

Teal ramp anchored on `#0a3d4f`, champagne ramp on `#b8962e`. Endorsement architecture: PHAROS appears as the issuing engineer in the kicker and cartouche; the product name on the sheets stays Contremaître.

## Related

- [[Areas/Lavoie/Dossiers Client Plan-Set — Chaîne de gouvernance éditoriale 5156–5165 (2026-07-08)]]
- [[Areas/Lavoie/Contremaître — Groupe Lavoie Field-Operations Platform]]
- [[Areas/Lavoie/Quiet Compliance Workbench — Standing Tone Rule]]
- [[Areas/PHAROS/Diamond-Eyes — Aesthetic Refinement Skill]]
- [[Areas/Lavoie/AREA|Area — Lavoie]]
