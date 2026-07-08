---
type: wiki
title: Obsidian Agent Vault Launch — Commercial Skill
aliases:
- obsidian-agent-vault-launch
- vault launch skill
- agent vault commercialization skill
- wiki/Obsidian Agent Vault Launch — Commercial Skill
tags:
- skill
- claude-code
- obsidian
- commercial
- launch
- agent-memory
- wiki
- obsidian-agent-vault-launch-commercial-skill-md
- claude
- retrieval
- agent
- color-orange
status: active
created: '2026-04-16'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Obsidian Agent Vault Launch — Commercial Skill.md
backlink_count: 9
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[wiki/Ask Vault — EMERAULD Vault Briefing Skill]]'
- '[[wiki/Elemental Agents — Productization Plan (2026-05-24)]]'
- '[[wiki/Obsidian Second Brain Product]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[archive/session-state/session-state-002]]'
- '[[assets/elemental-agents/positioning-memo]]'
- '[[assets/elemental-agents/sales-page-outline]]'
- '[[hephaistos/personal-assistant-agents/trismegiste/vault/CLAUDE]]'
---

# Obsidian Agent Vault Launch — Commercial Skill

## Summary

A Claude Code skill (from `obsidian-agent-vault-launch-v2.zip`, 2026-04-14) that converts rough product notes, launch fragments, and positioning ideas into commercial launch packages for lightweight agent-memory products. It is the production mechanism behind the [[Obsidian Agent Vault — Launch Kit]] and [[Obsidian Agent Vault — Setup Guide]] artifacts already in the vault. The v2 release is canonical.

## Context

This skill lives at the intersection of the [[GSD — Get Shit Done Context Engineering System]] (rapid, structured output production) and the vault's commercialization work documented in [[Obsidian Agent Vault — Launch Kit]]. It operationalizes the insight that the vault architecture itself — as practiced in [[EMERAULD Second Brain — Project Context]] — is a sellable product, not just a personal tool. The skill automates the translation from "here's a rough positioning idea" to "here's a market-ready launch kit." Part of the [[Claude Code Skill Corpus]].

## Details

### What It Does

Takes rough product notes, launch fragments, or positioning ideas and produces a complete commercial launch package for lightweight agent-memory products: Obsidian templates, Claude Code context layers, skill packs.

### Trigger Phrases

- "make this sellable"
- "turn this into a launch kit"
- "sharpen the offer"
- "write the product page"
- "write gumroad copy"

### Output Types

| Output | Description |
|---|---|
| Offer summary | Condensed positioning statement |
| Product page | Long-form framing asset with headline, benefits, price ladder |
| Marketplace copy | Gumroad or Lemon Squeezy listing — title, short desc, full desc, buyer/anti-fit |
| Demo script | Three-act before/after video sequence |
| Posting sequence | Problem hook, mechanism, social proof, ladder offer |
| Launch kit | Full package combining all of the above |

### Core Positioning Rule

Simple contrast framing:

- **Old way**: copy-paste context, re-explain to the agent every session
- **New way**: structured vault, reusable notes, guided retrieval

Default framing anchors: file-native, agent-legible, fast to install, zero RAG stack, useful immediately.

### Memory Architecture Vocabulary (v2 Addition)

v2 introduces a technical vocabulary drawn from production memory systems, giving the product credibility without overstating what files can do.

#### Retrieval Modes (file-native equivalents of [[LightRAG — Graph-Based RAG System]] modes)

| Mode | Vault Behavior |
|---|---|
| `local` | Agent reads a specific note directly (skill file, decision log, project spec) |
| `global` | Agent reads a hub note to orient across the whole project |
| `hybrid` | Agent reads hub note + linked notes to triangulate an answer |
| `naive` | Agent scans raw folder for recent unprocessed notes |
| `mix` | Agent reads full vault map (CLAUDE.md + all hub notes) before answering |

Use these terms when explaining retrieval behavior to technical buyers. They map to visible vault structure, not invisible infrastructure.

#### Progressive Disclosure (3-Layer Architecture)

Memory retrieval follows a token-cost-aware 3-layer pattern:

| Layer | Content | Token Cost |
|---|---|---|
| Index | CLAUDE.md + hub notes | Low — orientation only |
| Navigation | Linked wiki notes + skill files | Medium — specific domain |
| Detail | Raw notes, decision logs, full documents | High — only when needed |

Agents start at the index layer and descend only as needed. This is the vault's answer to "how does it handle large vaults and token cost."

#### Context-Aware Linking Rule

When converting a raw note into a wiki note, include: the original question that prompted the note, the project context it lives in, and at least one backlink to a related note. This is the vault equivalent of RAG-Anything's context-aware processing principle.

#### Privacy Tags

Sensitive content can be excluded from agent context using a `private::` frontmatter tag or inline `<!-- private -->` comment. Document this in the vault's CLAUDE.md template. (Pattern adapted from claude-mem's `<private>` tag system — see [[claude-mem — Persistent Memory Compression for Claude Code]].)

#### Session Lifecycle Framing

| Phase | Agent Action |
|---|---|
| SessionStart | Reads CLAUDE.md + relevant hub notes to orient |
| Active session | Navigates wiki layer as needed |
| SessionEnd | Agent (or user) promotes raw notes created during session |

Use this three-phase framing in demo scripts and product page body copy.

### Competitive Positioning (v2 Addition)

| Alternative | What it does | Why the vault is different |
|---|---|---|
| [[claude-mem — Persistent Memory Compression for Claude Code]] | Passive capture, SQLite + Chroma, background daemon on port 37777 | Zero-dependency, intentional structure, no daemon |
| [[LightRAG — Graph-Based RAG System]] | Graph-based RAG, full Python stack, FastAPI server | File-native, no infrastructure, installs in minutes |
| [[RAG-Anything — Multimodal RAG Framework]] | Multimodal document pipeline built on LightRAG | Vault is for code project memory, not document ingestion |

Positioning summary: more intentional than passive capture, zero infrastructure versus graph RAG stacks.

### Internal Workflow Steps

1. Identify the wedge — narrowest honest promise (what pain, what stops, what gets easier)
2. Identify the mechanism — translate vague benefit into visible structure (CLAUDE.md, hub notes, synthesis prompt, session lifecycle)
3. Identify the commercial ladder — sane escalation path
4. Build assets — only what is needed for the user's current stage
5. Pressure test — does this sound real, does it overclaim, can someone ship it today?

### Language Rules

**Avoid:**
- "revolutionary", "autonomous intelligence", "infinite memory"
- "guaranteed productivity", "fully automatic knowledge engine"

**Prefer:**
- "skip the RAG stack"
- "structured memory for file-aware agents"
- "your agent stops searching blind"
- "progressive retrieval from orientation to detail"
- "context that survives the session"

### Pricing Ladder

| Tier | Price | Scope |
|---|---|---|
| Template pack | $49 | Vault zip + setup guide |
| Guided setup | $299 | Async, 1 session |
| Team implementation | $2,500 | Up to 5 seats, live |

The ladder is one infrastructure product at three depths, not three separate products. The million-dollar path comes from escalation: template → service → team package → software layer.

### Technical Credibility Mapping

| Component | What to call it |
|---|---|
| CLAUDE.md | Orientation / context guidance (index layer) |
| skill.md files | Reusable workflow instructions (navigation layer) |
| Hub notes | Navigational structure (global retrieval posture) |
| Synthesis prompts | Note-conversion logic (raw-to-wiki pipeline) |
| Backlinks | Context-aware linking mechanism |
| Raw folder | Naive retrieval posture |
| Progressive disclosure | Token-cost management strategy |

Do not claim vector search, automatic compression, or database-backed retrieval.

### Version

- v2 is canonical (from `obsidian-agent-vault-launch-v2.zip`, 2026-04-14)
- v1 exists in archive (`skill.zip`) but v2 supersedes it; key v2 additions are retrieval-mode vocabulary, progressive disclosure framing, competitive positioning table, privacy tag protocol, and session lifecycle framing

### Source Files

- `raw sources/obsidian-agent-vault-launch-v2-skill-2026-04-16.md`

## Key Ideas

- The skill is a commercialization layer, not a product-building layer — it assumes the vault product already exists and focuses on how to sell it.
- The "skip the RAG stack" positioning is a deliberate subtraction move: it differentiates by what the product does *not* require, not by feature inflation. This connects directly to the anti-overbuild argument in [[Obsidian Agent Vault — Launch Kit]].
- The three-act demo script (messy notes → structured vault + CLAUDE.md → successful retrieval) is the proof-of-concept that the vault changes agent behavior — not a feature tour.
- The pricing ladder works because it is one product at three depths: buyers can enter cheap and upgrade, not choose between unrelated things.
- v2 introduces retrieval-mode vocabulary borrowed from [[LightRAG — Graph-Based RAG System]] but implemented as folder and link conventions — this gives the product technical credibility without requiring any LightRAG infrastructure. The mapping is honest: file-native equivalents, not claims of graph-based retrieval.
- Progressive disclosure is the vault's structural answer to the token-cost objection: orient at the index layer (cheap), navigate to detail only when required.

## Open Questions

- Is v2 published or still draft?
- Does the skill handle French-language launch copy, given Martin's bilingual market?
- Should this skill be listed in the [[Claude Code Skill Corpus]] index for discoverability?
- The skill references three load-on-demand reference files (`references/offer-templates.md`, `references/demo-structures.md`, `references/posting-hooks.md`) — do these exist in the skill zip, or are they stubs?
- Should the privacy tag protocol (`private::` frontmatter / `<!-- private -->` inline) be documented in the [[Obsidian Agent Vault — Setup Guide]]?

## Sources

- `raw sources/obsidian-agent-vault-launch-v2-skill-2026-04-16.md`

## Related

- [[manual]]
- [[Obsidian Agent Vault — Launch Kit]]
- [[Obsidian Agent Vault — Setup Guide]]
- [[Claude Code Skill Corpus]]
- [[GSD — Get Shit Done Context Engineering System]]
- [[EMERAULD Second Brain — Project Context]]
- [[HEPHAISTOS]]
- [[Personal and Projects MOC]]
- [[CONTINUITY]]
- [[CHANGELOG]]
- [[CLAUDE]]
