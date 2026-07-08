#!/usr/bin/env bash
# emerauld-inbox-route — event-driven Inbox routing pass (OS build Stage 3).
# Fired by the systemd user path unit emerauld-inbox.path on Inbox/ changes.
# Contract (governance/EMERAULD-OS-SPEC — Event Triggers.md):
#   - drains up to MAX_PER_RUN eligible files per invocation, one headless pass each
#     (PathModified is edge-triggered: events arriving WHILE the service runs are lost,
#     so relying on re-triggering to drain the queue races — proven 2026-07-08 when the
#     second Inbox file was stranded; the bounded internal loop closes that race)
#   - never touches raw lanes, never deletes
#   - failures append to Logs/scheduled/FAILURES.md
#   - a file that fails twice is skipped thereafter (manual-review; loop protection)

export OBSIDIAN_VAULT_PATH="/home/martin/EMERAULD"
export PATH="/home/martin/.local/bin:/home/martin/.nvm/versions/node/v22.23.0/bin:$PATH"

VAULT="/home/martin/EMERAULD"
TODAY=$(date +%Y-%m-%d)
LOGDIR="$VAULT/Logs/scheduled"
mkdir -p "$LOGDIR"
LOG="$LOGDIR/inbox-route-$TODAY.log"
ATTEMPTS="$LOGDIR/inbox-attempts.txt"
LOCK="/tmp/emerauld-inbox-route.lock"

cd "$VAULT" || exit 1
touch "$ATTEMPTS"

exec 9>"$LOCK"
flock -n 9 || exit 0   # another routing pass is running; the next firing catches up

attempts_for() { grep -F -- "$1|" "$ATTEMPTS" | tail -1 | awk -F'|' '{print $2}'; }

pick_target() {
  # Oldest eligible file: top-level Inbox *.md, not README, <2 failed attempts.
  local f base n
  while IFS= read -r f; do
    base=$(basename "$f")
    [ "$base" = "README.md" ] && continue
    n=$(attempts_for "$base"); n=${n:-0}
    [ "$n" -ge 2 ] && continue
    echo "$base"
    return 0
  done < <(ls -tr "$VAULT/Inbox/"*.md 2>/dev/null)
  return 1
}

MAX_PER_RUN=5
ROUTED=0
while [ "$ROUTED" -lt "$MAX_PER_RUN" ]; do

TARGET=$(pick_target) || exit 0   # nothing eligible; quiet exit

echo "=== $(date -u +%FT%TZ) routing: $TARGET" >> "$LOG"

/home/martin/.local/bin/claude --dangerously-skip-permissions --model haiku -p "
Read _CLAUDE.md at the vault root first — follow its rules exactly, especially Section 1 (PARA routing map) and Section 3 (linking rules). Also read Inbox/README.md (routing decision tree).

You are the event-driven Inbox routing pass. Route EXACTLY ONE file and stop: 'Inbox/$TARGET'.

Steps:
1. Read the file. Decide its destination per the PARA map: Areas/PHAROS/, Areas/Writing/, Areas/Personal/, Areas/Lavoie/, Resources/, or (only if genuinely vault-machinery) wiki/. If it is client/financial content requiring operator confirmation per _CLAUDE.md Section 11, do NOT route it — instead append '- $TODAY | Inbox/$TARGET | held: needs operator confirmation' to '_vault/VAULT ADDITIONS TRACKER.md' and stop.
2. Normalize its frontmatter to the vault schema: type, title, tags (meaningful kebab-case only), status: active, domain (pharos/writing/personal/lavoie/reference as fits), created (keep original date/created value if present, else $TODAY), updated (preserve existing; only set $TODAY if you change the body), vault_area, canonical_path (the destination path). Convert upstream keys: date→created; drop ai-first; keep source: mcp if present.
3. Ensure the body has a '> For future Claude:' preamble and at least 2 inline wikilinks to notes that exist (verify with ls/grep). Add a link to the note from the most relevant MOC (Areas/PHAROS/Governance and PHAROS MOC.md, Areas/Personal/Personal and Projects MOC.md, or Areas/Writing/Research and Papers MOC.md).
4. Move the file to its destination (git mv if tracked, plain mv otherwise).
5. Append one line to '_vault/VAULT ADDITIONS TRACKER.md': '- $TODAY | [[<dest-path-without-.md>|<title>]] | routed from Inbox by event-driven pass.'

Hard rules: never write to 'raw sources/' or 'raw/'; never delete anything; do not touch any other Inbox file; do not commit to git. Stop when the one file is routed.
" >> "$LOG" 2>&1
STATUS=$?

if [ $STATUS -ne 0 ]; then
  n=$(attempts_for "$TARGET"); n=${n:-0}
  echo "$TARGET|$((n + 1))" >> "$ATTEMPTS"
  echo "- $TODAY $(date +%H:%M) inbox-route FAILED (exit $STATUS) on '$TARGET' (attempt $((n + 1))) — see Logs/scheduled/inbox-route-$TODAY.log" >> "$LOGDIR/FAILURES.md"
  exit $STATUS
fi

# Success is defined by the file leaving Inbox/; if it stayed (model chose 'held'
# or silently failed), count an attempt so a stuck file cannot loop forever.
if [ -f "$VAULT/Inbox/$TARGET" ]; then
  n=$(attempts_for "$TARGET"); n=${n:-0}
  echo "$TARGET|$((n + 1))" >> "$ATTEMPTS"
  echo "note: '$TARGET' still in Inbox after pass (attempt $((n + 1))/2 before manual-review skip)" >> "$LOG"
fi

ROUTED=$((ROUTED + 1))
done
exit 0
