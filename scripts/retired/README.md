---
type: note
title: Retired scripts
tags:
- note
- scripts
- retired
status: active
created: '2026-07-08'
updated: '2026-07-08'
vault_area: scripts
canonical_path: scripts/retired/README.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

# Retired scripts

- `auto_tagger.py` — retired 2026-07-08. Its TF-IDF filename/body-word fallback generated the noise tags (filename-echo slugs, stray body nouns) stripped by the overhaul's `enrich_frontmatter_backlinks.py --strip-noise-tags`. Re-running it would re-pollute.
- `color_tagger.py` — retired 2026-07-08. Source of the `color-*` tag class (1,353 occurrences at baseline), removed in the same pass.
