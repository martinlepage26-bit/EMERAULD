# Architecture Summary: HEPHAISTOS Multi-Agent Governance Framework

**Audit target:** `/home/martin` governance documentation and operational context  
**Application type:** Local multi-agent governance / constitutional orchestration layer  
**Primary users:** Operator (Martin Lepage) and AI CLI agents (Claude, Codex, Grok, Gemini, Kimi, Antigravity, Mistral/Vibe)  
**Tech stack:** Markdown constitution files, symlinks, skills ecosystem (`~/.agents/skills/`, `~/.codex/skills/`), tmux, Cloudflare platform (downstream targets)  
**Comparable systems:** Anthropic Constitutional AI, Microsoft AutoGen / CrewAI / LangGraph, OpenAI Swarm, internal PHAROS frameworks (RDAIG, RECURSO, HELIX, DAST)

---

## 1. What This System Is

HEPHAISTOS is a local constitutional layer for coordinating multiple AI agents under a single operator. It is not the application code itself; it sits above projects like `pharos-suite` and `martin-lepage-site` and defines:

- A three-agent core stack: **HEPHAISTOS** (artifact/scope), **Queen Keyport** (governance/constraints), **Hermes** (routing/monitoring)
- Independent specialists at **Argus level**: Argus (meta-governance auditor), HENRY (research writing), Gadget (external integration)
- Operator-facing council peers: Codex, Grok
- Co-equal authority model with operator arbitration on conflicts
- Binding principles (Seven Ethical Ground values, Diamond-Eyes gate, Anti-Charm, Machine Limitation, etc.)
- Canonical handoff packets and path-authority rules

---

## 2. Trust Model

### Actors and Authority

| Actor | Authority | Enforced By |
|---|---|---|
| **Operator (Martin)** | Final arbitration, single-owner control, override with justification | `AGENTS.md`, `CO-EQUAL-AUTHORITY-DECISION.md`, `SPECIALIST-GUIDELINE-AUTHORITY.md` |
| **HEPHAISTOS** | Artifact definition, scope boundaries, evidence requirements, skill composition | `HEPHAISTOS.md`, `HEPHAISTOS_OPERATIONS.md` |
| **Queen Keyport** | Governance constraints, approval thresholds, refusal conditions | `QUEEN-KEYPORT.md`, `QUEEN-KEYPORT_OPERATIONS.md` |
| **Hermes** | Routing, monitoring, escalation (downstream only) | `HERMES.md` |
| **Argus** | Meta-governance audit; flag-only findings | `ARGUS.md` |
| **HENRY / Gadget** | Independent specialists; report to operator; bound by Class 1 principles | `AGENTS.md`, `SPECIALIST-GUIDELINE-AUTHORITY.md` |
| **Codex / Grok** | Council peers; direct operator findings | `AGENTS.md` |

### Key Trust Boundaries

- **No cryptographic identity**: agent identity and authority are document-proclaimed and procedurally enforced.
- **Co-equal authorities**: HEPHAISTOS and Queen Keyport neither outrank the other; conflicts escalate to the Operator.
- **Operator override is the ultimate bypass**: direct user instructions take precedence over all governance docs.
- **Hermes is downstream**: it does not adjudicate conflicts; it routes or escalates them back.
- **Argus is flag-only**: findings are recommendations, not mandates.

---

## 3. Input Surfaces

### Network-Facing Surfaces
- Public downstream targets: `https://pharos-ai.ca`, `https://martin.govern-ai.ca`, `https://aurora-pharos.martinlepage26.workers.dev`
- InfraFabric hosted API / managed MCP front door (`if-cli blackboard api ...`)
- Session bootstrap: `/root/scripts/if_rook_session_start.sh` reads `/root/.claude/projects/-root/*.jsonl`
- Rule: never use direct `10.10.10.170` MCP URLs

### File-Based Input
- Constitutional markdown: `AGENTS.md`, `HEPHAISTOS.md`, `QUEEN-KEYPORT.md`, `HERMES.md`, `ARGUS.md`, `CLAUDE.md`
- Canonical handoff packets: `.agents/hephaistos/hephaistos-to-queen-keyport.md`, `.agents/hephaistos/queen-keyport-to-hermes.md`
- Supporting governance: `CO-EQUAL-AUTHORITY-DECISION.md`, `L99-DEMOTION-TO-ARGUS.md`, `SPECIALIST-GUIDELINE-AUTHORITY.md`, `HEPHAISTOS_OPERATIONS.md`, `QUEEN-KEYPORT_OPERATIONS.md`
- Skill definitions: `~/.agents/skills/*/SKILL.md`, `~/.codex/skills/`
- Session state: `/root/.codex/rook_arrival/capabilities.current.md`, `/root/.codex/rook_arrival/postits.current.md`
- Trackers: `MASTER TRACKER ... .md`

### IPC / Inter-Service Input
- Canonical handoff packets mediate agent transitions.
- Shared skill directories are loaded by agents at runtime.
- InfraFabric blackboard API is the durable task-state authority.

### User-Generated Content Surfaces
- Operator instructions in chat/prompts (highest precedence)
- Operator-curated memory (`CLAUDE.md`)
- Agent outputs recorded in trackers, handoffs, session notes

### External Integrations
- Cloudflare platform (Workers, Pages, D1, R2, AI, Vectorize, Email, Turnstile, Tunnels, WAF)
- GitHub repos (`pharos-suite`, `martinlepage26-bit.github.io`)
- FastAPI + MongoDB backends for AurorA and COMPASSai
- Wrangler, pnpm/npm, Obsidian, tmux

---

## 4. Dangerous Sinks

| Sink | Risk | Mitigation Observed |
|---|---|---|
| **Skill loading** | Malicious/erroneous skill files alter agent behavior; infra skills can drive deployments | Skills are installed from skills.sh with security scans; local skill directory is writable by operator |
| **Session start script** | Tampering with JSONL input hijacks session context | Located in `/root/` (root-owned) |
| **Symlink / path redirection** | `~/AGENTS.md` symlink; retired paths can subvert authority checks | Canonical packets control over divergent summaries |
| **Operator override** | Direct user instructions override governance docs | By design; operator is single-owner control |
| **MCP / remote coordination** | Prohibited direct `10.10.10.170` URLs could connect to untrusted servers | Explicitly forbidden in `AGENTS.md` |
| **Hermes downstream routing** | Misconfigured webhooks/API targets could promote harmful artifacts | Work only routes after upstream clearance |
| **Tracker / credential files** | Secrets with broad permissions; sensitive operational context | `600` target for secret files under `/home/cerebrhoe`; rotation required if exposed |
| **Governance conflict bypass** | Automated bypass of HEPHAISTOS/QK conflict degrades control model | Conflicts must be operator-arbitrated |

---

## 5. Key File Paths for Phase 2 Hunting

- `/home/martin/AGENTS.md`
- `/home/martin/HEPHAISTOS.md`
- `/home/martin/QUEEN-KEYPORT.md`
- `/home/martin/HERMES.md`
- `/home/martin/ARGUS.md`
- `/home/martin/CLAUDE.md`
- `/home/martin/.agents/hephaistos/hephaistos-to-queen-keyport.md`
- `/home/martin/.agents/hephaistos/queen-keyport-to-hermes.md`
- `/home/martin/.agents/hephaistos/CO-EQUAL-AUTHORITY-DECISION.md`
- `/home/martin/.agents/hephaistos/SPECIALIST-GUIDELINE-AUTHORITY.md`
- `/home/martin/.agents/hephaistos/HEPHAISTOS_OPERATIONS.md`
- `/home/martin/.agents/hephaistos/QUEEN-KEYPORT_OPERATIONS.md`
- `/home/martin/.agents/skills/*/SKILL.md`

---

## 6. Audit Notes

- This is a **documentation/constitutional system**, not executable application code. Traditional code vulnerabilities (SQLi, XSS, etc.) are not applicable.
- The primary security concerns are **governance integrity**, **path-authority correctness**, **skill supply-chain trust**, and **operator-override accountability**.
- Prior runs: none.
