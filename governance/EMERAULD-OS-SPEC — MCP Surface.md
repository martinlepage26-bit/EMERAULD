---
type: governance-doc
title: EMERAULD-OS-SPEC — MCP Surface
tags:
- governance-doc
- emerauld-os
- spec
- mcp
status: active
domain: governance
created: '2026-07-08'
updated: '2026-07-08'
vault_area: governance
canonical_path: governance/EMERAULD-OS-SPEC — MCP Surface.md
---

# OS Spec — MCP Surface for the Vault (gap 6)

> For future Claude: decision + wiring spec for giving the vault a programmatic API surface. As of 2026-07-08 every `mcpServers` config on this host is empty — no tool other than a filesystem-access CLI session can reach the vault. Build in Stage 2 of [[governance/EMERAULD-OS-BUILD-ORDER|the build order]].

## Decision (2026-07-08)

Activate the **vendored MCP server that already ships with obsidian-second-brain** at `~/.claude/vendor/obsidian-second-brain/integrations/obsidian-mcp-server/` — zero new code, already aligned with the vault's operating rules. Alternatives rejected: a custom FastAPI wrapper (new code, new maintenance surface) and the Obsidian REST-API community plugin (requires the GUI this host doesn't have).

## Wiring spec

1. Inspect the server's README/config; point its vault root at `/home/martin/EMERAULD`.
2. Register in `~/.claude.json` `mcpServers` (project scope first, global after a week of clean use). Never place tokens in vault-tracked files.
3. Enforcement: the server must respect the raw-lane protection (`raw sources/`, `raw/` read-only) — if it lacks a path-exclusion config, front it with filesystem permissions or patch the exclusion in before exposure.
4. Smoke test from a second surface (Claude Desktop or another session): read a note, create a scratch note in Inbox/, verify frontmatter schema + tracker discipline, delete the scratch.
5. Record activation in RELAY-LEDGER (it changes the vault's authority surface).

## Exit criterion

Another Claude surface performs a rule-compliant note create through MCP (schema frontmatter, ≥2 wikilinks, tracker line) without filesystem access.

## Related

- [[governance/EMERAULD-OS-BUILD-ORDER|EMERAULD OS Build Order]]
- [[Areas/PHAROS/InfraFabric MCP Stack — Remote Bundles]]
