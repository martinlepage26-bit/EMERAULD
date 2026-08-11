#!/usr/bin/env bash
# Shared, side-effect-free dry-run contract for EMERAULD scheduled automation.

emerauld_parse_scheduled_mode() {
  EMERAULD_SCHEDULED_DRY_RUN=${EMERAULD_DRY_RUN:-0}

  while [ "$#" -gt 0 ]; do
    case "$1" in
      --dry-run)
        EMERAULD_SCHEDULED_DRY_RUN=1
        ;;
      -h | --help)
        printf 'Usage: %s [--dry-run]\n' "${0##*/}"
        printf '  --dry-run  Validate inputs and print the write-capable actions without running them.\n'
        return 2
        ;;
      *)
        printf 'error: unknown argument: %s\n' "$1" >&2
        return 64
        ;;
    esac
    shift
  done

  case "$EMERAULD_SCHEDULED_DRY_RUN" in
    0 | 1) ;;
    *)
      printf 'error: EMERAULD_DRY_RUN must be 0 or 1\n' >&2
      return 64
      ;;
  esac
  return 0
}

emerauld_print_dry_run() {
  local job=$1
  local vault=$2
  shift 2

  if [ ! -d "$vault" ]; then
    printf 'error: vault does not exist: %s\n' "$vault" >&2
    return 66
  fi

  printf 'EMERAULD scheduled dry-run\n'
  printf 'job=%s\n' "$job"
  printf 'vault=%s\n' "$vault"
  printf 'write_policy=none\n'
  printf 'claude=not-invoked\n'
  printf 'python_mutators=not-invoked\n'
  printf 'git=not-invoked\n'
  printf 'network=not-used\n'
  printf 'planned_actions:\n'
  while [ "$#" -gt 0 ]; do
    printf '  - %s\n' "$1"
    shift
  done
}
