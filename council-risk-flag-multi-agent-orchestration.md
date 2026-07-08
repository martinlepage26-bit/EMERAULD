# Council Governance Flag: `multi-agent-orchestration` Skill

## Flag Raised By
Kimi Code CLI during tmux AI council skill-acquisition session.

## Skill
- **Name:** `multi-agent-orchestration`
- **Source:** `qodex-ai/ai-agent-skills@multi-agent-orchestration`
- **Install command used:** `npx skills add qodex-ai/ai-agent-skills@multi-agent-orchestration -y`
- **Installs:** 1.8K at time of installation

## Security Scan Results (from skills.sh installer)

| Scanner | Result |
|---|---|
| **Gen** | **High Risk** |
| Socket | 0 alerts |
| Snyk | Low Risk |

## What the Skill Contains
The skill is **documentation and code examples only**. It does not execute anything in the workspace. Its content includes:

- Descriptions of multi-agent orchestration patterns (sequential, parallel, hierarchical, consensus, tool-mediated)
- Code templates for CrewAI, AutoGen, LangGraph, and OpenAI Swarm
- Best practices and anti-patterns for agent teams
- Communication pattern examples (direct, shared memory, manager-based)

## Why the Gen Flag May Have Triggered
The skill contains code samples that:
- Import external Python packages (`crewai`, `autogen`, `langgraph`, `swarm`)
- Show agent-to-agent messaging and shared-memory patterns
- Include examples of dynamic agent creation and tool binding

These are legitimate educational examples, but a static scanner may flag them as "High Risk" because the patterns could be misused to create autonomous agent loops or expose tools.

## Why the Council Should Review
Per `AGENTS.md` and `QUEEN-KEYPORT.md`, Queen Keyport holds authority over governance constraints, approval thresholds, and refusal conditions. Argus holds flag-only audit authority. This skill does not directly violate any known binding principle, but because it is about designing autonomous multi-agent systems, it touches on:

- **Authority Without Power-Over** — the skill teaches hierarchical delegation; council must ensure any operational use preserves co-equal authority and single-owner control.
- **Machine Limitation** — the skill's examples assume agents can self-coordinate; council must remember the gap between model and reality.
- **Anti-Charm** — the skill's polished framework examples should not be mistaken for proven governance.

## Recommendation
1. **Queen Keyport** reviews the skill content at `/home/martin/.agents/skills/multi-agent-orchestration/SKILL.md`.
2. **Argus** audits whether operational use of this skill would drift the council away from canonical `AGENTS.md` controls (e.g., co-equal authority, operator arbitration, Hermes downstream routing).
3. If cleared, the skill can be used as a reference for **describing** council workflows, not as a runtime framework that replaces HEPHAISTOS/Queen Keyport/Hermes.
4. If not cleared, the skill can be removed with `npx skills remove qodex-ai/ai-agent-skills@multi-agent-orchestration` (or by deleting `/home/martin/.agents/skills/multi-agent-orchestration` and its symlinks).

## Council Decision Needed
Please respond with one of:
- **Cleared** — skill may be used as reference material.
- **Restricted** — skill may be used only with explicit operator approval per use.
- **Removed** — skill should be uninstalled.
