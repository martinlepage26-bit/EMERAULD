---
type: runbook
title: 'RUN ORDER — L99 PHAROS Migration + PR #4'
tags:
- runbook
- artifacts
- 2026-04-19-pharos-migration-pr4
- backend
- bundle
- hardening
- deploy
- railway
status: active
created: '2026-04-19'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/2026-04-19-pharos-migration-pr4/_manifest/RUN-ORDER.md
backlink_count: 2
backlinks:
- '[[Areas/Writing/Research and Papers MOC]]'
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
level: L99
bundle: pharos-migration-pr4
date: '2026-04-19'
---

# RUN ORDER — L99 PHAROS Migration + PR #4

The sequence matters. Do it in this order. Each step has a verification gate;
do not proceed if a gate fails. Copy-paste commands are ready as written,
assuming the bundle sits at `<REPO>/artifacts/2026-04-19-pharos-migration-pr4/`
or you have unzipped the L99 bundle into a sibling of `backend/`.

---

## Phase 0 — Preflight (5 min)

```bash
# Verify bundle integrity
cd <bundle-root>/_manifest
sha256sum -c SHA256SUMS.txt

# Confirm no .py file is broken
cd <bundle-root>
python3 -m py_compile 02-pipeline-triage/*.py 03-pr4-hardening/*.py 03-pr4-hardening/reference/*.py
```

**Gate:** every file OK. If any fails, stop — the bundle is corrupt.

---

## Phase 1 — Close the PR #4 P1 blocker (10 min)

Two paths. Pick one.

### Path A — Drop-in patch

```bash
cd <pharos-repo>/backend
# Apply the surgical diff to the PR #4 branch
git checkout pr-4-branch
git apply <bundle-root>/_manifest/PATCH-pr4-dnspython.diff
git add requirements.txt
git commit -m "fix(backend): restore dnspython==2.6.1 for mongodb+srv:// Atlas resolution (closes P1)"
git push
```

### Path B — Full requirements replacement

```bash
cp <bundle-root>/01-deploy-config/requirements.txt <pharos-repo>/backend/requirements.txt
git add backend/requirements.txt
git commit -m "fix(backend): restore dnspython + pin full dep tree (closes PR #4 P1)"
git push
```

**Gate:** GitHub Actions `test-backend` job passes. If it doesn't, read the log —
the test suite in this bundle (`03-pr4-hardening/test_backend_hardening.py`) has
an explicit regression guard for dnspython that will emit the exact error text.

---

## Phase 2 — Apply PR #4 server hardening (20–30 min)

```bash
cd <pharos-repo>/backend
# Install bundle's diagnostic and test alongside the real code
cp <bundle-root>/03-pr4-hardening/server_hardening_patch.py .
mkdir -p tests
cp <bundle-root>/03-pr4-hardening/test_backend_hardening.py tests/

# Step 2a — See what's already in server.py and what's missing
python3 server_hardening_patch.py --check

# Step 2b — Hand the Codex prompt the real server.py
#   Open <bundle-root>/03-pr4-hardening/CODEX_PROMPT_SERVER_HARDENING.md
#   Paste into Codex with server.py in context. Let Codex produce a diff.
#   Review the diff. Apply.

# Step 2c — Verify
pip install -r requirements.txt
pytest tests/test_backend_hardening.py -v
```

**Gate:** 15/15 tests pass. If any fail, compare your `server.py` against
`<bundle-root>/03-pr4-hardening/reference/server.py` — it's the golden reference
and passes cleanly.

---

## Phase 3 — Cloudflare dashboard migration (30 min — operator-manual)

Follow `01-deploy-config/migration-govern-to-pharos.md` §1–§4 exactly.

**Important:** Cloudflare Pages projects **cannot be renamed**. The procedure for Pages
is create-fresh + cut-over DNS + delete-old, not rename. D1 databases and R2 buckets
likewise cannot be renamed in place — migrate (create new, copy data, point bindings
at the new resource) or recreate, then drop the old.

**Order matters:**

1. **CF Pages** — create a fresh `pharos-ai` project in the dashboard, connect it to
   the same GitHub repo and build settings, verify it builds green, cut `pharos-ai.ca`
   DNS to the new `pharos-ai.pages.dev` target, then delete the old `govern-ai`
   project. Expect ~5 min DNS propagation. *(Do this FIRST — the deploy pipeline is
   pointed at the new name.)*
2. **D1 database** — migrate `govern-suite` → `pharos-suite` (create new, export/import
   data, repoint bindings) or recreate fresh if the data is rebuildable.
3. **R2 buckets** — migrate `govern-artifacts` → `pharos-artifacts` and
   `govern-evidence` → `pharos-evidence` (create new buckets, copy objects with
   `wrangler r2 object` or `rclone`, cut bindings, delete old).

After each rename, update the corresponding line in `01-deploy-config/wrangler.toml`:

| Line | Field | Before | After |
|---|---|---|---|
| 31 | `database_name` | `govern-suite` | `pharos-suite` |
| 32 | `database_id` | `REPLACE_WITH_ACTUAL_ID` | (from CF dashboard) |
| 39 | `bucket_name` | `govern-artifacts` | `pharos-artifacts` |
| 45 | `bucket_name` | `govern-evidence` | `pharos-evidence` |

```bash
# Commit wrangler.toml after dashboard changes
cp <bundle-root>/01-deploy-config/wrangler.toml <pharos-repo>/aurorai/wrangler.toml
# ...edit the four lines above...
git add aurorai/wrangler.toml
git commit -m "chore(aurora): sync wrangler.toml with CF dashboard renames"
git push
```

**Gate:** `wrangler deploy --env production` succeeds. Check the CF dashboard
— only `pharos-aurora-worker-prod` should be present, bindings resolve to
`pharos-*` resources, not `govern-*`.

---

## Phase 4 — Railway deploy with fixed Dockerfile (15 min)

The Dockerfile in `03-pr4-hardening/` is the only one you should ship. The one
in `01-deploy-config/` uses exec-form `CMD` and will silently fail on Railway.

```bash
cp <bundle-root>/03-pr4-hardening/Dockerfile <pharos-repo>/backend/Dockerfile
git add backend/Dockerfile
git commit -m "fix(backend): shell-form CMD so Railway \$PORT injection expands"
git push
```

**Gate:** Railway deploy health check passes. `curl https://<railway-host>/api/health`
returns `{"status":"ok","db_ready":true,...}`.

If `db_ready` is `false`, the app is up but Atlas is unreachable. That's not the
dnspython bug (that would crash before health) — it's a config miss: check
Railway env vars `MONGO_URL`, `DB_NAME`, IP allow-list in Atlas.

---

## Phase 5 — GitHub Actions pipeline (10 min)

```bash
mkdir -p <pharos-repo>/.github/workflows
cp <bundle-root>/01-deploy-config/deploy.yml <pharos-repo>/.github/workflows/deploy.yml
git add .github/workflows/deploy.yml
git commit -m "ci: unified deploy pipeline (test-backend / deploy-backend / deploy-frontend)"
git push
```

**Gate:** Next push to main produces three green jobs: `test-backend`,
`deploy-backend`, `deploy-frontend`. The first ensures the dnspython regression
guard runs on every PR forever.

**Required repo secrets** (Settings → Secrets → Actions):

- `RAILWAY_TOKEN`
- `CLOUDFLARE_API_TOKEN`
- `CLOUDFLARE_ACCOUNT_ID`
- `REACT_APP_ADMIN_PASSPHRASE`

**Required repo variables:**

- `REACT_APP_BACKEND_URL`  (the Railway URL, with `/api`)
- `RAILWAY_SERVICE_NAME`  (optional; defaults to `pharos-backend`)

---

## Phase 6 — Archive triage decisions (operator-manual)

Read `02-pipeline-triage/martin_decision_brief.md`. Three decisions needed:

1. **AI & Society manuscript** (`ai-anxiety-...md`, flagged MERGE, source-bearing,
   high-confidence): decide **KEEP** or **HUMAN-REVIEW-MERGE**. Do NOT auto-merge.
2. **Topology vocabulary gap** (`topology_theseus`, `topology_auryn`, `topology_hopf`
   have zero keyword hits): decide whether to re-run extraction with corrected
   target strings, or declare the method docs not-yet-ingested.
3. **`moving parts.txt`** (only file with CompassAI + AurorAI hits, flagged MERGE):
   extract provenance before merge — otherwise the archive loses its only
   keyword-traceable link to both implementation surfaces.

Run the tools after deciding:

```bash
cd <bundle-root>/02-pipeline-triage
python3 pharos_pipeline_filter.py        # applies decisions
python3 compassai_aurorai_extractor.py   # pulls refs for both products
python3 topology_audit.py                 # re-verifies topology coverage
```

---

## Final verification

```bash
# End-to-end smoke
curl https://pharos-ai.ca                           # 200, SPA shell
curl https://<railway-host>/api/health              # 200, db_ready:true
curl https://pharos-aurora-worker-prod.ACCOUNT.workers.dev/health  # 200

# Repo state
cd <pharos-repo>
git log --oneline -10                               # should show the 4 commits above
gh pr view 4                                         # should be mergeable
```

If all three probes are 200 and `gh pr view 4` is mergeable — merge PR #4 and this
bundle is discharged.

## Related

- [[Research and Papers MOC]]
- [[SHOW-ME-WHAT-TO-DO]]
