---
title: Build | Compute | Workers & Pages | Martinlepage26@me.com's Account
source: https://dash.cloudflare.com/1713c51cc6fbcf8d7143526b93495b76/workers/services/view/helix/production/builds/f6ee10f9-a325-49d9-b6b5-78973ad0a6a4
author:
published: 2026-04-21
created: 2026-04-21
status: synthesized
description: Log in to the Cloudflare dashboard. Make your websites, apps, and networks fast and secure. Build modern apps on our developer platform.
tags:
  - cloudflare
synthesized_to:
  - "[[Cloudflare Pages-to-Worker Migration — Build and Asset Behavior]]"
---
what happens if i turn a page into a worker?

Here's what changes when you migrate a Pages project to a Worker:

### What stays the same

- Static assets still work — Workers has built-in asset serving via the `assets` config
- Custom domains and routes continue to work
- Build process — your framework's build command (e.g., `npm run build`) doesn't change

### What changes

|  | Pages | Worker |
| --- | --- | --- |
| Deploy command | `wrangler pages deploy` | `wrangler deploy` |
| Config | `pages_build_output_dir` | `"assets": { "directory": "./dist" }` |
| Functions | `functions/` directory auto-detected | Must be compiled into `_worker.js` via `wrangler pages functions build` |
| Preview | `wrangler pages dev` | `wrangler dev` |
| Git integration | Built-in (GitHub/GitLab) | Also supported via Builds tab |
| `_routes.json` | Controls function routing | Not used — routing is in `wrangler.jsonc` |

### Key things to know

- It's mostly a config change — your app code doesn't need to change
- Pages Functions in a `functions/` directory must be explicitly built into a Worker script
- Wrangler v4+ is required for the modern Workers Assets format
- Bindings (KV, D1, R2, etc.) work the same way, just defined in `wrangler.jsonc` instead of the dashboard

### Why you might do it

- Workers give you more flexibility (cron triggers, queues, custom routing)
- Single `wrangler.jsonc` config instead of split dashboard + file config
- Access to the full Workers platform (Durable Objects, Workflows, etc.)

### Why you might not

- Pages Git integration is more streamlined for static sites
- Preview deployments on every PR are a Pages feature
- If your project is purely static with no server logic, Pages is simpler
