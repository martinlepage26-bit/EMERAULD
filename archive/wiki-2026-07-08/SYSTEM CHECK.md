---
type: wiki
title: SYSTEM CHECK
tags:
- archive
- linux
- remote
- governess
- suite
- location
- wiki
- wiki-2026-07-08
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: archive
canonical_path: archive/wiki-2026-07-08/SYSTEM CHECK.md
backlink_count: 15
backlinks:
- '[[Areas/PHAROS/Agent Session Phenomenology]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[Areas/Writing/PAPER BUILDER — Source Bundle and HENRY Origin]]'
- '[[wiki/Governance Controls and Mechanisms]]'
- '[[wiki/Root Loose Notes Cluster Map — 2026-05-06]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[archive/session-state/session-state-001]]'
- '[[archive/wiki-2026-07-08/Documents Root Intake — Hermes Action Map 2026-04-28]]'
- '[[archive/wiki-2026-07-08/Documents Root Loose Files Intake — 2026-04-28]]'
- '[[archive/wiki-2026-07-08/Local Hardware and Discovery Snapshot — Laptop A]]'
- '[[artifacts/stale-projects-2026-07-04]]'
- '[[artifacts/stale-projects-2026-07-05]]'
- '[[artifacts/stale-projects-2026-07-06]]'
- '[[artifacts/stale-projects-2026-07-07]]'
- '[[memory/daily/2026-04-28]]'
---

# SYSTEM CHECK

## Summary

Read-only topology audit of the broader Windows and WSL workspace surrounding EMERAULD. The note identifies canonical repositories, duplicate clusters, and cleanup decisions that affect how the vault fits into the larger operating environment.

## Context

Captured on 2026-04-15 as a Hermes dependency map. This note preserves the audit text below as operational evidence rather than rewriting it into a normalized architecture page. Part of [[Personal and Projects MOC]] and related to [[InfraFabric Architecture]], [[CLI-Anything — Agent Harness for Tool Integration]], and [[Obsidian Agent Vault — Launch Kit]].

2026-04-28 follow-up: [[Local Hardware and Discovery Snapshot — Laptop A]] preserves the root Documents hardware/WSL discovery files that complement this broader topology audit, while [[Documents Root Loose Files Intake — 2026-04-28]] records the exact loose-file capture pass.

## Audit Capture

 HERMES DEPENDENCY MAP — Project Topology Audit

  Date: 2026-04-15 | Scope: C:\Users\softinfo + /home/cerebrhoe
  (WSL2) | Mode: Read-only. No modifications made.

  ---
  I. ECOSYSTEM MAP — Top-Level

  Two physical workspaces, one logical ecosystem:

  C:\Users\softinfo\         ← Windows home (WSL path:
  /mnt/c/Users/softinfo)
  /home/cerebrhoe/           ← Linux/WSL home (primary execution
  environment)

  These are not isolated. They share repos, symlinks, and live
  credentials. The Linux side is the active workspace. The Windows
  side is a mix of active git repos, stale mirrors, and
  documentation/writing hubs.

  4 root systems detected:
  1. PHAROS-SUITE — platform core (multi-surface, multi-branch)
  2. Governess — agent/tool project (fragmented across 3 copies)
  3. Writing/Publishing Corpus — academic, narrative, and
  governance writing (CODEX hub on Desktop)
  4. Governance Stack — HEPHAISTOS architecture (local repo +
  root-level loose files)

  ---
  II. FULL ARBORESCENCE

  A. PHAROS-SUITE CLUSTER

  github.com/martinlepage26-bit/pharos-suite.git
  │
  ├── [CANONICAL — Linux WIP]
  │   /home/cerebrhoe/PHAROS-SUITE/repos/pharos-suite/
  │   branch: wip/com-aur-runtime-build
  │   contains: aurorai/, backend/, compassai/, frontend/, infra/,
  docs/, ...
  │
  ├── [CLEANUP BRANCH — Linux]
  │   /home/cerebrhoe/PHAROS-SUITE/repos/pharos-suite-cleanup/
  │   branch: cleanup (same remote)
  │
  ├── [WINDOWS MIRROR — main branch]
  │   /mnt/c/Users/softinfo/PHAROS-SUITE/
  │   branch: main | has codex/ and claude/ remote branches
  │   same folder structure as canonical, but diverged state
  │
  ├── [SYMLINKS — /home/cerebrhoe/repos/]
  │   pharos-suite →
  /home/cerebrhoe/PHAROS-SUITE/repos/pharos-suite
  │   pharos-ai    → /home/cerebrhoe/PHAROS-SUITE/repos/pharos-ai
  │   AurorA      → /home/cerebrhoe/PHAROS-SUITE/repos/AurorA
  │   CompassAI    → /home/cerebrhoe/PHAROS-SUITE/repos/CompassAI
  │   pharos-ai-release-candidate-2026-03-14 → (symlink)
  │
  ├── SUB-PROJECTS (inside PHAROS-SUITE/repos/):
  │   ├── pharos-ai/              ← pharos-ai.ca backend/site (git
  status unverified)
  │   ├── AurorA/                ← AurorA module code — NO .git
  (subdir only)
  │   ├── CompassAI/              ← COMPASSai module code — NO .git
  │   └── pharos-ai-release-candidate-2026-03-14/  ← frozen
  snapshot
  │
  └── PHAROS DATA/ARCHIVE:
      /mnt/c/Users/softinfo/Documents/PHAROS-ARCHIVE/    ← Obsidian
   vault, tracker snapshots
      /mnt/c/Users/softinfo/Documents/PHAROS_PAPERS_DB/  ← SQLite
  DB + Python script
      /mnt/c/Users/softinfo/Documents/PHAROS METHOD REPOSITORY/  ←
  Obsidian vault, method docs
      /mnt/c/Users/softinfo/Documents/PHAROS_PAPERS_DB/export/
      /mnt/c/Users/softinfo/Documents/PAPERS_MASTER_CONSOLIDATED_20
  26-04-10/
      /mnt/c/Users/softinfo/Documents/pharos-ops-dashboard/     ←
  GitHub Desktop clone

  ---
  B. GOVERNESS CLUSTER

  github.com/martinlepage26-bit/Governess
  │
  ├── [PRIMARY — Windows]
  │   /mnt/c/Users/softinfo/Governess/   branch: main
  │   ├── AutoResearchClaw/   ← NESTED REPO →
  github.com/aiming-lab/AutoResearchClaw.git
  │   ├── zep/                ← NESTED REPO →
  github.com/getzep/zep.git
  │   ├── triangulation/      ← subdir (no git)
  │   └── desktop_app/governess_agatha/  ← Agatha desktop app stub
  │
  ├── [ARCHIVE DUPLICATE — Linux]
  │   /home/cerebrhoe/_archive/Governess_duplicate_2026-03-18/
  │   same remote (Governess), marked as duplicate
  │
  └── [SHELL BACKUP — Linux — DIFFERENT REMOTE]
      /home/cerebrhoe/_archive/Governess_empty_shell_backup/
      remote: github.com/martinlepage26-bit/govern.git   ← NOT
  Governess; distinct repo
      ├── AutoResearchClaw/  ← NESTED (archive copy)
      └── zep/               ← NESTED (archive copy)

  ---
  C. AURORAI GHOST

  github.com/martinlepage26-bit/AurorA.git
  │
  └── [GHOST TRACKING — Windows home IS the repo]
      /mnt/c/Users/softinfo/   ← git root tracking AurorA
      branch: 4 commits, many deleted files (D status)
      HEAD: "Add LOTUS refined model and missing modules patch"
      NOTE: The Windows home directory is inside this git working
  tree.
      This is stale — the module was renamed to AurorA and absorbed
   into pharos-suite.

  ---
  D. MARTIN-LEPAGE-SITE

  github.com/martinlepage26-bit/martinlepage26-bit.github.io.git
  │
  ├── [CANONICAL — Linux]
  │   /home/cerebrhoe/martin-lepage-site/
  │
  ├── [TMP WORKING COPIES — Linux]
  │   /home/cerebrhoe/tmp/martinlepage26-bit.github.io-work/
  │   /home/cerebrhoe/tmp/mlepage.github.io/
  │
  └── [DESKTOP MODELS working material]
      /mnt/c/Users/softinfo/Desktop/CODEX/Website_Content_Snapshot/

  ---
  E. GOVERNANCE / HEPHAISTOS STACK

  /home/cerebrhoe/hephaistos/    ← REPO (no remote confirmed —
  local-only)
  │   AGENTS.md, CLAUDE.md, HEPHAISTOS.md, QUEEN-KEYPORT.md,
  HERMES.md
  │   ORCHESTRATION.md, FORGING-*.md, DIAMOND-EYES.md
  │   Phase 7 complete per git log
  │
  ├── [LOOSE DUPLICATES at Linux root — /home/cerebrhoe/]
  │   HEPHAISTOS.md, QUEEN-KEYPORT.md, HERMES.md, ORCHESTRATION.md
  │   AGENTS.md, ROOK.md, RED-HANDBOOK.md, RED-HANDBOOK.pdf
  │   PROTOCOLS/, RECURSO_PHASE_PACKET_FROM_RECURSUS/
  │   → These appear to be copies or exports from hephaistos/ repo
  │
  ├── [BUILD ARTIFACTS]
  │   /home/cerebrhoe/HEPHAISTOS_BUILD/
  │   ├── EXTRACTED/
  │   ├── MASTERxMASTERxMASTER_REBUILT/
  │   └── SKILLS to CODEXAGENT.zip
  │
  └── [GOVERNANCE PROJECT]
      /home/cerebrhoe/governance-project/
      Phased structure (00_ROOT, 01_PHASE1, 02_GOVERNANCE,
  03_CONTINUITY, 04_SURFACES)

  ---
  F. WRITING / PUBLISHING CORPUS

  Desktop/CODEX/   ← PRIMARY WRITING HUB (no git)
  ├── 2026-03-12_PUBLISHER_BOOK_PACKAGES/
  ├── 2026 - Martin Lepage - THE WEATHER BENEATH THE WALLS/
  ├── AI_Anxiety_Recursive_Governance/
  ├── Trust_Advantage_Analysis/
  ├── Legitimacy_Machines_Altors_of_Control/
  ├── Paper on Buffy The Vampire Slayer Ethics/
  ├── Paper on Recursive Deterministic AI Governance/
  ├── Recurso/
  ├── BUFFY/
  ├── Breath_of_the_Astral_Year/
  ├── SocialCompass_Agatha/
  ├── Papers/, Publications/, Academia Saved Papers/, BOOKS/
  ├── hephaistos-pass/, Downloads_Writing_Imports/, TENTATIVE/
  ├── CODEX_DEDUPE_REPORT_2026-03-17.json
  ├── CODEX_WRITING_PROJECTS_MANIFEST_2026-03-16.md
  ├── MASTER_PROJECT_TRACKER_2026-03-17.md
  └── codex-writing-system.ps1, codex-functions.ps1

  /home/cerebrhoe/manuscripts/
  ├── le-palais-sous-les-racines-kdp/
  ├── the-palace-under-the-root-kdp/
  └── whos-the-boob-whos-the-trap/

  Documents/Séries Articles Pharos/
  Documents/Publications/
  Documents/PHAROS METHOD REPOSITORY/
  Documents/PAPERS_MASTER_CONSOLIDATED_2026-04-10/

  ---
  G. AGENT / TOOL PROJECTS

  github.com/martinlepage26-bit/glammy-site.git
  └── /home/cerebrhoe/repos/glammy-site/

  Desktop/Hermes Dashboard/    ← Python desktop app (SEPARATE from
  governance Hermes)
  ├── hermes.py
  ├── HERMES.exe  (compiled)
  ├── dashboard.html, Manus Project Dashboard.html
  └── .backup/, build/, dist/, __pycache__/

  /home/cerebrhoe/document-organizer-app/   (no remote confirmed)
  ├── document_organizer.spec, config/, output/

  /home/cerebrhoe/perso-review/   (no remote confirmed)
  ├── apps/, backend/, docs/, output/

  /home/cerebrhoe/dr-sort/
  ├── apps/, backend/, docs/, tmp/

  /home/cerebrhoe/tmp/sante-france/  ← git repo in tmp
  (health-related project)

  /mnt/c/Users/softinfo/Documents/GitHub/   ← GitHub Desktop clones
  ├── CLI-Anything-main/        (Claude plugin)
  ├── OpenSpace-main/           (openspace plugin)
  ├── claude-peers-mcp-main/    (MCP server)
  ├── pharos-ops-dashboard/     (ops dashboard)
  ├── autoresearch-master/      ← DUPLICATE (also at Windows home
  root)
  └── Downloads Intake 2026-03-29/

  /home/cerebrhoe/claude-peers-mcp/    ← MCP server (Linux version)
  /home/cerebrhoe/ai_governance_audio/
  /home/cerebrhoe/astrology-gaialogy/
  /home/cerebrhoe/fantasy-expansion/
  /home/cerebrhoe/competitor-analysis/
  /mnt/c/Users/softinfo/autoresearch-master/   ← ML training (no
  git, dup)

  ---
  H. OBSIDIAN VAULTS (6 locations)

  1. /mnt/c/Users/softinfo/Documents/EMERAULD/          ← active
  (.obsidian present)
  2. /mnt/c/Users/softinfo/Documents/PHAROS-ARCHIVE/    ← archive
  vault (.obsidian present)
  3. /mnt/c/Users/softinfo/Documents/PHAROS METHOD REPOSITORY/
  (.obsidian present)
  4. /home/cerebrhoe/Obsidian Vault/                    ← minimal
  (Welcome.md only)
  5. /home/cerebrhoe/obsidian-agent-vault/               ← agent
  vault
  6. /home/cerebrhoe/.obsidian                           ← home-dir
   level (no canonical vault here)

  ---
  I. PERSONAL ASSISTANT (split)

  /mnt/c/Users/softinfo/Desktop/personal-assistant/     ← scripts/,
   services/, vault/
  /home/cerebrhoe/personal-assistant/                   ← mem/,
  rag/, scripts/, services/,

  trismegiste/, vault/ (different structure)

  ---
  J. TRACKERS (Windows Documents root)

  MASTER TRACKER (recreated from MASTER PACK 4).md   ← primary
  cross-session tracker
  MASTER TRACKER (recreated from MASTER PACK 4).csv  ← CSV export
  of above
  PHAROS-AI CHANGE TRACKER.md
  METHOD TRACKER.md
  CLIENT ACCOUNTS TRACKER.md
  MARTIN-SITE CHANGE TRACKER.md

  ---
  K. ROOT CLUTTER ZONES

  Windows home root (/mnt/c/Users/softinfo/):
  backend_test.py, build_pharos_forms.py,
  build_pharos_master_sop.py, build_pharos_pdfs.py
  design_guidelines.json    ← orphaned? duplicate of pharos-suite
  version?
  data.tar                  ← 53MB archive, undocumented
  diskpart_wsl_check*.txt   ← diagnostic artifacts
  gsd-commands.txt          ← 102KB command log
  CLAUDE.md                 ← CODEX router (intentional)
  README.md
  __pycache__/
  frontend/                 ← React stub (no git, only config
  files, no src)
  build/                    ← empty
  memory/                   ← small memory doc set
  chrome_secure_install/

  Linux home root (/home/cerebrhoe/):
  Loose governance files: HEPHAISTOS.md, QUEEN-KEYPORT.md,
  HERMES.md, ORCHESTRATION.md, etc.
  Loose screenshots: index-*.png, pharos-*.png, cq-*.png (20+
  files)
  Loose scripts: make_trismegiste_icon.py, recover_trismegiste.sh,
  document_sorter.py
  Loose data: lightrag.log, inderscience_submission_notes.md,
  package.json, package-lock.json
  Misrouted files: ":USERPROFILE\Downloads\Obsidian.exe",
  "C:\Users\softinfo\diskpart_wsl_check.txt"
                   → Windows path fragments written into Linux
  filesystem (shell errors)

  ---
  III. PROJECT REGISTER (with confidence ratings)

  Project: pharos-suite
  Location(s): Linux/repos/pharos-suite (canonical), Linux/cleanup,

    Windows/PHAROS-SUITE
  Remote: pharos-suite.git
  Status: Active — 3 clones
  Confidence: High
  ────────────────────────────────────────
  Project: pharos-ai
  Location(s): Linux/PHAROS-SUITE/repos/pharos-ai
  Remote: unverified
  Status: Active sub-project
  Confidence: Medium
  ────────────────────────────────────────
  Project: AurorA (module)
  Location(s): Linux/PHAROS-SUITE/repos/AurorA (no .git)
  Remote: —
  Status: Absorbed into pharos-suite
  Confidence: High
  ────────────────────────────────────────
  Project: CompassAI (module)
  Location(s): Linux/PHAROS-SUITE/repos/CompassAI (no .git)
  Remote: —
  Status: Absorbed into pharos-suite
  Confidence: High
  ────────────────────────────────────────
  Project: AurorA (legacy standalone)
  Location(s): Windows home dir ghost tracking
  Remote: AurorA.git
  Status: Stale — ghost tracking
  Confidence: High
  ────────────────────────────────────────
  Project: martin-lepage-site
  Location(s): Linux/martin-lepage-site + 2 tmp copies
  Remote: martinlepage26-bit.github.io.git
  Status: Active
  Confidence: High
  ────────────────────────────────────────
  Project: Governess
  Location(s): Windows/Governess (primary) + 2 archive copies
  Remote: Governess
  Status: Fragmented
  Confidence: High
  ────────────────────────────────────────
  Project: AutoResearchClaw
  Location(s): Nested in Governess (third-party clone)
  Remote: aiming-lab/AutoResearchClaw.git
  Status: Third-party eval
  Confidence: High
  ────────────────────────────────────────
  Project: zep
  Location(s): Nested in Governess (third-party clone)
  Remote: getzep/zep.git
  Status: Third-party eval
  Confidence: High
  ────────────────────────────────────────
  Project: hephaistos
  Location(s): Linux/hephaistos (no remote)
  Remote: none
  Status: Active — local only
  Confidence: High
  ────────────────────────────────────────
  Project: governance-project
  Location(s): Linux/governance-project
  Remote: none
  Status: Active governance work
  Confidence: High
  ────────────────────────────────────────
  Project: glammy-site
  Location(s): Linux/repos/glammy-site
  Remote: glammy-site.git
  Status: Unknown activity
  Confidence: Medium
  ────────────────────────────────────────
  Project: agency-lotus-clone
  Location(s): Linux/_archive/
  Remote: Agency.git
  Status: Archived
  Confidence: High
  ────────────────────────────────────────
  Project: govern (shell)
  Location(s): Linux/_archive/Governess_empty_shell_backup
  Remote: govern.git
  Status: Stale backup
  Confidence: Medium
  ────────────────────────────────────────
  Project: document-organizer-app
  Location(s): Linux/
  Remote: none confirmed
  Status: Unknown
  Confidence: Low
  ────────────────────────────────────────
  Project: perso-review
  Location(s): Linux/
  Remote: none confirmed
  Status: Unknown
  Confidence: Low
  ────────────────────────────────────────
  Project: dr-sort
  Location(s): Linux/
  Remote: none
  Status: Sub-project of martin site
  Confidence: Medium
  ────────────────────────────────────────
  Project: HERMES Dashboard
  Location(s): Desktop/Hermes Dashboard
  Remote: none
  Status: Active desktop app
  Confidence: High
  ────────────────────────────────────────
  Project: sante-france
  Location(s): Linux/tmp/
  Remote: unverified
  Status: Unknown, in tmp
  Confidence: Low
  ────────────────────────────────────────
  Project: autoresearch-master
  Location(s): Windows home + Documents/GitHub (dup)
  Remote: none
  Status: Duplicate, no git in root
  Confidence: High
  ────────────────────────────────────────
  Project: CODEX Writing Hub
  Location(s): Desktop/CODEX
  Remote: none
  Status: Active writing system
  Confidence: High
  ────────────────────────────────────────
  Project: pharos-ops-dashboard
  Location(s): Documents/GitHub/pharos-ops-dashboard
  Remote: unverified
  Status: Tool project
  Confidence: Medium
  ────────────────────────────────────────
  Project: CLI-Anything
  Location(s): Documents/GitHub/CLI-Anything-main
  Remote: unverified
  Status: Claude plugin
  Confidence: Medium
  ────────────────────────────────────────
  Project: claude-peers-mcp
  Location(s): Documents/GitHub/ + Linux/
  Remote: unverified
  Status: MCP server
  Confidence: Medium
  ────────────────────────────────────────
  Project: manuscripts
  Location(s): Linux/manuscripts/
  Remote: none
  Status: Creative/publishing
  Confidence: High
  ────────────────────────────────────────
  Project: EMERAULD
  Location(s): Documents/EMERAULD
  Remote: none
  Status: Obsidian vault (active)
  Confidence: High
  ────────────────────────────────────────
  Project: personal-assistant
  Location(s): Desktop/ + Linux/ (split)
  Remote: none
  Status: Fragmented
  Confidence: High
  ────────────────────────────────────────
  Project: fantasy-expansion
  Location(s): Linux/
  Remote: none
  Status: Creative project
  Confidence: Low
  ────────────────────────────────────────
  Project: astrology-gaialogy
  Location(s): Linux/
  Remote: none
  Status: Unknown
  Confidence: Low
  ────────────────────────────────────────
  Project: competitor-analysis
  Location(s): Linux/
  Remote: none
  Status: Research
  Confidence: Low

  ---
  IV. FRAGMENTATION AND DUPLICATION REPORT

  Critical (structural risk)

  1. Windows home dir is a live git repo (AurorA ghost)
  - /mnt/c/Users/softinfo/ has .git tracking AurorA.git
  - Status: hundreds of deleted files (D prefix in git status)
  - Risk: any git checkout, git restore, or accidental git
  operation could overwrite or ghost-delete files in
  C:\Users\softinfo\
  - This is almost certainly unintentional persistence from an
  early project setup
  - Evidence: 4 commits only; AurorA was renamed and absorbed into
  pharos-suite months ago

  2. pharos-suite exists in 3 clones simultaneously
  - Linux canonical (active WIP branch)
  - Linux cleanup (same remote, separate branch)
  - Windows mirror (main branch, partially diverged)
  - Risk: patches applied in Windows may not be in the Linux
  canonical; cleanup branch may or may not be merged

  3. Governess_empty_shell_backup points to govern.git, NOT
  Governess
  - These are different GitHub repos
  - The backup was not made from the same remote as the primary
  - Inference (labeled as inference): govern.git may be an earlier
  or parallel Governess incarnation

  Significant (fragmentation)

  4. autoresearch-master exists twice on Windows
  - /mnt/c/Users/softinfo/autoresearch-master/ — no git, data files
  - /mnt/c/Users/softinfo/Documents/GitHub/autoresearch-master/ —
  with git
  - These may be out of sync

  5. personal-assistant split across two locations
  - Desktop version: scripts/, services/, vault/
  - Linux version: mem/, rag/, scripts/, services/, trismegiste/,
  vault/
  - Different internal structure — not clear which is authoritative

  6. 6 Obsidian vault locations with no clear canonical
  - 3 on Windows (EMERAULD, PHAROS-ARCHIVE, PHAROS METHOD
  REPOSITORY)
  - 3+ on Linux (Obsidian Vault minimal, obsidian-agent-vault,
  .obsidian at root)
  - The EMERAULD vault on Windows appears most active

  7. Governance files loose at Linux root
  - HEPHAISTOS.md, QUEEN-KEYPORT.md, HERMES.md, etc. exist both in
  /home/cerebrhoe/hephaistos/ (git repo) AND at /home/cerebrhoe/
  (root loose files)
  - If these diverge in content, the loose files may be stale
  exports

  8. martin-lepage-site has 2 tmp working copies
  - /home/cerebrhoe/tmp/martinlepage26-bit.github.io-work/ and
  mlepage.github.io/ are working copies in tmp
  - Likely from deploy experiments — but git state unverified

  Moderate (clutter)

  9. tmp/ is functioning as a secondary project graveyard
  - /home/cerebrhoe/tmp/ contains: echo-deploy, lotus-deploy,
  sante-france (git), pharos-ai-results, various one-off
  audit/deploy folders
  - sante-france is a git repo sitting in tmp — its residency there
   suggests it never graduated to a proper home

  10. MODELS folder on Desktop has unmapped sub-projects
  - paper.builder, pdf_sorter_v1, HENRY, VOICE 11 — no git, no
  documented relationship to main projects

  11. HEPHAISTOS_BUILD artifacts
  - EXTRACTED/, MASTERxMASTERxMASTER_REBUILT/ — build artifacts
  from earlier HEPHAISTOS work
  - Should probably be in archive or documented as such

  12. Root screenshot files
  - 20+ index-.png, pharos-.png, etc. at Linux root — deploy
  verification artifacts
  - Useful at the time, now clutter at the repo root

  13. Windows misrouted files
  - Files named C:\Users\softinfo\diskpart_wsl_check.txt and
  :USERPROFILE\Downloads\Obsidian.exe exist as literal filenames in
   the Linux filesystem — these are shell redirection errors that
  created files with Windows path strings as names

  ---
  V. PROPOSED CANONICAL TARGET STRUCTURE

  This is a proposed clean topology. It is a recommendation only —
  no modifications made.

  /home/cerebrhoe/                          ← Linux home (primary
  workspace)
  │
  ├── PHAROS-SUITE/                         ← platform mono-repo
  (keep)
  │   └── repos/
  │       ├── pharos-suite/  (canonical)    ← one active clone, on
  main
  │       ├── pharos-ai/                    ← pharos-ai.ca
  sub-project
  │       ├── AurorA/                      ← AurorA module
  (in-repo, no .git needed)
  │       └── CompassAI/                    ← same
  │
  ├── martin-lepage-site/                   ← keep (canonical)
  ├── hephaistos/                           ← keep (local
  governance repo)
  ├── governance-project/                   ← keep
  ├── repos/                                ← symlinks only (no
  duplication)
  │   └── (symlinks to PHAROS-SUITE/repos/* as needed)
  │
  ├── manuscripts/                          ← creative writing
  (keep)
  ├── dr-sort/                              ← martin-site
  sub-project (keep)
  ├── personal-assistant/                   ← consolidate with
  Desktop version
  │
  ├── tools/                                ← tool projects
  │   ├── document-organizer-app/
  │   ├── glammy-site/
  │   └── claude-peers-mcp/
  │
  ├── _archive/                             ← keep (clearly
  labeled)
  │   ├── Governess_duplicate_2026-03-18/
  │   ├── Governess_empty_shell_backup/
  │   └── agency-lotus-clone/
  │
  └── tmp/                                  ← ephemeral only (no
  git repos reside here)

  C:\Users\softinfo\                        ← Windows home (support
   / doc layer)
  │
  ├── PHAROS-SUITE/       ← DECISION NEEDED: keep as secondary
  mirror or remove
  ├── Governess/          ← PRIMARY Windows repo (keep if active)
  ├── Desktop/
  │   ├── CODEX/          ← writing hub (keep, consider
  git-tracking it)
  │   └── Hermes Dashboard/  ← rename to avoid confusion with agent
   Hermes
  │
  ├── Documents/
  │   ├── EMERAULD/       ← primary Obsidian vault (keep)
  │   ├── PHAROS-ARCHIVE/ ← tracker archive (keep, reduce vault
  redundancy)
  │   ├── PHAROS_PAPERS_DB/
  │   ├── PAPERS_MASTER_CONSOLIDATED_2026-04-10/
  │   ├── GitHub/         ← GitHub Desktop clones (keep as
  read-only cache)
  │   └── [trackers]      ← keep at Documents root
  │
  └── [root loose files]  ← clean up: move scripts to project homes
   or delete

  ---
  VI. FINAL TRIAGE

  Roots (canonical, authoritative — do not disturb)

  - /home/cerebrhoe/PHAROS-SUITE/repos/pharos-suite/ — pharos-suite
   canonical
  - /home/cerebrhoe/martin-lepage-site/ — Martin site canonical
  - /home/cerebrhoe/hephaistos/ — governance stack canonical
  - /mnt/c/Users/softinfo/Governess/ — Governess canonical
  (primary)
  - /mnt/c/Users/softinfo/Documents/EMERAULD/ — primary active
  Obsidian vault
  - /mnt/c/Users/softinfo/Desktop/CODEX/ — writing system hub

  Duplicates requiring decision

  Item: pharos-suite
  Copies: 3 clones (Linux canon + cleanup + Windows)
  Recommended action: Consolidate to 1 canonical; archive or delete

    others after verifying no uncommitted work
  ────────────────────────────────────────
  Item: autoresearch-master
  Copies: 2 Windows copies
  Recommended action: Determine canonical; delete the non-git root
    version or merge
  ────────────────────────────────────────
  Item: personal-assistant
  Copies: 2 (Desktop + Linux)
  Recommended action: Determine which is live; consolidate
  ────────────────────────────────────────
  Item: Governess
  Copies: Primary + archive-dup + shell-backup
  Recommended action: Keep primary; archive dup already labeled;
    verify govern.git identity and document separately
  ────────────────────────────────────────
  Item: martin-lepage-site tmp copies
  Copies: 2 in tmp/
  Recommended action: Delete if nothing uncommitted
  ────────────────────────────────────────
  Item: Governance loose files at Linux root
  Copies: Loose vs. hephaistos/ repo
  Recommended action: Verify they match repo HEAD; delete
  duplicates
    if matched
  ────────────────────────────────────────
  Item: Obsidian vaults
  Copies: 6 locations
  Recommended action: Reduce to 1 canonical (EMERAULD most active);

## Archive Closeout Addendum

- 2026-04-20 21:35 EDT — Archive closeout: removed live Windows-home duplicates (`/mnt/c/Users/softinfo/AutoResearchClaw`, `/mnt/c/Users/softinfo/zep`) and the Linux-side tools copy (`/home/cerebrhoe/document-organizer-app`) from active paths; archive copies now live under the existing `/home/cerebrhoe/_archive/` tree (`Governess_empty_shell_backup/*`, `document-organizer-app_2026-04-21`) with manifest at `/home/cerebrhoe/_archive/MANIFEST_2026-04-21.md`.
