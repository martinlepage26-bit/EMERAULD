See also [[Manuscript Pipeline MOC]].
---
name: deploy_cloudflare_first
description: Always deploy to Cloudflare Pages after making site changes, not just git push
type: feedback
---

Always commit, build, and deploy to Cloudflare Pages after making changes to the Perso site. The full sequence is mandatory after every change.

**Why:** User wants the full cycle every time — no half-stops at just git commit or just build.

**How to apply:** After any change to the Perso site, always run in this exact order:
1. `git add <changed files>`
2. `git -c user.name="martinlepage26-bit" -c user.email="martinlepage26@me.com" commit -m "..."`
3. `npm run build`
4. `npx wrangler pages deploy dist --project-name martin-lepage-site --commit-dirty=true`

Order is: COMMIT → BUILD → DEPLOY. Never skip a step, never reorder.
