---
name: COMPASSai deployment phasing
description: Launch on Cloudflare free tier; migrate to custom Canadian hosting post-Lavoie
type: project
originSessionId: a383712c-ac27-4ec4-8eca-8c862212be3f
---
## Decision

**COMPASSai/AurorA deployment phased approach.**

**Date:** 2026-04-18  
**Decided by:** Martin Lepage

## Sequencing

**Phase 1 (Now → Lavoie project completion):**
- Platform: Cloudflare Pages (frontend) + Cloudflare Workers (backend)
- Cost: Free tier (~$0)
- AurorA: File-deposit module inside COMPASSai; clients upload assessment files
- Rationale: Speed to market, fast launch, no infrastructure cost

**Phase 2 (Post-Lavoie):**
- Platform: Custom hosting on Canadian infrastructure (Hetzner Canada, DigitalOcean Canada, or similar)
- Cost: ~$10-30/month
- Data residency: Canadian; full sovereignty
- Compliance: Audit trail, access control, encryption at rest all under Martin's control
- Rationale: Regulatory defensibility + client trust; justify infrastructure cost once revenue flows

## Why This Matters

- AurorA holds client files → data sovereignty critical for governance consultancy
- Cloudflare free tier acceptable for MVP; not acceptable for production client data
- Lavoie project likely first/early revenue → infrastructure investment justified post-launch
- Positions PHAROS as data-sovereign alternative (competitive advantage)

## Related Decisions

- [decision_compass_web_saas.md](./decision_compass_web_saas.md) — COMPASSai is Web/SaaS
- Hermes Dashboard: Separate product (can stay on Cloudflare; no client data)

## Related

- [[Governance and PHAROS MOC]]
- [[HELIX — Value Proposition and Buyer Profile]]
