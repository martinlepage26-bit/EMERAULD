# LegiPro Data Licensing Explainer for Jade

Document ID: 4170  
Date: 2026-06-09  
Status: internal all-in-one explainer  
Audience: Jade, Martin, operator-side review  
Scope: LegiPro autocomplete intent work, conveyor extraction traces, accounting/legal corpus ingestion workflows  
Explicitly out of scope: `if.trace` current-volume claims

## Executive Summary

LegiPro has data assets that may be as valuable as the Blackboard governance traces, but the value is different.

The strongest LegiPro licensing candidates are not the raw accounting/legal corpus text. The strongest candidates are the **workflow traces and derived evaluation assets** created while building the product:

1. **Conveyor extraction and validation traces**
   - agents convert accounting/legal source material into structured extraction artifacts;
   - each candidate carries manifests, patch records, events, closeouts, validation gates, and quarantine/acceptance decisions;
   - this teaches models how to extract, validate, reject, and boundary-control professional source material.

2. **Autocomplete intent and result-precalculation data**
   - real French accounting/tax search strings are converted into professional intents, source-family hints, route-bias rules, and expected results;
   - this can become a high-value retrieval-evaluation dataset:
     `messy user query -> professional intent -> correct source family -> expected source/result -> rejected bad sources`.

3. **Corpus ingestion decision and source-scoring records**
   - source candidates are scored for authority, machine ingestability, rights posture, validation value, and product impact;
   - this teaches source-selection discipline in a professional accounting/legal domain.

The most important boundary:

> License the operational traces, labels, routing decisions, tests, source-scoring records, and relevance judgments. Do not casually license raw official corpus text, proprietary methodology, raw user/client data, or unredacted logs.

This work is ongoing. If micro1 or another data buyer confirms that this category has value, the LegiPro data-production lane could be accelerated dramatically: more autocomplete queries can be classified, more result packs can be precalculated, more conveyor traces can be normalized, and a controlled sample can be produced quickly.

## Company and Naming Clarification

Pharos AI and InfraFabric are trading names / product identities of the same company.

For a first micro1 conversation, use **Pharos AI** as the cleaner sender identity. LegiPro can be introduced as the accounting/legal product surface. InfraFabric can be introduced later, under NDA if needed, as the infrastructure/evidence workflow layer.

Do not frame this as a two-company joint IP negotiation. It is a single-company product-boundary and licensability question.

## What LegiPro Has That micro1 Might Value

micro1 is likely looking for operational data that helps train or evaluate AI systems on expert workflows. The best LegiPro assets map to that need in three ways.

### 1. Extraction and Validation Workflow Data

LegiPro's conveyor system records how remote/agent workers generate, submit, validate, quarantine, and accept structured extraction artifacts.

Current evidence from local status and repo inspection:

- conveyor accepted candidates: **7,350**
- conveyor quarantine candidates: **1,025**
- conveyor receipts: **2,135**
- extraction JSON files in repo: **8,888**
- extraction tests in repo: **9,344**
- integration preflight gates include JSON parse, focused pytest, git diff check, graph orphan gate, card manifest, claim-boundary regression, and no-overclaim scan.

This is valuable because the data is not just "legal text." It is a large operational record of:

- source extraction,
- artifact generation,
- patch review,
- failure classification,
- source-path validation,
- claim-boundary enforcement,
- test generation,
- preflight approval,
- accepted/quarantined outcomes.

That is closer to what AI labs need for evaluation and model improvement than raw source documents.

### 2. Autocomplete Intent and Search-Relevance Data

LegiPro has a saved Google autocomplete/search-intent corpus:

- raw autocomplete rows: about **62,681**
- major buckets: **8**
- current curated public suggestions: **50**
- current live asset: `site/legipro-fr/assets/bureau-suggestions.json`

The raw autocomplete data is not the main asset. It is noisy, misspelled, premise-heavy, and not always professionally safe.

The valuable asset is the transformation:

```text
raw query
-> normalized professional intent
-> safe display label
-> intent hint
-> source-family bias
-> route-bias rule
-> expected result/source family
-> bad-source rejection rule
```

That transformation is exactly the kind of retrieval and intent-understanding data that can help train or evaluate AI systems for professional search.

### 3. Corpus Source-Scoring and Ingestion Decisions

LegiPro has a source-ingestion scoreboard for accounting/legal/professional sources. It scores sources on:

- product-level impact,
- commercial-path impact,
- authority and trust,
- machine ingestability,
- rights and redistribution posture,
- benchmark and validation value,
- operational leverage,
- maintenance burden.

Example source decisions include:

- Publicodes / mon-entreprise: `integrate_now`
- INSEE Sirene: `integrate_now`
- INSEE Esane: `adapter_next`
- INPI/RNE public accounts: `adapter_next`
- Service-Public / Entreprendre: `adapter_next`
- DGCCRF payment guidance: `adapter_next`
- DCG/CRCF annales: `spot_check_only`
- commercial accounting blogs: `avoid_ingest`

This is a valuable "source judgment" dataset. It teaches:

- which sources are authoritative,
- which sources are useful but not citation-grade,
- which sources are rights-risky,
- which sources improve scenario calculations,
- which sources should be excluded despite being tempting.

## Why This Is Valuable for AI Training and Evaluation

Many datasets show answers. LegiPro's better assets show **how to get to a professional answer safely**.

The high-value patterns are:

- messy query -> professional intent;
- official source -> structured extraction;
- candidate answer -> claim-boundary check;
- weak source -> rejection;
- source rights unclear -> spot-check only;
- exact legal/accounting reference -> exact-route handling;
- wrong-domain retrieval -> regression failure;
- agent output -> test -> accepted/quarantined outcome.

That is the practical difference between:

```text
"Here is a legal/accounting answer"
```

and:

```text
"Here is how a professional system decides what it can safely retrieve, cite, route, and claim"
```

The second category is rarer and more valuable.

## Asset 1: Conveyor Extraction / Validation Traces

### What the conveyor does

The conveyor is an operational pipeline around candidate work artifacts.

A typical accepted candidate includes:

- candidate metadata,
- assignee/model lane,
- status JSON,
- patch artifact,
- manifest,
- closeout note,
- transcript,
- events JSONL,
- heartbeat,
- validation report,
- source-path scope check,
- accepted/quarantine movement history.

Example candidate shape:

```json
{
  "schema": "pharos.candidate_conveyor.v1",
  "candidate_id": "t_ffdf9977-20260531T180255Z-fab9992a",
  "assignee": "pharos-gce-mini54-low-48h",
  "lifecycle_state": "completed",
  "classification": "staged",
  "artifacts": [
    {"role": "status_json", "present": true, "sha256": "..."},
    {"role": "patch", "present": true, "sha256": "..."},
    {"role": "manifest", "present": true, "sha256": "..."},
    {"role": "closeout", "present": true, "sha256": "..."},
    {"role": "transcript", "present": true, "sha256": "..."},
    {"role": "events", "present": true, "sha256": "..."}
  ],
  "validation": {
    "git_apply_check": {"status": "pass"},
    "path_scope": {
      "status": "pass",
      "unsafe_paths": []
    }
  },
  "history": [
    {"event": "stage", "note": "candidate received"},
    {"event": "move:validating", "note": "GCE-DRAIN..."},
    {"event": "validate", "note": "pass"},
    {"event": "move:accepted", "note": "accepted after bundled preflight"}
  ]
}
```

### What the data teaches

This dataset teaches a model or evaluation harness:

- how source-backed extraction work is packaged;
- how to distinguish candidate/planning artifacts from evidence-ready artifacts;
- how to reject unsafe paths;
- how to preserve source paths;
- how to avoid overclaim language;
- how to generate tests for extracted artifacts;
- how to classify worker failures and retry conditions;
- how to move work from incoming to staging to validating to accepted/quarantine.

### Why this may be higher value than raw corpus data

Raw legal/accounting text is often rights-sensitive and not unique.

The conveyor traces are different. They show:

- the operational method of transforming sources into useful structured artifacts;
- the mistakes workers make;
- the gates that catch them;
- the accepted vs quarantined distinction;
- the provenance chain for each output.

That is useful for training/evaluating AI systems that need to work under professional constraints.

### Licensability posture

Likely licensable after redaction:

- candidate metadata,
- role/type of artifact,
- validation status,
- failure class,
- accepted/quarantine outcome,
- source-path category after abstraction,
- test outcome,
- claim-boundary classification.

Needs redaction or exclusion:

- raw transcripts,
- exact repo paths,
- hostnames,
- SIDs,
- source text excerpts,
- client/domain-specific material,
- methodology-revealing prompts,
- model provider secrets or credential-like data.

## Asset 2: Extraction JSON + Tests

The repo contains thousands of extraction artifacts and tests.

Current repo inspection:

- `data/extractions/*.json`: **8,888**
- `tests/test_extraction_*.py`: **9,344**

Example extraction artifact fields:

```json
{
  "schema": "gce_sf_v4_coverage_bridge...",
  "generated_at_utc": "2026-05-31T01:00:25Z",
  "status": "candidate / planning_only / not_evidence_ready",
  "classification": "candidate / planning_only / not_evidence_ready",
  "source_paths": ["data/coverage/api_field_occurrence_tally_v1.json"],
  "task_focus": "Convert the existing API field occurrence coverage inventory...",
  "findings": [
    {
      "finding_id": "...-001",
      "finding": "The source tally covers 18 JSON files...",
      "source_paths": ["data/coverage/api_field_occurrence_tally_v1.json"]
    }
  ],
  "blockers": [
    {
      "blocker_id": "...-B001",
      "issue": "The input is a coverage inventory tally..."
    }
  ]
}
```

Example test behavior:

```python
def test_required_fields_present(self):
    for field in REQUIRED_FIELDS:
        assert field in self.data

def test_boundary_fields_are_candidate_only(self):
    assert self.data["status"] == "candidate_only"
    assert self.data["classification"] == "planning_only_not_evidence_ready"

def test_no_forbidden_overclaim_language(self):
    text = json.dumps(self.data, ensure_ascii=False).lower()
    for term in FORBIDDEN_TERMS:
        assert term not in text
```

### What this teaches

This is a strong professional-evaluation pattern:

- extracted artifact must carry required fields;
- source paths must exist;
- claim boundary must be explicit;
- candidate-only artifacts must not overclaim authority;
- forbidden legal/compliance wording is mechanically rejected.

This is useful for AI labs because it is not generic coding data. It is domain-specific **professional caution encoded as tests**.

### Licensability posture

Potentially licensable after transformation:

- schema requirements,
- field-level validation patterns,
- candidate/evidence-ready labels,
- forbidden-overclaim tests,
- extraction QA outcomes,
- generalized source-path and claim-boundary structures.

Needs caution:

- raw source excerpts,
- official corpus text,
- exact internal file paths,
- proprietary extraction schema names where they leak method,
- worker transcripts.

## Asset 3: Autocomplete Intent and Result-Precalculation

### Current autocomplete stack

Current public stack:

- frontend: `site/legipro-fr/bureau.html`
- curated suggestions: `site/legipro-fr/assets/bureau-suggestions.json`
- local browser matching/ranking
- optional runtime search call to `/v0/search/routed`
- no per-keystroke LLM calls
- no live Google Suggest dependency

Current internal data:

- raw autocomplete rows: **62,681**
- categories: **8**
- public curated suggestions: **50**

Current public suggestion example:

```json
{
  "id": "sug_tva_btp_autoliquidation_sous_traitance",
  "category": "tva_btp_travaux",
  "suggestion_type": "intent_search",
  "display_label": "Autoliquidation de TVA en sous-traitance BTP",
  "normalized_query": "autoliquidation de tva en sous-traitance btp",
  "default_query": "Autoliquidation de TVA en sous-traitance BTP",
  "target_route": "search_v2",
  "intent_hint": "tva_btp_autoliquidation",
  "corpus_hints": ["bofip_tva", "legi_cgi_tva"],
  "authority_id": "sa--bofip_tva_planning",
  "risk_boundary_notes": [
    "Recherche source uniquement; verifier contrat, factures et date d'application."
  ],
  "alias_terms": [
    "auto liquidation tva btp",
    "tva sous traitance btp",
    "tva auto liquidation sous traitance"
  ]
}
```

### Why result-precalculation matters

Raw autocomplete queries alone are weak. Precalculated result packs are strong.

The valuable dataset shape is:

```json
{
  "raw_query": "tva travaux logement ancien",
  "normalized_query": "tva sur travaux dans un logement de plus de deux ans",
  "professional_intent": "tva_logement_travaux",
  "safe_display_label": "TVA sur travaux dans un logement de plus de deux ans",
  "source_family_bias": ["bofip_tva", "legi_cgi_tva"],
  "expected_result_type": "official_source_search",
  "top_expected_sources": [
    {"source_family": "bofip_tva", "role": "doctrine"},
    {"source_family": "legi_cgi_tva", "role": "legal_text"}
  ],
  "bad_source_rejects": [
    {"source_family": "pcg", "reason": "accounting-plan source is not primary for TVA rate qualification"},
    {"source_family": "urssaf", "reason": "social source is wrong-domain"}
  ],
  "answerability": "sourceable_with_missing_facts",
  "missing_facts": ["nature des travaux", "age du logement", "date", "facture details"]
}
```

This is much more valuable than autocomplete text because it encodes expert retrieval judgment.

### What the data teaches

Precalculated autocomplete/result packs teach:

- intent normalization from messy French accounting language;
- typo and alias handling;
- exact-reference promotion;
- source-family routing;
- bad-source rejection;
- answerability boundaries;
- missing-fact detection;
- professional labels instead of raw user phrasing.

This could be valuable for:

- retrieval evaluation,
- legal/accounting search benchmark construction,
- query-router training,
- answer-grounding evaluation,
- model behavior under source constraints.

### Ongoing work and acceleration option

The raw autocomplete corpus is already available. The current public slice is intentionally small.

If this has licensing value, work can accelerate dramatically:

- classify the top 100 to 500 rows per bucket;
- generate result-precalculation packs;
- create deterministic route-bias assets;
- add bad-source rejection labels;
- create a validation harness for expected top sources;
- produce a 100-row redacted sample for micro1 after NDA.

The important point:

> This is not a fixed dataset only. It is an active data-production pipeline that can generate more high-value evaluation records if the buyer confirms the category.

## Asset 4: Corpus Source-Scoring and Ingestion Decisions

LegiPro also has a source-ingestion scoreboard.

This is valuable because professional AI systems need to know not only what a source says, but whether the source should be trusted, cited, adapted, or avoided.

Example source decision schema:

```json
{
  "source_id": "publicodes_mon_entreprise",
  "source_name": "Publicodes / mon-entreprise",
  "decision": "integrate_now",
  "score_total": 82,
  "scores": {
    "product_level_impact": 16,
    "commercial_path_impact": 7,
    "authority_trust": 12,
    "machine_ingestability": 15,
    "rights_posture": 12,
    "benchmark_validation_value": 10,
    "operational_leverage": 5,
    "maintenance_burden": 3
  },
  "citation_role": "calculation_rule_source",
  "not_for": ["unsupervised_advice", "production_without_review"],
  "next_action": "build adapter spike against scenario MVP"
}
```

### Why this matters

Most AI systems fail professional work because they treat all plausible text as equally useful.

LegiPro source-scoring teaches:

- official doctrine beats commentary;
- open data with unclear redistribution may be spot-check only;
- source authority and machine ingestability are separate dimensions;
- a source can be useful for tests but not citation-grade;
- source rights can cap a decision even when content quality is high.

That is highly aligned with professional AI evaluation.

## Relative Value Ranking

| Asset | micro1-style value | Why |
|---|---:|---|
| Conveyor extraction / validation traces | Very high | Shows agentic professional extraction, validation, rejection, and acceptance workflows |
| Autocomplete result-precalculation packs | High if built | Encodes messy user intent into professional retrieval judgments |
| Extraction JSON + tests | High | Domain-specific claim-boundary and overclaim-prevention tests |
| Source-scoring / ingestion decisions | Medium-high | Teaches authority, rights, and product-impact judgment |
| Raw autocomplete strings | Medium | Useful discovery input but noisy and not enough alone |
| Raw accounting/legal corpus text | Risky / not preferred | Rights-sensitive and less differentiated than workflow/evaluation traces |

## What To License vs What Not To License

### Likely licensable after redaction

- conveyor lifecycle metadata,
- accepted/quarantined outcome labels,
- validation results,
- failure classes,
- extraction QA test patterns,
- claim-boundary labels,
- source-family routing labels,
- autocomplete intent normalization,
- route-bias and bad-source-reject labels,
- source-scoring decisions and rationales,
- synthetic/redacted examples.

### Do not license casually

- raw official corpus text,
- raw Google autocomplete dump,
- raw transcripts,
- raw model prompts,
- unredacted paths/SIDs/hostnames,
- secrets or credential-adjacent rows,
- client-derived facts,
- proprietary methodology documents,
- unbounded current product logic that could reconstruct the system.

## Licensability Risks

### 1. Source rights

Official/legal/accounting sources may be accessible but not freely redistributable as training data.

Safer posture:

- license labels, routing decisions, extraction workflows, and evaluation traces;
- avoid selling raw source text unless rights are clear.

### 2. Google autocomplete rights

The raw autocomplete corpus is valuable internally, but licensing raw Google-derived suggestion dumps may create rights and policy concerns.

Safer posture:

- use raw autocomplete as discovery input;
- license transformed professional-intent labels and evaluation records, not raw dumps.

### 3. Methodology reconstruction

Conveyor and autocomplete assets can leak how LegiPro works.

Controls:

- remove exact internal paths and schema names where not needed;
- flatten workflow fields;
- normalize timestamps;
- abstract source-route labels;
- preserve utility without teaching the entire product architecture.

### 4. Client/domain contamination

Some operational traces may include real client or domain-specific content.

Controls:

- exclude client-derived rows from first sample;
- run PII/confidentiality scans;
- keep only internal product/corpus/QA workflow data for pilot.

## Suggested micro1 Positioning

Use:

> LegiPro is our accounting/legal product surface. The valuable data is not raw legal text or generic chat. It is the operational record of how messy professional questions and official sources are transformed into safe intents, route decisions, extraction artifacts, validation tests, and source-bound answerability judgments.

If asked what makes it different:

> It captures professional retrieval and evidence discipline: which source family should answer a question, which sources should be rejected, what facts are missing, when an artifact is only a candidate, and when a claim is too strong.

If asked about volume:

> We have substantial raw and operational volume, including about 62.7k autocomplete-derived search strings, thousands of conveyor extraction artifacts, and thousands of generated extraction tests. We are not treating those gross counts as licensable volume until the audit and redaction pass are complete.

If asked about timeline:

> If this category is valuable, we can accelerate the work. A synthetic or schema-level specimen can be shared pre-NDA. A controlled redacted sample could be prepared after NDA, starting with autocomplete intent/result packs and conveyor validation traces.

## Recommended First Sample Pack

Pre-NDA:

1. synthetic autocomplete/result-precalculation examples,
2. synthetic conveyor lifecycle example,
3. field map,
4. no raw source text,
5. no raw paths/SIDs/hostnames.

Post-NDA:

1. 25 autocomplete intent/result-precalculation records,
2. 25 conveyor validation traces,
3. 10 extraction-test examples,
4. 10 source-scoring decisions,
5. disclosure manifest and redaction notes.

Pilot:

1. 500 to 2,000 autocomplete/result records,
2. 500 to 2,000 conveyor/evaluation traces,
3. selected source-scoring records,
4. benchmark split with holdout queries,
5. rights and field-of-use limits.

## Checks Needed Before Sample Delivery

Minimum checks:

- no raw official source text unless cleared;
- no raw Google autocomplete dump;
- no secrets or API keys;
- no client facts;
- no exact host paths;
- no SIDs or operator identifiers;
- no model-provider credentials;
- no product-internal prompts that reveal the crown-jewel method;
- no claims that candidate/planning artifacts are evidence-ready;
- no "legal/compliance-grade" overclaim language unless explicitly verified.

Recommended automated checks:

```text
PII scan
secret scan
path/SID/hostname scan
source-text excerpt scan
client/domain contamination scan
forbidden-overclaim scan
methodology leakage scan
JSON schema validation
sample manifest hash check
```

## Acceleration Plan If micro1 Confirms Value

This is ongoing work and can be accelerated if it has value.

### Week 1: Sample readiness

- create synthetic pre-NDA specimen;
- pick candidate-safe conveyor rows;
- create 25 to 50 autocomplete/result examples;
- strip paths/SIDs/timestamps;
- write field map and redaction manifest.

### Week 2: Pilot dataset

- classify more autocomplete buckets;
- build 500+ intent/result records;
- normalize conveyor event fields;
- add accepted/quarantine labels;
- prepare test/evaluation split;
- run contamination checks.

### Week 3+: Production data lane

- scale autocomplete result-precalculation;
- add more source-family bad-reject labels;
- add answerability/missing-facts labels;
- expand conveyor trace normalization;
- package recurring refreshes;
- price separately for evaluation-only vs general model training.

## Commercial Readiness

Ready now:

- qualification conversation;
- high-level explanation;
- synthetic examples;
- field-map discussion;
- statement that a meaningful data-production lane exists.

Not ready yet:

- raw data delivery;
- final licensable volume;
- exclusivity discussion;
- price quote;
- broad corpus-text license.

Best first-call posture:

> We can qualify whether this category is valuable, then prepare a controlled sample under NDA. The most interesting LegiPro data is workflow/evaluation data around professional search, extraction, validation, and source discipline, not raw legal text.

## Bottom Line for Jade

LegiPro gives the company another strong data-licensing angle beyond Blackboard.

Blackboard is the governance-workflow dataset.

LegiPro is the professional accounting/legal retrieval and extraction dataset.

The highest-value LegiPro package is:

```text
autocomplete intent/result-precalculation
+ conveyor extraction/validation traces
+ extraction tests and claim-boundary labels
+ source-scoring decisions
```

That package teaches AI systems how professional accounting/legal work is searched, sourced, extracted, validated, and bounded.

If micro1 confirms demand for this category, the work can be accelerated quickly because the raw materials, pipelines, and validation harnesses already exist.
