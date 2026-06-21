---
type: raw-source
source: `~/.claude/skills/writing-skills/SKILL.md` (TDD frame), `~/.codex/skills/skill-architect/SKILL.md` (Brain+Map), `~/.claude/skills/skill-development/SKILL.md` (eval/iterate loop)
captured: 2026-04-30
status: captured
tags: [workflow, skill-development, skill-architect, writing-skills, tdd, dual-layer, claude-code, codex, anthropic-best-practices]
---

# Skill Development Workflow — Raw Capture

## Provenance

Three skills converge on the same workflow under different names:

- **`writing-skills`** (Claude side, `~/.claude/skills/writing-skills/SKILL.md`) — frames skill creation as **TDD applied to process documentation**: write a pressure scenario with a subagent, watch it fail without the skill (RED), write the skill (GREEN), then refactor to close loopholes. "If you didn't watch an agent fail without the skill, you don't know if the skill teaches the right thing." Requires `superpowers:test-driven-development` as background. Cross-references `anthropic-best-practices.md` for official skill authoring guidance.
- **`skill-architect`** (Codex side, `~/.codex/skills/skill-architect/SKILL.md`) — frames skill creation as **Brain + Map**: the Brain controls how the model thinks (persona, ordered logic, refusals, output format, examples); the Map controls what the skill can load and use (knowledge paths, tool orchestration, memory, token pruning, mode locks). Operates in three modes: build, audit, standalone combinatorial.
- **`skill-development`** / **`skill-creator`** (Claude side, `~/.claude/skills/skill-development/SKILL.md`) — frames skill creation as an **eval/iterate loop**: draft, test prompts, evaluate qualitatively + quantitatively, rewrite, repeat. Includes a description-improver script for trigger-quality optimization.

## The dual-layer architecture (skill-architect's verbatim model)

| Layer | Controls | Failures it explains |
|---|---|---|
| **Brain** | Persona, ordered execution logic, refusals, output format, examples | Chatty/poor scope; wrong output structure |
| **Map** | Knowledge retrieval (paths), tool orchestration, memory, token pruning, mode locks | Hallucinated facts; repeated manual calculation; context rot |
| **Metadata** | Frontmatter `description` field | Trigger misses, false positives |

The Brain answers: *given perfect information, how should the skill behave?*  
The Map answers: *what does the skill need access to in order to execute correctly?*

## The TDD mapping (writing-skills's verbatim model)

| TDD concept | Skill-creation analogue |
|---|---|
| Test case | Pressure scenario with a subagent |
| Production code | The SKILL.md |
| RED | Agent violates the rule without the skill loaded |
| GREEN | Agent complies with the skill loaded |
| Refactor | Close loopholes while keeping compliance |
| Write test first | Run baseline before writing the skill |
| Watch it fail | Document the exact rationalizations the agent uses |

A skill is a **reusable reference for proven techniques**. A skill is *not* "a narrative about how you solved a problem once."

## The eval/iterate loop (skill-development's verbatim model)

1. Decide what the skill should do and roughly how.
2. Draft the skill.
3. Create a few test prompts; run claude-with-access-to-the-skill on them.
4. Evaluate results qualitatively and quantitatively (`eval-viewer/generate_review.py`).
5. Rewrite based on feedback + quantitative flaws.
6. Repeat until satisfied.
7. Expand the test set; try again at larger scale.
8. Run the description-improver to optimize triggering.

## Combinatorial mode (skill-architect's standalone case)

When `skill-architect` is invoked without a target, default to skill suggestion + synergy. Inventory existing skills, identify whether the task needs one skill, an `N ≥ 2` stack, or a macro-skill, and prefer hierarchical composition (e.g., `(research-ingestion → literature-review) → drafting → peer-review-workflow`). If the same stack will likely recur, propose a macro-skill rather than an ad-hoc chain. The dual-layer preview format is required for every proposed combination.

## What this means for the operator's vault

- The skill ecosystem is governed by *three converging skills* on **both surfaces** (Claude + Codex). They are not redundant; each emphasizes a different axis (test discipline / structural separation / eval loop).
- New skills the operator authors should:
  - have a Brain and a Map,
  - have a baseline failure documented before the skill is written,
  - go through at least one eval/iterate cycle before being declared stable.
- This is the meta-workflow that produced [[Diamond-Eyes — Aesthetic Refinement Skill]], [[Ask Vault — EMERAULD Vault Briefing Skill]], [[Operator-Check Skill — Burnout Cascade Interrupt]], and the wider [[Claude Code Skill Corpus]].

## Status

Raw. To be synthesized into wiki note `Skill Development Workflow — TDD, Dual-Layer, and Eval-Iterate`.
