---
type: readme
title: Personal Assistant Agents
aliases:
- personal-assistant-agents/README
- hephaistos/personal-assistant-agents/README
tags:
- readme
- agents
- personal-assistant-agents
- readme-md
- hephaistos
- marketplace
- cartographer
- warden
- demand
- director
- color-orange
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: hephaistos
canonical_path: hephaistos/personal-assistant-agents/README.md
backlink_count: 1
backlinks:
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
---

# Personal Assistant Agents

Operate as a dual-purpose personal-assistant ecosystem that both maintains a retrieval-ready vault and commercializes owned content through bounded sub-agents dispatched into marketplaces.

## Assumptions
- The operator owns or controls the content being commercialized.
- Marketplace dispatch means preparing and routing marketplace-specific packets or workers, not making hidden commitments on the operator's behalf.
- Vault maintenance remains a standing responsibility rather than a one-time setup task.

## Source Packet
- Original vault-maintenance brief from the prior bundle set in this workspace
- User clarification on 2026-04-14: "the purpose of the agent is to sell its own content material using sub-agents dispacthed in market places"
- User clarification on 2026-04-14: "maintain the vault-maintenance as well. they will do nboth"

## Roster
| Slug | Agent | Scope |
| --- | --- | --- |
| `intake-triager` | Intake Triager | Route mixed requests across vault-maintenance and marketplace lanes. |
| `raw-archivist` | Raw Archivist | Preserve raw evidence, provenance, and content-commercialization trace. |
| `synthesis-editor` | Synthesis Editor | Turn raw material into durable notes and creator-ready briefs. |
| `metadata-link-warden` | Metadata and Link Warden | Keep frontmatter, source flags, product states, and backlinks coherent. |
| `graph-retrieval-cartographer` | Graph and Retrieval Cartographer | Maintain hubs, maps, and retrieval packets across the vault. |
| `content-inventory-cartographer` | Content Inventory Cartographer | Map owned content into saleable inventory and product families. |
| `demand-scout` | Demand Scout | Read demand, competitor patterns, and channel fit for owned content. |
| `rights-policy-warden` | Rights and Policy Warden | Protect sellability by clearing rights, licensing, and platform-policy fit. |
| `offer-pricing-architect` | Offer and Pricing Architect | Package safe content into offers, bundles, tiers, and price ladders. |
| `listing-creative-director` | Listing Creative Director | Create marketplace-facing copy, previews, and merchandising assets. |
| `marketplace-dispatcher` | Marketplace Dispatcher | Dispatch approved offers into marketplace-specific launch packets. |
| `revenue-support-optimizer` | Revenue and Support Optimizer | Read sales, support, and conversion signals and feed iteration back upstream. |

## Typical Routes
- Vault maintenance: `intake-triager` -> `raw-archivist` -> `synthesis-editor` -> `metadata-link-warden` -> `graph-retrieval-cartographer`
- Content-to-market pipeline: `graph-retrieval-cartographer` or `content-inventory-cartographer` -> `demand-scout` -> `rights-policy-warden` -> `offer-pricing-architect` -> `listing-creative-director` -> `marketplace-dispatcher`
- Post-launch learning loop: `revenue-support-optimizer` -> `offer-pricing-architect`, `listing-creative-director`, `marketplace-dispatcher`, or `demand-scout`

## Package Shape
Every agent bundle contains:
- `SKILL.md`
- `agents/openai.yaml`
- `references/method.md`
- `references/subjectivity.md`
- `references/ecosystem.md`
- `references/evolution.md`
- `skill.zip`

## Regeneration
Re-run `python3 personal-assistant-agents/generate_bundles.py` to rebuild the generated files and package zips.

## Related

- [[Governance and PHAROS MOC]]
- [[Obsidian Agent Vault — Launch Kit]]
