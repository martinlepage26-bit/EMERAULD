---
type: wiki
title: ComplyScan — Bilingual Law 25 - AI Act Compliance SaaS
aliases:
- ComplyScan
- Law 25 compliance SaaS
- bilingual compliance tool
- AI Act self-assessment
- bilingual Law 25
- ComplyScan — Bilingual Law 25 AI Act Compliance SaaS
- ComplyScan — Bilingual Law 25 / AI Act Compliance SaaS
- wiki/ComplyScan — Bilingual Law 25 - AI Act Compliance SaaS
tags:
- product
- saas
- compliance
- law-25
- ai-act
- bilingual
- micro-saas
- market-opportunity
- blink
- wiki
- complyscan-bilingual-law-25-ai-act-compliance-saas-md
- complyscan
- solo
- regulation
- color-purple
status: active
created: '2026-04-23'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/ComplyScan — Bilingual Law 25 - AI Act Compliance SaaS.md
backlink_count: 9
backlinks:
- '[[wiki/AI Governance Public Statement and Market Impact Pack]]'
- '[[wiki/ChatGPT Apps SDK — Planning, Metadata, Deployment, and Operations]]'
- '[[wiki/PHAROS Launch — Fluency, Evidence, and Mid-Funnel Trust (Synthesis)]]'
- '[[wiki/Personal and Projects MOC]]'
- '[[wiki/Regulatory Arbitrage — EU AI Act + Law 25 + 93-Day Window (Synthesis)]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[archive/session-state/session-state-001]]'
- '[[memory/clients/Sante-France]]'
- '[[memory/daily/2026-04-23]]'
---

# ComplyScan — Bilingual Law 25 - AI Act Compliance SaaS

## Summary

ComplyScan is a productized bilingual (EN/FR) compliance self-assessment SaaS concept for Canadian SMBs, surfaced during a [[90-Day $1M Challenge — Status Report|90-day revenue challenge]] market scan as the highest-leverage solo-dev opportunity for [[Martin Lepage — Professional Profile|Martin]]. Core flow: sign up → pick regulation (Law 25, AIDA/Bill C-27, EU AI Act, GDPR, PIPEDA) → answer dynamic questionnaire → receive AI-generated compliance report with risk score, gap list, and prioritized remediation roadmap, exportable as PDF in EN or FR.

## Context

Emerged from a 2026-04-22 Codex market research session identifying five recreatable app opportunities ranked by solo-dev leverage and defensibility. ComplyScan ranked first because it productizes existing [[PHAROS Procurement-Unblock Sprint|consulting IP]] Martin already delivers at consulting rates, adds a bilingual moat no generic competitor can replicate in the Quebec market, and targets an underserved SMB segment adjacent to both [[PHAROS-AI Webservice — pharos-ai.ca|PHAROS's enterprise deployment surface]] and [[COMPASSai — Governance Engine|COMPASSai's]] governance engine work. The raw session capture is at `raw sources/2026-04-22_emerging-market-app-opportunities-blink-compliance-saas.md`.

## Details

### Product Concept

- **Target market:** Quebec and Canadian SMBs needing compliance with Law 25, AIDA/Bill C-27, EU AI Act, GDPR, PIPEDA
- **Core loop:** Sign up (Supabase auth) → pick regulation from dropdown → dynamic questionnaire (15–25 yes/no/short-text questions generated from a JSON rulepack) → AI-generated compliance report (risk score 0–100, gap list with severity, prioritized remediation roadmap, executive summary)
- **Dashboard:** All past assessments, re-assessment reminders, progress chart
- **Export:** PDF in EN or FR
- **Pricing:** $49/mo Starter, $149/mo Pro (unlimited assessments + team seats)
- **Stack:** Next.js App Router + Tailwind + shadcn/ui, Supabase (auth + Postgres), OpenAI GPT-4o-mini, Stripe, react-pdf

### Regulatory Status Note (2026-04-23)

AIDA/Bill C-27 is **not in force** — Parliament was prorogued in January 2025 and the Bill died on the order paper. Canada has no enacted federal AI regulation as of April 2026. A replacement framework is expected from the new government under a "light, tight, right" framing, but no draft is published. ComplyScan should position the federal AI regulation slot as "prepare for Canada's incoming AI regulation" (early-mover positioning) rather than claiming current AIDA compliance. Law 25 (Quebec) and PIPEDA remain the active Canadian regulatory obligations. EU AI Act and GDPR are active for businesses with EU exposure.

### Competitive Moat

The bilingual requirement is structural, not cosmetic: every string translated, language toggle in header, PDF export in either language. Quebec's Law 25 enforcement landscape creates a mandatory compliance event for SMBs with no fluent bilingual tool serving them. Martin's consulting work provides the rulepack content (the actual questionnaire IP) immediately — no research sprint needed to seed the Law 25 rulepack.

### Market Comparables

- **Formula Bot** (~$220k/mo, solo founder): AI wrapper over a painful, repetitive professional task at $19–99/mo willingness-to-pay — the exact pattern
- **ShipFast** (~$133k/mo, solo founder): SaaS boilerplate for professionals; similar solo-dev origin
- Pattern: horizontal tools exist everywhere; vertical, niche-specific tools win on retention

### Blink.new Scaffold

A paste-ready Blink scaffold prompt for the full stack is in the raw source capture. Paste into blink.new, press Create — the rulepacks and bilingual polish are where no competitor can follow.

### Relationship to PHAROS

ComplyScan is a standalone product, not a [[PHAROS Method — Technical Reference|PHAROS]] internal tool. The connection points:

- The Law 25 / AI Act regulation rulepacks (JSON question sets) are direct outputs of consulting IP developed through PHAROS governance method work
- The bilingual EN/FR hard rule mirrors [[PHAROS-AI Webservice — pharos-ai.ca|pharos-ai.ca]]'s non-negotiable requirement
- Revenue from ComplyScan could fund the [[90-Day $1M Challenge — Status Report|90-day $1M challenge]] sprint alongside the enterprise consulting track

## Related

- [[90-Day $1M Challenge — Status Report]] — Revenue challenge this concept addresses
- [[PHAROS Procurement-Unblock Sprint]] — Parallel enterprise revenue path; both serve the same sprint
- [[PHAROS-AI Webservice — pharos-ai.ca]] — Stack overlap and bilingual requirement mirror
- [[COMPASSai — Governance Engine]] — Adjacent governance assessment engine; different scope and market
- [[Martin Lepage — Professional Profile]] — Consulting IP is the core moat
- [[PHAROS Legal Classification — CAE Code Strategy]] — Regulatory context for Quebec-facing products
