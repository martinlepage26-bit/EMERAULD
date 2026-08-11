# Scheduled automation safety contract

The four calendar jobs support a side-effect-free readiness mode:

```bash
scripts/scheduled/morning.sh --dry-run
scripts/scheduled/nightly.sh --dry-run
scripts/scheduled/weekly.sh --dry-run
scripts/scheduled/health-check.sh --dry-run
```

`--dry-run` validates that the configured vault directory exists and prints the
actions the normal run would take. It returns before creating log directories,
running Python, invoking Claude, changing Git or vault state, rebuilding vector
or graph data, or opening a network connection. `EMERAULD_DRY_RUN=1` provides
the same contract for service wrappers.

Normal execution is unchanged unless `--dry-run` or `EMERAULD_DRY_RUN=1` is
explicitly supplied. Tests use a disposable representative vault, sentinel
executables, a byte-level tree fingerprint, and `strace` file/network syscall
inspection:

```bash
python3 -m unittest -v tests/test_scheduled_dry_run.py
```
