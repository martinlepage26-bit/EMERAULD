---
type: wiki
title: Red Team Handbook — Offensive Security Reference
aliases:
- red team
- RED-HANDBOOK
- offensive security
- penetration testing
tags:
- security
- red-team
- reference
- tooling
- resources
- red-team-handbook-offensive-security-reference-md
- exploitation
- handbook
- recon
- redteam
- offensive
- color-red
status: reference
created: '2026-04-18'
updated: '2026-06-26'
vault_area: Resources
canonical_path: Resources/Red Team Handbook — Offensive Security Reference.md
backlink_count: 4
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[archive/wiki-2026-07-08/Vault Deep Linking Pass — 2026-05-06]]'
- '[[wiki/archive/red-team]]'
---

# Red Team Handbook — Offensive Security Reference

## Summary

A compiled offensive security reference at `/home/cerebrhoe/RED-HANDBOOK.md` covering red team lab setup, reconnaissance, exploitation, post-exploitation, data exfiltration, and emerging AI/LLM red teaming techniques. Assembled from public guides and Feb 2026 AI red-team research. Relevant to the [[PROTOCOLS — Debate and Red-Team Runbook|debate and red-team governance process]] and any authorized security testing contexts.

## Context

Distinct from the governance red-team process in [[PROTOCOLS — Debate and Red-Team Runbook]] — that protocol governs argument-level review of AI outputs. This handbook covers technical offensive security for authorized engagements. Referenced in the HEPHAISTOS skill map as the `$red-team` skill domain. Relevant to [[PHAROS Method — Technical Reference|PHAROS]] in contexts where security review is part of governance (e.g., [[RECURSO — Final Audit and Ethical Review]]).

## Details

### Coverage areas

1. **Lab platform**: Kali/Parrot/BlackArch + VirtualBox/VMware/Proxmox targets; essential toolset (Nmap, BloodHound, CrackMapExec, Impacket, Responder, Evil-WinRM, Kerbrute, Mimikatz)
2. **C2 frameworks**: Cobalt Strike, Sliver, Havoc, Metasploit C2
3. **Recon/enumeration**: Nmap, Amass, Masscan, theHarvester, Recon-ng
4. **Exploitation**: Metasploit, Cobalt Strike beacons, CrackMapExec, BloodHound AD mapping
5. **Post-exploitation**: Meterpreter, scheduled tasks, PowerSploit, PowerShell Empire
6. **Exfiltration/cleanup**: SCP/HTTP server, zip/encrypt, `wevtutil`, log clearing
7. **AI/LLM red teaming**: Co-RedTeam (multi-agent LLM orchestration, 60%+ exploit success rate in Feb 2026 eval), BlackIce (14-tool containerized AI red-team toolkit)
8. **OPSEC**: User agent rotation, scan throttling, C2 encryption, MITRE ATT&CK mapping, evidence folder structure

### Folder structure recommendation

`Recon / Initial Access / Payloads / Credentials / Lateral Movement / Screenshots / Reports / C2 Logs`

### AI red-team highlights

- **Co-RedTeam**: Multi-agent LLMs planning discovery, executing commands, validating results, learning from memory. Evaluated Feb 2026: consistently exceeded 60% exploitation success and 10+ percentage points over baseline in vulnerability detection.
- **BlackIce**: Containerized toolkit (Docker) with 14 reproducible open-source tools for probing LLMs and ML services.

## Key Ideas

- Red teaming differs from pentesting: simulates real adversaries chasing crown jewels, not just reporting bugs
- AI-assisted red teams (Co-RedTeam) now match human red team cycles on standard benchmarks
- OPSEC and evidence documentation are part of the engagement, not optional cleanup

## Open Questions

- Is RED-HANDBOOK.md used in active PHAROS client security reviews?
- Should this be linked from the RECURSO audit framework as a reference source?

## Sources

- `/home/cerebrhoe/RED-HANDBOOK.md`

## Related

- [[PROTOCOLS — Debate and Red-Team Runbook]]
- [[RECURSO — Final Audit and Ethical Review]]
- [[PHAROS Method — Technical Reference]]
- [[Architectural AI Governance — Willis and PBSAI]]
