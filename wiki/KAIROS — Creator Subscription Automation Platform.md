---
type: wiki
title: KAIROS — Creator Subscription Automation Platform
aliases:
- KAIROS
- Creator Subscription Automation
tags:
- product
- pharos
- saas
- automation
- governance
- projects
status: active
created: '2026-08-13'
updated: '2026-08-13'
vault_area: wiki
canonical_path: wiki/KAIROS — Creator Subscription Automation Platform.md
---

# KAIROS — Creator Subscription Automation Platform

## Summary

KAIROS is a subscription platform that plans, publishes, and grows a creator's audience without the creator scheduling posts or answering messages by hand. It was built in this vault at `projects/products/kairos/` on the same Cloudflare Workers stack as [[AurorA — Fisher King Project State]] and [[COMPASSai — Fisher King Project State]], and it carries the same governance posture as the rest of the [[PHAROS — Fisher King Project State]] product line.

The name takes the Greek sense of *kairos*: not clock time, but the opportune moment. The system's actual decision is when a thing should be said, and to whom.

## Context

The brief was to build a growth engine around systems rather than daily labour, reaching $50,000 monthly recurring revenue in ninety days with AI tooling and no employees.

The strategically load-bearing finding is that $50,000 MRR is two different businesses depending on the buyer, and only one is reachable by a single operator in ninety days. Selling to solo creators at $49 requires roughly 1,020 accounts, which at normal self-serve conversion means about 34,000 trials from a standing start. Selling to agencies who manage other people's accounts requires 127 customers at a blended ARPU near $395, which is two closes per working day. Same product, same build cost, twenty-fold difference in ARPU depending on where it is pointed.

This mirrors the positioning logic in [[Obsidian Agent Vault Launch — Commercial Skill]]: the artefact is not the product, the buyer's cost of labour is.

## Details

Five autonomous loops, each a cron trigger over a D1-backed job queue:

- **Planning** builds a rolling fourteen-day calendar, allocating across content pillars by measured performance.
- **Drafting** generates several variants per slot against a prompt-cached brand-voice prefix.
- **Publishing** dispatches through platform adapters with retry, backoff, and idempotency keys that make double-posting structurally impossible.
- **Engagement** triages inbound messages by intent and priority, drafts replies, and sends only those that clear an explicit policy gate.
- **Growth** measures results, rewrites pillar weights, and recycles proven posts. This feedback edge is what separates a growth engine from a scheduler.

### Governance surface

The vault's standing ethical layer requires that automated pipelines carry a stop condition, an audit trail, and a rollback path. Each is a table rather than a convention, which is the same argument made in [[the-control-is-the-evidence-trail]] and [[human-in-the-loop-is-not-an-accountability-structure]]: a control that exists only as intention is not a control.

Autopilot defaults to off, and an account with no controls row gets autopilot off rather than a permissive default, because a creator who has never made a choice has not consented to unattended publishing. Two policies are enforced in code rather than in prompts, since a prompt is a request and a gate is a guarantee: the banned-phrase list is checked after generation, and the system refuses to auto-send replies on lead, collaboration, and hostile threads regardless of what the per-intent rules table permits.

### Economics

Prompt caching is architectural rather than an optimisation. The operator prompt and the creator's strategy sit first in the prefix behind a cache breakpoint, turning a $0.0075 input span into $0.00075 per call. Across 300 accounts that difference is roughly the margin on ten Pro subscriptions.

Plan allowances were set from the margin model, not from intuition. The first pass gave the Agency tier 8,000 replies and 2,500 posts, which computed to 59.7% gross margin at full consumption; the allowance was cut rather than the claim softened. Every tier now clears 70% at full consumption and lands near 88% at realistic use.

## Status

Code complete and verified: 30 tests pass against real SQLite through a D1-shaped shim, executing the actual migration rather than mocks. `DRY_RUN` defaults on, so the full pipeline runs end to end before any creator connects an account. Not yet deployed, and no live platform credentials are configured.

## Related

- [[PHAROS — Fisher King Project State]] — parent product line and stack
- [[AurorA — Fisher King Project State]] — shares the Workers/D1/R2 architecture
- [[Governance and PHAROS MOC]] — governance index
- [[Projects Hub]] — project map
