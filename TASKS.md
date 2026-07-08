---
type: note
title: Tasks
tags:
- note
status: active
created: '2026-07-08'
updated: '2026-07-08'
vault_area: TASKS.md
canonical_path: TASKS.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

# Tasks

## Active

- [ ] **Verify Lavoie Patricia message** — Confirm MESSAGE_SUIVI_PATRICIA.md v3 was sent. If not: send immediately, no changes. Do not follow up before 7 days after send. (`Lavoie/MESSAGE_SUIVI_PATRICIA.md`)
- [x] **AurorA Module 03 — file intake build** — Entry point: `aurorai/src/modules/intake/validators.ts`. Spec: `docs/specs/com-aur/03-aurora-file-intake-module.md §intake-validation`. (`apps/web-apps/pharos-suite/`)
- [ ] **Wrangler bindings confirmation** — Confirm R2 bucket name and D1 database_id from `docs/d1-r2-endpoint-mapping.md` before activating `aurorai/wrangler.toml` / `compassai/wrangler.toml`. (`apps/web-apps/pharos-suite/`)
- [ ] **PHAROS-NEWLOOK → frontend/ absorption** — Consolidate public routes from PHAROS-NEWLOOK reference app into canonical `frontend/`. (`apps/web-apps/pharos-suite/`)

## Waiting On

- [ ] **Lavoie gates A1–A5** — Waiting on Israël + Guillaume Lavoie response via Patricia:
  - A1: canonical site URL + secondary domains
  - A2: GSC viewer access → ml@pharos-ai.ca
  - A3: GBP manager access → ml@pharos-ai.ca
  - A4: LocalGo asset-control matrix signed by Israël (approved-requirements.md §8)
  - A5: zones/services list signed by Guillaume
- [ ] **Lavoie corpus** (Action 1 — Martin) — Assemble 20–30 field report examples in `Lavoie/corpus-rapports/`. Blocked on client timing but can start independently.
- [ ] **Lavoie process documentation** (Action 2 — Martin) — Record step-by-step report production session (audio/video). Can start independently.

## Someday

- [ ] **Lavoie Base44/Jade apps** (blocked on 0-A/0-B gates):
  - App 2 GVI Tenant Dispatch — no gate dependency, start first
  - App 1 Report Approval UI
  - App 3 Review Funnel Admin
- [ ] **AurorA/COMPASSai schema activation** — Un-comment `aurorai-d1-schema.sql` + `compassai-d1-schema.sql` after Spec 08 sign-off
- [ ] **AurorA/COMPASSai registries** — Populate `EXTRACTION_CONTROLS` and `POLICY_TEMPLATES` (requires Spec 04 and 07 review)
- [ ] **Example handoff case study** — P1 remainder from Phase 7 (three-agent architecture); `.agents/hephaistos/`
- [ ] **RDAIG manuscript** — Recursive Deterministic AI Governance
- [ ] **Self-Polygraph Protocol** — AI evaluation experiment → academic paper
- [ ] **Why Be King?** — PhD thesis → book (queer embodiment, ritual, neo-Pagan spirituality)
- [ ] **The Broken Frequency of the Word** — Novel in progress
- [ ] **VIGIL/GSK** — Clinical trial governance proposal
- [ ] **RECURSO/RECURSOTRUE** — 14-layer governance framework, publication track

## Done

- [x] Home root reorg — moved misfiled utilities, session artifacts, PHAROS logo assets, and the orphan root `package-lock.json` into canonical folders; manifest written (2026-07-01)
- [x] pharos-ai.ca hero wordmark + nav logo deployed (2026-06-17)
- [x] Home directory migration — all repos under canonical paths (2026-06-21)
- [x] BOARD.md authority-chain lint: PASS 176 checks (2026-06-22)
- [x] tmux-ai-council skill: Antigravity + Vibe/Mistral added (2026-06-22)
- [x] tmux-council-loop skill created (2026-06-22)
- [x] AurorA Worker (`aurora-pharos`) — last successful CI deploy (2026-05-20)
- [x] Lavoie Group A scaffold: 4/4 Jest tests passing, npm audit 0 vulnerabilities (2026-06-13)
- [x] Lavoie offre-de-service-revisee-v2.md + jade-base44-handoff.md produced (2026-06-14)
- [x] Three-agent architecture Phases 1–7 complete: 56+ skills, ethical hardening, Argus deployed (2026-04-09)
- [x] AurorA/COMPASSai Modules 00–10 skeleton: 0 TypeScript errors (2026-03-29)
- [x] AurorA/COMPASSai handoff contract: `shared/types/handoff-contract.ts` live (2026-03-29)
- [x] pharos-ai.ca PHAROS-NEWLOOK skin absorbed into repo (2026-05-08)
