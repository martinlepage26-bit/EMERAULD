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
