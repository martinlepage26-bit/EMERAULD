---
type: wiki
title: Claude Code Skill Corpus
aliases:
- Claude Code Skill Corpus
tags:
- areas
- skill
- claude-code-skill-corpus-md
- anything
- mubu
- novita
- skills
- color-orange
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/Claude Code Skill Corpus.md
backlink_count: 40
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[Areas/PHAROS/Agatha Unified Skill System — Eight Sovereign Operators]]'
- '[[wiki/Ask Vault — EMERAULD Vault Briefing Skill]]'
- '[[archive/wiki-2026-07-08/Codex Skill Corpus Sync — 2026-04-20]]'
- '[[wiki/Codex Skills Inventory — Complete Registry (241 Skills)]]'
- '[[Areas/PHAROS/Diamond-Eyes — Aesthetic Refinement Skill]]'
- '[[Resources/Epistemic Governance — Canonical Reference]]'
- '[[wiki/Epistemic Operator — Operational Specification]]'
- '[[wiki/GSD Tier 1 — Core Workflow Skills Hub]]'
- '[[wiki/Governed Revision Loop — Responsible Self-Improving Agents]]'
- '[[Areas/PHAROS/HEPHAISTOS Agent Architecture]]'
- '[[archive/wiki-2026-07-08/HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)]]'
- '[[wiki/Home]]'
- '[[wiki/Kickstart App Prompt — Template and Synthesis Framework]]'
- '[[wiki/MASTERxMASTERxMASTER — Skill Corpus Map]]'
- '[[wiki/Martin Lepage Professional Identity]]'
- '[[wiki/Martin Lepage — Adjacent Skill Ring]]'
- '[[wiki/Martin Lepage — Authored Skills]]'
- '[[wiki/Martin Lepage — Skills by Life Domain]]'
- '[[wiki/Obsidian Agent Vault Launch — Commercial Skill]]'
- '[[Areas/PHAROS/Obsidian Agent Vault — Launch Kit]]'
- '[[Areas/PHAROS/Obsidian Agent Vault — Setup Guide]]'
- '[[wiki/Obsidian Second Brain Product]]'
- '[[wiki/PHAROS Skill Corpus Change Genealogy — 2026-05-06]]'
- '[[Areas/PHAROS/PHAROS Strategic Analysis — Keep Stop Fix Finish (2026-04-18)]]'
- '[[wiki/PHAROS Workspace Inventory 2026-04-18]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[wiki/Phenomenology Hermeneutics Heuristics — Robinson 1996 Seminar Critique]]'
- '[[wiki/Reddit Data API — Access Terms and Rate Limits]]'
- '[[wiki/Rest and Consolidation Guide — Martin]]'
- '[[wiki/Skill Corpus Genealogy Delta — 2026-05-06]]'
- '[[Areas/PHAROS/Skill Corpus — Complete Live Index (260 Active Skills)]]'
- '[[wiki/Skill Development Workflow — TDD, Dual-Layer, and Eval-Iterate]]'
- '[[Areas/PHAROS/Skill Ecosystem — Professional Capability Registry]]'
- '[[wiki/Skill-Pairing — Five-Case Test Suite]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[archive/session-state/session-state-002]]'
- '[[wiki/claude-mem — Persistent Memory Compression for Claude Code]]'
- '[[memory/agents/Journal]]'
- '[[wiki/skills/observability-governance]]'
---

# Claude Code Skill Corpus

## Summary
A library of Claude Code skills stored in raw sources and `/home/cerebrhoe/.codex/skills/`. Skills are invokable instruction sets that extend agent behavior for specific domains. The corpus includes governance, aesthetic refinement, research, and agent-subagent coordination patterns. Core to the [[InfraFabric Architecture]] and the [[Recursive Deterministic AI Governance — Method and Paper|three-agent governance]] workflow. **Unified registry:** [[Skill Ecosystem — Professional Capability Registry]].

## Context
Skills are invoked via the Claude Code Skill tool. Primary skill directory: `/home/cerebrhoe/.codex/skills/`. Legacy scaffolding: `HEPHAISTOS_BUILD/EXTRACTED/SKILLS Claude/`. The raw sources directory contains 15 SKILL files representing two distinct categories: Claude Code agent skills (portable reasoning modes) and CLI-Anything harness skills (tool-specific operational skill files for the [[CLI-Anything — Agent Harness for Tool Integration]] project). See also [[Diamond-Eyes — Aesthetic Refinement Skill]] for a detailed example of a Claude Code agent skill.

## Details

### Claude Code Agent Skills

| File | Skill Name | Domain |
|---|---|---|
| `SKILL.md` | `diamond-eyes` | Aesthetic refinement — see [[Diamond-Eyes — Aesthetic Refinement Skill]] |
| `SKILL(1).md` | `queen-keyport` | High-pressure analytical reasoning, structural analysis, governance-critical rewriting |
| `gsd-advisor-researcher.md` | `gsd-advisor-researcher` | Sub-agent: researches gray area decisions, returns comparison table |
| `gsd-assumptions-analyzer.md` | `gsd-assumptions-analyzer` | Sub-agent: analyzes unstated assumptions in proposed decisions |

### CLI-Anything Harness Skills

| File | Skill Name | Tool |
|---|---|---|
| `SKILL(2).md` | `cli-anything-libreoffice` | LibreOffice — real ODF file editing without GUI or installation |
| `SKILL(3).md` | `cli-anything-mermaid` | Mermaid diagrams via mermaid.ink renderer |
| `SKILL(4).md` | `cli-anything-mubu` | Mubu mindmap (packaged entrypoint) |
| `SKILL(5).md` | `musescore` | MuseScore 4 — transpose, export PDF/audio/MIDI/MusicXML |
| `SKILL(6).md` | `cli-anything-n8n` | n8n workflow automation platform |
| `SKILL(7).md` | `cli-anything-notebooklm` | NotebookLM notebook management and source ingestion |
| `SKILL(8).md` | `cli-anything-novita` | Novita AI — OpenAI-compatible API for DeepSeek, GLM |
| `SKILL(9).md` | `cli-anything-obsidian` | Obsidian vault via Local REST API |
| `SKILL(10).md` | `cli-anything-obs_studio` | OBS Studio scene collection editing |
| `SKILL(11).md` | `cli-anything-ollama` | Ollama local LLM inference |
| `SKILL(12).md` | `cli-anything` (OpenClaw) | CLI-Anything builder adapted for OpenClaw agent |
| `SKILL(13).md` | `cli-anything-openscreen` | Openscreen screen recording editor |
| `SKILL(14).md` | `cli-anything-pm2` | PM2 Node.js process management (stateless) |

### Queen Keyport Skill Profile
Operates as a sovereign editor and structural analyst. Leads with governing claim, names the frame before entering detail. Used for: argument stripping, stress-testing claims, exposing weak logic, governance framing, manuscript rewriting for precision and intellectual force. Especially effective in philosophy, governance, and strategic framing contexts. This skill is distinct from the [[Recursive Deterministic AI Governance — Method and Paper|Queen Keyport governance agent]] — it implements the analytical stance, not the full governance protocol.

### GSD Subagents
Two sub-agents spawned by a `discuss-phase` coordinator for decision-support workflows:
- **gsd-advisor-researcher**: researches a single gray area, produces a 5-column comparison table with rationale paragraph. Spawned via `Task()`, returns structured markdown to the main agent.
- **gsd-assumptions-analyzer**: analyzes unstated assumptions in a proposed course of action.

### GSD Workflow Hub
The wider GSD workflow family now has a dedicated vault-side entrypoint:

- [[GSD Tier 1 — Core Workflow Skills Hub]] — Tier 1 command-family documentation hub
- [[GSD — Get Shit Done Context Engineering System]] — command and architecture reference
- [[GSD — Get-Shit-Done Claude Code System]] — local installation and surface reference

### Skill Loading Rules
- No skill is self-authorizing; skills are advisory and invoked on demand
- Skills are invoked via the Skill tool, not embedded in governance files
- `diamond-eyes` as a local refinement skill lives at `/home/cerebrhoe/.codex/skills/diamond-eyes/` (the governance principle is now [[Consented Frame — Ethics and Wisdom Gate]], avoiding the old naming collision)
- For complex orchestration, `skill-architect` delegates to other skills via parallel Tasks

## Key Ideas
- Two distinct categories share the SKILL file namespace: Claude Code agent skills and CLI-Anything harness skill files
- The CLI-Anything skills are documentation/instruction files consumed by the agent to operate each tool — not governance skills
- 14 CLI-Anything tools are currently represented: LibreOffice, Mermaid, Mubu, MuseScore, n8n, NotebookLM, Novita, Obsidian, OBS Studio, Ollama, OpenClaw, Openscreen, PM2

## Insights
- The queen-keyport skill encodes the analytical stance of the governance agent as a portable reasoning mode — applicable outside formal governance contexts
- The GSD sub-agent pattern (spawned via `Task()`, returns structured output for synthesis) is a clean parallel-research architecture
- OpenClaw appears to be an agent runtime (SKILL(12) adapts CLI-Anything methodology for it) — distinct from the CLI-Anything project itself
- The GSD workflow system is a separate documentation cluster from the two GSD sub-agents; Tier 1 now has its own hub page

## Open Questions
- What is OpenClaw exactly? An agent runtime, a different AI assistant, or an internal tool?
- Is the `gsd-assumptions-analyzer` currently active or archived?
- Are the LibreOffice, Mermaid, n8n, and Novita harnesses as complete as Mubu/Ollama/Obsidian?

## Sources
`raw sources/SKILL.md`, `raw sources/SKILL(1).md` through `SKILL(14).md`, `raw sources/gsd-advisor-researcher.md`, `raw sources/gsd-assumptions-analyzer.md`

## Corpus Events
- 2026-04-20 — [[Codex Skill Corpus Sync — 2026-04-20]] — Codex ran `rsync --ignore-existing` and now holds a superset of Claude's 84 skills plus `peer-channel` and `ingest`.
- 2026-04-23 — [[Ask Vault — EMERAULD Vault Briefing Skill]] — local read-only retrieval skill added at `/home/cerebrhoe/.codex/skills/ask-vault/`; routes questions across `session-state.md`, `memory.md`, `wiki/`, and `scripts/vsearch.py`.

## Related

- [[HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)]]
- [[MASTERxMASTERxMASTER — Skill Corpus Map]]
- [[Skill-Pairing — Five-Case Test Suite]]
- [[claude-mem — Persistent Memory Compression for Claude Code]]
- [[README]]
