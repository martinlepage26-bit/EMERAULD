---
type: artifact
title: What breaks when your Obsidian vault passes 100 notes (and how to fix it)
tags:
- obsidian
- ai
- productivity
- knowledge-management
- developer-tools
- artifact
- artifacts
- marketplace
- happening
- decision
- symptom
- auth
- myproject
status: preserved
created: '2026-06-21'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/promo/hashnode-iter14-scaling.md
backlink_count: 3
backlinks:
- '[[Areas/Writing/Research and Papers MOC]]'
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
- '[[artifacts/marketplace/promo/hashnode-iter34-skill-guides]]'
subtitle: The scaling problems nobody warns you about — and the structural changes that solved them for a 212-note AI-agent vault.
published: false
---

# What breaks when your Obsidian vault passes 100 notes (and how to fix it)

The advice for starting an Obsidian vault is solid: capture everything, link related notes, build a hub for each project. It works. The vault grows. And somewhere around 80–120 notes, things start breaking in ways the getting-started guides don't cover.

Here's what actually breaks, and the structural fixes I landed on after hitting each problem in a 212-note vault I use daily with AI agents.

---

## Problem 1: Hub notes become unusable

**Symptom:** Your project hub note has 40+ links. Scrolling it feels like reading a sitemap. The agent loads it, gets 40 links, and doesn't know which 3 are relevant to the current task.

**What's happening:** Hub notes are designed to be entry points, not indexes. Past ~15 links, they stop functioning as navigation and start functioning as noise.

**Fix: Introduce Maps of Content (MOCs) as a second tier.**

A MOC sits between the hub and the individual notes. It indexes a *domain* within a project, not the whole project.

```
Project Hub — CompassAI
  → MOC: Evidence Lifecycle
      → Decision — Evidence Ingest Scope
      → Decision — Rate Limit Telemetry Scope
      → Active Constraints — Evidence API
      → Open Questions — Evidence Versioning
  → MOC: Auth and Security
      → Decision — Auth Layer Scope
      → Decision — Token Refresh Strategy
      → Active Constraints — Auth
```

The hub stays short (links to 4–6 MOCs). Each MOC indexes 5–10 notes in its domain. The agent traverses hub → relevant MOC → specific note rather than hub → 40 candidates.

**Rule of thumb:** Create a MOC when any section of your hub note exceeds 7 links.

---

## Problem 2: Decision logs become orphans

**Symptom:** You have 30 decision logs. The agent keeps surfacing decisions from 6 months ago as if they're current. Or it misses a recent decision because it isn't reachable via the traversal path.

**What's happening:** As volume grows, the hub-to-decision link chain breaks. A decision linked from a MOC that itself is buried 3 hops from the entry point effectively doesn't exist — the agent stops traversing at the hop limit.

**Fix: Status tags and a Decisions Index.**

Add a `status` field to every decision note frontmatter:

```yaml
---
type: decision
status: locked        # locked | superseded | under-review
superseded-by:        # link if status is superseded
date: 2026-03-12
---
```

Then create a `wiki/Decisions Index — MyProject.md` as a flat list of active decisions only:

```markdown
# Decisions Index — CompassAI

## Locked (authoritative)
- [[Decision — Auth Layer Scope]] · 2026-03-12
- [[Decision — Rate Limit Telemetry Scope]] · 2026-04-19
- [[Decision — DB Schema for Evidence Records]] · 2026-02-28

## Under Review
- [[Decision — Backend Hosting — Railway vs Hetzner]] · pending cost analysis

## Superseded (archived)
- [[Decision — Auth-in-Gateway]] → superseded by [[Decision — Auth Layer Scope]]
```

Link the Decisions Index from the hub. The agent loads it early in traversal, gets the current active decisions, and knows which ones are still authoritative. Superseded decisions still exist in the graph (for audit trail) but aren't surfaced as current.

---

## Problem 3: The linking discipline breaks under time pressure

**Symptom:** You start creating orphan notes. You're in the middle of something, you capture a decision fast, you skip the linking step. Two weeks later, the agent doesn't know that decision exists.

**What's happening:** The linking discipline ("every note needs 2+ inline links before saving") works when you have time. Under pressure, it's the first thing to drop.

**Fix: A weekly link-hygiene pass using a skill guide.**

Instead of trying to link perfectly in real time, run a 15-minute weekly pass with an explicit checklist:

```markdown
# Ariun — Linking Hygiene Skill Guide

When invoked, scan the vault for:
1. Notes with zero internal links
2. Notes with links only in a trailing "Related" section (not inline)
3. Notes created in the last 7 days not linked from any hub or MOC
4. Decision logs not appearing in the Decisions Index

For each finding:
- Add inline [[links]] to the body where connections exist
- Update the relevant hub or MOC to include the note
- If no related notes exist: create a minimal stub for the concept, then link
```

This is the Ariun skill guide from the vault template — a plain prose file the agent follows when invoked. Running it weekly catches the orphans before they accumulate.

---

## Problem 4: Raw captures contaminate the synthesis layer

**Symptom:** The agent starts reasoning from half-formed captures in `raw/` as if they're established facts. A raw note from a brainstorm session gets treated as a constraint.

**What's happening:** As `raw/` fills up, you start linking raw notes into `wiki/` before synthesizing them — "just temporarily" — and the distinction breaks down.

**Fix: Hard separation with an explicit synthesis queue.**

Keep `raw/` strictly write-only for the agent. The agent may read it for reference but should never cite it as established knowledge.

Add a `needs-synthesis` tag to raw notes when they're ready to be processed:

```yaml
---
type: raw
needs-synthesis: true
source: meeting-2026-04-19
---
```

Create `wiki/Synthesis Queue.md` — a manually maintained list of raw notes ready to become wiki entries:

```markdown
# Synthesis Queue

- [ ] `raw/meeting-2026-04-19-lavoie.md` → [[Lavoie — Client Note]]
- [ ] `raw/pharos-strategy-2026-04-18.md` → [[PHAROS Strategic Direction 2026]]
- [x] `raw/rhet-ai.md` → [[Rhétorique antique et IA]] ✓
```

The agent knows to treat `Synthesis Queue.md` as a processing backlog, not as knowledge. Items move off the queue only when a corresponding `wiki/` note exists with proper links.

---

## Problem 5: The CLAUDE.md entry file becomes stale

**Symptom:** The "Last session" line in your CLAUDE.md is 3 weeks old. The agent loads it, sees stale state, and either ignores it or treats it as current.

**What's happening:** The entry file is manual to update, so it drifts. Past a certain staleness threshold, it's worse than nothing — it gives the agent false confidence about recent context.

**Fix: Move volatile state out of CLAUDE.md and into a dedicated session log.**

```markdown
# CLAUDE.md — Entry Point

## Project
@wiki/Project Hub — MyProject.md

## Stack
TypeScript + Python · Cloudflare · MongoDB

## Session log
@wiki/Session Log — MyProject.md
```

The session log is a dated append-only file:

```markdown
# Session Log — CompassAI

## 2026-04-19
Added rate-limit telemetry to evidence ingest endpoint. Tests green (4/4).
Open: PR not yet pushed — no remote configured for CompassAI repo.

## 2026-04-17
Completed Fort Knox audit. Token RTW36 revoked and history-purged.
```

The agent loads the session log via the `@` reference and gets the last few entries without the CLAUDE.md itself needing to change. You append to the log, not edit the entry file.

---

## The pattern at scale

These fixes share a structure: **separate concerns that get conflated as volume grows.**

- Hubs vs. MOCs: navigation vs. indexing
- Current vs. superseded decisions: active state vs. historical record  
- Real-time linking vs. weekly hygiene: in-flow capture vs. graph maintenance
- Raw vs. synthesized: staging vs. knowledge
- Static entry vs. volatile session state: config vs. log

The vault architecture that works at 20 notes works differently at 200. The fixes above are the structural changes I made as each problem surfaced — not in advance, but in response to the specific failure.

---

The full template — vault skeleton, all four note types, MOC structure, skill guides including Ariun (linking hygiene) and Mnara (archival), session log pattern, and optional local runtime — is at **[Obsidian Agent Vault, $49](https://pharosml.gumroad.com/l/kvbhdo)**.

If you're already past 50 notes and hitting any of the symptoms above, the template gives you the mature structure without the iteration time.

## Related

- [[Research and Papers MOC]]
- [[hashnode-iter34-skill-guides]]
