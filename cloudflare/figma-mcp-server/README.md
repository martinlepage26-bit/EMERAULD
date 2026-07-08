---
type: readme
title: Figma MCP Server on Cloudflare Workers
aliases:
- cloudflare/figma-mcp-server/README
tags:
- readme
- cloudflare
- figma-mcp-server
- figma
- token
- workers
- server
- vars
- color-orange
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: cloudflare
canonical_path: cloudflare/figma-mcp-server/README.md
backlink_count: 1
backlinks:
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
---

# Figma MCP Server on Cloudflare Workers

This is a remote MCP server that exposes focused Figma REST API tools for design-to-code work. It is meant to give Codex/Claude a real way to fetch Figma file metadata, node JSON, image export URLs, and compact design summaries.

## Tools

- `figma_extract_from_url` parses a Figma URL into file key and node id.
- `figma_get_file_metadata` reads `GET /v1/files/:key/meta`.
- `figma_get_file` reads `GET /v1/files/:key` with optional `ids`, `depth`, `version`, and `geometry`.
- `figma_get_nodes` reads `GET /v1/files/:key/nodes`.
- `figma_get_image` reads `GET /v1/images/:key` and returns expiring render URLs.
- `figma_get_image_fills` reads `GET /v1/files/:key/images`.
- `figma_summarize_file` returns a compact page/frame tree for design-context intake.

## Figma token

For personal use, create a Figma personal access token with:

- `file_content:read`
- `file_metadata:read`

The server expects the token in a Worker secret named `FIGMA_PERSONAL_ACCESS_TOKEN`.

## Local dev

```bash
npm install
cp .dev.vars.example .dev.vars
# edit .dev.vars and paste your Figma token locally
npm run dev
```

Then run MCP Inspector and connect to `http://localhost:8788/mcp`:

```bash
npm run inspect
```

## Deploy

```bash
npx wrangler secret put FIGMA_PERSONAL_ACCESS_TOKEN
npm run deploy
```

The deployed MCP endpoint will be:

```text
https://figma-mcp-server.<your-workers-subdomain>.workers.dev/mcp
```

Clients that still need a local proxy can use:

```json
{
  "mcpServers": {
    "figma": {
      "command": "npx",
      "args": ["mcp-remote", "https://figma-mcp-server.<your-workers-subdomain>.workers.dev/mcp"]
    }
  }
}
```

## Related

- [[Governance and PHAROS MOC]]
- [[SHOW-ME-WHAT-TO-DO]]
