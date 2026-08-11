#!/usr/bin/env python3
"""Regression proof for the scheduled automation's non-writing dry-run."""

from __future__ import annotations

import hashlib
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import tempfile
import unittest


REPO = Path(__file__).resolve().parents[1]
SCHEDULED = REPO / "scripts" / "scheduled"
JOBS = ("morning", "nightly", "weekly", "health-check")

NETWORK_SYSCALL = re.compile(
    r"\b(?:socket|socketpair|connect|bind|listen|accept|accept4|sendto|sendmsg|"
    r"sendmmsg|recvfrom|recvmsg|recvmmsg|shutdown)\("
)
MUTATING_FILE_SYSCALL = re.compile(
    r"\b(?:creat|truncate|rename|renameat|renameat2|unlink|unlinkat|mkdir|mkdirat|"
    r"rmdir|link|linkat|symlink|symlinkat|chmod|fchmod|fchmodat|chown|fchown|"
    r"fchownat|lchown|mknod|mknodat|utime|utimes|utimensat)\("
)
WRITE_OPEN = re.compile(r"\bopenat?\([^\n]*(?:O_WRONLY|O_RDWR|O_CREAT|O_TRUNC|O_APPEND)")
FORBIDDEN_EXEC = re.compile(
    r'execve\("[^"]*/(?:claude|python(?:3(?:\.\d+)?)?|git|curl|wget|ssh|scp|rsync)"'
)


def successful_matches(trace_text: str, pattern: re.Pattern[str]) -> list[str]:
    """Return matching syscalls that succeeded; failed open probes cannot mutate."""

    matches = []
    for line in trace_text.splitlines():
        if pattern.search(line) and not re.search(r"\)\s+=\s+-1\b", line):
            matches.append(line)
    return matches


def tree_fingerprint(root: Path) -> str:
    """Hash paths, types, modes, symlink targets, and regular-file bytes."""

    digest = hashlib.sha256()
    for path in sorted(root.rglob("*"), key=lambda item: item.as_posix()):
        relative = path.relative_to(root).as_posix()
        metadata = path.lstat()
        digest.update(relative.encode())
        digest.update(b"\0")
        digest.update(f"{stat.S_IFMT(metadata.st_mode):o}:{stat.S_IMODE(metadata.st_mode):o}".encode())
        digest.update(b"\0")
        if path.is_symlink():
            digest.update(os.readlink(path).encode())
        elif path.is_file():
            with path.open("rb") as handle:
                for block in iter(lambda: handle.read(1024 * 1024), b""):
                    digest.update(block)
        digest.update(b"\0")
    return digest.hexdigest()


class ScheduledDryRunTest(unittest.TestCase):
    maxDiff = None

    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory(prefix="emerauld-dry-run-")
        self.root = Path(self.tempdir.name)
        self.vault = self.root / "vault"
        scheduled = self.vault / "scripts" / "scheduled"
        scheduled.mkdir(parents=True)
        for filename in ("dry-run-lib.sh", *(f"{job}.sh" for job in JOBS)):
            shutil.copy2(SCHEDULED / filename, scheduled / filename)

        # Representative mutable lanes and Git metadata are deliberately present.
        fixtures = {
            "_CLAUDE.md": "fixture policy\n",
            "CLAUDE.md": "fixture instructions\n",
            "session-state.md": "fixture state\n",
            "Logs/scheduled/existing.log": "do not change\n",
            ".vector_store/index.json": '{"fixture": true}\n',
            ".graph_store/summary.json": '{"zero_backlink": 0}\n',
            ".git/HEAD": "ref: refs/heads/main\n",
            ".git/refs/heads/main": "0123456789012345678901234567890123456789\n",
        }
        for relative, content in fixtures.items():
            target = self.vault / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")

        self.guard_marker = self.vault / "forbidden-command-invoked"
        guard = self.root / "forbidden-command"
        guard.write_text(
            "#!/usr/bin/env bash\n"
            'printf "%s\\n" "${0##*/}" >> "$EMERAULD_GUARD_MARKER"\n'
            "exit 97\n",
            encoding="utf-8",
        )
        guard.chmod(0o755)
        self.guard = guard

        self.guard_bin = self.root / "guard-bin"
        self.guard_bin.mkdir()
        for name in ("claude", "python3", "git", "curl", "wget", "ssh", "scp", "rsync"):
            (self.guard_bin / name).symlink_to(guard)

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def test_all_four_dry_runs_are_byte_stable_and_have_no_write_or_network_syscalls(self) -> None:
        strace = shutil.which("strace")
        self.assertIsNotNone(strace, "strace is required for the non-mutation proof")
        baseline = tree_fingerprint(self.vault)

        modes = (("flag", ["--dry-run"], "0"), ("environment", [], "1"))
        for job in JOBS:
            for mode, arguments, environment_flag in modes:
                with self.subTest(job=job, mode=mode):
                    trace = self.root / f"{job}-{mode}.strace"
                    script = self.vault / "scripts" / "scheduled" / f"{job}.sh"
                    environment = os.environ.copy()
                    environment.update(
                        {
                            "EMERAULD_VAULT_PATH": str(self.vault),
                            "EMERAULD_CLAUDE_BIN": str(self.guard),
                            "EMERAULD_PYTHON_BIN": str(self.guard),
                            "EMERAULD_GUARD_MARKER": str(self.guard_marker),
                            "EMERAULD_DRY_RUN": environment_flag,
                            "PATH": f"{self.guard_bin}:{environment['PATH']}",
                        }
                    )
                    result = subprocess.run(
                        [
                            strace,
                            "-f",
                            "-qq",
                            "-o",
                            str(trace),
                            "-e",
                            "trace=%file,%network",
                            str(script),
                            *arguments,
                        ],
                        cwd=self.root,
                        env=environment,
                        text=True,
                        capture_output=True,
                        check=False,
                        timeout=20,
                    )
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertIn(f"job={job}", result.stdout)
                    self.assertIn("write_policy=none", result.stdout)
                    self.assertIn("claude=not-invoked", result.stdout)
                    self.assertIn("git=not-invoked", result.stdout)
                    self.assertIn("network=not-used", result.stdout)

                    trace_text = trace.read_text(encoding="utf-8")
                    network_calls = successful_matches(trace_text, NETWORK_SYSCALL)
                    file_mutations = successful_matches(trace_text, MUTATING_FILE_SYSCALL)
                    write_opens = successful_matches(trace_text, WRITE_OPEN)
                    forbidden_execs = successful_matches(trace_text, FORBIDDEN_EXEC)
                    self.assertEqual(network_calls, [])
                    self.assertEqual(file_mutations, [])
                    self.assertEqual(write_opens, [])
                    self.assertEqual(forbidden_execs, [])
                    self.assertFalse(self.guard_marker.exists(), "a forbidden command was invoked")
                    self.assertEqual(tree_fingerprint(self.vault), baseline)


if __name__ == "__main__":
    unittest.main(verbosity=2)
