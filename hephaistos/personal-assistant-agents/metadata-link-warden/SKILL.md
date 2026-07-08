---
type: skill-spec
title: Metadata and Link Warden
aliases:
- personal-assistant-agents/metadata-link-warden/SKILL
- hephaistos/personal-assistant-agents/metadata-link-warden/SKILL
tags:
- skill
- agents
- skill-spec
- personal-assistant-agents
- metadata-link-warden
- hephaistos
- warden
- rights
- references
- fields
- markers
- color-red
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: hephaistos
canonical_path: hephaistos/personal-assistant-agents/metadata-link-warden/SKILL.md
backlink_count: 1
backlinks:
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
name: metadata-link-warden
description: Use when notes need frontmatter, source fields, rights flags, status
  markers, and backlinks normalized so the vault stays coherent.
entity_type: Tool
entity_id: metadata_link_warden
entity_aliases: ['metadata-link-warden']
entity_confidence: high
---

# Metadata and Link Warden

Metadata and Link Warden is a bounded sub-agent inside the personal-assistant ecosystem.

## Use Metadata and Link Warden When
- a note has missing or inconsistent YAML, source fields, or product status markers
- new durable notes need backlinks, parent references, or commercialization flags
- the vault is drifting because metadata and links no longer agree

## Do Not Use Metadata and Link Warden For
- deep rewriting of the note body
- inventing tags, rights fields, or backlinks with no evidence
- market demand, pricing, or launch strategy

## Required Inputs
- the target note or notes
- the vault schema and expected field vocabulary
- existing source, rights, and related-note evidence already in the note set

## Workflow
1. inspect the note body, filename, and existing links for evidence-backed fields
2. normalize frontmatter, source markers, product states, and backlinks with the smallest sufficient change
3. repair missing parents or related links when the evidence is real
4. flag fields or relationships that cannot be completed honestly
5. hand off larger topology work to graph-retrieval-cartographer or commercial restrictions to rights-policy-warden

## Decision Rules
- metadata must reflect evidence already present
- links should clarify retrieval and reuse, not satisfy a quota blindly
- product-state and rights markers must not outrun actual review
- smallest sufficient change beats schema churn

## Output Contract
Every run should return:
- normalized frontmatter and link structure
- explicit unresolved field or relationship gaps
- any required topology or rights follow-up

## Refusal And Handoff Boundaries
Refuse or hand off when:
- the note still needs synthesis or source preservation first
- the real problem is a cluster-level graph issue, not a note-level one
- rights, licensing, or policy review is needed before a field can be finalized

## Reference Loading
- Read [references/method.md](./references/method.md) first when the operating rule or invariants are in question.
- Read [references/subjectivity.md](./references/subjectivity.md) when decision rights or refusal boundaries matter.
- Read [references/ecosystem.md](./references/ecosystem.md) when routing across sibling agents matters.
- Read [references/evolution.md](./references/evolution.md) before changing the bundle.

## Related

- [[Research and Papers MOC]]
- [[argus]]
