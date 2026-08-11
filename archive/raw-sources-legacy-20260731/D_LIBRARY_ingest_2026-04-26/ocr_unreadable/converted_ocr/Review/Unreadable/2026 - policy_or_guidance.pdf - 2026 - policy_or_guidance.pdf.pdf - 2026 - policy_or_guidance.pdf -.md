---
type: raw
source_kind: pdf_text
source_path: /mnt/d/LIBRARY/Review/Unreadable/2026 - policy_or_guidance.pdf - 2026 - policy_or_guidance.pdf.pdf - 2026 - policy_or_guidance.pdf - 2026 - policy_or_guidance.pdf.pdf.pdf
source_rel: Review/Unreadable/2026 - policy_or_guidance.pdf - 2026 - policy_or_guidance.pdf.pdf - 2026 - policy_or_guidance.pdf - 2026 - policy_or_guidance.pdf.pdf.pdf
pages_total: 4
text_first_pages: 4
text_last_pages: 0
pdfinfo:
  CreationDate: "Fri Feb 20 22:12:51 2026 EST"
  Creator: "www.smallpdf.com"
  Custom Metadata: "no"
  Encrypted: "no"
  File size: "248492 bytes"
  Form: "none"
  JavaScript: "no"
  Metadata Stream: "no"
  ModDate: "Fri Feb 20 22:12:51 2026 EST"
  Optimized: "no"
  PDF version: "1.7"
  Page rot: "0"
  Page size: "595.45 x 841.7 pts (A4)"
  Pages: "4"
  Producer: "www.smallpdf.com"
  Suspects: "no"
  Tagged: "no"
  UserProperties: "no"
dr_sort_original_filename: "2026 - policy_or_guidance.pdf - 2026 - policy_or_guidance.pdf.pdf - 2026 - policy_or_guidance.pdf - 2026 - policy_or_guidance.pdf.pdf.pdf.md"
dr_sort_original_path: "raw sources/D_LIBRARY_ingest_2026-04-26/ocr_unreadable/converted_ocr/Review/Unreadable/2026 - policy_or_guidance.pdf - 2026 - policy_or_guidance.pdf.pdf - 2026 - policy_or_guidance.pdf - 2026 - policy_or_guidance.pdf.pdf.pdf.md"
dr_sort_filename_normalized: "2026-05-06"
---

# 2026 - policy_or_guidance.pdf - 2026 - policy_or_guidance.pdf.pdf - 2026 - policy_or_guidance.pdf - 2026 - policy_or_guidance.pdf.pdf.pdf

## Extracted Text

Deterministic Governance for Agentic AI
Proof-Carrying Actions and Bounded Execution Substrates

Abstract
Current AI safety practice relies predominantly on probabilistic behavioral alignment.
Techniques such as RLHF, red-teaming, and output filtering attempt to shape how models
behave. This approach becomes structurally insufficient once AI systems move from text
generation to autonomous execution. Agentic systems do not merely produce language —
they plan, invoke tools, mutate infrastructure, and act within real environments. At that point,
safety can no longer be treated as a statistical property of outputs. It must become a
structural property of execution. This paper proposes a shift from behavioral alignment to
deterministic governance at the execution substrate level. I introduce the concept of ProofCarrying Actions (PCA) — a structured interface separating probabilistic reasoning from
deterministic control. In this model, safety is enforced as a system invariant rather than
inferred from model intent.

1. The Structural Gap
Traditional AI safety operates at the semantic layer of output. Agentic AI shifts risk to the
state-transition layer. We define an agentic system as: S = ⟨M, E, Π⟩
Where:
●
●
●

M — probabilistic reasoning model (e.g., LLM)
E — execution environment (OS, cloud runtime, APIs)
Π — safety policy

In most current architectures, Π is embedded inside M (e.g., system prompts, RLHF
constraints). This creates a fundamental coupling: the same probabilistic model that reasons
is also expected to enforce policy.
I propose decoupling: S' = ⟨M, Es, ℐ⟩
Where:
●
●

Es — deterministic execution substrate
ℐ — formally defined invariant set

The reasoning model may remain probabilistic. The control layer must not.

2. Authority as a Bounded State Region
Most AI systems rely on identity-based access control. This is insufficient for autonomous
agents. Instead of modeling authority via identity, we model it via reachable state space. Let:
●
●

Σ — global system state space
ℐ ⊆ Σ — invariant-preserving safe region

An action a is admissible if and only if: ∀s ∈ ℐ, δ(s, a) ∈ ℐ
Where δ is the transition function. Safety is therefore a geometric property of execution. Not
a behavioral assumption about the model. We do not attempt to constrain all possible
environments. We constrain the region of state transitions the agent is allowed to induce.

3. Proof-Carrying Actions (PCA)
The core architectural construct is: PCA = ⟨A, E, 𝒞, R⟩
Each component exists to eliminate ambiguity between reasoning and execution.
3.1 Action Payload (A)
The raw output of the model:
●
●
●
●

Generated code
API invocation
Shell command
Structured plan step

It is treated strictly as untrusted input. No semantic trust is assumed.
3.2 Constructive Effect Bound (E)
Rather than describing intent, E declares the maximum permissible blast radius. Examples
include:
●
●
●
●
●

Filesystem scope (e.g., read-only /data, write /tmp/session_id/)
Network egress whitelist
CPU and memory ceilings
API schema constraints
Time-bound execution windows

Formally: E = {e₁, e₂, ..., eₙ} Each eᵢ defines a constrained operational region. The system
does not verify what the model intends. It verifies whether declared effects are admissible.
3.3 Attenuated Capability Tokens (𝒞)
Authority is represented through Object-Capability principles. Agents do not “have
permissions.” They possess cryptographically attenuated tokens granting scoped access.
Properties:
●
●
●
●

Delegable but restrictable
Time-bound
Resource-bound
Non-forgeable

Capability attenuation (e.g., Macaroons) ensures authority can only decrease along
execution paths. Authority is attached to the token — not to the identity of the caller.
3.4 Deterministic Recovery State (R)

Fail-closed architectures risk deadlock in distributed systems. To prevent catastrophic
halting, each PCA includes a deterministic fallback: If verification fails: St+₁ = R(St)
Examples:
●
●
●
●

Transaction rollback
Circuit breaker activation
Safe termination of execution loop
Structured error propagation

The system degrades predictably instead of freezing unpredictably.

4. Deterministic Verification Layer
The execution substrate Es performs four strictly deterministic checks:
1.
2.
3.
4.

Syntactic Validation: Verify E conforms to schema.
Capability Validation: Cryptographically verify tokens 𝒞.
Invariant Intersection: Confirm E ⊆ ℐ.
Constructive Enforcement: Execute A inside enforced sandbox (e.g., eBPF,
WebAssembly, microVM).

If runtime behavior exceeds E, the kernel terminates execution. The control layer does not
interpret reasoning. It verifies structure.

5. Addressing Known Failure Modes
5.1 Confused Deputy
In traditional systems, privileged tools can be misused. Under PCA:
●
●
●
●

Tools require capability tokens.
Authority must propagate explicitly.
Absence of token ⇒ operation fails at substrate level.
Privilege cannot be implicitly inherited.

5.2 Semantic Gap
Intent verification is undecidable in open systems. We do not attempt to evaluate intent. We
constrain effect space. If malicious logic is generated but network egress is not permitted,
exfiltration fails regardless of semantic intent. Security becomes boundary enforcement, not
behavioral prediction.

6. Computational Feasibility
Verification operations are computationally lightweight:
●
●
●

Capability Verification: O(1) (Cryptographic check)
Invariant Inclusion: O(n) (Set intersection)
Sandbox Enforcement: <5% overhead (eBPF / microVM)

Inference remains the dominant cost. The execution substrate remains deterministic and
scalable.

7. Trade-Offs and Limits
This architecture does not:
●
●
●

Guarantee semantic correctness
Eliminate long-horizon cumulative risk
Solve open-world completeness

It enforces bounded authority. The trade-off is explicit: Greater structural safety ⇄ Reduced
unconstrained flexibility. This is a deliberate design decision.

8. Integration with Deterministic Substrates
In deterministic fail-closed execution engines:
●
●
●

PCA validation becomes pre-execution gating
Invariant violation triggers atomic interruption
Recovery states prevent cascading deadlock

This integrates naturally with execution kernels designed around deterministic state
transitions, formally modelable invariants, and explicit halting semantics. Safety becomes
enforceable at the substrate — not inferred from behavior.

9. Conclusion
As AI systems gain execution authority, alignment alone becomes insufficient. Probabilistic
reasoning can remain probabilistic. Execution authority must not. Proof-Carrying Actions
offer a structured bridge between uncertain reasoning and deterministic control. The longterm stability of agentic AI systems may depend less on making models “well-behaved,” and
more on ensuring they are mathematically bounded in what they can change. Safety, in this
framing, is not a prediction problem. It is a constraint problem.

## Related

- [[Governance and PHAROS MOC]]
- [[ChatGPT Apps SDK — Planning, Metadata, Deployment, and Operations]]
