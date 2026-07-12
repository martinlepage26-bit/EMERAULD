---
type: wiki
title: Marketplace de débordement — Job Overflow and Payments Architecture (2026-07-10)
aliases:
- Job Overflow Marketplace
- Marketplace de débordement
- Stripe Connect architecture
tags:
- lavoie
- contremaitre
- pharos
- marketplace
- payments
- stripe
- regulatory
- multi-tenancy
- areas
- wiki
status: active
domain: lavoie
created: '2026-07-12'
updated: '2026-07-12'
vault_area: Areas
canonical_path: Areas/Lavoie/Marketplace de débordement — Job Overflow and Payments Architecture (2026-07-10).md
---

# Marketplace de débordement — Job Overflow and Payments Architecture (2026-07-10)

> For future Claude: the "one more thing" of the [[Areas/Lavoie/Contremaître — Groupe Lavoie Field-Operations Platform|Contremaître]] pitch — once the platform is multi-tenant and licensable, contractors who cannot take a job can pass it to another tenant, payment flows through the app, and a commission returns to Israël Concept as network owner. This note holds the architecture, the neutrality design, and the **load-bearing legal UNCLEARs that block it**. Do not present this as a shippable Phase 1 feature. Source on disk: `~/Lavoie/lavoie-fieldops/docs/product/marketplace-payments-regulatory-note-v0-01.md`; client-facing sheets F-216 (multi-tenancy) and F-217 (money flow) in binder v0.13.

## Summary

The payments design is Stripe Connect Express with destination charges and an `application_fee`. The platform is merchant of record **for the card charge only**; the contractor remains the RBQ entrepreneur of record and the platform is never a party to the construction contract. Tax flows through two invoices. A holdback is a delayed second Transfer, never called "escrow". Commission returns to Israël Concept because he owns the network, not because he sits above the contractors — which is the whole psychological problem the client page had to solve.

## Context

Martin's framing question was blunt: « is Israël the top of the pyramid, or is there a better way to present the money flow? » A pyramid reads as extraction. The answer adopted for the client binder is a **toll bridge**: the big gold pipe carries the work and the money to the executing company, and a thin tap takes the platform's share at each job. Page 28 of the binder was rebuilt around "follow the money" and then rewritten in plain human French. Multi-tenancy (F-216) is the precondition; without it there is no network to overflow into.

## Details

### Payments architecture (6 lines)

1. Stripe Connect **Express** accounts per contractor tenant.
2. **Destination charges** with `application_fee` — the platform takes its share at the charge, not by invoicing later.
3. Platform = merchant of record for the card charge only. Contractor = RBQ entrepreneur of record.
4. The platform is **never** a party to the construction contract. Four-contract stack: platform↔tenant, tenant↔client, platform↔payment processor, network agreement.
5. Two invoices for tax (platform→tenant for the fee; tenant→client for the work).
6. Holdback = a delayed second Transfer. Never the word "escrow".

### Neutrality (how the owner's own company does not get preferential treatment)

Algorithmic allocation, identical fees for every tenant **including the owner's own company**, and disclosed affiliation. Precedents: Amazon's own-brand placement scrutiny, the FTC action against HomeAdvisor. Client-facing wording adopted: « mêmes frais pour tous, y compris le propriétaire » and « Pas d'exception, pas de passe-droit ».

### Blocking UNCLEARs (do not build past these)

> [!warning] Legal gate, unresolved
> FINTRAC money-services-business registration and Revenu Québec ESM (entreprise de services monétaires) may both apply once the platform moves money between third parties. This is **load-bearing** — it decides whether the marketplace is legal to operate as designed, not merely how to build it. Named human review required (Martin decides; agents flag). Gate wording already in the binder: the marketplace « s'active seulement » under conditions written into the commercial offer, **before the first network job**.

### Governance note

The commission mechanism affects a client's revenue and a third party's payment. It is a decision-supporting output under the ethical-review gates: it does not go to Israël without Martin's review, and it never reaches the client except through Patricia.

## Related

- [[Areas/Lavoie/Contremaître — Groupe Lavoie Field-Operations Platform]]
- [[Areas/Lavoie/Domain API Foundation — Phase 1 Work Orders and Ports (2026-07-10)]]
- [[Areas/Lavoie/Trait de chantier — Dossier Drawing Language and AI Honesty Strips (2026-07-10)]]
- [[Areas/Lavoie/Contrat PHAROS x Groupe Lavoie — v6.x Résolutions Track (2026-07-10)]]
- [[Areas/Lavoie/AREA|Area — Lavoie]]
