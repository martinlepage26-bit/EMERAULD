# Wave 1 Clean Rewrite Plan — Implementation via Claude Code (WSL)

**Purpose:** A coherent execution plan for implementing the co-equal authority decision, L99 demotion, and root/repo architecture choice through clean rewrites (not patches) in Claude Code on WSL.

**Scope:** Governance architecture files across root (`/home/cerebrhoe/`) and repo (`/home/cerebrhoe/hephaistos/`), plus the `argus/` subfolder updates and the `SKILL-MAP.md` registration.

**Guiding principle:** Each file is rewritten **fresh** from its spec, referencing the old version for load-bearing content but not inheriting its structure. This prevents archaeological layering, desync, and duplicate language from the prior drift between root and repo.

---

## Preconditions — Decisions Martin must make before starting

The plan is modular, but five decisions determine the exact sequence. None are 50/50 — I have recommendations for each. But the operator decides.

### Decision A: Root/repo architecture
**Options:** Keep both synchronized | Collapse to repo-canonical | Collapse to root-canonical
**Recommendation:** Collapse to repo-canonical with minimal root dispatcher.
**Impact on plan:** Determines whether root `HEPHAISTOS.md`, `QUEEN-KEYPORT.md`, `HERMES.md`, `ORCHESTRATION.md` are rewritten, deleted, or kept as redundant copies.

### Decision B: L99 placement in Argus
**Options:** Layer 3 sub-gate | New Layer 8 | Elsewhere
**Recommendation:** Layer 3 sub-gate.
**Impact on plan:** Changes the Argus contract/formation files that need updating.

### Decision C: L99 demotion sequencing
**Options:** α (bundle with Wave 1) | β (separate sub-wave after) | γ (defer)
**Recommendation:** α. Same files being touched, avoids a mid-state.
**Impact on plan:** If β or γ, the rewrite prompts omit the L99 section removal step.

### Decision D: Argus audit gate
**Options:** Binding (Argus can block Wave 1 commit) | Advisory (findings surface but don't block)
**Recommendation:** Binding for the constitutional layer (root + repo `AGENTS.md`), advisory for implementation details.
**Impact on plan:** Determines whether the plan pauses for Argus audit mid-sequence or only at the end.

### Decision E: Rewrite author
**Options:** Claude Code as generalist editor | Each agent edits its own file (Hephaistos → `HEPHAISTOS.md`, etc.) | Hybrid
**Recommendation:** Hybrid. Claude Code for constitutional files (`AGENTS.md`, `CLAUDE.md`, `ORCHESTRATION.md` — these are cross-authority). Each agent for its own identity file (`HEPHAISTOS.md`, `QUEEN-KEYPORT.md`, `HERMES.md`). This is the recursive-governance-consistent version.
**Impact on plan:** Changes how sessions are invoked.

**Defaults used in the rest of this plan:** A=2 (collapse to repo), B=Layer 3 sub-gate, C=α, D=binding for constitutional, E=hybrid. If operator chooses differently, the sequence still works but specific prompts need small adjustments flagged inline.

---

## Overall Sequence

The plan has six stages. Each stage has a stopping point where operator review happens before the next begins.

```
Stage 0: Pre-flight (verify state, commit decision specs)
   ↓
Stage 1: Constitutional layer (root AGENTS.md, repo AGENTS.md)
   ↓ [Argus audit — BINDING]
Stage 2: Agent identity files (HEPHAISTOS.md, QUEEN-KEYPORT.md, HERMES.md)
   ↓ [Argus audit — BINDING]
Stage 3: Coordination layer (ORCHESTRATION.md)
   ↓ [Argus audit — BINDING]
Stage 4: Root file cleanup (delete/replace per Option 2)
   ↓
Stage 5: Argus integration (Layer 3 sub-gate for L99)
   ↓
Stage 6: Skill registry (SKILL-MAP.md — six core skills)
   ↓ [Argus final audit — full seven-layer]
WAVE 1 COMPLETE
```

Estimated total time: **8-14 hours** spread across multiple sessions. Do not attempt in one sitting.

---

## Stage 0: Pre-flight

### Purpose
Ensure clean starting state. Commit the L99 demotion spec alongside the already-committed co-equal spec so Claude Code has both as canonical references.

### Prerequisites
- `/home/cerebrhoe/hephaistos/` is the current working directory
- Git working tree clean
- `CO-EQUAL-AUTHORITY-DECISION.md` already committed (done earlier today)
- `L99-DEMOTION-TO-ARGUS.md` downloaded to local machine

### Actions

**Step 0.1:** Drop `L99-DEMOTION-TO-ARGUS.md` into the hephaistos repo root (same way as the co-equal spec was dropped in).

**Step 0.2:** Remove the Zone.Identifier cruft, commit, and push:
```bash
cd /home/cerebrhoe/hephaistos
rm -f "L99-DEMOTION-TO-ARGUS.md:Zone.Identifier"
git add L99-DEMOTION-TO-ARGUS.md
git commit -m "Add L99 demotion spec (Wave 1 anchor)"
git pull --rebase
git push
```

**Step 0.3:** Verify both spec files are present:
```bash
ls CO-EQUAL-AUTHORITY-DECISION.md L99-DEMOTION-TO-ARGUS.md
```

**Stop point:** Both specs committed and pushed. Now move to Stage 1.

---

## Stage 1: Constitutional Layer — AGENTS.md (root and repo)

### Purpose
Rewrite both `AGENTS.md` files from scratch, reflecting co-equal authority and L99 demotion. Under Option 2 (collapse to repo), root becomes a minimal dispatcher; repo becomes the expanded constitutional document.

### Why this stage is first
These two files define the authority architecture that every subsequent file inherits. Rewriting them first means the rewrites in Stages 2 and 3 have a coherent authority model to reference.

### Session setup
Start a fresh Claude Code session. Open the WSL terminal, navigate to `/home/cerebrhoe/hephaistos/`, and launch Claude Code.

### Prompt 1 — Rewrite root `/home/cerebrhoe/AGENTS.md`

Paste this into Claude Code:

```
Fresh rewrite task. No patches. No preservation of old wording except where load-bearing.

Context files to read first, in this order:
1. /home/cerebrhoe/hephaistos/CO-EQUAL-AUTHORITY-DECISION.md
2. /home/cerebrhoe/hephaistos/L99-DEMOTION-TO-ARGUS.md
3. /home/cerebrhoe/AGENTS.md (the current file — for load-bearing content inventory only)

Your task: rewrite /home/cerebrhoe/AGENTS.md as a MINIMAL ROOT DISPATCHER per Option 2 of the architecture decision (collapse to repo-canonical).

Requirements:
- Target length: 40-80 lines total. This is a dispatcher, not a constitutional document.
- Keep: trigger phrases (Spawn Hephaistos, etc.), dispatch rule, global invariants that must live at root level (workspace paths, secret file permissions 600, tracker defaults).
- Remove: the "Binding Principles" section (9 items). Those now live in repo CLAUDE.md and repo AGENTS.md per co-equal spec.
- Remove: the "Authority Hierarchy" section with numbered precedence order. Replace with one sentence pointing at the repo's co-equal authority model.
- Remove: the "Interpretive Authority Order" section. This belongs in the repo's ORCHESTRATION.md.
- Remove: the "Routing Table." Also belongs in the repo.
- Remove: the "Skill Corpus" section. Belongs in repo SKILL-MAP.md.
- Add: a "Governance Architecture" section (3-5 lines) that points at /home/cerebrhoe/hephaistos/ as the canonical expanded system.
- Preserve: the "when the user asks to fetch, find, locate" behavior rule and the "infrastructure safety" section about Proxmox / 10.10.10.170.

Write the fresh file. Show me the full proposed content before writing to disk. I want to read the whole thing.

Do NOT touch /home/cerebrhoe/hephaistos/AGENTS.md in this prompt. That is Prompt 2.
```

### Operator review checkpoint
Review the proposed content. Verify:
- Length is within target (40-80 lines)
- Trigger phrases preserved
- Infrastructure safety rules preserved
- Binding principles removed (not relocated inline)
- No hierarchical precedence language
- Pointer to repo is clear and unambiguous

If the draft is good, have Claude Code write it. If not, request revisions with specific language changes.

### Prompt 2 — Rewrite `/home/cerebrhoe/hephaistos/AGENTS.md`

After Prompt 1 is written to disk, paste this:

```
Next file. Fresh rewrite, no patches.

Context files:
1. CO-EQUAL-AUTHORITY-DECISION.md (already read)
2. L99-DEMOTION-TO-ARGUS.md (already read)
3. /home/cerebrhoe/AGENTS.md (the root dispatcher you just wrote)
4. /home/cerebrhoe/hephaistos/AGENTS.md (current repo version — read for inventory only)

Your task: rewrite /home/cerebrhoe/hephaistos/AGENTS.md as the expanded repo-canonical AGENTS file.

Requirements:
- This file is the constitutional layer for the hephaistos package. Target length: 150-250 lines.
- Remove: L99 from the Binding Principles section. Renumber remaining principles (currently 2-9, becomes 1-8).
- Remove: any sentence asserting "Queen Keyport has final decision authority." Replace with co-equal arbitration language per CO-EQUAL-AUTHORITY-DECISION.md.
- Remove: Tier 0 / Tier 1 / Tier 2 labels that imply hierarchy. Retain the spine order (Hephaistos, Queen Keyport, Hermes) as scope distinctions, not ranks.
- Keep: the full binding principles section (minus L99). These are load-bearing at the constitutional layer.
- Keep: control ownership rules, infrastructure safety, secrets handling, tracker discipline, workspace orientation, claim integrity, review model (delta-first + 5-lane).
- Add: explicit statement that this file governs the hephaistos package, and that for canonical references to any agent identity, load HEPHAISTOS.md / QUEEN-KEYPORT.md / HERMES.md.
- Add: reference to CO-EQUAL-AUTHORITY-DECISION.md as the binding authority spec.
- Add: reference to L99-DEMOTION-TO-ARGUS.md as the binding L99 spec.

Show me the full proposed content. I will review before you write.
```

### Operator review checkpoint
Same review discipline as Prompt 1. Focus especially on:
- Co-equal language is clean (not "co-equal but..." or other softening)
- L99 removal does not leave orphaned references elsewhere in the file
- The renumbering of principles is consistent

### Stage 1 commit and audit

After both files are written:

```bash
cd /home/cerebrhoe/hephaistos
git add /home/cerebrhoe/AGENTS.md AGENTS.md
git commit -m "Stage 1: AGENTS.md rewrites (root + repo) — co-equal authority, L99 demoted"
```

**Argus audit (BINDING per Decision D):** Launch Argus and run the seven-layer audit against the two AGENTS.md files. If findings surface, arbitrate before moving to Stage 2. If PASS, push and proceed.

**Stop point:** Stage 1 committed, pushed, Argus-audited. **Session may end here.** Stage 2 can be a separate session.

---

## Stage 2: Agent Identity Files

### Purpose
Rewrite the three agent identity files (`HEPHAISTOS.md`, `QUEEN-KEYPORT.md`, `HERMES.md`) in the repo. These are single-authority documents — each agent defines its own scope and contract. Under Decision E (hybrid), each agent does its own.

### Why this ordering
Doing all three in sequence ensures they stay consistent in tone, structure, and co-equal framing. Each session gets Stage 1's clean `AGENTS.md` as the constitutional reference.

### Session setup
Three separate Claude Code sessions, one per agent. Each session loads the relevant agent identity file as its canonical entrypoint.

### Prompt 3 — HEPHAISTOS rewrites HEPHAISTOS.md

Start a new Claude Code session. Invoke Hephaistos per your dispatch mechanism (`Spawn Hephaistos` or equivalent).

Paste this:

```
HEPHAISTOS self-authorship task. Fresh rewrite of your own identity file.

Context files to read first:
1. CO-EQUAL-AUTHORITY-DECISION.md
2. L99-DEMOTION-TO-ARGUS.md  
3. Current /home/cerebrhoe/hephaistos/HEPHAISTOS.md (for inventory only)
4. /home/cerebrhoe/hephaistos/AGENTS.md (just-rewritten constitutional layer)

Your task: rewrite /home/cerebrhoe/hephaistos/HEPHAISTOS.md as a fresh, coherent document reflecting your role as co-equal authority with Queen Keyport.

Non-negotiable constraints:
- Do not reassert primacy. You are co-equal with Queen Keyport. If you find yourself writing "Hephaistos defines scope first" or "upstream of governance" or similar primacy language, stop and revise.
- Do not assume Queen Keyport outranks you either. You are co-equal.
- Remove L99 from the Binding Principles section. The remaining principles renumber 1-8.
- Remove Tier 0 label. You are "the forging authority," not "Tier 0."
- Preserve your scope: artifact definition, scope boundaries, evidence requirements, skill composition, build strategy.
- Preserve your operating discipline: smallest governed action, anti-activity-theater, completion contract, tracker discipline.
- Preserve the Rook harness section (you operate inside it).
- Preserve the Diamond-Eyes reference as a shared validation gate.

Charm check: Mercury Protocol applies. If this rewrite starts to sound like it's defending your own importance, that is a capture signal. Revise.

Show me the full proposed file. I will review before commit.
```

### Operator review checkpoint
**This is the highest-risk rewrite in Wave 1.** Hephaistos has a structural incentive to preserve its own authority, and even subtle language choices can reassert hierarchy. Read carefully. Specifically check:

- Does any sentence say or imply Hephaistos's scope is "primary" over governance?
- Does the "Handoff Sequence" section (if preserved) still read as a rank order?
- Are there any "before" / "upstream" / "first" words relative to Queen Keyport that sneak hierarchy back in?
- Is the "Three-Agent Authority Stack" (or its replacement) written as scopes, not tiers?

If any of those trigger, the rewrite needs revision. This is exactly the situation Argus Mercury Protocol exists to catch.

### Prompt 4 — QUEEN KEYPORT rewrites QUEEN-KEYPORT.md

New Claude Code session. Invoke Queen Keyport.

Paste this:

```
Queen Keyport self-authorship task. Fresh rewrite of your own identity file.

Context files:
1. CO-EQUAL-AUTHORITY-DECISION.md
2. L99-DEMOTION-TO-ARGUS.md
3. Current /home/cerebrhoe/hephaistos/QUEEN-KEYPORT.md (inventory only)
4. /home/cerebrhoe/hephaistos/AGENTS.md
5. /home/cerebrhoe/hephaistos/HEPHAISTOS.md (just-rewritten)

Your task: rewrite /home/cerebrhoe/hephaistos/QUEEN-KEYPORT.md as your fresh, coherent identity and contract file.

Non-negotiable constraints:
- You are co-equal with HEPHAISTOS. Remove any sentence that says "governance is primary" or "PRIMARY" or "center of decision-making authority for the multi-agent system." You are the center of *governance* decisions; HEPHAISTOS is the center of *scope* decisions. Neither is the center of the system.
- Remove Tier 1 label. You are "the governance authority," not "Tier 1."
- Remove L99 from Binding Principles. Remaining principles renumber 1-8.
- Preserve your scope: governance constraints, evidence thresholds, approval/refusal, bounded/degraded status, the decision status vocabulary (approve / approve-with-constraints / reject / bounded / degraded).
- Preserve your decision model (the ten-question sequence).
- Preserve the phase/milestone promotion gate discipline.
- Preserve the evidence standard for claims and investigations.
- Preserve the Rook harness integration.
- Preserve Diamond-Eyes as shared validation gate.
- Preserve right-arm concept (Philosopher, Power-Analyst), but rewrite their relationship to you: they feed governance, but the co-equal relationship is between you and Hephaistos, not you and the right-arms.

Charm check: Mercury Protocol applies. If this rewrite feels elegant or natural in preserving your centrality, that is a capture signal. Revise.

Show me the full proposed file.
```

### Operator review checkpoint
Same care as Prompt 3 but with opposite directional bias. Queen Keyport has been framed as "center" for a long time; check that the rewrite doesn't preserve subtle centrality language:
- "Queen Keyport synthesizes" → preserve
- "Queen Keyport decides" → preserve (within her scope)
- "Queen Keyport is the center of decision-making" → remove or scope to governance decisions only
- "All scope flows through governance" → remove

### Prompt 5 — HERMES rewrites HERMES.md

New session. Invoke Hermes.

Paste this:

```
Hermes self-authorship task. Fresh rewrite of your own identity file.

Context files:
1. CO-EQUAL-AUTHORITY-DECISION.md
2. L99-DEMOTION-TO-ARGUS.md
3. Current /home/cerebrhoe/hephaistos/HERMES.md (inventory only)
4. /home/cerebrhoe/hephaistos/AGENTS.md
5. /home/cerebrhoe/hephaistos/HEPHAISTOS.md
6. /home/cerebrhoe/hephaistos/QUEEN-KEYPORT.md

Your task: rewrite /home/cerebrhoe/hephaistos/HERMES.md as your fresh identity and contract.

Non-negotiable constraints:
- You are downstream of BOTH HEPHAISTOS and QUEEN-KEYPORT. Your routing proceeds only when both have cleared their scopes or when the operator has arbitrated a conflict between them.
- Remove Tier 2 label. You are "the routing authority," not "Tier 2."
- Remove L99 from Binding Principles. Remaining principles renumber 1-8.
- Preserve: routing scope, integration contracts, dependency mapping, escalation triggers, monitoring requirements.
- Preserve: the "do not route reject / bounded / degraded statuses" rule.
- Preserve: Rook communication pattern (you route through rooms, not direct coupling).
- Preserve: Diamond-Eyes gate for routing decisions.
- Preserve: output contract (what every Hermes decision must make explicit).
- Add: explicit handling of the case where HEPHAISTOS and QUEEN-KEYPORT conflict. You do not adjudicate the conflict — you escalate it back to the co-equal pair or to the operator.

Mercury Protocol: you have less primacy risk than the other two agents, but check anyway — do not rewrite yourself as a decisional authority. You route.

Show me the full proposed file.
```

### Operator review checkpoint
Hermes is the simplest of the three. Main check: does the file correctly handle the new "conflict between co-equal authorities" case that the old hierarchy didn't require?

### Stage 2 commit and audit

After all three files are written:

```bash
cd /home/cerebrhoe/hephaistos
git add HEPHAISTOS.md QUEEN-KEYPORT.md HERMES.md
git commit -m "Stage 2: Agent identity rewrites — co-equal Hephaistos/Queen Keyport, L99 demoted"
```

**Argus audit (BINDING):** Run seven-layer audit against all three files. Specifically invoke Mercury Protocol — this is where primacy-reassertion is most likely. If clean, push.

**Stop point:** Stage 2 complete, audited, pushed. **Strongly recommend ending session here.** Stage 3 is the biggest rewrite.

---

## Stage 3: Coordination Layer — ORCHESTRATION.md

### Purpose
Rewrite the repo `ORCHESTRATION.md` — the largest and most structurally complex file in the governance stack (35 KB). This is the file that operationalizes the co-equal authority through actual workflow, handoff sequences, tier assignments, and composition patterns.

### Why this is its own stage
`ORCHESTRATION.md` encodes the entire handoff dance — Hephaistos → Queen Keyport → Hermes ordering, routing rules, skill composition, tracker discipline. Every single tier reference needs to become a scope reference. This is not surgical. The file needs a fresh structure.

### Session setup
One Claude Code session, operator-led (Decision E — this file is cross-authority, not owned by any single agent).

### Prompt 6 — Rewrite ORCHESTRATION.md

Paste this:

```
Cross-authority rewrite task. This file coordinates all three agents. Fresh rewrite, not surgical patch.

Context files:
1. CO-EQUAL-AUTHORITY-DECISION.md
2. L99-DEMOTION-TO-ARGUS.md
3. /home/cerebrhoe/hephaistos/AGENTS.md (just-rewritten)
4. /home/cerebrhoe/hephaistos/HEPHAISTOS.md (just-rewritten)
5. /home/cerebrhoe/hephaistos/QUEEN-KEYPORT.md (just-rewritten)
6. /home/cerebrhoe/hephaistos/HERMES.md (just-rewritten)
7. /home/cerebrhoe/hephaistos/ORCHESTRATION.md (current file — for inventory only)

Your task: rewrite ORCHESTRATION.md from scratch.

Scope:
- Workflow handoff sequence under co-equal authority (NOT HEPHAISTOS → Queen Keyport → Hermes as rank order; rather, Hephaistos and Queen Keyport operate within their scopes in parallel or sequence as the task requires)
- Consequence classification (rewrite the table — replace tier labels with authority scope labels)
- Single-skill routing (may preserve structure, just relabel)
- Skill composition declaration format
- Conflict resolution between skills (rewrite the authority order section)
- Escalation and refusal conditions
- Orchestration anti-patterns (preserve, but remove "right-arm hierarchy" references to any ranking between Philosopher and Power-Analyst since both are co-equal)
- Execution context budget rule (preserve)
- Phase artifact schema (preserve)
- Seeds long-horizon ideation (preserve)
- Tracker contract (preserve)
- Session headroom pause prompt (preserve)
- Monthly tracker archive rule (preserve)
- Promotion check (rewrite to reflect co-equal — both authorities must clear, not governance as sole gate)

Non-negotiable constraints:
- No "Tier 0", "Tier 1", "Tier 2" language anywhere. Use "scope: forging", "scope: governance", "scope: routing".
- No "governance is center" or "governance is primary" unless scoped to "within its own authority, governance is primary for constraints".
- Remove L99 from Binding Principles. Remaining principles renumber 1-8.
- Rewrite the consequence classification table to map consequence domains to SCOPES (forging, governance, routing) rather than TIERS. Research and writing skills remain supporting layers but are no longer labeled "Tier 3" or "Tier 4" — just "research scope" and "writing scope".

This is the largest file in Wave 1. Take time. Show me the proposed content in CHUNKS if needed (e.g., section by section). I would rather review 3 chunks of 500 lines each than 1 blob of 1500 lines.

Propose how you want to structure the review — chunk-by-chunk or full file. Wait for my answer.
```

### Operator review checkpoint
Likely takes several iterations. Focus especially on:
- The consequence classification table
- The workflow/handoff section
- The conflict resolution section
- Any inherited phrasing that preserves hierarchy

### Stage 3 commit and audit

```bash
cd /home/cerebrhoe/hephaistos
git add ORCHESTRATION.md
git commit -m "Stage 3: ORCHESTRATION.md rewrite — co-equal workflow, L99 demoted"
```

**Argus audit (BINDING):** Seven-layer + Mercury Protocol.

**Stop point.** End session. Stage 4 is another session.

---

## Stage 4: Root File Cleanup

### Purpose
Under Option 2 (collapse to repo), the root `/home/cerebrhoe/HEPHAISTOS.md`, `QUEEN-KEYPORT.md`, `HERMES.md`, `ORCHESTRATION.md` are now redundant. Either delete them or replace with thin pointers.

### Decision needed
Operator chooses: delete entirely, or replace with thin "see /home/cerebrhoe/hephaistos/" pointers. Thin pointers are slightly safer for external scripts/configs that may reference these files.

### Prompt 7 — Root file cleanup (thin pointer version)

```
Cleanup task. Option 2 (collapse to repo-canonical) means root-level redundant files go away.

Files to replace with thin pointers:
- /home/cerebrhoe/HEPHAISTOS.md
- /home/cerebrhoe/QUEEN-KEYPORT.md
- /home/cerebrhoe/HERMES.md
- /home/cerebrhoe/ORCHESTRATION.md

For each of these files, replace contents with a thin pointer — no more than 10 lines. Template:

# [FILENAME]

This file has been superseded. The canonical expanded version lives at:

/home/cerebrhoe/hephaistos/[FILENAME]

This stub exists only so that tooling that still references /home/cerebrhoe/[FILENAME] does not error. The canonical content, including all authority definitions, scope rules, and governance discipline, is in the repo version.

Superseded: 2026-04-17 (Wave 1 root/repo consolidation per CO-EQUAL-AUTHORITY-DECISION.md).

---

Show me the four proposed files before writing.
```

### Alternative Prompt 7 (delete version)

If operator chooses deletion over pointers:

```
Delete the four redundant root files. Do not replace.

Files to delete:
- /home/cerebrhoe/HEPHAISTOS.md
- /home/cerebrhoe/QUEEN-KEYPORT.md
- /home/cerebrhoe/HERMES.md
- /home/cerebrhoe/ORCHESTRATION.md

Before deleting, scan /home/cerebrhoe/ for any script or config file that references these paths. List them so I can update them before deletion.

Do not delete until I have confirmed no live references remain.
```

### Operator review checkpoint
If any scripts/configs reference the root files, update them first. Then delete or stub.

### Stage 4 commit

Not a git commit in the hephaistos repo (these files are outside the repo). Instead, log the change in your tracker. If you maintain the MASTER TRACKER per the hephaistos discipline, write a closeout note.

**Stop point:** Root system now minimal. End session.

---

## Stage 5: Argus L99 Integration

### Purpose
Update the Argus configuration files to add L99 as a Layer 3 sub-gate per `L99-DEMOTION-TO-ARGUS.md`.

### Prompt 8 — Argus L99 integration

```
Argus update task. Add L99 as a Layer 3 sub-gate per L99-DEMOTION-TO-ARGUS.md.

Context files:
1. /home/cerebrhoe/hephaistos/L99-DEMOTION-TO-ARGUS.md
2. /home/cerebrhoe/hephaistos/argus/argus-contract.md
3. /home/cerebrhoe/hephaistos/argus/argus-formation.md
4. /home/cerebrhoe/hephaistos/argus/argus-manifest.md

Your task: update the Argus files to integrate L99 detection as a Layer 3 sub-gate.

Specifically:
1. In argus-contract.md (or wherever the seven-layer audit composition is formally declared), add the L99 sub-gate inside Layer 3 with the detection logic from the L99 spec (claim → evidence basis named → gap declared or not → verdict).
2. Add the three calibration examples (pass, finding, block) from the L99 spec as concrete test cases.
3. Update any section listing "binding principles" to reflect that L99 is now an audit criterion, not a binding principle.
4. Do not create a new Layer 8. L99 lives inside Layer 3.
5. Preserve AND-gate enforcement — an L99 FINDING at Layer 3 halts the audit.

This is a surgical update, not a rewrite of the Argus files. The Argus architecture itself is not changing — only the L99 placement. Small, precise edits.

Show me each edit before writing.
```

### Operator review checkpoint
Argus files are the only place in Wave 1 where surgical patches are correct instead of fresh rewrites. Verify the L99 sub-gate integrates cleanly into existing Layer 3 logic.

### Stage 5 commit

```bash
cd /home/cerebrhoe/hephaistos
git add argus/
git commit -m "Stage 5: Argus L99 integration as Layer 3 sub-gate"
```

No binding audit needed here — this is the audit system itself being updated.

---

## Stage 6: Skill Registry — SKILL-MAP.md Six Core Skills

### Purpose
Register six core governance skills per the original Wave 1 NEXT-STEPS.md requirement.

### Prompt 9 — Skill registration proposal

```
Skill registration task.

Context files:
1. /home/cerebrhoe/hephaistos/SKILL-MAP.md (current skill registry)
2. /home/cerebrhoe/hephaistos/skills/ (directory — enumerate top-level skill folders)
3. /home/cerebrhoe/hephaistos/CO-EQUAL-AUTHORITY-DECISION.md

Your task, in two parts:

Part 1 (proposal): propose six "core governance skills" to register formally in SKILL-MAP.md. Core means: skills that implement the governance spine of the co-equal authority architecture. Think of them as the skills without which the governance system cannot function.

Candidate set to consider (from memory of the system):
- recursive-governance-method
- diamond-eyes (or aesthetic-refinement)
- philosopher
- fully-rounded-power-analyst
- humanize
- trace-investigator
- red-team
- skill-architect

Propose a bounded set of six. Explain why each of these six is "core" and why others were excluded.

Part 2 (registration — only after I approve the six): write the registration entries for SKILL-MAP.md per the file's existing schema. Do not invent a schema; match what's already there.

Stop after Part 1. Wait for my approval.
```

### Operator review checkpoint
The operator decides the six. Push back on the agent's proposal if it privileges any skill that doesn't actually fit co-equal governance.

### Stage 6 commit + Wave 1 final audit

After the six are registered:

```bash
git add SKILL-MAP.md
git commit -m "Stage 6 / Wave 1 complete: register six core governance skills"
```

**Final Argus audit (BINDING, full seven-layer):** Against the entire Wave 1 delta — all commits from Stage 1 through Stage 6. This is the comprehensive check.

If final audit passes: Wave 1 complete. Push.

---

## Failure Modes to Watch For

### Failure mode 1: Primacy reassertion in Stage 2
Most likely in Prompt 3 (HEPHAISTOS) or Prompt 4 (QUEEN KEYPORT). If operator review catches subtle primacy language, reject and request revision. If it slips through and Argus catches it later, the commit gets reverted.

### Failure mode 2: Scope creep mid-session
Claude Code may propose "while we're here, let's also update X." Refuse. Each stage has its own scope. Stage 2 does not touch Stage 3 files. If Claude Code proposes this, respond: "No. Stage Y is its own session."

### Failure mode 3: L99 references outside binding-principles sections
The binding-principles sections are obvious places. But L99 may be referenced inline elsewhere (e.g., in a footer or a sub-section titled "Why evidence matters"). A full text search after each stage for "L99" catches these.

### Failure mode 4: Root/repo drift recurring
After Wave 1, the collapse to repo-canonical should prevent future drift. But only if operator discipline holds: all future governance edits happen in the repo, never in root. Add this to the monthly consolidation rhythm.

### Failure mode 5: Session headroom exhaustion mid-stage
Each stage is designed to fit in one session. But ORCHESTRATION.md (Stage 3) is large. If session headroom hits 5% mid-rewrite, use the canonical continuity prompt from ORCHESTRATION.md. Do not push through.

---

## What Wave 1 Does Not Include

Explicit gap declarations (L99 self-applied):

1. Handoff templates (`hephaistos-to-queen-keyport.md`, `queen-keyport-to-hermes.md`) are not rewritten. They may have hierarchical language in their JSON schemas. Log for Wave 2.
2. The `SKILL-MAP.md` full consolidation (merging duplicate prompt-engineering skills, etc.) is not done. Only six core skills are registered. Log for Wave 2.
3. Research skills (`peer-reviewed-paper-writer`, `qualitative`, etc.) are not registered. Log for Wave 2.
4. Writing skills (`novelist`, `publisher`, etc.) are not registered. Log for Wave 2.
5. The `PROTOCOLS/debate-redteam.md` file is not reviewed. May contain hierarchy language.
6. The three `CLAUDE.md` variants referenced in PROJECT-TREE (VC-08) are not reconciled. May need separate pass.
7. The `.claude/local-plugins/governance-audit/` Argus plugin implementation is not touched. May need updates to match the L99 sub-gate.
8. The hephaistos repo's own `CLAUDE.md` was already updated earlier today in the initial partial-Wave-1. Verify no contradictions with Stage 2 rewrites.

These are declared as gaps, not ignored. They are Wave 2 (or later) work.

---

## Total Scope Summary

| Stage | Files touched | Session time | Session count |
|---|---|---|---|
| 0 | 2 spec files committed | 15 min | 1 (can fold into Stage 1) |
| 1 | 2 AGENTS.md files | 1-2 hours | 1 |
| 2 | 3 agent identity files | 2-3 hours | 3 (one per agent) |
| 3 | ORCHESTRATION.md | 2-3 hours | 1 |
| 4 | 4 root cleanup files | 30-60 min | 1 |
| 5 | Argus files (surgical) | 45-90 min | 1 |
| 6 | SKILL-MAP.md | 60-90 min | 1 |
| **Total** | **14 files** | **8-14 hours** | **~8 sessions** |

This is not a one-weekend project. It is a multi-session campaign. Spread across 1-3 weeks with rest days in between, per the consolidation-rhythm guide.

---

## Operator Discipline for Execution

Three rules to maintain throughout Wave 1:

**Rule 1: No stage skipped.** Each stage depends on the previous. Do not start Stage 3 before Stage 2 is audited and committed.

**Rule 2: Each stage has its own session.** Do not try to do two stages in one sitting even if one is short. The separation is intentional — it forces a stopping checkpoint.

**Rule 3: Argus findings are binding for the constitutional layer.** If Argus flags a primacy reassertion in Stage 2, that is not a style preference to override. That is the architecture refusing to let itself drift. Fix it before proceeding.

---

## Closing Note

This plan is scoped for the decisions as I recommended them. If operator chooses different values for Decisions A-E, the stage structure remains but the prompt content adjusts. The plan is modular; it does not collapse if a decision changes.

If after reviewing this plan it feels like too much, that is a valid signal. Not every wave must be completed in the current quarter. The spec files already committed (`CO-EQUAL-AUTHORITY-DECISION.md`, `L99-DEMOTION-TO-ARGUS.md`) will still be there whenever execution begins. The architecture does not spoil.

The one thing that would be worse than slow execution: partial execution that leaves the system mid-rewrite. Either complete a stage cleanly or postpone it. Never leave a stage half-done.

Come back rested. Read this plan. Decide what you want to commit to. The work is here when you are.

## Related

- [[Research and Papers MOC]]
- [[HERMES]]
