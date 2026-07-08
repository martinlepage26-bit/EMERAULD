---
type: artifact
title: How to Architect AI Agent Memory That Survives Context Window Limits
aliases:
- artifacts/marketplace/promo/devto-iter33-architecture-guide
tags:
- artifact
- ai
- agents
- artifacts
- marketplace
- traversal
- rejected
- project
- alternatives
- zone
- color-orange
status: preserved
created: '2026-06-21'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/promo/devto-iter33-architecture-guide.md
backlink_count: 3
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
- '[[artifacts/marketplace/promo/hashnode-iter34-skill-guides]]'
---

# How to Architect AI Agent Memory That Survives Context Window Limits

**Platform:** Dev.to  
**Iteration:** 33 — Cycle 8  
**Angle:** Technical architecture guide — graph traversal over flat-file retrieval  
**Tags:** ai, obsidian, devtools, claudeai  
**Status:** READY TO POST

**Instructions:** Log into dev.to → New Post → paste content below → add tags: ai, obsidian, devtools, claudeai → publish.

---

The most common advice for giving Claude Code project context: write a `CLAUDE.md` file. Put your architecture decisions, tech stack, constraints, and current state in there. Keep it updated.

This works until it doesn't.

Past about 300 tokens, attention dilutes. The most relevant constraint competes with everything else in the file. You end up with a `CLAUDE.md` that's 2,000 lines long and still misses context you need. The agent reads the whole thing and effectively prioritizes the first third.

The fix isn't a better `CLAUDE.md`. It's a different retrieval architecture.

## The core problem: retrieval, not storage

When you give an agent a long flat file, the retrieval model is "read everything." That's fine for small amounts of context. For anything beyond a few hundred tokens, it degrades — not because the model is bad, but because you're asking it to find a needle in a haystack it has to read start-to-finish.

The architecture that works is **graph traversal**: the agent starts from a short entry point and follows links to reach relevant context. Three hops covers anything specific. You never load everything at once.

## The three-zone structure

```
raw/              ← unsynthesized captures (never modified by the agent)
wiki/             ← synthesized, linked knowledge notes
session-state.md  ← live operational context per project
CLAUDE.md         ← 50-line entry point → graph
```

**Zone 1: `raw/`**

Captures go here exactly as written — meeting notes, paste-ins, half-formed thoughts. The agent knows this is staging material, not established knowledge. It can reference it but should never reason from it as settled fact.

**Zone 2: `wiki/`**

Synthesized notes only. Each note requires at least two inline `[[links]]` — not a trailing "Related" section, but links woven into the body where the connection is actually made. This creates the traversal graph.

**Zone 3: `session-state.md`**

Five fields, updated at every session close:

```markdown
## Objective
What this project is trying to accomplish.

## Active Constraints
- Deployment: Cloudflare Workers only (no Node.js runtime)
- Compliance: PIPEDA in scope; EU AI Act deferred to v2
- Timeline: Revenue-positive by June 22

## Decisions Made
- API gateway scoped separately from auth layer
  (reasons: latency isolation, independent scaling)
- Rejected: unified middleware — couples deploy cycles,
  adds latency on every data request

## Open Questions
- [ ] Whether to proxy through gateway on internal calls
      (UNRESOLVED — blocker for /auth/verify implementation)
- [ ] Caching strategy for user profile endpoint

## Next Step
Write /api/auth/verify endpoint spec.
Internal proxy question must be resolved first.
```

## The CLAUDE.md entry pattern

The entry file is not where context lives. It's where traversal starts.

```markdown
# Project: [Name]

## Current State
→ Read [[Session State — Project Name]] for live context.

## Architecture
→ [[Project Hub]] — technical decisions entry point
→ [[Active Constraints]] — non-obvious limits in effect
→ [[Decision Log Index]] — decisions made + alternatives rejected

## Quick Context
- Stack: React 18 + FastAPI + MongoDB + Cloudflare Pages
- Repo: ~/repos/project-name
- Deploy: `npm run build && wrangler publish`

## Agent Behavior
Read session-state first. Follow links to relevant context
before proposing solutions. Do not re-propose options listed
in "Alternatives Rejected" in any decision log.
```

~50 lines, ~400 tokens. The agent reads this, then follows links to retrieve exactly what it needs. Context in 2–3 hops; never loads everything.

## The decision log — highest ROI note type

```markdown
# Decision: [Title]

**Date:** 2026-03-12  
**Status:** Locked

## Decision
[What was decided]

## Reasoning
[Why this approach. The non-obvious parts.]

## Alternatives Rejected
- [Option A]: rejected because [specific reason]
- [Option B]: rejected because [specific reason]

## Open Questions
- [ ] [Anything still unresolved about this decision]
```

The "Alternatives Rejected" section is what earns the most. When this note is linked from the project hub, the agent reads it before proposing anything. It doesn't re-propose Option A — it already knows why you said no.

Without this record: the agent periodically re-proposes rejected approaches because the reasoning that ruled them out only existed in a closed chat window.

## The mandatory linking rule

Every `wiki/` note requires at least two inline `[[links]]`. Not links in a trailing section — links woven into the body where the connection is made.

This isn't aesthetic. A note with no backlinks is an orphan: the agent can't traverse to it. Your decision log doesn't exist to the agent if nothing links to it.

The enforcement pattern that works: **hub templates** that scaffold the link structure before you fill in content.

```markdown
# [[Project Name]] Hub

## Current State
→ [[Session State — Project Name]]

## Technical Architecture
→ [[Architecture Overview]]
→ [[Active Constraints]]
→ [[API Design Decisions]]

## Open Work
→ [[Sprint Log]]
→ [[Open Questions — Project Name]]

## Key People
→ [[Client Name]]
→ [[Stakeholder Name]]
```

Hub creates entry points. Entry points create traversal paths. Traversal paths mean context reaches the agent without the agent reading everything.

## Optional: local runtime for offline or local-model use

For Ollama / LM Studio / llama.cpp workflows, the vault ships with a Python runtime:

**`setup.sh`** — installs deps, builds the vector index:
```bash
pip install sentence-transformers
python embed.py   # ~2 min for 200+ notes, all-MiniLM-L6-v2
```

**`ask.py`** — hybrid query (vector similarity + backlink traversal):
```bash
python ask.py "what constraints apply to the auth module?"
python ask.py "what did we decide about the API gateway?" --top 5
python ask.py "current project state" --full
```

**`vault_watcher.py`** — watches for new notes, updates index on save.

Why hybrid? Vector similarity retrieves semantically close notes; backlink traversal then widens the result by following links from those notes. You get related content by meaning *and* by structure — chunks with relationships, not just chunks.

Runs fully on-device. No cloud required.

## Results

After 212 notes and six months daily use:

| Metric | Before | After |
|--------|--------|-------|
| Session startup | 15 min | 90 sec |
| Re-proposed rejected approaches | Weekly | Never |
| Handoff cost on context-switch | Full re-briefing | Read the hub |

Same model. Different retrieval architecture.

## The skeleton

The vault — note types, hub templates, decision-log format, skill guides, session-state protocol, and local runtime — is packaged as a $49 Obsidian template.

→ https://pharosml.gumroad.com/l/kvbhdo

Also: $299 guided setup (structure configured for your specific project type), $2,500 for teams who want a shared memory layer.

The architecture above is the complete system. The template is six months of iteration baked into a skeleton you can drop into an existing Obsidian vault in an afternoon.

## Related

- [[Governance and PHAROS MOC]]
- [[hashnode-iter34-skill-guides]]
