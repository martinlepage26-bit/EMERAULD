# Jade

A bounded, local-first AI assistant. It runs on this machine through Ollama, routes only a small read-only command set, and stores session memory locally.

```text
you: what time is it?
Jade: Let me check.
[ran: date]
Tue Jun 30 00:00:00 UTC 2026
```

## Architecture

```text
Input layer
  CLI: jade.py
  Voice stub: voice.py

LLM
  Ollama model: qwen2.5:7b
  Emits prose or one tool tag:
    [TOOL: shell | <command>]

Tool router
  tool_router.py classifies, executes, and audits tool calls.
  Audit log: ~/.jade/audit.log

Memory
  SQLite session store: ~/.jade/memory.db
```

## Install

```bash
ollama pull qwen2.5:7b
pip install ollama
cd ~/jade
python3 -m pytest test_tool_router.py test_prompt_contract.py -v
```

## Use

```bash
cd ~/jade
python3 jade.py
python3 jade.py --resume 20260626T092116Z
python3 jade.py --sessions
```

Inside Jade:

```text
you: what files are in my home directory?
you: what time is it?
you: log
you: memory
you: exit
```

## Tool Rules

Allowed commands:

```text
pwd ls find rg cat date echo wc du file
```

Always blocked:

```text
rm sudo ssh scp curl wget pip npm apt chmod chown mv cp mkdir touch
```

Also blocked: pipes, semicolons, redirects, subshells, path traversal, protected dotdirs, and filenames containing secret-like terms.

## Security Model

1. Read-only first: the allowlist contains introspective, non-mutating commands.
2. Parse before classify: `classify()` uses `shlex.split()` and returns a structured dict.
3. Log everything: accepted and blocked calls are written to `~/.jade/audit.log`.

## Voice

`voice.py` is a capability stub. Run:

```bash
python3 voice.py
```

Full voice requires openWakeWord, an STT backend, sounddevice/numpy, and Piper.

## Files

```text
~/jade/
├── jade.py
├── tool_router.py
├── voice.py
├── test_tool_router.py
├── test_prompt_contract.py
└── README.md

~/.jade/
├── memory.db
└── audit.log
```
