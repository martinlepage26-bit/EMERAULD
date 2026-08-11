---
type: Product
title: martin.govern-ai.ca
tags:
- product
- graph
- nodes
status: active
created: '2026-07-08'
updated: '2026-08-05'
vault_area: graph
canonical_path: graph/nodes/unmapped/martin_govern_ai_site.md
backlink_count: 1
backlinks:
- '[[graph/nodes/unmapped/martin_lepage]]'
id: martin_govern_ai_site
canonical_name: martin.govern-ai.ca
confidence: high
sources:
- root CLAUDE.md (corrected 2026-08-05)
- Hephaistos/Argus/Hermes joint personal-site audit — 2026-08-05 (live `wrangler pages project list` verification)
created_from: graphify_pass
---

# martin.govern-ai.ca

## Summary

Personal/educational site only, never client-facing. Same Cloudflare Pages deployment (`martin-lepage-site` project) as `martin-lepage-phd.pharos-ai.ca` — the two hostnames are aliases of one deploy, not separate sites. Sourced from the git repo `martinlepage26-bit.github.io` (GitHub Pages itself is unused on that repo; it returns 404). `martin-lepage-site` is the Cloudflare Pages *project name*, not a separate GitHub repo — [[CLAUDE]]'s Terms table and this node both stated otherwise before the 2026-08-05 correction below.

**Caution:** `govern-ai.ca` is a shared DNS zone also hosting unrelated products (patent-workbench, clearday, axis, fantasycast subdomains) — see [[wiki/MARTIN SURFACE|Martin Public Surface]]. Do not infer that everything on that zone belongs to Martin's personal site; only `martin.govern-ai.ca` does.

## Known Relationships

### Incoming

- [[Martin Lepage]] → owns → This Node

### Outgoing

- (none found in this pass)

## Related Files

- root CLAUDE.md

## Evidence

- "martin.govern-ai.ca | Personal/educational site only. Never client-facing." — root CLAUDE.md (original `graphify_pass` source; imprecise on hosting — see correction below)
- Verified 2026-08-05 via joint Hephaistos/Argus/Hermes personal-site consolidation audit: `wrangler pages project list` confirmed live that `martin.govern-ai.ca` and `martin-lepage-phd.pharos-ai.ca` are the same Cloudflare Pages deployment (`martin-lepage-site` project), sourced from git repo `martinlepage26-bit.github.io` (GitHub Pages itself unused — returns 404). Applied to this node and to [[CLAUDE]]'s Terms table by Trismégiste in the same correction pass.

## Open Questions

- Resolved 2026-08-05: this node originally carried `confidence: high` while `sources:` listed only "root CLAUDE.md" — i.e. it was graphified straight from a single, since-corrected CLAUDE.md line, so the "high" label was unearned on that basis. `sources:` now carries a second, independent citation (the Hephaistos/Argus/Hermes live-infrastructure audit above), so `confidence: high` is retained on the broader, now-corroborated basis rather than the original single-source one.
