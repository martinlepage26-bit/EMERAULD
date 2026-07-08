---
type: wiki
title: Skill Development Workflow — TDD, Dual-Layer, and Eval-Iterate
aliases:
- Skill development workflow
- TDD for skills
- Brain and Map
- Skill creation pipeline
- wiki/Skill Development Workflow — TDD, Dual-Layer, and Eval-Iterate
tags:
- workflow
- skill-development
- skill-architect
- writing-skills
- tdd
- dual-layer
- claude-code
- codex
- meta-workflow
- wiki
- skill-development-workflow-tdd-dual-layer-and-eval-iterate-md
- skill
- iterate
- brain
- axis
- eval
- color-orange
status: active
created: '2026-04-30'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Skill Development Workflow — TDD, Dual-Layer, and Eval-Iterate.md
backlink_count: 16
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[wiki/Agatha Unified Skill System — Eight Sovereign Operators]]'
- '[[wiki/Anti-Charm]]'
- '[[wiki/Ask Vault — EMERAULD Vault Briefing Skill]]'
- '[[wiki/Codex Skills Inventory — Complete Registry (241 Skills)]]'
- '[[wiki/GSD Tier 1 — Core Workflow Skills Hub]]'
- '[[wiki/Kickstart App Prompt — Template and Synthesis Framework]]'
- '[[wiki/Martin Lepage — Adjacent Skill Ring]]'
- '[[wiki/Martin Lepage — Authored Skills]]'
- '[[wiki/Martin Lepage — Skills by Life Domain]]'
- '[[wiki/Personal and Projects MOC]]'
- '[[wiki/Skill Domain — Skill Architecture]]'
- '[[Areas/PHAROS/Skill Ecosystem — Professional Capability Registry]]'
- '[[wiki/Vault Graph Hygiene — Content Title Normalization Skill]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[wiki/skills/skill-architect]]'
---

# Skill Development Workflow — TDD, Dual-Layer, and Eval-Iterate

## Summary
The operator's skill ecosystem is governed by three converging skills — `writing-skills` (TDD), `skill-architect` (Brain + Map), and `skill-development` / `skill-creator` (eval/iterate). They are not redundant; each names a different axis of the same workflow. A skill is a **reusable reference for a proven technique**, never "a narrative about how I solved this once." This note is the meta-workflow note that connects [[Claude Code Skill Corpus]], [[Codex Skill Corpus Sync — 2026-04-20]], [[MASTERxMASTERxMASTER — Skill Corpus Map]], and [[Skill-Pairing — Five-Case Test Suite]] into one disciplined process. Raw capture: `raw sources/2026-04-30_skill-development-tdd-and-dual-layer-architecture.md`.

## Context
The vault already inventories the operator's skill corpus (Claude side at [[Claude Code Skill Corpus]], Codex side at [[Codex Skill Corpus Sync — 2026-04-20]]) and documents specific completed skills like [[Diamond-Eyes — Aesthetic Refinement Skill]] and [[Ask Vault — EMERAULD Vault Briefing Skill]]. What the vault has not yet held in one place is **how skills are produced** — the discipline shared across both surfaces. This note fills that gap and connects to [[HEPHAISTOS Agent Architecture]] (skills as the composable layer of the three-agent stack) and to [[Posture vs Execution Drift — The Practice of Refusal]] (the discipline of refusing premature skill creation).

## Details

### Three converging skills, one workflow

| Skill | Surface | Frame | Core question it answers |
|---|---|---|---|
| `writing-skills` | Claude (`~/.claude/skills/`) | TDD applied to process documentation | Does the skill teach the right thing? |
| `skill-architect` | Codex (`~/.codex/skills/`) | Brain + Map dual-layer | Is the skill structured so it can execute? |
| `skill-development` / `skill-creator` | Claude | Draft → eval → iterate | Does the skill perform under measurement? |

Each skill emphasizes a different axis. Together they form one workflow: **structure the skill correctly (architect), prove it teaches the right behavior (TDD), refine it under evaluation (iterate)**.

### Dual-layer architecture (the structural axis)

A SKILL.md has two layers and a metadata header.

- **Brain** — how the model thinks. Persona; ordered execution logic; negative constraints / refusals; output format; few-shot examples when output is non-trivial. Brain answers: *given perfect information, how should the skill behave?*
- **Map** — what the skill can reach. Knowledge retrieval with exact paths; tool orchestration for deterministic operations; memory and handoff rules; token pruning / progressive disclosure; mode locks. Map answers: *what does the skill need access to in order to execute correctly?*
- **Metadata** — frontmatter `description` field. Drives trigger accuracy. Underspecified description = misfires + false positives.

Diagnostic mapping for failures:

| Symptom | Likely cause | Layer |
|---|---|---|
| Hallucinated facts | No exact path or source-loading rule | Map |
| Chatty / poorly scoped behavior | Missing refusals or unclear goal | Brain |
| Wrong output structure | No explicit output format / examples | Brain |
| Repeated manual calculations | Deterministic step left in prose | Map |
| Trigger misses or false positives | Weak frontmatter description | Metadata |
| Context rot in long workflows | No token pruning / handoff discipline | Map |

### TDD discipline (the proof axis)

A skill that has not been **watched failing without itself loaded** is unverified.

| TDD concept | Skill analogue |
|---|---|
| Test case | Pressure scenario with a subagent |
| Production code | The SKILL.md |
| RED | Agent violates the rule without the skill loaded |
| GREEN | Agent complies with the skill loaded |
| Refactor | Close loopholes while keeping compliance |
| Write test first | Run baseline before writing the skill |
| Watch it fail | Document the exact rationalizations the agent uses |

This is also the doctrine behind [[Diamond-Eyes — Aesthetic Refinement Skill]]: a gate that passes a thing through is only meaningful if the gate has been observed *catching* something.

### Eval-iterate loop (the refinement axis)

1. Decide intent and rough shape.
2. Draft the SKILL.md.
3. Create test prompts; run with the skill loaded.
4. Evaluate qualitatively and quantitatively (`eval-viewer/generate_review.py`).
5. Rewrite based on user feedback + measured flaws.
6. Repeat until satisfied.
7. Expand the test set; rerun at larger scale.
8. Run the description-improver to optimize triggering.

### Combinatorial mode (when more than one skill is needed)

`skill-architect` invoked without a target defaults to skill suggestion + synergy. Rules:

- Inventory the most relevant existing skills first (do not invent before searching).
- Decide between one skill, an `N ≥ 2` stack, or a dedicated macro-skill.
- Prefer **hierarchical composition** over flat lists, e.g., `(research-ingestion → literature-review) → drafting → peer-review-workflow`.
- If the same stack will likely recur, propose a macro-skill rather than ad-hoc chaining.
- Use the dual-layer preview format for every proposed combination.

This is the discipline that produced [[Skill-Pairing — Five-Case Test Suite]] and informs [[Agatha Unified Skill System — Eight Sovereign Operators]].

### What this means for the operator

Before authoring any new skill:

1. Search the corpus first ([[Claude Code Skill Corpus]] / [[Codex Skill Corpus Sync — 2026-04-20]]) — most "new skill" intuitions are existing skills.
2. Run the baseline scenario without the skill. Document the exact failures.
3. Draft the SKILL.md with both layers explicit. A Map without a Brain hallucinates; a Brain without a Map drifts.
4. Run at least one eval/iterate cycle. A skill that has never been measured is a draft, not a skill.
5. Before publishing, optimize the description for trigger accuracy. Bad triggers waste more tokens than bad bodies.

The same discipline applied in reverse is **refusal**: if a skill cannot be specified along all three axes (structure, proof, evaluation), it is premature. Defer it. See [[Posture vs Execution Drift — The Practice of Refusal]] and [[The Lost-Loop Pattern — Avoidance Through System-Building]] for why "more skills" is often a retreat from execution.

## Related
- [[Skill Ecosystem — Professional Capability Registry]] — Unified hub
- [[Martin Lepage — Authored Skills]] — signature authored set and retrieval point
- [[Claude Code Skill Corpus]]
- [[Codex Skill Corpus Sync — 2026-04-20]]
- [[MASTERxMASTERxMASTER — Skill Corpus Map]]
- [[Skill-Pairing — Five-Case Test Suite]]
- [[Diamond-Eyes — Aesthetic Refinement Skill]]
- [[Ask Vault — EMERAULD Vault Briefing Skill]]
- [[Operator-Check Skill — Burnout Cascade Interrupt]]
- [[Agatha Unified Skill System — Eight Sovereign Operators]]
- [[Posture vs Execution Drift — The Practice of Refusal]]
- [[HEPHAISTOS Agent Architecture]]
