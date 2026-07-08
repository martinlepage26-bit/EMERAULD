#!/usr/bin/env bash
# =============================================================
# Personal Assistant — WSL Setup Script
# =============================================================
# Installs: LightRAG API, vault watcher, claude-mem hooks
# Requires: Ubuntu/Debian WSL, Python 3.10+, an Anthropic API key
# Run: bash setup.sh
# =============================================================

set -euo pipefail

AGENT_DIR="$HOME/personal-assistant"
VAULT_DIR="$AGENT_DIR/vault"
VENV="$AGENT_DIR/.venv"
LIGHTRAG_PORT=9621
ANTHROPIC_MODEL="claude-sonnet-4-20250514"

# ── Colors ────────────────────────────────────────────────────
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
BLUE='\033[0;34m'; BOLD='\033[1m'; NC='\033[0m'
info()    { echo -e "${BLUE}[INFO]${NC}  $*"; }
success() { echo -e "${GREEN}[OK]${NC}    $*"; }
warn()    { echo -e "${YELLOW}[WARN]${NC}  $*"; }
error()   { echo -e "${RED}[ERR]${NC}   $*"; exit 1; }
step()    { echo -e "\n${BOLD}▶ $*${NC}"; }

# ─────────────────────────────────────────────────────────────
step "Checking prerequisites"
command -v python3 >/dev/null || error "Python 3 not found. Install with: sudo apt install python3"
command -v pip3   >/dev/null || error "pip3 not found. Install with: sudo apt install python3-pip"
PYVER=$(python3 -c 'import sys; print(sys.version_info[:2] >= (3,10))')
[[ "$PYVER" == "True" ]] || error "Python 3.10+ required"
success "Python $(python3 --version)"

# ─────────────────────────────────────────────────────────────
step "Setting up project directory"
mkdir -p "$AGENT_DIR"/{vault/{raw,wiki,skills,archive},rag,scripts,services,mem}
success "Created $AGENT_DIR"

# ─────────────────────────────────────────────────────────────
step "Creating Python virtual environment"
if [[ ! -d "$VENV" ]]; then
    python3 -m venv "$VENV"
    success "venv created at $VENV"
else
    info "venv already exists, skipping"
fi
source "$VENV/bin/activate"

# ─────────────────────────────────────────────────────────────
step "Installing LightRAG"
pip install --quiet --upgrade pip
pip install --quiet "lightrag-hku[api]"
pip install --quiet watchdog httpx
success "LightRAG installed"

# ─────────────────────────────────────────────────────────────
step "Configuring LightRAG environment"
LIGHTRAG_ENV="$AGENT_DIR/rag/.env"
if [[ ! -f "$LIGHTRAG_ENV" ]]; then
    echo "Enter your Anthropic API key (it will be saved to $LIGHTRAG_ENV):"
    read -rs ANTHROPIC_KEY
    echo
    cat > "$LIGHTRAG_ENV" <<EOF
LLM_BINDING=anthropic
LLM_MODEL=$ANTHROPIC_MODEL
EMBEDDING_BINDING=ollama
EMBEDDING_MODEL=nomic-embed-text
LIGHTRAG_PORT=$LIGHTRAG_PORT
RAG_DIR=$AGENT_DIR/rag/storage
ANTHROPIC_API_KEY=$ANTHROPIC_KEY
EOF
    chmod 600 "$LIGHTRAG_ENV"
    success "Created $LIGHTRAG_ENV"
else
    info ".env already exists, skipping"
fi

# ─────────────────────────────────────────────────────────────
step "Checking for Ollama (embeddings)"
if command -v ollama >/dev/null 2>&1; then
    info "Ollama found — pulling nomic-embed-text..."
    ollama pull nomic-embed-text || warn "Could not pull model — do it manually: ollama pull nomic-embed-text"
else
    warn "Ollama not found. Two options:"
    warn "  1. Install Ollama: curl -fsSL https://ollama.com/install.sh | sh"
    warn "  2. Or switch EMBEDDING_BINDING=anthropic in $LIGHTRAG_ENV"
fi

# ─────────────────────────────────────────────────────────────
step "Copying vault files"
# Only copy if they don't exist (don't overwrite user's data)
for f in CLAUDE.md; do
    DEST="$VAULT_DIR/$f"
    SRC="$(dirname "$0")/../vault/$f"
    if [[ ! -f "$DEST" ]] && [[ -f "$SRC" ]]; then
        cp "$SRC" "$DEST"
        success "Copied $f"
    elif [[ -f "$DEST" ]]; then
        info "$f already exists, skipping"
    fi
done

# ─────────────────────────────────────────────────────────────
step "Installing systemd user services"
SYSTEMD_DIR="$HOME/.config/systemd/user"
mkdir -p "$SYSTEMD_DIR"

# LightRAG service
cat > "$SYSTEMD_DIR/lightrag.service" <<EOF
[Unit]
Description=LightRAG API Server
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

# Vault watcher service
cat > "$SYSTEMD_DIR/vault-watcher.service" <<EOF
[Unit]
Description=Vault Watcher (auto-ingest to LightRAG)
After=lightrag.service

[Service]
Type=simple
WorkingDirectory=$AGENT_DIR
ExecStart=$VENV/bin/python3 $AGENT_DIR/scripts/vault_watcher.py \
    --vault $VAULT_DIR \
    --lightrag-url http://localhost:$LIGHTRAG_PORT
Restart=on-failure
RestartSec=10

[Install]
WantedBy=default.target
EOF

systemctl --user daemon-reload
systemctl --user enable lightrag.service vault-watcher.service
success "Systemd user services installed"

# ─────────────────────────────────────────────────────────────
step "Installing claude-mem hooks for Claude Code"
CLAUDE_CODE_HOOKS="$HOME/.claude/hooks"
mkdir -p "$CLAUDE_CODE_HOOKS"

cat > "$CLAUDE_CODE_HOOKS/session-start.sh" <<'HOOK'
#!/usr/bin/env bash
# SessionStart hook — loads vault context into Claude Code
VAULT="$HOME/personal-assistant/vault"
echo "=== Vault Context ==="
cat "$VAULT/CLAUDE.md"
echo ""
echo "=== Recent raw/ notes ==="
ls -t "$VAULT/raw/"*.md 2>/dev/null | head -5 | xargs -I{} basename {}
HOOK
chmod +x "$CLAUDE_CODE_HOOKS/session-start.sh"
success "Claude Code hooks installed"

# ─────────────────────────────────────────────────────────────
step "Starting services"
systemctl --user start lightrag.service || warn "Could not start lightrag — check: journalctl --user -u lightrag"
sleep 3
systemctl --user start vault-watcher.service || warn "Could not start vault-watcher"

# ─────────────────────────────────────────────────────────────
echo ""
echo -e "${GREEN}${BOLD}════════════════════════════════════════${NC}"
echo -e "${GREEN}${BOLD}  ✅ Personal Assistant ready!${NC}"
echo -e "${GREEN}${BOLD}════════════════════════════════════════${NC}"
echo ""
echo "  Vault:       $VAULT_DIR"
echo "  LightRAG:    http://localhost:$LIGHTRAG_PORT"
echo "  Services:    systemctl --user status lightrag vault-watcher"
echo "  Logs:        journalctl --user -u lightrag -f"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "  1. Edit $VAULT_DIR/CLAUDE.md — add your name, projects, preferences"
echo "  2. Drop notes in $VAULT_DIR/raw/ — they auto-ingest to LightRAG"
echo "  3. Open vault in Obsidian (Windows): point it to $VAULT_DIR"
echo "  4. Run Claude Code from $AGENT_DIR — CLAUDE.md loads automatically"
echo ""
