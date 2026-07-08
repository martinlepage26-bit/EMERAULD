---
type: wiki
title: Skill-Pairing — Five-Case Test Suite
aliases:
- skill-pairing tests
- skill-pairing behavioral suite
- pairing compliance tests
tags:
- skills
- claude-code
- testing
- skill-pairing
- governance
- behavioral-compliance
- areas
- pairing
- skill
- pair
- stage
- handoff
- wiki
- pharos
status: active
domain: pharos
created: '2026-04-20'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/Skill-Pairing — Five-Case Test Suite.md
backlink_count: 18
backlinks:
- '[[Areas/PHAROS/Claude Code Skill Corpus]]'
- '[[Areas/PHAROS/DEEPER CONNECTIONS — The Triple Synthesis and the Governance Architecture]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Areas/PHAROS/Governance and Platform Signals Memo — 2026-05-14]]'
- '[[Areas/PHAROS/Governed Revision Loop — Responsible Self-Improving Agents]]'
- '[[Areas/PHAROS/Skill Development Workflow — TDD, Dual-Layer, and Eval-Iterate]]'
- '[[Areas/PHAROS/Skill Ecosystem — Professional Capability Registry]]'
- '[[Areas/PHAROS/Skill Map — Canonical Routed Skills (2026-05-06)]]'
- '[[wiki/Martin Lepage — Adjacent Skill Ring]]'
- '[[wiki/Martin Lepage — Authored Skills]]'
- '[[wiki/Martin Lepage — Skills by Life Domain]]'
- '[[wiki/Skill Domain — Skill Architecture]]'
- '[[archive/wiki-2026-07-08/Codex Skill Corpus Sync — 2026-04-20]]'
- '[[artifacts/stale-projects-2026-07-04]]'
- '[[artifacts/stale-projects-2026-07-05]]'
- '[[artifacts/stale-projects-2026-07-06]]'
- '[[artifacts/stale-projects-2026-07-07]]'
- '[[wiki/skills/skill-architect]]'
---

# Skill-Pairing — Five-Case Test Suite

## Summary

A five-case behavioral test suite for the `skill-pairing` skill, prioritizing protocol compliance (file-reading, handoff artifacts, uncertainty propagation, skill-ceiling enforcement) over output quality. Sourced from a Claude conversation on 2026-04-20 (`Clippings/Complete solutions, not compromises.md`). Ties the skill-pairing discipline into the broader [[Claude Code Skill Corpus]] and the [[MASTERxMASTERxMASTER — Skill Corpus Map|skill corpus map]].

## Context

`skill-pairing` is a meta-skill that composes two other skills in sequence with a formal handoff artifact between stages. This test suite exists because fluent output can mask protocol violations — a pair can produce beautiful prose while silently skipping the handoff artifact, over-pairing three skills into two, or quietly resolving an ambiguity that should have been propagated. The cases reach into several other skills in the corpus: `qualitative`, `peer-reviewed-paper-writer`, `novelist`, `trace-investigator`, `recursive-governance-method`, [[Diamond-Eyes — Aesthetic Refinement Skill|diamond-eyes]], and a hypothetical `data-viz`/`pptx` pair.

## Details

### Test 1 — Correct Pairing Selection and Full Execution
Prompt: stakeholder interview notes → `qualitative` → `peer-reviewed-paper-writer` → publication-ready abstract. **Pass criteria:** pair named before execution; both SKILL.md files actually read (not inferred from memory); Stage 1 output visibly distinct from Stage 2; handoff artifact (≤150 words) present between stages with summary, key outputs, constraints, open questions; Stage Summary at end; no silent resolution of Stage 1 uncertainties.

### Test 2 — Single-Skill Deflection
Prompt: "Use skill-pairing to help me write a blog post about AI governance." **Pass criteria:** no artificial pairing constructed; single skill (e.g., `novelist` or `peer-reviewed-paper-writer`) named and used; one-sentence explanation of why pairing was not warranted; output is a complete blog draft, not a framework.

### Test 3 — Missing-Skill Failure
Prompt: `data-viz` → `pptx` (where `data-viz` is not installed). **Pass criteria:** missing skill named explicitly; no improvised substitute offered as if it were the real skill; graceful offer to proceed with `pptx` alone if the user supplies the visualization; no fabricated Stage 1 output.

### Test 4 — Uncertainty Propagation
Prompt: `trace-investigator` on a deliberately ambiguous governance clause (delegation-or-exemption), then `recursive-governance-method` to build an evidence hierarchy. **Pass criteria:** Stage 1 names the ambiguous clause explicitly; handoff artifact carries the uncertainty as an open question; Stage 2 does not silently resolve it; final output acknowledges the interpretive limit. Directly relevant to [[Recursive Deterministic AI Governance — Method and Paper|recursive governance]] protocol discipline.

### Test 5 — Over-Pairing Rejection (Three Skills)
Prompt: `qualitative` → `peer-reviewed-paper-writer` → `diamond-eyes` (three stages). **Pass criteria:** all three skills named; no silent omission of the third; clear explanation of the two-skill ceiling; concrete recommendation for a two-step workflow (pair the first two, apply the third as a follow-up pass); does not simply refuse — routes the user forward.

### Grading Philosophy
Behavioral compliance outranks output quality. A response that produces high-quality prose but skips the handoff artifact — or names a skill without reading it — fails the test regardless of surface polish. This is the same discipline as the [[Recursive Deterministic AI Governance — Method and Paper|recursive governance method]]: form is cheap, protocol is load-bearing.

## Key Ideas

- **Protocol compliance as the primary grading axis.** This inverts the default AI-evaluation bias toward fluent output.
- **The handoff artifact is the artifact.** Without a discrete, bounded handoff (≤150 words, structured), the pair collapses into one blurry response.
- **Uncertainty must survive handoff.** A pair that resolves ambiguity silently between stages is worse than a single-skill response that flags the ambiguity.
- **Two-skill ceiling is a routing discipline.** Three-stage requests get routed to a sequential workflow, not a silent drop.

## Insights

- The test pattern is reusable: any multi-skill composition protocol (not just `skill-pairing`) could adopt the same five-lens grid — selection, deflection, failure-naming, uncertainty propagation, ceiling enforcement.
- Tests 2 and 5 together define the correct aperture: the skill must neither over-pair (force composition when one will do) nor under-route (refuse when three are requested).
- The discipline overlaps with [[Recursive Governance Protocol — Theseus, Auryn, Hopf|Theseus/Auryn/Hopf]] governance layering: each stage must hand forward uncertainty rather than absorb it.

## Open Questions

- Are these tests actually runnable in the current harness, or are they a specification awaiting an evaluator?
- Does `skill-pairing` enforce the two-skill ceiling structurally (refusal to take a third parameter) or only behaviorally (explanation + route)?
- Which skills in the [[Claude Code Skill Corpus|corpus]] are the likeliest near-misses for Test 3's "improvised substitute" failure mode?

## Related

- [[Claude Code Skill Corpus]] — primary skill index
- [[MASTERxMASTERxMASTER — Skill Corpus Map]] — broader skill-corpus map
- [[Diamond-Eyes — Aesthetic Refinement Skill]] — referenced in Test 5
- [[Recursive Deterministic AI Governance — Method and Paper]] — referenced in Test 4
- [[Recursive Governance Protocol — Theseus, Auryn, Hopf]] — same handoff-discipline lineage
- [[Codex Skill Corpus Sync — 2026-04-20]] — recent context on the skill corpus

## Sources

- `Clippings/Complete solutions, not compromises.md` — Claude conversation, 2026-04-20, three messages
- Source URL: https://claude.ai/chat/28766802-19f9-4e8b-a01d-320b1d5b1350
