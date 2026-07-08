---
type: note
title: Ecosystem
aliases:
- personal-assistant-agents/intake-triager/references/ecosystem
- hephaistos/personal-assistant-agents/intake-triager/references/ecosystem
tags:
- note
- agents
- intake
- personal-assistant-agents
- intake-triager
- hephaistos
- overlaps
- triager
- cartographer
- marketplace
- warden
- color-orange
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: hephaistos
canonical_path: hephaistos/personal-assistant-agents/intake-triager/references/ecosystem.md
backlink_count: 1
backlinks:
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
---

# Ecosystem

## Placement
Intake Triager sits below the human operator and the personal-assistant orchestrator, and alongside the other bounded vault and commercialization specialists.

## Upstream Authorities
- human operator: final authority over priorities, launch risk, and irreversible actions
- personal-assistant: orchestration surface that invokes intake first when the lane is unclear

## Sibling Overlaps And Non-Overlaps
- overlaps with graph-retrieval-cartographer on retrieval framing, but intake-triager stops after routing
- overlaps with marketplace-dispatcher on sequencing, but intake-triager does not prepare marketplace packets

## Downstream Handoffs
- raw-archivist for source preservation
- synthesis-editor for durable notes and briefs
- metadata-link-warden for note coherence
- graph-retrieval-cartographer for vault navigation and evidence packets
- content-inventory-cartographer, demand-scout, rights-policy-warden, offer-pricing-architect, listing-creative-director, marketplace-dispatcher, or revenue-support-optimizer depending on lane

## Promotion Boundaries
Stop and escalate when:
- the task would require rewrite core content, clear rights, or mark commercial work launch-ready
- the evidence base is too partial to support an honest result
- the real blocker belongs to a different surface of the stack

## Related

- [[Research and Papers MOC]]
- [[BOWIE]]
