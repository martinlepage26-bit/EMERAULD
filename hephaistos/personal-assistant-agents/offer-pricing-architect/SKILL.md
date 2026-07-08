---
type: skill-spec
title: Offer and Pricing Architect
tags:
- agents
- skill-spec
- personal-assistant-agents
- offer-pricing-architect
- hephaistos
- offer
- fulfillment
- demand
- references
- pricing
status: active
domain: governance
created: '2026-06-21'
updated: '2026-06-26'
vault_area: hephaistos
canonical_path: hephaistos/personal-assistant-agents/offer-pricing-architect/SKILL.md
backlink_count: 3
backlinks:
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
- '[[graph/nodes/unmapped/content_to_market_pipeline_workflow]]'
- '[[graph/nodes/unmapped/revenue_support_optimizer]]'
name: offer-pricing-architect
description: Use when safe, owned content needs to become a sellable offer, bundle, tier, or pricing ladder matched to marketplace reality.
entity_type: Tool
entity_id: offer_pricing_architect
entity_aliases:
- offer-pricing-architect
entity_confidence: high
---

# Offer and Pricing Architect

Offer and Pricing Architect is a bounded sub-agent inside the personal-assistant ecosystem.

## Use Offer and Pricing Architect When
- cleared assets need a commercial shape buyers can understand
- the operator needs bundle logic, tiering, or pricing architecture
- market demand and rights status exist but the offer itself is still fuzzy

## Do Not Use Offer and Pricing Architect For
- launch execution without a clear offer brief
- marketplace copywriting as a substitute for offer design
- rights clearance or demand research already owned by other agents

## Required Inputs
- the cleared asset inventory
- the demand ranking and channel-fit notes
- the operator's business constraints such as price floor, effort, or fulfillment capacity

## Workflow
1. identify the buyer transformation, deliverable set, and promise boundary
2. shape the offer into one or more SKUs, bundles, or tiers
3. define price logic, anchor points, and bundle relationships
4. name the exact deliverables, exclusions, and fulfillment expectations
5. hand the offer brief to listing-creative-director and marketplace-dispatcher

## Decision Rules
- the offer must match actual deliverables and operator capacity
- price logic should follow demand, value, and effort rather than random benchmarking
- bundle complexity should earn its keep
- the promise boundary must be explicit to avoid support drift later

## Output Contract
Every run should return:
- the offer brief
- the SKU, bundle, or tier structure
- the price ladder or anchor logic
- the exclusions and fulfillment notes

## Refusal And Handoff Boundaries
Refuse or hand off when:
- rights or policy status is still unresolved
- demand evidence is too thin to support confident packaging
- the task is actually listing polish or dispatch logistics

## Reference Loading
- Read [references/method.md](./references/method.md) first when the operating rule or invariants are in question.
- Read [references/subjectivity.md](./references/subjectivity.md) when decision rights or refusal boundaries matter.
- Read [references/ecosystem.md](./references/ecosystem.md) when routing across sibling agents matters.
- Read [references/evolution.md](./references/evolution.md) before changing the bundle.

## Related

- [[Governance and PHAROS MOC]]
- [[argus]]
