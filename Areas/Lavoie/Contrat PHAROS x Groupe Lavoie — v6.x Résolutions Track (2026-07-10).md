---
type: client-doc
title: Contrat PHAROS x Groupe Lavoie — v6.x Résolutions Track (2026-07-10)
aliases:
- Contrat v6.3
- Contract v6 Lavoie
tags:
- client-doc
- lavoie
- contract
- signature-gate
- contract-review
- areas
status: active
domain: lavoie
priority: high
created: '2026-07-12'
updated: '2026-07-12'
vault_area: Areas
canonical_path: Areas/Lavoie/Contrat PHAROS x Groupe Lavoie — v6.x Résolutions Track (2026-07-10).md
---

# Contrat PHAROS x Groupe Lavoie — v6.x Résolutions Track (2026-07-10)

> For future Claude: the Groupe Lavoie contract advanced from v5 to **v6.3** over 2026-07-09/07-10 through three review-and-fix cycles run with the `contract-review` skill. The contract is still **UNSIGNED** and one upstream decision (founder / Annexe E ownership) gates the send to Israël. Canonical sources on disk win over this snapshot: `~/Lavoie/contrat-v6.3-source.md`, `ContratPharosAIxGroupeLavoiev6.3.pdf`, `sommaire-executif-v6.3-source.md`. Supersedes the pricing/structure snapshot in [[Areas/Lavoie/Contrat PHAROS x Groupe Lavoie — v5 Signature Track (2026-07-08)|the v5 signature track]] for anything touching articles 5, 7, 10 and Annexe E.

## Summary

Three self-review cycles on the [[Areas/Lavoie/AREA|Groupe Lavoie]] contract produced v6.1 → v6.2 → v6.3, each fix pass reviewed fresh so that defects introduced by the previous edit were caught (an undefined trigger, a too-short window, an over-broad condition). The résolutions are tracked in-document with a `⟦R#⟧` journal convention, R4 through R11. Pricing is unchanged from the [[Areas/Lavoie/Offre de service — v5 Pyramid (2026-07-05)|pyramid]]: cumulative 4 500 / 14 500 / 29 500 $ plus 1 500 $/mois récurrent. Everything below is drafting state, not legal advice: 14 `[à compléter]` fields and 5 `[à valider juridique]` clauses remain, and a lawyer pass is still required before signature.

## Context

The v5 track set the milestone as a **signature, not a production deploy**, in the ~July 13 window. The v6 line is the work of getting that text to a state a lawyer and a counterparty can both read. It runs alongside the client-facing binder ([[Areas/Lavoie/Dossiers Client Plan-Set — Chaîne de gouvernance éditoriale 5156–5165 (2026-07-08)|dossier chain]]) and the delivery workstream ([[Areas/Lavoie/Contremaître — Groupe Lavoie Field-Operations Platform|Contremaître]]). Client communication is unchanged: Martin → Patricia → {Israël, Guillaume}, nothing sent from a repo, no follow-up inside 7 days.

## Details

### Résolutions journal (⟦R#⟧ convention)

| R# | Version | What it fixes |
|---|---|---|
| R4 | v6.2 | Deemed acceptance of a palier after 10 jours ouvrables of client silence |
| R5 | v6.2 | Licence granted conditional on payment |
| R6 | v6.2 | Annexe E inventory (client-side pre-existing assets) |
| R7 | v6.2 | Retention precision in the sommaire exécutif |
| R8 | v6.3 | **Avis de livraison defined**: a written email from the Prestataire to the client's designated persons, naming the palier delivered and attaching the acceptance-criteria list from annexes A–C |
| R9 | v6.3 | Prolongation: client may request a motivated extension, capped at +10 jours ouvrables |
| R10 | v6.3 | « montants échus et non contestés »; a payment default **suspends** the licence after the Article 10 cure period, it does not revoke it |
| R11 | v6.3 | Generic document templates stay with PHAROS, **excluding** the client's letterhead templates (logo, RBQ, NEQ), which are client Livrables |

Also in v6.3: Annexe E carries « (l'Article 5 prévaut) », and the BarrioPro row reads « préexistant » with the earlier hedge dropped.

### Residual findings on v6.3 (batch these into the lawyer pass, do not churn a v6.4)

- « personnes désignées du Client » is used in the R8 definition but is itself undefined. Anchor it to the Article 1 representative or to « désignées par avis écrit ».
- R9's extension expiry does not explicitly re-arm the deemed acceptance clock. Proposed: « à l'échéance de la prolongation, le palier est réputé accepté dans les mêmes conditions ».
- Article 10's cure period is a vague « délai raisonnable ». Market standard is 30 days.
- Two « montants dus » residuals to context-check (likely the benign Art. 10 « sommes déjà dues » plus journal text).

### Method worth reusing

The gain did not come from a single expert pass. It came from **reviewing each fix pass as if it were a fresh document**: every round of edits introduced at least one new defect, and only a clean re-read caught them. Same pattern as build-time enforcement in the [[Areas/Lavoie/Dossiers Client Plan-Set — Chaîne de gouvernance éditoriale 5156–5165 (2026-07-08)|dossier chain]] — the rule is only real when something re-checks it after the edit. Skill installed at `~/.claude/skills/contract-review/` (from `evolsb/claude-legal-skill`).

### Blockers before send

1. **Upstream, unresolved by design:** the founder / Annexe E ownership decision — see [[Areas/PHAROS/Founder Agreement — PHAROS x Danny Stocker Perimeter Reset (2026-07-10)|the founder-agreement perimeter]]. Annexe E cannot be finalized while ownership of the underlying assets is an open fork.
2. 14 `[à compléter]` fields (legal forms, NEQ, addresses, designated contacts).
3. Lawyer batch: the 5 `[à valider juridique]` items, insurance/E&O, intérêts de retard, dormancy limit, porte-fort affiliés, confidentiality super-cap, plus the v6.3 residuals above.

## Related

- [[Areas/Lavoie/Contrat PHAROS x Groupe Lavoie — v5 Signature Track (2026-07-08)]]
- [[Areas/Lavoie/AREA|Area — Lavoie]]
- [[Areas/Lavoie/Offre de service — v5 Pyramid (2026-07-05)]]
- [[Areas/PHAROS/Founder Agreement — PHAROS x Danny Stocker Perimeter Reset (2026-07-10)]]
- [[Areas/Lavoie/Lavoie Artifact Map — Working Directory (2026-07-08)]]
