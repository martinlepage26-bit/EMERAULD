# Sanitization Report

Build: `obsidian-agent-vault-2026-04-19`

## Source

The marketplace vault was built from the clean scaffold in:

`raw sources/vault-product-scaffold/`

The optional local runtime scripts were copied from the live personal-assistant scaffold and then sanitized for buyer use.

It was not built from the live EMERAULD `wiki/`, `session-state.md`, PHAROS artifacts, legal notes, or private project notes.

## Included

- Generic starter vault files
- Folder-level README files
- Placeholder `CLAUDE.md`
- One generic raw-note example
- One generic wiki-note example
- Hub templates
- Three reusable workflow guides: synthesis, link review, and archive hygiene
- Buyer-side guide-name customization script
- Buyer-side local runtime installer, query CLI, raw-note watcher, and Windows launcher
- Minimal Obsidian app settings

## Excluded

- EMERAULD notes
- PHAROS operational material
- Legal or institutional files
- API keys, secrets, local paths, account identifiers, session state, private names, logs, runtime storage, and virtualenv contents
- Marketplace credentials

## Sanitization Check

Run before upload:

```bash
rg -n -i "Martin|EMERAULD|BRAINiaC|softinfo|cerebrhoe|Calian|Novartis|pharos-suite|session-state|pharos-ai|consult@|ml@|sk-" artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault
```

Expected result: no matches.

## Related

- [[Governance and PHAROS MOC]]
- [[Obsidian Second Brain Product]]
