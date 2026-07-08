---
type: wiki
title: GSD — Get Shit Done Context Engineering System
aliases:
- GSD
- get-shit-done
- get-shit-done-cc
tags:
- claude-code
- context-engineering
- agents
- workflow
- meta-prompting
- areas
- gsd-get-shit-done-context-engineering-system-md
- phase
- discuss
- planning
- milestone
- plans
- color-orange
status: active
created: '2026-04-16'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/GSD — Get Shit Done Context Engineering System.md
backlink_count: 16
backlinks:
- '[[Areas/PHAROS/Claude Code Skill Corpus]]'
- '[[Areas/PHAROS/Epistemic Operator — Operational Specification]]'
- '[[Areas/PHAROS/GSD Tier 1 — Core Workflow Skills Hub]]'
- '[[Areas/PHAROS/Kickstart App Prompt — Template and Synthesis Framework]]'
- '[[wiki/LightRAG — Graph-Based RAG System]]'
- '[[wiki/Martin Lepage — Adjacent Skill Ring]]'
- '[[Areas/PHAROS/Obsidian Agent Vault Launch — Commercial Skill]]'
- '[[wiki/PHAROS Final Voice Operator — GPT Creator]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[wiki/RAG-Anything — Multimodal RAG Framework]]'
- '[[Areas/PHAROS/Skill Ecosystem — Professional Capability Registry]]'
- '[[wiki/The Blind Leading the Automated — AI Governance Failure Case Study]]'
- '[[memory/agents/Decisions]]'
- '[[memory/agents/Events]]'
- '[[memory/agents/Journal]]'
- '[[memory/agents/Learning]]'
---

# GSD — Get Shit Done Context Engineering System

## Summary

GSD (Get Shit Done) is a lightweight, spec-driven meta-prompting framework for Claude Code and other AI coding tools. It solves **context rot** — the quality degradation that occurs as Claude fills its context window during long sessions. Closely related to [[HEPHAISTOS]] skill architecture and the [[EMERAULD Second Brain — Project Context]] workflow.

## Context

Ingested from `get-shit-done-main.zip` (2026-04-16). Relevant to the [[HEPHAISTOS]] forging system because GSD provides a complementary agent orchestration pattern: spec extraction → planning → parallel execution → verification. Compare with the local three-agent stack (HEPHAISTOS / Queen Keyport / Hermes).

Install: `npx get-shit-done-cc@latest` — installs to `~/.claude/skills/` (Claude Code 2.1.88+) or `.claude/commands/gsd/` (older).

## Details

### Core problem it solves
Context rot: as a session grows, model quality degrades because prior context crowds out the current task's relevant state. GSD maintains planning context separately from implementation context via structured spec files.

### Architecture

**Core planning files created:**
- `PROJECT.md` — Project vision, always loaded
- `REQUIREMENTS.md` — Scoped v1/v2 requirements with phase traceability
- `ROADMAP.md` — Where you're going, what's done
- `STATE.md` — Decisions, blockers, position (memory across sessions)
- `{phase}-CONTEXT.md` — Implementation decisions from discuss step
- `{phase}-{N}-PLAN.md` — Atomic task with XML structure
- `{phase}-VERIFICATION.md` — Phase delivery check
- `{phase}-UAT.md` — User acceptance test results

**Core workflow (6 steps):**
1. `/gsd-new-project` — Questions → research → requirements → roadmap
2. `/gsd-discuss-phase N` — Capture implementation decisions before planning (gray area resolution)
3. `/gsd-plan-phase N` — Research + create atomic plans + verify plans against requirements
4. `/gsd-execute-phase N` — Run plans in parallel waves, fresh 200k context per plan, atomic commits per task
5. `/gsd-verify-work N` — Walk through deliverables one by one; diagnose failures via debug agents
6. Loop → `/gsd-ship N` → `/gsd-complete-milestone` → `/gsd-new-milestone`

**Wave execution model:** Plans are grouped into dependency waves. Independent plans run in parallel within a wave; waves run sequentially. This keeps the main session context at 30–40% even during large phase executions. "Vertical slices" (feature end-to-end) parallelize better than "horizontal layers" (all models, then all APIs).

**XML task format:**
```xml
<task type="auto">
  <name>Create login endpoint</name>
  <files>src/app/api/auth/login/route.ts</files>
  <action>Precise implementation instructions</action>
  <verify>Verification command</verify>
  <done>Success criteria</done>
</task>
```

### Full command reference (v1.36.0)

**Core workflow:**
| Command | What it does |
|---|---|
| `/gsd-new-project [--auto]` | Full init: questions → research → requirements → roadmap |
| `/gsd-discuss-phase [N] [--auto] [--analyze] [--chain]` | Capture implementation decisions; `--chain` auto-chains into plan+execute |
| `/gsd-plan-phase [N] [--auto] [--reviews]` | Research + plan + verify |
| `/gsd-execute-phase <N>` | Execute plans in parallel waves |
| `/gsd-verify-work [N]` | Manual user acceptance testing |
| `/gsd-ship [N] [--draft]` | Create PR from verified phase work |
| `/gsd-next` | Auto-detect and run next step |
| `/gsd-fast <text>` | Inline trivial tasks — skips planning |
| `/gsd-complete-milestone` | Archive milestone, tag release |
| `/gsd-new-milestone [name]` | Start next version |
| `/gsd-forensics [desc]` | Post-mortem for failed workflow runs |
| `/gsd-milestone-summary [version]` | Summary for team onboarding |

**Session management:**
| Command | What it does |
|---|---|
| `/gsd-pause-work` | Write HANDOFF.json when stopping mid-phase |
| `/gsd-resume-work` | Restore from last session |
| `/gsd-session-report` | Summary of work performed |

**Code quality:**
| Command | What it does |
|---|---|
| `/gsd-review` | Cross-AI peer review of current phase or branch |
| `/gsd-secure-phase [N]` | Security enforcement with threat-model-anchored verification |
| `/gsd-docs-update` | Verified documentation generation |

**Phase management:**
| Command | What it does |
|---|---|
| `/gsd-add-phase` | Append phase to roadmap |
| `/gsd-insert-phase [N]` | Insert urgent work between phases |
| `/gsd-remove-phase [N]` | Remove future phase, renumber |

**Utilities:**
| Command | What it does |
|---|---|
| `/gsd-quick [--full] [--validate] [--discuss] [--research]` | Ad-hoc task with GSD guarantees |
| `/gsd-settings` | Configure model profile and workflow agents |
| `/gsd-set-profile <profile>` | Switch model profile (quality/balanced/budget/inherit) |
| `/gsd-debug [desc]` | Systematic debugging with persistent state |
| `/gsd-health [--repair]` | Validate `.planning/` directory integrity |
| `/gsd-stats` | Project statistics |

**Workstreams (parallel milestone work):**
- `/gsd-workstreams create/switch/complete <name>`

**Multi-project workspaces:**
- `/gsd-new-workspace`, `/gsd-list-workspaces`, `/gsd-remove-workspace`

### Configuration (`/gsd-settings` or `.planning/config.json`)

**Model profiles:**
| Profile | Planning | Execution | Verification |
|---|---|---|---|
| `quality` | Opus | Opus | Sonnet |
| `balanced` (default) | Opus | Sonnet | Sonnet |
| `budget` | Sonnet | Sonnet | Haiku |
| `inherit` | Inherit | Inherit | Inherit |

**Key workflow settings:**
| Setting | Default | What it does |
|---|---|---|
| `mode` | `interactive` | `yolo` vs confirm at each step |
| `workflow.research` | `true` | Research domain before planning |
| `workflow.plan_check` | `true` | Verify plans before execution |
| `workflow.verifier` | `true` | Confirm must-haves delivered |
| `workflow.auto_advance` | `false` | Auto-chain discuss → plan → execute |
| `workflow.discuss_mode` | `discuss` | `discuss` (interview) or `assumptions` (codebase-first) |
| `parallelization.enabled` | `true` | Run independent plans simultaneously |
| `git.branching_strategy` | `none` | `none`, `phase`, or `milestone` |

### Quality gates (built-in)
- Schema drift detection: flags ORM changes missing migrations
- Security enforcement: anchors verification to threat models
- Scope reduction detection: catches planner silently dropping requirements
- Context-window-aware prompt thinning for sub-200K models

### Security hardening (v1.27+)
- Path traversal prevention on user-supplied file paths
- Prompt injection detection via centralized `security.cjs` module
- PreToolUse `gsd-prompt-guard` hook scans writes to `.planning/`
- CI-ready injection scanner: `prompt-injection-scan.test.cjs`
- Safe JSON parsing for `--fields` arguments

**Protect sensitive files** by adding to Claude Code deny list in `.claude/settings.json`:
```json
{ "permissions": { "deny": ["Read(.env)", "Read(.env.*)", "Read(**/secrets/*)"] } }
```

### v1.36.0 highlights
- Knowledge graph integration (`/gsd-graphify`)
- TDD pipeline mode (`--tdd` flag)
- Project skills awareness: 9 agents discover and use project-scoped skills
- Registry-based SDK typed query command with classified errors
- Context-window-aware prompt thinning for sub-200K models
- 30+ bug fixes: worktree safety, state management, installer paths

## Key Ideas

- The system handles complexity internally; what the user sees is a few commands that work
- Planning context is kept separate from execution context to fight context rot
- Works across Claude Code, Cursor, Windsurf, Codex, Cline, and 10+ other AI coding tools
- Comparison point for [[HEPHAISTOS]]: GSD is product-oriented; HEPHAISTOS is governance-oriented

## Open Questions

- Does the GSD `gsd-graphify` agent complement or conflict with [[LightRAG — Graph-Based RAG System]] already running in EMERAULD?
- Could GSD agent templates inform HEPHAISTOS skill design?

## Sources

- Raw capture: `raw sources/get-shit-done-2026-04-16.md`
- Origin: https://github.com/gsd-build/get-shit-done (v1.36.0, 2026-04-15)

## Related

- [[HEPHAISTOS]] — Local three-agent stack; compare planning architecture
- [[claude-mem — Persistent Memory Compression for Claude Code]] — Complementary tool for context preservation
- [[LightRAG — Graph-Based RAG System]] — Knowledge graph backend; gsd-graphify overlap
- [[EMERAULD Second Brain — Project Context]] — Vault this note lives in
- [[GSD Tier 1 — Core Workflow Skills Hub]] — vault-side documentation hub for the GSD command family
- [[README]]
- [[2026 - notes_or_journal]]
