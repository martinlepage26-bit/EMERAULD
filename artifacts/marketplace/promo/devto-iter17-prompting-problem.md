---
type: artifact
title: Why Better Prompts Aren't the Fix (And What Actually Is)
aliases:
- artifacts/marketplace/promo/devto-iter17-prompting-problem
tags:
- artifact
- artifacts
- marketplace
- prompt
- session
- mediocre
- rejected
- context
- color-orange
status: preserved
created: '2026-06-21'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/promo/devto-iter17-prompting-problem.md
backlink_count: 3
backlinks:
- '[[wiki/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
- '[[artifacts/marketplace/promo/hashnode-iter34-skill-guides]]'
---

# Why Better Prompts Aren't the Fix (And What Actually Is)

*Dev.to — Iteration 17 — Cycle 4 — 2026-04-20*
*Angle: The prompting problem — structured context beats prompt engineering*
*Product: https://pharosml.gumroad.com/l/kvbhdo*

---

I spent three months trying to get consistent results from Claude by improving my prompts.

Better structure. More examples. Chain-of-thought instructions. Role framing. Temperature tuning. The whole toolkit.

The results got marginally better, then plateaued. And then I noticed something uncomfortable: the same prompt produced wildly different output depending on *when* in a project I ran it.

Early in a project, when I had full context in my head — great results. Six weeks in, after I'd context-switched five times — mediocre results, even with the "good" prompt.

The prompt hadn't changed. *My context had.*

## The actual variable

Prompts tell the model what to do. Context tells the model who's asking, what they've already decided, what constraints they're operating under, and what "good" looks like for this specific situation.

When you have rich context, a mediocre prompt works fine. When you have weak context, even a perfect prompt produces generic output.

This is the thing prompt engineering tutorials don't address: they optimize the instruction while assuming context is constant. It isn't. Context degrades continuously across sessions, context-switches, and team handoffs.

## What degraded context looks like in practice

You're working on a technical document. You've been iterating on it for two weeks. You have strong opinions about what should and shouldn't be in it — but those opinions live in your head, not anywhere the AI can see them.

You open a new session. You paste in the document and your prompt. The AI helpfully adds sections you explicitly decided to exclude last week. It uses a tone you've already rejected. It misses the specific constraint that makes this project unusual.

You spend 20 minutes correcting outputs that a well-contextualised session would have gotten right in one pass.

Multiply that by every session, every project, every team member. That's the real cost.

## What structured context actually looks like

The fix isn't a better prompt. It's a persistent record that travels with every session:

**Decision log** — what's been decided and, critically, what's been *rejected*. Not just the current answer but the ruled-out alternatives. When the AI suggests something you've already considered and discarded, you can point to the record: "We tried that. Here's why it failed."

**Active constraints** — the specific requirements, boundaries, and non-obvious rules that apply to this project. Things that wouldn't be obvious from the artifact alone.

**Current state** — where the project is right now. Not a full history, just the present position: what's done, what's in progress, what's blocked and why.

**Next step** — the concrete action that closes the gap between current state and goal. Not "continue working on X" — the actual next move.

This structure takes 10 minutes to set up per project. It eliminates the context-reconstruction overhead on every subsequent session.

## The compounding effect

The real payoff isn't session 2. It's session 20.

By the time you've been working on something for three months, the accumulated decisions, rejected approaches, and learned constraints are substantial. Without a record, you reconstruct a fraction of them each session and forget the rest. With a record, they're all available to the AI immediately, every time.

The output quality doesn't plateau. It improves as the record grows.

## The vault structure

I built a file-native knowledge vault that operationalises this pattern across all my AI-assisted work:

- **Hub notes** per project — one canonical entry point with the current state, decisions made, and active constraints
- **Decision log format** — a specific structure for recording *why* things were rejected, not just what was chosen
- **Skill notes** — reusable task templates that carry their own context requirements
- **Session-state protocol** — a start/end ritual that updates the record so the next session starts clean

The skeleton for this system — all the note types, hub templates, linking patterns, and the optional local runtime — is packaged as a $49 Obsidian vault template.

→ [Obsidian Agent Vault on Gumroad](https://pharosml.gumroad.com/l/kvbhdo)

If you've been frustrated by inconsistent AI output and your first instinct has been to improve the prompt, consider that the problem might be upstream of the prompt.

---

*Tags: `#productivity` `#ai` `#obsidian` `#promptengineering` `#devtools`*

## Related

- [[Governance and PHAROS MOC]]
- [[hashnode-iter34-skill-guides]]
