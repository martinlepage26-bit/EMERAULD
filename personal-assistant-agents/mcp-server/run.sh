#!/usr/bin/env bash
# Personal-Assistant MCP Server launcher
# Ensures the correct PYTHONPATH for fastmcp and deps before starting the server.

export PYTHONPATH="/home/cerebrhoe/.local/lib/python3.12/site-packages:/usr/lib/python3/dist-packages:${PYTHONPATH}"

exec python3 "$(dirname "$0")/server.py" "$@"
