---
type: artifact
title: The 3 Notes Every AI-Assisted Project Needs Before the First Session
aliases:
- artifacts/marketplace/promo/devto-iter37-three-notes
tags:
- artifact
- ai
- artifacts
- marketplace
- projectname
- session
- project
- minutes
- guides
- color-orange
status: preserved
created: '2026-06-21'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/promo/devto-iter37-three-notes.md
backlink_count: 3
backlinks:
- '[[Areas/Writing/Research and Papers MOC]]'
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
- '[[artifacts/marketplace/promo/hashnode-iter34-skill-guides]]'
---

# The 3 Notes Every AI-Assisted Project Needs Before the First Session

**Platform:** Dev.to
**Iteration:** 37 — Cycle 9
**Angle:** Prescriptive quick-win — 3 specific files to create right now, no system required
**Tags:** ai, obsidian, productivity, claudeai
**Status:** READY TO POST

**Instructions:** Log into dev.to → New Post → paste content below → add tags: ai, obsidian, productivity, claudeai → publish.

---

Most advice about AI context management assumes you're building a full system. Vault architecture, note types, skill guides, linking rules — useful eventually, but a lot to absorb before you've even started.

This is the minimal version. Three notes. You can create them in 20 minutes. They'll cut your session startup time in half before you've built anything else.

## Note 1: The project hub

One file per project. Call it `[ProjectName] Hub.md`. Put it somewhere you'll remember.

Contents:

```markdown
# [Project Name] Hub

## What This Is
One sentence. What this project is trying to accomplish.

## Current State
What's true right now. Not the goal — the present position.
- What's built / done
- What's in progress
- What's blocked

## Stack / Environment
The non-obvious technical details:
- Language/framework versions
- Deployment target
- Key external dependencies
- Anything that constrains how the AI should suggest solutions

## Key Files
The 3–5 files the AI should know about. Paths, not descriptions.

## Links
→ [[Active Constraints — Project Name]]
→ [[Session State — Project Name]]
```

This is the file your `CLAUDE.md` (or equivalent) points to. Instead of loading everything at once, the agent reads the hub and follows links to what it needs.

Keep it under 100 lines. If it grows past that, the project needs a more structured setup — but for most projects, this is enough.

## Note 2: Active constraints

A separate file: `Active Constraints — [ProjectName].md`.

This is the note that earns its keep fastest. It captures the non-obvious rules — the ones an agent wouldn't know from reading your code, and that you've been re-explaining at the start of every session.

```markdown
# Active Constraints — [Project Name]

## Deployment
- [e.g. Cloudflare Workers only — no Node.js filesystem access]
- [e.g. Must stay within free tier limits for now]

## Compliance / Legal
- [e.g. PIPEDA in scope — no US-only data storage]
- [e.g. Client NDA — no third-party AI APIs on their data]

## Technical
- [e.g. No new dependencies without approval — bundle size constraint]
- [e.g. Postgres only — no other databases]

## Timeline
- [e.g. Hard launch: June 22 — no scope creep past MVP definition]

## Explicitly Out of Scope (This Phase)
- [Thing you keep getting asked about that's intentionally deferred]
- [Another deferred decision]
```

The "Explicitly Out of Scope" section is the one most people skip. It's also the one that saves the most time. When the agent suggests something you've already decided not to do this phase, you need to be able to say "it's in the out-of-scope list" rather than re-arguing the point.

Fill this in before your first session. Update it whenever a constraint changes or a scope decision gets made.

## Note 3: Session state

One file per project: `Session State — [ProjectName].md`. Five fields. Update it at the end of every session. Read it at the start of the next one.

```markdown
# Session State — [Project Name]

**Last updated:** [date]

## Objective
[What this project is currently trying to accomplish — may be more specific than the hub]

## Decisions Made
- [Decision]: [brief reason why]
  - Rejected: [alternative] — [why it was ruled out]
- [Another decision]

## Open Questions
- [ ] [Something explicitly unresolved — not a to-do, an open decision]
- [ ] [Another unresolved question]

## Blockers
- [Anything currently preventing forward progress]

## Next Step
[The exact action to take at the start of the next session. One sentence. Specific enough that the agent can start without clarification.]
```

The "Decisions Made" and "Open Questions" fields are the ones that matter most.

**Decisions Made** prevents re-litigation. When you write "Rejected: unified middleware — couples deploy cycles, adds latency on every data request," the agent reads that before suggesting anything architectural. It doesn't re-propose unified middleware. The no is on record.

**Open Questions** prevents silent gap-filling. Questions not marked open get filled in — by you with guesses, by the agent with plausible inference. Writing them down forces both of you to hold the uncertainty rather than pretend it doesn't exist.

**Next Step** is what makes session re-entry frictionless. Not "continue working on auth." Specific: "Write the /api/auth/verify endpoint spec. The internal proxy question is a blocker — resolve that first."

## Wiring it up

In your `CLAUDE.md` (or whatever entry file you use), add three lines:

```markdown
## Context
→ Read [[ProjectName Hub]] for current state and stack.
→ Read [[Active Constraints — ProjectName]] before proposing solutions.
→ Read [[Session State — ProjectName]] to understand where we are and what's next.
```

That's it. The agent reads the hub, checks constraints, loads current state. The session starts with context instead of a briefing.

## What this gets you

Without these three notes, every session opens cold. You re-explain the project. The agent suggests something you've already ruled out. You correct it. You remember a constraint at minute eight and add it to the prompt. You spend 15 minutes getting to useful work.

With these three notes, you read them at session open (2 minutes), the agent reads them too, and the session starts from current state. Not from zero.

That shift — from 15 minutes to 2 minutes — is the whole value. Everything else (full vault structure, skill guides, linked knowledge graph) is an amplification of this core pattern.

---

These three notes are part of a larger vault system I've been running for six months on a 212-note Obsidian vault. The full skeleton — note types, hub templates, decision-log format, linking rules, skill guides, session-state protocol, optional local runtime — is packaged as a $49 template.

→ https://pharosml.gumroad.com/l/kvbhdo

But you don't need the template to start. Create the three notes above this week. See what happens to your session startup time. Then decide if the larger system is worth building.

## Related

- [[Research and Papers MOC]]
- [[hashnode-iter34-skill-guides]]
