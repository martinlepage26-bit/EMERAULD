---
type: wiki
title: LegiPro Canada-QC — Compliance Evidence Service Plan
aliases:
- LegiPro
- LegiPro Canada/QC
tags:
- lavoie
- pharos
- legipro
- compliance
- quebec
- governance
- product
status: active
created: '2026-07-06'
updated: '2026-07-06'
vault_area: wiki
canonical_path: wiki/LegiPro Canada-QC — Compliance Evidence Service Plan.md
---

# LegiPro Canada-QC — Compliance Evidence Service Plan

> For future Claude: LegiPro is a planned (docs-only, not yet implemented) Québec/Canada construction-compliance evidence service that integrates with [[Contremaître — Groupe Lavoie Field-Operations Platform|Contremaître]] over REST/MCP. Load this note before any LegiPro design, docs, or implementation work — it carries the standing "quiet compliance workbench" tone rule and the rights boundaries. Main deliverable on disk: `/home/martin/Lavoie/lavoie-fieldops/docs/integrations/legipro-canada-qc-api-plan.md`.

## Summary

LegiPro finds and cites relevant Québec/Canada regulatory sources, assembles project context, and prepares cited evidence packets **for human professional review** — it organizes and points, it doesn't decide. Executive decision: **integrate, not merge** — a separate service talking to [[Contremaître — Groupe Lavoie Field-Operations Platform|Contremaître]] via REST/MCP, no database access. Implementation is gated behind the QC (PostgreSQL) cutover and is a future phase for the [[Areas/Lavoie/AREA|Groupe Lavoie]] engagement.

## Context

Grew out of the Contremaître full-package work (2026-07-05/06). The plan document, risks note, roadmap Phase 5, and handoff all live in the lavoie-fieldops repo; the parent master plan `~/Lavoie/plan-directeur-lavoie-2026.md` §16 carries the workstream and division/source map. Martin (relayed by rook-509) set the standing tone direction on 2026-07-06.

## Details

### Standing tone rule — quiet compliance workbench (2026-07-06, Martin via rook-509)

Dedicated note: [[Quiet Compliance Workbench — Standing Tone Rule]]. All future LegiPro UI/API/docs work uses calm operational language: **Sources trouvées, Points à confirmer, Dossier prêt pour revue, Source officielle, Ajouter une note de revue, Exporter le dossier**. Review states: *En préparation* / *Prêt pour revue*. Avoid warning banners, popups, and scary terms (illegal, non-compliant, no legal advice, liability) on everyday surfaces. Formal caveats belong mostly in exports, guides, and admin surfaces — short and neutral. Softening is UX language only: source rigor, source cards, evidence traceability, rights boundaries, and the human-review workflow stay intact. Design for confidence and flow — "a quiet compliance workbench, not anxiety confetti". Applied across all LegiPro docs and committed (lavoie-fieldops `bd643fe` pushed; parent plan `7c30917` local).

### Architecture and scope

- Identifier taxonomy: jurisdictions `ca` / `ca-qc` / `ca-qc-saguenay`; sectors `construction.general`, `excavation`, `plumbing.septic`, `fencing.pool`, `property.management`, `landlord.tenant.tal`, `ccq.labour`, `cnesst.chantier`, `rbq.licensing`, `req.entity`
- Source registry: Données Québec/CKAN (`package_show` = metadata, resource URLs = data), RBQ, REQ, RENA, property rolls, LégisQuébec, NRC, CNESST, CCQ, TAL, SOQUIJ, CanLII, Revenu Québec — each with method, cadence, rights caveat, first use
- AI-assisted pre-check + cited evidence packets + **human professional signoff** — the human decides
- Rights posture: no bulk-ingest of paid/protected NRC/CNRC code text; property rolls are redacted (no re-identification)

### Effective-date facts captured in the plan

- Plumbing amendments 2024-07-11; new systems after 2025-01-11
- Building CNB 2020: 2025-04-17; mandatory for projects ≥ 2026-10-17
- Pools built pre-2010-11-01 must comply by 2027-09-30
- CNESST chantier notice ≥ 10 days, up to 180

### Key repo files

- `docs/integrations/legipro-canada-qc-api-plan.md` — main plan (§5 REST/MCP, §6 Séquençage & états de revue + langage UI recommandé, §7 rights posture, §8 open questions, §9 garde-fous)
- `docs/product/risks-and-open-questions.md`, `docs/product/roadmap.md` (Phase 5), `docs/api/conventions.md`, `docs/guides/llm-guide.md`, `docs/architecture/structurizr.dsl` (legipro external system, no DB access)
- Parent: `~/Lavoie/plan-directeur-lavoie-2026.md` §16

## Related

- [[Contremaître — Groupe Lavoie Field-Operations Platform]]
- [[Areas/Lavoie/AREA|Area — Lavoie]]
- [[Master Project Tracker — 2026]]
