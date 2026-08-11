---
type: raw-source
aliases: [orphan-raw-2026-05-06-004]
graph_repair: 2026-05-06
---

# Free-First Architecture

## Public product
`govern-ai.ca` is the only public website
`www.govern-ai.ca` redirects to the apex domain
`AurorAI` and `CompassAI` are treated as internal delivery modules, not public standalone products

## Current free setup
- Frontend: Cloudflare Pages
- DNS and redirects: Cloudflare
- Backends: local only for now
- Database and file processing: local only for now

  ## Simple rule
    If it needs a Python server, Mongo, PDF processing, or file uploads, keep it private until we choose one paid host or redesign it for a simpler platform.

## What to tell yourself
1. Keep `govern-ai` public
2. Keep `AurorAI` and `CompassAI` internal
3. Do not create public backend subdomains yet
4. Use one storage plan before exposing backend features

## Storage recommendation
- Use `D1` only for lightweight structured records if we simplify the data mode
        l
- Use `R2` for uploaded files and generated evidence packages
- Do not try to store documents directly in `D1`

## Next clean path
1. Keep building the public product in `govern-ai`
2. Decide later whether `AurorAI` and `CompassAI` stay local, move to one paid
        host, or get redesigned for Cloudflare-native storage and APIs

Hey Dan! So govern-ai.ca is getting real and InfraFabric is gonna be a big part of why it works. I wanted to check in with you honestly before anything goes public — AurorAI and ComPassAI are my own things, but the governance architecture they're built on? That's yours, and I want to say so clearly on the site. Also been thinking about whether there's an actual partnership between us worth naming. What do you think? I was thinking along the lines of:

Governance Architecture

AurorAI and ComPassAI are built on a single constraint: governance documentation is only as credible as the evidence it derives from, and no capability claim in either product exceeds what the underlying infrastructure currently supports. Both products are original creations of Martin Lepage, developed under GovernAI. Their technical architecture and claim-boundary discipline are built on InfraFabric's governance framework, used with permission from Danny Stocker, InfraFabric's owner.

InfraFabric's framework does specific structural work here. It supplies the registry-pinned module status system that prevents capability claims from outrunning deployment reality, the evidence hierarchy that distinguishes what is publicly verifiable from what requires operator configuration, and the fail-closed posture that treats uncertainty as a reason to downgrade claims rather than smooth them over. Where InfraFabric modules are integrated into AurorAI or ComPassAI, each is described at its actual registry status — shipped, preview, or roadmap — and that status is the floor of what can be claimed, not a starting point for negotiation.

The implication is deliberate and non-optional: an AI governance platform that overstates its own capabilities cannot credibly govern the AI systems of others. GovernAI holds itself to the same evidentiary standard it asks of every system it governs.

This is not an accidental design choice. It reflects a shared conviction: that AI governance platforms must hold themselves to the same standard of honesty and auditability they ask of the systems they govern.

## Related

- [[Research and Papers MOC]]
- [[AurorA — COMPASSai Input Module]]
