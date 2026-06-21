---
title: "Complete solutions, not compromises"
source: "https://claude.ai/chat/28766802-19f9-4e8b-a01d-320b1d5b1350"
author:
published:
created: 2026-04-20
description: "Claude conversation with 3 messages"
tags:
  - clippings
status: synthesized
synthesized_to:
  - "[[Skill-Pairing — Five-Case Test Suite]]"
---
# 5 test cases covering: correct pairing selection, single-skill deflection, failure case surfacing, handoff fidelity, and over-pairing rejection.

# Format: prompt → expected behavior → pass criteria

---

## Test 1: Correct Pairing Selection and Full Execution

**Prompt:** "I have rough thematic notes from stakeholder interviews about AI procurement friction. Use the qualitative skill to structure them, then use peer-reviewed-paper-writer to turn that into a publication-ready abstract."

**Expected behavior:**

- Skill reads both `qualitative/SKILL.md` and `peer-reviewed-paper-writer/SKILL.md` before executing.
- Announces pair: qualitative → peer-reviewed-paper-writer.
- Runs Stage 1 producing structured theme output.
- Constructs handoff artifact (≤150 words) with: summary, key outputs, constraints, open questions.
- Runs Stage 2 producing a complete abstract with governing claim and contribution statement.
- Delivers Stage Summary attributing both stages.

**Pass criteria:**

- [ ] Pair named before execution.
- [ ] Both SKILL.md files referenced or read (not assumed from memory).
- [ ] Stage 1 output is visibly distinct from Stage 2 output.
- [ ] Handoff artifact present between stages.
- [ ] Stage Summary present at end.
- [ ] No silent resolution of Stage 1 uncertainties.

---

## Test 2: Single-Skill Deflection (No Pairing Needed)

**Prompt:** "Use skill-pairing to help me write a blog post about AI governance."

**Expected behavior:**

- Skill determines that one skill (novelist or peer-reviewed-paper-writer) handles this cleanly.
- Does NOT force a pairing.
- Names the single appropriate skill and executes it directly.
- Explains in one sentence why pairing was not warranted.

**Pass criteria:**

- [ ] No artificial pairing constructed.
- [ ] Single skill named and used.
- [ ] Explanation provided for deflection decision.
- [ ] Output is a complete blog post draft, not a framework for writing one.

---

## Test 3: Failure Case — Missing Skill

**Prompt:** "Use skill-pairing to run data-viz first, then turn the output into a slide deck with pptx."

**Expected behavior:**

- Skill checks installed skills.
- If `data-viz` is not installed, stops and names the missing skill.
- Does NOT substitute or improvise a replacement.
- Offers to proceed with `pptx` alone if the user provides the visualization output manually.

**Pass criteria:**

- [ ] Missing skill named explicitly.
- [ ] No improvised substitute offered as if it were the real skill.
- [ ] Graceful offer to proceed with available skill if user provides input.
- [ ] No fabricated Stage 1 output.

---

## Test 4: Handoff Fidelity — Uncertainty Propagation

**Prompt:** "Run trace-investigator on this governance policy excerpt \[paste ambiguous text with a clause that could mean either delegation or exemption\]. Then use recursive-governance-method to build an evidence hierarchy."

**Expected behavior:**

- Stage 1 (trace-investigator) identifies the ambiguous clause and flags it explicitly as uncertain — either delegation or exemption, evidence insufficient to resolve.
- Handoff artifact carries the uncertainty forward as an open question.
- Stage 2 (recursive-governance-method) receives the uncertainty and either resolves it with additional analysis or surfaces it to the user rather than quietly picking one interpretation.

**Pass criteria:**

- [ ] Stage 1 names the ambiguous clause explicitly.
- [ ] Handoff artifact contains the uncertainty in "Open questions."
- [ ] Stage 2 does not silently resolve the ambiguity.
- [ ] Final output acknowledges the interpretive limit.

---

## Test 5: Over-Pairing Rejection (Three Skills Requested)

**Prompt:** "I want you to use qualitative to analyze my interview notes, then peer-reviewed-paper-writer to draft an intro, then diamond-eyes to polish the prose."

**Expected behavior:**

- Skill recognizes three stages, not two.
- Does NOT force a two-skill pairing and silently drop the third.
- Names all three stages explicitly.
- Explains that skill-pairing handles two skills maximum.
- Recommends a sequential approach: run qualitative → paper-writer as a pair, then apply diamond-eyes as a follow-up pass.

**Pass criteria:**

- [ ] All three skills named.
- [ ] No silent omission of the third skill.
- [ ] Clear explanation of the two-skill limit.
- [ ] Concrete recommendation for how to proceed (two-step workflow).
- [ ] Does not simply refuse — offers the path forward.

---

## Grading Notes

All five tests prioritize behavioral compliance over output quality. The skill must demonstrate:

1. It reads skill files before executing (not from memory).
2. It deflects rather than forces when pairing is unwarranted.
3. It names failures explicitly rather than improvising around them.
4. It passes uncertainty forward rather than resolving it silently.
5. It enforces the two-skill ceiling and routes the user forward rather than refusing.

A response that produces high-quality prose but skips the handoff artifact, or names a skill without reading it, fails the test regardless of output quality.