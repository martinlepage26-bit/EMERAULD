---
name: Seven Pillars of Full-Stack Architecture
description: Martin's canonical seven-pillar framework for full-stack architecture — must inform all stack-related work and recommendations
type: reference
originSessionId: 17c66af4-27ef-4b85-ac0e-8bb64a66fd53
---
The seven pillars of full-stack architecture. Apply this framework whenever designing, reviewing, or building any application stack.

1. **Frontend** — everything the user interacts with: pages, buttons, forms. Stack: Next.js + Tailwind.
2. **Backend** — the code that controls what happens when a user interacts with the frontend (form submit, button press). The logic layer.
3. **Database** — where all data lives. Prefer Postgres via Supabase (managed, pre-configured).
4. **Authentication** — how users are set up in the app. Lean on Supabase for execution.
5. **Payments** — monetization layer. Stripe for integration.
6. **Security** — not a separate phase, a continuous concern across all pillars. Key questions: where are secret keys? Can users see other users' data? Think about this at every step.
7. **Infrastructure** — where the app lives, how it's hosted, CI/CD pipelines. Default for simple apps: GitHub + Vercel.

**Why:** Martin stated this must become part of agentic-code make-up. Apply this framework proactively when building or reviewing any stack — not just when asked.

## Related

- [[Governance and PHAROS MOC]]
- [[ChatGPT Apps SDK — Planning, Metadata, Deployment, and Operations]]
