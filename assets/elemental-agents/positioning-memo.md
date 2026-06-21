---
type: memo
status: draft
created: 2026-05-24
audience: operator
---

# Elemental Agents — Positioning Memo

## One-line offer

A file-native multi-agent execution framework for Claude Code, Cursor, and other file-aware agents: ten role contracts, six orchestration phases, and a self-validating combination matrix that polices its own structure on every commit.

## The wedge

Most agent frameworks ship a runtime (LangGraph, AutoGen, CrewAI) and ask the buyer to learn an SDK. Elemental Agents ships a **set of markdown contracts and a shell validator**. It runs anywhere the buyer's agent already runs. Zero SDK, zero daemon, zero new infrastructure.

The honest promise: structure your agent workflows so the agent has explicit roles, explicit handoffs, and explicit validation gates — and so the structure itself fails loud when it drifts.

## Audience scope — see also the expansion analysis

This memo's launch ladder targets the narrowest, fastest buyer segment (Claude Code / Cursor agent operators). For the wider audience picture — productized-methodology buyers, TTRPG/magic-system creators, compliance and controls professionals, enterprise AI platform teams, and educators — see `audience-expansion.md` in this folder. The recommended sequencing ships the AI-operator launch first, then adds methodology buyers in the same week with a parallel storefront.

## Two-door ladder with Obsidian Agent Vault

The vault product (already shipped, see [[Obsidian Agent Vault — Launch Kit]]) sells the **memory layer** for file-aware agents. Elemental Agents sells the **role layer**. Same buyer persona, different cut of the same problem.

| Door | What it sells | Price | Anchors |
|---|---|---|---|
| Obsidian Agent Vault | Memory layer (CLAUDE.md, hub notes, raw→wiki pipeline) | $49 / $299 / $2,500 | Already shipped |
| Elemental Agents | Role layer (10 agents, 6 orchestration phases, validator) | $0 / $49 / lead-magnet PDF | This memo |

Both doors lead to the same upsell: [[PHAROS Procurement-Unblock Sprint]] ($35k–$125k). The vault buyer who wants the role discipline can stack on Elemental Agents; the Elemental Agents buyer who wants the memory layer can stack on the vault. Cross-selling is automatic because the two products solve adjacent halves of the same buyer problem.

## Mechanism — what makes it credible

1. **`validate-combinations.sh`** is 216 lines of awk-based enforcement: count integrity, unique permutations, required-field presence, no token stutter, escalation-lead rule. It is the rare agent framework that polices its own invariants. **Demo this script in the sales video.**
2. **Triangulated validation** — every agent contract specifies three independent angles. This is a real epistemic claim, not decoration.
3. **The element system is intellectually serious** — three element traditions (classical, Wuxing, esoteric) composed under explicit manifestation rules. This gives the framework a defensible philosophical spine that competitors lack.
4. **It's already in use** — the framework exists on Martin's D: drive and is captured at `raw/D-drive-scan-2026-05-12/elemental-agents/`. The product is not vaporware.

## Pricing ladder

| Tier | Price | Scope | Status |
|---|---|---|---|
| Free GitHub repo | $0 | Full framework, MIT-licensed, public | To ship |
| Skill Pack (Gumroad) | $49 | Claude Code skill bundle, install script, example transcripts, branded PDF reference card | To ship |
| Lead-magnet PDF | $0 (email-gated) | "10 Agents, 165 Combinations — the role layer for file-aware AI agents" | To ship |
| PHAROS Procurement-Unblock Sprint (upsell) | $35k–$125k | Existing offer; Elemental Agents becomes a credibility artifact attached to the warm-intro pitch | Already exists |

The $49 tier is not the revenue play. It is the qualification filter: anyone who buys at $49 has self-identified as a serious agent operator and becomes a viable target for the Sprint pitch.

## Positioning fork — answer before shipping

The framework's element/Wuxing/esoteric vocabulary is its strongest differentiator and its biggest risk. Decision required:

**Option A — Lean in.** Lead with the mythopoetic frame. Buyer audience: technical operators who appreciate symbolic depth (Obsidian/PKM crowd, post-Zettelkasten productivity space, philosophical Claude Code users). Sales line: *"Engineers stopped naming abstractions a long time ago. We didn't. Here's why naming matters when you're orchestrating ten autonomous roles."*

**Option B — Hide it.** Reframe agents in plain titles (Coordinator, Architect, Engineer, etc.) and treat the element layer as an internal indexing system surfaced only inside the validator. Buyer audience: enterprise platform teams, classical software shops. Sales line: *"A markdown contract per role. A shell script that enforces the invariants. Drop it next to your agent runtime."*

**Recommendation:** Ship Option A. The mythopoetic layer is the framework's moat — every me-too AutoGen wrapper looks the same; nothing looks like Elemental Agents. The buyers who reject the framing on aesthetic grounds were never the target market. The buyers who accept it will pay $49 instantly and become Sprint candidates.

The vault product (which is technical-neutral) covers the Option B buyer if needed. Don't dilute Elemental Agents to chase that audience twice.

## Risks and dependencies

1. **Structure-check gap** — closed today by drafted source completions in `source-completions/`. Before publishing the GitHub repo, Martin must (a) reconcile the drafted Quality Auditor with whatever exists on D: drive; (b) merge the new examples (03, 05) and validation file (02) back to the source; (c) re-run `validate-combinations.sh` and `01-structure-check.md` to confirm all gates pass.
2. **Example thinness** — the four existing examples are ~25 lines each. The new 03 and 05 match that voice. A buyer evaluating against AutoGen will want at least one **fully narrated end-to-end transcript**. Add this as a one-week post-launch task; do not block initial publish.
3. **Combination boilerplate** — 19 of 45 duals use the generic best-use-case default. Acceptable for $49 launch; surface as "v1.0 — content depth increases in v1.1" in the changelog.
4. **License clarity** — MIT for the framework markdown, but the validator script and install hooks may need a separate notice if Martin wants to reserve commercial use of the validator for the paid Skill Pack tier. Decide before publishing the repo.
5. **No backlinks from Hermes Dashboard** — the live business-state dashboard does not yet reference Elemental Agents as a revenue line. Add when GitHub repo is live.

## 14-day launch checklist

| Day | Action |
|---|---|
| 1 | Reconcile source-completions with D: drive; resolve any conflicts |
| 1 | Run validate-combinations.sh and structure-check; confirm all gates pass |
| 2 | Decide positioning fork (Option A recommended) |
| 3 | Create public GitHub repo, push framework, add MIT LICENSE |
| 4 | Record 3-minute demo: route a feature request through 10 agents, run validator, show triangulated verdict |
| 5–7 | Write lead-magnet PDF (8–12 pages, mythopoetic frame) |
| 8 | Build Gumroad listing for $49 Skill Pack tier |
| 9 | Package Claude Code skill bundle (install script, agent files, validator, examples) |
| 10 | Write three launch posts: problem hook, mechanism, ladder offer |
| 11 | Soft-launch to warm list (same channel as Sprint) |
| 12 | Add Sprint upsell CTA to GitHub README and Gumroad page |
| 13 | Update [[Hermes Dashboard — Professional Governance Tool]] with new revenue line |
| 14 | Public launch posts |

## Cross-product relationships

- `audience-expansion.md` — five-segment expansion analysis; ship this memo's launch first, then add bets 1–3 in sequence
- [[Obsidian Agent Vault — Launch Kit]] — memory-layer twin product
- [[Obsidian Agent Vault Launch — Commercial Skill]] — voice rules for the sales page apply identically here
- [[Obsidian Agent Vault — Asset Canon]] — model for tracking productized assets
- [[PHAROS Procurement-Unblock Sprint]] — terminal upsell for both doors
- [[Trust Advantage Analysis — Sales and AI Governance]] — trust differential that makes the upsell viable
- [[Governed Revision Loop — Responsible Self-Improving Agents]] — thought-leadership tailwind seed post

## Open questions for operator review

- Confirm Option A vs Option B positioning.
- Confirm license split: MIT for framework, separate for validator?
- Confirm whether to wait for content-depth pass before publishing, or ship at v1.0 with changelog promise.
- Confirm Sprint upsell wording on the Gumroad page — soft mention or explicit CTA?
