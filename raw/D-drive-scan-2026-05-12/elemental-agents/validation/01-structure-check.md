# Structure Check

See also [[Manuscript Pipeline MOC]].
## Required counts

- `agents/`: 10 markdown files
- `orchestration/`: 6 markdown files
- `examples/`: 6 markdown files
- `validation/`: 3 markdown files
- Framework root: `README.md`

## Commands

```bash
find elemental-agents -type f | sort
find elemental-agents/agents -maxdepth 1 -type f -name '*.md' | wc -l
find elemental-agents/orchestration -maxdepth 1 -type f -name '*.md' | wc -l
find elemental-agents/examples -maxdepth 1 -type f -name '*.md' | wc -l
find elemental-agents/validation -maxdepth 1 -type f -name '*.md' | wc -l
```

## Pass criteria

All counts match required values and README exists.
