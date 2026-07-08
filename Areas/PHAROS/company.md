---
type: note
title: PHAROS — Operational Context
aliases:
- Areas/PHAROS/company
tags:
- note
- areas
- pharos
- apps
- aurora
- cloudflare
- suite
- martinlepage
- color-orange
status: active
created: '2026-06-26'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/company.md
backlink_count: 1
backlinks:
- '[[memory/agents/Vibe]]'
---

# PHAROS — Operational Context

## Identity
- Full name: PHAROS (pharos-ai.ca)
- Type: AI governance consultancy + software development operation
- Location: Montréal, Québec
- Structure: Solo practitioner (Martin Lepage, PhD)
- Positioning: Constraint-first AI governance architecture — operational controls, evidence trails, auditability (not compliance theater)

## Products in Active Development
1. **AurorA** — governance-gated document intake + evidence extraction
   - Stack: Cloudflare Workers/D1/R2/TypeScript + FastAPI+MongoDB (Python backend)
   - Path: `apps/web-apps/pharos-suite/aurorai/`
   - Deployed worker: `aurora-pharos` (last CI deploy 2026-05-20)
   - Next: Module 03 full build (file intake validators)
2. **COMPASSai** — multi-step governance engine for high-stakes workflows
   - Stack: same as AurorA
   - Path: `apps/web-apps/pharos-suite/compassai/`
   - Receives AurorA handoff via `shared/types/handoff-contract.ts`

## Extended Product Line
| Product | Surface | Path |
|---------|---------|------|
| HELIX | pharos-ai.ca | `apps/web-apps/pharos-suite/helix/` |
| ECHO | martin surface | `apps/web-apps/ECHOapp/` |
| LOTUS | martin surface | `apps/mobile-apps/lotus-mobile/` |
| SCRIPTO / DR. SORT | martin surface | `apps/web-apps/Agency/scripto` |
| GAIA | martin surface | `apps/web-apps/gaia/`, `apps/mobile-apps/GAIAapp/` |

## Stack
- Cloudflare Workers (compute)
- Cloudflare D1 (SQLite serverless DB)
- Cloudflare R2 (object storage)
- Cloudflare Pages (static hosting)
- TypeScript (Workers + frontend)
- FastAPI + MongoDB (AurorA + COMPASSai Python backends)
- React (pharos-suite frontend)
- GitHub org: MartinLepage26-BIT
- Repos: pharos-suite, martinlepage26-bit.github.io
- Wrangler (Cloudflare Workers deployment tool)
- pnpm (frontend build)

## Brand
- Primary: deep teal #0a3d4f
- Accent: champagne gold #b8962e
- Public URL: pharos-ai.ca

## Public Topology
| Surface | URL | Repo |
|---------|-----|------|
| PHAROS public | pharos-ai.ca | `apps/web-apps/pharos-suite/` |
| Martin personal | martin.govern-ai.ca | `martin-lepage-site` |
| GitHub Pages | martinlepage26-bit.github.io | separate repo |
- AurorA, COMPASSai, HELIX → PHAROS surface only
- LOTUS, SCRIPTO, GAIA, ECHO, DR. SORT → Martin surface only
- PHAROS, COMPASSai, and AurorA stay off the Martin surface

## Email Routing
- ml@pharos-ai.ca → professional / client-facing
- martinlepage.ai@gmail.com → personal Claude account ONLY
- martin.govern-ai.ca → personal/educational ONLY, never client-facing

## Active Clients
| Client | Status | Work location |
|--------|--------|---------------|
| Groupe Lavoie (SOS Plomberie / Excavations Lavoie / GVI / Clôtures Israel Concept) | On ice — awaiting gates A1–A5 from Israël + Guillaume Lavoie via Patricia | `~/Lavoie/` |

## Governance Frameworks (proprietary)
- RDAIG (Recursive Deterministic AI Governance)
- DAST (Discursive Authority Stress Test)
- Sealed Card Protocol
- RECURSO / RECURSOTRUE (14-layer framework)
- Self-Polygraph Protocol
- HELIX stress-test protocol
- L99 evidence-completeness standard
- PHAROS Governance Loop

## Internal Governance Architecture — Three-Agent Stack
| Agent | Authority |
|-------|-----------|
| Hephaistos | Tier 0 forging — scope, artifact definition, skill composition |
| Queen Keyport | Governance — constraints, approvals, refusals (co-equal with Hephaistos) |
| Hermes | Routing + integration — routes after both Hephaistos + QK clear |
| Argus | Independent meta-governance auditor (reports to Operator) |
| HENRY | Independent specialist — research writing (reports to Operator) |
| Gadget | Independent specialist — frontier scouting, integrations (reports to Operator) |

All authority ultimately reports to the Operator (Martin Lepage).
56+ skills registered across the ecosystem (`.agents/hephaistos/`, `.codex/skills/`, `.claude/`).

## AI CLI Council (operator-facing, not subordinate to three-agent stack)
Claude · Codex · Grok · Gemini · Kimi · Antigravity · Vibe (Mistral)

## Personal Knowledge
- **EMERAULD** — personal knowledge vault, Obsidian-based. 511+ wiki notes. `~/EMERAULD/`
- Session start: rook harness (`if_rook_session_start.sh`) writes capabilities + postits arrival files before any substantive work

## Research & Academic Identity
- PhD, Religious Sciences
- Thesis: "WHY BE KING" — queer embodiment, ritual, neo-Pagan spirituality
- MA: Université Laval 2010, on Yvon Rivard
- Published: Religiologiques; submissions to AI & Society, Social Compass, Magic Ritual and Witchcraft
- Fields: queer theory, ritual studies, STS, digital culture, neo-paganism, ancient Greek civilization, glitch aesthetics

## Language
- Bilingual: Québécois French + English
- Respond in language Martin uses; default English
