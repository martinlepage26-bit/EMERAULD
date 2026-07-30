---
type: resource
title: Martin GCE to mtl-01 Access
tags:
- resource
- resources
- codexresume
- tmux
- docs
- detach
- ctrl
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: resources
canonical_path: resources/mtl-01-access.md
backlink_count: 1
backlinks:
- '[[wiki/RESOURCES MOC]]'
---

# Martin GCE to mtl-01 Access

Installed on `martin@pharos-corpus-runner-01`.

Commands:

- `mtl-docs` opens an interactive root shell on `mtl-01` in `/root/docs`.
- `mtl-codexresume` attaches to the existing `codexresume` tmux session on `mtl-01`.

Equivalent manual command:

```bash
ssh -tt mtl-01-docs 'cd /root/docs && tmux attach -t codexresume'
```

Detach from tmux without killing the session with `Ctrl-b d`.

## Related

- [[AI Infrastructure Stack]]
