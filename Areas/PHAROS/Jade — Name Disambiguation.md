---
type: disambiguation
title: Jade — Name Disambiguation
tags:
- disambiguation
- jade
- lavoie
- local-agent
- naming-collision
- areas
- pharos
status: active
domain: pharos
created: '2026-07-08'
updated: '2026-07-08'
vault_area: Areas
canonical_path: Areas/PHAROS/Jade — Name Disambiguation.md
backlink_count: 2
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
---

# Jade — Name Disambiguation

> For future Claude: "Jade" refers to two completely unrelated things in Martin's working environment. Never conflate them — check which one a document means before acting on it.

## Summary

Two unrelated entities are both called "Jade" across Martin's environment:

1. **Jade (software)** — Martin's local, Ollama-based bounded personal assistant, at `/home/martin/jade/` (mirrored at `/home/martin/EMERAULD/projects/jade/`).
2. **Jade (person)** — the human Base44 developer building the Groupe Lavoie client apps, documented in `/home/martin/Lavoie/jade-base44-handoff.md`.

## Context

Verified on disk 2026-07-08. `/home/martin/jade/` contains `jade.py` (8,902 bytes), `tool_router.py`, `voice.py`, `test_prompt_contract.py`, `test_tool_router.py`, and a `README.md` — a local Python project. `/home/martin/EMERAULD/projects/jade/` mirrors the same file set (`jade.py`, `tool_router.py`, `voice.py`, tests, `README.md`), confirming it as the vault-side copy of the same software project, not a different Jade.

`/home/martin/Lavoie/jade-base44-handoff.md` (17,083 bytes, last modified 2026-06-14) is the handoff document for the human developer Jade, referenced in `~/CLAUDE.md`'s People table as "Jade — Base44 developer. Handoff at `Lavoie/jade-base44-handoff.md` (3 apps, specs, acceptance criteria)." Per this note's own scope, client details from that handoff are not summarized here — the handoff file itself is the reference for the human Jade; this note only exists to prevent the name collision from causing confusion.

`/home/martin/EMERAULD/graph/nodes/unmapped/jade.md` also exists as an unmapped graph node — worth checking against both entities if it surfaces in future graph work, since it is not yet resolved to either.

## Details

| | Jade (software) | Jade (person) |
|---|---|---|
| **What** | Martin's local, Ollama-based bounded personal assistant | Human Base44 developer for Groupe Lavoie |
| **Location on disk** | `/home/martin/jade/` (primary), `/home/martin/EMERAULD/projects/jade/` (vault mirror) | Referenced via `/home/martin/Lavoie/jade-base44-handoff.md` |
| **Key files** | `jade.py`, `tool_router.py`, `voice.py`, `README.md`, test files | `jade-base44-handoff.md` (3 apps, specs, acceptance criteria) |
| **Relationship to PHAROS** | Internal tooling — a bounded AI assistant Martin runs locally | External contractor working on client (Groupe Lavoie) deliverables |
| **Relationship to Lavoie project** | None | Central — builds the Base44 apps for [[Contremaître — Groupe Lavoie Field-Operations Platform]] |

The collision is purely nominal — there is no shared codebase, no shared purpose, and no indication either entity was named with the other in mind. The risk this note guards against is a future agent reading "Jade" in one context (e.g. a Lavoie gate status question) and pulling in the wrong entity's files (e.g. `/home/martin/jade/jade.py`) or vice versa.

## Related

- [[Contremaître — Groupe Lavoie Field-Operations Platform]]
- [[Governance and PHAROS MOC]]
