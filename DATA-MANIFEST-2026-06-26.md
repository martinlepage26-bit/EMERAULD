# DATA MANIFEST — `/home/martin`
# Generated: 2026-06-26T00:00:00Z (operator scan)
# Scope: Full home directory inventory
# Method: `find`, `du`, `ls`, git metadata, extension histogram
# Prior manifests: `MIGRATION-MANIFEST-2026-06-15.md`, `MIGRATION-MANIFEST-2026-06-21.md`

---

## 1. Executive Summary

| Metric | Value |
|--------|-------|
| **Total disk footprint** | ~34 GB |
| **Total files** | 527,102 |
| **Total directories** | 72,356 |
| **Source files** (excl. node_modules, .git, .cache, .npm, .venvs, .vscode-server) | 138,387 |
| **Git repositories** | 25 |
| **Markdown files** | 18,971 |
| **TypeScript files** | 60,478 |
| **JavaScript files** | 132,723 |
| **Python files** | 41,545 |

**Operator:** Martin Lepage — PHAROS (pharos-ai.ca), Montréal  
**Canonical control layer:** `AGENTS.md` → symlink to `.agents/hephaistos/AGENTS.md`  
**Canonical memory:** `CLAUDE.md` (workspace root)

---

## 2. Top-Level Taxonomy

```
/home/martin/
├── CONTROL & MEMORY
│   ├── AGENTS.md          → .agents/hephaistos/AGENTS.md (symlink)
│   ├── BOARD.md           → .agents/hephaistos/BOARD.md (symlink)
│   ├── CLAUDE.md          Workspace memory (projects, people, stack)
│   ├── TASKS.md           Active/waiting/someday/done task ledger
│   ├── company.md, glossary.md
│   └── MIGRATION-MANIFEST-*.md, PHAROS-AI CHANGE TRACKER.md
│
├── PRODUCTS & APPS
│   ├── apps/
│   │   ├── web-apps/      PHAROS + Martin-surface web products
│   │   ├── mobile-apps/   React Native / Expo apps
│   │   └── ai-agent-board/ Agent coordination monorepo (1.7G)
│   └── products/          pharos-governance-tools (140K)
│
├── PUBLIC SURFACES
│   └── websites/          Static sites, Astro personal site, CF Pages
│
├── CLIENT
│   └── Lavoie/            Groupe Lavoie consulting (455M)
│
├── KNOWLEDGE
│   └── EMERAULD/          Obsidian vault (154M, 2,126 .md files)
│
├── INFRASTRUCTURE
│   └── infra/             Tooling, ML pipeline, VSCode ext, peer review (802M)
│
├── AI CLI RUNTIMES
│   ├── .claude/           Claude Code (1.8G, 90 skills)
│   ├── .codex/            Codex (312M, 84 skills)
│   ├── .grok/             Grok (539M, 72 skills)
│   ├── .agents/           Hephaistos canonical docs + CF skills (11M, 15 skills)
│   ├── .gemini/           Gemini / Antigravity (1018M)
│   ├── .kimi-code/        Kimi (295M)
│   ├── .vibe/               Mistral Vibe (3.4M)
│   ├── .aider/, .copilot/, .deepcode/, .coderabbit/
│   └── .hermes/, .hermes-codex-home/
│
├── RUNTIME DEPENDENCIES (not source)
│   ├── .cache/            6.6G
│   ├── .venvs/            5.6G
│   ├── .npm/              4.0G
│   ├── .nvm/              1.6G
│   ├── .vscode-server/    3.2G
│   ├── .local/            2.3G
│   └── .wrangler/         23M
│
├── SESSION & TOOLING
│   ├── CLAUDEX/           Claude session transcripts (19 files, 228K)
│   ├── agentboard/        Agent board config + projects
│   ├── workspaces/        mock-governance-dataset
│   ├── remote-bundles/    Codex remote bundle (2026-03-17)
│   ├── aider/             Aider tooling (552K)
│   ├── bin/               User scripts
│   └── test-results/      Playwright output
│
└── ASSETS & MISC
    ├── pharos-logo-128.{png,svg}
    ├── voice-dictation.ahk
    ├── martin-mtl-03-codex-claude-session-ids.csv
    ├── .UPLOADS/          13M staging
    ├── Downloads/         32K
    └── snap/              20K
```

---

## 3. Disk Allocation (Top 30)

| Path | Size | Class |
|------|------|-------|
| `.cache/` | 6.6G | Runtime cache |
| `.venvs/` | 5.6G | Python virtualenvs |
| `apps/` | 4.6G | Product source |
| `.npm/` | 4.0G | Node package cache |
| `.vscode-server/` | 3.2G | Remote IDE server |
| `.local/` | 2.3G | Local app data |
| `.claude/` | 1.8G | Claude Code runtime |
| `.nvm/` | 1.6G | Node version manager |
| `.gemini/` | 1018M | Gemini/Antigravity |
| `infra/` | 802M | Infrastructure tooling |
| `websites/` | 792M | Public sites |
| `.grok/` | 539M | Grok runtime |
| `Lavoie/` | 455M | Client project |
| `.codex/` | 312M | Codex runtime |
| `.kimi-code/` | 295M | Kimi runtime |
| `EMERAULD/` | 154M | Knowledge vault |
| `.wrangler/` | 23M | Cloudflare CLI state |
| `.railway/` | 19M | Railway deploy state |
| `.UPLOADS/` | 13M | Upload staging |
| `.agents/` | 11M | Hephaistos + CF skills |
| `.vibe/` | 3.4M | Mistral Vibe |
| `.coderabbit/` | 3.1M | CodeRabbit |
| `workspaces/` | 2.0M | Governance datasets |
| `.aider/` | 1.6M | Aider |
| `.config/` | 1.2M | User config |
| `aider/` | 552K | Aider repo |
| `.dotnet/` | 264K | .NET tooling |
| `CLAUDEX/` | 228K | Session transcripts |
| `products/` | 140K | Governance tools stub |
| `remote-bundles/` | 32K | Remote bundle archive |

---

## 4. Applications — `apps/`

### 4.1 Web Apps — `apps/web-apps/` (2.8G)

| Project | Size (approx) | Source files | Git | Public surface | Notes |
|---------|---------------|--------------|-----|----------------|-------|
| **pharos-suite** | ~2.2G | 1,115 | yes | pharos-ai.ca | Canonical PHAROS repo. Remote: `github.com/martinlepage26-bit/pharos-suite.git`. Branch: `main`. Last commit: 2026-06-22 |
| ECHOapp | — | 17,366 | yes | Martin surface | Full-stack (frontend + backend) |
| corpus-5point | — | 882 | partial | — | Legacy patent workbench nested git |
| gaia | — | 386 | no | martin.govern-ai.ca/gaia | Vue + Terraform UI |
| extensions | — | 252 | no | — | Browser extensions |
| nexusos | — | 131 | yes | — | base44 SPA |
| Agency | — | 79 | yes | martin.govern-ai.ca | Lotus, Scripto, DR. SORT |
| DG | — | 68 | yes | — | Full-stack |

#### pharos-suite internal map

| Subdirectory | Size | Role |
|--------------|------|------|
| `frontend/` | 895M | Canonical React frontend (pharos-ai.ca) |
| `PHAROS-NEWLOOK/` | 536M | Reference skin — absorption into frontend/ in progress |
| `aurorai/` | 292M | AurorA Worker (D1/R2/TS) + FastAPI backend |
| `compassai/` | 244M | COMPASSai governance engine |
| `helix/` | 96M | HELIX stress-test protocol (nested git) |
| `docs/` | 73M | Specs, deployment, D1/R2 mapping |
| `pharos-products/` | 28M | Product modules |
| `backend/` | 124K | Shared Python backend |
| `shared/` | 72K | Handoff contracts, shared types |
| `pharos-workers/` | 88K | CF Workers (live proxy) |
| `pharos_governance_suite/` | 1.1M | Governance suite modules |
| `pharos_integrations/` | 44K | Integration stubs |
| `pharos_mcp/` | 44K | MCP server stubs |
| `mock-data/` | 300K | Test fixtures |
| `skills/` | 56K | In-repo skills |
| `infra/` | 96K | CF worker infra |
| `assets/` | 8.1M | Brand assets |

**Deployed Worker:** `aurora-pharos` — last successful CI deploy 2026-05-20

### 4.2 Mobile Apps — `apps/mobile-apps/` (172M)

| Project | Source files | Git | Notes |
|---------|--------------|-----|-------|
| GAIAapp | 15,111 | no | GAIA product |
| clearday-mobile | 71 | no | ClearDay mobile |
| fantasycast-gay | 20 | yes | Expo React Native |
| lotus-mobile | 42 | no | LOTUS mobile |

### 4.3 Agent Board — `apps/ai-agent-board/` (1.7G)

Monorepo with packages (client, server, e2e), `.squad/` orchestration, MCP integration. Source files: 351 (excluding node_modules). Git: yes.

---

## 5. Websites — `websites/` (792M)

| Site | Size | Source files | Git | Deploy target | Stack |
|------|------|--------------|-----|---------------|-------|
| martinlepage26-bit.github.io | 470M | 968 | no | martin.govern-ai.ca | Astro + CF Pages + echo-tts Worker |
| glammy-site | 303M | 65 | yes | — | Static HTML portfolio |
| VoiceBridge | 17M | 96 | yes | CF Pages | wrangler.toml |
| clearday | 1.5M | 5 | yes | — | Static HTML |
| reflexive-inhabitation-audit | 556K | 43 | yes | — | React |
| percephal | 304K | 5 | yes | — | CF landing page |
| gov-2026-06-25 | 280K | 6 | no | — | CF Pages (wrangler.jsonc) |
| martinlepage26-bit.github.io-echo | 124K | 0 | yes | — | Empty portfolio echo |

---

## 6. Infrastructure — `infra/` (802M)

| Path | Size | Source files | Notes |
|------|------|--------------|-------|
| `src/infrafabric-vscode` | 759M | — | VSCode extension (dominant) |
| `src/if-switchboard-runtime` | 1.4M | — | IF switchboard runtime |
| `PEER-REVIEW` | 30M | 45 | Academic research docs. Git: yes |
| `distillation` | 516K | 81 | ML training pipeline |
| `micro1` | 13M | 44 | Interview prep project |
| `agent-collab` | 12K | 2 | Agent coordination tooling |

**Not present (migrated per 2026-06-21 manifest):** `Client-Delivery-Environment`, `aether` — may have been removed or consolidated.

---

## 7. Client — `Lavoie/` (455M)

| Component | Size | Notes |
|-----------|------|-------|
| `site/` | 454M | CF Pages site + functions + wrangler |
| Root docs | ~1M | Plans, offers, handoffs, diagnostics |
| `offre-lavoie-domain-proxy/` | — | Domain proxy Worker |
| `artifacts/` | 12K | Deliverables |

**Git:** yes (private client repo)  
**Governed env:** `.env` (600 permissions expected)  
**Status:** On ice pending gates A1–A5 (see `TASKS.md`)  
**Key artifacts:** `jade-base44-handoff.md`, `plan-directeur-lavoie-2026.md`, `MESSAGE_SUIVI_PATRICIA.md`

---

## 8. Knowledge Vault — `EMERAULD/` (154M)

| Zone | Size | Contents |
|------|------|----------|
| `raw sources/` | 65M | Unprocessed source material |
| `assets/` | 25M | Media, attachments |
| `wiki/` | 7.2M | 886 files — topics: archive, bridges, genealogy, raw-sources, skills |
| `archive/` | 2.7M | Archived notes |
| `tmp/` | 2.1M | Scratch |
| `raw/` | 2.0M | Raw captures |
| `artifacts/` | 996K | Build artifacts incl. pharos-migration-pr4 |
| `personal-assistant-agents/` | 744K | PA agent configs |
| `governance/` | 704K | Governance notes |
| `memory/` | 608K | Session memory |
| `Publications/` | 324K | Academic/publication drafts |
| `scripts/` | 336K | Vault automation |
| `hephaistos/` | 100K | Hephaistos mirror docs |
| `_vault/` | 124K | Vault internals |

**Totals:** 2,126 markdown files vault-wide  
**Git:** yes  
**Session state:** `session-state.md`, `memory.md`, `CLAUDE.md`

---

## 9. Governance Layer — `.agents/hephaistos/` (494 source files)

Canonical three-agent architecture documentation. Symlinked to workspace root via `AGENTS.md` and `BOARD.md`.

**Core identity docs:** HEPHAISTOS.md, QUEEN-KEYPORT.md, HERMES.md, HENRY.md, GADGET.md  
**Binding specs:** CO-EQUAL-AUTHORITY-DECISION.md, L99-DEMOTION-TO-ARGUS.md, SPECIALIST-GUIDELINE-AUTHORITY.md  
**Handoff packets:** hephaistos-to-queen-keyport.md, queen-keyport-to-hermes.md  
**Phase completion:** PHASE-1 through PHASE-7  
**Skills tree:** 49 skill directories in-repo  
**Argus:** `argus/` subdirectory

**Cloudflare skills:** `.agents/skills/` — 15 SKILL.md files (cloudflare, wrangler, workers-best-practices, durable-objects, agents-sdk, turnstile-spin, etc.)

---

## 10. AI CLI Council — Runtime Inventory

| CLI | Path | Disk | Skills | Agents | Auth/state |
|-----|------|------|--------|--------|------------|
| Claude Code | `.claude/` | 1.8G | 90 | 20 agent defs | cache, commands, plugins, backups |
| Codex | `.codex/` | 312M | 84 | — | auth.json, sqlite logs/goals/memories |
| Grok | `.grok/` | 539M | 72 | — | auth.json, bundled skills, marketplace-cache |
| Gemini/Antigravity | `.gemini/` | 1018M | — | — | antigravity-cli, projects.json |
| Kimi | `.kimi-code/` | 295M | — | — | oauth, sessions, telemetry |
| Mistral Vibe | `.vibe/` | 3.4M | — | — | config.toml, vibehistory |
| Aider | `.aider/` + `aider/` | 1.6M + 552K | — | — | oauth-keys.env, chat history |
| CodeRabbit | `.coderabbit/` | 3.1M | — | — | PR review integration |
| Hermes | `.hermes/` | 12K | — | — | secrets (governed) |

**Council seats (per CLAUDE.md):** Claude, Codex, Grok, Gemini, Kimi, Antigravity, Vibe (Mistral)

---

## 11. Git Repositories (25)

| Repository | Path |
|------------|------|
| pharos-suite (canonical) | `apps/web-apps/pharos-suite` |
| helix (nested) | `apps/web-apps/pharos-suite/helix` |
| patent-workbench (nested) | `apps/web-apps/corpus-5point/legacy/patent-workbench` |
| ai-agent-board | `apps/ai-agent-board` |
| Agency | `apps/web-apps/Agency` |
| DG | `apps/web-apps/DG` |
| ECHOapp | `apps/web-apps/ECHOapp` |
| nexusos | `apps/web-apps/nexusos` |
| fantasycast-gay | `apps/mobile-apps/fantasycast-gay` |
| EMERAULD | `EMERAULD` |
| Lavoie | `Lavoie` |
| aider | `aider` |
| hephaistos | `.agents/hephaistos` |
| PEER-REVIEW | `infra/PEER-REVIEW` |
| VoiceBridge | `websites/VoiceBridge` |
| clearday | `websites/clearday` |
| glammy-site | `websites/glammy-site` |
| percephal | `websites/percephal` |
| reflexive-inhabitation-audit | `websites/reflexive-inhabitation-audit` |
| martinlepage26-bit.github.io-echo | `websites/martinlepage26-bit.github.io-echo` |
| tmux-ai-council (skill) | `.codex/skills/tmux-ai-council` |
| nvm | `.nvm` |
| claude-plugins-official | `.claude/plugins/marketplaces/claude-plugins-official` |
| codex plugins tmp | `.codex/.tmp/plugins` |
| grok marketplace cache | `.grok/marketplace-cache/*` (2) |

---

## 12. Cloudflare Deployment Map

| wrangler config | Project |
|-----------------|---------|
| `pharos-suite/wrangler.toml` | Root PHAROS Pages |
| `pharos-suite/aurorai/wrangler.toml` | AurorA Worker (`aurora-pharos`) |
| `pharos-suite/compassai/wrangler.toml` | COMPASSai Worker |
| `pharos-suite/PHAROS-NEWLOOK/wrangler.toml` | Legacy skin reference |
| `pharos-suite/pharos-workers/*` | Live proxy workers |
| `pharos-suite/infra/*` | API + live proxy workers |
| `Lavoie/site/wrangler.toml` | Client site |
| `Lavoie/offre-lavoie-domain-proxy/wrangler.toml` | Domain proxy |
| `websites/VoiceBridge/wrangler.toml` | VoiceBridge |
| `websites/martinlepage26-bit.github.io/wrangler.toml` | Martin personal site |
| `websites/martinlepage26-bit.github.io/workers/echo-tts-online/` | ECHO TTS Worker |
| `websites/percephal/wrangler.toml` | Percephal landing |
| `websites/gov-2026-06-25/wrangler.jsonc` | Governance snapshot site |
| `apps/web-apps/DG/worker/wrangler.toml` | DG worker |
| `apps/web-apps/corpus-5point/frontend/wrangler.jsonc` | Corpus frontend |
| `EMERAULD/cloudflare/figma-mcp-server/wrangler.jsonc` | Figma MCP server |

**Account handle:** MLePage26  
**Brand colors:** Deep teal `#0a3d4f`, Champagne gold `#b8962e`

---

## 13. Public Surface Topology

| URL | Canonical repo/path | Surface |
|-----|---------------------|---------|
| https://pharos-ai.ca | `apps/web-apps/pharos-suite` → `frontend/` | PHAROS business |
| https://martin.govern-ai.ca | `websites/martinlepage26-bit.github.io` | Martin personal/educational |
| `/lotus`, `/scripto`, `/gaia`, `/echo`, `/dr-sort` | Agency, GAIA, ECHOapp (Martin surface only) | Martin products |
| AurorA, COMPASSai, HELIX | pharos-suite subdirs | PHAROS surface only |

**Deleted/historical (not current authority):** pharos-suite-review.pages.dev, preview-api.pharos-ai.ca

---

## 14. Governed & Sensitive Artifacts (paths only)

| Path | Type | Notes |
|------|------|-------|
| `.env.local` | Env | Root local secrets |
| `Lavoie/.env` | Env | Client credentials |
| `.aider/oauth-keys.env` | OAuth | Aider auth |
| `.hermes/secrets` | Secrets dir | Hermes governed |
| `.gemini/antigravity-cli/antigravity-oauth-token` | OAuth | Gemini |
| `.config/obsidian-second-brain/.env` | Env | Obsidian bridge |
| `.vibe/.env` | Env | Vibe CLI |
| `.codex/auth.json`, `.grok/auth.json` | Auth | CLI session tokens |
| `.vscode-server/cli/agent-host-token` | Token | VS Code remote |
| `.config/gcloud/access_tokens.db` | OAuth | GCloud |
| `.ssh/` | Keys | SSH (24K) |

**Permission target for secrets:** `600` where applicable

---

## 15. File Type Distribution (Top 20 extensions)

| Extension | Count | Extension | Count |
|-----------|-------|-----------|-------|
| `.js` | 132,723 | `.json` | 22,173 |
| `.ts` | 60,478 | `.md` | 18,971 |
| `.py` | 41,545 | `.mjs` | 9,807 |
| `.map` | 40,324 | `.cjs` | 6,361 |
| `.pyc` | 31,129 | `.txt` | 2,378 |
| `.h` | 28,509 | `.png` | 1,144 |

---

## 16. Creative & Scholarly Works (in vault / tasks, not isolated dirs)

| Codename | Status | Primary location |
|----------|--------|------------------|
| RDAIG manuscript | In progress | EMERAULD / tasks |
| Self-Polygraph Protocol | Paper experiment | EMERAULD / tasks |
| Why Be King? | PhD → book | EMERAULD |
| The Broken Frequency of the Word | Novel | EMERAULD |
| VIGIL/GSK | Clinical trial proposal | EMERAULD |
| RECURSO/RECURSOTRUE | 14-layer framework | EMERAULD / hephaistos |
| HEXA / Hexadecimal Mystic | Art project | External (Substack, X) |

---

## 17. Operational State (from TASKS.md, 2026-06-26)

**Active:**
- Verify Lavoie Patricia message sent
- Wrangler bindings confirmation (R2, D1)
- PHAROS-NEWLOOK → frontend/ absorption

**Waiting:**
- Lavoie gates A1–A5 (via Patricia)
- Lavoie corpus + process documentation

**Recently completed:**
- Home directory migration (2026-06-21)
- BOARD.md authority-chain lint PASS (176 checks, 2026-06-22)
- AurorA Module 03 intake build
- Three-agent architecture Phases 1–7

---

## 18. Cross-References

| Document | Purpose |
|----------|---------|
| `MIGRATION-MANIFEST-2026-06-21.md` | Directory reorg record (COMPLETE) |
| `apps/web-apps/pharos-suite/MANIFEST.md` | PHAROS repo manifest |
| `CLAUDE.md` | Operator memory (projects, people, terms) |
| `TASKS.md` | Task ledger |
| `PHAROS-AI CHANGE TRACKER.md` | Change log |
| `EMERAULD/session-state.md` | Vault session continuity |

---

## 19. Scan Limitations

- **node_modules / .git / caches** excluded from per-project source file counts
- **Binary content** not inspected (images, fonts, compiled artifacts counted by extension only)
- **Secret values** not read or recorded — paths only
- **Live deploy state** inferred from wrangler configs + TASKS.md; not runtime-verified in this scan
- **Nested git submodules** may exist beyond the 25 repos listed

---

*End of manifest.*