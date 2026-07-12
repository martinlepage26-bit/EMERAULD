---
type: client-doc
title: Lavoie Artifact Map — Working Directory (2026-07-08)
tags:
- client-doc
- lavoie
- artifact-map
- areas
status: active
domain: lavoie
created: '2026-07-08'
updated: '2026-07-08'
vault_area: Areas
canonical_path: Areas/Lavoie/Lavoie Artifact Map — Working Directory (2026-07-08).md
backlink_count: 3
backlinks:
- '[[Areas/Lavoie/Contrat PHAROS x Groupe Lavoie — v5 Signature Track (2026-07-08)]]'
- '[[Areas/Lavoie/Offre de service — v5 Pyramid (2026-07-05)]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
---

# Lavoie Artifact Map — Working Directory (2026-07-08)

> For future Claude: index of the `~/Lavoie/` working directory as of 2026-07-08, so vault sessions can find client artifacts without re-scanning disk. Canonical sources always win over this snapshot. Communication rule: Martin → Patricia → {Israël, Guillaume}; Patricia never initiates; 7-day follow-up rule after any send. Full operating constraints live in the lavoie-gatekeeper skill.

## Summary

The engagement's paper trail lives in `~/Lavoie/`, git-tracked at martinlepage26-bit/Lavoie. Current instruments: the [[Areas/Lavoie/Contrat PHAROS x Groupe Lavoie — v5 Signature Track (2026-07-08)|v5 contract track]] and the [[Areas/Lavoie/Offre de service — v5 Pyramid (2026-07-05)|v5 offer]]. Delivery platform documentation: [[Areas/Lavoie/Contremaître — Groupe Lavoie Field-Operations Platform|Contremaître]].

## Details

| Artifact | Path | Role |
|---|---|---|
| Contract v5 source | `contrat-v5-source.md` + `Contrat-Pharos-AI-x-Groupe-Lavoie-SIGNATURE-v5.docx` | Signature text (unsigned), corrections C2–C13 |
| Corrections note | `contrat-corrections-2026-07-05.md` | 2026-07-05 correction set feeding v5 |
| Critical revision | `dossier-v6/revision-critique-lavoie.md` | 2026-07-06 revision that produced C2–C13 |
| Offer v5 | `dossier-v6/offre-de-service-v5.html` | Current offer, published at offre-lavoie.pharos-ai.ca |
| Offer domain proxy | `offre-lavoie-domain-proxy/` | Cloudflare Worker serving the offer preview |
| Review gate | `review-gate-signature-2026-07-06.md` | P0/P1/P2 tiering against the ~July 13 signature gate |
| Diagnostic dossier | `dossier_israel_lavoie_diagnostic_fr.md` (+ `artifacts/questions_israel_lavoie_reponses_fr.xlsx`) | 25-question questionnaire for Israël, parallel to A1–A5 |
| Patricia relay template | `MESSAGE_SUIVI_PATRICIA.md` | Client-facing gate wording; source of the 7-day rule |
| CTO roadmap | `quebec-plumbing-cto-roadmap-2026-06-13.md` | Quebec plumbing CTO-level roadmap (2026-06-13; duplicate copy exists in `~/.UPLOADS/`) |
| Hosting infrastructure | `5019-Lavoie-Pharos-AI-hosting-infrastructure.md` | M1 hosting/redundancy/backup/security reference cited by contract Art. 4.1 |
| Plan directeur | `plan-directeur-lavoie-2026.md` | Company structure + diagnosis source of truth |
| Jade handoff | `jade-base44-handoff.md` | Base44 app specs (4 apps; numbering drifts — anchor to priority table, name the app) |
| Client dossiers | `dossiers-client/` (plan-set revisions 5146–5165 + OSS variants, `DESIGN.md`, `PRODUCT.md`, `REGLE-ECRITURE-v2.md`, `stale-terms-v2-staged.txt`) | Plan-set revision family; chain record at [[Areas/Lavoie/Dossiers Client Plan-Set — Chaîne de gouvernance éditoriale 5156–5165 (2026-07-08)|dossier chain 5156–5165]] |
| Parity roadmap | `lavoie-fieldops/docs/product/progressionlive-parity-roadmap.md` (commit ff38a48) | ProgressionLIVE → Contremaître replication roadmap; source of dossier 5157 |
| Audit trail | `docs/audits/argus-chaine-5156-5159-2026-07-08.md`, `docs/audits/codex-revue-finale-v0-04-brief.md` | Argus audit + parked Codex final-review brief |
| Case-study handoff | `docs/handoff/cas-etude-chaine-gouvernance-2026-07-08.md` | Deferred case-study writing (RDG applied to documents) |
| Archived lineage | `_archive/cleanup-2026-07-08/` (incl. offre v4 md) | Superseded documents |

Known disk stray (report-only): a 0-byte accidental copy exists at `~/home/martin/Lavoie/offre-de-service-revisee-v4.md` (rsync artifact, outside the vault; flagged for deletion in the overhaul handoff).

## Related

- [[Areas/Lavoie/AREA|Area — Lavoie]]
- [[Areas/Lavoie/Quiet Compliance Workbench — Standing Tone Rule]]
- [[Areas/Lavoie/Dossiers Client Plan-Set — Chaîne de gouvernance éditoriale 5156–5165 (2026-07-08)]]
