---
type: wiki
title: Cloudflare Pages-to-Worker Migration — Build and Asset Behavior
aliases:
- Pages to Worker migration
- Pages-to-Worker conversion
- Cloudflare Pages migration to Worker
tags:
- cloudflare
- deployment
- pages
- workers
- wrangler
- routing
- assets
- areas
- cloudflare-pages-to-worker-migration-build-and-asset-behavior-md
- worker
- jsonc
- color-orange
status: active
created: '2026-04-21'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/Cloudflare Pages-to-Worker Migration — Build and Asset Behavior.md
backlink_count: 8
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/Governance and Platform Signals Memo — 2026-05-14]]'
- '[[archive/wiki-2026-07-08/HELIX Production Shipping Runbook — Web, iOS, Android (2026-04-19)]]'
- '[[wiki/PHAROS Migration Runbook — PR4 Deploy and Cloudflare Migration (2026-04-19)]]'
- '[[Areas/PHAROS/PHAROS-AI Webservice — pharos-ai.ca]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[archive/session-state/session-state-001]]'
- '[[memory/daily/2026-04-21]]'
---

# Cloudflare Pages-to-Worker Migration — Build and Asset Behavior

## Summary

Cloudflare's Pages-to-Worker migration path is mostly a configuration shift, not an application rewrite: the build command can stay the same, static assets still serve through Workers assets, and custom domains/routes continue to work. What changes is the deployment surface and runtime contract: `wrangler pages deploy` becomes `wrangler deploy`, Pages Functions must be compiled into a Worker entrypoint, `_routes.json` stops mattering, and the worker config moves into `wrangler.jsonc`. Relevant to [[PHAROS-AI Webservice — pharos-ai.ca]] and the migration context captured in [[L99 PHAROS Migration Artifacts 2026-04-19]].

## Context

Source: `Clippings/Build  Compute  Workers & Pages  Martinlepage26@me.com's Account.md`, a Cloudflare dashboard help page opened from Martin's `helix` build view on 2026-04-21. The clipping answers the practical question, "what happens if I turn a Pages project into a Worker?" and is useful as a deployment boundary note for any Cloudflare-backed site that may eventually consolidate frontend and API behavior.

## Details

### What stays the same

- The existing framework build step usually does not need to change.
- Static assets still work through the Workers assets configuration.
- Custom domains and routes remain available.

### What changes

- Deploying shifts from `wrangler pages deploy` to `wrangler deploy`.
- The config surface shifts from `pages_build_output_dir` to a `wrangler.jsonc` assets block.
- Pages Functions are no longer auto-discovered from a `functions/` directory; they must be compiled into a Worker entrypoint.
- Preview and local-dev commands change from Pages-oriented commands to Worker-oriented ones.
- `_routes.json` is no longer the routing control surface.

### Why it matters

- A Worker gives more flexibility for cron, queues, and custom routing.
- Pages remains simpler for purely static sites with Git-integrated preview flows.
- Wrangler v4+ matters if you are using the modern Workers Assets format.
- The real decision is usually about deployment shape and routing control, not about rewriting the app itself.

## Key Ideas

- **This is a config migration, not a code migration.**
- **Workers expand control; Pages reduces operational friction.**
- **Routing responsibility moves from Pages conventions into `wrangler.jsonc`.**

## Insights

- For [[PHAROS-AI Webservice — pharos-ai.ca]], this clarifies the boundary between a Pages frontend and a Worker-backed deployment model.
- If PHAROS later collapses more behavior into a single Worker, the migration is mainly about asset and routing config, not application logic.
- The note gives a concrete reason to treat `wrangler.jsonc` as a live source of truth rather than just a build file.

## Open Questions

- Should PHAROS keep the public frontend on Pages and only use Workers for API logic, or eventually consolidate more of the surface into one Worker deployment?
- Which Cloudflare preview workflow is most stable for the PHAROS operator path: Pages-style preview deployments or Worker-oriented local dev?

## Related

- [[PHAROS-AI Webservice — pharos-ai.ca]]
- [[L99 PHAROS Migration Artifacts 2026-04-19]]
- [[Governance and PHAROS MOC]]

- [[README]]
## Sources

- `Clippings/Build  Compute  Workers & Pages  Martinlepage26@me.com's Account.md`
- Cloudflare dashboard help text from the Helix build view, 2026-04-21
