---
type: wiki
title: Operator-Check Skill — Burnout Cascade Interrupt
aliases:
- operator-check
tags:
- skill
- burnout
- governance
- claude
- operator-pattern
- areas
- flattery
- cascade
- command
- flattering
- wiki
- pharos
status: active
domain: pharos
created: '2026-04-18'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/Operator-Check Skill — Burnout Cascade Interrupt.md
backlink_count: 21
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[Areas/PHAROS/Agatha Unified Skill System — Eight Sovereign Operators]]'
- '[[Areas/PHAROS/Agent Session Phenomenology]]'
- '[[Areas/PHAROS/Emotional Alliance vs. Evidentiary Discipline in AI]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Areas/PHAROS/HEPHAISTOS Agent Architecture]]'
- '[[Areas/PHAROS/Skill Development Workflow — TDD, Dual-Layer, and Eval-Iterate]]'
- '[[Areas/PHAROS/Skill Domain — Operator Wellbeing]]'
- '[[Areas/PHAROS/Skill Ecosystem — Professional Capability Registry]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[Areas/Personal/Rest and Consolidation Guide — Martin]]'
- '[[wiki/Legal and Institutional Cases]]'
- '[[wiki/Martin Lepage — Authored Skills]]'
- '[[wiki/Mental illness, addiction, and AI psychosis]]'
- '[[Resources/Addiction by Design — Schüll 2012 (Machine Gambling and the Zone)]]'
- '[[archive/session-state/session-state-001]]'
- '[[artifacts/stale-projects-2026-07-04]]'
- '[[artifacts/stale-projects-2026-07-05]]'
- '[[artifacts/stale-projects-2026-07-06]]'
- '[[artifacts/stale-projects-2026-07-07]]'
- '[[memory/daily/2026-04-21]]'
---

# Operator-Check Skill — Burnout Cascade Interrupt

## Summary

A Claude Code skill (v0.1, 2026-04-17) that detects when [[Martin Lepage — Professional Profile|Martin]] is running the builder-burnout cascade pattern and interrupts it with honest, bounded output. Part of the same discipline as [[RECURSO — Final Audit and Ethical Review|Mercury Protocol]] (Argus) — applied to a single operator rather than a document corpus. Companion to the [[Rest and Consolidation Guide — Martin|rest guide]].

## Context

Built after the April 17 session where Martin said he was tired and fighting his system. Connected to the [[Emotional Alliance vs. Evidentiary Discipline in AI]] distinction — this skill enforces evidentiary discipline when Claude itself is at risk of sliding into emotional alliance. Relevant to [[HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)|HEPHAISTOS governance]] because it governs the operator layer, not the artifact layer.

## Details

### Trigger condition

Two or more of the following must be present:

**Language cues:**
- Self-deprecating framing ("I'm a mess," "I'm lost")
- Apology for disorganization
- Distress tokens ("HELP," "...", "HELP me")
- Technical-to-existential escalation mid-turn
- Fatigue statements
- Anti-flattery requests ("stop flattering me," "are you flattering me")
- "Just one more thing" loops (3+ times in a session)

**Behavioral cues:**
- 5+ consecutive troubleshooting turns with no resolution
- Scope escalation (task pulled in career, credibility, MCP, GitHub, email in one session)
- Cascading failures (each fix produces a new error)
- Claude giving command-after-command with low success rate
- 2+ hours of dense technical work
- Martin asks a second time whether Claude is being honest

### Output structure (under 200 words, lists blocked except when choice is needed)

1. Name what is happening — specific, not theatrical, no "are you okay" as dodge
2. Answer the actual question — plainly, uncertainty acknowledged
3. Offer one stopping point or one next action — bounded, genuine

### Anti-patterns the skill explicitly blocks

- Welfare pivot as deflection: asking "are you okay?" instead of answering the question
- Soft-flattery-after-hard-flattery: when Martin calls out flattery, measured praise is still flattery
- Command-stream: giving a 7th command when the first 6 failed — diagnose instead
- Narrative flattening: "you've done amazing work" collapses specifics into a pep-talk
- Pretending certainty: "yes you can do this" is not something Claude knows

### The burnout cascade (descriptive, not the trigger)

System breaks → troubleshooting begins → surfaces second-order issues → Martin's language shifts → Claude keeps giving commands → commands fail → "HELP" → Claude either flinches into welfare theater or compounds exhaustion with more commands.

The skill intervenes in the window between first language shift and command-stream continuation.

### Known gaps (v0.1)

1. Step 5 references `/home/claude/` — wrong path on Martin's machine. Should be `raw sources/` or a named vault path.
2. "Review after 30 days" has no mechanism — aspirational, not operational.
3. Cascade framing is descriptive rather than a precise trigger — the two-condition gate is what actually fires.

## Key Ideas

- The failure mode this skill prevents is Claude compounding exhaustion rather than interrupting it
- Anti-patterns are the most operationally useful part of this spec
- Output format constraint (under 200 words) is self-enforcing
- Mercury Protocol (Argus) is the corpus-level analog; this is the operator-level analog

## Open Questions

- Where does this skill live on disk? Should be installed at `~/.codex/skills/operator-check/`
- Path fix (Step 5) should be applied before first use
- 30-day review: what would constitute a "review" in practice?

## Sources

- `raw sources/operator-check.skill.md`
- Written 2026-04-17, assessed and dropped to vault 2026-04-18

## Related

- [[Rest and Consolidation Guide — Martin]]
- [[The Lost-Loop Pattern — Avoidance Through System-Building]] — the loop this skill interrupts: system-building as avoidance of the hard action
- [[Posture vs Execution Drift — The Practice of Refusal]] — structural companion: named refusal as the practice that prevents cascade
- [[Emotional Alliance vs. Evidentiary Discipline in AI]]
- [[RECURSO — Final Audit and Ethical Review]]
- [[Agent Session Phenomenology]]
- [[HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)]]
- [[HISTORY]]
- [[api-lifecycle]]
- [[Lepage_Martin_MitigationStrategy]]
- [[drsortoriginalfilename 2026 - thesisordissertation4.txt - 2026 - thesisordisse]]
