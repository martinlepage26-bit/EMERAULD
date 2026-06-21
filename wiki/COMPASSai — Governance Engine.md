---
type: wiki
aliases: [COMPASSai, COMPASS AI, governance engine]
tags: [pharos, product, governance-software, compassai]
status: active
created: 2026-04-18
updated: 2026-05-07
---

# COMPASSai — Governance Engine

## Summary

COMPASSai is the governance engine software product within the [[PHAROS AI Ethics Submission — Springer Draft|PHAROS]] ecosystem — now recorded as a Web/SaaS application decision as of 2026-04-18 — that operationalizes the [[PHAROS Method — Technical Reference|PHAROS recursive governance method]] for client-facing use. It receives structured input through [[AurorA — COMPASSai Input Module]], its client-facing intake layer. COMPASSai is developed and operated by [[Martin Lepage — Professional Profile|Martin Lepage]] through PHAROS Inc.

## Context

COMPASSai is the product that converts the PHAROS governance pipeline into a deployable tool for organizations running AI inference workflows. It sits at the intersection of the [[PHAROS Runbook SOP|governance SOP]] and the [[InfraFabric Architecture]] module stack.

Earlier versions of this note described the architecture as TBD. Later operator-state evidence records the decision as Web/SaaS on 2026-04-18, aligned with the [[PHAROS-AI Webservice — pharos-ai.ca]] front door and direct client-facing assessment workflow. Treat the old desktop-vs-web language as superseded unless a newer architecture decision reverses it.

The [[Hermes Dashboard — Professional Governance Tool]] provides Martin's own activity-lane view of governance operations; COMPASSai is the client-facing counterpart.

## Details

**Role in the PHAROS stack:**
- Input layer: [[AurorA — COMPASSai Input Module]] (client-facing intake)
- Engine: COMPASSai (governance processing — this note)
- Operator view: [[Hermes Dashboard — Professional Governance Tool]]
- Public deployment: [[PHAROS-AI Webservice — pharos-ai.ca]]

**Current architecture decision:** Web/SaaS application available online for clients (decided 2026-04-18; recorded in `raw sources/2026-05-06_trismegiste-operator-state.md`).

**Current implementation evidence:** Local-stack runbook material describes a CompassAI backend at `http://127.0.0.1:9205/api/`, Mongo database `compassai`, JWT-protected routes, and an evidence-ingest route that can accept the internal service token used by AurorAI/AurorA handoff. This is local operational evidence, not proof of public production readiness.

**Source-of-truth candidates:** Current evidence points to `/home/cerebrhoe/PHAROS-SUITE/repos/pharos-suite/compassai` and older/parallel traces at `/home/cerebrhoe/PHAROS-SUITE/repos/CompassAI`, `/home/cerebrhoe/repos/CompassAI`, and the Martin public project page source at `/home/cerebrhoe/martin-lepage-site/src/content/projects/compassai-governance-engine.md`. These paths require a live repo check before any public capability claim.

**Governance alignment:** COMPASSai implements the 10-stage PHAROS pipeline (see [[PHAROS Invention Disclosure]]) and must enforce the consequence-binding map, admissibility rules, and promotion statuses described in the [[PHAROS Method — Technical Reference]].

## Key Ideas
- Governance engine that turns the PHAROS method into a product
- Client-facing intake through AurorA
- Web/SaaS is the current recorded architecture decision
- Capability claims must be bounded to verified routes, tests, and deployment evidence

## Open Questions
- Integration depth with InfraFabric modules
- Relationship to the Hermes Dashboard — separate interface or same product?
- Which repo/module path is authoritative for current development?
- Which capabilities are public-production-ready versus local-stack-only?

## Non-Claims

- Do not present COMPASSai as publicly production-ready unless the live deployment, auth, database, and assessment routes have been verified.
- Do not claim the full PHAROS 10-stage pipeline is operational merely because route shells or tests exist.
- Do not conflate older `CompassAI` repo traces with the current `COMPASSai` product name without source reconciliation.

## Related
- [[AurorA — COMPASSai Input Module]]
- [[COMPASSai — Fisher King Project State]]
- [[PHAROS Method — Technical Reference]]
- [[PHAROS Invention Disclosure]]
- [[Hermes Dashboard — Professional Governance Tool]]
- [[PHAROS-AI Webservice — pharos-ai.ca]]
- [[Governance and PHAROS MOC]]
