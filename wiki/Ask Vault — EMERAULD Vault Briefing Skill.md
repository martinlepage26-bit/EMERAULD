---
type: wiki
title: Ask Vault — EMERAULD Vault Briefing Skill
aliases:
- ask-vault
- EMERAULD vault briefing skill
- vault query skill
- wiki/Ask Vault — EMERAULD Vault Briefing Skill
tags:
- skill
- codex
- emerauld
- retrieval
- second-brain
- trismegiste
- obsidian
- wiki
- ask-vault-emerauld-vault-briefing-skill-md
- briefing
- apps
- color-orange
status: active
created: '2026-04-23'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Ask Vault — EMERAULD Vault Briefing Skill.md
backlink_count: 22
backlinks:
- '[[.planning/PROJECT]]'
- '[[.planning/phases/01-lightrag-script-runtime-hardening/01-REVIEW]]'
- '[[wiki/AI Infrastructure Stack]]'
- '[[Areas/PHAROS/Claude Code Skill Corpus]]'
- '[[archive/wiki-2026-07-08/Desktop Obsidian and Personal Assistant Setup Logs — 2026-04-14]]'
- '[[Areas/PHAROS/Kickstart App Prompt — Template and Synthesis Framework]]'
- '[[wiki/Martin Lepage — Adjacent Skill Ring]]'
- '[[wiki/Martin Lepage — Authored Skills]]'
- '[[wiki/Martin Lepage — Skills by Life Domain]]'
- '[[Areas/PHAROS/Obsidian Second Brain Product]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[wiki/Root Loose Notes Cluster Map — 2026-05-06]]'
- '[[wiki/Skill Development Workflow — TDD, Dual-Layer, and Eval-Iterate]]'
- '[[wiki/Skill Domain — Vault and Knowledge]]'
- '[[Areas/PHAROS/Skill Ecosystem — Professional Capability Registry]]'
- '[[artifacts/marketplace/obsidian-agent-vault-2026-04-19/AGENT-NAMING-STUDY]]'
- '[[governance/hephaistos/CLAUDE-REVIEW-CHECKLIST]]'
- '[[hephaistos/personal-assistant-agents/metadata-link-warden/references/ecosystem]]'
- '[[hephaistos/personal-assistant-agents/raw-archivist/SKILL]]'
- '[[hephaistos/personal-assistant-agents/synthesis-editor/SKILL]]'
- '[[hephaistos/personal-assistant-agents/synthesis-editor/references/ecosystem]]'
- '[[projects/Second Brain — Fisher King Project State]]'
---

# Ask Vault — EMERAULD Vault Briefing Skill

## Summary

Ask Vault is a local [[Claude Code Skill Corpus|Claude Code skill]] that turns EMERAULD into a read-only briefing surface. It answers retrieval questions from the vault by distinguishing current state (`session-state.md`, `memory.md`) from durable knowledge (`wiki/`), then returning a concise answer plus the most relevant canonical note. The live bundle sits at `/home/cerebrhoe/.codex/skills/ask-vault/`.

## Context

The skill was created on 2026-04-23 after the Apps SDK planning pass concluded that the strongest P0 surface was not a write workflow or a compliance report generator, but a **read-only EMERAULD vault briefing app**. In that sense, Ask Vault operationalizes the same bounded use case described in [[ChatGPT Apps SDK — Planning, Metadata, Deployment, and Operations]]: brief the user from an existing knowledge base first, prove discovery and retrieval, and add riskier actions only later.

Inside the local stack, Ask Vault is effectively a portable Trismégiste stance. [[Trismégiste — Personal AI Assistant]] remains the named assistant identity for EMERAULD; Ask Vault packages the retrieval logic of that role into a reusable skill with explicit routing and boundaries. Raw capture of the bundle is preserved at `raw sources/2026-04-23_ask-vault-skill.md`.

## Details

### What the skill does

- answers from EMERAULD before answering from general memory
- identifies one canonical note when confidence is high
- adds 1-3 supporting notes only when they materially improve the answer
- keeps provenance visible by naming the note path in the reply
- stays read-only: no note creation, rewriting, or backlink repair

### Retrieval model

The skill uses a three-layer distinction that matches EMERAULD's actual operating boundaries:

- **Recent working state** — `session-state.md`
- **Live business mirror** — `memory.md`
- **Durable knowledge graph** — `wiki/`

That distinction matters because many vault questions are not really "what is this note about?" but "what is happening now?" or "what should I read first?". Ask Vault encodes that routing explicitly in `references/emerauld-entrypoints.md`.

### Search surface

The skill does not rely on passive intuition. It names the concrete local tools to use:

- `rg` across `wiki/`, `session-state.md`, and `memory.md` when the target is probably exact or near-exact
- `scripts/vsearch.py` when the question is conceptual or wording is fuzzy

This makes the skill a thin operational layer over the actual EMERAULD retrieval stack documented in [[AI Infrastructure Stack]].

### Why it matters

Ask Vault is important for three different reasons at once:

1. It makes Trismégiste's retrieval behavior reusable instead of leaving it as an implicit operator habit.
2. It is the cleanest current proof that EMERAULD can act as a **question-answering second brain**, not just a note archive.
3. It provides a concrete bridge from the vault to a future product surface or Apps SDK connector, because the use case is already sharply bounded and read-only.

### Boundaries

The skill refuses several tempting failure modes:

- no live web facts from vault notes alone
- no editing or synthesis through the retrieval surface
- no descent into `raw sources/` unless the wiki lacks the answer or provenance is explicitly requested
- no conflation of vault mirrors with external runtime systems of record

These constraints keep the skill narrow enough to be trustworthy.

## Key Ideas

- A second brain becomes more useful when its retrieval behavior is explicit, not only embodied in one agent persona
- Canonical-note selection is part of the answer, not an optional convenience
- Read-only boundedness is a feature, not a limitation, for first-stage vault products

## Insights

- Ask Vault is not just another skill in the corpus; it is a direct formalization of EMERAULD's internal memory architecture into a user-facing briefing pattern
- The split between `session-state.md`, `memory.md`, and `wiki/` is one of the sharpest parts of the design because it preserves the difference between "what is true now" and "what the archive knows durably"

## Open Questions

- Should Ask Vault remain purely local to Trismégiste workflows, or become the first public-facing retrieval skill in the Obsidian Agent Vault product line?
- Does a later version need a write companion, or is keeping retrieval and editing separate the safer long-term architecture?

## Sources

- `raw sources/2026-04-23_ask-vault-skill.md`
- `/home/cerebrhoe/.codex/skills/ask-vault/SKILL.md`
- `/home/cerebrhoe/.codex/skills/ask-vault/references/emerauld-entrypoints.md`

## Related

- [[Trismégiste — Personal AI Assistant]]
- [[ChatGPT Apps SDK — Planning, Metadata, Deployment, and Operations]]
- [[Claude Code Skill Corpus]]
- [[AI Infrastructure Stack]]
- [[Obsidian Second Brain Product]]
- [[Obsidian Agent Vault Launch — Commercial Skill]]
- [[Skill Development Workflow — TDD, Dual-Layer, and Eval-Iterate]]
- [[PROJECT]]
- [[01-REVIEW]]
- [[AGENT-NAMING-STUDY]]
- [[CLAUDE-REVIEW-CHECKLIST]]
- [[ecosystem]]
- [[SKILL]]
