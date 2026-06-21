# Personal Assistant — WSL Setup

A 24/7 personal assistant combining **Obsidian file-native memory** and **LightRAG graph RAG**, running as background services on WSL.

---

## Architecture

```
personal-assistant/
├── vault/                  ← Your Obsidian vault (open this in Obsidian)
│   ├── CLAUDE.md           ← Agent boot context (edit this first!)
│   ├── raw/                ← Drop notes here → auto-ingested to LightRAG
│   ├── wiki/               ← Synthesized, linked notes (agent navigates here)
│   ├── skills/             ← Reusable agent procedures
│   └── archive/            ← Completed notes
├── rag/
│   ├── .env                ← API keys and config (never commit this)
│   └── storage/            ← LightRAG graph + vector index
├── scripts/
│   ├── setup.sh            ← One-time install script
│   ├── vault_watcher.py    ← Auto-ingestion daemon
│   └── ask.py              ← Terminal query CLI
└── services/               ← Systemd service templates
```

---

## Quick Start

### 1. Run setup
```bash
cd ~/personal-assistant
bash scripts/setup.sh
```

This installs LightRAG, sets up services, and configures Claude Code hooks.

### 2. Edit your vault context
```bash
nano vault/CLAUDE.md
```
Fill in your name, active projects, preferences.

### 3. Open vault in Obsidian
Point Obsidian (Windows) to `\\wsl$\Ubuntu\home\<you>\personal-assistant\vault`

### 4. Ask your assistant
```bash
# From anywhere in WSL:
cd ~/personal-assistant
python3 scripts/ask.py "What are my active projects?"
python3 scripts/ask.py --mode global "Summarize everything I know about health"
python3 scripts/ask.py --vault-only "What skills do I have defined?"
```

---

## How Memory Works

### File-native layer (always on)
Notes in `wiki/` and `skills/` are read directly by Claude Code via `CLAUDE.md`.  
No database. No embeddings. Just files the agent can navigate.

### RAG layer (LightRAG)
Notes dropped in `raw/` are automatically ingested by the vault watcher into LightRAG's graph index.  
This lets you query across hundreds of documents semantically.

**Retrieval modes:**
| Mode | Use when... |
|------|-------------|
| `naive` | Quick keyword scan |
| `local` | Specific note lookup |
| `global` | Topic overview |
| `hybrid` | Best for most questions |
| `mix` | Full context, slower |

---

## Services

```bash
# Check status
systemctl --user status lightrag vault-watcher

# View logs
journalctl --user -u lightrag -f
journalctl --user -u vault-watcher -f

# Restart
systemctl --user restart lightrag vault-watcher

# Stop everything
systemctl --user stop lightrag vault-watcher
```

---

## LightRAG API

Once running, LightRAG is available at `http://localhost:9621`

```bash
# Query
curl -X POST http://localhost:9621/query \
  -H "Content-Type: application/json" \
  -d '{"query": "your question", "mode": "hybrid"}'

# Ingest a document manually
curl -X POST http://localhost:9621/documents/text \
  -H "Content-Type: application/json" \
  -d '{"text": "your content here", "description": "note title"}'

# Check health
curl http://localhost:9621/health
```

---

## Adding a New Note

**Fast (auto-ingest):**
```bash
echo "# Quick Note\nContent here" > ~/personal-assistant/vault/raw/2026-04-14-my-note.md
# The watcher picks it up within seconds
```

**From Claude Code:**
```
Drop a new raw note and ask: "Synthesize the note I just added"
```

---

## Requirements
- WSL (Ubuntu 22.04+)
- Python 3.10+
- Anthropic API key
- Ollama (for local embeddings) OR use `EMBEDDING_BINDING=anthropic` in `.env`

---

## Troubleshooting

**LightRAG won't start:**
```bash
cd ~/personal-assistant/rag
source ../.venv/bin/activate
lightrag-server --port 9621 --working-dir storage
```

**Embeddings failing:**
```bash
# Option A: Install Ollama and pull the model
curl -fsSL https://ollama.com/install.sh | sh
ollama pull nomic-embed-text

# Option B: Use Anthropic embeddings
# Edit rag/.env: EMBEDDING_BINDING=anthropic
```

**WSL services don't survive reboot:**
```bash
# Enable WSL systemd (Ubuntu 22.04+)
echo -e "[boot]\nsystemd=true" | sudo tee /etc/wsl.conf
# Then restart WSL from PowerShell: wsl --shutdown
```

## Related

- [[Research and Papers MOC]]
- [[LightRAG — Graph-Based RAG System]]
