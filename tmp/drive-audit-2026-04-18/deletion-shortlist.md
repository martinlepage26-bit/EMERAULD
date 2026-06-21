# Drive G — Ranked Deletion Shortlist
Generated: 2026-04-18

Tiers are ordered by confidence and storage impact.
Do not delete without reviewing each tier once — but within each tier, all items listed are safe to batch-delete.

---

## Tier 1 — Zero-risk, batch-delete now (~negligible size, zero content value)

### 94 × desktop.ini
Windows Explorer metadata files. No content. Safe to delete all 94 instances across Drive G and Drive F.
Pattern: `G:\Mon disque\**\desktop.ini` and `F:\Mon disque\desktop.ini`

### 3 × .DS_Store + 3 × ._.DS_Store
macOS Finder metadata left over from a Mac or Time Machine backup. Zero content.
Locations: `G:\Mon disque\KK\Futurama\Futurama Season 4\`, `Season 5\`, `Season 1\`

### ~100 × *.télécharger files
Partial Chrome/Firefox download residue from a saved webpage scrape.
All live in one folder: `G:\Mon disque\AI\SEALED CARD MASTER MARKDOWN\SAKURA-SC1\(99+) Butler-undoing gender_files\`
The entire `_files` subfolder is browser residue; the only thing worth keeping in that folder is the `.html` file itself if you want the saved page.

**Tier 1 total: ~100+ files, ~negligible bytes freed (all tiny)**

---

## Tier 2 — Confirmed "Copie de" duplicates in Impôts (~safe, review pair once)

These are exact copies auto-named by Google Drive "Make a copy." Keep the original, delete the `Copie de` version unless you remember changing the copy.

| Keep | Delete |
|------|--------|
| `2022-TousLesFeuillets.pdf` | `Copie de 2022-TousLesFeuillets.pdf` |
| `2023-TousLesFeuillets.pdf` | `Copie de 2023-TousLesFeuillets.pdf` |
| `Avis_de_nouvelle_cotisation_2023_09_11_05_57_29_452878.pdf` | `Copie de Avis_de_nouvelle_cotisation_...pdf` |
| `QC2022Avis.pdf` | `Copie de QC2022Avis.pdf` |
| `QC2022Concentrix.pdf` | `Copie de QC2022Concentrix.pdf` |
| `QC2022CRA.pdf` | `Copie de QC2022CRA.pdf` |
| `QC2022Tangerine.pdf` | `Copie de QC2022Tangerine.pdf` |
| `QC2023Actuel.pdf` | `Copie de QC2023Actuel.pdf` |
| `QC2023Concentrix.pdf` | `Copie de QC2023Concentrix.pdf` |
| `QC2023T4E.pdf` | `Copie de QC2023T4E.pdf` |
| `QC2023Tangerine.pdf` | `Copie de QC2023Tangerine.pdf` |

**Tier 2 total: 11 files freed. Small bytes, high clutter cost.**

---

## Tier 3 — Document duplicates (review before deleting)

| Situation | Recommendation |
|-----------|----------------|
| `BALLAD.gdoc` (root) + `Copie de BALLAD.gdoc` (root) | Keep the non-"Copie de" version unless you edited the copy |
| `1️⃣ MEDFAR (EMR   clinic-facing vendor).gdoc` + `Copie de...` | Same — keep original |
| `THE SIXTH SIGNAL.gdoc` (root) + `THE SIXTH SIGNAL.gdoc` (BOOKS/BUFFY BOOK) | Both are `.gdoc` stubs pointing to the same Google Doc; the one in `BOOKS` is likely in the right folder — delete the root copy |
| `Reboot Performance, Gender, and the Computing of IdentityMT.gdoc` in `Soumis/` + `Soumis/REJECTED/` | Keep the `REJECTED/` copy (it's in its correct outcome folder); delete the parent `Soumis/` copy |
| `introduction.docx` in `COMPRESS/` and `Compress without Opacity/` | Compare — same size means identical content. Delete one folder's copy. |
| `Document sans titre.gdoc` × 3 (root, Impôts, BUFFY) | Empty Google Doc stubs. Safe to delete all 3 if blank. |
| `index (1).html` on G: and F:\ | Browser-save artifact. Both are the same 21 KB. Delete both or keep one locally. |
| `martin_lepage_governance_tree.html` on G: and F: | Same file, 12 KB. Keep the G: root copy; delete the F: copy if F: is just a mirror. |
| `MIRO-From AI Anxiety to Recursive Govern.txt` on G: and F: | Same. Keep G: root; delete F: copy if F: is just a mirror. |
| `openai.yaml` in `fully-rounded-power-analyst/agents/` and `red-team/agents/` | Same content, 257 bytes. These are skill config files — intentional or accidental? Check if both skills actually need their own copy or if it's a leftover. |

**Tier 3 total: ~12–15 files, mostly negligible bytes.**

---

## Tier 4 — Media review (biggest storage decision — 30.45 GB)

The entire `KK` folder is 30.45 GB. This is the only decision that meaningfully reclaims Drive quota.

### What's in KK
- `Kath And Kim` — 4 seasons + extras + movie (AVI, ~700 MB/episode)
- `30 Rock` — 7 seasons
- `Futurama` — 7 seasons
- `Home Movies` — 4 seasons
- `Ocean's Eight (2018)` — 1080p WEBRip

### Decision options
1. **Delete all of KK** — reclaims ~30 GB immediately. Only do this if you have another copy (local NAS, external drive) or don't need these.
2. **Delete specific series** — if you've already watched and won't re-watch, pick the series. Kath And Kim alone is the largest chunk by episode count.
3. **Keep KK, move to cold storage** — if you want them off Drive quota but not deleted, move to a local drive or use Drive's "offline only" mode.

**Tier 4 note**: Do not delete KK without deciding where your archive lives. This is the only irreversible action on this list.

---

## Summary

| Tier | Files | Risk | Storage freed |
|------|-------|------|---------------|
| 1 — System artifacts | ~200 | Zero | ~negligible |
| 2 — Tax PDF copies | 11 | Zero | ~negligible |
| 3 — Doc duplicates | ~15 | Low (review once) | ~negligible |
| 4 — KK media | 273 | Medium (irreversible) | **~30 GB** |

The only path to meaningful Drive quota recovery is Tier 4. Tiers 1–3 are hygiene.

---

## What this does NOT address

- **936 local files missing from Drive** — see `topic_missing_on_drive.csv`. Separate task.
- **31 paper clusters with incomplete companion artifacts** — see `official_paper_gaps.csv`. Separate task.
- **Unnatural Selection** scattered between root and `Shared with ChatGPT/Papers/` — Google Doc stub, not a real duplicate risk.

## Related

- [[Writing and Novels MOC]]
- [[D-drive-dedup-report-2026-04-21]]
