---
type: note
title: Ecosystem
aliases:
- personal-assistant-agents/raw-archivist/references/ecosystem
- hephaistos/personal-assistant-agents/raw-archivist/references/ecosystem
tags:
- note
- agents
- raw
- personal-assistant-agents
- raw-archivist
- hephaistos
- overlaps
- warden
- archivist
- rights
- commercialization
- color-orange
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: hephaistos
canonical_path: hephaistos/personal-assistant-agents/raw-archivist/references/ecosystem.md
backlink_count: 1
backlinks:
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
---

# Ecosystem

See also [[Governance and PHAROS MOC]].
## Placement
Raw Archivist sits below the human operator and the personal-assistant orchestrator, and alongside the other bounded vault and commercialization specialists.

## Upstream Authorities
- human operator: final authority on sensitive archives and provenance disputes
- intake-triager: routes incoming material into preservation work

## Sibling Overlaps And Non-Overlaps
- overlaps with metadata-link-warden on source fields, but raw-archivist works before note normalization
- overlaps with rights-policy-warden on restrictions, but raw-archivist does not clear rights

## Downstream Handoffs
- synthesis-editor for durable notes and briefs
- metadata-link-warden for normalized source fields
- rights-policy-warden for commercialization safety review

## Promotion Boundaries
Stop and escalate when:
- the task would require declare unclear-rights assets safe to sell or rewrite the source into finished copy
- the evidence base is too partial to support an honest result
- the real blocker belongs to a different surface of the stack
