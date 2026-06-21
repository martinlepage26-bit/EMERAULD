# H3RME3 (Agents SDK)

H3RME3 is a Cloudflare Agents SDK chat agent whose purpose is to operate an Obsidian second-brain workflow (capture → process → connect → maintain) using a PARA structure.

## Dev

```bash
npm install
npm run dev
```

## Deploy

```bash
npm run deploy
```

## Notes

- This agent can generate vault folders/templates/dashboards as Markdown outputs, but it does not have access to your local filesystem. Apply its outputs into your local Obsidian vault (or wire a separate sync layer/tool).
- It also exposes a dispatch-oriented tool for mixed status updates, so client changes, manuscript updates, and daily-log tracking can stay aligned across multiple vault surfaces.
