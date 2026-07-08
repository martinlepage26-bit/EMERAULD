# Council Orchestration Mapping

## Test Objective
Apply the newly installed `multi-agent-orchestration` skill to the HEPHAISTOS / Queen Keyport / Hermes workflow defined in `AGENTS.md` and the canonical agent entrypoints.

## The Council Workflow (from AGENTS.md)

```
User Request / Task
    ↓
┌─────────────────┐    ┌──────────────────┐
│   HEPHAISTOS    │    │  Queen Keyport   │
│  (artifact      │    │  (governance,    │
│   definition,   │    │   constraints,   │
│   scope,        │    │   refusal        │
│   evidence)     │    │   conditions)    │
└────────┬────────┘    └────────┬─────────┘
         │                      │
         └──────────┬───────────┘
                    │
            Conflict detected?
                 /     \
              YES       NO
               │         │
               ↓         ↓
          Operator   Clearance gate
          arbitrates      │
               └──────────┘
                          ↓
                    ┌──────────┐
                    │  Hermes  │
                    │ (routing,│
                    │ state,   │
                    │ delivery)│
                    └────┬─────┘
                         ↓
                    Output / Action
```

## Pattern Match from `multi-agent-orchestration`

The closest named patterns in the skill are:

| Pattern | Fit | Why |
|---|---|---|
| **Sequential** | Poor | HEPHAISTOS and Queen Keyport are not ordered; they are co-equal. |
| **Parallel** | Partial | Both agents process the same input independently and in parallel. |
| **Hierarchical** | Partial | Hermes sits downstream, but HEPHAISTOS and Queen Keyport are peers, not subordinates. |
| **Consensus** | Poor | They do not vote or debate to reach agreement; they each clear their own scope. |
| **Tool-mediated** | Poor | Communication is direct, not through a shared tool/memory. |

## Proposed Mapping: Gated Parallel Clearance with Operator Arbitration

This is a **composite pattern** not explicitly named in the skill, built from:

1. **Parallel execution** — HEPHAISTOS and Queen Keyport independently validate their respective domains.
2. **Conflict-detection gate** — Compare the two outputs for contradictions on the same task.
3. **Human-in-the-loop arbitration** — If conflict exists, escalate to the Operator (Martin); neither agent proceeds unilaterally.
4. **Sequential downstream routing** — Once cleared, work flows to Hermes for routing, integration, and state monitoring.

## Skill Gaps for This Workflow

The `multi-agent-orchestration` skill's examples focus on:
- CrewAI / AutoGen / LangGraph / Swarm framework code
- Business scenarios (finance, legal, support)
- Patterns where agents cooperate or delegate

It does **not** directly address:
- **Co-equal authority models** with explicit non-veto conflict handling
- **Constitutional / governance-first agent stacks**
- **Human-in-the-loop arbitration as a first-class pattern**

## Recommendation

For the council's own stack, treat the workflow as:

> **Gated Parallel → Operator Arbitration → Router Delivery**

This can be implemented in LangGraph as:
- State node with parallel branches for HEPHAISTOS and Queen Keyport
- Gate node that checks for conflict
- Conditional edge to Operator (human) or Hermes
- Hermes node for final routing

## Council Action

If the council wants to operationalize this, the next step is to draft an ADR using the newly installed `architecture-decision-records` skill, documenting why the co-equal model requires a custom composite pattern rather than an off-the-shelf orchestration framework pattern.
