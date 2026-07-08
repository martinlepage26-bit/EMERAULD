---
type: artifact
title: 'The Active Constraints Note: The One File That Stops AI from Violating Your Project Rules'
tags:
- artifact
- ai
- artifacts
- marketplace
- constraints
- constraint
- entries
- locked
- doesn
status: preserved
created: '2026-06-21'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/promo/hashnode-iter46-active-constraints.md
backlink_count: 3
backlinks:
- '[[Areas/Writing/Research and Papers MOC]]'
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
- '[[artifacts/marketplace/promo/hashnode-iter34-skill-guides]]'
---

# The Active Constraints Note: The One File That Stops AI from Violating Your Project Rules

**Platform:** Hashnode
**Iteration:** 46 — Cycle 11
**Angle:** Single artifact deep-dive — active constraints note type, format, four categories, maintenance
**Tags:** obsidian, ai, knowledge-management, developer-tools, claudeai
**Status:** READY TO POST

**Instructions:** Log into hashnode.com → Write → paste content below → tags: obsidian, ai, knowledge-management, developer-tools, claudeai → publish to your blog.

---

Every project has rules the AI doesn't know about.

Not requirements — those are usually in the spec. Not goals — those are in the brief. Rules: the non-obvious constraints that have accumulated through decisions, negotiations, discoveries, and hard lessons. The things that would make a suggestion wrong for this specific project even if it's correct in general.

"We can't use filesystem access — we're on Cloudflare Workers."  
"The client's lawyers said no to storing any data outside Canada."  
"We decided not to add new npm dependencies until after the security audit."  
"That approach would violate the auth layer separation we locked in March."

An AI agent working without these constraints will violate them regularly. Not through incompetence — through ignorance. It suggests what makes sense in general, not what's permitted in your specific context.

The active constraints note is the fix. One file per project. Updated as constraints change. Loaded before every session.

---

## What a constraint is (and isn't)

**A constraint is not a goal.** "Build a fast API" is a goal. "All auth-path endpoints must complete under 200ms P95" is a constraint — it has a specific threshold and a defined scope.

**A constraint is not a requirement.** "Support user authentication" is a requirement. "Use our existing SSO provider — no building a new auth system" is a constraint — it rules out a class of solutions.

**A constraint is not a preference.** "I like TypeScript" is a preference. "TypeScript only — no JavaScript files in this repo, enforced by CI" is a constraint.

The distinction matters because constraints do a specific job: they tell the agent what it *cannot* do, not just what it should do. A well-written constraints file eliminates entire solution spaces before the agent starts proposing solutions.

---

## The four constraint categories worth capturing

### 1. Deployment and infrastructure constraints

What the runtime environment rules out.

```markdown
## Deployment Constraints
- Runtime: Cloudflare Workers
  - No filesystem access
  - No long-running processes (max 30s execution)
  - No Node.js built-ins (fs, path, child_process, etc.)
  - Memory limit: 128MB per request
- Database: Supabase (Postgres) only — no other data stores
- Storage: R2 for files — no S3, no local disk
```

These are the constraints that produce the most frustrating errors when missed: suggestions that look architecturally sound but are fundamentally incompatible with where the code runs.

### 2. Compliance and regulatory constraints

What legal, policy, or contractual obligations rule out.

```markdown
## Compliance Constraints
- Data residency: Canada only — no data storage on US-only infrastructure
  (PIPEDA obligation, confirmed with counsel 2026-02-14)
- Client NDA: no third-party AI APIs on client data
  (covers all data in the /client-data/ namespace)
- Accessibility: WCAG 2.1 AA minimum — no exceptions for UI components
- EU AI Act: deferred — out of scope until v2 launch
  (see [[Decision: EU AI Act Scope]])
```

The "deferred" entries are as important as the active ones. They tell the agent not to flag EU AI Act compliance issues — you know, you've decided to handle it later, and re-raising it every session is noise.

### 3. Architectural constraints (locked decisions)

Design decisions that are settled and should not be re-evaluated.

```markdown
## Architectural Constraints (Locked)
- Auth layer is separate from the API gateway
  Reason: independent scaling, latency isolation, separate deploy cycles
  Do not suggest coupling these. (see [[Decision: Auth Layer Separation]])

- No unified middleware
  Reason: couples auth and data deploy cycles, adds latency on every request
  Rejected 2026-03-12. (see [[Decision: API Gateway Architecture]])

- Session tokens not stored in KV
  Reason: compliance — doesn't meet data handling requirements
  Rejected 2026-02-28. (see [[Decision: Session Token Storage]])
```

These entries link to the decision log for full reasoning. The constraints file carries the summary; the decision log carries the argument. The agent reads the constraint, sees it's locked, and doesn't re-open the discussion.

### 4. Scope and boundary constraints

What's explicitly out of scope for this phase, this project, or this engagement.

```markdown
## Scope Constraints (Current Phase)
- Mobile app: out of scope until v2 — do not suggest mobile-specific patterns
- Internationalization: English only for now — no i18n infrastructure
- Analytics: no tracking beyond server-side logging — privacy decision, not revisiting
- New npm dependencies: require explicit approval — bundle size constraint
  (current budget: 180kb gzipped)

## Out of Scope (Flagged, Do Not Raise Again)
- Multi-tenant architecture: decided against for v1, revisit at 1000 users
- GraphQL: REST only for this project, team preference + operational simplicity
- Microservices: monolith for now, explicit decision, not a gap to fix
```

The "Do Not Raise Again" section is the one that saves the most conversational overhead. If the agent keeps suggesting GraphQL and you keep saying no — write it down. Once it's in the constraints file, the agent stops suggesting it.

---

## The format

```markdown
# Active Constraints — [Project Name]

**Last updated:** [date]
**Project hub:** [[Project Hub]]

## Deployment and Infrastructure
[entries]

## Compliance and Regulatory
[entries]

## Architectural (Locked Decisions)
[entries — each with link to decision log entry]

## Scope Boundaries
[entries]

## Do Not Raise Again
[entries — patterns the agent keeps suggesting that are explicitly off the table]
```

Keep each entry to 2–3 lines max. One line for the constraint, one line for the reason, one line for the reference if applicable. The constraints file should be scannable in under two minutes — if it takes longer, it's too detailed.

---

## How to populate it (and keep it current)

**Populate it before the first session**, not after. Work backwards from what you already know:

- What deployment environment constraints exist?
- What decisions were made before this project started that the agent should know?
- What's explicitly not in scope?
- What have you had to explain multiple times in past sessions?

That last question is the fastest route to a complete constraints file. If you've explained something three times, it belongs in the constraints note.

**Update it when:**
- A new constraint is discovered (often through an AI suggestion that violates it)
- A decision is locked (move it from session-state's "decisions made" to the constraints file)
- A scope boundary changes (add the new boundary, mark the old one as superseded)
- A constraint is lifted (remove it and note why it no longer applies)

**Remove entries when they no longer apply.** A stale constraints file is worse than none — the agent will follow outdated rules and miss current ones. Date your entries so you can see which ones haven't been reviewed recently.

---

## Where it connects

The active constraints file is one of three files the agent reads before every session:

```
CLAUDE.md
  → [[Project Hub]]
       → [[Active Constraints]] ← the constraints file
       → [[Session State]]      ← current position and next step
       → [[Decision Log]]       ← historical decisions + rejected alternatives
```

The constraints file and the decision log work together. The constraints file carries the current rules. The decision log carries the reasoning for why those rules exist. When a constraint is questioned (sometimes legitimately — constraints do become outdated), the decision log shows whether the original reasoning still applies.

---

## What changes when this file exists

Without a constraints file, every session has a tax: the agent proposes something reasonable in general but wrong for your project, you correct it, it proposes another variation, you correct again.

With a constraints file loaded before every session:

- The agent doesn't propose Cloudflare-incompatible solutions because it knows the runtime
- It doesn't re-suggest unified middleware because it's explicitly locked out
- It doesn't raise mobile architecture because it knows that's a v2 concern
- It doesn't flag GraphQL as a missing feature because it knows you chose REST deliberately

The proposals it makes are pre-filtered against your actual constraints. First-pass suggestions are more often usable. Sessions spend less time correcting and more time building.

---

The vault template that includes the active constraints format, decision log, hub structure, and session-state protocol — pre-wired to work together — is $49.

→ https://pharosml.gumroad.com/l/kvbhdo

$299 guided setup — I configure the constraint categories for your specific project type (SaaS, client services, research, etc.). The constraints file varies more by project type than any other note, so a configured template saves meaningful setup time.

## Related

- [[Research and Papers MOC]]
- [[hashnode-iter34-skill-guides]]
