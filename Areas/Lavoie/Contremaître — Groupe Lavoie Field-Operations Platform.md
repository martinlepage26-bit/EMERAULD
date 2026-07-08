---
type: wiki
title: Contremaître — Groupe Lavoie Field-Operations Platform
aliases:
- Contremaître
- Contremaitre
- PHAROS FieldOps
- lavoie-fieldops
tags:
- lavoie
- pharos
- client
- product
- contremaitre
- fieldops
- cloudflare
- fastapi
status: active
created: '2026-07-06'
updated: '2026-07-06'
vault_area: Areas
canonical_path: Areas/Lavoie/Contremaître — Groupe Lavoie Field-Operations Platform.md
---

# Contremaître — Groupe Lavoie Field-Operations Platform

> For future Claude: Contremaître (formerly PHAROS FieldOps) is the field-operations software Martin is building for [[Areas/Lavoie/AREA|Groupe Lavoie]]. Repo lives at `/home/martin/Lavoie/lavoie-fieldops/` (moved from `~/pharos-fieldops`). Load this note for any Contremaître/Lavoie-software question: architecture, deployment, module map, CLI/MCP package, or the LegiPro compliance extension. State current as of 2026-07-06.

## Summary

Contremaître is a FastAPI + React PWA field-operations platform delivered under the [[Areas/Lavoie/AREA|Groupe Lavoie]] PHAROS contract. It covers a 16-module delivery map (Carte des modules), ships with a REST-backed Typer CLI and a FastMCP server facade, and is deployed behind a Cloudflare Worker with mtl-03 as interim backend host. A separate compliance/evidence service, [[LegiPro Canada-QC — Compliance Evidence Service Plan|LegiPro Canada/QC]], is planned (docs-only) as a future integrated phase.

## Context

Built for Israël Lavoie's four divisions (SOS Plomberie, Excavations Lavoie, GVI, Clôtures Israel Concept) under the PHAROS contract at `~/Lavoie/Contrat-Pharos-AI-x-Groupe-Lavoie-PROJET.docx`. Cross-division visibility is the "Tableau de Bord Israël". Delivery framing: each tracker lane is a real task to be done for Israël. Connects to [[Master Project Tracker — 2026]] client lane and the [[Personal and Projects MOC]].

> [!warning] Contradiction detected
> Flagged by the 2026-07-06 nightly pass: this note documents **active production delivery** for Groupe Lavoie — deployed Cloudflare Worker, proven prod migrations, real client login `info@israelconcept.ca` — while the standing engagement framing in older notes says the opposite: [[CLIENT ACCOUNTS]] (row synced 2026-07-05) has the engagement "gated on client prerequisites A1–A5" with next step "Collect A1–A5", and the [[Areas/Lavoie/AREA|Area — Lavoie]] header (created 2026-06-29) opens with "On ice pending gates A1–A5", all five gates still `pending`. Both claims cannot describe the same engagement state. Likely resolution: A1–A5 gate the **SEO/marketing** workstream (URL, GSC, GBP, LocalGo, zones) while the software workstream (Contremaître/LegiPro) proceeds under the PHAROS contract independently — but no note currently states that split, and the "on ice" wording covers the whole client. Older notes left untouched; operator to confirm the two-workstream reading and reword the area header and CLIENT ACCOUNTS row accordingly.

## Details

### Naming (decision, 2026-07)

Product renamed **Contremaître** (Martin's choice) across all code and infra. First round of French-poetic suggestions (Aplomb/Vigie/Socle) was rejected as too clever; trades-register names won. The auth page (`Login.jsx`) had its own hardcoded `<h1>` outside `Layout.jsx` and was fixed separately to "Contremaître" / "Groupe Lavoie".

### Stack and deployment

- Backend: FastAPI + SQLAlchemy 2.0 + Pydantic v2; SQLite interim → PostgreSQL target (QC cutover pending)
- Frontend: React + Vite PWA
- Edge: Cloudflare Worker serving SPA + `/api/*` proxy; named cloudflared tunnel to mtl-03 (interim backend host)
- GitHub: `martinlepage26-bit/Lavoie`
- Alembic migrations with custom `GUID`/`UTCDateTime` TypeDecorators, `render_as_batch` for SQLite; baseline `9cd2e6958d8b`, api_tokens `07f8f434bba7`. Migration path proven on LIVE prod (backup → stop → upgrade → start, data intact).
- API tokens: `ctm_` prefix, sha256-hashed, org-scoped, revocable, accepted alongside JWT via `Authorization: Bearer`
- Encrypted GFS-rotation backups (openssl AES-256, online SQLite snapshot via `sqlite3.backup`); `runtime/backup.key` offsite copy still pending Martin's destination choice
- CLI: Typer package `cli/` with entry points `contremaitre`/`ctm`; global options precede the command (`ctm -o json version`), `CONTREMAITRE_OUTPUT` env fallback
- MCP: FastMCP server in `mcp/`, read-only by default, writes gated by `CONTREMAITRE_MCP_ALLOW_WRITES=true`
- Docs: Structurizr C4 DSL, ADRs, OpenAPI freshness test; 49 tests total (backend 42 / CLI 4 / MCP 3)

### Canonical URL rule (standing, for Danny/Codex and all agents)

The canonical API base is the **public Worker URL** — never localhost, 127.0.0.1, mtl-03, or the private tunnel origin. Encoded in `docs/api/conventions.md` ("Base publique (canonique)") and `docs/guides/llm-guide.md`. Cloudflare WAF error 1010 blocks the default python/urllib User-Agent — clients must set a real UA (encoded in CLI/MCP + docs).

### Module map

16 delivery modules (Carte des modules) grouped by palier: Fondation / Opérations / Intelligence / Spécifiques. Highlights: BarrioPro (M5 materials/pricing/fence estimating — two Rs), M4 auto-punch, Division model + cross-division "Tableau de Bord Israël", CustomerDetail + QuoteDetail pages. M-ORCH/M-AUDIT noted in `backend/app/api/modules.py`.

### Accounts and data (decisions)

- Two orgs collapsed to a single clean "Groupe Lavoie" org; placeholder accounts and demo data removed; ml@ and ds@ kept as testers; `BOOTSTRAP_ADMIN_*` blanked so the bootstrap org won't recreate.
- **Real client login/org email is `info@israelconcept.ca`** — NOT israel@groupelavoie.ca (Martin corrected this twice; fixed in prod DB + seed).
- ds@ password restored byte-for-byte from backup DB after rebuild (plaintext never seen); its live-login 401 is expected.

### Bugs fixed (notable)

- SPA deep-link routing: wrangler `run_worker_first: true` + `not_found_handling: single-page-application`
- UTC datetime serialization via `UTCDateTime` TypeDecorator
- Security review clean: no `dangerouslySetInnerHTML`/`innerHTML`/`eval` sinks, so stored-XSS customer payloads render inert
- Alembic autogenerate omitted `import app.core.database` (needed for GUID/UTCDateTime) — added manually
- `ApiTokenCreated.model_validate(token)` failed → `ApiTokenCreated(**ApiTokenOut.model_validate(token).model_dump(), token=plaintext)`

### Standing product direction — quiet compliance workbench (2026-07-06)

Full rule at [[Quiet Compliance Workbench — Standing Tone Rule]]. Per Martin (via rook-509): all LegiPro/Contremaître UI/API/docs language must be **calm and operational, not panic/disclaimer theatre** — "a zen place to work, not a courtroom simulator". Calm states: Sources trouvées, Points à confirmer, Dossier prêt pour revue, Source officielle, Ajouter une note de revue, Exporter le dossier. Avoid repeated warning banners and scary terms (illegal / non-compliant / no legal advice / liability) on everyday surfaces; formal caveats stay short and neutral, mostly on exports/guides/admin. Source rigor, source cards, evidence traceability, rights boundaries, and the review workflow are unchanged — UX softening does not weaken correctness. Applied 2026-07-06: lavoie-fieldops commit `bd643fe` (pushed) + parent-repo plan §16 commit `7c30917` (local, no remote). Details in [[LegiPro Canada-QC — Compliance Evidence Service Plan]].

### Pending / deferred (do not auto-start)

- QC cutover to PostgreSQL — blocked on QC stack availability; gates LegiPro implementation
- Copy `runtime/backup.key` offsite — needs Martin's destination
- Frontend custom domain `contremaitre.pharos-ai.ca` — needs Worker moved to the ml@pharos-ai.ca Cloudflare account
- Optional proxy-header cleanup

Living handoff: `docs/handoff/contremaitre-full-package-handoff-2026-07-05.md` in the repo.

## Related

- [[Areas/Lavoie/AREA|Area — Lavoie]]
- [[LegiPro Canada-QC — Compliance Evidence Service Plan]]
- [[Master Project Tracker — 2026]]
- [[CLIENT ACCOUNTS]]
- [[Personal and Projects MOC]]
