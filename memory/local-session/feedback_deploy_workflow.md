---
type: memory-register
title: feedback_deploy_workflow
tags:
- memory
- memory-register
- local-session
- commit
- deploy
- pages
- cloudflare
- push
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: memory
canonical_path: memory/local-session/feedback_deploy_workflow.md
backlink_count: 2
backlinks:
- '[[Areas/Writing/Manuscript Pipeline MOC]]'
- '[[wiki/archive/Orphan Index — Operations And Misc — 2026-05-06]]'
---

See also [[Manuscript Pipeline MOC]].
---
name: Always commit, build, and deploy to Cloudflare Pages
description: After any code or content change, always commit → build → deploy to Cloudflare Pages without waiting to be asked
type: feedback
---

Always end every working session with: git commit → npm run build → git push → npx wrangler pages deploy dist --project-name martin-lepage-site

**Why:** User explicitly said "always cloudflare commit build and deploy" — they do not want to ask each time.

**How to apply:** After any change to src/, content/, data/, pages/, or styles/, automatically stage, commit with a descriptive message, push to origin, and deploy to Cloudflare Pages. Do not wait for the user to request it.
