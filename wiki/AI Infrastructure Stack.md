---
type: map
aliases:
  - TOPIC — AI Infrastructure Stack
tags: [index, map, topic, infrastructure, tooling, mcp, rag, agents]
created: 2026-04-18
updated: 2026-05-06
---

# AI Infrastructure Stack

All the technical infrastructure supporting Martin's research, writing, and governance work: operator surfaces, retrieval/memory systems, voice pipelines, MCP servers, and Codex/Claude CLI tooling.

This is the infrastructure branch of the PHAROS graph. It underpins [[HEPHAISTOS Agent Architecture]] and the wider governance method, while linking back up to [[Recursive Governance Theory]] and [[Governance and PHAROS MOC]].

Primary runtime cluster index: [[MCP and Runtime Integration MOC]].

---

## Stack Layers (Fast Map)

- **Operator surfaces**: [[Hermes Dashboard — Professional Governance Tool]] (desktop lane workbench), [[memory]] (vault-side business mirror), `wiki/` (durable notes), `raw sources/` (captures and provenance).
- **Assistant runtimes**: Codex CLI + Claude Code workflows (shared skill corpus topology; see [[Codex Skill Corpus Sync — 2026-04-20]] and [[Claude Code Skill Corpus]]).
- **Retrieval**: LightRAG + vault search (`rg`, `scripts/vsearch.py`) and multimodal extensions (see [[Ask Vault — EMERAULD Vault Briefing Skill]]).
- **Coordination**: MCP servers + peer messaging + session boundary model (InfraFabric bundle, peers, ROOK).
- **Media**: local TTS/voice pipeline + paper-writing system.

---

## Knowledge Graph and Retrieval

- [[LightRAG — Graph-Based RAG System]] — Graph-based RAG powering EMERAULD. Snapshot (2026-04-18): KV store 188 docs; graph 217 nodes / 185 edges; embeddings all-MiniLM-L6-v2 (local); LLM via OpenRouter (meta-llama/llama-3.2-3b-instruct:free). Status: partial — free quota exhausted, retry-with-backoff added.
- [[RAG-Anything — Multimodal RAG Framework]] — Extends LightRAG to multimodal inputs (PDFs, images, tables, audio, video).
- [[claude-mem — Persistent Memory Compression for Claude Code]] — MCP-based session memory compression for code projects. Local tool (not the EMERAULD vault memory layer).
- [[EMERGENT HELIX Session — Truth Claims, Ingestion, and Booby-Trap Diagnostics (2026-05-07)]] — Compact transcript artifact showing HELIX truth-claim pressure + “ingestion” semantics under adversarial pivots; a replayable infrastructure test case.
- [[Vault Deep Linking Pass — 2026-05-06]] — Conservative graph-maintenance pass over low-inbound wiki notes; links current scan records, Argus audit output, and client/design notes into MOCs and TOPIC hubs.
- [[Root Loose Notes Cluster Map — 2026-05-06]] — Semantic repair layer for root-level graph outliers; distinguishes HELIX evidence, commercial scratchpads, writing raw lists, infrastructure checklists, RIA provenance, and empty stubs.
- [[Vault Cluster Discovery and Linking Opportunities — 2026-05-01]] — Earlier cluster-discovery roadmap for the vault graph; use with [[Vault Linking Gaps & Bridge Opportunities — 2026-05-01]] and the two session summaries for provenance on the relinking campaign.
- [[Vault Linking Session Summary — 2026-05-01]], [[Vault Linking Session 2 Summary — 2026-05-01]], and [[Vault Linking Scan — 2026-05-01, 15-XX (Loop Iteration 1)]] — Session-level summaries and scan output from the May 1 vault linking campaign.
- [[Desktop Text Intake — 2026-05-06]] — Desktop `.md`/`.txt` scan promoted beyond raw copy into duplicate detection, synthesis notes, and review queue.

---

## Codex / Claude CLI Tooling

- [[AI Platform Dependence — Anthropic OpenClaw and Commoditization Pressure]] — Platform-strategy note on Anthropic/OpenClaw access, provider abstraction, open-weight commoditization pressure, and why agent workflows need provider-agnostic infrastructure.
- [[Ask Vault — EMERAULD Vault Briefing Skill]] — Read-only EMERAULD vault briefing skill that routes questions across `session-state.md`, `memory.md`, `wiki/`, and local vector search.
- [[Claude Code Skill Corpus]] — Registry of all skills in the HEPHAISTOS corpus.
- [[Codex Skill Corpus Sync — 2026-04-20]] — Codex became a superset of the Claude skill corpus via additive sync; governance purity is no longer structural.
- [[GSD — Get-Shit-Done Claude Code System]] — Context-rot mitigation via meta-prompting and spec-driven development. v1.36.0. Path: `~/GSD/`.
- [[CLI-Anything — Agent Harness for Tool Integration]] — Agent harness for arbitrary tool integration into Claude Code sessions.
- [[Diamond-Eyes — Aesthetic Refinement Skill]] — Aesthetic refinement and governance gate skill.
- [[Obsidian Agent Vault Launch — Commercial Skill]] — Skill for launching lightweight agent-memory products.
- [[Desktop Obsidian and Personal Assistant Setup Logs — 2026-04-14]] — Desktop setup traces showing the Windows Obsidian app, WSL runtime, Markdown vault, and LightRAG/service layers as distinct parts of the assistant stack.

---

## MCP and Agent Coordination

- [[InfraFabric MCP Stack — Remote Bundles]] — Four MCP servers: if_context (SSH, context storage), if_blackboard (SSH, shared state), openspace (skill bridge), if_chat (ROOK room communication). Bundle at `~/remote-bundles/`.
- [[claude-peers-mcp — Claude Peer Network]] — Real-time messaging between parallel Claude Code sessions. Peer discovery and ambient awareness.
- [[ROOK — Session Boundary Model]] — Infrastructure harness: session lifecycle, headroom tracking, tool tiers, communication rooms.
- [[InfraFabric Architecture]] — Modular AI governance and infrastructure platform. Module map: if.switchboard, if.bus, if.blackboard, if.trace, if.context, if.knowledge, if.api, if.gov.

---

## Voice and Media Production

- [[voice11 — ElevenLabs TTS Pipeline]] — Local Python TTS pipeline. British accent rendering, reference voice cloning, drag-and-drop batch processing. Path: `~/voice11/`.
- [[HENRY — Research Paper Writing System]] — Note-to-paper pipeline with voice synthesis capabilities. Path: `~/HENRY/`. Includes `henry_voice_optimizer.py`.

---

## Development and Context Management

- [[ChatGPT Apps SDK — Planning, Metadata, Deployment, and Operations]] — Working note from a pasted Apps SDK docs pack; use for app scoping, metadata tuning, deployment, security, and troubleshooting.
- [[PROTOCOLS — Debate and Red-Team Runbook]] — Five-lane review process for governance and security.
- [[Red Team Handbook — Offensive Security Reference]] — Offensive security reference. AI/LLM red-team techniques including Co-RedTeam and BlackIce.
- [[Awesome Design Resources — Curated UI-UX Reference List]] — Design reference stack for interface work across PHAROS, Martin public surfaces, and client/product UI.

---

## Skill Architecture

- [[Agatha Unified Skill System — Eight Sovereign Operators]] — Eight sovereign operator skills designed with Agatha. Each skill is self-contained; no dependency chains.
- [[Operator-Check Skill — Burnout Cascade Interrupt]] — Burnout cascade detection and interruption skill.
- [[Recursive Governance Protocol — Theseus, Auryn, Hopf]] — HELIX operator: Chrome automation skill for stress-testing LLMs.
- [[HELIX Desktop Corpus — Protocol Evolution and Stress-Test Runs (2026-05-06)]] — Desktop capture of HELIX code/protocol evolution, live transcripts, and Chain-of-Scrutiny / ASE implementation material.
- [[HELIX Comparison Matrix — v2.6 vs External Evaluators (2026-05-06)]] — Comparison matrix showing how HELIX differs from Garak, PyRIT, Promptfoo, Giskard/DeepTeam, Epistemic Blinding, and observability stacks.
- [[Archive Rebuild Normalized Tracker — MASTER PACK and HEPHAISTOS]] — HTML tracker intake documenting archive-rebuild confidence, file-role interpretation, and manual-review boundaries between MASTER PACK and rebuilt HEPHAISTOS artifacts.
- [[Möbius Protocol — AI Self-Polygraph Template]] — AI self-evaluation template.
- [[Skill Development Workflow — TDD, Dual-Layer, and Eval-Iterate]] — Meta-workflow shared across `writing-skills` (TDD), `skill-architect` (Brain + Map), and `skill-development` (eval/iterate); the discipline that produces a skill, not a single skill.
- [[InfraFabric Codex Alignment — System-Shaper Frame]] — Operator-side adoption diagnostic for InfraFabric surfaces (`if.context`, `if.blackboard`, `if.bus`, graph, trace) — surfaces earn their place by mapping to existing operator behavior.
- [[CODEX HANDOFF — 2026-05-03 Trismégiste Keystone Cycle]] — Handoff record tying Codex continuity work back into the Trismégiste/vault infrastructure layer.

---

## Infrastructure Status (Snapshot)

This table is a *snapshot* for operational orientation, not a claim that every system is currently running in every session. Prefer verifying locally (tooling state can drift).

### Snapshot (2026-04-18)

| System | Status | Issue |
|---|---|---|
| LightRAG | Partial | OpenRouter free quota exhausted (402 errors) |
| Hermes Dashboard | Local | Operator tool (desktop surface) |
| claude-peers-mcp | Active | Peer messaging available when configured/running |
| InfraFabric MCP (if_context) | SSH-dependent | Drops silently if tunnel fails |
| InfraFabric MCP (if_chat) | Active | ROOK room communication |
| openspace MCP | Active | Skill bridge running |
| voice11 | Local | No known issues |
| HENRY | Local | No known issues |
| GSD | Local | No known issues |

---

## Open Gaps

- LightRAG needs funded OpenRouter account to clear 402 errors
- OpenRouter API key exposure is a historical incident; rotation was closed on 2026-04-20 and should not be treated as an active open task here
- CODEX-HERMES Control Surface (9-dir Node dashboard) has no wiki note
- dr-sort (2.7G academic doc sorter) has no wiki note
- astrology-gaialogy (69M) has no wiki note

---

## Related

- [[Research and Papers MOC]]
- [[HEPHAISTOS Agent Architecture]] — Agents that run on this infrastructure
- [[Recursive Governance Theory]] — Governance method this infrastructure carries
- [[AI Identity and Phenomenology]] — Identity continuity across sessions on this stack
- [[Structural Analogy & Governance Systemic Parallels Between Biological, Epistemic, and Computational Memory Architectures]] — Crosswalk for model weights, prompts, retrieval, and runtime as governed memory architecture.
- [[Obsidian Second Brain Product]] — Vault as the memory/knowledge surface for agents
- [[Personal and Projects MOC]]
- [[Governance and PHAROS MOC]]
