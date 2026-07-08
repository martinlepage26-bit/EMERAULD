---
type: artifact
title: Most AI "Hallucinations" Are Context Failures, Not Model Failures
tags:
- artifact
- ai
- artifacts
- marketplace
- model
- errors
- hallucination
- failures
- context
status: preserved
created: '2026-06-21'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/promo/devto-iter25-hallucination-fix.md
backlink_count: 3
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
- '[[artifacts/marketplace/promo/hashnode-iter34-skill-guides]]'
---

# Most AI "Hallucinations" Are Context Failures, Not Model Failures

*Dev.to — Iteration 25 — Cycle 6 — 2026-04-20*
*Angle: The hallucination fix — structured context as a reliability tool*
*Product: https://pharosml.gumroad.com/l/kvbhdo*

---

"Hallucination" is the word we use when an AI model produces something plausible but wrong. It's treated as a fundamental model failure — an inherent limitation of probabilistic text generation that we're stuck managing.

I want to challenge that framing, at least for applied AI work.

Most of what gets called hallucination in real workflows isn't the model inventing things out of nothing. It's the model filling in missing context with its best guess. And most of the time, the context isn't actually missing from reality — it's just missing from what you gave the model.

That's a context problem, not a model problem. And it's fixable.

## What hallucination actually looks like in practice

You're writing a technical specification. You ask Claude to add a section on authentication. It writes something technically reasonable but inconsistent with your actual architecture — it suggests OAuth when you've already decided on JWT for specific reasons, proposes a token rotation period that conflicts with your security policy, and doesn't mention the session handling constraint that came out of last month's incident review.

Is that a hallucination? Sort of. The model generated plausible content. But the failures are all traceable to missing context:
- It didn't know you'd decided on JWT (no decision log)
- It didn't know your security policy constraints (no active-constraints record)
- It didn't know about the incident and what you learned from it (no session history)

Give the model all three pieces of context explicitly, and those specific errors disappear. The model wasn't wrong because it can't reason about authentication — it was wrong because it was reasoning from incomplete information.

## The gap between capability and consistency

Modern LLMs are remarkably capable. They can reason about complex domains, maintain logical consistency within a context window, and produce high-quality output when given the right inputs.

The problem in applied work isn't capability — it's consistency. The same model, asked the same question at different times with different context, produces different answers. Some of those differences are fine (appropriate variation). Some are errors that get called hallucinations.

The consistency gap is almost entirely explained by context variation. What you told the model in this session vs. last session. What you remembered to include vs. forgot. What changed in your project since the last time you worked on this.

## What structured context actually prevents

When I introduced a session-state protocol into my workflow — a structured record of active constraints, decisions made, open questions, and current project state, read by the AI at the start of every session — the incidence of the errors I was calling "hallucinations" dropped substantially.

Not to zero. There are genuine model errors that context doesn't fix. But the large majority of my workflow failures were context failures that looked like model failures.

Specific patterns that disappeared:

**Constraint violations.** "The AI keeps suggesting X even though I've told it we can't do X." Once the constraint was written into the active-constraints field and read every session, this stopped. The model was never incapable of respecting the constraint — it just wasn't being told about it consistently.

**Decision revisiting.** "The AI keeps re-opening questions I've already answered." Once the decisions-made field included not just the decision but the rationale and the rejected alternatives, this stopped. The model could see not just what was decided but why — making the closed question clearly closed.

**Stale-reference errors.** "The AI is working from an outdated version of the spec." Once the current-state field explicitly named the version and what had changed since the last session, this stopped.

**Cross-project contamination.** "The AI seems to be mixing up details from different projects." Once each project had its own hub note with its own explicit context, this stopped.

## The architecture that makes this work

The context needs to be:

1. **Structured** — not a prose dump, but specific fields: constraints, decisions, state, next step. Structured context is more reliably loaded than narrative context.

2. **Current** — updated at session close, not just at project start. Context that's six weeks stale is almost as bad as no context.

3. **Connected** — linked to other relevant notes. An authentication constraint note that links to the threat model, the incident log, and the relevant decision records is more useful than a standalone note.

4. **Scoped** — per project, not global. A hub note for each active engagement prevents cross-project contamination.

This is graph-structured, file-native knowledge — Obsidian's model, applied to AI workflow.

## The vault

The Obsidian vault skeleton that operationalises this architecture — hub templates, session-state protocol, decision-log format, linking rules, note types — is packaged as a $49 template.

→ [Obsidian Agent Vault on Gumroad](https://pharosml.gumroad.com/l/kvbhdo)

If your AI workflow is producing errors you're attributing to model failures, run the diagnosis first: how much of that context does the model actually have access to in each session? The answer is often "less than you think."

---

*Tags: `#ai` `#llm` `#productivity` `#obsidian` `#pkm` `#softwareengineering` `#devtools`*

## Related

- [[Governance and PHAROS MOC]]
- [[hashnode-iter34-skill-guides]]
