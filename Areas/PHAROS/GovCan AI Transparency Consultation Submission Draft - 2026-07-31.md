---
type: draft
title: GovCan AI Transparency Consultation Submission Draft - 2026-07-31
tags:
- pharos
- ai-governance
- consultation
- transparency
- government-of-canada
status: draft
created: '2026-07-31'
updated: '2026-07-31'
vault_area: Areas
canonical_path: Areas/PHAROS/GovCan AI Transparency Consultation Submission Draft - 2026-07-31.md
---

# Submission Draft: AI Transparency That Canadians Can Use

Prepared for Innovation, Science and Economic Development Canada's consultation on advancing AI transparency in Canada.

Suggested respondent profile, if submitting with attribution: independent AI governance practitioner / professional services / Quebec / sole practitioner or microenterprise.

Do not include personal or confidential information in the submitted version unless intentionally identifying the respondent.

## Executive Summary

Canada should treat AI transparency as an operational accountability system, not merely as a disclosure exercise. A label that says "AI was used" can be useful, but it does not by itself let a person contest a decision, help a business assess a vendor, or help a regulator reconstruct what happened after an incident. Transparency becomes trustworthy only when it produces usable evidence, clear decision rights, and practical routes to interruption, correction, escalation, and review.

This submission recommends a proportionate Canadian approach built around four linked instruments:

1. A Canadian AI Transparency Packet standard for developers, deployers, and procurers.
2. Tiered disclosure duties that distinguish public notices, affected-person explanations, business due diligence, and regulator access.
3. Serious AI incident and near-miss reporting designed around harm, recurrence risk, and evidence preservation.
4. Agentic AI transparency requirements focused on identity, authority, tool use, logs, and chain of custody.

The main principle is simple: transparency should answer "what can I do with this information?" If a Canadian is told that an AI system affected them, they should know who used it, for what purpose, what consequence followed, what evidence exists, and how to challenge or correct the result. If a business is asked to adopt an AI tool, it should be able to inspect the system's role, limitations, data dependencies, oversight requirements, logging capacity, change history, and incident route. If a regulator or researcher needs to understand emerging harms, the relevant evidence should not be scattered across vendors, platforms, integrators, and deployers in incompatible formats.

Transparency is most important in high-stakes contexts: public services, employment, credit, insurance, housing, education, health, policing, immigration, legal services, child-facing systems, elections, fraud-sensitive content, and autonomous or semi-autonomous agentic workflows. It is less urgent for low-risk, routine, and clearly assistive uses such as spelling correction, formatting assistance, or internal productivity tools that do not materially affect rights, access, safety, finances, reputation, or democratic participation.

Canada should avoid two extremes. The first is under-regulation: generic "AI may be used" notices, voluntary principles, and AI literacy campaigns that leave affected people with no route to act. The second is over-broad formalism: requiring every AI-assisted output or low-risk internal workflow to carry the same burden as high-stakes decision systems. The better path is risk-sensitive, evidence-based, and interoperable with provincial, territorial, and international frameworks.

## Core Principle: Transparency Must Be Usable

The Government's discussion paper correctly recognizes that transparency can support informed decision-making, accountability, good business practices, and future public intervention. The key design question is whether the disclosed information can actually be used by the person or institution receiving it.

Different audiences need different kinds of transparency. A citizen interacting with a benefits portal does not need the same document as a bank procuring an AI vendor, a regulator investigating an incident, or a researcher studying systemic harms. A useful transparency regime should therefore define the audience, context, purpose, and consequence of disclosure before defining the content of disclosure.

A practical Canadian framework should distinguish at least four levels:

1. Public notice: simple, clear information that AI is used, why it is used, and where more information or recourse can be found.
2. Affected-person explanation: case-relevant information for people materially affected by an AI-supported decision, including how to contest, correct, or escalate.
3. Business and procurement due diligence: structured documentation that lets customers and partners assess risks before adopting or integrating an AI system.
4. Regulator and incident evidence: deeper technical and operational records available through protected channels when there is material harm, systemic risk, or credible investigation.

This tiered approach protects confidential business information while still giving Canadians meaningful transparency. It also avoids the mistake of treating transparency as a single document. In practice, transparency is a chain: disclosure, evidence, decision rights, monitoring, incident response, and revision.

## Recommended Instrument: The Canadian AI Transparency Packet

Canada should develop a voluntary standard, reinforced through federal procurement and risk-based regulation where necessary, for an AI Transparency Packet. The packet should not be a marketing document. It should be a structured evidence artifact that helps organizations and public authorities understand what an AI system is, what it does, what it does not do, and what controls surround it.

At minimum, the packet should include:

1. System identity: name, version, provider, deployer, integration context, and date.
2. Use-case description: what the system is intended to do, where it is deployed, and what decisions or outputs it influences.
3. Value-chain role map: developer, deployer, integrator, data provider, platform, and operator responsibilities.
4. Data information: high-level data categories, provenance where appropriate, update cycles, known data limitations, and privacy constraints.
5. Capability and limitation summary: supported tasks, known failure modes, unsuitable uses, and prohibited claims.
6. Human oversight model: who reviews, who can override, who can halt, who is notified, and who reviews after the fact.
7. Logging and evidence trail: what is logged, where logs are retained, how long they are retained, and how they can be retrieved during review.
8. Claims and non-claims register: what the vendor or deployer can support with evidence and what it explicitly does not claim.
9. Change and supersession log: material changes to models, prompts, data sources, interfaces, policy settings, or agent permissions.
10. Incident and escalation route: how failures, harms, near misses, and complaints are detected, reported, triaged, and corrected.

This packet could be scaled by risk and role. A small business deploying a low-risk chatbot should not face the same requirements as a company selling an AI hiring tool, a healthcare triage system, or an autonomous procurement agent. But every organization should be able to answer the basic governance question: if the system fails, what record allows another person to reconstruct what happened?

## AI-Generated Content

Canadians need to know when AI-generated or AI-manipulated content materially changes what they are being asked to believe. The highest-priority contexts are those where synthetic content can misrepresent reality, impersonate a person, distort democratic debate, enable fraud, exploit children, simulate evidence, or damage reputation. This includes realistic images, video, audio, political communications, public-interest journalism, emergency information, health information, investment material, and content that appears to show a real person saying or doing something they did not say or do.

Not every AI-assisted artifact should be treated the same way. A document corrected for grammar, an image resized with an AI tool, or a routine accessibility transformation does not raise the same transparency concern as a synthetic video of a public figure or an AI-generated health claim. The policy distinction should be between AI assistance that changes form and AI generation or manipulation that changes evidentiary meaning.

The strongest approach is layered:

1. Visible disclosure for high-risk or realism-claiming content.
2. Invisible or machine-readable provenance metadata where technically feasible.
3. Platform preservation of provenance metadata rather than stripping it during upload or compression.
4. Public education that teaches people how to interpret labels without assuming labels are proof of truth.
5. Enforcement against deceptive removal, alteration, or misrepresentation of provenance information.

Watermarks and provenance metadata should be treated as useful but incomplete. They can be removed, fail across platforms, or create false confidence. For that reason, Canada should avoid building the entire policy approach around detection. The central question is not only whether AI was used; it is whether the content is presented in a way that deceives people about origin, authorship, evidence, consent, or reality.

Responsibility should be shared across the value chain:

1. Developers should build provenance, watermarking, labeling, and documentation capabilities into systems that generate realistic synthetic media.
2. Deployers and publishers should disclose when they use AI-generated or materially AI-manipulated content in contexts where the disclosure affects interpretation.
3. Platforms should preserve provenance metadata, support consistent label display, and provide reporting channels for deceptive synthetic media.
4. Advertisers, campaigns, and organizations publishing public-interest content should carry final responsibility for the claims they distribute.

Current market practice is not sufficient. Labels vary, metadata is fragile, incentives are uneven, and deceptive actors will not self-disclose. Government action should focus on interoperability, public-interest contexts, procurement expectations, standards work, and targeted obligations for realistic synthetic media that creates material deception risk. Broad labeling of every AI-assisted artifact would create noise and train the public to ignore the label.

## AI Interaction

It is most important to know that one is interacting with AI when the interaction creates dependency, emotional reliance, material consequence, or an obstacle to human recourse. The priority contexts include public services, healthcare, mental health, education, banking, insurance, employment, housing, immigration, legal services, customer complaint resolution, debt collection, child-facing systems, and companion or relationship-simulating chatbots.

Disclosure is less important where AI is clearly incidental, low-risk, or already expected as part of a familiar tool. For example, autocomplete, spelling correction, spam filtering, routing of a non-sensitive inquiry, or internal search may not need prominent disclosure every time. However, even low-risk uses should become more transparent if the person cannot reach a human, if the system gathers sensitive data, or if the interaction affects a decision.

An effective disclosure should be:

1. Just-in-time: shown when it matters, not buried in terms of service.
2. Specific: explaining what the AI is doing in that interaction.
3. Consequence-aware: stating whether the AI can affect a decision, recommendation, delay, refusal, or escalation.
4. Actionable: telling the person how to reach a human, contest the result, correct information, or complain.
5. Plain-language: understandable without technical vocabulary.
6. Non-deceptive: not using anthropomorphic design to make a machine interaction appear human.

The deployer should normally be responsible for interaction transparency because the deployer controls the user relationship and the operational context. Developers should be required to provide deployers with the information and technical hooks needed to disclose accurately. Contract terms between developers and deployers should allocate transparency duties explicitly. When a platform or vendor provides a hosted AI system directly to the public, it is both developer and deployer for practical purposes and should carry the corresponding responsibility.

Current practice is not sufficient. Many notices say only that AI "may" be used. That does not tell the user what the system is doing, whether the user has a choice, whether the output is reviewed by a human, or how to challenge the result. A Canadian approach should define minimum content for AI interaction notices in high-impact contexts and should require disclosure to be connected to a recourse route.

The phrase "human in the loop" should not be accepted as a transparency answer unless it is decomposed into decision rights. The useful questions are: which human sees the relevant evidence, which human can refuse, which human can override, which human can halt, which human is notified, which human reviews after the fact, and which artifact proves that the intervention happened? Without those answers, human oversight can become a comfort phrase rather than an accountability structure.

## Information About AI Systems

Canadians need different information depending on whether they are general users, affected individuals, business adopters, civil society researchers, or regulators. For ordinary use, the most useful information is practical: what the system is for, whether AI is involved, whether the output may be wrong, whether personal information is used, whether a decision may be affected, and how to obtain review.

For affected individuals, transparency should become more concrete. A person denied a service, flagged for risk, ranked for opportunity, or routed away from human review needs case-relevant information. They do not need to receive trade secrets, but they should know that AI was involved, the purpose of the system, the category of information relied on, the role of human review, the reason category for the result, and the available route to contest or correct the decision.

Businesses need stronger due diligence information before adoption. They need to know:

1. The system's intended and prohibited uses.
2. The provider's role in the value chain.
3. The model or system version and material update practices.
4. Relevant data sources or data categories.
5. Known limitations, failure modes, and evaluation boundaries.
6. Security, privacy, and logging capabilities.
7. Human oversight requirements.
8. Incident history or incident categories where appropriate.
9. Subprocessor, model-provider, or third-party dependency information.
10. Evidence that governance controls are operating, not merely described.

In procurement and regulated industries, trust is an audit artifact. Buyers are not simply asking whether the product works. They are asking whether the decision to use it can be defended if the system later fails. "Responsible AI," "human oversight," or "aligned with leading frameworks" are weak claims unless mapped to owners, controls, evidence, and review triggers.

Confidential business information can be protected through tiered disclosure. Canada should not require public disclosure of sensitive model weights, security-sensitive details, proprietary training recipes, or information that could enable abuse. Instead, it should define disclosure levels:

1. Public summary for ordinary users and the public.
2. Affected-person explanation for people materially affected by a system.
3. Customer due-diligence packet, possibly under confidentiality terms.
4. Regulator-accessible technical and operational records in protected review channels.
5. Aggregated public reporting for systemic trends, incidents, and adoption patterns.

This model avoids the false choice between secrecy and full publication. It asks the right actor to provide the right information to the right audience under the right access conditions.

## AI Incidents

The public and government do not yet have enough structured information about AI-related incidents, near misses, and emerging harms. AI failures often appear as ordinary operational failures: a rejected application, a bad recommendation, a biased ranking, a harmful chatbot interaction, a fraudulent image, a misrouted service request, a privacy breach, or a tool that silently changes workflow. Without a shared incident language, these events remain fragmented and difficult to learn from.

Canada should define serious AI incidents by consequence and recurrence risk, not only by technology category. A serious AI incident should include at least:

1. Death, bodily injury, or credible risk of severe physical harm.
2. Material denial, delay, or distortion of access to public services, employment, housing, credit, insurance, healthcare, education, immigration, or legal rights.
3. Discriminatory or systematically unequal outcomes affecting protected or vulnerable groups.
4. Significant financial loss, fraud, extortion, or impersonation enabled or amplified by AI.
5. Material privacy breach, unauthorized disclosure, or misuse of sensitive data involving an AI system.
6. Election, democratic, or public-safety interference through realistic synthetic media or automated influence operations.
7. Loss of control, unauthorized action, or unsafe tool use by an AI agent.
8. Repeated near misses showing a pattern of foreseeable harm.
9. Failure of a required control, such as logging, human review, escalation, or rollback.

Incident reporting should capture enough information to support learning and accountability:

1. System identity and version.
2. Deployment context and use case.
3. Role of AI in the event.
4. Actors in the value chain.
5. Timeline of detection, escalation, and mitigation.
6. Affected population or group, where known.
7. Type and severity of harm.
8. Evidence retained, including logs and decision records.
9. Known or suspected cause.
10. Corrective actions, rollback, user notification, and recurrence controls.
11. Whether the incident is resolved, unresolved, disputed, or under investigation.

Canada should also collect near misses in high-stakes contexts. Near misses are where prevention improves fastest. A chatbot that almost disclosed sensitive information, an AI agent blocked before it executed an unauthorized transaction, or a scoring system caught before use can reveal weaknesses before Canadians are harmed.

Reporting requirements should encourage proactive disclosure. Organizations are often reluctant to report incidents because of reputational, liability, and confidentiality concerns. Canada should consider protected reporting channels, tiered public disclosure, safe-harbour treatment for timely good-faith reporting, and separation between immediate safety reporting and later enforcement decisions. This does not mean immunity for negligence or concealment. It means the system should not punish early learning so harshly that organizations hide incidents until harm becomes undeniable.

Existing Canadian incident regimes provide useful analogies but are not sufficient on their own. Product safety, medical device, privacy breach, transportation, cybersecurity, and workplace reporting regimes each capture parts of the problem. AI incidents cut across those domains and add distinctive features: model opacity, upstream/downstream value-chain fragmentation, fast version changes, synthetic content, automated interaction, and agentic tool use. Canada should create an interoperable AI incident taxonomy that can connect to existing regulators rather than replacing them.

## AI Agents

AI agents raise a different transparency problem from ordinary chatbots because they can take actions, call tools, interact with systems, communicate externally, transact, retrieve data, delegate subtasks, or operate through multi-step workflows. The transparency question is not only "am I speaking with AI?" It is "what is this agent allowed to do, under whose authority, with what tools, and what evidence will exist after it acts?"

Concern is highest where agents can:

1. Spend money or authorize transactions.
2. Communicate externally on behalf of a person or organization.
3. Access personal, confidential, financial, health, legal, or employment data.
4. Affect public services or rights.
5. Modify records, documents, code, infrastructure, or contracts.
6. Interact with other agents or third-party tools.
7. Continue operating after the user stops actively supervising.
8. Simulate a human representative in a way that creates reliance.

Agent transparency should include both disclosure and observability. Disclosure tells people and organizations that an agent is in use. Observability lets the responsible organization reconstruct what the agent did.

At minimum, deployers of material AI agents should record:

1. Agent identity, version, owner, and deployment context.
2. Scope of authority and prohibited actions.
3. Tools and systems the agent can access.
4. Permissions granted and changes to those permissions.
5. Human approval thresholds.
6. Tool invocations, external communications, and transactions.
7. Inputs, retrieved sources, and output destinations where proportionate.
8. Agent-to-agent interactions and chain of custody.
9. Exceptions, refusals, blocked actions, and escalation events.
10. Kill switch, rollback, and incident procedures.

Businesses need this information before confidently using agents. They need to know what the agent can do, what it cannot do, what it logs, what can be audited, how authority is delegated, where human approval is required, what happens after a tool failure, and who is liable for unauthorized or harmful actions. Many current market tools provide partial logging or observability, but practices are still immature and inconsistent.

Government action should focus on standards and procurement before imposing broad, technology-specific obligations on all agent use. Canada should support interoperable agent observability standards, identity credentials for agent interactions, common logging semantics, sandboxing guidance, and procurement clauses requiring agent activity records. Binding obligations should apply first to high-impact and externally acting agents rather than to every internal workflow assistant.

The core accountability test should be reconstructability. If an agent affects a person, a record, a transaction, a public service, or a contractual obligation, another actor should be able to reconstruct the route from instruction to action to consequence.

## Cross-Cutting Considerations

AI transparency is most important when a person, business, regulator, or researcher must act on the information. It is especially important where AI affects rights, access, safety, money, public trust, children, democratic participation, or recourse. It is also important where power is uneven: an individual against an institution, a small supplier against a large procurement process, a patient against a health system, a worker against an automated assessment tool, or a citizen against a public authority.

Some action would be premature. Canada should avoid broad rules that require identical treatment of low-risk and high-risk AI uses. It should avoid requiring public disclosure of sensitive security details or proprietary information where protected regulator access would be more appropriate. It should avoid treating public AI literacy as a substitute for institutional duties. And it should avoid purely symbolic transparency requirements that create labels but no contestability, correction, or evidence trail.

For small and medium-sized enterprises, proportionality is essential. SMEs need templates, examples, shared infrastructure, and staged requirements. A small firm should not have to invent an AI governance program from scratch in order to answer a basic customer questionnaire or deploy a low-risk tool responsibly. The federal government can help by publishing model AI Transparency Packets, standard questionnaire formats, plain-language disclosure templates, open-source logging and provenance tools, procurement-ready checklists, and guidance scaled by role and risk.

At the same time, SME proportionality should not mean SME exemption where serious harm is possible. A small vendor can still deploy a high-impact system. The obligation should follow the risk and role, not only the size of the organization. The more a system affects rights, safety, money, access, public trust, or autonomous action, the stronger the transparency and evidence obligations should be.

Federal coherence should be built through interoperability. Canada should align with provincial and territorial privacy, labour, consumer protection, human rights, and sectoral regulators while providing a common federal vocabulary for AI transparency. The federal government is well placed to coordinate standards, procurement expectations, incident taxonomy, intergovernmental learning, and international alignment. Relevant international approaches include the EU AI Act's transparency provisions, risk-management frameworks such as NIST AI RMF, management-system standards such as ISO/IEC 42001, and emerging agent observability standards.

To account for continuing technical change, Canada should define transparency obligations around function, risk, evidence, and consequence rather than around a fixed list of model types. The law and guidance should ask what the system does, whom it affects, what authority it exercises, what evidence is available, what rights or interests are at stake, and what happens when it fails. This will age better than rules tied only to current product categories.

## Implementation Path

Canada can move in stages:

1. Short term: publish guidance, templates, and model AI Transparency Packets for voluntary adoption and federal procurement.
2. Short term: define high-priority disclosure contexts for AI-generated content, AI interactions, and agentic workflows.
3. Medium term: create an AI incident taxonomy and protected reporting pathway for serious incidents and near misses.
4. Medium term: require federal procurement of AI systems to include transparency packets, logging commitments, change notifications, incident routes, and claims/non-claims registers.
5. Longer term: consider targeted regulation for high-impact AI systems, realistic synthetic media used in public-interest contexts, and externally acting AI agents.

Procurement is the fastest practical lever. If the Government of Canada asks vendors for structured transparency evidence, the market will adapt quickly. This also helps SMEs by standardizing what customers ask for, rather than leaving each buyer to invent a different questionnaire.

## Closing

The question is not whether Canada should choose innovation or accountability. The question is whether Canada can design transparency in a way that makes responsible adoption easier to prove. The public will not trust AI because institutions say "AI was used" or "humans supervise it." Businesses will not trust vendors because they claim alignment with principles. Regulators will not understand emerging harms if incident evidence disappears into private logs and incompatible formats.

Trustworthy AI transparency should leave a usable trail. It should tell Canadians when AI matters, what role it played, who is responsible, what evidence exists, and what route is available to interrupt or correct the result. That is the difference between transparency as a label and transparency as democratic infrastructure.

## Internal Drafting Sources - Not For Submission

Official consultation materials:

- Local PDF: `M:\Enhancing trust in artificial intelligence through increased transparency-GOV-CAN.pdf`
- Local PDF: `M:\Formulaire-AI-GOVCAN.pdf`
- ISED consultation page verified 2026-07-31: open July 23 to September 23, 2026.

Vault basis:

- `transparency-without-interruption-is-still-discretion.md` - core argument that transparency must include interruption, contestation, correction, and review.
- `trust-is-an-audit-artifact.md` - trust as evidence and due-diligence burden, not tone.
- `the-control-is-the-evidence-trail.md` - governance as reconstructible control chain and evidence hierarchy.
- `human-in-the-loop-is-not-an-accountability-structure.md` - oversight decomposed into visibility, authority, refusal, escalation, monitoring, and records.
- `the-customer-becomes-the-regulator-before-the-regulator-arrives.md` - procurement and contract pressure as practical enforcement.
- `wiki/Governance Controls and Mechanisms.md` - control, monitoring, incident-response, and verification vocabulary.
- `resources/NIST AI RMF 1.0 — NIST AI 100-1 (2023).md` - Govern/Map/Measure/Manage alignment.
- `resources/Regulatory Standards Reference Stack — Governance Controls Grounding.md` - standards and control-grounding vocabulary.
- `Areas/PHAROS/company.md` - PHAROS operational context and positioning.
