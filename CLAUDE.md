# Memory

## Me
Martin Lepage (PhD, Religious Sciences), founder of PHAROS (pharos-ai.ca), Montréal-based.
Solo practitioner: AI governance consultancy + software development.
Professional identity: ml@pharos-ai.ca
Personal Claude account: martinlepage.ai@gmail.com (never surfaced professionally)

## Projects
| Codename | What |
|----------|------|
| **AurorA** | Governance-gated document intake and evidence extraction product. Cloudflare Workers/D1/R2/TypeScript stack + FastAPI+MongoDB Python backend. Modules 00–10 skeleton live; next: Module 03 full build. |
| **COMPASSai** | Multi-step governance engine for high-stakes workflows. Same stack. Handoff from AurorA via `shared/types/handoff-contract.ts`. |
| **ECHO** | Product (echoapp). Under `apps/web-apps/ECHOapp/`. |
| **LOTUS** | Product. On Martin surface (martin.govern-ai.ca), not PHAROS surface. |
| **SCRIPTO / DR. SORT** | Product under Agency. On Martin surface only. |
| **GAIA** | Product under `apps/web-apps/gaia/` and `apps/mobile-apps/GAIAapp/`. |
| **HELIX** | Recursive governance stress-test protocol for auditing LLMs (Theseus → Auryn → Hopf phases). Product under `websites/pharos-suite/helix/`. |
| **HEXA / Hexadecimal Mystic** | Glitch-aesthetic art project. Substack + X/Twitter. |
| **The Broken Frequency of the Word** | Novel in progress. |
| **Why Be King?** | PhD thesis → book adaptation. Queer embodiment, ritual, neo-Pagan spirituality. |
| **RDAIG** | Recursive Deterministic AI Governance manuscript. |
| **DAST** | Discursive Authority Stress Test. |
| **RECURSO / RECURSOTRUE** | 14-layer governance framework. |
| **VIGIL/GSK** | Clinical trial proposal (governance/research). |
| **Self-Polygraph Protocol** | AI evaluation experiment → academic paper. |
| **martin.govern-ai.ca** | Personal/educational site only. Never client-facing. Hosted via `martin-lepage-site` repo. |
| **pharos-ai.ca** | Canonical public business URL. Hosted via `pharos-suite` → Cloudflare Pages. |
| **PHAROS-NEWLOOK** | Current live skin for pharos-ai.ca. Absorbed into `websites/pharos-suite/PHAROS-NEWLOOK/` as reference; being consolidated into `frontend/`. |
| **Lavoie / Groupe Lavoie** | Active client (on ice pending gates A1–A5). SOS Plomberie / Excavations Lavoie / GVI / Clôtures Israel Concept. Work at `~/Lavoie/`. |

## Terms
| Term | Meaning |
|------|---------|
| PHAROS | pharos-ai.ca — governance consultancy + dev operation |
| AurorA | Document intake/evidence extraction product |
| COMPASSai | Multi-step governance engine product |
| RDAIG | Recursive Deterministic AI Governance |
| DAST | Discursive Authority Stress Test |
| RECURSO | 14-layer governance framework |
| HELIX | LLM stress-test protocol (Theseus/Auryn/Hopf phases) |
| SPP | Self-Polygraph Protocol |
| D1 | Cloudflare D1 (SQLite-based serverless DB) |
| R2 | Cloudflare R2 (object storage) |
| BIT | MartinLepage26-BIT (GitHub org) |
| MLePage26 | Cloudflare account handle |
| pharos-suite | Main PHAROS repo at `websites/pharos-suite/` (moved from `apps/web-apps/` — old path is dead) |
| L99 | Evidence-completeness standard (PHAROS internal) |
| RDG | Recursive Deterministic Governance |
| diamond-eyes | Aesthetic refinement skill in PHAROS skill ecosystem |
| killcritic-x10think | Critique skill in PHAROS skill ecosystem (not currently installed on this host — do not invoke) |
| philosopher | Meta-router skill in PHAROS ecosystem |
| boil-the-ocean | Skill: execute end-to-end without stopping for confirmation |
| HEXA | Hexadecimal Mystic glitch-art project |
| TIHP: | Action trigger → transform into styled HEXA post |
| déshabille le texte | Action trigger → convert to TTS-safe prose |
| EMERAULD | Personal knowledge vault — Obsidian-based, 511+ wiki notes. At `~/EMERAULD/`. |
| PHAROS-NEWLOOK | Current live skin for pharos-ai.ca. At `websites/pharos-suite/PHAROS-NEWLOOK/`. |
| rook | Session start harness — `if_rook_session_start.sh`. Writes capabilities + postits arrival files to disk. |
| Hephaistos | Tier 0 forging agent in three-agent architecture. Scope: artifact definition, skill composition, build strategy. |
| Queen Keyport | Governance agent in three-agent architecture (co-equal with Hephaistos). Scope: constraints, approvals, refusal conditions. |
| Hermes | Routing/integration agent in three-agent architecture. Routes after Hephaistos + Queen Keyport clear. |
| Argus | Independent meta-governance auditor. Peer of HENRY and Gadget. Reports to Operator. |
| tmux-council-loop | Named bounded AI council loop skill. Wraps `tmux-ai-council`. Currently in `.codex/skills.disabled/` — the installed council skills are `tmux-ai-council` + `tmux-council-update`. |
| Groupe Lavoie | Active PHAROS client — SOS Plomberie, Excavations Lavoie, GVI (property mgmt), Clôtures Israel Concept. |
| A1–A5 | Lavoie client gate prerequisites (URL, GSC access, GBP access, LocalGo matrix, zones list). |
| aurora-pharos | Deployed Cloudflare Worker name for AurorA. URL: https://aurora-pharos.martinlepage26.workers.dev (personal Cloudflare account). Last confirmed deploy: 2026-06-22. No root handler — 404 on GET / is expected behavior. |

## People
| Who | Role |
|-----|------|
| Martin | That's you. |
| Patricia | Martin's sister. Internal relay at Groupe Lavoie. Collects A1–A5 responses from Israël + Guillaume and relays to Martin. Does not initiate outreach. |
| Israël Lavoie | Groupe Lavoie — grand patron, visionnaire, autodidacte. |
| Guillaume Lavoie | Groupe Lavoie — co-owner, signs gate A5 (zones/services list). |
| Jade | Base44 developer. Handoff at `Lavoie/jade-base44-handoff.md` (3 apps, specs, acceptance criteria). |

## Stack
- Cloudflare Workers / D1 / R2 / Pages
- TypeScript (Workers, frontend)
- FastAPI + MongoDB (AurorA + COMPASSai Python backends)
- React (pharos-suite frontend)
- GitHub: MartinLepage26-BIT / pharos-suite + martinlepage26-bit.github.io
- Wrangler (Cloudflare Workers deployment)
- pnpm (pharos-suite frontend), npm (Lavoie scaffold)
- Obsidian (EMERAULD vault)
- tmux (AI CLI council sessions)

## AI CLI Council (all report to Operator)
| Agent | Role |
|-------|------|
| Claude | General execution, skills, subagents |
| Codex | Code execution, architecture, file ops |
| Grok | Adversarial review, contradiction detection |
| Gemini | Parallel synthesis and alternate review |
| Kimi | Additional code/reasoning seat |
| Antigravity | Workspace pair-programming, repo orientation |
| Vibe (Mistral) | Mistral council seat |

## Directory Structure (verified on disk 2026-07-05)
```
.agents/hephaistos/   governance framework (AGENTS.md, BOARD.md, agent docs, skills)
.claude/              Claude config, agents, skills, memory
.codex/               Codex config, skills
apps/
  mobile-apps/        GAIAapp, clearday-mobile, fantasycast-gay, lotus-mobile, montreal-plus
  web-apps/           Agency, DG, ECHOapp, gaia, nexusos, corpus-5point, extensions
websites/
  pharos-suite/       ALL PHAROS products: aurorai, compassai, helix, frontend, backend, PHAROS-NEWLOOK
  (also)              VoiceBridge, clearday, glammy-site, percephal, martinlepage26-bit.github.io
infra/                distillation, micro1, src, agent-collab
EMERAULD/             personal knowledge vault
Lavoie/               client project
CLAUDEX/              Claude tooling docs
```
NOTE: pharos-suite lives under `websites/`, NOT `apps/web-apps/`. Any doc or agent still pointing at `apps/web-apps/pharos-suite/` is stale.

## Brand
- Deep teal: #0a3d4f
- Champagne gold: #b8962e
- Canonical URL: pharos-ai.ca

## Writing Rules (standing)
- Never begin sentences with "And"
- Never use em dashes
- No fabricated citations, no Wikipedia in academic papers
- Conclusions analytical, not lyrical
- Full original length preserved in revisions

## Operator Set v1 (apply in order on revisions)
CLAIM-EARLY → SCOPE-CLAMP → CLAIM-LADDER → CONSEQUENCE-ANCHOR → VERB-UPGRADE → ANTI-CHAIN-CLAUSE → PRONOUN-AUDIT → NOUN-DISCIPLINE → CONTROLLED-HEAT → METAPHOR-GROUNDING → CITATION-HYGIENE → QUOTE-CONTAINMENT → DUPLICATE-SOURCE-MERGE

<!-- infrafabric-agent-runtime:managed:start -->
## InfraFabric Hosted Task Discipline

- Durable task state uses the official hosted API through `if-cli blackboard api ...` or the managed MCP front door. Do not write local JSONL, ledger files, or ad hoc database rows as authority.
- Before ending task-backed work, run `if-cli blackboard api closeout-report --tenant-id <tenant> --workspace-id <workspace> --project-id <project>` for the active hosted scope.
- Treat `task.closed` as the only completed closeout event. Checkpoints, commits, local notes, and handoff docs are evidence, not completion.
- Use WebSocket and tmux bridges only for live progress or terminal interaction, not as durable write, search, or proof authority.
- On mtl-03, use the shared `/usr/local/bin/hermes` wrapper; do not invoke the root Hermes venv binary directly.
- Never print tokens, auth JSON, bearer values, private keys, or credential file contents in chat or logs.
<!-- infrafabric-agent-runtime:managed:end -->
