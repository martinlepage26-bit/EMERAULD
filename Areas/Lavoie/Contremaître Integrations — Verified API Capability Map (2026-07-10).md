---
type: wiki
title: Contremaître Integrations — Verified API Capability Map (2026-07-10)
aliases:
- Integration Capability Map
- VoIP.ms webhook finding
- Lavoie integrations
tags:
- lavoie
- contremaitre
- integrations
- api
- voipms
- nextcloud
- openproject
- espocrm
- acomba
- progressionlive
- areas
- wiki
status: active
domain: lavoie
created: '2026-07-12'
updated: '2026-07-12'
vault_area: Areas
canonical_path: Areas/Lavoie/Contremaître Integrations — Verified API Capability Map (2026-07-10).md
---

# Contremaître Integrations — Verified API Capability Map (2026-07-10)

> For future Claude: the six external systems [[Areas/Lavoie/Contremaître — Groupe Lavoie Field-Operations Platform|Contremaître]] must integrate with, with their **verified** capabilities and, more importantly, their verified *absences*. Each finding below was checked against vendor documentation, not assumed. Load this before designing any integration, work package, or client-facing claim that depends on one of these systems. Canonical doc on disk: `~/Lavoie/lavoie-fieldops/docs/integrations/integration-capability-map-v0-01.md`. Confidence: high (documented), and the architecture was corrected because of it.

## Summary

Six parallel research passes replaced assumption with documentation across VoIP.ms, Nextcloud, OpenProject, EspoCRM, Acomba and ProgressionLIVE. The single most consequential finding: **VoIP.ms has no inbound-call webhook**. Realtime call events are SIP-only. That killed the "voice agent answers the phone in Phase 1" design and moved voice to a Phase 2 SIP path, with CDR polling covering Phase 1. Several other findings are cost or legal facts (Acomba import is a paid add-on; EspoCRM is AGPLv3) that belong in the client conversation, not only the code.

## Context

The map exists because the [[Areas/Lavoie/Contremaître — Groupe Lavoie Field-Operations Platform|Contremaître]] Phase 1 work orders were about to be handed to a less capable executor agent. Handing an executor a plan built on unverified vendor capability is how a build fails silently. It is also the evidence base behind the "IA au travail" and "SANS IA, par choix" strips in the client binder ([[Areas/Lavoie/Trait de chantier — Dossier Drawing Language and AI Honesty Strips (2026-07-10)|drawing language and AI strips]]) — every AI claim on a page has to trace back to an endpoint that actually exists.

## Details

### VoIP.ms

- **No inbound-call webhook.** SIP is the only realtime channel for calls. SMS and fax webhooks do exist.
- Native call recording $0.0025/min; transcription $0.05/min with an fr-CA locale.
- API cap of 100 SMS/day; IP allowlist required.
- Consequence: Phase 1 = CDR polling; voice agent = Phase 2 SIP. Written asks outstanding: caps and data residency.

### Nextcloud

- `oc:fileid` **changes on trash-restore**. Never delete through the trash if the id is load-bearing.
- Resolver: SEARCH (RFC 5323). `webhook_listeners` needs NC30+. `files_retention` **deletes**, it does not protect. Redis locking required.

### OpenProject

- Webhook signature is undocumented — a spike is required before relying on it.
- Optimistic locking via `lockVersion` (409 on conflict). No native external-id field. Community tier is sufficient.

### EspoCRM

- Duplicate detection is unreliable. Do our own lookup, carry `cExternalId`, send `X-Skip-Duplicate-Check`.
- HMAC auth. Custom fields cannot be created through REST. **Licence: AGPLv3** (a distribution question, not just a technical one).

### Acomba

- Import is a **paid client-side add-on**: Import-data ~$789/yr, or Trans-xls.
- Taxes are posted by tax-group code (`NoGroupeTaxe`), never a raw percentage.
- ODBC ~$60/mo and 32-bit. The $0 ACCEO developer tier does include the import-format documentation.

### ProgressionLIVE

- Paid per-tenant REST API, 192 endpoints, OpenAPI verified.
- **No invoice object** — check what the client's Acomba already holds before designing around it.
- Attachments are per-record only.

## Related

- [[Areas/Lavoie/Contremaître — Groupe Lavoie Field-Operations Platform]]
- [[Areas/Lavoie/Domain API Foundation — Phase 1 Work Orders and Ports (2026-07-10)]]
- [[Areas/Lavoie/AREA|Area — Lavoie]]
- [[Areas/Lavoie/LegiPro Canada-QC — Compliance Evidence Service Plan]]
