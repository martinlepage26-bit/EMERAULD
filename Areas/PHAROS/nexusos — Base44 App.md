---
type: product
title: nexusos — Base44 App
tags:
- base44
- internal-tooling
- strategy-ops
- react
- command-center
- pharos
- vm-inventory
- product
- areas
status: active
domain: pharos
created: '2026-07-08'
updated: '2026-07-08'
vault_area: Areas
canonical_path: Areas/PHAROS/nexusos — Base44 App.md
backlink_count: 4
backlinks:
- '[[Areas/PHAROS/PHAROS Product Stack]]'
- '[[Areas/PHAROS/ai-agent-board — Third-Party Tool Evaluation]]'
- '[[Areas/PHAROS/corpus-5point — FastAPI-Next.js Research Platform]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
---

# nexusos — Base44 App

> For future Claude: this is a Base44 low-code app (a hosted
> app-builder platform, not a from-scratch codebase) living at
> `/home/martin/apps/web-apps/nexusos/`. It reads as an internal strategy /
> operations command center rather than a client-facing product. Verify with
> Martin whether it is actively used before assuming it's live tooling.

## Summary

`nexusos` is a Base44-generated React web app functioning as an internal
strategy and operations "command center": portfolio health, strategic
lanes/objectives, client and project tracking, decisions, an opportunity
pipeline, a knowledge base, dependency tracking (including a GitHub
dependency connector), weekly AI-generated summaries, and AI
recommendations. The active git history (10+ "File changes" commits plus a
"Update base44 packages" commit) shows it has been iterated on, not just
scaffolded and abandoned.

## Context

Sources read (read-only): `README.md`, `package.json`, the `base44/`
config directory (entity schemas + connectors + functions), and the `src/`
tree (pages/components). No `.env.local` or Base44 app id/base URL contents
were inspected beyond confirming the file exists.

- `README.md` is the stock Base44 boilerplate ("Welcome to your Base44
  project... View and Edit your app on Base44.com") — confirms this is a
  hosted low-code build, edited both locally and in the Base44 web builder,
  not an independent codebase.
- `package.json` name is the generic `base44-app`.
- Git log shows repeated "File changes" commits (the typical Base44 →
  GitHub sync commit message) plus one explicit "Update base44 packages"
  commit — evidence of ongoing, not one-off, iteration.

## Details

**Stack:** React + Vite + Tailwind + shadcn/ui component library
(`components.json`, extensive `src/components/ui/*`), TanStack Query for
data fetching, Base44 as backend-as-a-service (`src/api/base44Client.js`).

**Entity model** (`base44/entities/*.jsonc`): `AIRecommendation`, `Client`,
`Decision`, `Dependency`, `KnowledgeItem`, `OpportunityPipeline`, `Project`,
`ReviewLog`, `StrategicLane`, `StrategicObjective`, `User`,
`WeeklySummary` — a schema clearly built around running a consulting /
product portfolio (multiple clients, multiple projects/lanes, decision
logging, opportunity tracking) rather than a single product.

**Pages** (`src/pages/*.jsx`): Command Center (dashboard), Strategy,
Clients, Opportunities, Projects + Project Detail, Decisions, Knowledge,
Dependencies + GitHub Dependencies, Reviews, Weekly Summaries, Resources,
Portfolio Health, Lane Health Dashboard, Templates, plus auth pages
(Login/Register/Forgot-Reset Password).

**Automated backend functions** (`base44/functions/*`):
`generateWeeklySummary`, `githubDependencies` (a GitHub connector is
configured at `base44/connectors/github.jsonc`), `decisionDeadlineReminder`
— indicating scheduled/triggered automation, not just CRUD screens.

**Dashboard composition** (`CommandCenter.jsx`): live clock, and panels for
Portfolio Health, AI Recommendations, Decisions, Active Projects, and Lane
Health, all queried live via TanStack Query against Base44 entities — this
is the app's home screen and best single artifact for understanding its
purpose.

**Reading of purpose:** the entity/page combination (strategic lanes +
objectives + clients + projects + decisions + opportunity pipeline + weekly
AI summaries) strongly suggests this is Martin's own internal PHAROS
business-operations dashboard rather than a product built for an external
client — a "command center" for running the consultancy itself.

## Related

- [[Areas/PHAROS/PHAROS Product Stack]] — canonical PHAROS product-family bridge note; `nexusos` reads as internal tooling supporting that stack rather than a member of it.
- [[Areas/PHAROS/Agent Orchestration — PHAROS Launch as Governed Multi-Agent Execution]] — `nexusos`'s decision/opportunity/lane tracking overlaps conceptually with this note's governed multi-agent execution model; both are attempts to run PHAROS's portfolio in a structured, trackable way.
- [[Areas/PHAROS/corpus-5point — FastAPI-Next.js Research Platform]] — another substantial internal app on the same VM, contrast in scale and stack (Base44 low-code vs. custom FastAPI/Next.js).
- [[Areas/PHAROS/ai-agent-board — Third-Party Tool Evaluation]] — a different kind of "internal ops tooling" (task/agent orchestration) evaluated on the same host; worth comparing as two answers to the same underlying need (managing PHAROS's own multi-project, multi-agent workload).
