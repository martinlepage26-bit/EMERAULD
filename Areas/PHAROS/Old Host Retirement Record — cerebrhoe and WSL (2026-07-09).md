---
type: note
title: Old Host Retirement Record — cerebrhoe and WSL (2026-07-09)
tags:
- note
- governance
- infrastructure
- retirement
status: active
domain: governance
created: '2026-07-09'
updated: '2026-07-09'
vault_area: Areas/PHAROS
---

# Old Host Retirement Record — cerebrhoe and WSL (2026-07-09)

Operator decision (Martin, 2026-07-09, delegated resolution of the Argus/BOWIE audit
residuals). This note is the single authority for what the old-host references in this
vault mean. Any vault note still containing `/home/cerebrhoe/...` or
`/mnt/c/Users/softinfo/...` paths should be read against this record.

> [!warning] Contradiction detected
> [[Skill Corpus — Complete Live Index (260 Active Skills)]] (updated 2026-06-26) presents itself as a current filesystem inventory of 260 active skill entries at `.codex/skills/`, and [[Claude Code Skill Corpus]] describes the same corpus as live. The record shows (verified 2026-07-09) that only 25 skill directories exist at `/home/martin/.codex/skills/` on this host. Reconciliation: this Retirement Record supersedes the live-index claims. The 260-entry index was accurate for the retired WSL host on 2026-05-06 and stays as documentation of the retired corpus; it is not a current inventory. Flagged 2026-07-09 by the nightly consolidation pass; older notes kept intact per the no-deletion rule.

## The record shows

- The WSL host (`/home/cerebrhoe` on Ubuntu under Windows 11, Windows mount
  `/mnt/c/Users/softinfo`) is retired. The current host is Linux, home `/home/martin`.
- The old Codex skill corpus (200+ documented directories under
  `/home/cerebrhoe/.codex/skills/`, counted at 250 in the 2026-04-23 agent audit) did
  not migrate. This host carries 25 directories at `/home/martin/.codex/skills/`. No
  backup of the full corpus exists on this host (verified 2026-07-09).
- Decision: the corpus is **retired, not lost-pending-recovery**. Vault notes under
  `wiki/skills/` and elsewhere that document those skills are records of a retired
  corpus. They stay as documentation; the skills they describe are not installed and
  are not expected to return unless deliberately rebuilt.
- The 76 vault files referencing the `/mnt/c/Users/softinfo` WSL mount are likewise
  historical. No mechanical path mapping to this host exists. Decision: no bulk
  rewrite; treat as historical references covered by this record, fix opportunistically
  when a note is next edited for content.

## What was cleaned vs kept (2026-07-08/09 passes)

- 214 live vault files had mechanical `/home/cerebrhoe/ → /home/martin/` fixes where
  the target exists (BOWIE, backup + manifest at `~/.agents/hephaistos/bowie/`).
- The canon repo (`~/.agents/hephaistos/`) and the vault's governance mirrors were
  cleaned in that order (canon first, mirrors to match).
- Kept on purpose: dated audit records, archive notes, and sentences whose point is
  that the old path is dead. A `cerebrhoe` mention inside a historical record is
  correct, not stale.

## Unresolved

- Individual `wiki/skills/` notes are not annotated one-by-one; this record covers
  them collectively. If a retired skill is rebuilt, update its note and this record.
