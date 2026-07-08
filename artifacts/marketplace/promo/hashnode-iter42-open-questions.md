---
type: artifact
title: 'The Open Questions Protocol: How to Stop AI from Filling In What It Doesn''t
  Know'
aliases:
- artifacts/marketplace/promo/hashnode-iter42-open-questions
tags:
- artifact
- ai
- artifacts
- marketplace
- invalidation
- open
- questions
- resolved
- blocked
- color-purple
status: preserved
created: '2026-06-21'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/promo/hashnode-iter42-open-questions.md
backlink_count: 3
backlinks:
- '[[wiki/Research and Papers MOC]]'
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
- '[[artifacts/marketplace/promo/hashnode-iter34-skill-guides]]'
---

# The Open Questions Protocol: How to Stop AI from Filling In What It Doesn't Know

**Platform:** Hashnode
**Iteration:** 42 — Cycle 10
**Angle:** Single pattern deep-dive — open questions as held uncertainty, not to-do items
**Tags:** obsidian, ai, knowledge-management, developer-tools, claudeai
**Status:** READY TO POST

**Instructions:** Log into hashnode.com → Write → paste content below → tags: obsidian, ai, knowledge-management, developer-tools, claudeai → publish to your blog.

---

There's a failure mode in AI-assisted work that's almost invisible until you know to look for it.

Questions that haven't been answered don't stay open in the AI's working model. They get filled in.

If you're working on an API design and it's genuinely unclear whether internal service calls should route through the gateway or bypass it — but you haven't written that uncertainty down anywhere the agent can read — the agent will treat it as resolved. It'll pick an approach (the more common one, or the one that appears most often in similar contexts it's been trained on) and proceed. It won't flag the decision point. It won't ask. It'll just produce work that implicitly assumes an answer you never gave.

This is the open question problem. The fix is a simple protocol, but getting it right requires understanding what an open question actually is.

## What an open question is (and isn't)

An open question is not a to-do item.

A to-do: "Add error handling to the auth endpoint."
An open question: "Should auth errors return 401 with a WWW-Authenticate header or 403 with a JSON error body — and which choice affects our frontend error handling?"

To-dos have clear execution paths. Open questions don't — they're decision points where the right answer depends on constraints, tradeoffs, or information you don't yet have.

An open question is not a vague uncertainty either.

Vague: "Figure out the caching situation."
Open question: "Which cache invalidation strategy to use for user profile data — time-based TTL (simple, risks stale data during profile updates) or event-based invalidation (consistent, requires webhook infrastructure we don't have yet). Blocked on: decision about webhook capacity in Q3 roadmap."

The difference matters for the AI. "Figure out the caching situation" gives the agent permission to make a decision and move on. "Time-based TTL vs event-based invalidation — blocked on Q3 roadmap decision" tells the agent this is explicitly unresolved, here's why, and here's what would resolve it.

## The two failure modes of untracked open questions

**Failure mode 1: Silent gap-filling**

The agent encounters an unresolved design point. Without a signal that it's unresolved, it picks an approach — usually the one that seems most reasonable in isolation. The work looks complete. You review it, notice the implicit decision, and spend 20 minutes re-doing the section to implement a different approach.

This happens constantly in undirected AI work. Each instance is small. Across a project, it adds up to hours of rework on questions that should have been decided before the work started.

**Failure mode 2: False resolution**

Worse than silent gap-filling: the agent produces confident-sounding analysis of an open question in a way that makes the question look resolved.

"The most appropriate approach here would be event-based invalidation, as it provides consistency guarantees that time-based TTL cannot."

This is a reasonable argument. It's also a position the agent has adopted without knowing that you're blocked on the Q3 webhook capacity decision that determines whether event-based invalidation is even feasible. If you don't recognize that this is addressing an open question rather than an established fact, you might proceed based on analysis that doesn't account for your actual constraints.

## The protocol

The open questions protocol has three components: a structured list, a consistent format, and a maintenance habit.

### 1. The list

Keep open questions in a dedicated section of your session-state note. Not mixed with to-dos. Not buried in the middle of a project description. A clearly labeled, standalone list.

```markdown
## Open Questions

- [ ] Auth error response format: 401+WWW-Authenticate vs 403+JSON body
      Impact: frontend error handling, API consumer expectations
      Blocked on: discussion with frontend team (scheduled 2026-04-25)

- [ ] Cache invalidation strategy: TTL vs event-based
      Impact: data consistency SLA, infrastructure complexity
      Blocked on: Q3 roadmap decision on webhook capacity

- [ ] Internal service calls: route through gateway or bypass?
      Impact: latency, observability, gateway load
      Not blocked — can be decided now, needs decision

- [x] Database: Postgres vs MongoDB — RESOLVED 2026-04-12
      Decision: Postgres (see [[Decision: Database Selection]])
```

The `[ ]` / `[x]` markers tell the agent at a glance: unresolved vs resolved. The "blocked on" line tells it what would resolve the question. The resolved entry with a link to the decision log closes the loop.

### 2. The format

Each open question entry needs four pieces:

**The question itself** — specific, not vague. Framed as a decision between named options where possible.

**The impact** — what changes depending on how it resolves. This tells the agent which parts of the current work are downstream of this decision and should be treated as provisional.

**The blocker** (if any) — what information or event would resolve it. If there's no blocker, the question can be decided now.

**The status** — open, blocked, or resolved. Resolved questions should link to the decision log entry that captured the final choice and reasoning.

### 3. The maintenance habit

Open questions require two updates, not one:

**When a question is added:** Write it in full format. Don't just add "figure out caching" — write the structured entry.

**When a question is resolved:** Don't just check it off. Write the decision log entry that captures what was decided, why, and what alternatives were rejected. Then link the resolved question to that entry. The check-off without the decision log means the reasoning disappears.

The resolution is as important as the question. An AI that knows "cache invalidation: RESOLVED" without knowing *what was decided and why* will still make inconsistent choices downstream.

## How the AI uses this

When the open questions list is in your session-state note and your `CLAUDE.md` entry file points to session-state, the agent reads the list at the start of every session.

The effect is specific and measurable:

- Questions marked `[ ]` are treated as unresolved. The agent won't make implicit decisions about them.
- Questions with "blocked on" entries are flagged if work touches them. The agent will surface the dependency rather than proceeding through it.
- Resolved questions with decision log links can be referenced when adjacent decisions come up — "we chose Postgres; see [[Decision: Database Selection]] for the tradeoffs evaluated."

The agent stops filling gaps silently because it knows which gaps are genuinely open and which have been closed.

## A note on question volume

The protocol breaks down if you have 40 open questions. At that point, the list is noise rather than signal.

Keep the list to questions that are actively shaping current work — the decisions whose resolution (or non-resolution) affects what gets built in the next few sessions. Questions that are genuinely deferred to a later phase should be in a "deferred decisions" section, not the active open questions list.

A healthy session-state has 3–7 open questions. More than that usually means some of them should be deferred or are already implicitly resolved and just haven't been written down.

## The bigger picture

The open questions protocol is one piece of a session-state system. The full session-state covers: objective, active constraints, decisions made (with rejected alternatives), open questions, and next step.

The open questions section is the one most people skip initially — and the one that produces the most visible improvement in AI session quality when added.

---

The Obsidian vault template that includes the full session-state format, open questions protocol, decision log template, and hub structure is $49.

→ https://pharosml.gumroad.com/l/kvbhdo

$299 guided setup. $2,500 for teams.

If your AI sessions produce work you then have to revise because of implicit decisions the agent made, the open questions list is almost certainly the missing piece.

## Related

- [[Research and Papers MOC]]
- [[hashnode-iter34-skill-guides]]
