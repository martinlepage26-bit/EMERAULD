---
type: sales-page-outline
title: Elemental Agents — Sales Page Outline
aliases:
- assets/elemental-agents/sales-page-outline
tags:
- sales-page-outline
- assets
- elemental-agents
- agent
- validator
- framework
- script
- show
- color-orange
status: draft
created: '2026-05-24'
updated: '2026-06-26'
vault_area: assets
canonical_path: assets/elemental-agents/sales-page-outline.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
target_surface: gumroad + github README
voice_rules_from: Obsidian Agent Vault Launch — Commercial Skill (v2)
---

# Elemental Agents — Sales Page Outline

## Headline (8–12 words)

**The role layer your file-aware agent has been missing.**

Alternative drafts:

- Ten agents, six orchestration phases, one shell script that polices them all.
- A multi-agent framework that fails loud when it drifts.
- Markdown role contracts for Claude Code, Cursor, and any file-aware AI.

## Subhead (one sentence)

A file-native multi-agent execution framework — ten explicit role contracts, six orchestration phases, and a validation matrix that polices its own structure on every commit. No SDK. No daemon. No new infrastructure.

## Problem (2–3 short paragraphs)

When you give your AI agent more than one job to do, it starts hand-waving. It calls itself a "coordinator" in one paragraph and a "tester" two paragraphs down. It never tells you which role is producing the verdict. It never tells you which gates were checked. It never tells you what got skipped.

You can solve this with a graph runtime, an SDK, a daemon, and a vector database. Or you can solve it by giving your agent explicit role contracts in markdown — files the agent can read, files you can audit, files that fail a shell check when they drift.

This is the second option.

## Mechanism (the "what's in the box" section)

- **10 agent contracts** (`agents/01-prime-coordinator.md` through `10-delivery-operator.md`) — each one specifies Mission, Inputs, Procedure, Pairing protocol, Triangulation protocol, Outputs. Drop them into any file-aware agent's context.
- **6 orchestration phases** (`orchestration/01-intake-and-routing.md` through `06-recovery-and-escalation.md`) — the ordering and gates that the agents move through.
- **165 named combinations** — 45 duals + 120 triples, each one a composed verb (Water+Fire = `diagnose-then-execute`), each one with a documented best-use-case, risk, lead agent, supporting cast, handoff, and autonomous trigger.
- **`validate-combinations.sh`** — 216 lines of awk-based enforcement. Counts integrity. Unique permutations. No token stutter. Escalation rules. Pre-commit hook ready.
- **Triangulated validation** — every gate validates from three independent angles: build (structure), quality (content), governance (assumptions/risk/deviation).
- **6 worked examples** — feature request implementation, code review, bug triage, incident response, post-incident retrospective, release readiness.

## Proof (the visible asymmetry vs. competitors)

Most agent frameworks ask you to learn their abstractions. Elemental Agents asks the agent to read your file structure.

| | Elemental Agents | AutoGen / CrewAI / LangGraph |
|---|---|---|
| Runtime dependency | None | Python + framework SDK |
| Visible role boundaries | 10 markdown files | Hidden in code |
| Self-policing | Shell script + git hook | None included |
| Validation philosophy | Triangulated (3 angles) | Single-angle (tests pass / fail) |
| Buyer learning curve | Read 10 markdown files | Learn the SDK |
| Marginal install time | 60 seconds | Hours |

**The video demo:** record three minutes. Route a feature request through all ten agents. Run the validator. Show the triangulated verdict ledger. That is the entire proof regime. Buyers either get it in three minutes or they were never the buyer.

## Pricing ladder

| Tier | Price | What ships |
|---|---|---|
| **GitHub repo** (lead) | Free, MIT | Full framework markdown + validator + install hooks + examples |
| **Skill Pack** (Gumroad) | $49 | Claude Code skill bundle: install script, agent file pack, validator with pre-configured hooks, branded PDF reference card, 2 worked example transcripts |
| **Sprint** (warm intro only) | $35k–$125k | [[PHAROS Procurement-Unblock Sprint]] — full governance dossier, decision-rights map, evidence pack for stalled enterprise AI deals. Not sold here; mentioned at the bottom only. |

**The $49 tier is the qualification filter.** Anyone who buys at $49 has self-identified as a serious agent operator. They become the warm list for the Sprint upsell.

## Buyer fit

This is for you if:

- You ship agent workflows in Claude Code, Cursor, Aider, or any file-aware AI.
- You've already tried prompting your way to multi-role orchestration and watched the agent collapse into one voice.
- You want explicit role boundaries you can audit, not implicit ones you have to guess at.
- You'd rather read ten markdown files than learn another SDK.
- You believe naming an abstraction is part of engineering it.

## Anti-fit (the explicit no-list)

This is **not** for you if:

- You want a managed runtime, a hosted dashboard, or a vendor's API.
- You expect agents to "just work" with no structural discipline on your side.
- You react badly to symbolic names (Water, Fire, Earth, Spirit, Chi, Akasha). The framework uses these on purpose, throughout. There is a defense of this choice in the lead-magnet PDF, but if the names are a dealbreaker, save your money.
- You're looking for a Python library to import.

## FAQ (5–6 questions)

**Q: Why elements? Why not just "Coordinator, Engineer, Tester"?**
A: Because composed verbs are how you get from "ten roles" to "165 combinations" without the combinatorics collapsing into mush. Water diagnoses. Fire executes. Water+Fire is a specific composed behavior ("diagnose-then-execute") with its own pairing rules. The element vocabulary is the index that makes the combinations addressable. Read the lead-magnet PDF for the full defense.

**Q: Does this work with [my agent stack]?**
A: If your agent reads files, yes. The framework is markdown plus a shell script. There is no runtime to integrate.

**Q: How long does it take to install?**
A: Sixty seconds to clone the repo and run `install-hooks.sh`. Five to fifteen minutes to read the ten agent contracts. Zero ongoing maintenance unless you change a contract.

**Q: Why is the $49 Skill Pack different from the free GitHub repo?**
A: The repo has the framework. The Skill Pack adds the installable Claude Code skill bundle, a branded PDF reference card, and two end-to-end example transcripts that show the framework running. If you only want to read the framework, take the free repo.

**Q: Is this part of PHAROS?**
A: It's adjacent. PHAROS is a governance method for enterprise AI risk. Elemental Agents is a file-native execution framework. They share a philosophy (evidence first, explicit gates, triangulated verdicts) but they're sold separately. If your enterprise deal is stalled in procurement or audit, the [[PHAROS Procurement-Unblock Sprint]] is the right offer; reach out directly.

**Q: What's the license?**
A: Framework markdown is MIT. Validator script and install hooks follow the same MIT terms. The branded PDF reference card in the Skill Pack is licensed for personal/single-team use; multi-team license available.

## CTA

**Primary:** *Clone the repo. Run it on your next feature. If it changes how your agent behaves, come back for the $49 Skill Pack.*

**Secondary** (at page bottom, low-key): *Enterprise AI deal stalled in procurement? [[PHAROS Procurement-Unblock Sprint]] →*

## Voice rules (operator-facing, not on the page)

- Avoid "revolutionary", "autonomous intelligence", "infinite memory", "AI-powered orchestration".
- Avoid claiming vector search, automatic compression, or database-backed retrieval. The framework does none of those things.
- Prefer concrete verbs: "your agent stops collapsing into one voice", "the validator fails loud when a contract drifts", "ten markdown files, one shell script".
- Subtract before adding. The strongest line is *"no SDK, no daemon, no new infrastructure."*
- Reference the validator by line count (216 lines) — specific numbers are harder to dismiss than adjectives.

## Three-act demo script (video, ≤3 minutes)

**Act 1 — Problem (30s):** Show a single-agent Claude Code session collapsing under a multi-step feature request. Voice-over: "Your agent doesn't know which role it's playing. So neither do you."

**Act 2 — Mechanism (90s):** Show the ten agent files. Walk through the Prime Coordinator's pairing protocol. Show `validate-combinations.sh` running clean. Show a triangulated verdict ledger.

**Act 3 — Proof (60s):** Re-run the feature request with the framework loaded. Show the explicit handoffs. Show the gate-pass evidence. Close on the GitHub URL.

## Posting sequence (4 posts, spaced over the launch week)

1. **Problem hook** — "Most agent frameworks ship a runtime. We ship ten markdown files and a shell script." → link to repo.
2. **Mechanism** — The validator script as the credibility artifact. Quote 5 lines of awk. → link to repo.
3. **Combinatorics** — "Ten agents. Forty-five duals. One hundred and twenty triples. The framework knows the difference, and so will your agent." → link to lead-magnet PDF.
4. **Ladder offer** — "Free framework. $49 Skill Pack for the installable Claude Code bundle. Live now on Gumroad." → link to Gumroad.

Hold the social-proof post until a real buyer quote exists.

---

## Related

- [[Elemental Agents Framework — Multi-Agent Role and Validation Architecture (2026-05-12)]]
- [[Obsidian Agent Vault Launch — Commercial Skill]] — voice rules for sales copy
- [[Obsidian Agent Vault — Launch Kit]] — twin product, same upsell
- [[PHAROS Procurement-Unblock Sprint]] — terminal upsell
