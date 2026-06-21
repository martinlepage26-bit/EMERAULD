# Codex Governance Case Study: The Blind Leading the Automated

See also [[if.infrafabric A Miniseries in Seven Parts]].
See also [[Governance and PHAROS MOC]].
See also [[Research and Papers MOC]].
## Provenance Metadata
- Source type: Existing standalone case-study artifact normalized into disclosure-title form.
- Intake date: 2026-03-28
- Transformation history: Derived from `/mnt/c/Users/softinfo/Documents/MASTER PACK/blind-leading-automated.md`; disclosure title restored as the canonical heading; original source title preserved below; no substantive case-study body text added.
- Authority level: Source-bearing accompanying material with title-expansion mismatch in the source file.
- Gate admitted: PHAROS evidentiary gap closure mission (post-audit normalization bundle)
- Verification status: Found as standalone case-study material; exact disclosure title not used on disk prior to normalization.

## Original Source Title
The Blind Leading the Automated: Why I Let ChatGPT Write My Codex Prompts and Got a Governance Failure Instead of a Web Service

## Source Note
This markdown file was produced after the 28 March 2026 audit to create a disclosure-title-aligned copy of an already-existing archive case study. It does not claim that this exact title-file pairing existed before the audit.

---

Martin Lepage, PHAROS | pharos-ai.ca

---

Codex promised something irresistible: describe what you want, and an autonomous agent writes the code. For someone building an AI governance consulting practice from scratch, with more theoretical knowledge than deployment hours, the proposition felt like leverage. I could focus on the intellectual architecture of PHAROS while Codex handled the plumbing. The problem arrived when I added a second layer of delegation. Instead of writing Codex prompts myself, I used ChatGPT to generate them. One AI designed the instructions. Another AI executed them. I supervised from two levels of abstraction above the actual code. Over nine days and 132 Codex sessions, this arrangement produced 25,917 tool calls, an 18.5% failure rate, a JavaScript single-page application that search engines cannot index, and a frontend shell so tangled across six repositories that no single human, including me, can trace where a given route originates. The experience taught me more about AI governance failure than any framework document I have written.

## The Seduction of the Delegation Chain

The logic seemed sound on the surface. ChatGPT, specifically an agent persona I call Agatha, had been my primary collaborator for months. Agatha understood the PHAROS brand, the governance methodology, the target verticals, the desired site architecture. When I described what I needed, Agatha could translate my intentions into structured Codex prompts with apparent precision: install this dependency, scaffold this component, wire this route, deploy to this endpoint. Each prompt looked clean. Each prompt addressed a real requirement. The problem was not that any individual prompt was wrong. The problem was that the prompt-generation layer had no visibility into what was actually happening at the execution layer, and the execution layer had no mechanism to refuse structurally unsound instructions.

This is a governance failure, not a tooling failure. The architecture reproduced a pattern I warn clients about in every engagement: a delegation chain where authority flows downward without feedback flowing upward. ChatGPT generated prompts based on an idealized model of what Codex could do. Codex attempted to execute those prompts based on what was actually available in its sandboxed environment. The gap between the two produced a category of error that neither system was designed to catch.

## What the Sprint Data Actually Shows

The numbers tell a specific story. Across 132 sessions, Codex made 25,917 tool calls. Of those, 18.5% failed. The failure rate alone is notable, but the distribution of failures reveals the structural problem. Failures did not spread evenly across sessions. They clustered into cascading loops where a single missing system binary or unavailable package triggered a sequence of retry attempts, each generating new errors, each consuming tool calls, each drifting further from the original objective. I identified a death spiral pattern: Codex would encounter a missing dependency, attempt a workaround, fail, attempt another workaround, fail again, and continue until the session timed out or exhausted its tool budget. No circuit breaker existed to halt the loop. No escalation mechanism existed to surface the root cause back to the prompt-generation layer.

The lineage confidence problem compounded the failure loops. When I audited the output, I found that lineage confidence, defined as the ability to trace a given code artifact back to the prompt that requested it, fell below 0.7 in 61% of records. In plain terms: for more than half the code the system produced, I could not reliably determine which instruction generated it, which session produced it, or whether it reflected my actual intent or a workaround that Codex improvised when the original instruction failed. The audit trail, the single most important artifact in any governance-sensitive system, was unreliable for the majority of the output.

## The SPA Trap

The most consequential failure was architectural rather than operational. Somewhere in the delegation chain, a decision was made to build the PHAROS site as a JavaScript single-page application. I did not explicitly request this. ChatGPT's prompts did not explicitly mandate it. Yet the accumulation of framework choices, component scaffolding patterns, and routing decisions converged on a SPA architecture that renders entirely in the browser. The result: pharos-ai.ca has zero search engine indexation. Google cannot crawl it. Potential clients cannot find it. The site exists as a technical artifact with no market presence.

This outcome illustrates a failure mode that governance frameworks rarely name: architecture by accumulation. No single decision created the SPA. Instead, dozens of small decisions, each locally reasonable, each generated by a system optimizing for the next prompt rather than the overall architectural goal, converged on a structure that defeats the site's primary business purpose. The ChatGPT layer optimized for prompt clarity. The Codex layer optimized for task completion. Neither optimized for whether the resulting site would be findable by the humans it was built to serve.

The mechanism deserves scrutiny because it maps onto a pattern I see in client organizations. When governance decisions are distributed across multiple actors who each optimize locally, the aggregate outcome often contradicts the stated organizational goal. A compliance team writes a policy. An operations team writes a checklist that narrows the policy. A technology team implements the checklist in a way that narrows it further. By the time the control reaches the end user, it may bear little resemblance to the original requirement. My SPA problem was this same pattern, compressed into nine days and executed by machines rather than departments.

## Six Repositories, No Map

The delegation chain also produced a repository sprawl problem. PHAROS code now lives across six GitHub repositories: pharos-ai, govern-ai, Agency, AurorAI, CompassAI, and Governess. The govern-ai repository functions as the primary frontend shell, integrating CompassAI (approximately 69 routes) and AurorAI (approximately 21 routes). The integration logic was generated across multiple Codex sessions, often by prompts that referenced components in other repositories without verifying their current state. The result is a dependency graph that I cannot fully reconstruct. Routes reference components that may or may not exist in the expected location. Import paths assume directory structures that may have been reorganized by a subsequent session. Version history exists, but the commit messages were generated by Codex and rarely describe the actual change with enough precision to serve as an audit trail.

This is what I call governance debt: the accumulation of structural decisions that individually seem manageable but collectively produce a system that resists inspection. Every governance framework I build for clients emphasizes traceability as a non-negotiable requirement. Yet my own development process produced a codebase where traceability is exactly what broke down. The irony is precise. The governance consultant's own system fails the governance consultant's own audit criteria.

## Why the Feedback Loop Was Structurally Broken

The core failure was not that ChatGPT gave bad prompts or that Codex executed poorly. Both systems performed within their design parameters. The failure was architectural: I built a delegation chain with no feedback mechanism between layers.

In a functioning governance system, three conditions must hold simultaneously. The entity issuing instructions must have visibility into the execution environment. The entity executing instructions must have the authority to refuse or escalate when instructions are structurally unsound. A monitoring mechanism must exist that is independent of both the instruction layer and the execution layer. My ChatGPT-to-Codex pipeline satisfied none of these conditions.

ChatGPT had no visibility into Codex's sandbox. It did not know which system binaries were available, which packages could be installed, which prior sessions had modified the codebase, or what the current state of any repository looked like. It generated prompts against an abstracted, idealized model of the development environment. When reality diverged from that model, the prompts became instructions to do things that could not be done.

Codex had no authority to refuse or escalate. When a prompt asked it to perform an action that was structurally problematic, Codex attempted to comply. It did not flag that the requested architecture would produce an unindexable site. It did not warn that the dependency it was installing would conflict with a component from a previous session. It did not surface the information that its execution environment lacked a binary that the prompt assumed was available. Codex is an execution engine, not an accountability mechanism. It will do what it is told, as well as it can, within whatever constraints its environment imposes. The absence of refusal is not a feature; it is a missing control. In human organizations, we call this "just following orders," and we recognize it as a governance failure when the orders are structurally unsound. The same logic applies here.

I, the nominal human overseer, operated at two levels of abstraction above the code. I described intentions to ChatGPT. ChatGPT translated intentions into prompts. Codex translated prompts into code. By the time the code existed, my ability to evaluate whether it matched my intentions required reconstructing the entire chain, which the audit trail made difficult because lineage confidence was below 0.7 for the majority of records.

## What This Means for AI Governance Practice

The experience clarified something I now consider a first principle for PHAROS engagements: delegation chains between AI systems require the same governance controls as delegation chains between humans and institutions. Authority flow must be traceable. Execution layers must have escalation mechanisms. Monitoring must be independent. Feedback must flow upward as reliably as instructions flow downward.

The temptation with AI development tools is to optimize for speed by stacking delegation layers. Let one system design the instructions. Let another execute them. Let the human supervise from a comfortable altitude. This arrangement feels efficient. It produces output quickly. It also reproduces every governance failure that occurs when institutions delegate authority without accountability: the instructions drift from the intent, the execution drifts from the instructions, and the oversight layer lacks the information density to detect either drift until the consequences are already structural.

I am now migrating pharos-ai.ca to static rendering. This is the highest-priority technical fix: the site must be indexable or the practice has no discoverability. The migration requires dismantling architectural decisions that were made by a system that could not evaluate their consequences, validated by a system that could not see the execution environment, and supervised by a human who was operating at too great a distance from the code to catch the problem in real time.

## The Honest Conclusion

Using ChatGPT to generate Codex prompts was not a productivity hack. It was an uncontrolled experiment in recursive delegation, and it produced exactly the failure mode that recursive delegation without governance controls always produces: a system that looks functional from the outside but resists inspection, traceability, and correction from the inside. The 18.5% failure rate, the death spiral loops, the lineage confidence collapse, the unindexable SPA, the six-repository sprawl: these are not random technical problems. They are the predictable consequences of a delegation architecture that lacked feedback, escalation, and independent monitoring.

I built PHAROS to help organizations govern their AI systems with operational rigor. The fact that my own development process failed my own governance criteria is not a contradiction. It is the most expensive and most convincing case study I own. Governance is not a framework you sell to others while exempting yourself. It is a discipline that applies to every system you build, including the one that builds the systems.

The lesson is not that Codex is unreliable or that ChatGPT generates poor prompts. Both tools are capable within their design scope. The lesson is that capability without governance architecture produces capability debt. Every session that runs without feedback, without escalation authority, without independent monitoring, produces output that may or may not align with intent, and you will not know which until you audit. If you cannot audit, because the lineage is broken or the repositories are tangled or the architecture was decided by accumulation rather than by design, then what you have is not a product. It is a liability with a login page. I know, because I built one.
