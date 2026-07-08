---
type: governance-doc
title: EMERAULD-OS-SPEC — MCP Surface
tags:
- governance-doc
- emerauld-os
- spec
- mcp
- governance
status: active
domain: governance
created: '2026-07-08'
updated: '2026-07-08'
vault_area: governance
canonical_path: governance/EMERAULD-OS-SPEC — MCP Surface.md
backlink_count: 4
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[EMERAULD_OS_ARCHITECTURE]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[governance/EMERAULD-OS-BUILD-ORDER]]'
---

# OS Spec — MCP Surface for the Vault (gap 6)

> For future Claude: decision + wiring spec for giving the vault a programmatic API surface. Build in Stage 2 of [[governance/EMERAULD-OS-BUILD-ORDER|the build order]].

> [!success] Executed 2026-07-08 (same day, operator directive)
> Server registered in Claude Code local scope (project /home/martin) and health-checked Connected: `uv run --with mcp python .../obsidian-mcp-server/server.py`, env `OBSIDIAN_VAULT_PATH=/home/martin/EMERAULD` + `OBSIDIAN_PROTECTED_DIRS="raw sources:raw"`. Raw-lane write guard added to vault_ops.py (env-extensible, vendored-repo commit 3818257) and verified — both lanes refuse writes. **Exit criterion met:** a headless second surface with MCP tools only (filesystem tools disallowed) read a governance note, created `Inbox/2026-07-08 - mcp-surface-smoke-test-2026-07-08.md` with two resolving wikilinks, appended the tracker line via `obsidian_update_note`, and passed validation with no issues. Ledger: RELAY-20260708-001. Open: promote scope local→global after ~1 week clean; MCP-created notes carry the upstream ai-first schema until the Stage 3 routing pass normalizes them on filing.

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
