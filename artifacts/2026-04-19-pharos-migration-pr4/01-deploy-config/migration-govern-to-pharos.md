# docs/migration-govern-to-pharos.md
# PHAROS Migration Runbook: govern-ai → pharos-ai
#
# Status: IN PROGRESS
# Owner: Martin Lepage
# Last updated: 2026-04
#
# This document is the authoritative checklist for completing the rename of every
# object, project, path, and reference from the govern-ai/GovernAI namespace to the
# PHAROS/pharos-ai namespace. Nothing is tabled. Every item has a concrete action.
# Check boxes as you complete them.

---

## 0. Context and boundaries

| Surface | Old name | New name | Status |
|---|---|---|---|
| Public domain | govern-ai.ca | pharos-ai.ca | ✅ Done |
| CF Pages project | govern-ai | pharos-ai | ⬜ Pending |
| CF Pages default URL | govern-ai.pages.dev | pharos-ai.pages.dev | ⬜ Pending |
| Local working tree | /home/cerebrhoe/repos/govern-ai | /home/cerebrhoe/repos/pharos-ai | ✅ Done (symlink in place) |
| Repo remote | github.com/.../pharos-suite | — | ✅ Done |
| Worker name | pharos-aurora-worker | — | ✅ Done |
| D1 database | govern-suite | pharos-suite | ⬜ Pending (data migration) |
| R2 bucket (artifacts) | govern-artifacts | pharos-artifacts | ⬜ Pending (data migration) |
| R2 bucket (evidence) | govern-evidence | pharos-evidence | ⬜ Pending (data migration) |

---

## 1. Cloudflare Pages — rename the project

This is the highest-priority UI step. Everything else in CF depends on it.

**Why it matters:** The deploy pipeline (GitHub Actions and Wrangler) will reference
`pharos-ai` as the project name. While the old project exists under `govern-ai`, any
CI deploy that targets `pharos-ai` will create a NEW project instead of deploying to
the existing one, silently. You will end up with two projects and split deployments.

**Steps:**
1. Log into Cloudflare dashboard → Workers & Pages → govern-ai
2. Click Settings → General → scroll to "Project name"
3. Rename from `govern-ai` to `pharos-ai`
4. Confirm the rename. The new default URL becomes `pharos-ai.pages.dev`
5. Verify that `pharos-ai.ca` custom domain is still attached (it should survive rename)
6. Check that `govern-ai.ca` redirect is still in place if you're keeping legacy compat

**After rename:** Update `deploy.yml` → `projectName: pharos-ai` (already done in
the updated workflow — just ensure you've merged it after doing this step).

---

## 2. Cloudflare Pages — remove govern-ai.pages.dev references

After the rename, `govern-ai.pages.dev` no longer exists. Remove or redirect:

- [ ] Any external links pointing to `govern-ai.pages.dev` (update to `pharos-ai.ca`)
- [ ] Any hardcoded `govern-ai.pages.dev` in frontend code or env vars
- [ ] The Cloudflare Workers bot comment in PR #4 references `b4cdc18e.govern-ai.pages.dev`
      — this is a historical artifact, no action needed, but note it in close-out comment

---

## 3. Cloudflare D1 — rename govern-suite database

**Important:** Cloudflare D1 does not support renaming a database in place. You must:

**Option A — Rename only the display name (no data migration, no risk):**
CF dashboard → D1 → govern-suite → Settings → rename the display name to `pharos-suite`
This is cosmetic. The `database_id` stays the same. The binding in wrangler.toml uses
the ID, not the name, for routing. This is safe and takes 30 seconds.

**Option B — Full migration to new database (only if you want a clean slate):**
1. `wrangler d1 export govern-suite --output schema-and-data.sql`
2. `wrangler d1 create pharos-suite`
3. Note the new database_id output
4. `wrangler d1 execute pharos-suite --file schema-and-data.sql`
5. Update `wrangler.toml` → `database_name = "pharos-suite"` and `database_id = "<new id>"`
6. Deploy the worker with the new binding
7. Verify data integrity with a query
8. Delete old `govern-suite` database

**Recommendation:** Do Option A now (cosmetic rename). Option B when you next have a
maintenance window and want a full clean infrastructure audit.

---

## 4. Cloudflare R2 — rename buckets

**Same situation as D1.** R2 buckets cannot be renamed. Options:

**Option A — Cosmetic (keep bucket names, update binding names only):**
The `wrangler.toml` binding names have already been updated from `GOVERN_*` to `PHAROS_*`
in this PR. The bucket names in CF remain `govern-artifacts` and `govern-evidence`. This
is zero-risk and already done.

**Option B — Full migration (new buckets with new names):**
1. For each bucket (`govern-artifacts`, `govern-evidence`):
   a. Create new bucket: `wrangler r2 bucket create pharos-artifacts`
   b. Download all objects: `rclone sync r2:govern-artifacts /tmp/govern-artifacts-backup`
   c. Upload to new: `rclone sync /tmp/govern-artifacts-backup r2:pharos-artifacts`
   d. Verify object count matches
   e. Update `wrangler.toml` bucket_name entries
   f. Deploy worker
   g. Delete old bucket after 30-day retention period

**Recommendation:** Option A for now. Option B in a scheduled maintenance window.

---

## 5. Local filesystem — retire the symlink

The compatibility symlink at `/home/cerebrhoe/repos/govern-ai` can be removed once:
- All local scripts that reference it have been updated
- CI/CD no longer uses local paths (it shouldn't — CI runs fresh)

**Steps:**
```bash
# Audit: find any scripts still using the old path
grep -r "govern-ai" /home/cerebrhoe/repos/pharos-ai/scripts/ 2>/dev/null
grep -r "govern-ai" /home/cerebrhoe/repos/pharos-ai/dev.ps1 2>/dev/null
grep -r "govern-ai" /home/cerebrhoe/repos/pharos-ai/dev.commands.ps1 2>/dev/null

# Once confirmed clean:
rm /home/cerebrhoe/repos/govern-ai

# Add a note to your shell history or a local DONE.md
echo "Symlink /home/cerebrhoe/repos/govern-ai removed $(date)" >> ~/pharos-migration.log
```

---

## 6. Environment variables — audit for hardcoded govern-ai references

```bash
# In the repo root:
grep -rn "govern-ai" . \
  --include="*.env*" \
  --include="*.toml" \
  --include="*.json" \
  --include="*.yml" \
  --include="*.yaml" \
  --include="*.ts" \
  --include="*.js" \
  --include="*.py" \
  --include="*.md" \
  | grep -v ".git" \
  | grep -v "node_modules"
```

Known remaining references as of this writing:
- `wrangler.toml` → bucket/DB names (tracked above in steps 3–4)
- `CHANGELOG.md` → historical references (leave as-is, they are accurate history)
- `README.md` → migration stance section (update once migration is complete)

---

## 7. PR #4 — resolve and merge

PR #4 is blocked by the dnspython P1 bug. To unblock:

1. On the `codex/explain-pull-request-functionality-rfo8xj` branch, add to `backend/requirements.txt`:
   ```
   dnspython==2.6.1
   ```
2. Commit with message: `fix: restore dnspython for mongodb+srv:// SRV resolution`
3. Push the branch — Cloudflare Pages will deploy a new preview
4. Verify the backend starts without error against your Atlas MONGO_URL
5. Merge PR #4 into main

The complete corrected `requirements.txt` is in this PR as `backend/requirements.txt`.

---

## 8. Backend hosting — resolve the Python/Cloudflare Pages gap

The FastAPI backend cannot deploy to Cloudflare Pages. It is currently running locally
at `http://127.0.0.1:9202`. Production requires a persistent Python host.

**Chosen solution: Railway**

Railway supports FastAPI natively, connects to MongoDB Atlas over SRV, and deploys
from this repo's `backend/` directory with zero additional config files beyond what
is already in this PR.

**Setup steps:**

1. Create a Railway account at railway.app
2. New project → Deploy from GitHub repo → select `pharos-suite`
3. Set root directory to `backend/`
4. Railway auto-detects Python and uses `requirements.txt`
5. Set environment variables in Railway dashboard:
   ```
   MONGO_URL=mongodb+srv://<user>:<pass>@<cluster>.mongodb.net/
   DB_NAME=ai_governance
   RESEND_API_KEY=re_...
   SENDER_EMAIL=governance@pharos-ai.ca
   ADMIN_EMAILS=martin@pharos-ai.ca
   ```
6. Set the start command (Railway Settings → Deploy):
   ```
   uvicorn server:app --host 0.0.0.0 --port $PORT --workers 2
   ```
   Note: Railway injects `$PORT` — use it, not a hardcoded 9202
7. Add a custom domain in Railway: `api.pharos-ai.ca`
8. Add the CNAME in your DNS (Cloudflare DNS):
   ```
   CNAME  api  →  <your-service>.up.railway.app
   ```
9. Update `REACT_APP_BACKEND_URL` in Cloudflare Pages env vars:
   ```
   REACT_APP_BACKEND_URL=https://api.pharos-ai.ca
   ```
10. Redeploy frontend (or push a commit to trigger CI)

**GitHub Actions:** The `deploy.yml` in this PR handles Railway deploys automatically
on every push to main that passes tests. Add `RAILWAY_TOKEN` to repo secrets.

**Dockerfile:** `backend/Dockerfile` is included in this PR. Railway can use it instead
of its auto-detected Python buildpack — either works. The Dockerfile gives you more
control and faster builds after the first run.

---

## 9. Post-migration verification checklist

Run this after all steps above are complete:

- [ ] `curl https://pharos-ai.ca` → returns the PHAROS frontend (200)
- [ ] `curl https://api.pharos-ai.ca/api/health` → returns `{"status": "ok"}` (200)
- [ ] `curl https://api.pharos-ai.ca/api/services` → returns service packages (200)
- [ ] Admin panel at `https://pharos-ai.ca/admin` → loads, authenticates, all tabs work
- [ ] Booking flow → submits, email received via Resend
- [ ] Aurora Worker → `wrangler dev` starts cleanly against `PHAROS_DB` binding
- [ ] No references to `govern-ai.pages.dev` in production traffic (CF Analytics)
- [ ] `govern-ai.ca` redirects correctly to `pharos-ai.ca`
- [ ] GitHub Actions → both jobs green on last push to main
- [ ] Local symlink `/home/cerebrhoe/repos/govern-ai` removed (or noted as intentional)

---

## 10. Migration close-out

Once all boxes above are checked:

1. Update `README.md` → remove "Migration stance" section, replace with current state
2. Update `CHANGELOG.md` → add entry for migration completion
3. Delete this document's "⬜ Pending" items and mark the file as historical
4. Tag the commit: `git tag -a migration-complete-2026 -m "govern-ai → pharos-ai migration complete"`

---

*This runbook was generated as part of the PHAROS boil-the-ocean initiative.
No dangling threads. No workarounds. No tabling.*

## Related

- [[Research and Papers MOC]]
- [[SHOW-ME-WHAT-TO-DO]]
