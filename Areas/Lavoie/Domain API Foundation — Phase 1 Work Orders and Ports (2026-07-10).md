---
type: wiki
title: Domain API Foundation — Phase 1 Work Orders and Ports (2026-07-10)
aliases:
- Domain API Foundation
- Phase 1 Work Orders
- WP-01 to WP-19
tags:
- lavoie
- contremaitre
- architecture
- api
- work-orders
- ports-and-adapters
- areas
- wiki
status: active
domain: lavoie
created: '2026-07-12'
updated: '2026-07-12'
vault_area: Areas
canonical_path: Areas/Lavoie/Domain API Foundation — Phase 1 Work Orders and Ports (2026-07-10).md
---

# Domain API Foundation — Phase 1 Work Orders and Ports (2026-07-10)

> For future Claude: the executor-ready foundation for [[Areas/Lavoie/Contremaître — Groupe Lavoie Field-Operations Platform|Contremaître]] Phase 1 — a domain-named API (not vendor-named), six ports with a mock-plus-contract-test rule, and nineteen work packages in a fixed execution order. Written so a less capable agent can build against it without re-deciding architecture. Docs on disk: `~/Lavoie/lavoie-fieldops/docs/build/phase1-work-orders-v0-01.md`, `docs/api/domain-api-foundation-v0-01.md`, `docs/architecture/customer-lifecycle-orchestration-v0-01.md`, pickup at `docs/handoff/phase1-foundation.md`. **Execution awaits Martin's green light** (WP-01 first).

## Summary

Martin's instruction was to stop naming the API after vendors. The foundation therefore exposes `/api/v1/accounting/…`, `/api/v1/documents/…` and so on, behind six ports (Documents, Accounting, Comms, Crm, Projects, Compliance), each with a mock implementation and a contract test that the real adapter must also pass. Seventy-eight raw vendor endpoints were mapped onto that domain surface. The point is not tidiness: it is that swapping Acomba, EspoCRM or ProgressionLIVE later becomes an adapter change, and that the whole stack can eventually be sold as one product rather than a bag of tools.

## Context

This is the planner half of a planner-executor split. It exists because the [[Areas/Lavoie/Contremaître Integrations — Verified API Capability Map (2026-07-10)|verified capability map]] changed what is buildable (voice moves to Phase 2 SIP; CDR polling covers Phase 1), and because the client-facing promise in the binder is a **single unified experience** over many tools — a promise the API layer has to actually make true. Conventions: v1 aliasing, one error envelope, pagination, `client_request_id` for idempotency, and no vendor names in paths.

## Details

### The six ports

Documents · Accounting · Comms · Crm · Projects · Compliance. Every port ships a mock plus a contract test; an adapter is not done until it passes the same test the mock passes. `VisioPort` and multicanal messaging (SMS, WhatsApp, Google Meet for customer-facing chat) were added after Martin asked to standardize messaging platforms through our own surface rather than per-vendor.

### Work packages

WP-01 (idempotency / ExternalId) through WP-19 (visio). Execution order starts WP-01 → WP-14 → WP-15 → WP-16 → WP-02 → … Revisions v0.02 (corrections forced by the verified API research) and v0.03 (token scopes, multicanal Message, the M365 email decision) are folded in.

### Customer lifecycle — the birth rule

A customer is **created at first commitment**, not at first contact. That single rule resolves the "where does a customer live" question across CRM, dispatch, accounting and documents, and it is what the P-112 customer-journey sheet in the client binder explains in plain French. Documented with a state diagram, a swimlane, and a write-rules table naming which system owns which write.

### Standing rules learned here

- Use cost-efficient subagent tiers matched to the task (Martin, standing; saved to Claude memory). The six integration research passes ran as parallel Sonnet researchers, not as one expensive agent.
- Be honest where AI does not help. The same honesty rule that produced the "SANS IA, par choix" strip in the binder applies to the build plan: a work package that is plumbing gets described as plumbing.

## Related

- [[Areas/Lavoie/Contremaître — Groupe Lavoie Field-Operations Platform]]
- [[Areas/Lavoie/Contremaître Integrations — Verified API Capability Map (2026-07-10)]]
- [[Areas/Lavoie/Marketplace de débordement — Job Overflow and Payments Architecture (2026-07-10)]]
- [[Areas/Lavoie/AREA|Area — Lavoie]]
