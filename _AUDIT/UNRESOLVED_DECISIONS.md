---
type: audit-doc
title: UNRESOLVED DECISIONS
tags:
- audit
- vault
- unresolved
- emerauld
status: active
created: '2026-07-10'
updated: '2026-07-10'
vault_area: _AUDIT
canonical_path: _AUDIT/UNRESOLVED_DECISIONS.md
---

# UNRESOLVED DECISIONS

## Martin decisions still needed

1. Should `projects/` remain fully visible inside EMERAULD long term, or should the vault keep only selected project mirrors and state notes?
2. Should generated directory MOCs such as `wiki/GRAPHIFY-OUT MOC.md`, `wiki/RAW MOC.md`, and `wiki/RESOURCES MOC.md` be archived later or simply left as low-priority legacy surfaces?
3. Should `graphify-out/` root runtime artifacts be quarantined in a later pass once active dependency is checked?
4. Should `wiki/Master Project Tracker — 2026.md` remain in `wiki/`, or should a future pass relocate it into a more explicit control lane?
5. Should the stale `updated` field pattern be corrected with a dedicated metadata repair pass, knowing that bulk rewriting can further damage freshness signals if done carelessly?

## Explicitly deferred for safety

- mass broken-link repair
- any `.trash/` purge
- any move or contraction inside embedded repos
- broad raw-source pruning
