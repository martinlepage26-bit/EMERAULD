---
type: note
title: pharos-inventory-2026-04-18_b9b1ffde
aliases:
- graphify-out/converted/pharos-inventory-2026-04-18_b9b1ffde
tags:
- note
- graphify-out
- converted
- delete
- dormant
- documents
- reference
- cleanup
- color-teal
status: active
created: '2026-04-18'
updated: '2026-06-26'
vault_area: graphify-out
canonical_path: graphify-out/converted/pharos-inventory-2026-04-18_b9b1ffde.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

<!-- converted from pharos-inventory-2026-04-18.xlsx -->

## Sheet: Inventory
| Name | Location | Type | Status | Last modified | Ship priority | Next action | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MARTIN-SITE (change tracker) | ~\Documents\MARTIN-SITE CHANGE TRACKER.md | Tracker | ACTIVE | 2026-04-18 | 1 | Open and share with me — we build the ship-plan from what you've already been tracking | Touched TODAY, 23 KB. This is the website you mentioned. |
| MASTER TRACKER | ~\Documents\MASTER TRACKER (recreated from MASTER PACK 4).md | Tracker | ACTIVE | 2026-04-18 | 1 | Treat as source-of-truth; everything below should reconcile with this | 37 KB, touched today. Name says it was RECREATED — suggests you lost an earlier one. |
| PHAROS-SUITE | ~\PHAROS-SUITE | Project (core) | ACTIVE | 2026-04-16 | 1 | Needs security + deployability audit in next session | Main Pharos infrastructure. |
| pharos-api | ~\pharos-api | Project (core) | ACTIVE | 2026-04-15 | 1 | Inventory endpoints, verify secrets live only in env, confirm deploy target | API layer for Pharos. |
| PHAROS METHOD REPOSITORY | ~\Documents\PHAROS METHOD REPOSITORY | Docs / Method | ACTIVE | 2026-04-15 | 2 | Decide: is this the canonical method doc or a working copy? |  |
| PHAROS_PAPERS_DB | ~\Documents\PHAROS_PAPERS_DB | Docs / Research | ACTIVE | 2026-04-14 | 2 | Consolidate with PAPERS_MASTER_CONSOLIDATED (likely duplicate intent) |  |
| PAPERS_MASTER_CONSOLIDATED_2026-04-10 | ~\Documents\PAPERS_MASTER_CONSOLIDATED_2026-04-10 | Docs / Research | ACTIVE | 2026-04-15 | 2 | Single source of truth for papers — archive the older PHAROS_PAPERS_DB once reconciled | Dated folder name = snapshot habit. Good. |
| Governess | ~\Governess | Project | ACTIVE | 2026-04-16 | 2 | Decide scope — separate product or Pharos sub-component? |  |
| BRAINiaC | ~\Documents\BRAINiaC | Project | ACTIVE | 2026-04-16 | 2 | Define shipping target or park |  |
| INTERNAL | ~\Documents\INTERNAL | Working folder | ACTIVE | 2026-04-13 | - | Keep — looks like ongoing governance work | Pinned to Quick Access. |
| NEW AGATHA STRESS-TEST | ~\Documents\NEW AGATHA STRESS-TEST | Test suite | ACTIVE | 2026-04-12 | 2 | Review FAIL files — Agatha currently failing per filenames | Files `FULL ST NEW AGATHA-FAIL.txt`, `stress0test NEW AGATHA - FAIL.txt` suggest unresolved failures. |
| provisional-arbitration-charter (v1.1 + v1) | ~\Documents | Governance doc | ACTIVE | 2026-04-14 | 2 | Freeze v1.1 as current; move v1 to archive |  |
| AutoResearchClaw | ~\AutoResearchClaw | Project | DORMANT | 2026-03-17 | - | Merge or kill — you have TWO copies (this and `autoresearch-master`) | Likely newer copy. |
| autoresearch-master | ~\autoresearch-master | Zip extract | DORMANT | 2026-03-25 | - | Archive to D: — this is almost certainly a zip extract of AutoResearchClaw | Name pattern `-master` = unpacked GitHub zip. |
| CompassAI | ~\CompassAI | Project | DORMANT | 2026-03-01 | - | Park or kill — untouched 6+ weeks |  |
| chrome_secure_install | ~\chrome_secure_install | Utility folder | DORMANT | 2026-03-17 | - | Review — read README to know purpose before deleting |  |
| zep | ~\zep | Library clone | DORMANT | 2026-03-22 | - | If just a reference clone, delete — you can `git clone` again anytime |  |
| dev | ~\dev | Catch-all | DORMANT | 2026-02-22 | - | Audit contents — two-month-old catch-alls rarely contain live work |  |
| AI GOVERNANCE LIBRARY | ~\Documents\AI GOVERNANCE LIBRARY | Reference | DORMANT | 2026-03-29 | - | Keep as reference; move to D:\ if not actively consulted |  |
| bundle | ~\Documents\bundle | Unknown | DORMANT | 2026-03-28 | - | Investigate — name too generic to judge |  |
| Séries Articles Pharos | ~\Documents\Séries Articles Pharos | Content draft | DORMANT | 2026-04-12 | - | Decide publishing target |  |
| Publications | ~\Documents\Publications | Content | DORMANT | 2026-04-11 | - | Merge with PAPERS_MASTER_CONSOLIDATED? |  |
| frontend | ~\frontend | Orphan | STALE | 2026-03-03 | - | Delete or move to project folder — bare `frontend/` in home is a red flag |  |
| tests | ~\tests | Orphan | STALE | 2026-03-03 | - | Delete or move into owning project |  |
| package.json + package-lock.json + yarn.lock + node_modules + server.py + scan_and_upload.py + requirements.txt + design_guidelines.json + README.md | ~\ (home root) | Abandoned project | STALE | 2026-03-02/03 | - | This is a Node+Python project that was started in your HOME directory. Move to a real folder or delete. | Home root is not a project folder. Having this here means a future `rm -rf` in home would nuke unrelated things. |
| Dadroit JSON Generator | ~\Documents\Dadroit JSON Generator | 3rd-party tool | STALE | 2026-03-03 | - | Uninstall or keep — not your code |  |
| Zoom | ~\Documents\Zoom | 3rd-party tool | STALE | 2020-12-02 | - | 5-year-old Zoom folder — safe to delete |  |
| ~ folder (literal tilde) | ~\~ | Shell mistake | CLEANUP | 2026-04-06 | - | Delete — this was created by a shell command that didn't expand `~` correctly | Harmless but embarrassing. |
| __pycache__ | ~\__pycache__ | Build cache | CLEANUP | 2026-03-03 | - | Delete — regenerates automatically |  |
| node_modules (in home root) | ~\node_modules | Build cache | CLEANUP | 2026-04-16 | - | Delete — a home-root node_modules = side effect of the abandoned home-root project | Can be hundreds of MB. |
| .venv (in home root) | ~\.venv | Build cache | CLEANUP | 2026-02-10 | - | Delete — home-root venv is a smell; venvs belong inside project folders |  |
| output | ~\output | Tool output | CLEANUP | 2026-04-12 | - | Scan, save anything interesting, then delete |  |
| tmp | ~\tmp | Tool output | CLEANUP | 2026-04-11 | - | Delete |  |
| __pycache__ in multiple subfolders | various | Build cache | CLEANUP | - | - | Delete recursively during cleanup session |  |
| memory | ~\memory | Tool output | CLEANUP | 2026-04-05 | - | Determine owner (Claude Code? Zep?) then delete or move |  |
| Apple | ~\Apple | Unknown | CLEANUP | 2026-04-10 | - | Investigate — bare `Apple/` in home root is suspicious |  |
| .env | ~\.env | Secret file | SECURITY-FLAG | 2026-03-23 | 1 | Move into the project that owns it. NEVER leave in home root. | Could contain API keys that would be included in any backup of your profile. |
| .cloudflare-govern-ai.env | ~\.cloudflare-govern-ai.env | Secret file | SECURITY-FLAG | 2026-03-06 | 1 | Move to the Cloudflare-governance project folder |  |
| set-cloudflare-e...bat | ~\set-cloudflare-e... .bat | Env-set script | SECURITY-FLAG | 2026-03-06 | 2 | Audit the contents — .bat that sets env vars may be hardcoding secrets |  |
| .codex | ~\.codex | Tool config | SECURITY-FLAG | 2026-04-03 | 2 | Check whether it contains auth tokens |  |
| claude-md-snapshots | ~\Documents\claude-md-snapshots | Reference | REFERENCE | 2026-04-05 | - | Keep — useful history |  |
| Claude | ~\Documents\Claude | Reference | REFERENCE | 2026-04-04 | - | Review — might be duplicates of claude-md-snapshots |  |
| LinkedIn | ~\Documents\LinkedIn | Reference | REFERENCE | 2026-04-06 | - | Keep |  |
| CVs | ~\Documents\CVs | Career assets | REFERENCE | 2026-04-15 | - | Keep |  |
| GitHub | ~\Documents\GitHub | Workspace | REFERENCE | 2026-04-15 | - | Keep — likely your git clones |  |
| WindowsPowerShell | ~\Documents\WindowsPowerShell | Profile/config | SYSTEM | 2026-04-09 | - | Leave alone |  |
| Agatha-Dottie-Mobi | D:\Agatha-Dottie-Mobi | Archive / mobile build | ARCHIVE | ? | - | Confirm what this is — appears mobile-oriented |  |
| CODEX | D:\CODEX | Reference library | REFERENCE | ? | - | Keep as reference safe | Also appears on Desktop as a shortcut. |
| LIBRARY | D:\LIBRARY | Reference library | REFERENCE | ? | - | Keep |  |
| MASTER PACK | D:\MASTER PACK | Reference / Backup | ARCHIVE | ? | - | Confirm — name suggests a versioned bundle; keep most recent, archive or delete older |  |
| MASTER REFERENCE SAFE | D:\MASTER REFERENCE SAFE | Reference library | REFERENCE | ? | - | Keep as the canonical reference safe | Good naming — already treating D: as an archive drive. |
| MODELS | D:\MODELS | Model weights/assets | REFERENCE | ? | - | Keep on D: — shouldn't be on SSD anyway |  |
| claude-mem-main.zip | D:\claude-mem-main.zip | Zip archive | ARCHIVE | ? | - | Unpack only if you intend to use; otherwise delete — you can re-download |  |
| LightRAG-main.zip | D:\LightRAG-main.zip | Zip archive | ARCHIVE | ? | - | Same — delete unless actively used |  |
| obsidian-agent-vault-launch-v2.zip | D:\obsidian-agent-vault-launch-v2.zip | Zip archive | ARCHIVE | ? | - | Same — delete unless actively used |  |
| E:\ MLONF3 | E:\ | Drive (unknown role) | ? | ? | - | Scan next session — we don't know what's on this drive yet |  |
| G:\ Mon disque (Google Drive) | G:\ | Cloud drive mirror | ? | ? | - | Scan next session — often hosts decks, half-finished proposals |  |
| H:\ SDHC | H:\ | SD card | ? | ? | - | Check if contents should move to D: or be erased |  |
## Sheet: Legend
| Status | Meaning | Your default move |
| --- | --- | --- |
| ACTIVE | Touched in the last ~7 days. Real ongoing work. | Keep; consider for ship list. |
| DORMANT | Untouched 3-6 weeks. Unclear if abandoned or just paused. | Decide: ship, park, or delete. |
| STALE | Untouched 6+ weeks OR in a wrong location. | Usually delete or archive. |
| CLEANUP | Zero-value noise — caches, shell mistakes, tmp output. | Delete. |
| REFERENCE | Passive assets you consult but don't edit. | Keep; consider moving to D:\. |
| SYSTEM | OS/tool config — don't touch. | Leave alone. |
| ARCHIVE | Old snapshot, already on D:\ or should be. | Verify then freeze. |
| SECURITY-FLAG | File in the wrong place that could leak secrets. | Move out of home root before next backup. |
| ? | I didn't see this drive/folder — needs a follow-up scan. | Schedule scan. |
## Sheet: Drives
| Drive | Label | Role (proposed) | Status | Notes |
| --- | --- | --- | --- | --- |
| C: | Windows-SSD | OS + active projects only | Overloaded | Home folder has 66 top-level items + Documents has 101. Needs cleanup. |
| D: | BACKEND | Reference safe + archives | Good naming in place | MASTER REFERENCE SAFE, LIBRARY, MODELS, CODEX suggest a working archive system. Audit then formalize. |
| E: | MLONF3 | Unknown | Needs scan | Purpose unclear — check contents next session. |
| G: | Mon disque | Google Drive (cloud mirror) | Unmapped | Often holds decks + half-finished proposals. Scan if ship-list references anything cloud-only. |
| H: | SDHC | SD card | Transient | Check contents, decide keep or wipe. |