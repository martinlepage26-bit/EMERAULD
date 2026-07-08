---
type: agent-instructions
title: CLAUDE
tags:
- agents
- agent-instructions
- artifacts
- marketplace
- tracker
- softinfo
- monthly
- users
- aurora
status: active
created: '2026-04-19'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/CLAUDE.md
backlink_count: 1
backlinks:
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
---

● Caelir - Context Guide

  ▎ This file gives the agent its standing map before work begins.
  ▎ The file name stays CLAUDE.md for Claude Code compatibility.
  ▎ Edit it once, update it when your project changes.

  Mission

  Use this vault as the shared memory layer for Martin Lepage's PHAROS-SUITE work. Before answering
  project questions, orient from Home.md, the relevant hub notes, and wiki/. Treat raw/ as unsorted
  evidence, not finished knowledge. Governance constraints from /home/cerebrhoe/AGENTS.md and
  /home/cerebrhoe/hephaistos/AGENTS.md are authoritative; this vault is operational memory, not
  authority.

  Who

  - Name: Martin Lepage, PhD
  - Role: Founder/principal of PHAROS-SUITE; AI governance researcher and operator. Designs and runs a
   three-agent governance harness (HEPHAISTOS / Queen Keyport / Hermes) plus independent specialists
  (Argus, HENRY, Gadget, Trismégiste).

  Active Projects

  - PHAROS-SUITE: Canonical PHAROS repo (pharos-suite), serves https://pharos-ai.ca. Houses AurorA,
  COMPASSai, HERMES dashboard, MiroFish. See [[hub_pharos_suite]].
  - martin-lepage-site: Public Martin identity, serves https://martin.govern-ai.ca. Hosts /lotus,
  /scripto, /gaia, /echo, /dr-sort and authored governance/skill-tree artifacts. See
  [[hub_martin_site]].
  - AurorA: Active module under pharos-suite/aurorai/ (not standalone repo). See [[hub_aurora]].
  - COMPASSai: Web/SaaS for clients. Phase 1 on Cloudflare free tier; Phase 2 on custom Canadian
  hosting post-Lavoie. See [[hub_compassai]].
  - HEPHAISTOS governance harness: /home/cerebrhoe/hephaistos/ — three-agent stack, skill corpus,
  co-equal authority model. See [[hub_hephaistos]].
  - Adversarial evaluation paper: Formal multi-model adversarial evaluation manuscript (HENRY scope).
  See [[hub_adversarial_eval_paper]].

  Stack / Tools

  - Python, TypeScript/JavaScript, Markdown, CSS
  - Cloudflare Pages (deployment target — npm run build before commit on frontend)
  - Claude Code + Codex (paired agents; install/configure both unless told otherwise)
  - Obsidian (EMERAULD vault at /mnt/c/Users/softinfo/Documents/EMERAULD/)
  - WSL2 on Windows 11; primary workspace /home/cerebrhoe, mounted Windows at /mnt/c/Users/softinfo
  - rg / apply_patch preferred over alternatives

  Preferences

  - Be direct. No boilerplate, no preamble, no trailing summaries unless asked.
  - Course-correct on blunt feedback; do not re-explain or defend prior approach.
  - Use Obsidian wikilinks [[like this]], not markdown links, inside the vault.
  - Inline [[links]] in Summary / Context / Details — ## Related does not substitute for inline
  linking.
  - Apply changes to BOTH Claude Code AND Codex unless explicitly scoped otherwise.
  - Default to cheapest model + lowest effort that completes the task correctly; escalate only on real
   complexity, ambiguity, or governance risk.
  - Plan before code. Re-plan after scope change or new evidence. No completion claim without
  verification.
  - Spelling: AurorA (capital A at end) — never Aurora, AurorA, or aurorai in prose.

 Standing Rules (corrected)

  - Always check wiki/ before searching raw/.
  - When creating a new wiki note, link it back to at least one hub note or MOC.
  - Never create an unlinked note. A note without links is stored text, not usable memory.
  - When unsure where something goes: raw/ first, wiki/ after synthesis.
  - Prefer updating an existing wiki note over creating a near-duplicate.
  - Ask before deleting raw source material unless a deletion policy is already set.
  - Update the relevant tracker at every major change (see Tracker Registry below); default
  cross-session tracker is the Master.
  - Run the monthly tracker archive cycle on the 15th (covers trackers 1–4); archives to
  /mnt/c/Users/softinfo/Documents/PHAROS-ARCHIVE/tracker-snapshots/.
  - Separate evidence from inference. Bounded claims only — no exhaustive-coverage claims.
  - Diamond-Eyes gate is non-negotiable before promotion. L99 gap-declaration applies on advisory
  deviation.
  - Do not cross-publish between pharos-ai.ca and martin.govern-ai.ca surfaces.
  - Frontend changes: run npm run build before commit; commit + build + deploy to Cloudflare Pages
  without being re-asked.

  Tracker Registry

  Five live trackers (four in the monthly archive cycle, plus Martin-site, plus an Argus audit tracker
   observed on disk):

  1. Master — /mnt/c/Users/softinfo/Documents/MASTER TRACKER (recreated from MASTER PACK 4).md
  (default; archived monthly)
  2. PHAROS-AI — /mnt/c/Users/softinfo/Documents/PHAROS-AI CHANGE TRACKER.md (archived monthly)
  3. Method — /mnt/c/Users/softinfo/Documents/METHOD TRACKER.md (archived monthly)
  4. Client Accounts — /mnt/c/Users/softinfo/Documents/CLIENT ACCOUNTS TRACKER.md (fourth subtracker;
  archived monthly)
  5. Martin-site — /mnt/c/Users/softinfo/Documents/MARTIN-SITE CHANGE TRACKER.md (live; not confirmed
  in monthly archive cycle)
  6. Argus Audit — /mnt/c/Users/softinfo/Documents/ARGUS AUDIT TRACKER.md (present on disk; not in the
   canonical registry memory — verify scope before relying on it)

## Buyer Safety Rules

- Do not invent private facts about the user or their projects.
- Do not treat examples in this starter vault as real project history.

## Vault Map

```
vault/
- CLAUDE.md        <- you are here
- START_HERE.md    <- first setup loop
- Home.md          <- human entry point
- raw/             <- incoming captures, unprocessed
- wiki/            <- linked, durable knowledge
- skills/          <- reusable agent instructions
- archive/         <- completed or retired material
- templates/       <- hub-note templates
```

## Related

- [[Governance and PHAROS MOC]]
- [[Trismégiste — Personal AI Assistant]]
