# Community Posts — Obsidian Agent Vault

Replace https://pharosml.gumroad.com/l/kvbhdo with your live Gumroad URL before posting.

---

## r/ObsidianMD

**Title:** Built a starter vault structure specifically for AI coding agents (Claude Code, Cursor, Aider) — sharing the design

I've been using Obsidian as a persistent memory layer for AI coding sessions, and after iterating on the structure for a while, I packaged it up into a clean starter vault.

The core design:

**Folder structure:**
- `wiki/` — durable linked knowledge notes (concepts, decisions, project context)
- `raw sources/` — unsynthesized captures, preserved as-is
- `skills/` — synthesis and workflow guides
- `archive/` — rotated-out material that stays discoverable
- `templates/` — hub templates for projects, people, concepts, decisions, and MOCs

**What makes it Obsidian-native:**
Every note is designed around wikilinks and backlinks, not just flat text. The hub templates enforce `[[links]]` inline rather than in trailing "Related" dumps — the goal is graph traversal, not filing. MOC pages anchor the structure so you can actually navigate 100+ notes without search.

**The AI agent angle:**
The vault includes a `CLAUDE.md` context loader that agents like Claude Code read at session start. The idea is that the vault holds project context, decisions, person notes, and synthesis — and the agent picks it up cold rather than you re-explaining it every session.

There's also an optional local runtime for WSL users: `setup.sh`, a CLI (`ask.py`), a `vault_watcher.py` for live updates, and a Windows `.bat` launcher.

I packaged this as a paid template ($49) on Gumroad https://pharosml.gumroad.com/l/kvbhdo — figured if it was useful enough for me to maintain, it was worth making properly. Happy to discuss the structural decisions if anyone has questions or wants to push back on the design choices.

---

## r/ClaudeAI

**Title:** Built a vault structure to solve Claude Code's cold-start problem — CLAUDE.md as a real persistence layer

If you use Claude Code regularly, you know the problem: every session starts cold. You re-explain the project structure, the decisions you've already made, the context that took you three sessions to build up. CLAUDE.md helps, but most people treat it as a static README rather than a live system.

This vault is built around treating CLAUDE.md as the top of a structured knowledge graph.

**How it works:**
- `CLAUDE.md` at the vault root points to the active project context, current decisions, and open threads
- `wiki/` holds durable notes — project hubs, person notes, decision logs, concept synthesis — all cross-linked
- The agent reads the context loader, traverses to the relevant notes, and picks up where the last session ended

**Structure the vault enforces:**
- Project hub templates with status, decisions, and open questions fields
- Decision notes that log the reasoning, not just the outcome
- A synthesis skill guide so notes get linked properly rather than piling up as orphans

There's also an optional local runtime (WSL): `setup.sh`, `ask.py` CLI for querying the vault directly, and a `vault_watcher.py` that keeps the vector store current as you add notes.

It's a paid template pack ($49, Gumroad https://pharosml.gumroad.com/l/kvbhdo) — not a hosted product, not an autonomous agent, just a clean file structure you own. Worth it if you're spending real time re-priming Claude every session.

---

## r/SideProject

**Title:** I built a structured Obsidian vault to give AI coding agents persistent memory between sessions — $49 template pack

I kept losing context between Claude Code sessions. I'd spend 20 minutes re-explaining project structure, decisions I'd already made, things that had already been tried. CLAUDE.md helped but my notes were a mess.

So I built a vault structure that actually solves it — and used it for a few months before packaging it up.

**What it is:**
An Obsidian starter vault with a specific folder structure (`wiki/`, `raw sources/`, `skills/`, `archive/`, `templates/`) and a `CLAUDE.md` context loader that AI agents read at session start. Hub templates for projects, people, concepts, and decisions. Three skill guides for synthesis, linking, and archiving. An optional local runtime for WSL (setup script, CLI, vault watcher) and a Windows `.bat` launcher.

**What it's not:**
Not an autonomous AI, not a hosted service, not an enterprise thing. It's a file structure you own in Obsidian.

$49 on Gumroad: https://pharosml.gumroad.com/l/kvbhdo

Happy to answer questions about the design.

---

## r/LocalLLaMA

**Title:** File-native persistent memory for AI coding agents using Obsidian + sentence-transformers — architecture notes

Sharing something I built that might be interesting to people thinking about local-first agent memory.

**The problem:** AI coding agents (Claude Code, Cursor, Aider) are stateless between sessions. CLAUDE.md handles some of this but most people use it as a flat text dump rather than a structured retrieval surface.

**The approach:**
- Obsidian vault as the file-native memory store (markdown, plain files, no proprietary format)
- Structured folder hierarchy: `wiki/` for durable linked notes, `raw sources/` for unsynthesized captures, `skills/` for workflow guides, `archive/` for rotated material
- `CLAUDE.md` as the context injection point — agents read it at session start and traverse linked notes via wikilink references
- Optional local vector store using `sentence-transformers` (`all-MiniLM-L6-v2`) for semantic retrieval across the wiki, with a `vsearch.py` CLI and `vault_watcher.py` for incremental rebuilds
- No external API calls in the retrieval path — fully local

**Why file-native rather than a DB:**
The agent can read, write, and link notes directly without a retrieval wrapper. The file structure IS the memory architecture. Wikilinks provide explicit graph edges; the vector store handles fuzzy semantic queries when you don't know which note to point at.

It's a paid template ($49, Gumroad https://pharosml.gumroad.com/l/kvbhdo) — I packaged it up after using it as my own agent memory layer for several months. Architecture questions welcome.

---

## Hacker News — Show HN

**Title:** Show HN: Obsidian Agent Vault — file-native persistent memory for AI coding agents

I kept losing context between Claude Code sessions — re-explaining project structure, prior decisions, and things already tried every time I opened a new session. CLAUDE.md helps but most people treat it as a static file rather than the top of a knowledge graph. I built a structured Obsidian vault that functions as the persistence layer underneath the model: a `CLAUDE.md` context loader points into a linked wiki of project hubs, decision logs, person notes, and concept synthesis, all connected via wikilinks so the agent can traverse relevant context rather than receive a wall of text. There's an optional local vector store (sentence-transformers, all-MiniLM-L6-v2) with a CLI for semantic queries and a watcher for incremental rebuilds — fully local, no external API calls in the retrieval path. The files are plain markdown in a defined folder structure you own; no proprietary format, no hosted component. I packaged it as a $49 template on Gumroad https://pharosml.gumroad.com/l/kvbhdo after using it as my own agent memory layer for several months. What's novel isn't the individual pieces — it's the structural discipline enforced by the templates that keeps the graph navigable as notes accumulate past 100+.

## Related

- [[Governance and PHAROS MOC]]
- [[hashnode-iter34-skill-guides]]
