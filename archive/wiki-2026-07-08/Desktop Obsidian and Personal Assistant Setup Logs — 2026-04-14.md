---
type: wiki
title: Desktop Obsidian and Personal Assistant Setup Logs — 2026-04-14
aliases:
- Desktop Obsidian setup logs
- personal assistant Desktop scaffold
- Obsidian WSL setup transcript
tags:
- obsidian
- personal-assistant
- lightrag
- infrastructure
- desktop-intake
- vault-product
- archive
- desktop-obsidian-and-personal-assistant-setup-logs-2026-04-14-md
- assistant
- desktop
- personal
- windows
- color-orange
status: active
created: '2026-05-06'
updated: '2026-06-26'
vault_area: archive
canonical_path: archive/wiki-2026-07-08/Desktop Obsidian and Personal Assistant Setup Logs — 2026-04-14.md
backlink_count: 5
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[archive/wiki-2026-07-08/Desktop Text Intake — 2026-05-06]]'
- '[[archive/wiki-2026-07-08/Documents and Downloads Coverage Matrix — 2026-05-06]]'
- '[[wiki/Obsidian Second Brain Product]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
---

# Desktop Obsidian and Personal Assistant Setup Logs — 2026-04-14

## Summary

Synthesis of the Desktop setup traces around Obsidian, WSL, and the personal-assistant vault scaffold. The captured files show the transition from "is Obsidian installed?" to a usable local-first memory architecture: Windows Obsidian as the correct desktop app, WSL as the agent/runtime layer, Markdown vault folders as memory substrate, and LightRAG as optional graph retrieval.

## Source Cluster

| Raw source | Role |
|---|---|
| `raw sources/Desktop-Scan-2026-05-06/Windows PowerShell.txt` | Long PowerShell/Claude Code transcript checking Obsidian installation, WSL behavior, and first note-writing experiments. |
| `raw sources/Desktop-Scan-2026-05-06/README.md` | Personal Assistant WSL setup guide; exact duplicate of `personal-assistant-agents/trismegiste/README.md`. |
| `raw sources/Desktop-Scan-2026-05-06/CLAUDE.md` | Personal Assistant boot context; exact duplicate of `personal-assistant-agents/trismegiste/vault/CLAUDE.md`. |
| `raw sources/Desktop-Scan-2026-05-06/hub-projects.md` | Generated projects hub; exact duplicate of the Trismégiste vault hub. |
| `raw sources/Desktop-Scan-2026-05-06/skill-synthesis.md` | Raw-to-wiki synthesis skill; exact duplicate of the Trismégiste vault skill. |

## Operational Findings

- Obsidian was confirmed as a Windows-side application, not a WSL-native dependency. The stable operator pattern is Windows opens the vault; WSL agents read and write Markdown files through `/mnt/c/...`.
- The personal-assistant scaffold uses a simple vault architecture: `raw/` for unprocessed notes, `wiki/` for synthesized linked notes, `skills/` for reusable procedures, `archive/` for stale/completed material, and `CLAUDE.md` as boot context.
- The setup notes anticipate the same rule now used in EMERAULD: raw capture is not enough; useful material must become linked wiki notes.
- The duplicate files are not new content, but they are provenance for the productized Trismégiste/personal-assistant line.

## Product Relevance

This source cluster supports [[Obsidian Second Brain Product]] because it documents the buyer-facing logic in rough operational form: unzip/open/configure/use folder layers/first retrieval loop. It also supports [[AI Infrastructure Stack]] because it separates three layers that often get blurred:

- Windows app surface: Obsidian;
- filesystem memory surface: Markdown vault;
- agent/runtime surface: WSL, Claude Code/Codex, LightRAG, scripts and services.

## Related

- [[Obsidian Second Brain Product]]
- [[Obsidian Agent Vault — Launch Kit]]
- [[Obsidian Agent Vault — Asset Canon]]
- [[Ask Vault — EMERAULD Vault Briefing Skill]]
- [[LightRAG — Graph-Based RAG System]]
- [[AI Infrastructure Stack]]
- [[Trismégiste — Personal AI Assistant]]
- [[Personal and Projects MOC]]

