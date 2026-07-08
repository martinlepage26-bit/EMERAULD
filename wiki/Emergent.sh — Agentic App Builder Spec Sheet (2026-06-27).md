---
type: tool-spec
title: Emergent.sh — Agentic App Builder Spec Sheet (2026-06-27)
aliases:
- emergent.sh
- Emergent
- Emergent AI
- Emergent app builder
- wiki/Emergent.sh — Agentic App Builder Spec Sheet (2026-06-27)
tags:
- ai-tools
- app-builder
- vibe-coding
- external-platform
- software-development
- tool-spec
- wiki
- emergent-sh-agentic-app-builder-spec-sheet-2026-06-27-md
- emergent
- export
- enterprise
- mobile
- official
- color-orange
status: active
created: '2026-06-27'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Emergent.sh — Agentic App Builder Spec Sheet (2026-06-27).md
backlink_count: 6
backlinks:
- '[[.graph_store/graph_report]]'
- '[[wiki/AI Infrastructure Stack]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[memory/daily/2026-06-27]]'
- '[[session-state]]'
source_urls:
- https://emergent.sh/
- https://emergent.sh/faq
- https://emergent.sh/pricing
- https://emergent.sh/enterprise
evidence_boundary: Official product pages only; no hands-on build, code audit, contract
  review, or security test performed.
---

# Emergent.sh — Agentic App Builder Spec Sheet (2026-06-27)

Emergent.sh is an external agentic app-builder / vibe-coding platform for turning natural-language product descriptions into web, mobile, and full-stack application prototypes. Its official pages position it as a no-code or low-code build surface that can generate frontend, backend, authentication, database, APIs, AI integrations, testing, and deployment flows from prompts.

**Claim boundary:** this note is a source-grounded spec sheet from official emergent.sh pages accessed 2026-06-27. It is not a hands-on evaluation, security review, legal review, or production-readiness certification.

---

## Working Position

For EMERAULD / PHAROS use, treat emergent.sh as a rapid external build surface, not as canonical infrastructure. It is useful for disposable prototypes, UI shells, MVP exploration, internal demos, and comparative platform analysis. It should not be used for regulated, client-confidential, or production PHAROS work without export, code review, test coverage, secret handling, and a deployment evidence pack.

Related local surfaces:
- [[AI Infrastructure Stack]]
- [[Personal and Projects MOC]]
- [[ChatGPT Apps SDK — Planning, Metadata, Deployment, and Operations]]
- [[Kickstart App Prompt — Template and Synthesis Framework]]
- [[Skill Domain — Deployment and Infrastructure]]

---

## Capability Matrix

| Area | Officially Claimed Capability | Use Boundary |
|---|---|---|
| Natural-language build | Describe an app idea and have the platform generate an application. | Good for initial prototypes; final scope still needs a written spec and acceptance tests. |
| Web applications | Full-stack web app generation with frontend and backend. | Verify generated architecture before treating it as maintainable. |
| Backend services | Database, authentication, user management, APIs, file storage, email services, and third-party services are listed in the FAQ. | Treat backend defaults as provisional until reviewed for auth, data model, migration, and logging behavior. |
| AI integrations | FAQ names AI integrations and OpenAI among supported integration examples. | Check model provider, key storage, data retention, and prompt exposure before use. |
| Payments | FAQ names Stripe / payment processing support. | Payment flows require separate Stripe account review, webhook verification, and legal/tax copy checks. |
| Mobile apps | FAQ claims native iOS and Android app creation, with app-store publishing support on higher tiers. | Native behavior, permissions, and store-compliance still need device testing. |
| Native mobile features | FAQ lists notifications, maps, camera, local storage, location services, and native UI components. | Each feature needs permission, privacy, and platform review. |
| Deployment | FAQ says deployment, security, backups, hosting, and scaling are handled by the platform. | Platform-managed does not mean independently verified; export and recovery path are required for governed work. |
| Custom domains | FAQ says custom domains are supported. | Confirm DNS, SSL, rollback, and ownership controls before public launch. |
| Code export | FAQ and pricing pages identify GitHub sync/export and ZIP export capabilities. | Export should be mandatory before any serious dependency on generated work. |
| Enterprise controls | Enterprise page claims SSO/SAML, RBAC, audit logs, isolated VPC or self-hosted options, encryption, custom models, IP indemnity, SLA, and dedicated support. | Enterprise claims need contract, DPA, security documentation, and proof of the actual deployment mode. |

---

## Pricing Snapshot

Official pricing pages accessed 2026-06-27 list:

| Tier | Price | Credits / Month | Notes |
|---|---:|---:|---|
| Free | $0 | 25 | Public projects; enough for roughly 2-3 simple apps or one medium app per FAQ guidance. |
| Agent | $20/month | 375 | Adds larger monthly capacity and GitHub export. |
| Pro | $200/month | 4,500 | Includes Agent features plus app-store publication lanes and custom integrations / CRM-style use. |
| Enterprise | Custom | Custom | Adds organizational security, deployment, support, and governance controls per enterprise page. |

Credit consumption should be validated empirically before planning real work. The public number of credits does not by itself reveal how quickly complex applications consume them.

---

## Best-Fit Use Cases

- MVP and proof-of-concept applications.
- Landing pages, customer portals, dashboards, marketplaces, and SaaS-style tools.
- Rapid UI exploration for PHAROS / COMPASSai / AurorA surfaces before committing engineering time.
- Internal demo apps where generated code can be exported and audited afterward.
- Comparative analysis against other agentic app builders and app-generation workflows.

---

## Governance Rules for Use

1. Do not enter client secrets, regulated data, legal evidence, unpublished manuscripts, or confidential PHAROS method material into emergent.sh unless the governing contract and security posture have been reviewed.
2. Export generated code through GitHub or ZIP before treating any output as durable.
3. Run a local code review, dependency audit, and application test pass before public deployment.
4. Replace generated secrets and environment variables; never trust platform-generated defaults blindly.
5. Record build prompts, generated outputs, deployment target, and verification evidence in the project tracker.
6. For public PHAROS-adjacent work, separate prototype screenshots from verified product claims.
7. For enterprise use, require security documentation covering data retention, model routing, audit logs, SSO, RBAC, encryption, IP terms, and recovery obligations.

---

## Production Acceptance Checklist

- Written product spec exists before generation.
- Generated app exports cleanly to GitHub or ZIP.
- Build can run outside emergent.sh or has an explicit platform-dependency decision.
- Authentication and authorization paths are reviewed.
- Database schema, migrations, and backups are understood.
- Payment and webhook flows are tested with sandbox credentials.
- AI calls, prompts, model routing, and API-key storage are documented.
- Mobile permissions are tested on real devices if app-store publication is in scope.
- Public copy, privacy policy, and terms are reviewed for the actual product.
- Deployment has rollback, domain ownership, and incident-recovery path.

---

## Open Questions

- What do current terms say about generated code ownership, IP assignment, training-data use, and customer data retention?
- What exact runtime stack is generated for web, backend, and mobile outputs?
- Can generated apps be fully self-hosted after export, or are some services platform-dependent?
- How predictable is credit burn for complex apps, multi-agent iterations, mobile builds, and app-store publication?
- What third-party processors receive prompts, files, logs, or generated application content?
- What security attestations, DPA terms, and regional data-residency options exist for enterprise customers?

---

## Sources

- Official homepage: https://emergent.sh/
- Official FAQ: https://emergent.sh/faq
- Official pricing: https://emergent.sh/pricing
- Official enterprise page: https://emergent.sh/enterprise

Accessed 2026-06-27.
