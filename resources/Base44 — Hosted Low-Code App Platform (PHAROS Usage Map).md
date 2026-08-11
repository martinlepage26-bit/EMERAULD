---
type: resource
title: Base44 — Hosted Low-Code App Platform (PHAROS Usage Map)
aliases:
- Base44
tags:
- resource
- base44
- low-code
- platform
- pharos
- lavoie
status: active
created: '2026-07-08'
updated: '2026-07-08'
---

# Base44 — Hosted Low-Code App Platform (PHAROS Usage Map)

> For future Claude: Base44 is a hosted low-code app-builder platform (generated React apps plus a hosted REST backend) that plays two distinct roles in Martin's work: backend/builder for PHAROS internal and product apps, and the delivery platform for the four Groupe Lavoie client apps built by the human developer Jade. Load this note when a task mentions Base44 to know which of the two lanes is in play. Synthesized 2026-07-08 by the nightly pass from five same-day notes; claims are sourced from those notes, not from direct platform inspection (confidence: high for usage, medium for platform description).

## Summary

Base44 is a hosted low-code platform that generates React web apps backed by its own hosted REST functions. In this vault it appears in two lanes: PHAROS-side apps such as [[Areas/PHAROS/nexusos — Base44 App|nexusos]] (a Base44-generated internal React app) and the [[Areas/PHAROS/clearday — Mobile App and App Store Review State|clearday]] backend (function `cleardayCore2`), and Lavoie-side client apps built on Base44 by the human developer Jade.

## Context

- **PHAROS lane:** [[Areas/PHAROS/nexusos — Base44 App]] is itself a Base44-generated app; [[Areas/PHAROS/clearday — Mobile App and App Store Review State]] uses a Base44 REST backend (`cleardayCore2`). A known boundary: the clearday reviewer-account Plus entitlement is granted client-side only; the Base44 backend never grants Plus server-side.
- **Lavoie lane:** the four Groupe Lavoie client apps are Base44 apps built by Jade (the person, not Martin's local `jade` assistant; see [[Areas/PHAROS/Jade — Name Disambiguation]]). Specs live in `~/Lavoie/jade-base44-handoff.md` (3 apps, specs, acceptance criteria per the handoff; the [[Areas/Lavoie/Lavoie Artifact Map — Working Directory (2026-07-08)]] refers to Base44 app specs for 4 apps). "Base44 review" appears as a client-delivery task in [[Areas/PHAROS/Grok Usage Account — Operator Snapshot (2026-07-06)]].

## Details

- Platform shape (as described in the nexusos note): hosted low-code builder producing React apps; iterated via commits such as "Update base44 packages", so generated apps are maintained code, not one-shot exports.
- Vault convention: notes about individual Base44 apps live in `Areas/PHAROS/` (products) or `Areas/Lavoie/` (client); this note is the platform-level anchor so those app notes have a shared reference target.
- Unresolved: no vault note documents Base44's pricing, hosting terms, or data residency. That matters for the Lavoie client lane under the Data Boundary gate; flag before any client data commitment is made on the platform.

## Related

- [[Areas/PHAROS/nexusos — Base44 App]]
- [[Areas/PHAROS/clearday — Mobile App and App Store Review State]]
- [[Areas/PHAROS/Jade — Name Disambiguation]]
- [[Areas/Lavoie/Lavoie Artifact Map — Working Directory (2026-07-08)]]
- [[Areas/PHAROS/Grok Usage Account — Operator Snapshot (2026-07-06)]]
