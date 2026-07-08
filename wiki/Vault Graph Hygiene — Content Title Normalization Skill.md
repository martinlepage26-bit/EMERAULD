---
type: wiki
title: Vault Graph Hygiene — Content Title Normalization Skill
aliases:
- vault-graph-hygiene
- graph-hygiene
- title normalization skill
- wrapper cleanup skill
tags:
- skills
- vault
- graph-hygiene
- normalization
- backlinks
- wiki
- hygiene
- graph
- generator
- aliases
- wrapper
status: active
created: '2026-05-06'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Vault Graph Hygiene — Content Title Normalization Skill.md
backlink_count: 12
backlinks:
- '[[Areas/PHAROS/Anti-Charm]]'
- '[[Areas/PHAROS/Skill Ecosystem — Professional Capability Registry]]'
- '[[Areas/PHAROS/Trace Investigator]]'
- '[[wiki/Codex Skills Inventory — Complete Registry (241 Skills)]]'
- '[[wiki/Martin Lepage — Authored Skills]]'
- '[[wiki/Skill Domain — Vault and Knowledge]]'
- '[[wiki/VAULT ADDITIONS TRACKER]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[artifacts/stale-projects-2026-07-04]]'
- '[[artifacts/stale-projects-2026-07-05]]'
- '[[artifacts/stale-projects-2026-07-06]]'
- '[[artifacts/stale-projects-2026-07-07]]'
---

# Vault Graph Hygiene — Content Title Normalization Skill

## Summary

This note tracks the EMERAULD-facing documentation for the `vault-graph-hygiene` Codex skill. It governs no-skip vault cleanup passes that normalize titles to content, preserve backward-compatible aliases when needed, repair backlinks and hub pages, and keep generator sources aligned so wrapper labels do not reappear on rebuild.

## What it does

- Renames or relabels notes according to their actual content rather than inherited wrapper prefixes.
- Preserves stable aliases when old links must continue to resolve.
- Updates hub pages, bridge notes, and tracker surfaces so the graph remains reciprocal.
- Keeps generator or script sources in sync with the live wiki graph.
- Treats raw sources as provenance, not as targets for graph-hygiene rewrites.

## Boundaries

- This is a graph-normalization skill, not a general archival or genealogy skill.
- It should not rewrite raw source packs to satisfy title hygiene.
- It favors additive repair and compatibility preservation unless the user explicitly asks for alias purge mode.

## Related

- [[Skill Ecosystem — Professional Capability Registry]]
- [[Codex Skills Inventory — Complete Registry (241 Skills)]]
- [[Skill Development Workflow — TDD, Dual-Layer, and Eval-Iterate]]
- [[VAULT ADDITIONS TRACKER]]
- [[Trace Investigator]]
