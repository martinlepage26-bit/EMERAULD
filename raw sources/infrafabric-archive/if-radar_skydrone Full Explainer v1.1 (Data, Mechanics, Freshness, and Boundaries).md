---
type: raw-source
aliases: [orphan-raw-2026-05-06-019]
graph_repair: 2026-05-06
---

# if-radar_skydrone Full Explainer v1.1 (Data, Mechanics, Freshness, and Boundaries)

Danny Stocker | ds@infrafabric.io | InfraFabric Research | 2026-03-03
Status: review
Last review date: 2026-03-03
Next checkpoint date: 2026-03-17
Checkpoint scope: freeze a complete Skydrone RAG explainer with exhaustive datasource registry, explicit runtime/update mechanics, and black/white claim boundaries.
Checkpoint pass criteria: (1) all cited live Skydrone endpoints return expected status, (2) datasource inventory totals reconcile to v12 records, (3) update cadence and failure modes are explicit, (4) non-claims remain strict for offline autonomy and universal guarantees.
Evidence `as_of_utc`: 2026-03-03T15:32:00Z
Accountable and responsible approver: Danny Stocker | ds@infrafabric.io
Backup reviewer/operator continuity owner: pending assignment (open continuity risk until named).
LLM-assist disclosure: synthesized and validated with `/rook-020` Codex runtime, using host + container verification on mtl-01.
Style Guide: Whitepaper v4.23
Writing Standard Source: `docs/2266-if-whitepapers-bible-v4.23-2026-03-02T120500Z.md`
Version lineage: v1.1 supersedes `docs/2316-if-radar_skydrone-full-explainer-v1.0-2026-03-03T150445Z.md`; consolidates Skydrone RAG facts previously spread across docs 378/379/380/690/697/698/700/704/900/2135 and runtime inventories.

## Who | Why | What | Where | When | How
This paper explains exactly what Skydrone RAG is today, what data it loads, how answers are built, how freshness is maintained, and where claims stop.

| Dimension | Current answer |
|---|---|
| Who | SkyDrone leadership, operators, engineers, reviewers, and procurement evaluators. |
| Why | Decision quality depends on traceable sources, bounded inference, and update discipline under changing regulation/market context. |
| What | A complete, evidence-backed map of datasource inventory, retrieval behavior, runtime APIs, freshness loops, and non-claims. |
| Where | `skydrone.infrafabric.io`, `/root/docs`, `/root/docs/data`, CT230 runtime paths, and graph snapshots. |
| When | Valid for current review window only; freshness controls determine promotion and downgrade. |
| How | Runtime-first evidence, explicit claim boundary, and fail-closed interpretation of stale or missing controls. |

Public no-login Skydrone surfaces (current check):
- `https://skydrone.infrafabric.io/` -> HTTP `200`
- `https://skydrone.infrafabric.io/static/if-chat/index.html` -> HTTP `200`
- `https://skydrone.infrafabric.io/if/suggested-questions?tenant=skydrone` -> HTTP `200`
- `https://skydrone.infrafabric.io/if/rag-sources?tenant=skydrone` -> HTTP `200`
- `https://skydrone.infrafabric.io/api/v1/models` -> HTTP `401`
- `https://skydrone.infrafabric.io/api/v1/auths/` -> HTTP `401`
- `https://skydrone.infrafabric.io/auth` -> HTTP `200`

## Executive Summary
Skydrone RAG is currently a governed, tenant-scoped retrieval-and-prompt assembly path served at `skydrone.infrafabric.io`.
It is not a free-form web search assistant; it answers from curated and crawled evidence packs plus structured question sets.
It is operationally useful now, but its strongest guarantees are bounded by data freshness, ingestion quality, and dependency health.

What is verified now:
- Live endpoints for suggested questions and RAG source metadata are reachable without login.
- Runtime endpoint exposes per-source file metadata including path, hash, loaded state, and doc refresh TTL.
- Inventory basis exists with `2263` substantive rows across `50` source feeds in v12.
- Graph snapshot includes Skydrone-linked doc/path/url nodes and live URLs in the knowledge graph build.
- Auth perimeter separates public `/if/*` surfaces from protected OpenWebUI model/auth APIs.

What is bounded now:
- Runtime loaded docs are a focused set (`7` declared sources, `5` loaded docs) and do not equal full per-page online retrieval.
- Some radar digest inputs are currently missing in live source metadata (`exists=false`).
- Much of the strongest verification remains host/container-assisted (Tier B), not fully mirrored to immutable no-login packs.

What is non-claim now:
- Full autonomous offline mission operation independent of dependent module health.
- Universal correctness of answers or legal/compliance sufficiency.
- Universal provenance receipt coverage for all runtime-loaded docs (`has_trace` currently false in live source metadata output).
- Automatic daily self-healing freshness across all Skydrone source lanes without operator execution.

## Claim Boundary (Black/White)
### Verified claims
- `skydrone.infrafabric.io/if/suggested-questions` returns tenant-scoped question categories and questions.
- `skydrone.infrafabric.io/if/rag-sources` returns runtime source metadata with TTL, path, hash, and loaded flags.
- Caddy route maps `/if/*` and `/auth*` for `skydrone.infrafabric.io` to CT230 backend (`10.10.10.230:5001`) and root shell to OpenWebUI (`10.10.10.230:8086`).
- Inventory artifacts in `docs/data/if1388_*v12*` provide deduped source/title/quality outputs with explicit totals.
- Hourly `if-knowledge-scope-regression.timer` exists and points to `if_api_knowledge_scope_regression_once.sh`.

### Bounded claims
- Answer quality depends on current loaded document set and corpus quality; stale/missing source lanes reduce reliability.
- Suggested question bank is curated and broad (`98` questions, `14` categories), but does not itself prove runtime grounding quality.
- Graph coverage of Skydrone is currently node-based (docs/paths/urls); no evidence here proves deep semantic edge linkage beyond those nodes.

### Non-claims
- No claim that this stack is certification-complete for EASA/AI Act deployment decisions.
- No claim that all Skydrone answers are always up-to-date; freshness is controlled by explicit jobs and operator-run rebuilds.
- No claim that all runtime docs are if.trace-bound receipts today.
- No claim that offline degraded-mode policy hardening is complete for multi-agent autonomous operations.

## Architecture: How Skydrone RAG Works End-to-End
### Request-to-answer path (runtime control flow)
1. Client sends question via OpenWebUI shell or custom if-chat UI.
2. Reverse proxy routes request by path: `/if/*` and `/auth*` to backend, root shell to OpenWebUI.
3. Tenant is inferred from header/query/token context in backend (`_infer_tenant`).
4. System prompt is selected by tenant (`_tenant_system_prompt`).
5. RAG doc set is resolved for tenant (`_resolve_docs_tenant`, `_docs_for_tenant`).
6. Docs cache is checked; if fresh TTL window is valid, cached docs/meta are reused.
7. If cache is stale or refresh requested, docs are reloaded from configured source file list.
8. For Skydrone, page corpus summary and source inventories are among default document sources.
9. Question text is combined with bounded RAG context (`build_rag_context`).
10. Snippet selection applies ordered docs and tenant-specific snippet priority bias.
11. If Skydrone page corpus is available, rows are sampled with per-source caps to avoid domination.
12. Prompt assembly merges base system contract + bounded context + user message.
13. Model routing resolves alias/backend and sends OpenAI-compatible completion call.
14. Backend returns answer payload (streaming or non-streaming depending endpoint call).
15. Response includes tenant attribution in timing/log structures for per-tenant observability.
16. Operators can run citation-format postchecks with `skydrone_run_queries_with_citations.py`.
17. Reviewers inspect `/if/rag-sources` for currently loaded source files and freshness metadata.
18. Decision language must remain bounded by weakest fresh evidence lane.

### Runtime endpoints and intent
- `/if/suggested-questions`: public tenant-scoped question bank used for guided analysis prompts.
- `/if/rag-sources`: public metadata endpoint for loaded source artifacts and freshness metadata.
- `/v1/chat/completions` and `/api/chat/completions`: OpenAI-compatible answer endpoints through backend model routing.
- `/auth`, `/auth/otp/request`, `/auth/otp/verify`: OTP shell and authentication flow for controlled access surfaces.
- `/api/v1/models` and `/api/v1/auths/`: protected OpenWebUI surfaces (401 unauthenticated in current checks).

### What keeps answers bounded instead of free-form
- Control 1: Tenant-specific prompt contract that enforces confidence framing and source discipline.
- Control 2: Curated question categories that anchor analysis to concrete decision lanes.
- Control 3: Fixed runtime doc source set with explicit metadata exposure via `/if/rag-sources`.
- Control 4: Per-source caps in corpus row selection to reduce single-domain domination.
- Control 5: Snippet ordering and priority bias for Skydrone-specific retrieval relevance.
- Control 6: Operator-side citation checks and scorecards for quality iteration.
- Control 7: Fail-closed interpretation when freshness signals are stale or missing.

## Live Runtime Source Set (`/if/rag-sources`)
Runtime metadata snapshot fields: `docs_refresh_ttl_sec, loaded_at_utc, loaded_docs_count, refresh_requested, resolved_tenant, sources, sources_count, tenant`
Runtime resolved tenant: `skydrone`
Runtime docs refresh TTL (seconds): `120`
Runtime declared sources count: `7`
Runtime loaded docs count: `5`

### Runtime source 1/7: `SKYDRONE_RADAR_DIGEST`
- Path: `/opt/skydrone-intelligence/reports/skydrone_radar_digest.latest.md`
- Exists: `False`
- Loaded: `False`
- Has trace receipt binding: `False`
- SHA256: `(empty)`
- Size bytes: `0`
- Character count: `0`
- mtime_utc: `None`
- Interpretation: `missing lane: fail-conservative interpretation`

### Runtime source 2/7: `SKYDRONE_RADAR_DIGEST_META`
- Path: `/opt/skydrone-intelligence/reports/skydrone_radar_digest.latest.json`
- Exists: `False`
- Loaded: `False`
- Has trace receipt binding: `False`
- SHA256: `(empty)`
- Size bytes: `0`
- Character count: `0`
- mtime_utc: `None`
- Interpretation: `missing lane: fail-conservative interpretation`

### Runtime source 3/7: `IF_CONTEXT_SYSTEM_PROMPT_PACK`
- Path: `/opt/skydrone-intelligence/reports/372-if-context-rag-system-prompt-external-review-pack-v1-2026-02-10.md`
- Exists: `True`
- Loaded: `True`
- Has trace receipt binding: `False`
- SHA256: `98249e2b963f7d9c0e1f1a063792965b952e595df23f1b9ce99dd3ce00a6ba16`
- Size bytes: `34523`
- Character count: `34431`
- mtime_utc: `2026-02-10T05:03:04.870309Z`
- Interpretation: `active evidence lane`

### Runtime source 4/7: `IF_CONTEXT_EXTERNAL_REVIEW_PACK`
- Path: `/opt/skydrone-intelligence/reports/365-if-context-if-blackboard-if-api-external-review-pack-v1-2026-02-09.md`
- Exists: `True`
- Loaded: `True`
- Has trace receipt binding: `False`
- SHA256: `c20c54bd05a97ce74c254d37e3ac1bb39bbca1beaa2bc373009d483c68ae5d6d`
- Size bytes: `40256`
- Character count: `40255`
- mtime_utc: `2026-02-10T05:03:04.119157Z`
- Interpretation: `active evidence lane`

### Runtime source 5/7: `IF_CONTEXT_SOURCE_TITLES`
- Path: `/opt/skydrone-intelligence/reports/if1388_ingested_source_titles.v10.tsv`
- Exists: `True`
- Loaded: `True`
- Has trace receipt binding: `False`
- SHA256: `e10a79cbc74c61f1d0948c1a49871d240810f8388273a48828451d04f61a3f8f`
- Size bytes: `428583`
- Character count: `424293`
- mtime_utc: `2026-02-10T06:35:02.080211Z`
- Interpretation: `active evidence lane`

### Runtime source 6/7: `IF_CONTEXT_SOURCE_SUMMARY`
- Path: `/opt/skydrone-intelligence/reports/if1388_ingested_sources_summary.v10.json`
- Exists: `True`
- Loaded: `True`
- Has trace receipt binding: `False`
- SHA256: `4419470c10510bcce07aa125cd7bc19b34a79511a8876369e7ddff2faf647a6c`
- Size bytes: `16147`
- Character count: `16055`
- mtime_utc: `2026-02-10T06:35:02.082960Z`
- Interpretation: `active evidence lane`

### Runtime source 7/7: `SKYDRONE_PAGES_CORPUS_SUMMARY`
- Path: `/opt/skydrone-intelligence/reports/skydrone_pages_corpus.v1.summary.json`
- Exists: `True`
- Loaded: `True`
- Has trace receipt binding: `False`
- SHA256: `752f2847896444c4cb4278a51ac184dd167449a59919d10ef116630d93bd414d`
- Size bytes: `119`
- Character count: `119`
- mtime_utc: `2026-02-24T17:24:48.137817Z`
- Interpretation: `active evidence lane`

## Datasource Inventory Basis (v12)
Inventory generated_utc: `2026-02-10T11:54:58Z`
Total dedup substantive rows: `2263`
Total source feeds: `50`
Runs scanned in build basis: `38`
Inventory union basis rule: `union_of_runs_scanned_dedup_source_id+url`

Category counts (v12 rows):
- `competitor`: `417` rows
- `defense`: `387` rows
- `press`: `288` rows
- `policy`: `264` rows
- `regulation`: `248` rows
- `funding`: `240` rows
- `research`: `151` rows
- `cinematography`: `135` rows
- `operator`: `107` rows
- `industry`: `23` rows
- `market`: `3` rows

## Full Datasource Feed Register (All 50 Feeds)
Each feed profile below is included because it contributes to Skydrone RAG answer space in the current v12 inventory basis.

### Feed 01/50: `cinematography_stack`
- Category: `cinematography`
- Inventory rows (summary): `86`
- Inventory rows (titles ledger): `135`
- Freshest fetched_utc observed: `2026-02-10T02:12:05Z`
- Quality substantive rows: `135`
- Quality non-substantive rows: `3`
- Top domain #1: `dronisos.com` (`89` rows)
- Top domain #2: `dji.com` (`24` rows)
- Top domain #3: `freeflysystems.com` (`11` rows)
- Dominant user-agent #1: `safari_mobile` (`117` rows)
- Dominant user-agent #2: `(none)` (`18` rows)
- Example title #1: DJI Account
- Example title #2: DJI Agriculture - Drones Better Growth, Better Life
- Coverage role: Civil cinematography operations context and adjacent market continuity.
- Risk note: Risk: civil use-cases may not transfer to defense contexts; keep domain boundaries explicit.
- Update trigger: Trigger refresh on major platform updates affecting capture operations.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 02/50: `dual_use_manufacturers_eu`
- Category: `competitor`
- Inventory rows (summary): `116`
- Inventory rows (titles ledger): `187`
- Freshest fetched_utc observed: `2026-02-10T02:11:16Z`
- Quality substantive rows: `187`
- Quality non-substantive rows: `5`
- Top domain #1: `parrot.com` (`181` rows)
- Top domain #2: `delair.aero` (`1` rows)
- Top domain #3: `quantum-systems.com` (`1` rows)
- Dominant user-agent #1: `safari_mobile` (`187` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: DELAIR – Professional Drones and Sensors for Industry - Delair
- Example title #2: The Future is Unmanned - Quantum Systems
- Coverage role: Competitive landscape and OEM capability tracking for benchmark answers.
- Risk note: Risk: vendor pages drift quickly and can overstate capability; requires citation discipline.
- Update trigger: Trigger rebuild when competitor launches/new product announcements materially change capability map.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 03/50: `dual_use_competitors_recovery`
- Category: `competitor`
- Inventory rows (summary): `80`
- Inventory rows (titles ledger): `104`
- Freshest fetched_utc observed: `2026-02-10T03:15:26Z`
- Quality substantive rows: `104`
- Quality non-substantive rows: `29`
- Top domain #1: `parrot.com` (`97` rows)
- Top domain #2: `airbus.com` (`3` rows)
- Top domain #3: `delair.aero` (`1` rows)
- Dominant user-agent #1: `safari_mobile` (`104` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: DELAIR – Professional Drones and Sensors for Industry - Delair
- Example title #2: The Future is Unmanned - Quantum Systems
- Coverage role: Competitive landscape and OEM capability tracking for benchmark answers.
- Risk note: Risk: vendor pages drift quickly and can overstate capability; requires citation discipline.
- Update trigger: Trigger rebuild when competitor launches/new product announcements materially change capability map.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 04/50: `counter_uas_stack`
- Category: `competitor`
- Inventory rows (summary): `68`
- Inventory rows (titles ledger): `80`
- Freshest fetched_utc observed: `2026-02-10T02:12:37Z`
- Quality substantive rows: `80`
- Quality non-substantive rows: `0`
- Top domain #1: `dedrone.com` (`67` rows)
- Top domain #2: `blighter.com` (`12` rows)
- Top domain #3: `robinradar.com` (`1` rows)
- Dominant user-agent #1: `safari_mobile` (`80` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: Home - Blighter
- Example title #2: Dedrone: Counter-Drone Defense Solutions & Systems
- Coverage role: Competitive landscape and OEM capability tracking for benchmark answers.
- Risk note: Risk: vendor pages drift quickly and can overstate capability; requires citation discipline.
- Update trigger: Trigger rebuild when competitor launches/new product announcements materially change capability map.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 05/50: `competitor_oem_global`
- Category: `competitor`
- Inventory rows (summary): `44`
- Inventory rows (titles ledger): `46`
- Freshest fetched_utc observed: `2026-02-10T03:21:22Z`
- Quality substantive rows: `46`
- Quality non-substantive rows: `6`
- Top domain #1: `leonardo.com` (`32` rows)
- Top domain #2: `aeronautics.leonardo.com` (`1` rows)
- Top domain #3: `cybersecurity.leonardo.com` (`1` rows)
- Dominant user-agent #1: `safari_mobile` (`46` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: Leonardo Aeronautics: Aerostructures, Aircraft and Uncrewed Systems | Aeronautics
- Example title #2: Professional cyber and security governance services | Leonardo - Cyber & Security
- Coverage role: Competitive landscape and OEM capability tracking for benchmark answers.
- Risk note: Risk: vendor pages drift quickly and can overstate capability; requires citation discipline.
- Update trigger: Trigger rebuild when competitor launches/new product announcements materially change capability map.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 06/50: `defense_drone_trend_reports_boost`
- Category: `defense`
- Inventory rows (summary): `117`
- Inventory rows (titles ledger): `119`
- Freshest fetched_utc observed: `2026-02-10T03:29:05Z`
- Quality substantive rows: `119`
- Quality non-substantive rows: `0`
- Top domain #1: `csis.org` (`113` rows)
- Top domain #2: `breakingdefense.com` (`1` rows)
- Top domain #3: `army-technology.com` (`1` rows)
- Dominant user-agent #1: `safari_mobile` (`119` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: unmanned systems Coverage - Breaking Defense
- Example title #2: Page not found - Army Technology
- Coverage role: Defense doctrine, procurement, and conflict-driven operating signal context.
- Risk note: Risk: narrative-heavy sources can inflate certainty; must separate fact vs interpretation.
- Update trigger: Trigger rebuild when major doctrine updates or conflict lessons change operational assumptions.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 07/50: `defense_publications`
- Category: `defense`
- Inventory rows (summary): `117`
- Inventory rows (titles ledger): `121`
- Freshest fetched_utc observed: `2026-02-10T02:14:10Z`
- Quality substantive rows: `121`
- Quality non-substantive rows: `0`
- Top domain #1: `nato.int` (`118` rows)
- Top domain #2: `eda.europa.eu` (`1` rows)
- Top domain #3: `defensenews.com` (`1` rows)
- Dominant user-agent #1: `safari_mobile` (`120` rows)
- Dominant user-agent #2: `(none)` (`1` rows)
- Example title #1: European Defence Agency
- Example title #2: Defense News, Covering the politics, business and technology of defense | Defense News
- Coverage role: Defense doctrine, procurement, and conflict-driven operating signal context.
- Risk note: Risk: narrative-heavy sources can inflate certainty; must separate fact vs interpretation.
- Update trigger: Trigger rebuild when major doctrine updates or conflict lessons change operational assumptions.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 08/50: `defense_publications_recovery`
- Category: `defense`
- Inventory rows (summary): `92`
- Inventory rows (titles ledger): `94`
- Freshest fetched_utc observed: `2026-02-10T02:57:12Z`
- Quality substantive rows: `94`
- Quality non-substantive rows: `0`
- Top domain #1: `nato.int` (`90` rows)
- Top domain #2: `breakingdefense.com` (`1` rows)
- Top domain #3: `eda.europa.eu` (`1` rows)
- Dominant user-agent #1: `safari_mobile` (`94` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: unmanned systems Coverage - Breaking Defense
- Example title #2: European Defence Agency
- Coverage role: Defense doctrine, procurement, and conflict-driven operating signal context.
- Risk note: Risk: narrative-heavy sources can inflate certainty; must separate fact vs interpretation.
- Update trigger: Trigger rebuild when major doctrine updates or conflict lessons change operational assumptions.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 09/50: `ukraine_drone_ops_public`
- Category: `defense`
- Inventory rows (summary): `7`
- Inventory rows (titles ledger): `25`
- Freshest fetched_utc observed: `2026-02-10T11:34:16Z`
- Quality substantive rows: `25`
- Quality non-substantive rows: `0`
- Top domain #1: `breakingdefense.com` (`19` rows)
- Top domain #2: `kyivindependent.com` (`1` rows)
- Top domain #3: `warontherocks.com` (`1` rows)
- Dominant user-agent #1: `(none)` (`18` rows)
- Dominant user-agent #2: `safari_mobile` (`7` rows)
- Example title #1: Breaking Defense - Defense industry news, analysis and commentary
- Example title #2: Drones - The Kyiv Independent
- Coverage role: Defense doctrine, procurement, and conflict-driven operating signal context.
- Risk note: Risk: narrative-heavy sources can inflate certainty; must separate fact vs interpretation.
- Update trigger: Trigger rebuild when major doctrine updates or conflict lessons change operational assumptions.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 10/50: `asia_defense_public_reporting`
- Category: `defense`
- Inventory rows (summary): `3`
- Inventory rows (titles ledger): `24`
- Freshest fetched_utc observed: `2026-02-09T16:42:50Z`
- Quality substantive rows: `24`
- Quality non-substantive rows: `6`
- Top domain #1: `csis.org` (`22` rows)
- Top domain #2: `iiss.org` (`1` rows)
- Top domain #3: `sipri.org` (`1` rows)
- Dominant user-agent #1: `(none)` (`24` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: CSIS | Center for Strategic and International Studies
- Example title #2: The International Institute for Strategic Studies
- Coverage role: Defense doctrine, procurement, and conflict-driven operating signal context.
- Risk note: Risk: narrative-heavy sources can inflate certainty; must separate fact vs interpretation.
- Update trigger: Trigger rebuild when major doctrine updates or conflict lessons change operational assumptions.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 11/50: `retry_sipri`
- Category: `defense`
- Inventory rows (summary): `1`
- Inventory rows (titles ledger): `4`
- Freshest fetched_utc observed: `2026-02-09T17:50:31Z`
- Quality substantive rows: `4`
- Quality non-substantive rows: `6`
- Top domain #1: `sipri.org` (`4` rows)
- Top domain #2: `(none)` (`0` rows)
- Top domain #3: `(none)` (`0` rows)
- Dominant user-agent #1: `(none)` (`4` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: Home | SIPRI
- Example title #2: (none)
- Coverage role: Defense doctrine, procurement, and conflict-driven operating signal context.
- Risk note: Risk: narrative-heavy sources can inflate certainty; must separate fact vs interpretation.
- Update trigger: Trigger rebuild when major doctrine updates or conflict lessons change operational assumptions.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 12/50: `eu_funding_core`
- Category: `funding`
- Inventory rows (summary): `35`
- Inventory rows (titles ledger): `35`
- Freshest fetched_utc observed: `2026-02-09T13:25:11Z`
- Quality substantive rows: `35`
- Quality non-substantive rows: `0`
- Top domain #1: `defence-industry-space.ec.europa.eu` (`32` rows)
- Top domain #2: `culture.ec.europa.eu` (`1` rows)
- Top domain #3: `ec.europa.eu` (`1` rows)
- Dominant user-agent #1: `(none)` (`35` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: Creative Europe - Culture and Creativity
- Example title #2: 2019 calls for proposals: European defence industrial development programme (EDIDP) - Defence Industry and Space
- Coverage role: Public funding and grant opportunity tracking for program strategy.
- Risk note: Risk: calls close quickly; stale eligibility can cause false opportunity claims.
- Update trigger: Trigger refresh at each new call publication window and before bid decisions.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 13/50: `fr_funding_innovation`
- Category: `funding`
- Inventory rows (summary): `32`
- Inventory rows (titles ledger): `32`
- Freshest fetched_utc observed: `2026-02-09T13:26:14Z`
- Quality substantive rows: `32`
- Quality non-substantive rows: `3`
- Top domain #1: `anr.fr` (`32` rows)
- Top domain #2: `(none)` (`0` rows)
- Top domain #3: `(none)` (`0` rows)
- Dominant user-agent #1: `(none)` (`32` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: Open calls and preannouncements | ANR
- Example title #2: Au service de la science | ANR
- Coverage role: Public funding and grant opportunity tracking for program strategy.
- Risk note: Risk: calls close quickly; stale eligibility can cause false opportunity claims.
- Update trigger: Trigger refresh at each new call publication window and before bid decisions.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 14/50: `eu_dual_use_defense_calls`
- Category: `funding`
- Inventory rows (summary): `29`
- Inventory rows (titles ledger): `31`
- Freshest fetched_utc observed: `2026-02-09T13:29:25Z`
- Quality substantive rows: `31`
- Quality non-substantive rows: `3`
- Top domain #1: `nato.int` (`31` rows)
- Top domain #2: `(none)` (`0` rows)
- Top domain #3: `(none)` (`0` rows)
- Dominant user-agent #1: `(none)` (`31` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: North Atlantic Treaty Organization | NATO
- Example title #2: About us
- Coverage role: Public funding and grant opportunity tracking for program strategy.
- Risk note: Risk: calls close quickly; stale eligibility can cause false opportunity claims.
- Update trigger: Trigger refresh at each new call publication window and before bid decisions.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 15/50: `funding_alt_reachable`
- Category: `funding`
- Inventory rows (summary): `24`
- Inventory rows (titles ledger): `24`
- Freshest fetched_utc observed: `2026-02-09T16:19:07Z`
- Quality substantive rows: `24`
- Quality non-substantive rows: `1`
- Top domain #1: `defence-industry-space.ec.europa.eu` (`20` rows)
- Top domain #2: `culture.ec.europa.eu` (`1` rows)
- Top domain #3: `eic.ec.europa.eu` (`1` rows)
- Dominant user-agent #1: `(none)` (`24` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: Creative Europe - Culture and Creativity
- Example title #2: Agenda Cassini - Defence Industry and Space - European Commission
- Coverage role: Public funding and grant opportunity tracking for program strategy.
- Risk note: Risk: calls close quickly; stale eligibility can cause false opportunity claims.
- Update trigger: Trigger refresh at each new call publication window and before bid decisions.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 16/50: `nato_eu_dual_use_programs`
- Category: `funding`
- Inventory rows (summary): `24`
- Inventory rows (titles ledger): `26`
- Freshest fetched_utc observed: `2026-02-09T16:41:32Z`
- Quality substantive rows: `26`
- Quality non-substantive rows: `3`
- Top domain #1: `nato.int` (`26` rows)
- Top domain #2: `(none)` (`0` rows)
- Top domain #3: `(none)` (`0` rows)
- Dominant user-agent #1: `(none)` (`26` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: North Atlantic Treaty Organization | NATO
- Example title #2: About us
- Coverage role: Public funding and grant opportunity tracking for program strategy.
- Risk note: Risk: calls close quickly; stale eligibility can cause false opportunity claims.
- Update trigger: Trigger refresh at each new call publication window and before bid decisions.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 17/50: `fr_eu_funding_depth`
- Category: `funding`
- Inventory rows (summary): `23`
- Inventory rows (titles ledger): `26`
- Freshest fetched_utc observed: `2026-02-09T16:42:52Z`
- Quality substantive rows: `26`
- Quality non-substantive rows: `4`
- Top domain #1: `cnc.fr` (`21` rows)
- Top domain #2: `ec.europa.eu` (`4` rows)
- Top domain #3: `anr.fr` (`1` rows)
- Dominant user-agent #1: `(none)` (`26` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: Appels en cours et à venir | ANR
- Example title #2: EU Funding & Tenders Portal
- Coverage role: Public funding and grant opportunity tracking for program strategy.
- Risk note: Risk: calls close quickly; stale eligibility can cause false opportunity claims.
- Update trigger: Trigger refresh at each new call publication window and before bid decisions.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 18/50: `fr_defense_innovation`
- Category: `funding`
- Inventory rows (summary): `21`
- Inventory rows (titles ledger): `31`
- Freshest fetched_utc observed: `2026-02-09T13:27:14Z`
- Quality substantive rows: `31`
- Quality non-substantive rows: `3`
- Top domain #1: `defense.gouv.fr` (`31` rows)
- Top domain #2: `(none)` (`0` rows)
- Top domain #3: `(none)` (`0` rows)
- Dominant user-agent #1: `(none)` (`31` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: Page d'accueil du ministère des Armées et des Anciens combattants | Ministère des Armées et des Anciens combattants
- Example title #2: Agence de l'innovation de défense | Ministère des Armées et des Anciens combattants
- Coverage role: Public funding and grant opportunity tracking for program strategy.
- Risk note: Risk: calls close quickly; stale eligibility can cause false opportunity claims.
- Update trigger: Trigger refresh at each new call publication window and before bid decisions.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 19/50: `fr_cinema_media_funding`
- Category: `funding`
- Inventory rows (summary): `8`
- Inventory rows (titles ledger): `35`
- Freshest fetched_utc observed: `2026-02-09T13:29:01Z`
- Quality substantive rows: `35`
- Quality non-substantive rows: `0`
- Top domain #1: `culture.gouv.fr` (`28` rows)
- Top domain #2: `cnc.fr` (`7` rows)
- Top domain #3: `(none)` (`0` rows)
- Dominant user-agent #1: `(none)` (`35` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: Soutien à la création cinéma, séries, TV, jeu vidéo | CNC
- Example title #2: Cinema | CNC
- Coverage role: Public funding and grant opportunity tracking for program strategy.
- Risk note: Risk: calls close quickly; stale eligibility can cause false opportunity claims.
- Update trigger: Trigger refresh at each new call publication window and before bid decisions.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 20/50: `china_drone_ecosystem_public`
- Category: `industry`
- Inventory rows (summary): `9`
- Inventory rows (titles ledger): `9`
- Freshest fetched_utc observed: `2026-02-09T16:39:40Z`
- Quality substantive rows: `9`
- Quality non-substantive rows: `12`
- Top domain #1: `ehang.com` (`7` rows)
- Top domain #2: `autelrobotics.com` (`1` rows)
- Top domain #3: `dji.com` (`1` rows)
- Dominant user-agent #1: `(none)` (`9` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: Autel Robotics Enterprise Drone, Quadcopter & UAV for Sale
- Example title #2: DJI - Official Website
- Coverage role: Industry ecosystem trend signal outside strict defense/regulation lanes.
- Risk note: Risk: industry blogs can mix opinion and data; classify confidence conservatively.
- Update trigger: Trigger refresh when ecosystem shifts alter integration assumptions.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 21/50: `asia_drone_industry_shenzhen`
- Category: `industry`
- Inventory rows (summary): `7`
- Inventory rows (titles ledger): `7`
- Freshest fetched_utc observed: `2026-02-09T13:29:03Z`
- Quality substantive rows: `7`
- Quality non-substantive rows: `12`
- Top domain #1: `ehang.com` (`5` rows)
- Top domain #2: `dji.com` (`1` rows)
- Top domain #3: `jouav.com` (`1` rows)
- Dominant user-agent #1: `(none)` (`7` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: DJI - Official Website
- Example title #2: EHang | Autonomous Aerial Vehicle (AAV) Innovator for Urban Air Mobility (UAM)
- Coverage role: Industry ecosystem trend signal outside strict defense/regulation lanes.
- Risk note: Risk: industry blogs can mix opinion and data; classify confidence conservatively.
- Update trigger: Trigger refresh when ecosystem shifts alter integration assumptions.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 22/50: `asia_shenzhen_alt_reachable`
- Category: `industry`
- Inventory rows (summary): `7`
- Inventory rows (titles ledger): `7`
- Freshest fetched_utc observed: `2026-02-09T16:23:14Z`
- Quality substantive rows: `7`
- Quality non-substantive rows: `11`
- Top domain #1: `ehang.com` (`5` rows)
- Top domain #2: `dji.com` (`1` rows)
- Top domain #3: `jouav.com` (`1` rows)
- Dominant user-agent #1: `(none)` (`7` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: DJI - Official Website
- Example title #2: EHang | Autonomous Aerial Vehicle (AAV) Innovator for Urban Air Mobility (UAM)
- Coverage role: Industry ecosystem trend signal outside strict defense/regulation lanes.
- Risk note: Risk: industry blogs can mix opinion and data; classify confidence conservatively.
- Update trigger: Trigger refresh when ecosystem shifts alter integration assumptions.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 23/50: `eu_market_country_nodes`
- Category: `market`
- Inventory rows (summary): `3`
- Inventory rows (titles ledger): `3`
- Freshest fetched_utc observed: `2026-02-10T02:59:35Z`
- Quality substantive rows: `3`
- Quality non-substantive rows: `169`
- Top domain #1: `ec.europa.eu` (`1` rows)
- Top domain #2: `ted.europa.eu` (`1` rows)
- Top domain #3: `lba.de` (`1` rows)
- Dominant user-agent #1: `safari_mobile` (`3` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: EU Funding & Tenders Portal
- Example title #2: Search results - TED
- Coverage role: Macro market framing and country-node context for decision support.
- Risk note: Risk: market snapshots age quickly; require timestamped recency statement.
- Update trigger: Trigger refresh when procurement cycle or geo-market assumptions change.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 24/50: `target_operator_public`
- Category: `operator`
- Inventory rows (summary): `21`
- Inventory rows (titles ledger): `69`
- Freshest fetched_utc observed: `2026-02-10T03:13:08Z`
- Quality substantive rows: `69`
- Quality non-substantive rows: `0`
- Top domain #1: `skydrone-robotics.com` (`68` rows)
- Top domain #2: `airtable.com` (`1` rows)
- Top domain #3: `(none)` (`0` rows)
- Dominant user-agent #1: `safari_mobile` (`69` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: Interface Form - Airtable
- Example title #2: Skydrone Robotics conception et fabrication de drones
- Coverage role: Skydrone-specific operator context and public footprint.
- Risk note: Risk: operator self-description can be marketing-heavy; pair with third-party corroboration.
- Update trigger: Trigger refresh when Skydrone public surfaces materially change services/positioning.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 25/50: `company_history_archive`
- Category: `operator`
- Inventory rows (summary): `18`
- Inventory rows (titles ledger): `25`
- Freshest fetched_utc observed: `2026-02-10T04:31:18Z`
- Quality substantive rows: `25`
- Quality non-substantive rows: `11`
- Top domain #1: `crt.sh` (`21` rows)
- Top domain #2: `web.archive.org` (`4` rows)
- Top domain #3: `(none)` (`0` rows)
- Dominant user-agent #1: `safari_mobile` (`20` rows)
- Dominant user-agent #2: `googlebot` (`5` rows)
- Example title #1: crt.sh | Certificate Search
- Example title #2: crt.sh | CA:295809
- Coverage role: Skydrone-specific operator context and public footprint.
- Risk note: Risk: operator self-description can be marketing-heavy; pair with third-party corroboration.
- Update trigger: Trigger refresh when Skydrone public surfaces materially change services/positioning.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 26/50: `target_operator_legacy_context`
- Category: `operator`
- Inventory rows (summary): `13`
- Inventory rows (titles ledger): `13`
- Freshest fetched_utc observed: `2026-02-10T02:03:06Z`
- Quality substantive rows: `13`
- Quality non-substantive rows: `1`
- Top domain #1: `skydrone.fr` (`13` rows)
- Top domain #2: `(none)` (`0` rows)
- Top domain #3: `(none)` (`0` rows)
- Dominant user-agent #1: `safari_mobile` (`13` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: Vidéo aérienne par drone - Skydrone donne des ailes à vos images
- Example title #2: Contactez-nous – Skydrone
- Coverage role: Skydrone-specific operator context and public footprint.
- Risk note: Risk: operator self-description can be marketing-heavy; pair with third-party corroboration.
- Update trigger: Trigger refresh when Skydrone public surfaces materially change services/positioning.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 27/50: `defense_ai_policy_alt_reachable`
- Category: `policy`
- Inventory rows (summary): `33`
- Inventory rows (titles ledger): `55`
- Freshest fetched_utc observed: `2026-02-10T11:33:54Z`
- Quality substantive rows: `55`
- Quality non-substantive rows: `1`
- Top domain #1: `darpa.mil` (`29` rows)
- Top domain #2: `nist.gov` (`19` rows)
- Top domain #3: `nato.int` (`3` rows)
- Dominant user-agent #1: `safari_mobile` (`36` rows)
- Dominant user-agent #2: `(none)` (`19` rows)
- Example title #1: OECD AI Policy Observatory Portal
- Example title #2: Home | DARPA
- Coverage role: AI/drone policy framing used for governance questions and non-claim boundaries.
- Risk note: Risk: policy summaries can be interpreted as binding law; keep policy/law split explicit.
- Update trigger: Trigger refresh on AI Act delegated acts, NATO policy updates, or national doctrine changes.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 28/50: `fr_ai_defense_policy`
- Category: `policy`
- Inventory rows (summary): `27`
- Inventory rows (titles ledger): `27`
- Freshest fetched_utc observed: `2026-02-09T16:40:50Z`
- Quality substantive rows: `27`
- Quality non-substantive rows: `2`
- Top domain #1: `cyber.gouv.fr` (`25` rows)
- Top domain #2: `defense.gouv.fr` (`1` rows)
- Top domain #3: `sgdsn.gouv.fr` (`1` rows)
- Dominant user-agent #1: `(none)` (`27` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: Au cœur d'un collectif, pour une nation cyber-résiliente — ANSSI
- Example title #2: Les actualités - Page 1 / 8 — ANSSI
- Coverage role: AI/drone policy framing used for governance questions and non-claim boundaries.
- Risk note: Risk: policy summaries can be interpreted as binding law; keep policy/law split explicit.
- Update trigger: Trigger refresh on AI Act delegated acts, NATO policy updates, or national doctrine changes.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 29/50: `korea_drone_policy_industry`
- Category: `policy`
- Inventory rows (summary): `27`
- Inventory rows (titles ledger): `28`
- Freshest fetched_utc observed: `2026-02-09T16:42:22Z`
- Quality substantive rows: `28`
- Quality non-substantive rows: `1`
- Top domain #1: `main.kotsa.or.kr` (`25` rows)
- Top domain #2: `tsum.kotsa.or.kr` (`2` rows)
- Top domain #3: `koti.re.kr` (`1` rows)
- Dominant user-agent #1: `(none)` (`28` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: TS한국교통안전공단
- Example title #2: TS Korea Transportation Safety Authority
- Coverage role: AI/drone policy framing used for governance questions and non-claim boundaries.
- Risk note: Risk: policy summaries can be interpreted as binding law; keep policy/law split explicit.
- Update trigger: Trigger refresh on AI Act delegated acts, NATO policy updates, or national doctrine changes.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 30/50: `japan_drone_policy_industry`
- Category: `policy`
- Inventory rows (summary): `26`
- Inventory rows (titles ledger): `29`
- Freshest fetched_utc observed: `2026-02-09T16:41:04Z`
- Quality substantive rows: `29`
- Quality non-substantive rows: `1`
- Top domain #1: `mlit.go.jp` (`13` rows)
- Top domain #2: `global.jaxa.jp` (`11` rows)
- Top domain #3: `dips-reg.mlit.go.jp` (`2` rows)
- Dominant user-agent #1: `(none)` (`29` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: JAXA | Japan Aerospace Exploration Agency
- Example title #2: JAXA | Board of Directors
- Coverage role: AI/drone policy framing used for governance questions and non-claim boundaries.
- Risk note: Risk: policy summaries can be interpreted as binding law; keep policy/law split explicit.
- Update trigger: Trigger refresh on AI Act delegated acts, NATO policy updates, or national doctrine changes.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 31/50: `ai_law_eu_fr`
- Category: `policy`
- Inventory rows (summary): `23`
- Inventory rows (titles ledger): `23`
- Freshest fetched_utc observed: `2026-02-09T13:33:36Z`
- Quality substantive rows: `23`
- Quality non-substantive rows: `2`
- Top domain #1: `cnil.fr` (`22` rows)
- Top domain #2: `digital-strategy.ec.europa.eu` (`1` rows)
- Top domain #3: `(none)` (`0` rows)
- Dominant user-agent #1: `(none)` (`23` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: AI Act | Shaping Europe’s digital future
- Example title #2: Particulier | CNIL
- Coverage role: AI/drone policy framing used for governance questions and non-claim boundaries.
- Risk note: Risk: policy summaries can be interpreted as binding law; keep policy/law split explicit.
- Update trigger: Trigger refresh on AI Act delegated acts, NATO policy updates, or national doctrine changes.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 32/50: `eu_ai_law_primary`
- Category: `policy`
- Inventory rows (summary): `21`
- Inventory rows (titles ledger): `30`
- Freshest fetched_utc observed: `2026-02-09T16:38:41Z`
- Quality substantive rows: `30`
- Quality non-substantive rows: `0`
- Top domain #1: `digital-strategy.ec.europa.eu` (`19` rows)
- Top domain #2: `artificialintelligenceact.eu` (`10` rows)
- Top domain #3: `eur-lex.europa.eu` (`1` rows)
- Dominant user-agent #1: `(none)` (`30` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: The Act Texts | EU Artificial Intelligence Act
- Example title #2: Shaping Europe’s digital future | Shaping Europe’s digital future
- Coverage role: AI/drone policy framing used for governance questions and non-claim boundaries.
- Risk note: Risk: policy summaries can be interpreted as binding law; keep policy/law split explicit.
- Update trigger: Trigger refresh on AI Act delegated acts, NATO policy updates, or national doctrine changes.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 33/50: `ai_policy_nato_oecd`
- Category: `policy`
- Inventory rows (summary): `10`
- Inventory rows (titles ledger): `22`
- Freshest fetched_utc observed: `2026-02-09T13:34:15Z`
- Quality substantive rows: `22`
- Quality non-substantive rows: `2`
- Top domain #1: `nato.int` (`13` rows)
- Top domain #2: `oecd.ai` (`9` rows)
- Top domain #3: `(none)` (`0` rows)
- Dominant user-agent #1: `(none)` (`22` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: OECD AI Policy Observatory Portal
- Example title #2: North Atlantic Treaty Organization | NATO
- Coverage role: AI/drone policy framing used for governance questions and non-claim boundaries.
- Risk note: Risk: policy summaries can be interpreted as binding law; keep policy/law split explicit.
- Update trigger: Trigger refresh on AI Act delegated acts, NATO policy updates, or national doctrine changes.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 34/50: `us_ai_defense_governance`
- Category: `policy`
- Inventory rows (summary): `2`
- Inventory rows (titles ledger): `28`
- Freshest fetched_utc observed: `2026-02-09T16:41:05Z`
- Quality substantive rows: `28`
- Quality non-substantive rows: `2`
- Top domain #1: `nist.gov` (`27` rows)
- Top domain #2: `whitehouse.gov` (`1` rows)
- Top domain #3: `(none)` (`0` rows)
- Dominant user-agent #1: `(none)` (`28` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: AI Risk Management Framework | NIST
- Example title #2: News – The White House
- Coverage role: AI/drone policy framing used for governance questions and non-claim boundaries.
- Risk note: Risk: policy summaries can be interpreted as binding law; keep policy/law split explicit.
- Update trigger: Trigger refresh on AI Act delegated acts, NATO policy updates, or national doctrine changes.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 35/50: `ai_policy_us_defense`
- Category: `policy`
- Inventory rows (summary): `1`
- Inventory rows (titles ledger): `22`
- Freshest fetched_utc observed: `2026-02-09T13:33:49Z`
- Quality substantive rows: `22`
- Quality non-substantive rows: `3`
- Top domain #1: `nist.gov` (`22` rows)
- Top domain #2: `(none)` (`0` rows)
- Top domain #3: `(none)` (`0` rows)
- Dominant user-agent #1: `(none)` (`22` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: AI Risk Management Framework | NIST
- Example title #2: (none)
- Coverage role: AI/drone policy framing used for governance questions and non-claim boundaries.
- Risk note: Risk: policy summaries can be interpreted as binding law; keep policy/law split explicit.
- Update trigger: Trigger refresh on AI Act delegated acts, NATO policy updates, or national doctrine changes.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 36/50: `competitor_news_trends_boost`
- Category: `press`
- Inventory rows (summary): `128`
- Inventory rows (titles ledger): `139`
- Freshest fetched_utc observed: `2026-02-10T03:25:05Z`
- Quality substantive rows: `139`
- Quality non-substantive rows: `1`
- Top domain #1: `droneii.com` (`61` rows)
- Top domain #2: `dronelife.com` (`53` rows)
- Top domain #3: `suasnews.com` (`21` rows)
- Dominant user-agent #1: `safari_mobile` (`139` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: DroneDJ - Drone news and views covering DJI, Skydio, Parrot and more
- Example title #2: Drone Industry Insights | Global Drone Market Research
- Coverage role: Market movement and recency signal lane to keep answers current.
- Risk note: Risk: press amplification can bias answers; enforce multi-source corroboration.
- Update trigger: Trigger refresh daily or at least every 24h to limit drift from market-moving events.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 37/50: `industry_press`
- Category: `press`
- Inventory rows (summary): `60`
- Inventory rows (titles ledger): `119`
- Freshest fetched_utc observed: `2026-02-10T02:17:08Z`
- Quality substantive rows: `119`
- Quality non-substantive rows: `1`
- Top domain #1: `dronelife.com` (`88` rows)
- Top domain #2: `droneii.com` (`11` rows)
- Top domain #3: `suasnews.com` (`10` rows)
- Dominant user-agent #1: `safari_mobile` (`119` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: Drone Industry Insights | Global Drone Market Research
- Example title #2: Dronelife - The Trusted Source for Drone Industry News
- Coverage role: Market movement and recency signal lane to keep answers current.
- Risk note: Risk: press amplification can bias answers; enforce multi-source corroboration.
- Update trigger: Trigger refresh daily or at least every 24h to limit drift from market-moving events.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 38/50: `industry_press_recovery`
- Category: `press`
- Inventory rows (summary): `29`
- Inventory rows (titles ledger): `30`
- Freshest fetched_utc observed: `2026-02-10T02:58:58Z`
- Quality substantive rows: `30`
- Quality non-substantive rows: `1`
- Top domain #1: `dronelife.com` (`26` rows)
- Top domain #2: `droneii.com` (`1` rows)
- Top domain #3: `suasnews.com` (`1` rows)
- Dominant user-agent #1: `safari_mobile` (`30` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: Drone Industry Insights | Global Drone Market Research
- Example title #2: Dronelife - The Trusted Source for Drone Industry News
- Coverage role: Market movement and recency signal lane to keep answers current.
- Risk note: Risk: press amplification can bias answers; enforce multi-source corroboration.
- Update trigger: Trigger refresh daily or at least every 24h to limit drift from market-moving events.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 39/50: `civil_regulation_global_recovery`
- Category: `regulation`
- Inventory rows (summary): `111`
- Inventory rows (titles ledger): `111`
- Freshest fetched_utc observed: `2026-02-10T03:14:14Z`
- Quality substantive rows: `111`
- Quality non-substantive rows: `15`
- Top domain #1: `caa.co.uk` (`71` rows)
- Top domain #2: `tc.canada.ca` (`37` rows)
- Top domain #3: `consultations.caa.co.uk` (`1` rows)
- Dominant user-agent #1: `safari_mobile` (`111` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: Customer Experience Survey - Survey Questions - Civil Aviation Authority - Citizen Space
- Example title #2: View my registration | UK Civil Aviation Authority
- Coverage role: Regulatory constraints and compliance framing for civil/dual-use operations.
- Risk note: Risk: stale legal text can produce non-compliant guidance; freshness checks are mandatory.
- Update trigger: Trigger immediate refresh on EASA/DGAC/CAA legal updates or advisory amendments.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 40/50: `civil_regulation_eu`
- Category: `regulation`
- Inventory rows (summary): `66`
- Inventory rows (titles ledger): `78`
- Freshest fetched_utc observed: `2026-02-10T02:04:15Z`
- Quality substantive rows: `78`
- Quality non-substantive rows: `2`
- Top domain #1: `transport.ec.europa.eu` (`56` rows)
- Top domain #2: `eur-lex.europa.eu` (`21` rows)
- Top domain #3: `easa.europa.eu` (`1` rows)
- Dominant user-agent #1: `safari_mobile` (`78` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: Directory of legal acts - EUR-Lex
- Example title #2: Treaties currently in force - EUR-Lex
- Coverage role: Regulatory constraints and compliance framing for civil/dual-use operations.
- Risk note: Risk: stale legal text can produce non-compliant guidance; freshness checks are mandatory.
- Update trigger: Trigger immediate refresh on EASA/DGAC/CAA legal updates or advisory amendments.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 41/50: `asia_regulatory_public`
- Category: `regulation`
- Inventory rows (summary): `22`
- Inventory rows (titles ledger): `23`
- Freshest fetched_utc observed: `2026-02-09T13:31:18Z`
- Quality substantive rows: `23`
- Quality non-substantive rows: `2`
- Top domain #1: `mlit.go.jp` (`21` rows)
- Top domain #2: `caac.gov.cn` (`1` rows)
- Top domain #3: `samr.gov.cn` (`1` rows)
- Dominant user-agent #1: `(none)` (`23` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: 中国民用航空局
- Example title #2: Civil Aviation Bureau - MLIT Ministry of Land, Infrastructure, Transport and Tourism
- Coverage role: Regulatory constraints and compliance framing for civil/dual-use operations.
- Risk note: Risk: stale legal text can produce non-compliant guidance; freshness checks are mandatory.
- Update trigger: Trigger immediate refresh on EASA/DGAC/CAA legal updates or advisory amendments.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 42/50: `civil_regulation_fr`
- Category: `regulation`
- Inventory rows (summary): `19`
- Inventory rows (titles ledger): `22`
- Freshest fetched_utc observed: `2026-02-10T02:04:59Z`
- Quality substantive rows: `22`
- Quality non-substantive rows: `29`
- Top domain #1: `sandbox-api.piste.gouv.fr` (`20` rows)
- Top domain #2: `geoportail.gouv.fr` (`1` rows)
- Top domain #3: `service-public.gouv.fr` (`1` rows)
- Dominant user-agent #1: `legifrance_api_v2` (`20` rows)
- Dominant user-agent #2: `safari_mobile` (`1` rows)
- Example title #1: Code de la consommation — article L425-1 — Chapitre V : Dispositions relatives aux aéronefs circulant sans équipage à bord
- Example title #2: Code de l'aviation civile — article D136-2-2 — Section 1 : Règles relatives à la formation exigée des télépilotes qui utilisent des aéronefs civils circulant sans personne à bord à des fins autres que le loisir
- Coverage role: Regulatory constraints and compliance framing for civil/dual-use operations.
- Risk note: Risk: stale legal text can produce non-compliant guidance; freshness checks are mandatory.
- Update trigger: Trigger immediate refresh on EASA/DGAC/CAA legal updates or advisory amendments.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 43/50: `civil_regulation_fr_recovery`
- Category: `regulation`
- Inventory rows (summary): `8`
- Inventory rows (titles ledger): `11`
- Freshest fetched_utc observed: `2026-02-10T11:51:27Z`
- Quality substantive rows: `11`
- Quality non-substantive rows: `183`
- Top domain #1: `lannuaire.service-public.gouv.fr` (`4` rows)
- Top domain #2: `service-public.gouv.fr` (`4` rows)
- Top domain #3: `geoportail.gouv.fr` (`2` rows)
- Dominant user-agent #1: `safari_mobile` (`11` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: Annuaire | Service Public
- Example title #2: Institut français du CHILI - Santiago - Annuaire | Service Public
- Coverage role: Regulatory constraints and compliance framing for civil/dual-use operations.
- Risk note: Risk: stale legal text can produce non-compliant guidance; freshness checks are mandatory.
- Update trigger: Trigger immediate refresh on EASA/DGAC/CAA legal updates or advisory amendments.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 44/50: `civil_regulation_global`
- Category: `regulation`
- Inventory rows (summary): `3`
- Inventory rows (titles ledger): `3`
- Freshest fetched_utc observed: `2026-02-10T11:53:02Z`
- Quality substantive rows: `3`
- Quality non-substantive rows: `68`
- Top domain #1: `faa.gov` (`2` rows)
- Top domain #2: `icao.int` (`1` rows)
- Top domain #3: `(none)` (`0` rows)
- Dominant user-agent #1: `safari_mobile` (`3` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: Airports | Federal Aviation Administration
- Example title #2: From the Flight Deck | Federal Aviation Administration
- Coverage role: Regulatory constraints and compliance framing for civil/dual-use operations.
- Risk note: Risk: stale legal text can produce non-compliant guidance; freshness checks are mandatory.
- Update trigger: Trigger immediate refresh on EASA/DGAC/CAA legal updates or advisory amendments.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 45/50: `asia_research_publishers`
- Category: `research`
- Inventory rows (summary): `14`
- Inventory rows (titles ledger): `29`
- Freshest fetched_utc observed: `2026-02-09T16:42:31Z`
- Quality substantive rows: `29`
- Quality non-substantive rows: `1`
- Top domain #1: `arxiv.org` (`23` rows)
- Top domain #2: `info.arxiv.org` (`4` rows)
- Top domain #3: `ieeexplore.ieee.org` (`1` rows)
- Dominant user-agent #1: `(none)` (`29` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: arXiv.org e-Print archive
- Example title #2: [2602.06949] DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos
- Coverage role: Primary research material for technical and evidence-strength responses.
- Risk note: Risk: abstract-only entries can hide method limits; cite primary source before conclusions.
- Update trigger: Trigger refresh when key benchmark/paper updates appear in tracked feeds.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 46/50: `asia_research_publications`
- Category: `research`
- Inventory rows (summary): `11`
- Inventory rows (titles ledger): `24`
- Freshest fetched_utc observed: `2026-02-09T13:29:28Z`
- Quality substantive rows: `24`
- Quality non-substantive rows: `1`
- Top domain #1: `arxiv.org` (`13` rows)
- Top domain #2: `frontiersin.org` (`6` rows)
- Top domain #3: `info.arxiv.org` (`4` rows)
- Dominant user-agent #1: `(none)` (`24` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: arXiv.org e-Print archive
- Example title #2: Robotics
- Coverage role: Primary research material for technical and evidence-strength responses.
- Risk note: Risk: abstract-only entries can hide method limits; cite primary source before conclusions.
- Update trigger: Trigger refresh when key benchmark/paper updates appear in tracked feeds.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 47/50: `papers_arxiv_uas`
- Category: `research`
- Inventory rows (summary): `11`
- Inventory rows (titles ledger): `25`
- Freshest fetched_utc observed: `2026-02-09T13:32:23Z`
- Quality substantive rows: `25`
- Quality non-substantive rows: `0`
- Top domain #1: `arxiv.org` (`21` rows)
- Top domain #2: `info.arxiv.org` (`4` rows)
- Top domain #3: `(none)` (`0` rows)
- Dominant user-agent #1: `(none)` (`25` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: arXiv.org e-Print archive
- Example title #2: [2602.06949] DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos
- Coverage role: Primary research material for technical and evidence-strength responses.
- Risk note: Risk: abstract-only entries can hide method limits; cite primary source before conclusions.
- Update trigger: Trigger refresh when key benchmark/paper updates appear in tracked feeds.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 48/50: `papers_hal_open`
- Category: `research`
- Inventory rows (summary): `9`
- Inventory rows (titles ledger): `24`
- Freshest fetched_utc observed: `2026-02-09T13:32:41Z`
- Quality substantive rows: `24`
- Quality non-substantive rows: `1`
- Top domain #1: `hal.science` (`17` rows)
- Top domain #2: `about.hal.science` (`3` rows)
- Top domain #3: `api.archives-ouvertes.fr` (`2` rows)
- Dominant user-agent #1: `(none)` (`24` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: Données personnelles - About HAL
- Example title #2: About HAL
- Coverage role: Primary research material for technical and evidence-strength responses.
- Risk note: Risk: abstract-only entries can hide method limits; cite primary source before conclusions.
- Update trigger: Trigger refresh when key benchmark/paper updates appear in tracked feeds.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 49/50: `papers_open_access_journals`
- Category: `research`
- Inventory rows (summary): `3`
- Inventory rows (titles ledger): `24`
- Freshest fetched_utc observed: `2026-02-09T13:33:25Z`
- Quality substantive rows: `24`
- Quality non-substantive rows: `1`
- Top domain #1: `zenodo.org` (`17` rows)
- Top domain #2: `frontiersin.org` (`6` rows)
- Top domain #3: `jstage.jst.go.jp` (`1` rows)
- Dominant user-agent #1: `(none)` (`24` rows)
- Dominant user-agent #2: `(none)` (`0` rows)
- Example title #1: Frontiers in Robotics and AI
- Example title #2: J-STAGE Home
- Coverage role: Primary research material for technical and evidence-strength responses.
- Risk note: Risk: abstract-only entries can hide method limits; cite primary source before conclusions.
- Update trigger: Trigger refresh when key benchmark/paper updates appear in tracked feeds.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

### Feed 50/50: `research_metadata_apis`
- Category: `research`
- Inventory rows (summary): `1`
- Inventory rows (titles ledger): `25`
- Freshest fetched_utc observed: `2026-02-10T11:35:58Z`
- Quality substantive rows: `25`
- Quality non-substantive rows: `0`
- Top domain #1: `zenodo.org` (`22` rows)
- Top domain #2: `api.crossref.org` (`1` rows)
- Top domain #3: `api.openalex.org` (`1` rows)
- Dominant user-agent #1: `(none)` (`21` rows)
- Dominant user-agent #2: `safari_mobile` (`4` rows)
- Example title #1: Search results
- Example title #2: (none)
- Coverage role: Primary research material for technical and evidence-strength responses.
- Risk note: Risk: abstract-only entries can hide method limits; cite primary source before conclusions.
- Update trigger: Trigger refresh when key benchmark/paper updates appear in tracked feeds.
- Retrieval boundary: this feed can support bounded evidence statements but not universal truth guarantees.
- Claim boundary note: if this feed is stale/missing, related claims must downgrade to conservative wording.

## Domain Distribution Register (Top 119 domains in v12 rows)
This register shows where the crawler-derived title inventory is concentrated; it is a drift and dominance visibility control.
- `nato.int`: `281` rows
- `parrot.com`: `279` rows
- `dronelife.com`: `167` rows
- `csis.org`: `136` rows
- `dronisos.com`: `89` rows
- `droneii.com`: `73` rows
- `caa.co.uk`: `71` rows
- `nist.gov`: `68` rows
- `skydrone-robotics.com`: `68` rows
- `dedrone.com`: `67` rows
- `arxiv.org`: `57` rows
- `transport.ec.europa.eu`: `56` rows
- `defence-industry-space.ec.europa.eu`: `52` rows
- `zenodo.org`: `39` rows
- `tc.canada.ca`: `37` rows
- `mlit.go.jp`: `34` rows
- `anr.fr`: `33` rows
- `suasnews.com`: `32` rows
- `leonardo.com`: `32` rows
- `defense.gouv.fr`: `32` rows
- `darpa.mil`: `29` rows
- `cnc.fr`: `29` rows
- `dji.com`: `28` rows
- `culture.gouv.fr`: `28` rows
- `cyber.gouv.fr`: `25` rows
- `main.kotsa.or.kr`: `25` rows
- `cnil.fr`: `22` rows
- `eur-lex.europa.eu`: `22` rows
- `crt.sh`: `21` rows
- `breakingdefense.com`: `21` rows
- `digital-strategy.ec.europa.eu`: `20` rows
- `sandbox-api.piste.gouv.fr`: `20` rows
- `ehang.com`: `18` rows
- `hal.science`: `17` rows
- `skydrone.fr`: `13` rows
- `oecd.ai`: `12` rows
- `info.arxiv.org`: `12` rows
- `frontiersin.org`: `12` rows
- `unmannedairspace.info`: `12` rows
- `blighter.com`: `12` rows
- `freeflysystems.com`: `11` rows
- `global.jaxa.jp`: `11` rows
- `artificialintelligenceact.eu`: `10` rows
- `sipri.org`: `6` rows
- `ec.europa.eu`: `6` rows
- `service-public.gouv.fr`: `5` rows
- `lannuaire.service-public.gouv.fr`: `4` rows
- `web.archive.org`: `4` rows
- `airbus.com`: `4` rows
- `defensenews.com`: `4` rows
- `iiss.org`: `3` rows
- `geoportail.gouv.fr`: `3` rows
- `delair.aero`: `3` rows
- `quantum-systems.com`: `3` rows
- `tekever.com`: `3` rows
- `about.hal.science`: `3` rows
- `jouav.com`: `2` rows
- `jstage.jst.go.jp`: `2` rows
- `ag.dji.com`: `2` rows
- `enterprise.dji.com`: `2` rows
- `viewpoints.dji.com`: `2` rows
- `we.dji.com`: `2` rows
- `faa.gov`: `2` rows
- `eda.europa.eu`: `2` rows
- `janes.com`: `2` rows
- `schiebel.net`: `2` rows
- `culture.ec.europa.eu`: `2` rows
- `eic.ec.europa.eu`: `2` rows
- `dips-reg.mlit.go.jp`: `2` rows
- `ossportal.dips.mlit.go.jp`: `2` rows
- `tsum.kotsa.or.kr`: `2` rows
- `api.archives-ouvertes.fr`: `2` rows
- `caac.gov.cn`: `1` rows
- `samr.gov.cn`: `1` rows
- `ieeexplore.ieee.org`: `1` rows
- `openalex.org`: `1` rows
- `autelrobotics.com`: `1` rows
- `account.dji.com`: `1` rows
- `my.dji.com`: `1` rows
- `store.dji.com`: `1` rows
- `easa.europa.eu`: `1` rows
- `vie-publique.fr`: `1` rows
- `icao.int`: `1` rows
- `consultations.caa.co.uk`: `1` rows
- `register-drones.caa.co.uk`: `1` rows
- `secweb.tc.canada.ca`: `1` rows
- `dronedj.com`: `1` rows
- `dronexl.co`: `1` rows
- `uasvision.com`: `1` rows
- `aeronautics.leonardo.com`: `1` rows
- `cybersecurity.leonardo.com`: `1` rows
- `electronics.leonardo.com`: `1` rows
- `helicopters.leonardo.com`: `1` rows
- `space.leonardo.com`: `1` rows
- `anduril.com`: `1` rows
- `skydio.com`: `1` rows
- `robinradar.com`: `1` rows
- `federalregister.gov`: `1` rows
- `army-technology.com`: `1` rows
- `navalnews.com`: `1` rows
- `wingcopter.com`: `1` rows
- `thalesgroup.com`: `1` rows
- `ted.europa.eu`: `1` rows
- `lba.de`: `1` rows
- `sgdsn.gouv.fr`: `1` rows
- `europe-en-france.gouv.fr`: `1` rows
- `thedefensepost.com`: `1` rows
- `jaxa.jp`: `1` rows
- `koti.re.kr`: `1` rows
- `cas.ccsd.cnrs.fr`: `1` rows
- `monitor.hal.science`: `1` rows
- `api.crossref.org`: `1` rows
- `api.openalex.org`: `1` rows
- `export.arxiv.org`: `1` rows
- `airtable.com`: `1` rows
- `kyivindependent.com`: `1` rows
- `warontherocks.com`: `1` rows
- `kyivpost.com`: `1` rows
- `whitehouse.gov`: `1` rows

## Suggested Question Bank (`/if/suggested-questions`)
Tenant: `skydrone`
Categories: `14`
Questions: `98`
Question category counts:
- `Son entreprise d'abord`: `8` questions
- `Concurrents directs`: `10` questions
- `Réglementation française`: `6` questions
- `Réglementation UE et internationale`: `6` questions
- `Marché défense et doctrine`: `8` questions
- `Financements et achats publics`: `6` questions
- `Stratégie transversale`: `6` questions
- `Questions pivot vers la gouvernance`: `10` questions
- `Intégration SkyDrone x InfraFabric (expliqueurs 600+)`: `8` questions
- `if.api : intégrations partenaires et limites de promesse`: `6` questions
- `if.security et if.trace : preuve, contrôle et falsification`: `6` questions
- `if.gov, if.switchboard et agent.rook : décisions sous contrainte`: `6` questions
- `if.context : continuité mission et budget de contexte`: `6` questions
- `Déploiement civil-défense : scénarios et résilience`: `6` questions

Full question register (all 98 questions):
- Q01 | Son entreprise d'abord | #1: Quels services Skydrone propose-t-elle actuellement selon son site web public ?
- Q02 | Son entreprise d'abord | #2: Comment le positionnement public de Skydrone diffère-t-il entre son site web et son activité sur LinkedIn ?
- Q03 | Son entreprise d'abord | #3: Qu'est-ce que Skydrone Robotics et quel est son lien avec l'activité initiale de Skydrone en photographie aérienne ?
- Q04 | Son entreprise d'abord | #4: Quels signaux pertinents pour le secteur de la défense apparaissent dans les communications externes publiques de Skydrone ?
- Q05 | Son entreprise d'abord | #5: Quels marchés verticaux Skydrone dessert-elle actuellement selon ses supports publics ?
- Q06 | Son entreprise d'abord | #6: Skydrone entretient-elle des partenariats ou relations clients visibles publiquement dans le secteur de la défense ?
- Q07 | Son entreprise d'abord | #7: Quelles capacités techniques Skydrone met-elle en avant pour les opérations de drones en direct et en retransmission ?
- Q08 | Son entreprise d'abord | #8: Comment le positionnement public actuel de Skydrone se compare-t-il à ce qu'un évaluateur en achats de défense rechercherait ?
- Q09 | Concurrents directs | #1: Quels sont les principaux fabricants européens de drones à double usage et quelles sont leurs positions sur le marché ?
- Q10 | Concurrents directs | #2: Que propose Delair et comment se positionne-t-elle sur le marché des drones professionnels ?
- Q11 | Concurrents directs | #3: Quelle est la gamme de produits actuelle de Quantum Systems et quels marchés cible-t-elle ?
- Q12 | Concurrents directs | #4: Comment TEKEVER se positionne-t-elle dans les domaines des drones de défense et maritimes ?
- Q13 | Concurrents directs | #5: Quel est le portefeuille de drones et systèmes sans équipage de Leonardo ?
- Q14 | Concurrents directs | #6: Comment l'activité de drones professionnels de Parrot se compare-t-elle à ses origines grand public ?
- Q15 | Concurrents directs | #7: Quelles entreprises de contre-mesures anti-drones opèrent en Europe et quelles solutions proposent-elles ?
- Q16 | Concurrents directs | #8: Comment fonctionne la technologie de contre-drones de Dedrone et qui sont ses clients ?
- Q17 | Concurrents directs | #9: Quelle est la position de Blighter sur le marché des contre-mesures anti-drones ?
- Q18 | Concurrents directs | #10: Comment l'écosystème de drones professionnels et agricoles de DJI se compare-t-il à celui de ses concurrents européens ?
- Q19 | Réglementation française | #1: Quelles sont les exigences légales actuelles en France pour les opérations commerciales de drones ?
- Q20 | Réglementation française | #2: Que prévoit la loi française en matière de formation et de certification des télépilotes ?
- Q21 | Réglementation française | #3: Quelles sont les dispositions légales françaises spécifiques régissant les aéronefs sans équipage — citez les articles pertinents du code ?
- Q22 | Réglementation française | #4: Comment le cadre réglementaire français pour les drones se compare-t-il au cadre européen de l'EASA ?
- Q23 | Réglementation française | #5: Quelles restrictions existent pour les opérations de drones à proximité des aéroports et des espaces aériens réglementés en France ?
- Q24 | Réglementation française | #6: Quelle est la position actuelle de la France concernant les opérations de drones en BVLOS ?
- Q25 | Réglementation UE et internationale | #1: Quels systèmes d'IA la loi européenne sur l'IA classe-t-elle comme à haut risque et comment cela s'applique-t-il aux drones autonomes ?
- Q26 | Réglementation UE et internationale | #2: Quel est le cadre actuel de l'EASA pour les opérations de drones dans la catégorie spécifique ?
- Q27 | Réglementation UE et internationale | #3: Comment la réglementation japonaise sur les drones se compare-t-elle à celle de l'UE pour les opérations commerciales ?
- Q28 | Réglementation UE et internationale | #4: Quelle est l'approche réglementaire de la Corée du Sud en matière d'opérations de drones et en quoi diffère-t-elle de celle de l'Europe ?
- Q29 | Réglementation UE et internationale | #5: Quelles sont les exigences actuelles de la CAA britannique pour les opérateurs de drones après le Brexit ?
- Q30 | Réglementation UE et internationale | #6: Quelles normes ou cadres internationaux existent pour les opérations de drones autonomes ?
- Q31 | Marché défense et doctrine | #1: Quelles sont les positions actuelles de l'OTAN sur les systèmes autonomes et le contrôle humain significatif ?
- Q32 | Marché défense et doctrine | #2: Quelles priorités l'Agence de l'Innovation de Défense française accorde-t-elle actuellement à la technologie des drones ?
- Q33 | Marché défense et doctrine | #3: Comment les drones sont-ils utilisés dans le conflit en Ukraine selon les rapports publics ?
- Q34 | Marché défense et doctrine | #4: Quelles leçons tirées des opérations de drones en Ukraine sont pertinentes pour les fabricants européens de drones de défense ?
- Q35 | Marché défense et doctrine | #5: Qu'est-ce que le programme ACE de la DARPA et que révèle-t-il sur la direction des systèmes autonomes aux États-Unis ?
- Q36 | Marché défense et doctrine | #6: Que requiert le cadre de gestion des risques liés à l'IA du NIST et comment s'applique-t-il aux systèmes autonomes de défense ?
- Q37 | Marché défense et doctrine | #7: Comment l'Agence européenne de défense aborde-t-elle le développement de la technologie des drones ?
- Q38 | Marché défense et doctrine | #8: Quels signaux publics d'achats de défense existent pour les capacités de essaims de drones autonomes en Europe ?
- Q39 | Financements et achats publics | #1: Quels programmes de financement de l'UE sont actuellement disponibles pour la R&D en matière de drones de défense ?
- Q40 | Financements et achats publics | #2: Qu'est-ce que l'EDIDP et quels types de projets de drones a-t-il financés ?
- Q41 | Financements et achats publics | #3: Quels appels à projets de l'ANR sont pertinents pour les systèmes autonomes ou la technologie des drones ?
- Q42 | Financements et achats publics | #4: Existe-t-il des programmes de financement européens ou français soutenant les technologies de drones à double usage civilo-militaire ?
- Q43 | Financements et achats publics | #5: Quels programmes OTAN Science pour la Paix et la Sécurité sont pertinents pour la technologie des drones ?
- Q44 | Financements et achats publics | #6: Quels financements Creative Europe ou CNC pourraient s'appliquer à l'innovation en matière de cinématographie par drone ?
- Q45 | Stratégie transversale | #1: Quelle architecture de gouvernance un fabricant européen de drones de défense devrait-il adopter pour se conformer à la fois à la loi européenne sur l'IA et aux principes de l'OTAN sur les systèmes autonomes ?
- Q46 | Stratégie transversale | #2: Comment les capacités actuelles de contre-mesures anti-drones affectent-elles la viabilité opérationnelle des essaims de drones commerciaux ?
- Q47 | Stratégie transversale | #3: Quel est l'état actuel des menaces de leurrage GPS pour les opérations de drones selon les rapports publics ?
- Q48 | Stratégie transversale | #4: Comparez l'état de préparation réglementaire pour les opérations de drones autonomes entre la France, l'UE, le Japon et la Corée du Sud.
- Q49 | Stratégie transversale | #5: Quelles preuves publiques existent de la convergence entre la technologie des drones de cinématographie et les applications de défense en ISR ?
- Q50 | Stratégie transversale | #6: Sur la base de toutes les preuves disponibles, quelles sont les trois meilleures opportunités de marché pour une entreprise française de drones à double usage, combinant cinématographie et défense ?
- Q51 | Questions pivot vers la gouvernance | #1: Quelle discipline de preuve devrions-nous démontrer à l'EASA et à la DGAC pour prouver que les décisions autonomes prises lors d'une perte de connectivité restent conformes à la politique ?
- Q52 | Questions pivot vers la gouvernance | #2: Comment la loi européenne sur l'IA définit-elle les exigences de supervision humaine pour les systèmes autonomes à haut risque, et à quoi ressemblerait un historique d'audit conforme pour les opérations de drones ?
- Q53 | Questions pivot vers la gouvernance | #3: Que requièrent les principes de l'OTAN sur les systèmes autonomes en matière de contrôle humain significatif, et comment les mettriez-vous en œuvre dans un essaim de drones perdant la connectivité satellite ?
- Q54 | Questions pivot vers la gouvernance | #4: Quelles leçons tirées des opérations de drones en Ukraine suggèrent l'importance de l'authentification des commandes et de la protection anti-rejeu ?
- Q55 | Questions pivot vers la gouvernance | #5: Comment un fabricant européen de drones de défense pourrait-il démontrer sa responsabilité post-incident à un comité de surveillance parlementaire après une défaillance d'un système autonome ?
- Q56 | Questions pivot vers la gouvernance | #6: Quel est l'état actuel de l'authentification des flux vidéo en direct pour les drones et quelles menaces existent pour la manipulation des flux de capteurs ?
- Q57 | Questions pivot vers la gouvernance | #7: Comparez les approches de Dedrone et Blighter en matière de gouvernance de détection de contre-mesures anti-drones et de journalisation des preuves. Quelles lacunes existent dans les historiques d'audit actuels des contre-drones ?
- Q58 | Questions pivot vers la gouvernance | #8: Quels éléments un protocole de vol en formation régi devrait-il inclure pour obtenir la certification EASA d'une opération de cinématographie multi-drones au-dessus d'un événement en direct avec public ?
- Q59 | Questions pivot vers la gouvernance | #9: Quels programmes de financement existent pour développer des architectures de systèmes autonomes gouvernés conformes à la fois à la loi européenne sur l'IA et à la doctrine de l'OTAN sur les systèmes autonomes ?
- Q60 | Questions pivot vers la gouvernance | #10: Sur la base de toutes les preuves disponibles, à quoi ressemblerait une couche de gouvernance minimale viable pour une entreprise française de drones opérant dans les secteurs de la cinématographie civile, de l'inspection professionnelle et de l'ISR de défense — couvrant la conformité réglementaire, l'auditabilité des décisions et les opérations en cas de connectivité dégradée ?
- Q61 | Intégration SkyDrone x InfraFabric (expliqueurs 600+) | #1: Quel enchaînement opérationnel SkyDrone doit-elle démontrer pour prouver qu'une action autonome reste traçable, gouvernée et explicable de bout en bout ?
- Q62 | Intégration SkyDrone x InfraFabric (expliqueurs 600+) | #2: Comment articuler les rôles de if.trace, if.bus, if.api, if.gov, if.context, if.switchboard et agent.rook dans une architecture unique lisible par un acheteur défense ?
- Q63 | Intégration SkyDrone x InfraFabric (expliqueurs 600+) | #3: Quelles preuves minimales faut-il publier pour passer d'une démonstration technique à une posture d'exploitation crédible auprès d'un grand compte ?
- Q64 | Intégration SkyDrone x InfraFabric (expliqueurs 600+) | #4: Quels cas d'usage SkyDrone doivent être priorisés pour prouver la valeur d'InfraFabric en inspection, événementiel et ISR dual-usage ?
- Q65 | Intégration SkyDrone x InfraFabric (expliqueurs 600+) | #5: Comment convertir le message 'autonomie rapide' en message 'autonomie contrôlée et révisable' pour des décideurs non techniques ?
- Q66 | Intégration SkyDrone x InfraFabric (expliqueurs 600+) | #6: Quelle feuille de route en trois phases permet d'intégrer InfraFabric chez SkyDrone sans perturber les opérations existantes ?
- Q67 | Intégration SkyDrone x InfraFabric (expliqueurs 600+) | #7: Quels indicateurs de succès montrent que l'intégration InfraFabric réduit réellement le risque opérationnel de SkyDrone ?
- Q68 | Intégration SkyDrone x InfraFabric (expliqueurs 600+) | #8: Quelles limites de promesse doivent rester explicites pour éviter tout sur-claim pendant le déploiement initial ?
- Q69 | if.api : intégrations partenaires et limites de promesse | #1: Quels connecteurs if.api sont prioritaires pour SkyDrone afin de réduire le délai d'intégration partenaire ?
- Q70 | if.api : intégrations partenaires et limites de promesse | #2: Comment distinguer clairement une preuve d'intégration existante d'un engagement de disponibilité runtime non encore démontré ?
- Q71 | if.api : intégrations partenaires et limites de promesse | #3: Quelle structure d'enveloppe normalisée SkyDrone devrait imposer aux flux entrants pour éviter la dérive sémantique entre systèmes ?
- Q72 | if.api : intégrations partenaires et limites de promesse | #4: Comment organiser la gouvernance des adaptateurs if.api pour maîtriser le risque de dérive protocolaire dans le temps ?
- Q73 | if.api : intégrations partenaires et limites de promesse | #5: Quels scénarios d'échec d'adaptateur doivent être testés en premier pour sécuriser l'intégration de partenaires critiques ?
- Q74 | if.api : intégrations partenaires et limites de promesse | #6: Quel plan de validation externe permet de prouver la robustesse d'if.api sans surestimer sa maturité actuelle ?
- Q75 | if.security et if.trace : preuve, contrôle et falsification | #1: Quels contrôles if.security doivent être activés en priorité pour empêcher des actions non autorisées sur des workflows SkyDrone à haut enjeu ?
- Q76 | if.security et if.trace : preuve, contrôle et falsification | #2: Comment traduire une exigence de sécurité en reçu if.trace vérifiable par un auditeur tiers sans contexte interne ?
- Q77 | if.security et if.trace : preuve, contrôle et falsification | #3: Quels tests de falsification doivent être exécutés avant toute montée en charge pour prouver que les garde-fous ne sont pas décoratifs ?
- Q78 | if.security et if.trace : preuve, contrôle et falsification | #4: Comment démontrer qu'une dérogation opérateur reste bornée, journalisée et réversible après incident ?
- Q79 | if.security et if.trace : preuve, contrôle et falsification | #5: Quels signaux d'abus doivent déclencher une escalade immédiate plutôt qu'une simple alerte informative ?
- Q80 | if.security et if.trace : preuve, contrôle et falsification | #6: Comment séparer noir/blanc ce qui est prouvé cryptographiquement de ce qui reste une interprétation opérationnelle ?
- Q81 | if.gov, if.switchboard et agent.rook : décisions sous contrainte | #1: Quelle politique de gate if.gov convient aux opérations SkyDrone quand la connectivité se dégrade en mission ?
- Q82 | if.gov, if.switchboard et agent.rook : décisions sous contrainte | #2: Comment if.switchboard doit-il isoler les domaines de défaillance pour éviter une contamination inter-agents ?
- Q83 | if.gov, if.switchboard et agent.rook : décisions sous contrainte | #3: Quels seuils décisionnels imposent une validation humaine obligatoire dans une chaîne autonome multi-agents ?
- Q84 | if.gov, if.switchboard et agent.rook : décisions sous contrainte | #4: Quel rôle exact agent.rook doit-il tenir entre supervision, intervention et continuité d'exécution ?
- Q85 | if.gov, if.switchboard et agent.rook : décisions sous contrainte | #5: Comment formaliser un protocole d'escalade qui reste opérable de nuit ou en cellule de crise sans perte de traçabilité ?
- Q86 | if.gov, if.switchboard et agent.rook : décisions sous contrainte | #6: Quelles preuves post-incident doivent être disponibles en moins de 30 minutes pour soutenir un comité de crise ?
- Q87 | if.context : continuité mission et budget de contexte | #1: Comment SkyDrone doit-elle structurer un chargement de contexte en tiers pour conserver la continuité sans saturer le budget token ?
- Q88 | if.context : continuité mission et budget de contexte | #2: Quelles données doivent rester en Tier 0 pour garantir des décisions robustes dès l'ouverture de session ?
- Q89 | if.context : continuité mission et budget de contexte | #3: Comment résumer les sessions stale sans polluer la vue live utilisée par les opérateurs en activité ?
- Q90 | if.context : continuité mission et budget de contexte | #4: Quels champs de session sont indispensables pour préserver la responsabilité lors des handoffs multi-équipes ?
- Q91 | if.context : continuité mission et budget de contexte | #5: Comment mesurer concrètement la compression de contexte obtenue sans dégrader la qualité des décisions ?
- Q92 | if.context : continuité mission et budget de contexte | #6: Quelle stratégie combine lecture rapide, mémoire append-only et récupération ciblée pour des opérations longues ?
- Q93 | Déploiement civil-défense : scénarios et résilience | #1: Quel scénario pilote SkyDrone devrait lancer en premier pour valider la valeur InfraFabric sur un périmètre civil-défense réaliste ?
- Q94 | Déploiement civil-défense : scénarios et résilience | #2: Comment définir les modes de repli en perte de lien pour rester conforme, sûr et exploitable en mission ?
- Q95 | Déploiement civil-défense : scénarios et résilience | #3: Quelles vérifications quotidiennes doivent être automatisées pour prouver la santé des modules critiques avant vol ?
- Q96 | Déploiement civil-défense : scénarios et résilience | #4: Comment bâtir un runbook post-incident qui distingue immédiatement les faits vérifiés des hypothèses de travail ?
- Q97 | Déploiement civil-défense : scénarios et résilience | #5: Quels signaux d'adoption interne montrent que la gouvernance devient un accélérateur opérationnel plutôt qu'un frein ?
- Q98 | Déploiement civil-défense : scénarios et résilience | #6: Quel dossier de preuve minimal faut-il préparer pour soutenir un cycle d'achat public ou de due diligence défense ?

## Quality and Gap Controls
Quality audit generated_utc: `2026-02-10T11:54:58Z`
- `total_rows_dedup`: `2964`
- `substantive_rows`: `2263`
- `non_substantive_rows`: `701`
- `inventory_rows`: `2263`
- `inventory_sources`: `50`
Non-substantive reason counts:
- `fetch_error`: `293`
- `topic_out_of_scope`: `244`
- `blocked_text_pattern`: `158`
- `too_short`: `4`
- `blocked_title_pattern`: `2`

Retarget gap report generated_utc: `2026-02-10T02:17:08Z`
Retarget per-source thinness flags (v1):
- `target_operator_public` -> ingest_ok=`85`, pages_error=`0`, pages_filtered=`0`, top_domain=`skydrone-robotics.com`, top_domain_share_pct=`98.8`, thin=`True`
- `target_operator_legacy_context` -> ingest_ok=`13`, pages_error=`1`, pages_filtered=`0`, top_domain=`www.skydrone.fr`, top_domain_share_pct=`100.0`, thin=`True`
- `civil_regulation_eu` -> ingest_ok=`78`, pages_error=`2`, pages_filtered=`0`, top_domain=`transport.ec.europa.eu`, top_domain_share_pct=`71.8`, thin=`False`
- `civil_regulation_fr` -> ingest_ok=`2`, pages_error=`19`, pages_filtered=`11`, top_domain=`www.service-public.gouv.fr`, top_domain_share_pct=`50.0`, thin=`True`
- `civil_regulation_global` -> ingest_ok=`2`, pages_error=`49`, pages_filtered=`48`, top_domain=`www.icao.int`, top_domain_share_pct=`50.0`, thin=`True`
- `dual_use_manufacturers_eu` -> ingest_ok=`188`, pages_error=`5`, pages_filtered=`0`, top_domain=`www.parrot.com`, top_domain_share_pct=`96.8`, thin=`True`
- `cinematography_stack` -> ingest_ok=`108`, pages_error=`2`, pages_filtered=`1`, top_domain=`www.dronisos.com`, top_domain_share_pct=`82.4`, thin=`True`
- `counter_uas_stack` -> ingest_ok=`69`, pages_error=`0`, pages_filtered=`0`, top_domain=`www.dedrone.com`, top_domain_share_pct=`97.1`, thin=`True`
- `defense_publications` -> ingest_ok=`118`, pages_error=`0`, pages_filtered=`0`, top_domain=`www.nato.int`, top_domain_share_pct=`96.6`, thin=`True`
- `industry_press` -> ingest_ok=`62`, pages_error=`1`, pages_filtered=`0`, top_domain=`dronelife.com`, top_domain_share_pct=`85.5`, thin=`True`

Interpretation rules:
- Thin=true means the lane exists but breadth/depth remains insufficient for strong claims.
- pages_error and pages_filtered growth indicates extraction fragility or scope mismatch.
- Dominant-domain concentration above ~90% can reduce diversity and should trigger balancing review.

## Graph Coverage: How Skydrone Appears in `if.knowledge`
Graph generated_utc: `2026-03-03T14:39:11Z`
Total nodes: `8898`
Total edges: `24527`
Skydrone direct node hits: `24`
Skydrone direct edge hits: `0`
Sample Skydrone-linked node IDs:
- `doc:2135-skydrone-auth-shell-singlefile.md`
- `doc:378-if-context-skydrone-full-system-consolidated-review-pack-v1-2026-02-10.md`
- `doc:379-if-context-skydrone-60q-navigator-and-cache-warm-delta-pack-v1-2026-02-10.md`
- `doc:380-if-context-skydrone-prompt-retune-scorecard-v1-2026-02-10.md`
- `doc:384-skydrone_60q_jester_zingers.fr.latest.md`
- `doc:690-skydrone-platform-presentation-v1.0-2026-02-23.md`
- `doc:696-skydrone-sales-explainer-from-opus-thread-v1.0-2026-02-23.md`
- `doc:697-skydrone-auth-phases-editable-2026-02-23.md`
- `doc:698-skydrone-suggested-questions-editable-2026-02-23.md`
- `doc:700-skydrone-suggested-questions-by-root-domain-v1.0-2026-02-24T204339Z.md`
- `doc:704-skydrone-management-in-depth-program-state-v1.0-2026-02-25T120500Z.md`
- `doc:900-skydrone-interface-index-frontend-single-pack-2026-02-24.md`
- `path:0ec6b6780c5f55e0`
- `path:18d7f94e6d7fad6e`
- `path:50de89fbf9c8c868`
- `path:76cfa9eb715dac80`
- `path:aee94cdbc442ecb9`
- `path:b5198d9a99c17358`
- `url:5c846c5189b7f02d`
- `url:730e5c86aaa6a3c2`
- `url:78e199ab26f2efab`
- `url:872abf86763bfe44`
- `url:9c3dc67980590500`
- `url:b159be150ec44a8d`

Graph interpretation boundary:
- Current skydrone signal in the graph is primarily doc/path/url presence evidence.
- This proves indexing presence and discoverability for those nodes.
- This does not by itself prove semantic correctness of every derived relationship.
- Graph freshness still depends on build cadence and input dataset updates.

## Update Cadence: How Skydrone RAG Stays Up-To-Date
### Automated cadence (verified)
- `if-knowledge-scope-regression.timer` exists and runs hourly.
- `if-knowledge-scope-regression.service` executes `/root/scripts/if_api_knowledge_scope_regression_once.sh`.
- Gate eval script enforces expected access/authorization response code patterns and writes gate status artifacts.

### Manual or operator-driven cadence (verified script capability)
- Crawl acquisition: `scripts/if_context_industry_web_crawl.py`
- Source inventory rebuild + quality audit: `scripts/if_context_build_source_inventory.py`
- Skydrone corpus materialization: `scripts/skydrone_build_pages_corpus.py`
- Query/citation quality run: `scripts/skydrone_run_queries_with_citations.py`
- Timing and latency breakdown: `scripts/skydrone_ttd_metrics.py`
- Research radar generation runner: `scripts/if_research_radar_runner.sh` + `scripts/if_research_radar.py`

### Freshness control model
- Runtime docs cache has explicit TTL exposure (`docs_refresh_ttl_sec` currently 120s in live output).
- Per-request forced refresh can be requested through `/if/rag-sources` refresh path handling.
- Inventory and corpus freshness are not guaranteed by runtime alone; they require crawl/inventory rebuild execution.
- Hourly knowledge-scope timer protects one governance lane but does not replace full datasource recrawl.
- Missing runtime source files in `/if/rag-sources` (`exists=false`) must downgrade confidence in affected lanes.
- No universal auto-heal claim is allowed unless all required schedulers and artifact refreshes are proven live.

### Failure and downgrade logic
- If endpoint reachability fails, treat live product posture as degraded until restored.
- If key runtime docs are missing or unloaded, downgrade from strong bounded claims to conservative preview wording.
- If inventory totals drift without reconciliation, block claim promotion for datasource completeness statements.
- If stale timestamps exceed policy windows for decision-critical categories (regulation/policy/defense), mark outputs stale-sensitive.
- If quality non-substantive ratio grows materially, prioritize source cleaning before adding new query patterns.

## Offline, Edge, and Multi-Agent Boundaries (Pre-Emptive Risk Control)
These boundaries address Antoine/Skydrone concerns directly and remain strict until dedicated hardening closes open gaps.

Current posture (black/white):
- Local serving of UI and backend can continue on-site where infra dependencies are local and healthy.
- Full disconnected autonomy is a non-claim unless signed degraded-mode policy + dependency health gates are explicit and enforced.
- Multi-session shared-state race conditions (last-writer-wins patterns) remain an open risk in related agent lanes until lock/lease hardening lands.
- Claims that imply switchboard independence or universal offline resilience are forbidden.

Required path to bounded offline claim (not yet complete):
1. Local inference fallback path with explicit health probe and mode switch.
2. Signed degraded-mode policy defining allowed actions by connectivity state.
3. Startup dependency gate that fails closed under unsafe partial connectivity.
4. Durable persistence for mission-critical attestation/registry state across restarts.
5. Multi-session concurrency replay proving race-safe behavior under parallel agents.

## Operational Verification Commands (No Logs, Reproducible)
### Surface and auth posture checks
```bash
curl -s -o /dev/null -w "%{http_code}
" https://skydrone.infrafabric.io/
curl -s -o /dev/null -w "%{http_code}
" https://skydrone.infrafabric.io/if/suggested-questions?tenant=skydrone
curl -s -o /dev/null -w "%{http_code}
" https://skydrone.infrafabric.io/if/rag-sources?tenant=skydrone
curl -s -o /dev/null -w "%{http_code}
" https://skydrone.infrafabric.io/api/v1/models
curl -s -o /dev/null -w "%{http_code}
" https://skydrone.infrafabric.io/api/v1/auths/
```

### Runtime source metadata checks
```bash
curl -fsS "https://skydrone.infrafabric.io/if/rag-sources?tenant=skydrone" | jq   "{tenant,resolved_tenant,docs_refresh_ttl_sec,sources_count,loaded_docs_count}"
curl -fsS "https://skydrone.infrafabric.io/if/rag-sources?tenant=skydrone" | jq   ".sources[] | {name,path,exists,loaded,has_trace,sha256,size_bytes,mtime_utc}"
```

### Suggested question integrity checks
```bash
curl -fsS "https://skydrone.infrafabric.io/if/suggested-questions?tenant=skydrone" | jq   "{tenant,categories:(.categories|length),questions:(.categories|map(.questions|length)|add)}"
```

### Inventory and quality checks (local docs)
```bash
jq ".total_records_dedup,.total_source_feeds,.generated_utc" docs/data/if1388_ingested_sources_summary.v12.json
jq ".totals,.generated_utc" docs/data/if1388_ingested_quality_audit.v12.json
jq ".totals,.generated_utc" docs/data/if1431_skydrone_retarget_gap_report.v1.json
```

### Timer/scheduler checks
```bash
systemctl list-timers --all --no-pager | rg -i "knowledge|scope|skydrone|radar"
systemctl cat if-knowledge-scope-regression.timer
systemctl cat if-knowledge-scope-regression.service
```

## Release Language Guardrails
Allowed wording now:
- "Skydrone RAG is live as a bounded tenant-scoped retrieval and prompt-assembly system with explicit source metadata exposure."
- "Datasource inventory and quality artifacts are published locally in v12 and can be replay-checked."
- "Current posture is preview; confidence depends on freshness and quality lanes that are explicitly tracked."

Blocked wording now:
- "Skydrone RAG is always up to date."
- "Skydrone RAG is certification-ready for autonomous defense operations."
- "All Skydrone RAG sources are receipt-bound in if.trace."
- "Offline autonomous operation is fully validated."

## 30/60/90 Execution Plan (Skydrone RAG)
### 0-30 days
- Promote runtime source metadata and critical inventories into immutable no-login evidence surfaces with checksums.
- Close missing radar digest source lane (`exists=false` in live runtime metadata) or explicitly remove it from active source contract.
- Add per-category freshness SLO (especially regulation/policy/defense).
- Add automatic reconciliation check between summary totals and row-level totals in v12 successors.

### 31-60 days
- Add signed degraded-mode policy for offline/edge behavior and publish non-claim boundaries in runtime contract form.
- Run multi-session concurrency replay for shared-state paths and publish pass/fail artifacts.
- Attach provenance receipts where feasible for runtime-loaded docs or publish explicit receipt-gap register.
- Stabilize radar cadence with verified daily artifacts in canonical path.

### 61-90 days
- Move from host-local Tier B dominance to mixed Tier A/Tier B with immutable reviewer packet mirrors.
- Publish operator and procurement decision packets with identical claim boundary language.
- Gate promotion on weakest dependency inheritance across if.context, if.rook, if.bus, if.blackboard, and if.trace where claims overlap.
- Re-run this explainer as v1.1 with explicit closure status for each open finding.

## Open Findings Register (Current)
| Finding ID | Severity | Statement | Impact | Next action | Target close |
|---|---|---|---|---|---|
| SKY-F1 | High | Runtime source gap: radar digest files not present in `/if/rag-sources` live output. | Can hide intended freshness lane and overstate update coverage. | Restore files or remove lane from runtime contract; add explicit status in reviewer packet. | 2026-03-10 |
| SKY-F2 | Medium | `has_trace=false` on all runtime source entries in live output. | Limits independent provenance posture and weakens external assurance claims. | Define receipt-binding rollout plan or publish explicit non-receipt boundary by source class. | 2026-03-17 |
| SKY-F3 | Medium | Hourly knowledge-scope timer exists, but full Skydrone crawl/inventory recrawl is not shown as fully automated continuous schedule. | Freshness drift risk for market/regulation lanes. | Publish authoritative scheduler map for crawl+inventory+corpus rebuild cadence. | 2026-03-17 |
| SKY-F4 | Medium | Graph contains Skydrone doc/path/url nodes but no demonstrated strong semantic edge evidence in this pack. | Could be misread as deeper knowledge connectivity than proven here. | Add graph query packet with explicit relation-level tests and expected counts. | 2026-03-24 |
| SKY-F5 | Low | Continuity owner remains unnamed. | Coordination risk during incident handoffs. | Assign backup owner with checkpoint accountability. | 2026-03-17 |

## Appendix A — Runtime Route Map (`skydrone.infrafabric.io`)
- Route block exists in CT210 Caddy config for `skydrone.infrafabric.io`.
- `@otp_shell` path `/auth /auth/` -> `10.10.10.230:5001`.
- `@otp_api` path `/auth/otp/*` -> `10.10.10.230:5001`.
- `@if_api` path `/if /if/*` -> `10.10.10.230:5001`.
- Default route -> `10.10.10.230:8086` (OpenWebUI shell).
- This map enforces path-level split between public RAG metadata/question surfaces and auth-bound API/model surfaces.

## Appendix B — Script Contract Register
### Script 01/09: `/root/scripts/if_context_industry_web_crawl.py`
- Purpose: Crawl and ingest public industry sources with filtering and ingest artifacts.
- Outputs: Produces crawl pages JSONL, ingest JSONL, summary JSON, UA/domain report.
- Claim boundary: script presence proves capability path, not successful latest execution without fresh artifacts.

### Script 02/09: `/root/scripts/if_context_build_source_inventory.py`
- Purpose: Build deduped source summary, titles inventory, and quality audit.
- Outputs: Produces `if1388_ingested_sources_summary.*`, `if1388_ingested_source_titles.*`, `if1388_ingested_quality_audit.*`.
- Claim boundary: script presence proves capability path, not successful latest execution without fresh artifacts.

### Script 03/09: `/root/scripts/skydrone_build_pages_corpus.py`
- Purpose: Build compact Skydrone corpus from crawl artifacts.
- Outputs: Produces `skydrone_pages_corpus.v1.jsonl` and summary JSON.
- Claim boundary: script presence proves capability path, not successful latest execution without fresh artifacts.

### Script 04/09: `/root/scripts/skydrone_run_queries_with_citations.py`
- Purpose: Run tenant question set through answer endpoint with citation/violation checks.
- Outputs: Produces JSON+Markdown run reports with per-question outcomes.
- Claim boundary: script presence proves capability path, not successful latest execution without fresh artifacts.

### Script 05/09: `/root/scripts/skydrone_ttd_metrics.py`
- Purpose: Read timing logs and compute tenant-specific latency windows.
- Outputs: Produces tenant row/window metrics for performance tuning.
- Claim boundary: script presence proves capability path, not successful latest execution without fresh artifacts.

### Script 06/09: `/root/scripts/if_research_radar_runner.sh`
- Purpose: Orchestrate daily radar build, manifest, and latest pointers.
- Outputs: Writes radar JSON/MD, metrics JSON, persona JSON, manifest.
- Claim boundary: script presence proves capability path, not successful latest execution without fresh artifacts.

### Script 07/09: `/root/scripts/if_research_radar.py`
- Purpose: Build ranked research radar candidates with recency weighting and thresholds.
- Outputs: Produces radar report JSON+MD and delta-vs-previous metrics.
- Claim boundary: script presence proves capability path, not successful latest execution without fresh artifacts.

### Script 08/09: `/root/scripts/if_api_knowledge_scope_regression_once.sh`
- Purpose: Run knowledge-scope regression + gate status publication pipeline.
- Outputs: Writes latest/gate/windows/alerts artifacts and index for `/llm/switchboard/knowledge-scope/`.
- Claim boundary: script presence proves capability path, not successful latest execution without fresh artifacts.

### Script 09/09: `/root/scripts/if_api_knowledge_scope_gate_eval.py`
- Purpose: Compute gate status from redteam windows and threshold rules.
- Outputs: Writes latest window and gate status JSON outputs used for claim state.
- Claim boundary: script presence proves capability path, not successful latest execution without fresh artifacts.

## Appendix C — Registry Context (Cross-Module Boundaries)
Relevant module IDs in `if.registry.json` affecting Skydrone RAG interpretation:
- 6:    "Brand labels are defined here (e.g., if.trace, IF.GOV). They may differ from product IDs.",
- 182:    "uses_receipts_from": "If present, indicates which product_id provides the receipt surface used to bind outputs (e.g., if.trace).",
- 215:    "surface": "A UI/distribution surface that routes users to verification primitives (e.g., narrative-red-team routes to if.trace receipts).",
- 221:      "product_id": "if.trace",
- 222:      "brand": "if.trace",
- 248:      "description": "Narrative red-team publishing/review UI that makes if.trace legible via dossiers/packs and routes reviewers to receipts.",
- 250:        "if.trace"
- 310:      "product_id": "if.bus",
- 360:        "if.trace"
- 380:        "if.trace"
- 457:      "product_id": "if.context",
- 458:      "brand": "if.context",
- 460:      "description": "Evidence environment for agent work: artifacts (bytes + provenance), read plans, and derived artifacts with verification chains. Not a replacement for `if.bus` (control plane) or `if.trace` (integrity receipts).",
- 462:        "if.trace"
- 505:        "if.trace"
- 520:      "product_id": "if.blackboard",
- 521:      "brand": "if.blackboard",
- 526:      "description": "Auditable single- and multi-agent coordination surface: append-only task snapshots + signals, rendered to GET-first `/llm` views; controlled-writer updates; no-login review posture. Legacy name: `if.tasks` (keep legacy `/llm/platform/if-tasks/**` docs as an alias surface; canonical product id is `if.blackboard`).",
- 555:        "if.trace"
- 574:        "if.trace"
- 587:        "if.trace"
- 600:        "if.trace"
- 614:      "product_id": "if.knowledge",
- 615:      "brand": "if.knowledge",
- 619:        "if.trace"
- 636:      "description": "Build-time developer knowledge base (KB) artifacts generated via `if.knowledge` (static Markdown/HTML; no runtime fetches). Preview: a bus/api KB snapshot is published; no deployed KB service on this host.",
- 638:        "if.trace"
- 662:        "if.trace"
- 676:        "if.trace"
- 679:        "if.trace",
- 680:        "if.bus",
- 682:        "if.blackboard",
- 683:        "if.switchboard",
- 684:        "if.context",
- 701:        "if.trace"
- 710:      "product_id": "if.switchboard",
- 711:      "brand": "if.switchboard",
- 713:      "description": "Real-time SIP-edge plus Redis-stream coordination module with canonical ingress through if.api and transport on if.bus; no supported bypass path is claimed in the public contract.",
- 716:        "if.trace"
- 723:        "if.bus"
- 736:        "if.trace"
- 749:        "if.trace"
- 762:        "if.trace"
- 775:        "if.trace"
- 788:        "if.trace"
- 803:        "if.trace"

Boundary reminder: Skydrone RAG explanation here is tenant/application behavior layered over these modules; module maturity and dependency state constrain claim strength.

## Appendix D — Fast Decision Checklist
1. Are `/if/suggested-questions` and `/if/rag-sources` both returning HTTP 200 right now?
2. Does `/if/rag-sources` show required sources as `exists=true` and `loaded=true`?
3. Do missing lanes (if any) have explicit downgrade language in stakeholder messaging?
4. Do current inventory totals reconcile (`summary total` vs `titles rows`)?
5. Is quality non-substantive ratio stable or improving versus previous run?
6. Is hourly knowledge-scope gate currently healthy and fresh?
7. Have regulation/policy/defense lanes been refreshed within accepted recency windows?
8. Are offline/autonomy claims still bounded to declared non-claim envelope?
9. Are open findings tracked with owner and close date before promotion?
10. Are release statements aligned with this document’s verified/bounded/non-claim split?

## Conclusion
Skydrone RAG is real, structured, and operationally useful, but it must be treated as a governed evidence system, not a blanket truth engine.
The strongest value today is disciplined decision support with explicit source metadata, bounded inference posture, and concrete update controls.
The highest risk is overclaiming beyond freshness and dependency boundaries; this explainer is designed to make that failure mode hard to ignore.
The immediate path forward is clear: close missing source lanes, harden provenance exposure, formalize offline boundaries, and keep claim language pinned to weakest fresh evidence.

## Related

- [[if.context Full Explainer v1.3 (Consolidated 1000+ Dense Lines)]]
- [[if.blackboard Full Explainer v1.2 (Four-Audience, Claim-Boundary Strict)]]
- [[if.bus Full Explainer v1.5 (Switchboard-Integrated, Claim-Boundary Strict)]]
- [[Governance and PHAROS MOC]]
- [[InfraFabric Architecture]]
