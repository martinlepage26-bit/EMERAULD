---
type: wiki
title: Elemental Agents — Productization Plan (2026-05-24)
aliases:
- Elemental Agents Launch
- Elemental Agents Commercial Plan
- Elemental Agents Productization
- wiki/Elemental Agents — Productization Plan (2026-05-24)
tags:
- product
- commercialization
- multi-agent
- claude-code
- framework
- launch
- audience-strategy
- wiki
- elemental-agents-productization-plan-2026-05-24-md
- elemental
- agents
- upsell
- assets
- color-orange
status: active
created: '2026-05-24'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Elemental Agents — Productization Plan (2026-05-24).md
backlink_count: 10
backlinks:
- '[[Areas/PHAROS/App Ideas — Hybrid Gaming Entertainment Social Fitness Music (2026)]]'
- '[[wiki/Charge & Circle — Four-Pivot Decision Map (2026-05-24)]]'
- '[[wiki/Charge & Circle — TTRPG Launch (2026)]]'
- '[[Areas/PHAROS/PHAROS Commercial Strategy]]'
- '[[wiki/PHAROS Stuck Deal Diagnostic — Minimum Viable Offer (2026-05-26)]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[archive/session-state/session-state-002]]'
- '[[assets/elemental-agents/ttrpg-repack/BRAND-DECISION]]'
- '[[session-state]]'
---

# Elemental Agents — Productization Plan (2026-05-24)

## Summary

A commercial launch plan for the Elemental Agents framework documented in [[Elemental Agents Framework — Multi-Agent Role and Validation Architecture (2026-05-12)]]. Ships as a free MIT GitHub repo plus a $49 Gumroad Skill Pack plus an email-gated lead-magnet PDF, all driving to the [[PHAROS Procurement-Unblock Sprint]] upsell. The launch ladders cleanly with [[Obsidian Agent Vault — Launch Kit]] — same buyer persona, adjacent half of the same problem (role layer vs memory layer). Companion audience-expansion analysis identifies four additional buyer segments worth pursuing in sequence. Part of [[Personal and Projects MOC]].

## Context

The framework was captured in `raw/D-drive-scan-2026-05-12/elemental-agents/` and is Martin's IP (distinct from the Vulcain framework). Reading the full snapshot identified four missing source files that the framework's own structure-check requires: `agents/05-quality-auditor.md`, `examples/03-bug-triage-and-fix.md`, `examples/05-post-incident-retrospective.md`, and `validation/02-operational-content-check.md`. All four are drafted in `assets/elemental-agents/source-completions/` and must be reconciled with the D: drive before the public GitHub repo ships. The validation file is the most structurally important — without it, `03-triangulated-verification.md` references a nonexistent dependency and the framework fails its own gate.

The launch plan inherits voice and pricing-ladder discipline from [[Obsidian Agent Vault Launch — Commercial Skill]] (v2 canonical). The competitive positioning, three-act demo script structure, and language rules carry over directly.

## Productization assets

All assets live in `assets/elemental-agents/`:

- [[../assets/elemental-agents/positioning-memo.md|positioning-memo.md]] — operator-facing memo: wedge, two-door ladder with the vault, pricing ladder ($0 / $49 / lead-magnet / Sprint upsell), positioning fork (lean-into vs hide-the mythopoetic), 14-day launch checklist
- [[../assets/elemental-agents/sales-page-outline.md|sales-page-outline.md]] — Gumroad-shaped sales page: headline drafts, mechanism, proof table vs AutoGen/CrewAI/LangGraph, pricing, buyer fit, anti-fit, FAQ, three-act demo script, four-post launch sequence
- [[../assets/elemental-agents/audience-expansion.md|audience-expansion.md]] — five-bet expansion analysis identifying methodology buyers ($79–$149), TTRPG/magic-system creators ($19–$149), compliance and controls professionals ($299–$499 + Sprint upsell), enterprise AI platform teams ($5k–$25k), and educators ($0–$500), with recommended four-phase sequencing
- `source-completions/` — drafts for the four missing framework files in the framework's spare declarative voice, ready for reconciliation with the live source on D: drive

## Launch ladder (Phase 1 — AI agent operator door)

| Tier | Price | Purpose |
|---|---|---|
| GitHub repo (MIT) | Free | Lead; full framework markdown + validator + install hooks + examples |
| Skill Pack (Gumroad) | $49 | Installable Claude Code skill bundle, branded PDF reference card, 2 worked transcripts |
| Lead-magnet PDF | $0 (email-gated) | "10 Agents, 165 Combinations — the role layer for file-aware AI agents" |
| PHAROS Sprint (upsell) | $35k–$125k | [[PHAROS Procurement-Unblock Sprint]] — warm-intro only |

## Two-door ladder with the Obsidian Agent Vault

The vault product sells the memory layer; Elemental Agents sells the role layer. Both ladder to the same Sprint upsell. The expansion analysis recommends growing this two-door picture into a five-door portfolio once Bets 1–3 ship: the same framework retails simultaneously at $19, $49, $79, $149, $299, $499, $5,000, and $25,000+ across non-overlapping audiences. This is the *one product, many doors* pattern that [[Obsidian Agent Vault — Launch Kit]] already validated at smaller scale.

## Structure-check gap — resolution

Before the public repo ships, the four drafted source-completion files must be:

1. Compared against any existing versions on Martin's D: drive
2. Reconciled — if D: has its own Quality Auditor that conflicts, prefer the canonical one and update the snapshot
3. Merged back to `/mnt/d/elemental-agents/` and to the EMERAULD snapshot at `raw/D-drive-scan-2026-05-12/elemental-agents/` if Martin wants the snapshot to reflect ground truth as of the publish date
4. Validated by running `combinations/validate-combinations.sh` and the commands in `validation/01-structure-check.md`; all four count-checks must pass (10 agents, 6 orchestration, 6 examples, 3 validation files)

## Positioning fork

The framework's element/Wuxing/esoteric vocabulary is its strongest differentiator and its biggest segmentation risk. Decision required between:

- **Option A — Lean in.** Lead with the mythopoetic frame. Buyer audience: technical operators who appreciate symbolic depth.
- **Option B — Hide it.** Reframe agents in plain titles, surface element vocabulary only inside the validator. Buyer audience: enterprise platform teams, classical software shops.

Memo recommendation is Option A for the AI operator door; the audience-expansion analysis then routes Option B audiences through Bets 3 and 4 (compliance and enterprise platform), where plain-vocabulary versions of the framework are the right answer. So the fork dissolves — both options ship, addressed to different segments under different storefronts.

## Risks and dependencies

- Structure-check gap (mitigated by the drafts in `source-completions/`)
- Example thinness — four existing example files are skeletal (~25 lines); plan one fully-narrated end-to-end transcript as a one-week post-launch task
- Combination boilerplate — 19 of 45 duals use the generic best-use-case default; tolerable for v1.0 with changelog promise of content depth in v1.1
- License clarity — MIT for framework markdown; decide before publishing whether validator script is also MIT or reserved-commercial
- Brand split — if TTRPG bet ships, the same artifact retails at $19 (hobbyists) and $35k (Sprint). Use distinct storefront brands for the hobbyist line

## Insights

- The validator script (`validate-combinations.sh`, 216 lines of awk) is the credibility artifact, not the agent contracts. Sales copy should foreground it.
- The element composition system is structurally identical to a hard-magic-system spec. This was likely not intentional; it is now a sellable accident.
- The framework's voice (spare, declarative, six-block contracts) is unusually consistent. This makes the missing-file drafting straightforward and the framework feel finished even at v1.0.
- The PHAROS Procurement-Unblock Sprint upsell becomes more credible with both the vault product and Elemental Agents in market — the operator no longer pitches "I have one offer" but "I have three feeder channels into one offer."
- The audience-expansion analysis is the load-bearing strategic insight. The narrow positioning would have left the methodology-buyer and TTRPG segments untouched; both are larger than the agent-operator audience and tolerate the same or higher price points.

## Open questions

- Confirm Option A positioning for the Phase 1 launch.
- Confirm appetite for the second storefront (Bet 1 — methodology buyers) shipping in the same week as the AI operator launch.
- Confirm whether to invest 3–4 weeks repackaging the framework for Bet 3 (compliance) before Phase 1 sales feedback comes in, or wait for that signal.
- Confirm license split: MIT framework + MIT validator, or MIT framework + reserved-commercial validator?
- Confirm whether the snapshot in `raw/` should be updated to include the drafted source completions, or kept as a frozen 2026-05-12 capture.

## Sources

- `raw/D-drive-scan-2026-05-12/elemental-agents/` — verified framework snapshot
- [[../assets/elemental-agents/positioning-memo.md|assets/elemental-agents/positioning-memo.md]]
- [[../assets/elemental-agents/sales-page-outline.md|assets/elemental-agents/sales-page-outline.md]]
- [[../assets/elemental-agents/audience-expansion.md|assets/elemental-agents/audience-expansion.md]]
- `assets/elemental-agents/source-completions/`

## Related

- [[Elemental Agents Framework — Multi-Agent Role and Validation Architecture (2026-05-12)]] — framework reference note
- [[Obsidian Agent Vault — Launch Kit]] — twin product, same upsell
- [[Obsidian Agent Vault Launch — Commercial Skill]] — voice rules carry over to Elemental Agents
- [[Obsidian Agent Vault — Asset Canon]] — model for tracking productized assets
- [[PHAROS Procurement-Unblock Sprint]] — terminal upsell
- [[Trust Advantage Analysis — Sales and AI Governance]] — trust differential that makes the upsell viable
- [[Governed Revision Loop — Responsible Self-Improving Agents]] — thought-leadership tailwind seed post
- [[Personal and Projects MOC]] — vault hub
