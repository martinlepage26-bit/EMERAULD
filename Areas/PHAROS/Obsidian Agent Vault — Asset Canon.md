---
type: wiki
title: Obsidian Agent Vault — Asset Canon
aliases:
- Obsidian Agent Vault Asset Inventory
- Obsidian Agent Vault Asset Canon
tags:
- product
- obsidian
- assets
- commercialization
- canon
- areas
- obsidian-agent-vault-asset-canon-md
- marketplace
- asset
- setup
- color-orange
status: active
created: '2026-04-18'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/Obsidian Agent Vault — Asset Canon.md
backlink_count: 11
backlinks:
- '[[archive/wiki-2026-07-08/Desktop Obsidian and Personal Assistant Setup Logs — 2026-04-14]]'
- '[[Areas/PHAROS/Elemental Agents — Productization Plan (2026-05-24)]]'
- '[[wiki/Governed Self-Improvement — Method Slide Asset]]'
- '[[Areas/PHAROS/Obsidian Agent Vault — Launch Kit]]'
- '[[Areas/PHAROS/Obsidian Agent Vault — Setup Guide]]'
- '[[wiki/Obsidian Second Brain Product]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[archive/session-state/session-state-001]]'
- '[[artifacts/marketplace/obsidian-agent-vault-2026-04-19/MARKETPLACE-MANIFEST]]'
- '[[assets/elemental-agents/positioning-memo]]'
- '[[projects/Second Brain — Fisher King Project State]]'
---

# Obsidian Agent Vault — Asset Canon

## Summary
The canonical asset inventory for the [[Obsidian Agent Vault — Launch Kit]]. This note separates the core memory-layer product bundle from adjacent PHAROS/method assets and records which files are active, superseded, or archived. Part of [[Obsidian Second Brain Product]].

## Context
This note was created after asset drift appeared inside `assets/`: two setup-guide PDFs coexisted, and `obsidian-vault-slides.html` was being treated as though it were a core vault-product deliverable even though its framing had drifted toward PHAROS/governance method messaging. The goal is to give the vault one stable answer to "which files still reflect the memory-layer build?"

## Canonical Core Product Assets

- `assets/obsidian-agent-vault.zip` - canonical marketplace-ready starter vault template, refreshed 2026-04-19 from the sanitized scaffold and upgraded to include the optional local runtime (`Launch_Agent.bat`, `scripts/setup.sh`, `scripts/ask.py`, `scripts/vault_watcher.py`, `services/README.md`); 40 zip entries; SHA256 `b5ed61c4a037259e54ed63bfdac852aff1daf31732e211ed8f680b374705c02a`
- `assets/obsidian-agent-vault-marketplace-2026-04-19.zip` - versioned marketplace build snapshot of the same runtime-inclusive package; 40 zip entries; SHA256 `b74496f36e67624e3921cc681ba9aa8d8ce7761d6b919c7f655f64eec4bf37f2`
- `assets/Obsidian_Agent_Vault_Setup_Guide.pdf` - canonical customer-facing setup guide PDF
- `assets/CLAUDE_md_Before_After.pdf` - before/after proof asset for the `CLAUDE.md` pitch
- `assets/demo_script_avatar.md` - canonical narration/demo script for the memory-layer product video
- `assets/Obsidian_Agent_Vault_Demo.pptx` - seven-slide demo deck for the product pitch

## Marketplace Build Artifacts

- `artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/` - sanitized staging folder used to build the active zip.
- `artifacts/marketplace/obsidian-agent-vault-2026-04-19/MARKETPLACE-LISTING.md` - marketplace listing packet with title, short description, full description, buyer fit, anti-fit, license note, and pricing ladder.
- `artifacts/marketplace/obsidian-agent-vault-2026-04-19/SANITIZATION-REPORT.md` - source and privacy-leak check for the marketplace build.
- `artifacts/marketplace/obsidian-agent-vault-2026-04-19/MARKETPLACE-MANIFEST.md` - build manifest and zip pointer.
- `artifacts/marketplace/obsidian-agent-vault-2026-04-19/AGENT-NAMING-STUDY.md` - 2026/early-2027 naming study for the buyer-facing guide names; recommends Caelir, Ilyris, Ariun, and Mnara.
- `artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/scripts/rename_guides.py` - buyer-side standard-library script for changing the visible guide names after purchase.
- `artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/scripts/setup.sh` - buyer-side WSL runtime installer.
- `artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/Launch_Agent.bat` - Windows launcher for the optional local runtime shell.

## Adjacent But Non-Core Assets

- [[Governed Self-Improvement — Method Slide Asset]] - HTML slide asset with PHAROS/method framing; useful for deployment and adjacent marketing, but not part of the core Obsidian Agent Vault product bundle

## Archived / Superseded Assets

- `assets/archive/obsidian_agent_vault_setup_guide_2026-04-14.pdf` - earlier dated setup-guide render kept as an archived snapshot after the branded PDF became canonical

## Usage Rules

- When a vault note refers to "the setup guide PDF," it should point to `assets/Obsidian_Agent_Vault_Setup_Guide.pdf`.
- When uploading the vault template to a marketplace, use `assets/obsidian-agent-vault-marketplace-2026-04-19.zip` as the dated upload artifact or `assets/obsidian-agent-vault.zip` as the canonical rolling asset.
- When a note refers to the governance-flavored HTML slide asset, it should link to [[Governed Self-Improvement — Method Slide Asset]] rather than treating it as the launch-kit deck.
- The memory-layer product proof bundle is the zip, setup guide, before/after PDF, demo script, and PPTX deck. Anything outside that set should be named explicitly.

## Related

- [[Obsidian Agent Vault — Launch Kit]]
- [[Obsidian Agent Vault — Setup Guide]]
- [[Obsidian Second Brain Product]]
- [[Personal and Projects MOC]]

- [[MARKETPLACE-MANIFEST]]
## Sources

- [[Obsidian Agent Vault — Launch Kit]]
- [[PHAROS Strategic Analysis — Keep Stop Fix Finish (2026-04-18)]]
- `session-state.md`
