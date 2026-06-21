---
type: wiki
aliases: []
tags: [prompt-engineering, templates, app-building, knowledge-synthesis]
status: active
created: 2026-05-31
updated: 2026-05-31
---

# Kickstart App Prompt — Template and Synthesis Framework

## Summary

A template for writing comprehensive, vault-aware prompts that bootstrap app development by systematically synthesizing required knowledge, constraints, architecture patterns, and success criteria into a single actionable specification. Used as a persistent reference note across [[EMERAULD]] sessions.

## Context

This template pairs with [[GSD — Get Shit Done Context Engineering System]] and [[Claude Code Skill Corpus]] to standardize how app-building prompts are structured when launching development in Claude Code. The framework pulls knowledge from [[AI Infrastructure Stack]] patterns, [[PHAROS Method — Technical Reference]] principles, and [[Governance Controls and Mechanisms]] constraints. Related: [[Ask Vault — EMERAULD Vault Briefing Skill]].

## Details

### Kickstart App Prompt Template

Use this structure when writing a full prompt to action app development. Sections can be adapted per project; the core order is binding.

---

#### 1. **Project Identity & Scope**
```
App Name: [name]
Purpose: [one sentence]
Owner/Domain: [who, which system]
Scope Boundary: [what is in/out]
Timeline: [deadline, phases]
```

#### 2. **Knowledge Synthesis — Synthesize from Vault**

Explicitly state which vault domains apply:
- **Architecture**: [[PHAROS Method — Technical Reference]], [[AI Infrastructure Stack]], [[InfraFabric Architecture]]
- **Governance**: [[Governance Controls and Mechanisms]], [[Queen Keyport — Governance Doctrine]] (reference only)
- **Product**: [[HELIX — Value Proposition and Buyer Profile]], [[PHAROS Commercial Strategy]], [[Obsidian Second Brain Product]]
- **Design**: [[Awesome Design Resources — Curated UI-UX Reference List]], design tokens from `design_guidelines.json`
- **Operations**: [[PHAROS Runbook SOP]], [[Skill Development Workflow — TDD, Dual-Layer, and Eval-Iterate]]
- **Domain-specific**: [other relevant vault notes]

Then include:
```
VAULT BRIEF:
- [Pattern 1 from Architecture]
- [Constraint 1 from Governance]
- [User model from Product]
- [Design system elements]
- [Testing discipline requirement]
```

#### 3. **Requirements & Constraints**

```
MUST HAVE:
- [constraint 1 — from governance/policy]
- [constraint 2 — from architecture]
- [constraint 3 — from operations]

SHOULD HAVE:
- [nice-to-have 1]
- [nice-to-have 2]

MUST NOT:
- [boundary violation 1]
- [boundary violation 2]

GIVEN CONSTRAINTS:
- Stack: [React/FastAPI/etc from [[Awesome Design Resources]]]
- Deploy: [Cloudflare/local/etc]
- Bilingual: [EN/FR or single-language]
- Testing: [[Never mock database]] / other discipline rule
```

#### 4. **Success Criteria & Verification**

```
SHIPPED WHEN:
- [ ] Functionality passes acceptance tests
- [ ] Security review cleared (if applicable)
- [ ] Code review completed ([[Diamond-Eyes]] gate if public-facing)
- [ ] Deployed to [environment]
- [ ] Linked to [[vault/relevant-project-note]]

VERIFY BY:
- Running [specific test command]
- Manual user flow test: [steps]
- Load/performance test: [criteria]
```

#### 5. **Handoff & Documentation**

```
TRACKER ENTRY:
[Write date, app name, status, next action to: [[Master Project Tracker — 2026]] or relevant project tracker]

VAULT LINK:
[If new, create/link [[ProjectName]] hub note; update [[Personal and Projects MOC]]]

NEXT STEP:
[After completion: code review → [[Diamond-Eyes]] → merge → tracker update]
```

---

### Example: DocSort PWA Kickstart (2026 Model)

```
PROJECT IDENTITY
App Name: DocSort — Multi-AI PDF Router
Purpose: Web app to upload PDFs, route to best-fit AI tool (Claude, OpenAI, Gemini, local models)
Owner: Martin Lepage / PHAROS research
Scope: Upload → analysis → structured JSON export; no persistence
Timeline: 1-week prototype, Feb 2026

VAULT BRIEF
- Architecture: LightRAG vector search; React Router 6 SPA; FastAPI backend
- Governance: No auth required (research tool), but API key rotation on exposure (PHAROS incident playbook)
- Product: Tool for researcher efficiency; premium-tier feature candidate for PHAROS launch
- Design: Swiss Scholar system (Newsreader headings, Public Sans body, JetBrains Mono code)
- Testing: Real database connections; no mocks; vector-store semantic tests required

REQUIREMENTS
MUST HAVE:
- React 18 + Tailwind + Shadcn UI ([[Awesome Design Resources]])
- FastAPI backend with Motor (async MongoDB driver)
- Multi-model AI routing (Claude, OpenAI, Gemini)
- PDF text extraction via pdfjs
- JSON export of structured analysis

SHOULD HAVE:
- EN/FR language toggle
- Session history (recent uploads)
- Model-selection override

MUST NOT:
- Store PDFs beyond session
- Expose API keys in frontend
- Mock MongoDB in tests

SUCCESS CRITERIA
SHIPPED WHEN:
- [ ] Upload → route → export works end-to-end
- [ ] Tested on Chrome, Firefox, Safari
- [ ] API keys rotate without manual intervention
- [ ] Linked to PHAROS Research Project Note

TRACKER ENTRY:
2026-05-31 | DocSort PDF Router | Complete | Link to PHAROS Commercial Strategy
```

---

### Integration with Session Workflow

1. **Start of session**: Load this template
2. **Before coding**: Fill sections 1–5 with project-specific data
3. **During development**: Refer to sections 2–4 as decision-making frame
4. **Before shipping**: Complete section 5 (verification & handoff)
5. **After merge**: Update vault project note and tracker

---

## Related

- [[GSD — Get Shit Done Context Engineering System]] — context engineering discipline that pairs with this template
- [[Ask Vault — EMERAULD Vault Briefing Skill]] — skill to auto-generate vault brief for a project
- [[Claude Code Skill Corpus]] — registry of available skills that may apply to the project
- [[Diamond-Eyes — Aesthetic Refinement Skill]] — verification gate for public-facing/client-facing apps
- [[PHAROS Method — Technical Reference]] — foundational patterns referenced in vault brief
