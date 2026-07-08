---
type: artifact
title: Medium Article + ProductHunt Copy — Obsidian Agent Vault
tags:
- artifact
- agents
- artifacts
- marketplace
- agent
- guides
- claude
- start
- obsidian
status: preserved
created: '2026-06-21'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/promo/medium-producthunt.md
backlink_count: 3
backlinks:
- '[[Areas/Writing/Research and Papers MOC]]'
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
- '[[artifacts/marketplace/promo/hashnode-iter34-skill-guides]]'
---

# Medium Article + ProductHunt Copy — Obsidian Agent Vault

Replace https://pharosml.gumroad.com/l/kvbhdo with your live Gumroad URL before posting.

---

## Medium Article

**Title:** Why Your AI Agent Forgets Everything (And How to Fix It with a $49 Obsidian Vault)

It happened again on Tuesday.

I was three hours into a session with Claude Code, deep in a refactor I had already explained twice before. I needed to reference a decision we had made two weeks ago — to scope the API gateway separately from the auth layer, for reasons that took an entire conversation to work through. I typed the summary from memory, got it slightly wrong, and spent twenty minutes untangling the confusion that followed.

That was the fourth time this month I had re-explained the same architectural decision to an agent that has no memory of the previous conversation. The agent is not stupid. The agent is stateless. That is a completely different problem, and I was solving the wrong one.

---

### Why AI Agents Start Cold

Every Claude Code session, every Cursor chat, every Aider run begins with an empty context window. The model has no memory of what you built last Tuesday, what you decided to avoid and why, which files are load-bearing, or what the three open questions were when you closed the laptop. All of that lives in your head. Or in a Notion doc you forgot to bookmark. Or nowhere.

The engineering community's instinct has been to reach for heavier tooling: vector databases, RAG pipelines, long-context models, memory plugins. These are real solutions to real problems. But they introduce infrastructure, latency, and complexity that most individual developers and small teams do not need — and they miss something simpler.

The model does not need to remember anything. It needs to be able to read.

---

### The Insight: The Fix Is a File Structure, Not a Smarter Model

Every AI coding agent I have worked with — Claude Code, Cursor, Aider — will read a file if you point it to one. The `CLAUDE.md` file that Claude Code picks up automatically at session start is not a clever trick. It is a contract. You write into that file everything the agent needs to know to start working without you explaining the same thing for the fifth time.

The question is not whether agents can read persistent context. They can. The question is whether you have built a file structure worth reading.

A working vault gives the agent a stable, navigable file-native memory layer. No database. No API. No cloud dependency. Just organized Markdown files in a folder structure the agent can traverse.

---

### What a Working Vault Actually Looks Like

The Obsidian Agent Vault I have built and refined over the past year has five directories and one entry point.

The entry point is `CLAUDE.md` — I call this configuration the Caelir loader. It tells the agent what the project is, what constraints are active, what decisions have been made, and where to look for more. It loads at the start of every session, automatically. This single file eliminates roughly sixty percent of the repetition I used to experience.

The five directories:

- `raw/` — unsynthesized captures. Notes from conversations, rough observations, pasted references. Never overwritten, never cleaned up mid-session. This is the intake buffer.
- `wiki/` — durable linked knowledge notes. Synthesized from raw captures after the information has stabilized. These are the notes the agent actually reasons over.
- `skills/` — workflow guides for the agent. Three are included out of the box: Ilyris (synthesis protocol for turning raw captures into wiki notes), Ariun (linking protocol for maintaining graph integrity), and Mnara (archive hygiene for retiring stale material). These are not prompts. They are procedural guides the agent follows when you invoke them.
- `archive/` — retired notes. Out of the active graph, but retrievable.
- `templates/` — note shapes for the main types (wiki note, raw capture, hub page, project index).

The vault is Obsidian-compatible. You can use it purely as a file folder without ever opening Obsidian. But if you do use Obsidian, you get backlinks, graph view, and fuzzy search across everything the agent has synthesized.

---

### The Optional Local Runtime

For developers who want to go further, the vault includes an optional local runtime: a `setup.sh` script that installs the Python environment, an `ask.py` CLI for querying the vault from the terminal, and a `vault_watcher.py` script that auto-ingests new files in `raw/` as they appear. There is also a Windows launcher for WSL users.

This is not required. The vault works without any of it. But if you want the agent to surface relevant notes semantically — not just by filename — the runtime adds a local vector search layer that runs entirely on your machine.

---

### Who This Is For (and Who It Is Not)

This vault is for developers who use AI coding agents regularly and are tired of re-explaining their project to a model that has no memory of the last conversation. It works best when you have a project with real decisions, real constraints, and real history.

It is not for people who want AI magic. There is no AI magic here. It is Markdown files and a folder structure. If that sounds too simple, you may be underestimating how much of your repeated context could be captured in a well-written `CLAUDE.md`.

---

### Three Tiers, One Starting Point

- **$49** — the template pack. Folder structure, Caelir loader, all three skill guides, hub templates, optional runtime.
- **$299** — guided setup. I configure the vault for your specific project, write the initial `CLAUDE.md` and skill adaptations, and walk you through the first synthesis session.
- **$2,500** — team setup. Full onboarding for a small team with shared conventions and agent workflow integration.

If you are an individual developer and the problem I described at the top of this piece is one you recognize, start with the $49 pack.

Get it here: **https://pharosml.gumroad.com/l/kvbhdo**

The agent does not need to get smarter. It needs a place to read. Build it the file-native way, and you only explain the architecture once.

---

*Martin Lepage, PhD is an AI governance researcher and workflow builder based in Montreal.*

---
---

## ProductHunt Launch Post

**Tagline:** Give your AI agent a memory it can read

**Description (150–300 words):**

Obsidian Agent Vault is a structured Markdown vault that gives AI coding agents (Claude Code, Cursor, Aider) stable, file-native memory across sessions.

The problem: AI agents start cold. Every session begins with an empty context window. You explain your project, decisions, constraints — and then do it again next session.

What's inside:
- **Caelir** — a `CLAUDE.md` context loader the agent reads automatically at session start
- **Five-directory structure** — raw captures, linked wiki notes, skill guides, archive, templates
- **Three workflow skill guides** — Ilyris (synthesis), Ariun (linking), Mnara (archive hygiene)
- **Optional local runtime** — `ask.py` CLI, `vault_watcher.py` auto-ingest, WSL setup, Windows launcher

No database. No API. No cloud. Just organized Markdown files in a structure the agent can traverse and reason over.

Pricing: $49 template pack / $299 guided setup / $2,500 team onboarding

https://pharosml.gumroad.com/l/kvbhdo

---

**Maker comment (post on launch day):**

I built this because I was explaining the same architectural decision to Claude Code for the fourth time in a week.

My first instinct was to reach for RAG, or a vector database, or some memory plugin. Those are real solutions. They are also substantial infrastructure for a problem that, at its core, is just: the agent needs to be able to read what I have already figured out.

So I stopped building infrastructure and started building files.

The Obsidian Agent Vault is what I settled on after about a year of iteration. A `CLAUDE.md` that loads at session start, a `wiki/` folder of synthesized notes the agent can traverse, a `raw/` buffer for unsynthesized captures, and three workflow skill guides the agent follows when asked.

The optional local runtime came later — `ask.py` for terminal queries, `vault_watcher.py` for auto-ingest, local vector search that runs entirely on-machine. Optional — the vault works without it.

I'm an AI governance researcher. I made this because I needed it. The $49 tier is the whole thing. The $299 tier is me spending two hours configuring it for your specific project. The $2,500 tier is full team onboarding.

The agent does not need to get smarter. It needs a place to read. If you have been re-explaining your project to an agent that forgot everything, this vault is the fix.

## Related

- [[Research and Papers MOC]]
- [[hashnode-iter34-skill-guides]]
