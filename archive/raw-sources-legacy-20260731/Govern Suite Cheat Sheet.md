---
type: raw-source
aliases: [orphan-raw-2026-05-06-007]
graph_repair: 2026-05-06
---

# Govern Suite Cheat Sheet

## Main paths

- `govern-ai` -> `/home/cerebrhoe/repos/govern-ai`
- `AurorAI` -> `/home/cerebrhoe/repos/AurorAI`
- `CompassAI` -> `/home/cerebrhoe/repos/CompassAI/backend`
- hosting scripts -> `/home/cerebrhoe/repo-hosting`

## Start everything

```bash
/home/cerebrhoe/repo-hosting/start-all.sh
```

## Check everything

```bash
/home/cerebrhoe/repo-hosting/status.sh
```

## Stop everything

```bash
/home/cerebrhoe/repo-hosting/stop-all.sh
```

## Rebuild govern-ai frontend

```bash
/home/cerebrhoe/repo-hosting/build-govern-ai.sh
```

## URLs

- Dashboard -> `http://127.0.0.1:9200/`
- govern-ai frontend -> `http://127.0.0.1:9201/`
- govern-ai backend -> `http://127.0.0.1:9202/health`
- CompassAI API root -> `http://127.0.0.1:9205/api/`
- AurorAI categories -> `http://127.0.0.1:9206/api/categories`
- Public site -> `https://govern-ai.ca`

## Quick health checks

```bash
curl http://127.0.0.1:9202/health
curl http://127.0.0.1:9205/api/
curl http://127.0.0.1:9206/api/categories
```

## AurorAI quick setup

Make sure uploads dir exists:

```bash
mkdir -p /home/cerebrhoe/repos/AurorAI/uploads
```

Set local token for API calls:

```bash
export AURORAI_TOKEN='aurorai-local-dev-token'
```

Upload a file:

```bash
curl -X POST http://127.0.0.1:9206/api/documents/upload \
  -H "Authorization: Bearer $AURORAI_TOKEN" \
  -F "file=@/path/to/document.txt"
```

Extract fields:

```bash
curl -X POST http://127.0.0.1:9206/api/documents/<DOC_ID>/extract \
  -H "Authorization: Bearer $AURORAI_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"document_id":"<DOC_ID>"}'
```

Hand off to CompassAI:

```bash
curl -X POST http://127.0.0.1:9206/api/documents/<DOC_ID>/handoff-to-compassai \
  -H "Authorization: Bearer $AURORAI_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"usecase_id":"<USE_CASE_ID>","producer":"aurorai","artifact_type":"evidence_package"}'
```

## CompassAI quick setup

Register:

```bash
curl -X POST http://127.0.0.1:9205/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"you@example.com","password":"TestPass123!","name":"Your Name","role":"admin"}'
```

Set token after login/register:

```bash
export COMPASS_TOKEN='<JWT>'
```

Create use case:

```bash
curl -X POST http://127.0.0.1:9205/api/v1/use-cases \
  -H "Authorization: Bearer $COMPASS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name":"Invoice review automation",
    "purpose":"Validate invoice extraction and governance handoff",
    "business_owner":"Finance Ops",
    "business_owner_confirmed":true,
    "systems_involved":["AurorAI","CompassAI"],
    "data_categories":["financial","contact"],
    "automation_level":"assistive",
    "decision_impact":"advisory",
    "regulated_domain":false,
    "scale":"team",
    "known_unknowns":["Threshold calibration pending"]
  }'
```

Assess use case:

```bash
curl -X POST http://127.0.0.1:9205/api/v1/use-cases/<USE_CASE_ID>/assess \
  -H "Authorization: Bearer $COMPASS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}'
```

Audit trail:

```bash
curl -H "Authorization: Bearer $COMPASS_TOKEN" \
  http://127.0.0.1:9205/api/v1/use-cases/<USE_CASE_ID>/audit-trail
```

## Logs

```bash
tail -f /home/cerebrhoe/repo-hosting/logs/govern-ai-backend.log
tail -f /home/cerebrhoe/repo-hosting/logs/aurorai.log
tail -f /home/cerebrhoe/repo-hosting/logs/compassai.log
```

## Best daily loop

```bash
/home/cerebrhoe/repo-hosting/start-all.sh
/home/cerebrhoe/repo-hosting/status.sh
/home/cerebrhoe/repo-hosting/build-govern-ai.sh
```

At the end:

```bash
/home/cerebrhoe/repo-hosting/stop-all.sh
```

## Related

- [[Research and Papers MOC]]
- [[AurorA — COMPASSai Input Module]]
