---
type: wiki
title: Governed Revision Loop — Responsible Self-Improving Agents
aliases:
- governed revision loop
- self-improving agent governance
- responsible agent self-revision
- Governed Revision Loop
- wiki/Governed Revision Loop — Responsible Self-Improving Agents
tags:
- ai-governance
- agents
- self-improvement
- obsidian-vault
- pharos
- drift
- evaluation
- wiki
- governed-revision-loop-responsible-self-improving-agents-md
- acceptance
- governed
- obsidian
- edits
- post
- color-orange
status: active
created: '2026-04-20'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Governed Revision Loop — Responsible Self-Improving Agents.md
backlink_count: 12
backlinks:
- '[[wiki/AI Iterative Loop — Frame Capture and Recursive Validation Failure]]'
- '[[wiki/Elemental Agents — Productization Plan (2026-05-24)]]'
- '[[wiki/Governance and PHAROS MOC]]'
- '[[wiki/OUTLIERS — Five Notes That Break the Architecture]]'
- '[[wiki/Obsidian Agent Vault — Launch Kit]]'
- '[[wiki/PHAROS LinkedIn April 2026 Publishing Routine]]'
- '[[wiki/Trismégiste Eval v2 — Argus Closure and Redesign (2026-05-05)]]'
- '[[archive/session-state/session-state-001]]'
- '[[assets/elemental-agents/positioning-memo]]'
- '[[memory/agents/Decisions]]'
- '[[memory/agents/Events]]'
- '[[memory/agents/Journal]]'
---

# Governed Revision Loop — Responsible Self-Improving Agents

## Summary

A thought-leadership argument that "self-improving agents" only become responsible when wrapped in a **governed revision loop**: versioned baselines, role separation for proposal/review/acceptance, input-sanitization boundaries, and real-task validation. Drafted as a LinkedIn post by Martin Lepage on 2026-04-16, positioning Obsidian-based agent stacks (cf. [[Obsidian Agent Vault — Launch Kit]]) as the practical infrastructure. Ties into [[Recursive Deterministic AI Governance — Method and Paper|recursive deterministic governance]] and the [[PHAROS Recalibration — Unified Governance Architecture|PHAROS method]].

## Context

Source: `raw sources/self-improving-agent-governed-revision-post.md` (LinkedIn post draft, 2026-04-16). The post targets a specific rhetorical failure mode in AI discourse: "self-improving agent" read as "system that rewrites its own instructions autonomously." Martin's reframe: the responsible version is a system where the model **proposes** edits to its own `SKILL.md` or `CLAUDE.md`, but acceptance runs through a governed loop — versioning, evaluation separation, input security, real-task validation, human arbitration. The post positions the Obsidian-based agent stack ([[Obsidian Agent Vault — Launch Kit]], [[Claude Code Skill Corpus]]) as the native substrate for this loop because it already provides versioning, backlinks, change logs, and graph memory.

## Details

### The Four Design Surfaces

The post identifies four places where "self-improvement" fails without governance, and what each requires:

1. **Drift as a design question, not a failure.**
   - Required: versioned baseline, explicit change logs, rollback points.
   - Converts drift from pathology into traceable evolution. Authorship is preserved because every change is inspectable and reversible.
2. **Evaluation separation.**
   - Required: distinct roles for **proposal**, **review**, and **acceptance** — not the same model doing all three.
   - Independent signals: task-based tests, constraint checks, before/after comparisons.
   - Fluency can assist; fluency cannot be the metric. This mirrors the [[Skill-Pairing — Five-Case Test Suite|skill-pairing]] discipline of grading behavioral compliance over output polish.
3. **Security as a design surface.**
   - Required: scope, sanitize, and tag inputs that could influence instruction edits.
   - External artifacts are untrusted by default. Instruction-layer changes require confirmation for any change touching core rules. This converts an apparent vulnerability into an explicit boundary condition.
4. **Validation against real tasks.**
   - Required: lightweight harnesses — repeatable prompts, small test suites, outcome logs.
   - Instructions run against real work, outcomes observed, results compared to baseline. Self-revision becomes evidence-backed iteration.

### The Governed Loop (Operational Form)

```
model proposes edits
    ↓
system tests edits against defined tasks
    ↓
differences logged, compared to baseline
    ↓
human operator accepts, modifies, or rejects
    ↓
(loop)
```

The loop is not a self-rewriting system. It is a **governed revision loop** with human arbitration at the acceptance gate.

### Why Obsidian-Based Agent Stacks Fit

Martin's argument for Obsidian as the native substrate:
- **Notes = versioned instruction files.** Every edit is a diff.
- **Backlinks = rule-to-justification traceability.** Rules link back to the tasks, failures, or incidents that justified them.
- **Change logs sit next to outcomes.** The same vault holds both the rule and the evidence of its effect.
- **Graph = memory, traceability, context.** The three things the model lacks when editing its own instructions in isolation.

The result: "not a more eloquent `SKILL.md`, but a more accountable one."

### What the Model Still Does

- Surfaces ambiguity, redundancy, gaps
- Drafts alternatives
- Accelerates iteration

What the model does **not** do: accept its own edits. The constitution remains governed.

## Key Ideas

- **"Self-improving" is the wrong word.** The responsible version is *governed revision*, with proposal–review–acceptance as distinct roles.
- **Drift is always present; the question is whether it's traceable.** Versioning + change logs + rollback turn drift from threat into trace.
- **Same-model evaluation is fluency-laundering.** If the model that drafts edits also judges them, fluency dominates. Real evaluation requires independent signals.
- **Input channels are instruction channels.** Tool outputs, external artifacts, and user inputs that can influence instruction edits must be treated as untrusted — else the instruction layer has the widest attack surface in the system.

## Insights

- The post operationalizes the [[Recursive Deterministic AI Governance — Method and Paper|recursive deterministic governance method]] for a specific artifact class (agent instruction files) and a specific infrastructure (Obsidian). It is a worked example of the method, not new theory.
- The Obsidian-as-agent-infrastructure argument is commercially load-bearing for [[Obsidian Agent Vault — Launch Kit|the Vault product]] — the LinkedIn post is, in effect, a thought-leadership tailwind for the product launch.
- The April root Documents publishing packet in [[PHAROS LinkedIn April 2026 Publishing Routine]] provides the calendar/cadence layer for this kind of post: lower volume, stronger governance infrastructure theme, and explicit PHAROS rebrand discipline.
- The proposal/review/acceptance separation maps cleanly onto the three-agent architecture in [[Recursive Governance Protocol — Theseus, Auryn, Hopf|Theseus/Auryn/Hopf]]. HEPHAISTOS proposes scope, Queen Keyport reviews governance fit, Hermes routes; the human operator accepts.
- This is the positive version of the critique in [[Governance by Denial]]: instead of governance that hides and defers, a governance structure that makes every change inspectable and accountable.

## Extraction Candidates (from the raw source)

The raw source flagged four extraction candidates:
- Governed revision loop concept → **this note**
- Drift-as-design-question framing → could split into its own note or merge with existing governance notes ([[Recursive Deterministic AI Governance — Method and Paper]] is the natural home)
- Evaluation separation (proposal/review/acceptance) → connects to [[PHAROS Recalibration — Unified Governance Architecture|PHAROS method]]
- Obsidian-as-agent-infrastructure argument → already captured in [[Obsidian Agent Vault — Launch Kit]]

## Open Questions

- Has the post been published on LinkedIn? If so, what response did it get — particularly around the proposal/review/acceptance separation claim?
- Does the governed revision loop have a place in the [[Claude Code Skill Corpus]] as its own skill, or is it a meta-discipline that governs how other skills evolve?
- How does this frame interact with Anthropic's model-card and constitutional AI work? (See [[ANTHRO PHAROS — Anthropic vs PHAROS Governance Comparison]].)

## Related

- [[Obsidian Agent Vault — Launch Kit]] — commercial substrate for the loop
- [[Recursive Deterministic AI Governance — Method and Paper]] — theoretical parent
- [[Recursive Governance Protocol — Theseus, Auryn, Hopf]] — three-agent architecture
- [[PHAROS Recalibration — Unified Governance Architecture]] — PHAROS method
- [[Claude Code Skill Corpus]] — the artifact class being governed
- [[Skill-Pairing — Five-Case Test Suite]] — same discipline (behavioral over fluency)
- [[Governance by Denial]] — the negative version of this argument
- [[PHAROS LinkedIn April 2026 Publishing Routine]] — public-surface cadence for this post family
- [[AI Governance Public Statement and Market Impact Pack]] — broader public governance language

- [[This file is not the tool itself. It is a whitepap]]
- [[`if.gov` Full Explainer v1.1 (Triage + Council + Extended, 4-Audience Deep Dive)]]
- [[if.blackboard Full Explainer v1.2 (Four-Audience, Claim-Boundary Strict)]]
- [[if.switchboard Full Explainer v1.4 — SIP Extension Edition]]
## Sources

- `raw sources/self-improving-agent-governed-revision-post.md` — Martin Lepage, LinkedIn post draft, 2026-04-16
- Hashtags used: `#AIGovernance #Agents #AISafety #PromptEngineering #AIInfrastructure`
