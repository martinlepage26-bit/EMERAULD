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
- wiki
- areas
status: active
domain: lavoie
created: '2026-07-06'
updated: '2026-07-12'
vault_area: Areas
canonical_path: Areas/Lavoie/Contremaître — Groupe Lavoie Field-Operations Platform.md
backlink_count: 16
backlinks:
- '[[Areas/Lavoie/AREA]]'
- '[[Areas/Lavoie/Contrat PHAROS x Groupe Lavoie — v5 Signature Track (2026-07-08)]]'
- '[[Areas/Lavoie/Lavoie Artifact Map — Working Directory (2026-07-08)]]'
- '[[Areas/Lavoie/LegiPro Canada-QC — Compliance Evidence Service Plan]]'
- '[[Areas/Lavoie/Offre de service — v5 Pyramid (2026-07-05)]]'
- '[[Areas/Lavoie/Quiet Compliance Workbench — Standing Tone Rule]]'
- '[[Areas/PHAROS/Agent Scaffolds — ~agents vs .claude-agents Distinction]]'
- '[[Areas/PHAROS/CLIENT ACCOUNTS]]'
- '[[Areas/PHAROS/Jade — Name Disambiguation]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[Logs/2026-07-06]]'
- '[[wiki/Master Project Tracker — 2026]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[archive/session-state/session-state-003]]'
- '[[memory/daily/2026-07-06]]'
- '[[memory/daily/2026-07-07]]'
---

# Contremaître — Groupe Lavoie Field-Operations Platform

> For future Claude: Contremaître (formerly PHAROS FieldOps) is the field-operations software Martin is building for [[Areas/Lavoie/AREA|Groupe Lavoie]]. Repo lives at `/home/martin/Lavoie/lavoie-fieldops/` (moved from `~/pharos-fieldops`). Load this note for any Contremaître/Lavoie-software question: architecture, deployment, module map, CLI/MCP package, or the LegiPro compliance extension. State current as of 2026-07-06.

## Summary

Contremaître is a FastAPI + React PWA field-operations platform delivered under the [[Areas/Lavoie/AREA|Groupe Lavoie]] PHAROS contract. It covers a 16-module delivery map (Carte des modules), ships with a REST-backed Typer CLI and a FastMCP server facade, and is deployed behind a Cloudflare Worker with mtl-03 as interim backend host. A separate compliance/evidence service, [[LegiPro Canada-QC — Compliance Evidence Service Plan|LegiPro Canada/QC]], is planned (docs-only) as a future integrated phase.

## Context

Built for Israël Lavoie's four divisions (SOS Plomberie, Excavations Lavoie, GVI, Clôtures Israel Concept) under the PHAROS contract at `~/Lavoie/Contrat-Pharos-AI-x-Groupe-Lavoie-PROJET.docx`. Cross-division visibility is the "Tableau de Bord Israël". Delivery framing: each tracker lane is a real task to be done for Israël. Connects to [[Master Project Tracker — 2026]] client lane and the [[Personal and Projects MOC]].

> [!success] Contradiction resolved (operator decision, 2026-07-08)
> The 2026-07-06 nightly-pass flag is closed. Operator confirmed the two-workstream reading: **A1–A5 gate the SEO/marketing + signature workstream** (URL, GSC, GBP, LocalGo, zones — relayed via Patricia), while the **software delivery workstream (Contremaître/LegiPro) proceeds independently** under the PHAROS engagement — active production delivery here does not contradict the gated track. [[CLIENT ACCOUNTS]] and the [[Areas/Lavoie/AREA|Area — Lavoie]] header were reworded the same day. Contract instrument: [[Areas/Lavoie/Contrat PHAROS x Groupe Lavoie — v5 Signature Track (2026-07-08)|contract v5 signature track]].

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

### ProgressionLIVE parity roadmap (2026-07-08)

A roadmap to replicate ProgressionLIVE functionality inside Contremaître lives at `lavoie-fieldops/docs/product/progressionlive-parity-roadmap.md` (+ handoff, committed `ff38a48`), generated from `~/Lavoie/progressionlive_functions_guidethrough.md`. It is also the source of client dossier 5157 (dossier de parité) — see [[Areas/Lavoie/Dossiers Client Plan-Set — Chaîne de gouvernance éditoriale 5156–5165 (2026-07-08)|dossier chain 5156–5165]].

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

### Phase 1 executor foundation (2026-07-10)

Three documents now stand between the plan and a less capable executor agent, and they should be read as a set:

- [[Areas/Lavoie/Contremaître Integrations — Verified API Capability Map (2026-07-10)|Verified API capability map]] — the six external systems, checked against vendor docs rather than assumed. **VoIP.ms has no inbound-call webhook** (SIP only), which moved the voice agent to Phase 2 and put CDR polling in Phase 1. Also: Nextcloud `oc:fileid` changes on trash-restore; OpenProject's webhook signature is undocumented; EspoCRM dedup is unreliable and the licence is AGPLv3; Acomba import is a paid client-side add-on; ProgressionLIVE has no invoice object.
- [[Areas/Lavoie/Domain API Foundation — Phase 1 Work Orders and Ports (2026-07-10)|Domain API foundation and work orders]] — domain-named `/api/v1` surface (no vendor names in paths), six ports with a mock-plus-contract-test rule, WP-01 → WP-19 in a fixed execution order, and the customer **birth rule** (a customer is created at first commitment, not first contact). Execution awaits Martin's green light; WP-01 first.
- [[Areas/Lavoie/Marketplace de débordement — Job Overflow and Payments Architecture (2026-07-10)|Marketplace de débordement]] — the multi-tenancy plus job-overflow licensing play, Stripe Connect Express with destination charges, commission returning to Israël Concept. Blocked on a real legal gate (FINTRAC MSB / Revenu Québec ESM), not on engineering.

### Pending / deferred (do not auto-start)

- QC cutover to PostgreSQL — blocked on QC stack availability; gates LegiPro implementation
- Copy `runtime/backup.key` offsite — needs Martin's destination
- Frontend custom domain `contremaitre.pharos-ai.ca` — needs Worker moved to the ml@pharos-ai.ca Cloudflare account
- Optional proxy-header cleanup

Living handoff: `docs/handoff/contremaitre-full-package-handoff-2026-07-05.md` in the repo.

## Related

- [[Areas/Lavoie/AREA|Area — Lavoie]]
- [[Areas/Lavoie/Contremaître Integrations — Verified API Capability Map (2026-07-10)]]
- [[Areas/Lavoie/Domain API Foundation — Phase 1 Work Orders and Ports (2026-07-10)]]
- [[Areas/Lavoie/Marketplace de débordement — Job Overflow and Payments Architecture (2026-07-10)]]
- [[LegiPro Canada-QC — Compliance Evidence Service Plan]]
- [[Master Project Tracker — 2026]]
- [[CLIENT ACCOUNTS]]
- [[Personal and Projects MOC]]
