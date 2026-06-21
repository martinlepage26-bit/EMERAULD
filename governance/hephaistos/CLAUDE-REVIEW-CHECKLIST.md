# Claude Review Checklist

Standing audit checklist for reviewing Claude-authored claims, diffs, and closeouts in
this repository.

Use this before accepting "already done," "missing," "pass," or "safe to lint" claims.

---

## Common Miss Patterns

- Requested change is already present on disk.
- Proposed required snippet does not match the exact text in the source file.
- Lint or test tightening is suggested before the underlying docs or code support it.
- Rename drift is missed between live installed skills, repo-local legacy names, and
  authority-doc references.
- A local diff looks plausible, but the docs, lint logic, and final PASS state are not
  coherent together.

---

## Review Pass

1. Check on-disk truth first.
   - Search the exact requested terms in the target docs and the enforcement script.
   - Confirm whether the requested change is already present before proposing edits.

2. Check exact-string fidelity.
   - Verify headings, required snippets, file names, and paths against the literal text
     on disk.
   - Do not accept paraphrase as proof of a passing exact-match lint rule.

3. Separate enforceable now from desired later.
   - Only require snippets or conditions the current docs can satisfy, unless the same
     change also updates those docs.
   - Treat "good future rule" and "rule that should pass today" as different states.

4. Check rename and path drift.
   - Compare live installed skill paths under `~/.codex/skills/` with repo-local skill
     names under `skills/` and authority-doc references.
   - Confirm whether an old name is intentionally still active or is stale drift.

5. Check coherence end-to-end.
   - The source docs, the lint or test logic, and the claimed final status must agree.
   - Run the verification step after writing. Do not stop at a plausible diff.

6. Report residual gaps explicitly.
   - Name what was already complete.
   - Name what changed.
   - Name what still requires upstream doc work.
   - Name any assumptions used to keep the change sound.

---

## Quick Commands

```bash
rg -n "EXACT TERM" /home/cerebrhoe/hephaistos
sed -n '1,220p' /home/cerebrhoe/hephaistos/scripts/lint_authority_chain.py
python3 /home/cerebrhoe/hephaistos/scripts/lint_authority_chain.py
git -C /home/cerebrhoe/hephaistos diff -- path/to/file
```

Prefer exact-string searches before interpretation.

## Related

- [[Research and Papers MOC]]
- [[Ask Vault — EMERAULD Vault Briefing Skill]]
