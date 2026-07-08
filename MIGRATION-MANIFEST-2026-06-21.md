---
type: note
title: Migration MANIFEST
tags:
- note
status: active
created: '2026-06-21'
updated: '2026-07-08'
vault_area: MIGRATION-MANIFEST-2026-06-21.md
canonical_path: MIGRATION-MANIFEST-2026-06-21.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

# Migration MANIFEST
# Generated: 2026-06-21T09:09:48Z
# Operator: clean-migrate (loop — /tmux-ai-council assess + /clean-migrate)
# Source root: /home/martin
# Skills: tmux-ai-council (assessment), clean-migrate (execution)
# Strategy: mv (same filesystem — atomic inode rename, no copy needed)

## Status: COMPLETE (2 passes + pharos-suite dedup) — sources removed by mv (atomic)

---

## Classification basis

PHAROS-SUITE (excluded from migration):
- pharos-ai.ca, COMPASSai, AurorA, and all products on their webpage
- Directories: apps/web-apps/PHAROS-SUITE, apps/web-apps/pharos-suite,
  repos/hephaistos, repos/helix, pharos-suite/ (root), products/pharos-governance-tools

---

## Mobile Apps → apps/mobile-apps/

| source | destination | type | git | status |
|--------|-------------|------|-----|--------|
| `repos/fantasycast-gay` | `apps/mobile-apps/fantasycast-gay` | Expo React Native | yes | ok |

Pre-existing mobile apps (untouched): GAIAapp, clearday-mobile, lotus-mobile

---

## Web Apps → apps/web-apps/

| source | destination | type | git | status |
|--------|-------------|------|-----|--------|
| ~~`repos/helix`~~ | ~~`apps/web-apps/helix`~~ | PHAROS product — moved back to repos/helix | yes | REVERTED |
| `repos/nexusos` | `apps/web-apps/nexusos` | base44 SPA | yes | ok |
| `repos/ECHOapp` | `apps/web-apps/ECHOapp` | Full-stack (frontend+backend) | yes | ok |
| `repos/DG` | `apps/web-apps/DG` | Full-stack (frontend+backend) | yes | ok |

Pre-existing web apps (untouched, PHAROS): PHAROS-SUITE, pharos-suite
Pre-existing web apps (untouched, other): corpus-5point, extensions

---

## Websites → websites/ (NEW DIRECTORY)

| source | destination | type | git | status |
|--------|-------------|------|-----|--------|
| `repos/glammy-site` | `websites/glammy-site` | Static HTML portfolio | yes | ok |
| `repos/clearday` | `websites/clearday` | Static HTML | yes | ok |
| `repos/percephal` | `websites/percephal` | CF landing page (wrangler) | yes | ok |
| `repos/reflexive-inhabitation-audit` | `websites/reflexive-inhabitation-audit` | React site | yes | ok |
| `repos/martinlepage26-bit.github.io-echo` | `websites/martinlepage26-bit.github.io-echo` | Portfolio echo (empty git) | yes | ok |
| `apps/web-apps/martinlepage26-bit.github.io` | `websites/martinlepage26-bit.github.io` | Astro personal site | no | ok |

---

## Pass 2 — Web Apps → apps/web-apps/

| source | destination | type | git | status |
|--------|-------------|------|-----|--------|
| `repos/Agency` | `apps/web-apps/Agency` | Python/FastAPI + Lotus/Scripto | yes | ok |
| `repos/gaia` | `apps/web-apps/gaia` | Vue frontend + Docker (Terraform UI) | yes | ok |

## Pass 2 — Websites → websites/

| source | destination | type | git | status |
|--------|-------------|------|-----|--------|
| `VoiceBridge/` (root) | `websites/VoiceBridge` | Foundation site (CF Pages + wrangler) | yes | ok |

## Pass 2 — Infra → infra/ (NEW DIRECTORY)

| source | destination | notes | status |
|--------|-------------|-------|--------|
| `repos/Client-Delivery-Environment` | `infra/Client-Delivery-Environment` | Empty scaffold | ok |
| `repos/PEER-REVIEW` | `infra/PEER-REVIEW` | Academic research docs | ok |
| `repos/aether` | `infra/aether` | Empty — deferred | ok |
| `distillation/` (root) | `infra/distillation` | ML training pipeline | ok |
| `micro1/` (root) | `infra/micro1` | Interview prep project | ok |
| `src/` (root) | `infra/src` | IF switchboard runtime + infrafabric VSCode ext | ok |
| `agent-collab/` (root) | `infra/agent-collab` | Agent coordination tooling | ok |

---

## pharos-suite Dedup (authorized 2026-06-21)

Three copies resolved to one canonical.

| directory | size | action | reason |
|-----------|------|--------|--------|
| `apps/web-apps/pharos-suite` | 1.7G | **KEEP** — canonical; live git remote to github.com/martinlepage26-bit/pharos-suite.git |
| `apps/web-apps/PHAROS-SUITE` | 639M | **DELETED** — legacy snapshot; no git, fully subsumed; unique content was empty uploads dir + reproducible venv/cache |
| `pharos-suite/` (root) | 3.2M | **DELETED** — hollow stub; frontend/ was an early version missing src/, build/, package.json |

~643MB freed.

---

## repos/ — Final state (PHAROS only)

| directory | reason |
|-----------|--------|
| `repos/helix` | PHAROS product (Helix 3.1) — incorrectly moved in pass 1, reverted |
| `repos/hephaistos` | PHAROS infrastructure (contains aurorai/, compassai/) |

---

## Not migrated — root-level (out of scope)

| directory | notes |
|-----------|-------|
| CLAUDEX | Claude tooling docs |
| EMERAULD | Personal knowledge vault |
| Lavoie | Client project (Pharos AI consulting) |

---

## Diamond-eyes gate — see section below

---

## Encoding
All moves used mv (same filesystem). No encoding conversion performed.
Binary and text files are untouched at byte level.
