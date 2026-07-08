---
type: product
title: Reflexive Inhabitation Audit — Built App
tags:
- chrome-extension
- blink-scaffold
- ria
- methodology-implementation
- react
- vite
- pharos
- vm-inventory
- product
- areas
status: active
domain: pharos
created: '2026-07-08'
updated: '2026-07-08'
vault_area: Areas
canonical_path: Areas/PHAROS/Reflexive Inhabitation Audit — Built App.md
backlink_count: 3
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Areas/PHAROS/fantasycast-gay — Expo App]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
---

# Reflexive Inhabitation Audit — Built App

> For future Claude: the vault already documents the Reflexive Inhabitation
> Audit (RIA) as a **methodology/prompt** — see
> [[Areas/PHAROS/Reflexive Inhabitation Audit — Prompt]]. This note is
> different: it documents a **working piece of software** at
> `/home/martin/websites/reflexive-inhabitation-audit/` that implements that
> exact methodology as an installable Chrome extension. Before this note,
> the vault had no record that the concept had been built as a tool.

## Summary

`reflexive-inhabitation-audit` is a Vite/React/TypeScript Chrome extension
(Manifest-style, with a `background.ts` service worker) that operationalizes
the five-step RIA prompt as a guided wizard: a user runs an audit against a
"target system," steps through Entry/Mechanism/The Blank/Origin/View
prompts, and the results are saved and browsable in an audit history view.
It persists data through the Blink platform's hosted backend
(`@blinkdotnew/sdk`), the same platform used for other scaffolds found
elsewhere on this VM (see Related).

## Context

Sources read (read-only): `README.md`, `package.json`,
`src/components/AuditWizard.tsx`, `src/components/AuditHistory.tsx`, and
`src/lib/blink-api.ts`. No `.env.local` contents were read beyond confirming
the file exists.

- Git history: two commits, "Initial commit from Blink" / "Initial commit"
  — file mtimes on disk are 2026-06-16, the same day as several other
  Blink-scaffolded projects found on this host.
- `README.md` is generic Vite/React/TypeScript template boilerplate
  (documents a CSS-variable-consistency linting feature) — it does not
  describe the RIA feature at all; the actual product logic lives in the
  component files, not the docs.

## Details

**Stack:** React 19 + Vite 6 + TypeScript, Tailwind + `clsx`/`tailwind-merge`
(shadcn-style utility patterns), Framer Motion for step transitions,
lucide-react icons, `@blinkdotnew/sdk` as the backend client. Build includes
a `prebuild` icon-generation script (`scripts/generate-icons.js` using
`@resvg/resvg-js`) — consistent with packaging this as an installable
browser extension icon set. `@types/chrome` is a dependency, and
`src/background.ts` exists — confirming this targets the Chrome extension
runtime, not a plain web app.

**The wizard (`AuditWizard.tsx`)** implements exactly five steps beyond the
initial target-selection screen, matching the RIA prompt's structure step
for step:
- `init` — Target (the `target_system` under audit)
- Step 1: Entry — captures `presence_condition`, the system's `own_language`
  vs. an `outsider_language`, and a `divergence_finding` between them
- Step 2: Mechanism — `inability`, `observation`, `repeating_mechanism`
- Step 3: The Blank — `withheld_center`
- Step 4: Origin — `installer`, `protection`, `naming_cost`
- Step 5: View — `final_view`

On completion, the form data is POSTed to `db//rest/v1/audits` via the
`blinkAPI` helper, which the extension routes through
`chrome.runtime.sendMessage` to its background script (a `BLINK_API`
message type) rather than calling the Blink API directly from the
content/UI context — the standard MV3 pattern for extensions that need a
persistent, cross-origin-capable message relay.

**`AuditHistory.tsx`** lists saved audits (`GET
db//rest/v1/audits?order=created_at.desc`), supports search, and supports
per-audit delete with a confirm prompt — a complete, working CRUD loop
around the audit data, not just a form.

**`blink-api.ts`** is a small, careful path-normalization wrapper: it strips
accidental absolute URLs, enforces the `module/projectId/...` shape Blink's
API expects, and surfaces `chrome.runtime.lastError` as a rejected promise —
evidence of real debugging/hardening effort, not a copy-pasted stub.

**Reading of significance:** this is a genuine, functioning implementation
of the RIA methodology as a repeatable, self-service audit tool — a step
beyond the prompt/protocol documentation that already exists in the vault.
It turns the RIA from "a prompt Martin runs manually against a target" into
"a tool anyone with the extension installed can run against any target."

## Related

- [[Areas/PHAROS/Reflexive Inhabitation Audit — Prompt]] — the underlying methodology/prompt this extension implements; read that note first for what each step (Entry/Mechanism/The Blank/Origin/View) actually means analytically.
- [[Areas/PHAROS/RIA-CODEX — System Audit Protocol]] — a related protocol note in the same audit family, worth cross-checking for terminology alignment.
- [[Areas/PHAROS/fantasycast-gay — Expo App]] — another same-day (2026-06-16) Blink-scaffolded project on this host, useful for spotting the Blink-template pattern across unrelated apps.
- [[Areas/PHAROS/PHAROS Product Stack]] — canonical PHAROS product-family bridge note; this tool is closer to an internal methodology instrument than a commercial product, but is cross-linked here for discoverability.
