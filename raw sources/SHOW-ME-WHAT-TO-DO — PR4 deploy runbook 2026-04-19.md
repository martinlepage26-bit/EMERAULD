# SHOW ME WHAT TO DO

**Date:** 2026-04-19 (late)
**Status of automated work:** DONE. All implementation complete; branches staged; tests green.
**Status of operator work:** 7 items below. Each has the exact command or URL.

> Order is intentional — do them in sequence unless you have a reason to parallelize. Estimated total time: ~60–90 min of hands-on operator time, plus Cloudflare propagation windows.

---

## 0. Before you start — sanity

Confirm what's already done, so you don't redo it:

```bash
# EMERAULD vault — 5 commits pushed to origin/main
git -C /mnt/c/Users/softinfo/Documents/EMERAULD log --oneline origin/main -7

# pharos-suite — 3 commits on local branch, NOT pushed
cd /home/cerebrhoe/PHAROS-SUITE/repos/pharos-suite
git log --oneline wip/com-aur-runtime-build..chore/pr4-archive-toolkit-and-docs
# Expected:
#   5a33fba fix(backend): apply PR #4 Path A — align server with bundle spec
#   46c2a3a docs: operational runbook, CSV diagnostic, decision brief, Codex prompt
#   5fa6999 feat(scripts): add archive-governance toolkit
```

If both are correct → proceed. If not → stop and ask.

---

## 1. Rotate the OpenRouter API key (5 min)

The key `REDACTED_ROTATED_KEY` is currently exported in `~/.bashrc`. It was exposed in a prior chat transcript.

**Browser:**
1. Go to https://openrouter.ai/settings/keys
2. Delete the compromised key.
3. Create a new one. Copy it.

**Then in terminal:**
```bash
# Remove the old export line from ~/.bashrc
sed -i.bak '/OPENROUTER_API_KEY/d' ~/.bashrc

# Verify it's gone
grep OPENROUTER_API_KEY ~/.bashrc && echo "STILL PRESENT — REMOVE MANUALLY" || echo "clean"

# Add the new key to a more restricted location (not ~/.bashrc)
# Option A: ~/.config/openrouter/env with 0600 perms
mkdir -p ~/.config/openrouter && chmod 700 ~/.config/openrouter
umask 077
cat > ~/.config/openrouter/env <<'EOF'
export OPENROUTER_API_KEY="PASTE_NEW_KEY_HERE"
EOF
chmod 600 ~/.config/openrouter/env

# Source it only when needed (tools that explicitly need the key source it themselves)
# Do NOT auto-source from ~/.bashrc.

# Start a fresh shell and verify the old key is gone:
bash -c 'echo "${OPENROUTER_API_KEY:-<unset>}"'
# Expected: <unset>
```

Paste the new key into `~/.config/openrouter/env` before sourcing.

---

## 2. Delete the old BRAINiaC directory (1 min)

```bash
# Confirm EMERAULD is pushed and the old copy isn't the only one
git -C /mnt/c/Users/softinfo/Documents/EMERAULD log --oneline -1 origin/main
# Should show: f0ad82e (or later) — newer than the rename commit cf1e007

ls /mnt/c/Users/softinfo/Documents/BRAINiaC/ | head -5
# Should still have files

# Safe to delete — EMERAULD has everything
rm -rf "/mnt/c/Users/softinfo/Documents/BRAINiaC"

# Verify
ls /mnt/c/Users/softinfo/Documents/BRAINiaC 2>&1
# Expected: "cannot access" — gone
```

---

## 3. Record Decision 1 — AI & Society manuscript (10 min)

This blocks the archive governance pipeline until recorded.

**Read the brief:**
```bash
less /mnt/c/Users/softinfo/Documents/EMERAULD/artifacts/2026-04-19-pharos-migration-pr4/docs/martin_decision_brief.md
# Decision 1 is at the top.
```

**The decision:** the file `ai-anxiety-recursive-governance-ai-society-aligned-2026-03-11.md` is flagged `MERGE_WITH_RELATED_FILE` in the manifest. This is wrong — it's your `AI & Society` submission. Two options:
- **Option A (recommended):** preserve as standalone, no merge.
- **Option B:** intentional merge (you know something the diagnostic doesn't).

**To record Option A** (recommended):
```bash
# Locate the real manifest — not the bundle fixture. It lives with the
# archive the diagnostic scanned. Most likely under your archive CSV location.
# The bundle ships a *synthetic* manifest under test_fixtures/ — do NOT
# use that one.

# Dry-run first against the REAL manifest (path TBD — if you don't know,
# skip this step and ask me to find it in the next session):
python3 /home/cerebrhoe/PHAROS-SUITE/repos/pharos-suite/scripts/manifest_decision_executor.py \
  --manifest <path-to-real-00_ARCHIVE_METADATA_MANIFEST.csv> \
  --decision 1 --dry-run

# If output looks right:
python3 /home/cerebrhoe/PHAROS-SUITE/repos/pharos-suite/scripts/manifest_decision_executor.py \
  --manifest <path-to-real-00_ARCHIVE_METADATA_MANIFEST.csv> \
  --decision 1 --apply
```

The script backs up the manifest before writing and sets `action=PRESERVE_AND_LIGHTLY_CLEAN`, `human_gate_cleared=true`, and the note. You can then run the pipeline filter without it exiting 1.

---

## 4. Record Decision 3 — Regulatory scope (15 min)

Read the brief §3. The question is simple: **does PHAROS make regulatory compliance claims** (EU AI Act, NIST AI RMF, ISO 42001, AIDA, CA Voluntary Code) in the patent, the manuscript, or the product pages?

**If NO** — flag it and move on:
```bash
# One-liner: annotate the empty regulatory CSV so the diagnostic stops flagging it
echo "# out_of_scope_v1 — PHAROS does not make regulatory compliance claims in the current scope." \
  > <path-to>/ai_governance_regulatory_docs.csv
```

**If YES** — bootstrap the corpus:
```bash
# From pharos-suite root, on the chore/pr4-archive-toolkit-and-docs branch
cd /home/cerebrhoe/PHAROS-SUITE/repos/pharos-suite
python3 scripts/regulatory_corpus_bootstrap.py --output-dir ./regulatory_corpus

# Then download the PDFs manually (links in regulatory_docs.csv):
# - NIST AI RMF:  https://www.nist.gov/artificial-intelligence/ai-risk-management-framework
# - EU AI Act:    https://eur-lex.europa.eu/eli/reg/2024/1689/oj
# - ISO 42001:    (purchase or via your institutional access)
# - Canadian AIDA: https://ised-isde.canada.ca/site/innovation-better-canada/en/artificial-intelligence-and-data-act
# - CA Voluntary Code: (URL in the CSV)
#
# Drop the PDFs into regulatory_corpus/pdfs/ and re-run the compliance-claim
# audit against the archive.
```

---

## 5. Pick backend hosting (5 min — decision only)

Two realistic choices. Decide, then the next step's commands differ by pick:

| | Railway | Hetzner VPS |
|---|---|---|
| **Simplicity** | One click; `$PORT` auto-injected; bundle Dockerfile already shell-form | You manage OS, nginx, TLS, log rotation |
| **Cost at current scale** | ~$5–20/mo | ~€4.50/mo (CX22) |
| **Cold-start** | <1 s | always warm |
| **Logs/metrics** | built-in | you wire it |
| **Time to deploy** | ~15 min | ~2 hr first time |

**If Railway:**
- Set env vars in Railway: `MONGO_URL`, `DB_NAME`, `ENVIRONMENT=production`, `ALLOWED_ORIGINS`.
- Point Railway's root dir to `/backend` in project settings.
- The Dockerfile already works; Railway injects `$PORT`.
- After deploy, `curl https://<railway-host>/api/health` should return `{"status":"ok","environment":"production","db_ready":true}`.

**If Hetzner:**
- Use `docs/PHAROS_OPERATIONAL_RUNBOOK.md` §6 as a starting point; it's Railway-oriented but the Dockerfile builds the same image either way.
- You'll additionally need: Caddy or nginx + Let's Encrypt, systemd unit for the container, UFW rules, a backup job for Mongo Atlas URL secrets.

**Record the pick** in `EMERAULD/session-state.md` under Decisions Made.

---

## 6. Cloudflare: recreate Pages, migrate D1 + R2 (30 min + 5 min DNS window)

CF Pages projects, D1 databases, and R2 buckets **cannot be renamed** — you migrate (create new, copy data, repoint bindings) or recreate.

Reference: `EMERAULD/artifacts/2026-04-19-pharos-migration-pr4/_manifest/RUN-ORDER.md` §Phase 3 (already updated to match the recreate procedure).

### 6a. Pages (FIRST — downtime window)

CF dashboard → **Workers & Pages** → **Create application** → **Pages** → connect the same GitHub repo as `govern-ai` with identical build settings, name it `pharos-ai`.

```bash
# After the new pharos-ai project builds green in the CF dashboard:
# Cut DNS — CF dashboard → pharos-ai.ca zone → DNS → update the CNAME on
# the apex to point at pharos-ai.pages.dev (was: govern-ai.pages.dev).

# Wait ~5 min for propagation. Verify:
dig +short pharos-ai.ca
curl -I https://pharos-ai.ca

# Once traffic is confirmed on pharos-ai, delete govern-ai:
# CF dashboard → Workers & Pages → govern-ai → Settings → Delete project
```

### 6b. D1 database

```bash
# Create the new D1 and capture its UUID
cd /home/cerebrhoe/PHAROS-SUITE/repos/pharos-suite/aurorai
wrangler d1 create aurorai-dev
# → copy the database_id it prints

# Apply the schema
wrangler d1 execute aurorai-dev --local \
  --file aurorai/schema/aurorai-d1-schema.sql   # adjust path if different

# If migrating data from an old govern-suite D1:
wrangler d1 export govern-suite --output /tmp/govern-suite.sql
wrangler d1 execute aurorai-dev --file /tmp/govern-suite.sql
# (or use sqlite3 directly if you have the binary)

# Update wrangler.toml — replace the placeholder database_id
# The relevant line in aurorai/wrangler.toml currently is:
#   database_id = "OPERATOR-MUST-PROVISION-RUN-WRANGLER-D1-CREATE-AURORAI-DEV"
# Replace with the UUID from the create step.
```

### 6c. R2 buckets

```bash
cd /home/cerebrhoe/PHAROS-SUITE/repos/pharos-suite/aurorai

# Create fresh buckets with the pharos prefix
wrangler r2 bucket create pharos-artifacts
wrangler r2 bucket create pharos-evidence

# If migrating existing objects:
wrangler r2 object list govern-artifacts --remote | while read key; do
  wrangler r2 object get  govern-artifacts/"$key" --file /tmp/r2-migrate/"$key"
  wrangler r2 object put  pharos-artifacts/"$key" --file /tmp/r2-migrate/"$key"
done   # adapt for evidence bucket; or use rclone for anything larger than a handful of files

# Update wrangler.toml — flip the bucket_name from govern-artifacts to pharos-artifacts
# (and repeat for govern-evidence → pharos-evidence)

# Then deploy:
wrangler deploy --env production

# Only after the worker is live against pharos-* bindings:
wrangler r2 bucket delete govern-artifacts
wrangler r2 bucket delete govern-evidence
```

### 6d. Commit wrangler.toml

```bash
cd /home/cerebrhoe/PHAROS-SUITE/repos/pharos-suite
git add aurorai/wrangler.toml
git commit -m "chore(aurora): sync wrangler.toml with Cloudflare resources (D1 + R2)"
# Do NOT push yet — do it together with the Path A push in step 7.
```

---

## 7. Review + push the pharos-suite branch (10 min)

```bash
cd /home/cerebrhoe/PHAROS-SUITE/repos/pharos-suite

# Review the four commits (three base + one wrangler if you did step 6d)
git log --oneline wip/com-aur-runtime-build..chore/pr4-archive-toolkit-and-docs

# Diff summary
git diff wip/com-aur-runtime-build..chore/pr4-archive-toolkit-and-docs --stat

# Full diff of the Path A server edit (this is the one that touches prod behavior):
git show 5a33fba -- backend/server.py

# Run the 15-test suite one more time to confirm it still passes:
cd backend && python3 -m pytest tests/test_backend_hardening.py -v && cd ..

# When you're happy:
git push -u origin chore/pr4-archive-toolkit-and-docs

# Then open the PR against main (or wip/com-aur-runtime-build, depending on your flow):
gh pr create --base main \
  --title "PR #4 Path A: server spec alignment + archive-governance toolkit" \
  --body-file /mnt/c/Users/softinfo/Documents/EMERAULD/artifacts/2026-04-19-pharos-migration-pr4/_manifest/GAP-pr4-server-spec-alignment.md
```

---

## 8. Final smoke (5 min)

After Railway (or Hetzner) deploy and CF migration:

```bash
# Public surface
curl -I https://pharos-ai.ca
# Expected: 200, CF headers

# Backend health (new contract)
curl -s https://<railway-host>/api/health | jq
# Expected:
# {
#   "status": "ok",
#   "environment": "production",
#   "db_ready": true
# }

# If db_ready is false — not the dnspython bug (guard would log CRITICAL at
# startup); it's a config miss. Check Railway env vars MONGO_URL, DB_NAME,
# and the Atlas IP allow-list.

# Aurora worker
curl -s https://pharos-aurora-worker-prod.<your-account>.workers.dev/health
# Expected: 200
```

If all three 200 and `db_ready:true` → PR #4 is discharged.

---

## What I did NOT do (and why)

- **Did not push the pharos-suite branch** — you review destructive infra changes before they hit a shared remote. Branch is staged at `chore/pr4-archive-toolkit-and-docs` (3 commits) locally.
- **Did not touch Cloudflare** — dashboard auth is yours, not mine. Commands in step 6 are copy-pasteable once you're logged in.
- **Did not rotate the OpenRouter key** — I cannot authenticate to openrouter.ai. Step 1 commands clean up the local bashrc once you've rotated in browser.
- **Did not delete BRAINiaC** — destructive, needed your sign-off. Step 2 is a one-liner.
- **Did not apply Decisions 1/3** — operator-scoped. Scripts exist; pick options first.
- **Did not pick Railway vs Hetzner** — architectural call, yours.

---

## If something goes wrong

- Backend won't start after Path A: the Path A edit is commit `5a33fba`. `git revert 5a33fba` on the branch rolls it back cleanly. Tests locked in the commit will catch regressions on future PRs.
- `/health` breaks a caller you didn't know about: grep that repo for `"healthy"` or `.timestamp` — I only grepped `pharos-suite`. Could exist in `pharos-suite-frontend` sibling repo if one exists.
- CF migration goes sideways: the old `govern-*` resources aren't deleted until step 6c final line. DNS cut can be reverted by pointing the CNAME back at `govern-ai.pages.dev`.

---

## After you finish

Update `EMERAULD/session-state.md`:
- Append outcomes of Decisions 1 and 3.
- Record hosting pick (Railway or Hetzner).
- Record CF migration timestamp and whether old resources were cleaned up.
- Mark "PR #4 spec decision" resolved → Path A.
- Then `git -C /mnt/c/Users/softinfo/Documents/EMERAULD add session-state.md && git commit && git push`.

## Related

- [[migration-govern-to-pharos]]
- [[martin_decision_brief]]
- [[CODEX_PROMPT_SERVER_HARDENING]]
- [[RUN-ORDER]]
- [[README]]
- [[CHANGELOG]]
- [[HISTORY]]
- [[readme]]
- [[changelog]]
- [[02_THESEUS_ARCHIVE]]
