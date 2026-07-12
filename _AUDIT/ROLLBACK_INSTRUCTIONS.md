---
type: audit-doc
title: ROLLBACK INSTRUCTIONS
tags:
- audit
- vault
- rollback
- emerauld
status: active
created: '2026-07-10'
updated: '2026-07-10'
vault_area: _AUDIT
canonical_path: _AUDIT/ROLLBACK_INSTRUCTIONS.md
---

# ROLLBACK INSTRUCTIONS

These instructions apply only to the 2026-07-10 audit/reorganization pass.

## Files created in this pass

Remove these if Martin wants a full rollback of the new artifacts:

- `_AUDIT/`
- `_INDEXES/CRITICAL_KNOWLEDGE_INDEX.md`
- `_QUARANTINE/README.md`

## Files edited in this pass

These files had no pre-existing user modifications in the initial scoped git check and can be restored directly from git if Martin wants to revert this pass:

- `Welcome.md`
- `index.md`
- `wiki/Home.md`
- `Areas/Writing/Writing and Novels MOC.md`

## Suggested rollback commands

```bash
cd /home/martin/EMERAULD
rm -rf _AUDIT _INDEXES _QUARANTINE
git restore -- Welcome.md index.md wiki/Home.md "Areas/Writing/Writing and Novels MOC.md"
```

## Warnings

- Do not run broader restore commands against the whole repository. The worktree was already dirty before this pass.
- Do not restore or reset inside `PEER-REVIEW/` or `projects/patent-workbench/` unless Martin explicitly asks.
