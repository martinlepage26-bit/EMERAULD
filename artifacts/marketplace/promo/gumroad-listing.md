---
type: artifact
title: Gumroad Listing — Obsidian Agent Vault
aliases:
- artifacts/marketplace/promo/gumroad-listing
tags:
- artifact
- agents
- artifacts
- marketplace
- agent
- obsidian
- session
- cursor
- project
- color-orange
status: preserved
created: '2026-06-21'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/promo/gumroad-listing.md
backlink_count: 6
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/Obsidian Agent Vault — Launch Kit]]'
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
- '[[memory/agents/Decisions]]'
- '[[memory/daily/2026-06-29]]'
- '[[projects/Second Brain — Fisher King Project State]]'
---

# Gumroad Listing — Obsidian Agent Vault

---

## Product Title
Obsidian Agent Vault — Memory Layer for AI Coding Agents

---

## Summary
Your AI agent forgets everything the moment you close the session. This vault gives Claude Code, Cursor, and Aider a structured memory layer so they start informed, not blank.

---

## Full Description

**The problem**

Every session, you re-explain the project. The stack. The decisions you already made. The folder structure. The constraints. You paste in context from last week's chat, hope you remembered the important parts, and watch the agent confidently re-suggest the thing you already ruled out.

This is not a model problem. It is a missing-layer problem. The model is capable. It just has no persistent memory of your project — because you never gave it one.

**What this vault is**

The Obsidian Agent Vault is a structured starter vault you drop into Obsidian and point your agent at. It gives your AI coding agent a stable, readable, session-persistent context layer: project state, decisions, constraints, active threads, and operating instructions — all in plain Markdown the agent can read on every invocation.

The vault ships with a pre-configured context loader called Caelir (a CLAUDE.md file your agent reads on startup), a START_HERE orientation doc, and a folder structure designed around how agents actually work: raw captures, synthesized wiki notes, skill definitions, an archive, and reusable templates.

Three named workflow guides — Ilyris (capture and intake), Ariun (synthesis and linking), Mnara (session state and continuity) — give your agent explicit operating procedures instead of improvised behavior.

For WSL users, optional local runtime scripts let you run a lightweight agent loop from the terminal without a GUI.

**What's inside**

- `CLAUDE.md` — Caelir context loader, read by Claude Code on every session start
- `START_HERE.md` — orientation document for both you and the agent
- Folder scaffold: `raw/`, `wiki/`, `skills/`, `archive/`, `templates/`
- Hub templates: Project, Person, Concept, Decision — pre-linked, ready to fill
- Three workflow guides: Ilyris (capture), Ariun (synthesis), Mnara (continuity)
- Rename script — swap the guide names to your own if you prefer
- WSL runtime scripts (optional): `setup.sh`, `ask.py`, `vault_watcher.py`
- Windows launcher: `Launch_Agent.bat` for one-click startup

Everything is plain Markdown. No plugins required beyond standard Obsidian. No cloud dependency. No account.

**Who this is for**

- Solo founders using Claude Code, Cursor, or Aider who are tired of re-explaining their project every session
- Developers who have tried to build their own context files but want a clean, pre-structured starting point
- Researchers managing messy notes who want a local-first, agent-readable knowledge base
- WSL users who want a complete local agent scaffold without cobbling one together from scratch
- Anyone who has said "the agent would be useful if it just remembered things"

**Who this is NOT for**

- Teams expecting enterprise SSO, access controls, or a hosted dashboard — this is a local file system vault
- People looking for an autonomous project manager or AI that makes decisions on its own
- Users who want a no-touch setup — you fill in your project context; the structure is provided, not the content
- Obsidian power users looking for a plugin ecosystem or graph-heavy automation — this is intentionally minimal

**The core promise**

Your agent reads the same context file every session. It knows what the project is, what decisions are locked, what is in progress, and what to do next. You stop repeating yourself. The agent stops starting cold. That is the entire value proposition — and it works because it is just Markdown files your agent can already read.

No new tool to learn. No API key. No subscription. Drop it in, fill in your project state once, and your next session starts from where you left off.

---

## Pricing Tiers

- **Template Pack — $49:** The complete vault scaffold, all templates, workflow guides, and runtime scripts — ready to drop into Obsidian and configure yourself.

- **Guided Setup — $299:** Everything in the Template Pack, plus a 90-minute working session where we configure the vault around your specific project, stack, and agent workflow.

- **Team Implementation — $2,500:** Full deployment across a team of up to five developers — vault configuration, shared context conventions, onboarding documentation, and a follow-up review session two weeks post-launch.

---

## Tags
obsidian, claude, cursor, ai agent, second brain, pkm, developer tools, context management, local ai, workflow

---

## License / Content Note

The Template Pack ($49) license covers one individual user. Do not redistribute the vault files or resell them. Team use requires the Team Implementation tier or a separate license — contact ml@pharos-ai.ca. All content is provided as-is; no guarantee of compatibility with future Obsidian or agent versions is implied.

## Related

- [[Governance and PHAROS MOC]]
- [[Obsidian Agent Vault — Launch Kit]]
