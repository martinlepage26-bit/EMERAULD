@echo off
setlocal
title Obsidian Agent Vault Agent Console

set "VAULT_WIN=%~dp0"
if "%VAULT_WIN:~-1%"=="\" set "VAULT_WIN=%VAULT_WIN:~0,-1%"

for /f "delims=" %%i in ('wsl wslpath "%VAULT_WIN%"') do set "VAULT_WSL=%%i"

if not defined VAULT_WSL (
    echo Could not translate this folder into a WSL path.
    echo Open WSL manually and run: bash scripts/setup.sh
    pause
    exit /b 1
)

wsl bash -lc "cd \"%VAULT_WSL%\" && if [ -d .venv ]; then source .venv/bin/activate 2>/dev/null; if command -v systemctl >/dev/null 2>&1; then systemctl --user is-active lightrag >/dev/null 2>&1 || systemctl --user start lightrag >/dev/null 2>&1 || true; systemctl --user is-active vault-watcher >/dev/null 2>&1 || systemctl --user start vault-watcher >/dev/null 2>&1 || true; fi; fi; echo; echo 'Vault:        %VAULT_WSL%'; echo 'LightRAG:     http://localhost:9621'; echo 'Setup:        bash scripts/setup.sh'; echo 'Ask:          python3 scripts/ask.py \"your question\"'; echo; exec bash"
