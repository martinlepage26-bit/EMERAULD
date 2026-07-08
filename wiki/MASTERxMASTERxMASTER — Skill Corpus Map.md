---
type: map
title: MASTERxMASTERxMASTER — Skill Corpus Map
aliases:
- MASTERxMASTERxMASTER
- skill corpus
- MASTER PACK skills
- wiki/MASTERxMASTERxMASTER — Skill Corpus Map
tags:
- index
- map
- skills
- pharos
- governance
- hephaistos
- wiki
- masterxmasterxmaster-skill-corpus-map-md
- const
- skill
- letters
- pack
- masterxmasterxmaster
- color-purple
status: active
created: '2026-04-16'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/MASTERxMASTERxMASTER — Skill Corpus Map.md
backlink_count: 17
backlinks:
- '[[Areas/Writing/AI Society Manuscript — From AI Anxiety to Recursive Governance]]'
- '[[wiki/APEX Papers — Research Archive Map]]'
- '[[wiki/Archive Rebuild Normalized Tracker — MASTER PACK and HEPHAISTOS]]'
- '[[Areas/PHAROS/Claude Code Skill Corpus]]'
- '[[archive/wiki-2026-07-08/Codex Skill Corpus Sync — 2026-04-20]]'
- '[[Areas/PHAROS/HEPHAISTOS Agent Architecture]]'
- '[[wiki/MASTER PACK — D Drive Archive Map]]'
- '[[wiki/Martin Lepage Professional Identity]]'
- '[[wiki/Martin Lepage — Adjacent Skill Ring]]'
- '[[wiki/PHAROS Cross-AI Strategy Matrix]]'
- '[[wiki/PHAROS Skill Corpus Change Genealogy — 2026-05-06]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[wiki/RECURSO — Recursive Governance Test Archive]]'
- '[[wiki/Skill Corpus Genealogy Delta — 2026-05-06]]'
- '[[wiki/Skill Development Workflow — TDD, Dual-Layer, and Eval-Iterate]]'
- '[[Areas/PHAROS/Skill Ecosystem — Professional Capability Registry]]'
- '[[wiki/Skill-Pairing — Five-Case Test Suite]]'
---

# MASTERxMASTERxMASTER — Skill Corpus Map

## Summary

MASTERxMASTERxMASTER is the primary skill corpus directory within the [[MASTER PACK — D Drive Archive Map]], located at `/mnt/d/MASTER PACK/MASTERxMASTERxMASTER/`. It contains 15 named skill directories, each containing a `SKILL.md` entrypoint plus supporting agents, references, scripts, and examples. A duplicate copy of the corpus (minus `triangulate` and with the addition of `diamond-eyes`, `ma-arts-letters`, and `skill-architect`) is archived at `/mnt/d/MASTER PACK/AI Const + Voice - SKILLS/SKILLS/`. These skills form the operational backbone of the [[HEPHAISTOS]] three-agent governance system and are invokable via the Claude Code Skill tool.

## Context

Skills in this corpus are used by [[HEPHAISTOS]], [[PHAROS]], and related research workflows. The `recursive-governance-method` skill is the methodological engine for the [[RECURSO — Recursive Governance Test Archive]] runs and the [[AI Society Manuscript — From AI Anxiety to Recursive Governance]] development. Several skills (`fully-rounded-power-analyst`, `philosopher`) are named interpretive authorities in the AGENTS.md governance dispatch stack. The corpus also includes production and publication-facing skills (`peer-reviewed-paper-writer`, `publisher`, `novelist`) used in manuscript development.

## Skill Inventory

### Core Governance and Analysis

| Skill | Description |
|---|---|
| `fully-rounded-power-analyst` | Maps actors, incentives, constraints, and multidimensional power to explain how power moves through events, institutions, policies, and conflicts. Named interpretive authority in the AGENTS.md routing stack. |
| `recursive-governance-method` | Runs recursive data analysis over mixed archives: separates source from generated layers, builds evidence hierarchies, detects method lock or governance drift, produces bounded findings, and drafts AI authorship disclosure language. Source: [[Recursive Deterministic AI Governance — Method and Paper]]. |
| `philosopher` | Interpretive and philosophical analysis co-equal with `fully-rounded-power-analyst` in the governance authority stack. Handles values, contradiction analysis, and deep conceptual reasoning. |
| `trace-investigator` | Traces how authority, accountability, definitions, exceptions, and monitoring signals move across a document pack; separates direct evidence from inference and speculation. |
| `red-team` | Plans, scopes, leads, and reports authorized red team exercises with rules of engagement, risk controls, adversary emulation, and executive-ready findings. |

### Research and Academic Writing

| Skill | Description |
|---|---|
| `peer-reviewed-paper-writer` | Helps plan, draft, revise, and quality-check scholarly manuscripts for peer-reviewed publication; covers abstracts, introductions, methods, results, discussion, reviewer responses, and cover letters. |
| `qualitative` | Compares, selects, and applies qualitative research methods (thematic analysis, phenomenology, ethnography, narrative inquiry, discourse analysis, autoethnography, etc.) for study design, coding, and synthesis. |
| `triangulation` | Explains and solves angle-based location problems using the Law of Sines; also used for methodological triangulation in research contexts. |
| `triangulate` | Compatibility alias for `triangulation`; use for workflows that reference the older name. |

### Writing, Voice, and Publication

| Skill | Description |
|---|---|
| `novelist` | Plans, drafts, revises, and critiques novels across concept, outline, draft, revision, and positioning modes; attends to character psychology, plot momentum, scene design, POV, voice, and dialogue. |
| `peer-reviewed-paper-writer` | (see Research above) |
| `publisher` | Evaluates, positions, and packages manuscripts for publication; combines editorial judgment with publishing strategy, jacket copy, metadata, cover briefs, and handoffs between editorial, design, and production. |
| `speech` | Generates text-to-speech narration, voiceover, accessibility reads, and audio prompts via the OpenAI Audio API; runs the bundled `scripts/text_to_speech.py` CLI. |
| `humanize` | Redrafts compliance, ethics, governance, and regulatory rules for real human behavior; applies behavioral-science lenses (RADAR, COM-B, TDF, MSI) and adapts rules for different cultures and power structures. |

### System and Brand Design

| Skill | Description |
|---|---|
| `brand-identity-system` | Analyzes and develops brand identity systems, logo direction, typography, color systems, and website visual direction for consultancies, research groups, and professional-services firms. |
| `skill-pairing` | Sequences two Codex skills for one user request, carrying the output of the first into the second; used for tasks that split into two distinct domain stages. |
| `skill-architect` | Designs, builds, audits, and restructures SKILL.md files using dual-layer architecture (execution logic + knowledge map); also available in the AI Const + Voice Skills archive. |

### Additional Skills (AI Const + Voice - SKILLS archive only)

| Skill | Description |
|---|---|
| `diamond-eyes` | Aesthetic refinement for prose, prompts, brand language, interface copy, and designed artifacts — increases cut, clarity, proportion, and emotional pull without cosmetic smoothing. See [[Diamond-Eyes — Aesthetic Refinement Skill]]. |
| `ma-arts-letters` | The intellectual formation layer underlying `philosopher`; covers hermeneutics, close reading, interpretive rigor, canon literacy, and humanities formation from an MA in Arts and Letters context. |

## File Structure

Each skill directory contains at minimum:
- `SKILL.md` — primary entrypoint with YAML frontmatter (`name`, `description`) and execution logic
- `agents/` — sub-agent definitions (where applicable)
- `references/` — supporting reference materials, templates, and method rules
- `scripts/` — CLI tools and automation scripts (where applicable)
- `examples/` — sample outputs and worked examples (where applicable)
- `assets/` — font guides, templates, and design references (where applicable)

## Sources

- Primary location: `/mnt/d/MASTER PACK/MASTERxMASTERxMASTER/`
- Secondary archive: `/mnt/d/MASTER PACK/AI Const + Voice - SKILLS/SKILLS/`
- Also includes: `CODEX FINAL TRUE.txt`, `RDAIG_governance_test_2026-03-14.md`, `RDAIG_method_editorial_consolidation_2026-03-14.md`, and several supporting `.txt` files in the root

## Related

- [[MASTER PACK — D Drive Archive Map]]
- [[HEPHAISTOS]]
- [[Diamond-Eyes — Aesthetic Refinement Skill]]
- [[Claude Code Skill Corpus]]
- [[Recursive Governance Method — Skill Corpus Entry]]
- [[RECURSO — Recursive Governance Test Archive]]
- [[AI Society Manuscript — From AI Anxiety to Recursive Governance]]
