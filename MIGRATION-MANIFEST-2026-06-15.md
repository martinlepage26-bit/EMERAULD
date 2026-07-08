# Migration MANIFEST
# Generated: 2026-06-15T00:00:00Z
# Updated: 2026-06-15 (pass 2 — apps reorganization + cleanup)
# Operator: clean-migrate + trace-investigator + diamond-eyes
# Source root: /home/martin
# Skills: trace-investigator, diamond-eyes, clean-migrate

## Status: COMPLETE

---

## Pass 1 — Document routing (copy+verify)

| source | destination | sha256 (first 12) | status |
|--------|-------------|-------------------|--------|
| `.UPLOADS/quebec-plumbing-cto-roadmap-2026-06-13.md` | `Lavoie/` | `8c31cb2b478f` | ok |
| `AI Council/ai-anxiety-5-pass-debate-2026-06-08.md` | `CLAUDEX/` | `569ffb2c951a` | ok |
| `docs/mtl-01-access.md` | `EMERAULD/30_Resources/` | `54aadac9b2fc` | ok |
| `.UPLOADS/AGENT_PROTOCOL_FOR_WORKING_WITH_MARTIN.md` | `.claude/` | `efc013118732` | ok |
| `.UPLOADS/martin_skills.md` | `.agents/skills/` | `27679fc05ad4` | ok |
| `.UPLOADS/martin_skills_all.zip` | `.agents/skills/` | `432e890af944` | ok |
| `gaia-screenshots/` (48 files) | `apps/mobile-apps/GAIAapp/store-assets/` | spot-check ok | ok |
| `governance_mock_dataset.csv` | `micro1/mock-governance-dataset/` | `a0c530c815d0` | overwrite |
| `governance_mock_dataset.jsonl` | `micro1/mock-governance-dataset/` | `9b6e40e5421b` | overwrite |
| `sample_gold_set.jsonl` | `micro1/mock-governance-dataset/` | `74d78abb7433` | overwrite |

Originals removed (authorized): `AI Council/`, `docs/`, `gaia-screenshots/`, `Claude/`, 3 root data files, `logo.png`, `og-image.png`

---

## Pass 2 — App reorganization (mv, same filesystem)

| source | destination | basis |
|--------|-------------|-------|
| `clearday-mobile/` | `apps/mobile-apps/clearday-mobile/` | Expo (React Native) |
| `lotus-mobile/` | `apps/mobile-apps/lotus-mobile/` | Expo (React Native) |
| `workspaces/GAIAapp/` | `apps/mobile-apps/GAIAapp/` | Expo (expo-router/entry) |
| `workspaces/PHAROS-SUITE/` | `apps/web-apps/PHAROS-SUITE/` | Full web platform |
| `pharos-suite/` | `apps/web-apps/pharos-suite/` | Cloudflare Vite app (PHAROS-NEWLOOK) |
| `workspaces/martinlepage26-bit.github.io/` | `apps/web-apps/martinlepage26-bit.github.io/` | Astro personal site |
| `workspaces/corpus-5point/` | `apps/web-apps/corpus-5point/` | Next.js research platform |
| `workspaces/extensions/` | `apps/web-apps/extensions/` | Browser extensions (3) |

---

## Security flag (open — handle manually)

`/home/martin/.UPLOADS/pharos-gce-498803-882c35a3bd6d.json`
GCP service account credential key. Do NOT move to any git-tracked directory.
Suggested destination: `~/.config/gcloud/` or a secrets vault.

---

## Diamond-eyes gate — remaining flags

- `apps/web-apps/pharos-suite/` vs `apps/web-apps/PHAROS-SUITE/` — mixed-case pair; same ecosystem, different layers. The all-caps one is the full platform; lowercase holds the Cloudflare skin and workspace docs. Naming asymmetry is a navigation tax but not a migration error.
- `apps/web-apps/extensions/` — 3 browser extensions sub-grouped correctly. No issues.
- `workspaces/` now holds only `Publications/` and `README.md` — thin container, could be dissolved or renamed.
- `repos/gaia/` — third-party Terraform UI clone (gaia-app/gaia), not Martin's code. Currently in `repos/`, correct.
- `src/if-switchboard-runtime/` — IF.story runtime infrastructure. `src/` is a single-item container.
