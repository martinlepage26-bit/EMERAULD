#!/usr/bin/env bash
# Optional local runtime installer for the Obsidian Agent Vault package.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
VAULT_DIR="$AGENT_DIR"
VENV="$AGENT_DIR/.venv"
LIGHTRAG_PORT="${LIGHTRAG_PORT:-9621}"
OPENAI_COMPAT_BASE_URL="${OPENAI_COMPAT_BASE_URL:-https://api.openai.com/v1}"
OPENAI_COMPAT_MODEL="${OPENAI_COMPAT_MODEL:-gpt-4o-mini}"
OPENAI_COMPAT_EMBED_MODEL="${OPENAI_COMPAT_EMBED_MODEL:-text-embedding-3-small}"
LIGHTRAG_ENV="$AGENT_DIR/rag/.env"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m'

info()    { echo -e "${BLUE}[INFO]${NC}  $*"; }
success() { echo -e "${GREEN}[OK]${NC}    $*"; }
warn()    { echo -e "${YELLOW}[WARN]${NC}  $*"; }
error()   { echo -e "${RED}[ERR]${NC}   $*"; exit 1; }
step()    { echo -e "\n${BOLD}> $*${NC}"; }

placeholder_key() {
    local key="${1:-}"
    [[ -z "$key" || "$key" == "your_openai_api_key" || "$key" == "changeme" || "$key" == "replace_me" ]]
}

step "Checking prerequisites"
command -v python3 >/dev/null || error "Python 3 not found. Install it first."
command -v pip3 >/dev/null || error "pip3 not found. Install it first."
PYVER=$(python3 -c 'import sys; print(sys.version_info[:2] >= (3,10))')
[[ "$PYVER" == "True" ]] || error "Python 3.10+ required."
success "Python $(python3 --version)"

step "Preparing runtime directories"
mkdir -p \
    "$AGENT_DIR/raw" \
    "$AGENT_DIR/wiki" \
    "$AGENT_DIR/skills" \
    "$AGENT_DIR/archive" \
    "$AGENT_DIR/templates" \
    "$AGENT_DIR/rag/storage" \
    "$AGENT_DIR/mem" \
    "$HOME/.config/systemd/user"
success "Runtime directories ready"

step "Creating virtual environment"
if [[ ! -d "$VENV" ]]; then
    python3 -m venv "$VENV"
    success "Created $VENV"
else
    info "Virtual environment already exists"
fi
source "$VENV/bin/activate"

step "Installing runtime dependencies"
pip install --quiet --upgrade pip
pip install --quiet "lightrag-hku[api]" watchdog httpx
success "Installed runtime dependencies"

step "Configuring LightRAG"
if [[ ! -f "$LIGHTRAG_ENV" ]]; then
    OPENAI_KEY="${OPENAI_API_KEY:-}"
    if placeholder_key "$OPENAI_KEY"; then
        OPENAI_KEY=""
        echo "Enter the API key for your OpenAI-compatible provider (saved to $LIGHTRAG_ENV):"
        read -rs OPENAI_KEY
        echo
    else
        info "Using OPENAI_API_KEY from the current shell"
    fi

    cat > "$LIGHTRAG_ENV" <<EOF
LLM_BINDING=openai
LLM_BINDING_HOST=$OPENAI_COMPAT_BASE_URL
LLM_BINDING_API_KEY=$OPENAI_KEY
LLM_MODEL=$OPENAI_COMPAT_MODEL
EMBEDDING_BINDING=openai
EMBEDDING_BINDING_HOST=$OPENAI_COMPAT_BASE_URL
EMBEDDING_BINDING_API_KEY=$OPENAI_KEY
EMBEDDING_MODEL=$OPENAI_COMPAT_EMBED_MODEL
LIGHTRAG_PORT=$LIGHTRAG_PORT
RAG_DIR=$AGENT_DIR/rag/storage
OPENAI_API_KEY=$OPENAI_KEY
EOF
    chmod 600 "$LIGHTRAG_ENV"
    success "Created $LIGHTRAG_ENV"
else
    info "Existing LightRAG env found"
fi

if grep -Eq '^OPENAI_API_KEY=(|your_openai_api_key|changeme|replace_me)$' "$LIGHTRAG_ENV"; then
    warn "OPENAI_API_KEY is blank in $LIGHTRAG_ENV. Queries and ingestion will fail until you add a real key."
else
    success "LightRAG credentials are present"
fi

step "Installing user services"
SYSTEMD_DIR="$HOME/.config/systemd/user"

cat > "$SYSTEMD_DIR/lightrag.service" <<EOF
[Unit]
Description=Obsidian Agent Vault LightRAG
After=network.target

[Service]
Type=simple
WorkingDirectory=$AGENT_DIR/rag
EnvironmentFile=$AGENT_DIR/rag/.env
ExecStart=$VENV/bin/lightrag-server --port $LIGHTRAG_PORT --working-dir $AGENT_DIR/rag/storage
Restart=on-failure
RestartSec=10

[Install]
WantedBy=default.target
EOF

cat > "$SYSTEMD_DIR/vault-watcher.service" <<EOF
[Unit]
Description=Obsidian Agent Vault watcher
After=lightrag.service

[Service]
Type=simple
WorkingDirectory=$AGENT_DIR
ExecStart=$VENV/bin/python3 $AGENT_DIR/scripts/vault_watcher.py --vault $VAULT_DIR --lightrag-url http://localhost:$LIGHTRAG_PORT
Restart=on-failure
RestartSec=10

[Install]
WantedBy=default.target
EOF

if command -v systemctl >/dev/null 2>&1; then
    if systemctl --user daemon-reload >/dev/null 2>&1; then
        systemctl --user enable lightrag.service vault-watcher.service >/dev/null 2>&1 || warn "Could not enable services automatically"
        success "Installed user services"
    else
        warn "systemctl --user is unavailable. If you are on WSL, enable systemd and rerun setup."
    fi
else
    warn "systemctl not found. The runtime files are installed, but services were not enabled."
fi

step "Installing optional Claude Code hook"
CLAUDE_HOOK_DIR="$HOME/.claude/hooks"
mkdir -p "$CLAUDE_HOOK_DIR"
cat > "$CLAUDE_HOOK_DIR/session-start.sh" <<EOF
#!/usr/bin/env bash
VAULT="$VAULT_DIR"
echo "=== Vault Context ==="
cat "$VAULT/CLAUDE.md"
echo
echo "=== Recent raw/ notes ==="
ls -t "$VAULT/raw/"*.md 2>/dev/null | head -5 | xargs -I{} basename {}
EOF
chmod +x "$CLAUDE_HOOK_DIR/session-start.sh"
success "Installed Claude Code session-start hook"

step "Starting services"
if command -v systemctl >/dev/null 2>&1 && systemctl --user daemon-reload >/dev/null 2>&1; then
    systemctl --user start lightrag.service >/dev/null 2>&1 || warn "Could not start lightrag.service"
    sleep 2
    systemctl --user start vault-watcher.service >/dev/null 2>&1 || warn "Could not start vault-watcher.service"
else
    warn "Skipping service start because systemctl --user is unavailable"
fi

echo
echo -e "${GREEN}${BOLD}========================================${NC}"
echo -e "${GREEN}${BOLD}  Local runtime ready${NC}"
echo -e "${GREEN}${BOLD}========================================${NC}"
echo
echo "Vault root : $VAULT_DIR"
echo "LightRAG   : http://localhost:$LIGHTRAG_PORT"
echo "Ask        : python3 scripts/ask.py \"your question\""
echo "Logs       : $AGENT_DIR/mem/vault-watcher.log"
echo
echo "Next steps:"
echo "  1. Finish editing CLAUDE.md if you have not done it yet"
echo "  2. Drop notes into raw/"
echo "  3. Use python3 scripts/ask.py to query the runtime"
