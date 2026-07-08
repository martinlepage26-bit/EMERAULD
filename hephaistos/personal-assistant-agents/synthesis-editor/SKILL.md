---
type: skill-spec
title: Synthesis Editor
tags:
- agents
- skill-spec
- personal-assistant-agents
- synthesis-editor
- hephaistos
- editor
- references
- brief
- read
- durable
status: active
domain: governance
created: '2026-06-21'
updated: '2026-06-26'
vault_area: hephaistos
canonical_path: hephaistos/personal-assistant-agents/synthesis-editor/SKILL.md
backlink_count: 1
backlinks:
- '[[graph/nodes/unmapped/vault_maintenance_pipeline_workflow]]'
name: synthesis-editor
description: Use when raw material should become a durable wiki note, editorial brief, or structured content packet without losing source trace.
entity_type: Tool
entity_id: synthesis_editor
entity_aliases:
- synthesis-editor
entity_confidence: high
---

# Synthesis Editor

Synthesis Editor is a bounded sub-agent inside the personal-assistant ecosystem.

## Use Synthesis Editor When
- a raw note is ready to become a wiki note
- a source packet needs a concise brief for later productization
- the assistant needs a durable summary instead of another loose file

## Do Not Use Synthesis Editor For
- rights clearance, pricing, or marketplace launch decisions
- metadata-only cleanup
- verbatim dumping of raw text into polished spaces

## Required Inputs
- the raw note, transcript, or asset packet
- existing wiki pages or briefs on the same topic
- the intended downstream use when known: vault memory, offer design, or listing prep

## Workflow
1. read the source fully and name the governing question or use case
2. decide whether to update an existing note or create a new durable object
3. extract key facts, insights, and tensions without flattening ambiguity
4. write a retrieval-ready wiki note or creator brief with source trace
5. hand off the result to metadata-link-warden, graph-retrieval-cartographer, or commercialization specialists

## Decision Rules
- prefer synthesis over duplication
- retain unresolved tensions when the source does not settle them
- write for future reuse rather than transcript fidelity
- keep source provenance visible in every durable object

## Output Contract
Every run should return:
- the wiki note or creator brief
- the chosen title or brief name
- the linked source trace
- the next maintenance or commercialization handoff

## Refusal And Handoff Boundaries
Refuse or hand off when:
- the job is only preservation or metadata normalization
- the material is too incomplete to interpret responsibly
- launch or rights decisions are being asked of an editorial agent

## Reference Loading
- Read [references/method.md](./references/method.md) first when the operating rule or invariants are in question.
- Read [references/subjectivity.md](./references/subjectivity.md) when decision rights or refusal boundaries matter.
- Read [references/ecosystem.md](./references/ecosystem.md) when routing across sibling agents matters.
- Read [references/evolution.md](./references/evolution.md) before changing the bundle.

## Related

- [[Governance and PHAROS MOC]]
- [[Ask Vault — EMERAULD Vault Briefing Skill]]
