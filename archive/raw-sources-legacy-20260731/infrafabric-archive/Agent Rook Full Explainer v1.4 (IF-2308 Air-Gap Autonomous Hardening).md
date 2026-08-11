---
type: raw-source
aliases: [orphan-raw-2026-05-06-001]
graph_repair: 2026-05-06
---

# Agent Rook Full Explainer v1.4 (IF-2308 Air-Gap Autonomous Hardening)

Date: 2026-03-03
Owner: InfraFabric Runtime
Status: preview autonomous operation with enforced air-gap controls (pass_with_risk)
Version lineage: v1.4 supersedes `docs/2306-agent-rook-full-explainer-v1.3-2026-03-03T091100Z.md`.
Debate bundle: `/root/tmp/if_rook_five_lane/IF-2308_2026-03-03T133532Z/` (`quality_gate_summary.json` ok=true, publish-ready=true).

## Who | Why | What | Where | When | How

- Who: executives, operators, implementation engineers, and technical reviewers.
- Why: v1.3 was runtime-correct for bootstrap/mirror, but did not fully encode the newly required offline air-gap control model.
- What: v1.4 adds explicit air-gap startup, probe semantics, closeout enforcement, and sync-path gate hardening.
- Where: `if.rook` runtime profile across startup scripts, compliance probes, and blackboard task controls.
- When: IF-2308 cycle, validated on 2026-03-03 (UTC).
- How: runtime-first patches + 5-lane debate + arbitration + publish-ready gate.

## Runtime Fixes First (Applied)

1. `if_rook_session_start.sh`
- evaluates air-gap intent before bootstrap (`IF_ROOK_AIRGAP_MODE=1` pre-bootstrap).
- passes `--airgap-mode` to capability/compliance probes.

2. `if_rook_capability_bootstrap.py`
- supports `--airgap-mode`.
- marks chat probe as skipped-by-policy without false health success semantics.

3. `if_rook_compliance_probe.py`
- supports `--airgap-mode`.
- adds `chat_probe_executed` gate.
- treats `chat_healthz_ok` as waived in air-gap mode when probe is intentionally skipped.

4. `if_blackboard.py`
- air-gap done-gate checks now run on broader air-gap scope inference, not just result marker text.
- air-gap closeout requires: `airgap_mode_confirmed`, `airgap_attestation_path`, `timestamp_utc`, `sha256`, `verify_command`.
- `sync-from-json` and `sync-from-taskboard` now enforce start/done gates.
- `--allow-noncompliant` now requires `--override-reason` (and optionally `--override-ref`) and persists override metadata in result notes.

## Claim Boundary (v1.4)

What is proven now:
- Rook air-gap requirements are enforced across startup, compliance, and task closeout paths.
- gate checks for done/start now apply to sync import paths.
- debate validation is green (`ok=true`, `ready=true`) with explicit residual risks recorded.

What is bounded now:
- residual adversarial/procurement items remain (`pass_with_risk`) and are declared.
- this is not a GA/certification claim.

What is not claimed:
- universal immunity to all sid-lock identity spoof patterns.
- full procurement-grade trust posture without further signature-gate hardening.

## Machine-Verifiable Checks

```bash
python3 /root/scripts/if_blackboard.py --dry-run create-task \
  --pillar ops --task "offline air-gap verifier" --status done \
  --result "artifact_path=/root/tmp/x verify_command=echo_ok no sub-agents no sessions"
# expected: fail (missing required air-gap fields)

python3 /root/scripts/if_blackboard.py --dry-run create-task \
  --pillar ops --task "offline air-gap verifier" --status done \
  --result "artifact_path=/root/tmp/x verify_command=echo_ok no sub-agents no sessions \
airgap_mode_confirmed=true airgap_attestation_path=/root/tmp/attest.json \
timestamp_utc=2026-03-03T14:15:00Z \
sha256=0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
# expected: pass

python3 /root/scripts/if_blackboard.py --dry-run create-task \
  --pillar ops --task "override audit test" --status done \
  --allow-noncompliant \
  --result "artifact_path=/root/tmp/x verify_command=echo_ok no sub-agents no sessions"
# expected: fail (missing --override-reason)
```

## Open Findings Register (pass_with_risk)

| Finding | Status | Severity | Next action |
|---|---|---|---|
| strict-production gate still env-backed vs runtime proof | Open | P2 | add signed live runtime probe gate |
| path-lock sid ownership uses caller sid string | Open | P2 | bind lock ownership to verified sid+agent identity |
| non-air-gap evidence checker remains heuristic | Open | P2 | migrate to structured closeout evidence schema |
| compliance PASS lacks blackboard ledger signature hard gates | Open | P1 | add tasks/sessions/path-lock signature gates |

## Checksums

| Artifact | sha256 |
|---|---|
| `/root/scripts/if_rook_session_start.sh` | `d99b598ff0024171a4d337956610532a586ceebc624a4c3ca20a8f9deb941632` |
| `/root/scripts/if_rook_capability_bootstrap.py` | `b93734da183fd513e4afc9d25bc873d1676ff4a77e5215dfa06b93dd2fc17477` |
| `/root/scripts/if_rook_compliance_probe.py` | `f59fc19116b1b75951f9ca30267dd73a6dc8a3583b14fda1f6c0847952731f5b` |
| `/root/scripts/if_blackboard.py` | `946a10e0b28636b0676552ef084b000c6887d9e8e8eecc89365e20b1eeb81e05` |
| `IF-2308 quality gate summary` | `9bdd1dbcf186200f7d74295fe45e9d0aa3600561c77fca57298f8b9839358527` |
| `IF-2308 air-gap attestation` | `51db1ae50f231dab270572b506c1b35c0244b58dabe81f97aae28238faa516b2` |

## Artifact Pointers

- `/root/tmp/if_rook_five_lane/IF-2308_2026-03-03T133532Z/quality_gate_summary.json`
- `/root/tmp/if_rook_five_lane/IF-2308_2026-03-03T133532Z/airgap_attestation.IF-2308.json`
- `/root/tmp/if2308_compliance_airgap.json`
- `/root/tmp/if2308_compliance_airgap.md`

## Conclusion

Rook v1.4 adds enforceable air-gap runtime controls validated through a full five-lane debate cycle. Current posture is publish-ready with explicit residual-risk boundaries.

Style Guide: Whitepaper v4.23
Writing Standard Source: `docs/2266-if-whitepapers-bible-v4.23-2026-03-02T120500Z.md`

## Related

- [[Governance and PHAROS MOC]]
- [[PROTOCOLS — Debate and Red-Team Runbook]]
