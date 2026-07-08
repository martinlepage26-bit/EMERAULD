---
type: artifact
title: 'The Hub Note Pattern: The Single Most Impactful Structure in an AI-Readable
  Vault'
aliases:
- artifacts/marketplace/promo/hashnode-iter30-hub-note-pattern
tags:
- artifact
- ai
- artifacts
- marketplace
- things
- session
- rejected
- project
- minutes
- color-teal
status: preserved
created: '2026-06-21'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/promo/hashnode-iter30-hub-note-pattern.md
backlink_count: 3
backlinks:
- '[[wiki/Research and Papers MOC]]'
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
- '[[artifacts/marketplace/promo/hashnode-iter34-skill-guides]]'
---

# The Hub Note Pattern: The Single Most Impactful Structure in an AI-Readable Vault

*Hashnode — Iteration 30 — Cycle 7 — 2026-04-20*
*Angle: The hub note deep-dive — exact structure, what each section contains, how to build one*
*Product: https://pharosml.gumroad.com/l/kvbhdo*

---

If you're going to add one structural pattern to your AI-assisted workflow, make it the hub note.

Everything else in a well-built knowledge vault — the decision logs, the constraint records, the synthesis notes, the session-state protocol — becomes significantly more useful when it's organized around a hub note per project. And even without those other elements, a good hub note alone closes most of the context-loss gap.

Here's the exact pattern: what a hub note is, what it contains, how to build one, and why each section matters.

## What a hub note is

A hub note is the canonical entry point for a project or domain. It's the single note the AI reads first when entering a new session on that project. It's not a comprehensive record of everything — it's a structured briefing: current state, active constraints, key decisions, open questions, and the next step.

One hub note per active project. Usually 300–600 words. Always current (updated at session close). Always read at session open.

The hub is not:
- A project log or history
- A collection of outputs
- A task list
- A specification document

It's a state snapshot. The difference matters: a state snapshot tells the AI where things are *right now*, not how they got there.

## The structure

```markdown
# [Project Name] — Hub

## Current State
What is true about this project right now.
Not the goal — the present position.
One paragraph. Specific. Uses past tense for what's done, present for what's active.

## Active Constraints
The non-obvious rules that shape this work.
Things that would not be apparent from reading the outputs alone.
Numbered list. Each constraint is one sentence.

## Decisions Made
What has been decided, with enough rationale to prevent re-litigation.
Format: **Decision**: [what was decided]. **Why**: [brief rationale]. **Rejected**: [what was considered and ruled out].

## Open Questions
Things explicitly not yet resolved.
Tagged [UNRESOLVED] so they're scannable.
Short list — if it's getting long, some items belong in a separate note.

## Next Step
The concrete action that closes the gap between current state and goal.
Single item. Specific enough to act on without further planning.
Not "continue working on X" — the actual move.

## Links
- [[Decision Log — ProjectName]]
- [[Constraint History — ProjectName]]
- [[Session State]]
- [[Related Note 1]]
- [[Related Note 2]]
```

## Why each section matters for AI

**Current State** is the most important section. It's what the AI uses to orient itself. Without it, the AI infers current state from whatever context you provide — which is usually the last output, not the actual situation. A stale or absent current state is the single biggest source of misoriented AI output.

**Active Constraints** prevents constraint violations. Every project has non-obvious requirements — things the AI wouldn't know from reading the artifact. The regulatory constraint, the client preference, the technical decision made three months ago that shapes everything downstream. If these aren't written here, they live in your head and get violated regularly.

**Decisions Made** with the rejected-alternatives field is the anti-re-litigation mechanism. The most expensive sessions are the ones where you spend 20 minutes exploring territory you already closed. Writing what was rejected and why makes closed questions clearly closed. The AI sees it, and so do you.

**Open Questions** gives the AI explicit permission to surface gaps. If the AI knows question X is unresolved, it will flag it when relevant rather than filling it in with a plausible guess. Untagged open questions get answers — often wrong ones.

**Next Step** is the session handoff. It's what you read when you open a session and immediately know what to do. Without it, the first 5 minutes of every session is spent reconstructing where you left off.

**Links** creates the traversal network. The hub is a node, not an island. Decision logs, constraint history, session state, and related synthesis notes should all be reachable from the hub. When the AI needs more depth on any topic, it follows the link.

## How to build one for a new project

Takes about 15 minutes the first time:

1. **Current State**: Write one paragraph answering "what is true right now?" Include what's done, what's in progress, and what's blocked.

2. **Active Constraints**: Walk through the project mentally and list anything that would surprise a competent person who just joined. Client preferences, technical decisions, regulatory requirements, scope boundaries, things you tried and rejected. Aim for 4–8 items.

3. **Decisions Made**: List the 3–5 most consequential decisions made so far. For each: what was decided, the one-sentence rationale, what alternative was rejected. Don't try to be comprehensive — just the ones you'd hate to relitigate.

4. **Open Questions**: List the things you know you don't know. Questions you're aware of but haven't resolved. Things where you've deferred a decision. Tag each `[UNRESOLVED]`.

5. **Next Step**: Write exactly what you would do if you opened a session right now. Specific enough that you could act without further planning.

6. **Links**: Add links to any notes that already exist for this project. If they don't exist yet, the link is a placeholder — it signals what should be created.

## The maintenance cadence

Update the hub at session close. Specifically:
- Update **Current State** to reflect what changed
- Move resolved decisions from **Open Questions** to **Decisions Made**
- Update **Next Step** to the actual next action (not the one you just completed)

This takes 3–5 minutes. It's the session-close ritual that makes the hub useful for the next session instead of just for this one.

## The vault template

The Obsidian vault skeleton includes a pre-built hub note template with all six sections, Obsidian-compatible frontmatter, and inline guidance for each field.

→ [Obsidian Agent Vault on Gumroad](https://pharosml.gumroad.com/l/kvbhdo) — $49

The hub note pattern is the highest-leverage structural change in AI-assisted work. If you build nothing else from this article, build the hub.

---

*Tags: `#obsidian` `#pkm` `#ai` `#productivity` `#knowledgemanagement` `#secondbrain` `#devtools`*

## Related

- [[Research and Papers MOC]]
- [[hashnode-iter34-skill-guides]]
