---
type: artifact
title: Writing Notes for AI, Not for Humans — The Structural Differences That Matter
aliases:
- artifacts/marketplace/promo/hashnode-iter38-writing-for-ai
tags:
- artifact
- ai
- artifacts
- marketplace
- auth
- know
- wrote
- middleware
- gateway
- color-red
status: preserved
created: '2026-06-21'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/promo/hashnode-iter38-writing-for-ai.md
backlink_count: 3
backlinks:
- '[[Areas/Writing/Research and Papers MOC]]'
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
- '[[artifacts/marketplace/promo/hashnode-iter34-skill-guides]]'
---

# Writing Notes for AI, Not for Humans — The Structural Differences That Matter

**Platform:** Hashnode
**Iteration:** 38 — Cycle 9
**Angle:** Structural shift — how AI-readable notes differ from human-readable ones
**Tags:** obsidian, ai, knowledge-management, developer-tools, claudeai
**Status:** READY TO POST

**Instructions:** Log into hashnode.com → Write → paste content below → tags: obsidian, ai, knowledge-management, developer-tools, claudeai → publish to your blog.

---

When you write a note for yourself, you're writing for a reader who shares your context. You know what project this belongs to. You know what decisions led here. You know which parts are settled and which are still open. You can afford shorthand, partial sentences, and cryptic titles — because future-you will remember enough to fill in the gaps.

When you write a note for an AI agent, none of that applies.

The agent has no background context unless you give it explicitly. It can't distinguish a locked decision from a half-formed hypothesis. It treats a note you wrote in 2023 with the same authority as one you wrote yesterday. It doesn't know what "the auth problem" means unless you've defined it somewhere the agent can read.

This shift — writing for AI, not just for yourself — changes five things about how notes should be structured.

## 1. Titles must be precise, not evocative

Human note titles are often shorthand: "auth thoughts," "meeting notes weds," "the middleware question."

These work for humans because you remember what "the middleware question" referred to when you wrote it. An agent searching your vault for information about your API architecture doesn't know that "the middleware question" is the relevant note. It can't make that inference.

**AI-readable titles are descriptive and complete:**
- ❌ "the middleware question"
- ✅ "Decision: API Gateway vs Unified Middleware — 2026-03-12"

- ❌ "auth thoughts"
- ✅ "Auth Layer Design — Options Evaluated and Approach Selected"

- ❌ "meeting notes weds"
- ✅ "Meeting: Client Kickoff — Scope Decisions and Blockers — 2026-04-10"

The rule: a title should tell an agent what the note contains without requiring the agent to read it first. If the title is accurate enough that the agent could decide whether to read the note from the title alone, it's good.

## 2. Summaries must establish context from scratch

Human notes often start mid-thought: "continuing from last session, we decided to…" or "as discussed, the main concern is…"

These work when you wrote the note immediately after the context that produced it. They fail for an agent that reads the note six months later in isolation.

**AI-readable summaries are self-contained:**

```markdown
## Summary
The decision to scope the API gateway separately from the auth layer was made on
2026-03-12. This was driven by latency isolation requirements: the auth path and
the data path have different SLA targets, and coupling them would force shared
deploy cycles. See [[API Gateway Architecture]] for the full design, and
[[Active Constraints — PHAROS]] for the SLA requirements that motivated this.
```

Every summary should answer: who, what, when, why, and what it connects to — without assuming the reader knows any of the background.

If a summary requires prior context to make sense, it's a human note, not an AI note.

## 3. Status and currency must be explicit

Humans navigate note age intuitively. You know roughly when you wrote something, and you know whether the situation has changed. You treat a three-year-old design note with appropriate skepticism.

An agent doesn't. It treats a superseded decision with the same authority as a current one unless you tell it otherwise.

**Add explicit status markers:**

```markdown
---
status: active      # agent can act on this
created: 2026-04-10
updated: 2026-04-18
---
```

```markdown
---
status: superseded
superseded_by: "[[Decision: Auth Layer v2 — 2026-04-15]]"
---
```

```markdown
---
status: draft       # agent should treat as tentative, not settled
---
```

These aren't bureaucratic metadata — they're instructions. When the agent encounters a note with `status: superseded`, it knows to find the current version rather than act on stale content.

## 4. Evidence must be separated from inference

When humans write notes, we naturally blend observation and interpretation: "the API is slow because the database queries aren't indexed." You know that "because" is an inference, not a confirmed fact.

An agent treats "the API is slow because the database queries aren't indexed" as established fact. It won't flag the reasoning gap. It will act on your inference as if it were confirmed.

**Separate evidence from inference explicitly:**

```markdown
## Observation
API response times averaging 800ms under load (measured: 2026-04-18, load test logs in raw/perf-2026-04-18.md).

## Hypothesis
Likely cause: N+1 query pattern in the user profile endpoint (see [[Profile Endpoint Design]]).
Unconfirmed — needs query plan analysis before acting.

## Open Question
- [ ] Run EXPLAIN ANALYZE on profile queries to confirm or rule out N+1
```

The agent now knows: the slow API is a fact; the cause is a hypothesis; analyzing the query plan is the next step. It won't jump to "add indexes" before confirming the diagnosis.

## 5. Links must carry meaning, not just exist

Human notes often have a trailing "see also" or "related" section — a dump of links that might be useful. You know which ones are actually relevant and which you added speculatively.

For an agent, all links in a note carry equal weight. A speculative link to a loosely related note is treated the same as a link to the most important adjacent concept.

**Contextual links in the body beat link dumps at the end:**

❌ This pattern (link dump):
```markdown
## Related

- [[Auth Layer Design]]
- [[API Gateway Architecture]]
- [[Database Schema v3]]
- [[Meeting: Client Kickoff]]
- [[Performance Requirements]]
```

✅ This pattern (contextual):
```markdown
The decision to use a separate auth layer (see [[Auth Layer Design]]) was driven by the
SLA requirements in [[Performance Requirements]], specifically the 200ms target for
auth-path requests. The [[API Gateway Architecture]] handles routing between the two
layers. The client's requirements that set these targets came from [[Meeting: Client Kickoff]].
```

The contextual version tells the agent *why* each linked note is relevant — and in what order to traverse them if it needs to go deeper.

- [[Research and Papers MOC]]
- [[hashnode-iter34-skill-guides]]
## The compound effect

These five changes — precise titles, self-contained summaries, explicit status, separated evidence, contextual links — don't just make individual notes better. They make the vault traversable.

An agent navigating a vault of well-structured notes can reach accurate, current, relevant context in two or three hops. An agent navigating a vault of human-optimized notes gets partial information, outdated content mixed with current, inferences treated as facts, and orphan notes it can't discover because nothing links to them meaningfully.

The structural shift is a one-time investment per note. Once you've written a note for AI, it stays AI-readable. The compounding happens automatically as the vault grows.

## What changes in practice

You don't need to rewrite your existing vault overnight. Start with the notes the agent reads most often — the project hub, the active constraints, the session state, the key decision logs.

Apply these five rules to those notes first. Watch what happens to the quality of your AI sessions. The investment is a few hours of revision; the return is sessions that start with real context instead of re-explanation.

---

The Obsidian vault template I use enforces these patterns from the start — note types, hub templates, frontmatter schemas, and linking rules that build AI-readability into the structure before you fill in content.

→ https://pharosml.gumroad.com/l/kvbhdo

$49 template. $299 guided setup. $2,500 for teams.

If you're using Obsidian as an AI memory layer and your sessions still feel like briefings, the notes are probably written for you, not for the agent.
