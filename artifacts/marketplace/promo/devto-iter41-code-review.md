---
type: artifact
title: Why AI Code Review Keeps Flagging the Wrong Things (and How to Fix It)
tags:
- artifact
- ai
- artifacts
- marketplace
- code
- auth
- rejected
- debt
- suggest
status: preserved
created: '2026-06-21'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/promo/devto-iter41-code-review.md
backlink_count: 3
backlinks:
- '[[Areas/Writing/Research and Papers MOC]]'
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
- '[[artifacts/marketplace/promo/hashnode-iter34-skill-guides]]'
---

# Why AI Code Review Keeps Flagging the Wrong Things (and How to Fix It)

**Platform:** Dev.to
**Iteration:** 41 — Cycle 10
**Angle:** Developer pain-point — AI code review without context produces generic noise
**Tags:** ai, programming, devtools, claudeai
**Status:** READY TO POST

**Instructions:** Log into dev.to → New Post → paste content below → add tags: ai, programming, devtools, claudeai → publish.

---

AI code review has a consistent failure mode: it surfaces generic issues and misses the ones that actually matter for your project.

You paste a function. The AI flags potential null pointer issues, suggests adding error logging, recommends extracting a constant. These are fine observations — for a codebase it knows nothing about. But it misses the actual problem: this function violates the constraint that all auth-path operations must complete under 200ms, which you established three months ago when you separated the auth layer from the API gateway.

The AI didn't miss this because it's bad at code review. It missed it because you never told it the constraint existed.

## What AI code review is actually reviewing

When you paste code for review without context, the AI is doing generic static analysis with pattern matching against common issues. It's reviewing your code against:

- General best practices for the language
- Common error patterns it's seen in training
- Standard code quality heuristics

It is not reviewing against:
- Your architectural decisions
- Your explicit constraints
- The alternatives you already ruled out and why
- The tech debt you're intentionally carrying
- The SLA requirements that define what "good" looks like for this specific function

The gap between "generic code review" and "project-aware code review" is the difference between a smart stranger looking at your code and a teammate who's been on the project for six months.

## The four things AI code review doesn't know without you

**1. Architectural decisions that constrain "correct"**

Your auth layer is separate from the API gateway. Any suggestion that couples them is wrong — not because coupling is bad in general, but because you've decided it's wrong for this project for specific reasons (independent scaling, latency isolation, deploy cycle separation).

Without knowing this, the AI will periodically suggest approaches that violate your architecture. These suggestions look reasonable in isolation.

**2. Intentional tech debt**

You have a known N+1 query in the profile endpoint. You know about it. You've decided to fix it in Q3 when you migrate to the new data layer. Until then, don't touch it.

Without knowing this, the AI will flag it every time you paste code that touches the profile endpoint. You'll spend time explaining why you're not fixing it right now.

**3. Non-obvious constraints**

Your application runs on Cloudflare Workers. There's no filesystem. No long-running processes. Any suggestion that involves either of those is invalid — not occasionally, but categorically, for every function in the codebase.

Without knowing this, the AI will suggest solutions that are architecturally impossible for your deployment target.

**4. Rejected alternatives**

You evaluated three caching strategies last month. Two were ruled out for specific reasons. The AI doesn't know this. It will suggest one of the rejected approaches as a "potential improvement."

Without knowing this, you'll spend time re-evaluating an approach you already rejected.

## The fix: a context file for code review

Before asking for code review, give the AI a context file. Not a full architecture document — a focused summary of what the AI needs to review correctly.

```markdown
# Code Review Context — [Project Name]

## Architecture Constraints
- Auth layer is separate from API gateway (independent scaling + latency isolation)
  - Do NOT suggest coupling these
- Deployment: Cloudflare Workers (no filesystem, no long-running processes, no Node.js APIs)
  - Any suggestion requiring filesystem or persistent process is invalid

## Performance Requirements
- Auth-path endpoints: < 200ms P95
- Data-path endpoints: < 500ms P95
- Flag anything that adds synchronous operations on the hot path

## Known Tech Debt (Do Not Flag)
- N+1 query in profile endpoint — tracked, fixing in Q3 migration
- Legacy error format in /api/v1/* routes — maintained for backwards compat

## Rejected Approaches
- In-memory caching: rejected — Workers are stateless, cache doesn't persist between requests
- Unified middleware: rejected — couples auth and data deploy cycles
- Session tokens in KV: rejected — doesn't meet compliance requirements

## What to Focus On
- Correctness against the constraints above
- Edge cases specific to the Cloudflare Workers runtime
- Anything that violates the auth/data separation
```

With this context loaded, the AI reviews against your actual project requirements. It won't suggest unified middleware — it knows that was rejected. It won't suggest filesystem operations — it knows the deployment target. It will flag the 200ms constraint violation you actually need to catch.

## Where this lives in a structured knowledge system

If you're using a knowledge vault for project context, the code review constraints belong in your active constraints note — the same one your `CLAUDE.md` points to for every session.

```markdown
# Active Constraints — [Project Name]

## Deployment
- Cloudflare Workers only — no filesystem, no persistent processes

## Performance
- Auth path: < 200ms P95
- Data path: < 500ms P95

## Architecture (locked decisions)
- Auth layer separate from API gateway (see [[Decision: Auth Layer Separation]])
- No unified middleware (see [[Decision: API Gateway Architecture]])

## Known Tech Debt (intentional, do not flag)
- N+1 query in profile endpoint — scheduled for Q3 migration
```

When this note is linked from your project hub and the `CLAUDE.md` points to the hub, the agent reads the constraints before every session — including code review sessions. You don't have to paste the context file manually each time.

## The shift in review quality

Code review without project context: generic, noisy, misses architectural violations, surfaces known tech debt as new findings.

Code review with project context: project-specific, accurate, flags actual violations of your constraints, respects intentional debt decisions.

Same model. Same code. Different context.

---

The vault structure that maintains this context automatically — active constraints note, decision logs with rejected alternatives, hub template, session-state — is packaged as a $49 Obsidian template.

→ https://pharosml.gumroad.com/l/kvbhdo

$299 guided setup for teams who want it configured for their specific stack. The code review context pattern above is one of eight note types included in the template.

## Related

- [[Research and Papers MOC]]
- [[hashnode-iter34-skill-guides]]
