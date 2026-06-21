See also [[Manuscript Pipeline MOC]].
---
name: Always commit, build, and deploy to Cloudflare Pages
description: After any code or content change, always commit → build → deploy to Cloudflare Pages without waiting to be asked
type: feedback
---

Always end every working session with: git commit → npm run build → git push → npx wrangler pages deploy dist --project-name martin-lepage-site

**Why:** User explicitly said "always cloudflare commit build and deploy" — they do not want to ask each time.

**How to apply:** After any change to src/, content/, data/, pages/, or styles/, automatically stage, commit with a descriptive message, push to origin, and deploy to Cloudflare Pages. Do not wait for the user to request it.
