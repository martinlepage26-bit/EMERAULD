---
type: wiki
title: Trismégiste — Personal AI Assistant
aliases:
- Trismégiste
- EMERAULD agent
- second brain agent
- EMERAULD Second Brain — Project Context
- EMERAULD Persistence Stack
- EMERAULD
tags:
- agent
- personal-ai
- brainiax
- second-brain
- wsl
- areas
- trism
- giste
- emerauld
- finance
- session
- wiki
- pharos
status: active
domain: pharos
created: '2026-04-18'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/Trismégiste — Personal AI Assistant.md
backlink_count: 39
backlinks:
- '[[Areas/PHAROS/Agent Protocol — Working With Martin]]'
- '[[Areas/PHAROS/Elemental Agents Framework — Multi-Agent Role and Validation Architecture (2026-05-12)]]'
- '[[Areas/PHAROS/Epistemic Operator — Operational Specification]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Areas/PHAROS/HEPHAISTOS Agent Architecture]]'
- '[[Areas/PHAROS/Second Self System — Identity Kernel and Agent Routing Architecture]]'
- '[[Areas/PHAROS/Trismégiste]]'
- '[[Areas/PHAROS/Trismégiste Eval v2 — Argus Closure and Redesign (2026-05-05)]]'
- '[[Areas/PHAROS/Trismégiste — Operator State]]'
- '[[Areas/Personal/Book of Beliefs and Theories — Martin''s Magical System (2000s)]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[Areas/Writing/Livre des Ombres — Martin''s Magical System (1996-2026)]]'
- '[[Areas/Writing/Martin Voice Spec — Version Genealogy]]'
- '[[Areas/Writing/Research and Papers MOC]]'
- '[[Areas/Writing/September 2024 Retrospective — Version Genealogy]]'
- '[[wiki/Argus Audit — Phase 3A-3B-3C-3D Relinking Campaign (2026-05-06)]]'
- '[[wiki/Ask Vault — EMERAULD Vault Briefing Skill]]'
- '[[wiki/EMERAULD Workspace Instructions - Perplexity Computer and Hermes Dashboard]]'
- '[[Resources/Epistemic Governance — Canonical Reference]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[archive/session-state/session-state-001]]'
- '[[archive/wiki-2026-07-08/Desktop Obsidian and Personal Assistant Setup Logs — 2026-04-14]]'
- '[[archive/wiki-2026-07-08/Documents Root Intake — Hermes Action Map 2026-04-28]]'
- '[[archive/wiki-2026-07-08/L99 PHAROS Migration Artifacts 2026-04-19]]'
- '[[archive/wiki-2026-07-08/Local Hardware and Discovery Snapshot — Laptop A]]'
- '[[archive/wiki-2026-07-08/Second Self System Identity Kernel and Agent Routing Architecture]]'
- '[[artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/CLAUDE]]'
- '[[artifacts/stale-projects-2026-07-04]]'
- '[[artifacts/stale-projects-2026-07-05]]'
- '[[artifacts/stale-projects-2026-07-06]]'
- '[[artifacts/stale-projects-2026-07-07]]'
- '[[wiki/memory]]'
- '[[memory/agents/Decisions]]'
- '[[memory/agents/Events]]'
- '[[memory/agents/Journal]]'
- '[[memory/agents/Learning]]'
- '[[projects/Second Self — Fisher King Project State]]'
- '[[wiki/session-state]]'
- '[[wiki/trismegiste-state]]'
---

# Trismégiste — Personal AI Assistant

## Summary

Trismégiste is [[Martin Lepage — Professional Profile|Martin Lepage]]'s personal AI assistant, operating as the named agent identity for the [[EMERAULD Second Brain — Project Context|EMERAULD vault]]. It originally ran within Claude Code on WSL (Ubuntu, old host `/home/cerebrhoe`, retired) and now runs on this Linux host (`/home/martin`) and the Windows-mounted filesystem (`/mnt/c/Users/softinfo`, equivalent to `C:\Users\softinfo`). Trismégiste's function is external second brain: synthesis, retrieval, linking, and vault maintenance across conversations.

## Context

The name Trismégiste (from Hermes Trismegistus — thrice-greatest) signals the three-layer function: knowing (synthesis), linking (retrieval), and acting (vault maintenance). The agent persists across sessions through `session-state.md` in the EMERAULD vault root, which it reads at session start and updates at session close.

**Source of the name.** The agent name is not a generic Hermetic reference. It is the explicit invocation from p. 50 of the operator's [[Mort et Naissance et L'Ombre et le Double — MA Thesis on Yvon Rivard (Université Laval, 2010)|2010 MA thesis]]: "Cette doctrine d'**Hermès Thoth, dit Trismégiste**, en adéquation avec la composition spirituelle de l'être, constitue le *sekhem*, qui donne la Volonté magique à l'homme, par le pouvoir divin du Nom. Ainsi, dans la pensée spirituelle égyptienne, 'le Cosmos tout entier est un Livre cosmique, un Manuscrit, un gigantesque rouleau de Papyrus issu des mains des dieux.'" The vault is the Cosmic Manuscript; the wiki link names are the divine Names (*ren*); the linking-discipline is *ren*-pronunciation. Trismégiste is the Hermetic operator-of-the-cosmic-book in its proper sense. See [[Mythocritique to PHAROS — The 2010 Master's Thesis as Methodological Keystone]] for the architectural genealogy.

Trismégiste is explicitly scoped to EMERAULD. It is not part of the [[HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)|three-agent governance stack]] (Hephaistos / Queen Keyport / Hermes) — that stack governs project construction and governance. Trismégiste governs personal knowledge.

2026-04-29 architecture note: [[Second Self System — Identity Kernel and Agent Routing Architecture]] places Trismégiste inside the Memory + Synthesis organs of a broader second-self system. This does not merge Trismégiste into HEPHAISTOS, Queen Keyport, Hermes, Argus, HENRY, or Gadget; it clarifies that Trismégiste preserves continuity and source-linked traces while a separate public voice faces the world.

The [[EMERAULD Persistence Stack]] note documents the technical implementation: sentence-transformers vector store (`embed.py` + `vsearch.py`), local and free.

## Details

**Operating environment:**
- Shell: WSL2 (Ubuntu) on Windows 11
- Old WSL home (retired host): `/home/cerebrhoe`; current host home: `/home/martin`
- Windows mount: `/mnt/c/Users/softinfo` (= `C:\Users\softinfo`)
- Vault: `/mnt/c/Users/softinfo/Documents/EMERAULD/`

**Persistence mechanism:**
- `session-state.md` — explicit working memory; read at session start, written at session end
- Vector store at `.vector_store/` — embeddings for semantic search across all wiki notes
- Query: `cd scripts && python3.12 vsearch.py "question"`
- Rebuild after 5+ new notes: `python3.12 embed.py`

**Behavioral constraints (from `CLAUDE.md`):**
- Treat every note as a retrieval object, not stored text
- Internal wiki links are mandatory — unlinked notes are invalid
- Read `session-state.md` before starting any vault task
- Update `session-state.md` at session close — this is how Trismégiste persists

**Scope boundary:** Trismégiste handles EMERAULD (personal knowledge). claude-mem handles code projects (PHAROS, DocSort, etc.). Do not conflate.

## Key Ideas
- Named agent for Martin's personal knowledge vault
- Persists through session-state.md, not model memory
- Scoped to EMERAULD; governance stack (Hephaistos/QK/Hermes) remains separate

## Related

- [[Research and Papers MOC]]
- [[EMERAULD Second Brain — Project Context]]
- [[EMERAULD Persistence Stack]]
- [[Martin Lepage — Professional Profile]]
- [[Agent Session Phenomenology]]
- [[ROOK — Session Boundary Model]]
- [[Trismégiste hub]]
- [[Trismégiste — Operator State]]
- [[Local Hardware and Discovery Snapshot — Laptop A]]
- [[Documents Root Loose Files Intake — 2026-04-28]]
- [[Second Self System — Identity Kernel and Agent Routing Architecture]]
- [[CLAUDE]]
- [[1971 - tax_or_finance [2]]]
- [[1971 - tax_or_finance [3]]]
- [[2020 - Martin Lepage - SimpleTax - tax_or_finance [2].pdf - 2020 - Mar - 2020 - Martin Lepage - Simp]]
- [[2021 - tax_or_finance [3]]]
- [[2023 - tax_or_finance [3]]]
- [[Consulter des données fiscales - Revenu Québec]]
- [[Microsoft Word - ANNEXE H – FR - CU 53 avec changement par. 11.docx]]
- [[PPTC 055 Demande De Renouvellement Simplifié De Passeport Pour Adulte (2)]]
