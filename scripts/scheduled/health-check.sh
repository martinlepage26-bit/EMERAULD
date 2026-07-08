#!/usr/bin/env bash
# obsidian-health-check — every Sunday 9:00 PM
# Vault health audit: orphans, missing frontmatter, broken links, stale claims.

export OBSIDIAN_VAULT_PATH="/home/martin/EMERAULD"
export PATH="/home/martin/.local/bin:/home/martin/.nvm/versions/node/v22.23.0/bin:$PATH"

VAULT="/home/martin/EMERAULD"
TODAY=$(date +%Y-%m-%d)
LOG="/tmp/obsidian-health.log"

cd "$VAULT" || exit 1

# Run the Python vector store check to get coverage stats
EMBED_STATUS=$(/home/martin/.venvs/emerauld/bin/python3 /home/martin/EMERAULD/scripts/embed.py --check 2>&1)

/home/martin/.local/bin/claude --dangerously-skip-permissions -p "
Read _CLAUDE.md and CLAUDE.md at the vault root first — follow their rules exactly.

TODAY is $TODAY.

Vector store status:
$EMBED_STATUS

Run a vault health check and write a report. Do NOT fix anything — report only.

Checks to run:
1. Orphaned notes — Areas/, Resources/, and wiki/ notes with zero outgoing [[wikilinks]] in their body
2. Missing frontmatter — Areas/, Resources/, and wiki/ notes missing any of: type, tags, status, created, updated
3. Broken links — [[wikilinks]] in Areas/, Resources/, and wiki/ notes pointing to files that do not exist anywhere in the vault (check Areas/, Resources/, wiki/, maps/, projects/, memory/, archive/)
4. Stale active projects — projects/ (top level) and Areas/ notes tagged 'project' with status: active or in-progress and updated: older than 30 days
5. Notes missing preamble — Areas/ and wiki/ notes with no '> For future Claude' blockquote
6. MOC coverage — check if each of the 9 MOCs in maps/ links to notes added in the last 30 days

Write a health report to wiki/Vault Health — ${TODAY}.md:
- Frontmatter: type: wiki, tags: [health, vault], status: active, created: $TODAY, updated: $TODAY
- Preamble: > For future Claude: vault health report for $TODAY. Load to understand structural debt and what needs attention.
- ## Critical (broken links, missing frontmatter on active notes)
- ## Warnings (orphans, stale projects, missing preambles)
- ## Info (MOC coverage gaps)
- ## Vector Store — paste the status above
- ## Related — [[EMERAULD]], [[MCP and Runtime Integration MOC]]

Update VAULT ADDITIONS TRACKER: one line for the health report.
Do not ask questions. Do not modify any existing notes. Stop when done.
" >> "$LOG" 2>&1
STATUS=$?
if [ $STATUS -ne 0 ]; then
  echo "- $TODAY $(date +%H:%M) health-check run FAILED (exit $STATUS) — see Logs/scheduled/health-check-$TODAY.log" >> "$LOGDIR/FAILURES.md"
fi
