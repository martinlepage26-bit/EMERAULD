---
type: raw
source_kind: pdf_text
source_path: /mnt/d/LIBRARY/Review/Unreadable/2023 - journal_article.pdf - 2023 - journal_article.pdf.pdf - 2023 - journal_article.pdf - 2023 - journal_article.pdf.pdf.pdf
source_rel: Review/Unreadable/2023 - journal_article.pdf - 2023 - journal_article.pdf.pdf - 2023 - journal_article.pdf - 2023 - journal_article.pdf.pdf.pdf
pages_total: 48
text_first_pages: 12
text_last_pages: 2
pdfinfo:
  Author: "National Institute of Standards and Technology"
  CreationDate: "Tue Jan 24 14:45:46 2023 EST"
  Creator: "LaTeX with hyperref"
  Custom Metadata: "yes"
  Encrypted: "no"
  File size: "1946127 bytes"
  Form: "none"
  JavaScript: "no"
  Keywords: "Artificial Intelligence (AI); AI; AI RMF; AI RMF 1.0; AI systems; trustworthy and responsible AI."
  Metadata Stream: "yes"
  ModDate: "Wed Jun  4 13:01:45 2025 EDT"
  Optimized: "yes"
  PDF version: "1.7"
  Page rot: "0"
  Page size: "612 x 792 pts (letter)"
  Pages: "48"
  Producer: "pdfTeX-1.40.24"
  Subject: "As directed by the National Artificial Intelligence Initiative Act of 2020 (P.L. 116-283), the goal of the AI RMF is to offer a resource to the organizations designing, developing, deploying, or using AI systems to help manage the many risks of AI and promote trustworthy and responsible development and use of AI systems. The Framework is intended to be voluntary, rights-preserving, non-sector specific, and use-case agnostic, providing flexibility to organizations of all sizes and in all sectors and throughout society to implement the approaches in the Framework. The AI RMF is intended to be practical, to adapt to the AI landscape as AI technologies continue to develop, and to be operationalized by organizations in varying degrees and capacities so society can benefit from AI while also being protected from its potential harms."
  Suspects: "no"
  Tagged: "no"
  Title: "Artificial Intelligence Risk Management Framework (AI RMF 1.0)"
  UserProperties: "no"
dr_sort_original_filename: "2023 - journal_article.pdf - 2023 - journal_article.pdf.pdf - 2023 - journal_article.pdf - 2023 - journal_article.pdf.pdf.pdf.md"
dr_sort_original_path: "raw sources/D_LIBRARY_ingest_2026-04-26/ocr_unreadable/converted_ocr/Review/Unreadable/2023 - journal_article.pdf - 2023 - journal_article.pdf.pdf - 2023 - journal_article.pdf - 2023 - journal_article.pdf.pdf.pdf.md"
dr_sort_filename_normalized: "2026-05-06"
---

# Artificial Intelligence Risk Management Framework (AI RMF 1.0)

## Extracted Text

NIST AI 100-1

Artificial Intelligence Risk Management
Framework (AI RMF 1.0)

NIST AI 100-1

Artificial Intelligence Risk Management
Framework (AI RMF 1.0)

This publication is available free of charge from:
https://doi.org/10.6028/NIST.AI.100-1

January 2023

U.S. Department of Commerce
Gina M. Raimondo, Secretary
National Institute of Standards and Technology
Laurie E. Locascio, NIST Director and Under Secretary of Commerce for Standards and Technology

Certain commercial entities, equipment, or materials may be identified in this document in order to describe
an experimental procedure or concept adequately. Such identification is not intended to imply recommendation or endorsement by the National Institute of Standards and Technology, nor is it intended to imply that
the entities, materials, or equipment are necessarily the best available for the purpose.

This publication is available free of charge from: https://doi.org/10.6028/NIST.AI.100-1

Update Schedule and Versions
The Artificial Intelligence Risk Management Framework (AI RMF) is intended to be a living document.
NIST will review the content and usefulness of the Framework regularly to determine if an update is appropriate; a review with formal input from the AI community is expected to take place no later than 2028. The
Framework will employ a two-number versioning system to track and identify major and minor changes. The
first number will represent the generation of the AI RMF and its companion documents (e.g., 1.0) and will
change only with major revisions. Minor revisions will be tracked using “.n” after the generation number
(e.g., 1.1). All changes will be tracked using a Version Control Table which identifies the history, including
version number, date of change, and description of change. NIST plans to update the AI RMF Playbook
frequently. Comments on the AI RMF Playbook may be sent via email to AIframework@nist.gov at any time
and will be reviewed and integrated on a semi-annual basis.

Table of Contents
Executive Summary

1

Part 1: Foundational Information

4

1 Framing Risk
1.1 Understanding and Addressing Risks, Impacts, and Harms
1.2 Challenges for AI Risk Management
1.2.1 Risk Measurement
1.2.2 Risk Tolerance
1.2.3 Risk Prioritization
1.2.4 Organizational Integration and Management of Risk

4
4
5
5
7
7
8

2 Audience

9

3 AI Risks and Trustworthiness
3.1 Valid and Reliable
3.2 Safe
3.3 Secure and Resilient
3.4 Accountable and Transparent
3.5 Explainable and Interpretable
3.6 Privacy-Enhanced
3.7 Fair – with Harmful Bias Managed

12
13
14
15
15
16
17
17

4 Effectiveness of the AI RMF

19

Part 2: Core and Profiles

20

5 AI RMF Core
5.1 Govern
5.2 Map
5.3 Measure
5.4 Manage

20
21
24
28
31

6 AI RMF Profiles

33

Appendix A: Descriptions of AI Actor Tasks from Figures 2 and 3

35

Appendix B: How AI Risks Differ from Traditional Software Risks

38

Appendix C: AI Risk Management and Human-AI Interaction

40

Appendix D: Attributes of the AI RMF

42

List of Tables
Table 1 Categories and subcategories for the GOVERN function.
Table 2 Categories and subcategories for the MAP function.
Table 3 Categories and subcategories for the MEASURE function.
Table 4 Categories and subcategories for the MANAGE function.
i

22
26
29
32

AI RMF 1.0

NIST AI 100-1

List of Figures
Fig. 1 Examples of potential harms related to AI systems. Trustworthy AI systems
and their responsible use can mitigate negative risks and contribute to benefits for people, organizations, and ecosystems.
Fig. 2 Lifecycle and Key Dimensions of an AI System. Modified from OECD
(2022) OECD Framework for the Classification of AI systems — OECD
Digital Economy Papers. The two inner circles show AI systems’ key dimensions and the outer circle shows AI lifecycle stages. Ideally, risk management efforts start with the Plan and Design function in the application
context and are performed throughout the AI system lifecycle. See Figure 3
for representative AI actors.
Fig. 3 AI actors across AI lifecycle stages. See Appendix A for detailed descriptions of AI actor tasks, including details about testing, evaluation, verification, and validation tasks. Note that AI actors in the AI Model dimension
(Figure 2) are separated as a best practice, with those building and using the
models separated from those verifying and validating the models.
Fig. 4 Characteristics of trustworthy AI systems. Valid & Reliable is a necessary
condition of trustworthiness and is shown as the base for other trustworthiness characteristics. Accountable & Transparent is shown as a vertical box
because it relates to all other characteristics.
Fig. 5 Functions organize AI risk management activities at their highest level to
govern, map, measure, and manage AI risks. Governance is designed to be
a cross-cutting function to inform and be infused throughout the other three
functions.

5

10

11

12

20

Page ii

NIST AI 100-1

AI RMF 1.0

Executive Summary
Artificial intelligence (AI) technologies have significant potential to transform society and
people’s lives – from commerce and health to transportation and cybersecurity to the environment and our planet. AI technologies can drive inclusive economic growth and support
scientific advancements that improve the conditions of our world. AI technologies, however, also pose risks that can negatively impact individuals, groups, organizations, communities, society, the environment, and the planet. Like risks for other types of technology, AI
risks can emerge in a variety of ways and can be characterized as long- or short-term, highor low-probability, systemic or localized, and high- or low-impact.
The AI RMF refers to an AI system as an engineered or machine-based system that
can, for a given set of objectives, generate outputs such as predictions, recommendations, or decisions influencing real or virtual environments. AI systems are designed
to operate with varying levels of autonomy (Adapted from: OECD Recommendation
on AI:2019; ISO / IEC 22989:2022).
While there are myriad standards and best practices to help organizations mitigate the risks
of traditional software or information-based systems, the risks posed by AI systems are in
many ways unique (See Appendix B). AI systems, for example, may be trained on data that
can change over time, sometimes significantly and unexpectedly, affecting system functionality and trustworthiness in ways that are hard to understand. AI systems and the contexts
in which they are deployed are frequently complex, making it difficult to detect and respond
to failures when they occur. AI systems are inherently socio-technical in nature, meaning
they are influenced by societal dynamics and human behavior. AI risks – and benefits –
can emerge from the interplay of technical aspects combined with societal factors related
to how a system is used, its interactions with other AI systems, who operates it, and the
social context in which it is deployed.
These risks make AI a uniquely challenging technology to deploy and utilize both for organizations and within society. Without proper controls, AI systems can amplify, perpetuate,
or exacerbate inequitable or undesirable outcomes for individuals and communities. With
proper controls, AI systems can mitigate and manage inequitable outcomes.
AI risk management is a key component of responsible development and use of AI systems. Responsible AI practices can help align the decisions about AI system design, development, and uses with intended aim and values. Core concepts in responsible AI emphasize human centricity, social responsibility, and sustainability. AI risk management can
drive responsible uses and practices by prompting organizations and their internal teams
who design, develop, and deploy AI to think more critically about context and potential
or unexpected negative and positive impacts. Understanding and managing the risks of AI
systems will help to enhance trustworthiness, and in turn, cultivate public trust.

Page 1

NIST AI 100-1

AI RMF 1.0

Social responsibility can refer to the organization’s responsibility “for the impacts
of its decisions and activities on society and the environment through transparent
and ethical behavior” (ISO 26000:2010). Sustainability refers to the “state of the
global system, including environmental, social, and economic aspects, in which the
needs of the present are met without compromising the ability of future generations
to meet their own needs” (ISO / IEC TR 24368:2022). Responsible AI is meant to
result in technology that is also equitable and accountable. The expectation is that
organizational practices are carried out in accord with “professional responsibility,”
defined by ISO as an approach that “aims to ensure that professionals who design,
develop, or deploy AI systems and applications or AI-based products or systems,
recognize their unique position to exert influence on people, society, and the future
of AI” (ISO / IEC TR 24368:2022).
As directed by the National Artificial Intelligence Initiative Act of 2020 (P.L. 116-283),
the goal of the AI RMF is to offer a resource to the organizations designing, developing,
deploying, or using AI systems to help manage the many risks of AI and promote trustworthy and responsible development and use of AI systems. The Framework is intended to be
voluntary, rights-preserving, non-sector-specific, and use-case agnostic, providing flexibility to organizations of all sizes and in all sectors and throughout society to implement the
approaches in the Framework.
The Framework is designed to equip organizations and individuals – referred to here as
AI actors – with approaches that increase the trustworthiness of AI systems, and to help
foster the responsible design, development, deployment, and use of AI systems over time.
AI actors are defined by the Organisation for Economic Co-operation and Development
(OECD) as “those who play an active role in the AI system lifecycle, including organizations and individuals that deploy or operate AI” [OECD (2019) Artificial Intelligence in
Society—OECD iLibrary] (See Appendix A).
The AI RMF is intended to be practical, to adapt to the AI landscape as AI technologies
continue to develop, and to be operationalized by organizations in varying degrees and
capacities so society can benefit from AI while also being protected from its potential
harms.
The Framework and supporting resources will be updated, expanded, and improved based
on evolving technology, the standards landscape around the world, and AI community experience and feedback. NIST will continue to align the AI RMF and related guidance with
applicable international standards, guidelines, and practices. As the AI RMF is put into
use, additional lessons will be learned to inform future updates and additional resources.
The Framework is divided into two parts. Part 1 discusses how organizations can frame
the risks related to AI and describes the intended audience. Next, AI risks and trustworthiness are analyzed, outlining the characteristics of trustworthy AI systems, which include
Page 2

NIST AI 100-1

AI RMF 1.0

valid and reliable, safe, secure and resilient, accountable and transparent, explainable and
interpretable, privacy enhanced, and fair with their harmful biases managed.
Part 2 comprises the “Core” of the Framework. It describes four specific functions to help
organizations address the risks of AI systems in practice. These functions – GOVERN,
MAP , MEASURE , and MANAGE – are broken down further into categories and subcategories. While GOVERN applies to all stages of organizations’ AI risk management processes and procedures, the MAP, MEASURE, and MANAGE functions can be applied in AI
system-specific contexts and at specific stages of the AI lifecycle.
Additional resources related to the Framework are included in the AI RMF Playbook,
which is available via the NIST AI RMF website:
https://www.nist.gov/itl/ai-risk-management-framework.
Development of the AI RMF by NIST in collaboration with the private and public sectors is directed and consistent with its broader AI efforts called for by the National AI
Initiative Act of 2020, the National Security Commission on Artificial Intelligence recommendations, and the Plan for Federal Engagement in Developing Technical Standards and
Related Tools. Engagement with the AI community during this Framework’s development
– via responses to a formal Request for Information, three widely attended workshops,
public comments on a concept paper and two drafts of the Framework, discussions at multiple public forums, and many small group meetings – has informed development of the AI
RMF 1.0 as well as AI research and development and evaluation conducted by NIST and
others. Priority research and additional guidance that will enhance this Framework will be
captured in an associated AI Risk Management Framework Roadmap to which NIST and
the broader community can contribute.

Page 3

NIST AI 100-1

AI RMF 1.0

Part 1: Foundational Information
1.

Framing Risk

AI risk management offers a path to minimize potential negative impacts of AI systems,
such as threats to civil liberties and rights, while also providing opportunities to maximize
positive impacts. Addressing, documenting, and managing AI risks and potential negative
impacts effectively can lead to more trustworthy AI systems.
1.1

Understanding and Addressing Risks, Impacts, and Harms

In the context of the AI RMF, risk refers to the composite measure of an event’s probability
of occurring and the magnitude or degree of the consequences of the corresponding event.
The impacts, or consequences, of AI systems can be positive, negative, or both and can
result in opportunities or threats (Adapted from: ISO 31000:2018). When considering the
negative impact of a potential event, risk is a function of 1) the negative impact, or magnitude of harm, that would arise if the circumstance or event occurs and 2) the likelihood of
occurrence (Adapted from: OMB Circular A-130:2016). Negative impact or harm can be
experienced by individuals, groups, communities, organizations, society, the environment,
and the planet.
“Risk management refers to coordinated activities to direct and control an organization with regard to risk” (Source: ISO 31000:2018).
While risk management processes generally address negative impacts, this Framework offers approaches to minimize anticipated negative impacts of AI systems and identify opportunities to maximize positive impacts. Effectively managing the risk of potential harms
could lead to more trustworthy AI systems and unleash potential benefits to people (individuals, communities, and society), organizations, and systems/ecosystems. Risk management
can enable AI developers and users to understand impacts and account for the inherent limitations and uncertainties in their models and systems, which in turn can improve overall
system performance and trustworthiness and the likelihood that AI technologies will be
used in ways that are beneficial.
The AI RMF is designed to address new risks as they emerge. This flexibility is particularly
important where impacts are not easily foreseeable and applications are evolving. While
some AI risks and benefits are well-known, it can be challenging to assess negative impacts
and the degree of harms. Figure 1 provides examples of potential harms that can be related
to AI systems.
AI risk management efforts should consider that humans may assume that AI systems work
– and work well – in all settings. For example, whether correct or not, AI systems are
often perceived as being more objective than humans or as offering greater capabilities
than general software.
Page 4

NIST AI 100-1

AI RMF 1.0

Fig. 1. Examples of potential harms related to AI systems. Trustworthy AI systems and their
responsible use can mitigate negative risks and contribute to benefits for people, organizations, and
ecosystems.

1.2

Challenges for AI Risk Management

Several challenges are described below. They should be taken into account when managing
risks in pursuit of AI trustworthiness.
1.2.1

Risk Measurement

AI risks or failures that are not well-defined or adequately understood are difficult to measure quantitatively or qualitatively. The inability to appropriately measure AI risks does not
imply that an AI system necessarily poses either a high or low risk. Some risk measurement
challenges include:
Risks related to third-party software, hardware, and data: Third-party data or systems
can accelerate research and development and facilitate technology transition. They also
may complicate risk measurement. Risk can emerge both from third-party data, software or
hardware itself and how it is used. Risk metrics or methodologies used by the organization
developing the AI system may not align with the risk metrics or methodologies uses by
the organization deploying or operating the system. Also, the organization developing
the AI system may not be transparent about the risk metrics or methodologies it used. Risk
measurement and management can be complicated by how customers use or integrate thirdparty data or systems into AI products or services, particularly without sufficient internal
governance structures and technical safeguards. Regardless, all parties and AI actors should
manage risk in the AI systems they develop, deploy, or use as standalone or integrated
components.
Tracking emergent risks: Organizations’ risk management efforts will be enhanced by
identifying and tracking emergent risks and considering techniques for measuring them.
Page 5

NIST AI 100-1

AI RMF 1.0

AI system impact assessment approaches can help AI actors understand potential impacts
or harms within specific contexts.
Availability of reliable metrics: The current lack of consensus on robust and verifiable
measurement methods for risk and trustworthiness, and applicability to different AI use
cases, is an AI risk measurement challenge. Potential pitfalls when seeking to measure
negative risk or harms include the reality that development of metrics is often an institutional endeavor and may inadvertently reflect factors unrelated to the underlying impact. In
addition, measurement approaches can be oversimplified, gamed, lack critical nuance, become relied upon in unexpected ways, or fail to account for differences in affected groups
and contexts.
Approaches for measuring impacts on a population work best if they recognize that contexts
matter, that harms may affect varied groups or sub-groups differently, and that communities
or other sub-groups who may be harmed are not always direct users of a system.
Risk at different stages of the AI lifecycle: Measuring risk at an earlier stage in the AI
lifecycle may yield different results than measuring risk at a later stage; some risks may
be latent at a given point in time and may increase as AI systems adapt and evolve. Furthermore, different AI actors across the AI lifecycle can have different risk perspectives.
For example, an AI developer who makes AI software available, such as pre-trained models, can have a different risk perspective than an AI actor who is responsible for deploying
that pre-trained model in a specific use case. Such deployers may not recognize that their
particular uses could entail risks which differ from those perceived by the initial developer.
All involved AI actors share responsibilities for designing, developing, and deploying a
trustworthy AI system that is fit for purpose.
Risk in real-world settings: While measuring AI risks in a laboratory or a controlled
environment may yield important insights pre-deployment, these measurements may differ
from risks that emerge in operational, real-world settings.
Inscrutability: Inscrutable AI systems can complicate risk measurement. Inscrutability
can be a result of the opaque nature of AI systems (limited explainability or interpretability), lack of transparency or documentation in AI system development or deployment, or
inherent uncertainties in AI systems.
Human baseline: Risk management of AI systems that are intended to augment or replace
human activity, for example decision making, requires some form of baseline metrics for
comparison. This is difficult to systematize since AI systems carry out different tasks – and
perform tasks differently – than humans.

Page 6

NIST AI 100-1

1.2.2

AI RMF 1.0

Risk Tolerance

While the AI RMF can be used to prioritize risk, it does not prescribe risk tolerance. Risk
tolerance refers to the organization’s or AI actor’s (see Appendix A) readiness to bear the
risk in order to achieve its objectives. Risk tolerance can be influenced by legal or regulatory requirements (Adapted from: ISO GUIDE 73). Risk tolerance and the level of risk that
is acceptable to organizations or society are highly contextual and application and use-case
specific. Risk tolerances can be influenced by policies and norms established by AI system owners, organizations, industries, communities, or policy makers. Risk tolerances are
likely to change over time as AI systems, policies, and norms evolve. Different organizations may have varied risk tolerances due to their particular organizational priorities and
resource considerations.
Emerging knowledge and methods to better inform harm/cost-benefit tradeoffs will continue to be developed and debated by businesses, governments, academia, and civil society.
To the extent that challenges for specifying AI risk tolerances remain unresolved, there may
be contexts where a risk management framework is not yet readily applicable for mitigating
negative AI risks.
The Framework is intended to be flexible and to augment existing risk practices
which should align with applicable laws, regulations, and norms. Organizations
should follow existing regulations and guidelines for risk criteria, tolerance, and
response established by organizational, domain, discipline, sector, or professional
requirements. Some sectors or industries may have established definitions of harm or
established documentation, reporting, and disclosure requirements. Within sectors,
risk management may depend on existing guidelines for specific applications and
use case settings. Where established guidelines do not exist, organizations should
define reasonable risk tolerance. Once tolerance is defined, this AI RMF can be used
to manage risks and to document risk management processes.
1.2.3

Risk Prioritization

Attempting to eliminate negative risk entirely can be counterproductive in practice because
not all incidents and failures can be eliminated. Unrealistic expectations about risk may
lead organizations to allocate resources in a manner that makes risk triage inefficient or
impractical or wastes scarce resources. A risk management culture can help organizations
recognize that not all AI risks are the same, and resources can be allocated purposefully.
Actionable risk management efforts lay out clear guidelines for assessing trustworthiness
of each AI system an organization develops or deploys. Policies and resources should be
prioritized based on the assessed risk level and potential impact of an AI system. The extent
to which an AI system may be customized or tailored to the specific context of use by the
AI deployer can be a contributing factor.

Page 7

[...]

NIST AI 100-1

AI RMF 1.0

Appendix D:
Attributes of the AI RMF
NIST described several key attributes of the AI RMF when work on the Framework first
began. These attributes have remained intact and were used to guide the AI RMF’s development. They are provided here as a reference.
The AI RMF strives to:
1. Be risk-based, resource-efficient, pro-innovation, and voluntary.
2. Be consensus-driven and developed and regularly updated through an open, transparent process. All stakeholders should have the opportunity to contribute to the AI
RMF’s development.
3. Use clear and plain language that is understandable by a broad audience, including
senior executives, government officials, non-governmental organization leadership,
and those who are not AI professionals – while still of sufficient technical depth to
be useful to practitioners. The AI RMF should allow for communication of AI risks
across an organization, between organizations, with customers, and to the public at
large.
4. Provide common language and understanding to manage AI risks. The AI RMF
should offer taxonomy, terminology, definitions, metrics, and characterizations for
AI risk.
5. Be easily usable and fit well with other aspects of risk management. Use of the
Framework should be intuitive and readily adaptable as part of an organization’s
broader risk management strategy and processes. It should be consistent or aligned
with other approaches to managing AI risks.
6. Be useful to a wide range of perspectives, sectors, and technology domains. The AI
RMF should be universally applicable to any AI technology and to context-specific
use cases.
7. Be outcome-focused and non-prescriptive. The Framework should provide a catalog
of outcomes and approaches rather than prescribe one-size-fits-all requirements.
8. Take advantage of and foster greater awareness of existing standards, guidelines, best
practices, methodologies, and tools for managing AI risks – as well as illustrate the
need for additional, improved resources.
9. Be law- and regulation-agnostic. The Framework should support organizations’
abilities to operate under applicable domestic and international legal or regulatory
regimes.
10. Be a living document. The AI RMF should be readily updated as technology, understanding, and approaches to AI trustworthiness and uses of AI change and as stakeholders learn from implementing AI risk management generally and this framework
in particular.

Page 42

This publication is available free of charge from:
https://doi.org/10.6028/NIST.AI.100-1

## Related

- [[Christin2020_Article_TheEthnographerAndTheAlgorithm.pdf]]
- [[type raw (2)]]
- [[Research and Papers MOC]]
- [[NIST AI RMF 1.0 — NIST AI 100-1 (2023)]]
