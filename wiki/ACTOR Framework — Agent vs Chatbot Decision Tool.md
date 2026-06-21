---
type: wiki
aliases:
  - ACTOR framework
  - agent vs chatbot decision
tags: [ai-agents, decision-framework, consulting, tool]
status: active
created: 2026-05-14
updated: 2026-05-14
---

# ACTOR Framework — Agent vs Chatbot Decision Tool

## Summary

The ACTOR framework is a five-dimension evaluation for deciding whether a client scenario requires an AI agent or a chatbot. Source: Praxis AI training material (captured 2026-05-14). Useful for [[PHAROS Commercial Strategy]] consulting intake and scoping.

## The Five Dimensions

| Letter | Dimension | Agent needed when... |
|---|---|---|
| **A** | Autonomy Requirements | System must operate without constant human oversight; real-time decisions required |
| **C** | Complexity Assessment | Multi-step interactions (5+ steps with variables); multi-source information gathering |
| **T** | Tool Integration | Must call external databases, APIs, business systems, or analytical engines |
| **O** | Outcome Variability | Multiple valid solutions; context (priority, seasonality) significantly changes the answer |
| **R** | Reasoning Depth | Trade-offs must be evaluated; solution must adapt to changing conditions |

## Decision Rule

- **3+ High scores → Strong Agent Recommendation**
- **2–3 Medium/High → Agent Recommended**
- **Mostly Low/Medium → Chatbot May Suffice**
- **All Low → Chatbot Recommended**

## Use in PHAROS Consulting

When scoping a new client engagement around AI tools, run ACTOR on their primary use case before recommending architecture. This prevents over-engineering (building agents for chatbot problems) and under-engineering (deploying chatbots for complex autonomous tasks). See [[AI Governance Offer Ladder - Montreal Quebec 90-Day Revenue Plan]] for where this fits in the service ladder.

## Related

- [[AI Governance Offer Ladder - Montreal Quebec 90-Day Revenue Plan]]
- [[PHAROS Commercial Strategy]]
- [[Governance and PHAROS MOC]]
- [[ChatGPT Apps SDK — Planning, Metadata, Deployment, and Operations]]
