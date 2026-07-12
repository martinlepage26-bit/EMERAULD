---
type: area
title: Area — Lavoie
tags:
- areas
- lavoie
- pending
- jade
- guillaume
- zones
status: active
domain: lavoie
created: '2026-06-29'
updated: '2026-07-12'
vault_area: Areas
canonical_path: Areas/Lavoie/AREA.md
backlink_count: 10
backlinks:
- '[[Areas/Lavoie/Contremaître — Groupe Lavoie Field-Operations Platform]]'
- '[[Areas/Lavoie/Lavoie Artifact Map — Working Directory (2026-07-08)]]'
- '[[Areas/Lavoie/LegiPro Canada-QC — Compliance Evidence Service Plan]]'
- '[[Areas/Lavoie/Quiet Compliance Workbench — Standing Tone Rule]]'
- '[[Areas/PHAROS/CLIENT ACCOUNTS]]'
- '[[Logs/2026-07-06]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[index]]'
- '[[memory/clients/Lavoie Construct]]'
- '[[memory/daily/2026-07-06]]'
---

# Area — Lavoie

Active PHAROS client, two workstreams (operator decision 2026-07-08): the signature + SEO/marketing track is gated on A1–A5 (relayed via Patricia, ~July 13 signature window per [[Areas/Lavoie/Contrat PHAROS x Groupe Lavoie — v5 Signature Track (2026-07-08)|contract v5]]); the software delivery track ([[Areas/Lavoie/Contremaître — Groupe Lavoie Field-Operations Platform|Contremaître]], [[Areas/Lavoie/LegiPro Canada-QC — Compliance Evidence Service Plan|LegiPro]]) proceeds independently and is in production.

## Scope
Groupe Lavoie: SOS Plomberie, Excavations Lavoie, GVI (property mgmt), Clôtures Israel Concept.

## People
- **Israël Lavoie** — grand patron, visionnaire
- **Guillaume Lavoie** — co-owner, signs gate A5 (zones/services list)
- **Patricia** — Martin's sister, internal relay, collects A1–A5 responses

## Gate status
| Gate | Description | Status |
|------|-------------|--------|
| A1 | Client URL confirmed | pending |
| A2 | GSC access | pending |
| A3 | GBP access | pending |
| A4 | LocalGo matrix | pending |
| A5 | Zones/services list (Guillaume signs) | pending |

## Active files
- `~/Lavoie/` — client project root on disk
- `~/Lavoie/lavoie-fieldops/` — **Contremaître** field-operations platform (formerly `~/pharos-fieldops`)
- `~/Lavoie/plan-directeur-lavoie-2026.md` — master plan (parent repo, local commits only)
- `Lavoie/jade-base44-handoff.md` — 3-app spec for Jade (Base44 dev)

## Client dossiers (as of 2026-07-08)
The plan-set client dossiers (parité 5157, feuille de route 5158, réalisation v0.15 = 5160, unified 62-page remise packet through 5165) plus the editorial register rules and build-time enforcement are documented at [[Areas/Lavoie/Dossiers Client Plan-Set — Chaîne de gouvernance éditoriale 5156–5165 (2026-07-08)|dossier chain 5156–5165]]. Argus verdict: remise dégagée. Blocker to closure: Codex re-auth for the final review; 5165 is marked NON APPROUVÉ until then. Standing: numbered dirs are the version history (no per-version git commits); nothing to the client except via Martin → Patricia.

## Contract (as of 2026-07-10)
The text advanced v5 → **v6.3** through three review-and-fix cycles: [[Areas/Lavoie/Contrat PHAROS x Groupe Lavoie — v6.x Résolutions Track (2026-07-10)|v6.x résolutions track]] (R4–R11). Still **unsigned**. Two things block the send: the founder / Annexe E ownership decision ([[Areas/PHAROS/Founder Agreement — PHAROS x Danny Stocker Perimeter Reset (2026-07-10)|open forks]]) and the lawyer batch (14 `[à compléter]`, 5 `[à valider juridique]`, plus v6.3 residuals).

## Phase 1 build foundation (as of 2026-07-10)
Executor-ready and awaiting Martin's green light (WP-01 first): [[Areas/Lavoie/Domain API Foundation — Phase 1 Work Orders and Ports (2026-07-10)|domain API foundation + WP-01→WP-19]], grounded in the [[Areas/Lavoie/Contremaître Integrations — Verified API Capability Map (2026-07-10)|verified integration capability map]] (VoIP.ms has no inbound-call webhook — voice is Phase 2 SIP). The licensing/network play is [[Areas/Lavoie/Marketplace de débordement — Job Overflow and Payments Architecture (2026-07-10)|marketplace de débordement]], blocked on a FINTRAC/Revenu Québec legal gate, not on engineering.

## Software workstream (as of 2026-07-06)
[[Contremaître — Groupe Lavoie Field-Operations Platform]] is deployed (Cloudflare Worker + mtl-03 interim backend, GitHub `martinlepage26-bit/Lavoie`): 16-module map, CLI + MCP + hardened API package, 49 tests. [[LegiPro Canada-QC — Compliance Evidence Service Plan]] is the planned compliance-evidence extension (docs-only, gated behind QC cutover). Standing direction from Martin (2026-07-06): all LegiPro/Contremaître language stays calm and operational — "quiet compliance workbench, not a courtroom simulator". Real client login/org email: `info@israelconcept.ca` (not israel@groupelavoie.ca).

## Notes for this area
Drop Lavoie meeting notes, gate updates, and comms here.
