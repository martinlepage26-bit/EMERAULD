---
type: note
title: Glossary — PHAROS / Martin Lepage
tags:
- note
- resources
- apps
- council
- lavoie
- suite
- tmux
status: active
domain: reference
created: '2026-06-26'
updated: '2026-08-05'
vault_area: Resources
canonical_path: Resources/glossary.md
backlink_count: 7
backlinks:
- '[[archive/session-state/session-state-003]]'
- '[[memory/agents/Antigravity]]'
- '[[memory/agents/Gemini]]'
- '[[memory/agents/Grok]]'
- '[[memory/agents/Kimi]]'
- '[[memory/agents/Vibe]]'
- '[[memory/daily/2026-07-02]]'
---

# Glossary — PHAROS / Martin Lepage

## Acronyms & Initialisms
| Term | Expansion |
|------|-----------|
| PHAROS | pharos-ai.ca — AI governance consultancy + software dev (Montréal) |
| RDAIG | Recursive Deterministic AI Governance |
| DAST | Discursive Authority Stress Test |
| RECURSO / RECURSOTRUE | 14-layer recursive governance framework |
| SPP | Self-Polygraph Protocol |
| RDG | Recursive Deterministic Governance |
| HELIX | LLM stress-test protocol: Theseus → Auryn → Hopf phases |
| L99 | Evidence-completeness standard (PHAROS internal) |
| VIGIL/GSK | Clinical trial governance proposal |
| HEXA | Hexadecimal Mystic — glitch-aesthetic art project |
| BIT | MartinLepage26-BIT (GitHub org handle) |
| D1 | Cloudflare D1 (SQLite serverless DB) |
| R2 | Cloudflare R2 (object storage) |
| STS | Science and Technology Studies |
| GSC | Google Search Console |
| GBP | Google Business Profile |

## Product Lexicon (canonical stylizations)
- COMPASSai
- AurorA
- ECHO
- LOTUS
- SCRIPTO
- GAIA
- DR. SORT
- HELIX

## Action Triggers
| Trigger | Action |
|---------|--------|
| `TIHP:` | Transform everything after colon into a complete, styled HEXA post ready for publication |
| `déshabille le texte` | Convert text into TTS-safe prose (remove orphan punctuation, full sentences, no decorative separators) |

## Codenames / Projects
| Name | Description |
|------|-------------|
| AurorA | Governance-gated document intake + evidence extraction. `apps/web-apps/pharos-suite/aurorai/` |
| COMPASSai | Multi-step governance engine for high-stakes workflows. `apps/web-apps/pharos-suite/compassai/` |
| HEXA / Hexadecimal Mystic | Glitch-aesthetic art project (Substack, X/Twitter) |
| Why Be King? | PhD thesis + book adaptation (queer embodiment, ritual, neo-Pagan spirituality) |
| The Broken Frequency of the Word | Novel in progress |
| RDAIG | Manuscript: Recursive Deterministic AI Governance |
| Self-Polygraph Protocol | AI evaluation experiment → academic paper |
| HELIX | Recursive governance stress-test for auditing LLMs. `apps/web-apps/pharos-suite/helix/` |
| Sakura / Sealed Card Protocol | Philosophical experiment |
| pharos-suite | Primary PHAROS repo. `apps/web-apps/pharos-suite/`. Serves pharos-ai.ca via Cloudflare Pages |
| martin.govern-ai.ca | Personal/educational only — never client-facing. Cloudflare Pages deployment (`martin-lepage-site` project, same deploy as `martin-lepage-phd.pharos-ai.ca`), sourced from repo `martinlepage26-bit.github.io` — not a separate `martin-lepage-site` repo. `govern-ai.ca` is a shared zone (also hosts patent-workbench, clearday, axis, fantasycast). Corrected 2026-08-05, see [[CLAUDE]] |
| pharos-ai.ca | Canonical business URL |
| PHAROS-NEWLOOK | Current live skin for pharos-ai.ca. At `apps/web-apps/pharos-suite/PHAROS-NEWLOOK/`. Being consolidated into `frontend/` |
| EMERAULD | Personal knowledge vault — Obsidian-based, 511+ wiki notes. At `~/EMERAULD/` |
| Lavoie / Groupe Lavoie | Active PHAROS client (on ice, awaiting A1–A5). SOS Plomberie, Excavations Lavoie, GVI, Clôtures Israel Concept. Work at `~/Lavoie/` |
| aurora-pharos | Deployed Cloudflare Worker name for AurorA. Last successful CI deploy: 2026-05-20 |

## Three-Agent Architecture
| Agent | Role |
|-------|------|
| Hephaistos | Tier 0 forging — artifact definition, scope, skill composition, build strategy. Entry: `.agents/hephaistos/HEPHAISTOS.md` |
| Queen Keyport | Governance — constraints, approvals, refusal conditions. Co-equal with Hephaistos. Entry: `.agents/hephaistos/QUEEN-KEYPORT.md` |
| Hermes | Routing + integration — routes after Hephaistos + Queen Keyport clear. Entry: `.agents/hephaistos/HERMES.md` |
| Argus | Independent meta-governance auditor. Peer of HENRY + Gadget. Reports to Operator. Entry: `.claude/agents/argus.md` |
| HENRY | Independent specialist — research writing. Entry: `.agents/hephaistos/HENRY.md` |
| Gadget | Independent specialist — frontier scout, external integrations. Entry: `.agents/hephaistos/GADGET.md` |
| Trismégiste | Operator continuity + vault agent. Entry: `.claude/agents/trismegiste.md` |
| Bowie | Consolidation + deduplication agent. Entry: `.claude/agents/bowie.md` |

## AI CLI Council (all report to Operator)
| Agent | Role |
|-------|------|
| Claude | General execution, skills, subagents |
| Codex | Code execution, architecture, file ops |
| Grok | Adversarial review, contradiction detection |
| [[memory/agents/Gemini|Gemini]] | Parallel synthesis, alternate review |
| Kimi | Additional code/reasoning seat |
| [[memory/agents/Antigravity|Antigravity (agy)]] | Workspace pair-programming, repo orientation |
| Vibe (Mistral) | Mistral council seat |

## Skills (PHAROS Skill Ecosystem — 56+ total)
| Skill | Function |
|-------|----------|
| philosopher | Meta-router (sovereign skill) |
| diamond-eyes | Aesthetic refinement |
| killcritic-x10think | Adversarial critique |
| skill-pairing | Dual-skill orchestration |
| boil-the-ocean | End-to-end execution without confirmation pauses |
| recursive-governance-method | Recursive data analysis + evidence hierarchy |
| trace-investigator | Authority trace across document packs |
| tmux-ai-council | Coordinate AI agents in tmux panes |
| tmux-council-loop | Bounded named AI council loop (wraps tmux-ai-council) |
| hermes-integration-monitor | Watches governance-constraint compliance in live execution |
| rook | Session start harness (`if_rook_session_start.sh`) — writes capabilities + postits arrival files |

## Operator
Martin Lepage — the human principal. All agents (three-agent stack, independent specialists, AI CLI council) report to Operator. ml@pharos-ai.ca.

## Lavoie Gate Prerequisites
| Gate | Required item |
|------|--------------|
| A1 | Canonical site URL + secondary domains |
| A2 | GSC viewer access → ml@pharos-ai.ca |
| A3 | GBP manager access → ml@pharos-ai.ca |
| A4 | LocalGo asset-control matrix signed by Israël (approved-requirements.md §8) |
| A5 | Zones/services list signed by Guillaume |
