---
type: raw
source_kind: pdf_text
source_path: /mnt/d/LIBRARY/Review/Unreadable/2016 - Big Datas Disparate Impact.pdf - 2016 - Big Datas Disparate Impact.pdf.pdf - 2016 - Big Datas Disparate Impact.pdf - 2016 - Big Datas Disparate Impact.pdf.pdf.pdf
source_rel: Review/Unreadable/2016 - Big Datas Disparate Impact.pdf - 2016 - Big Datas Disparate Impact.pdf.pdf - 2016 - Big Datas Disparate Impact.pdf - 2016 - Big Datas Disparate Impact.pdf.pdf.pdf
pages_total: 62
text_first_pages: 12
text_last_pages: 2
pdfinfo:
  Author: "Maria Eugenia VIDAL-MANOU, BA"
  CreationDate: "Sun May 29 14:05:00 2016 EDT"
  Creator: "Microsoft® Word 2010"
  Custom Metadata: "no"
  Encrypted: "no"
  File size: "760212 bytes"
  Form: "none"
  JavaScript: "no"
  Metadata Stream: "no"
  ModDate: "Sun May 29 14:05:00 2016 EDT"
  Optimized: "no"
  PDF version: "1.5"
  Page rot: "0"
  Page size: "612 x 792 pts (letter)"
  Pages: "62"
  Producer: "Microsoft® Word 2010"
  Suspects: "no"
  Tagged: "yes"
  UserProperties: "no"
dr_sort_original_filename: "2016 - Big Datas Disparate Impact.pdf - 2016 - Big Datas Disparate Impact.pdf.pdf - 2016 - Big Datas Disparate Impact.pd__21659f44a787.md"
dr_sort_original_path: "raw sources/D_LIBRARY_ingest_2026-04-26/ocr_unreadable/converted_ocr/Review/Unreadable/2016 - Big Datas Disparate Impact.pdf - 2016 - Big Datas Disparate Impact.pdf.pdf - 2016 - Big Datas Disparate Impact.pd__21659f44a787.md"
dr_sort_filename_normalized: "2026-05-06"
---

# 2016 - Big Datas Disparate Impact.pdf - 2016 - Big Datas Disparate Impact.pdf.pdf - 2016 - Big Datas Disparate Impact.pdf - 2016 - Big Datas Disparate Impact.pdf.pdf.pdf

## Extracted Text

Big Data’s Disparate Impact
Solon Barocas* & Andrew D. Selbst**
Advocates of algorithmic techniques like data mining argue that
these techniques eliminate human biases from the decision-making
process. But an algorithm is only as good as the data it works with.
Data is frequently imperfect in ways that allow these algorithms to
inherit the prejudices of prior decision makers. In other cases, data
may simply reflect the widespread biases that persist in society at
large. In still others, data mining can discover surprisingly useful
regularities that are really just preexisting patterns of exclusion and
inequality. Unthinking reliance on data mining can deny historically
disadvantaged and vulnerable groups full participation in society.
Worse still, because the resulting discrimination is almost always an
unintentional emergent property of the algorithm’s use rather than a
conscious choice by its programmers, it can be unusually hard to
identify the source of the problem or to explain it to a court.
This Essay examines these concerns through the lens of
American antidiscrimination law—more particularly, through Title

DOI: http://dx.doi.org/10.15779/Z38BG31
California Law Review, Inc. (CLR) is a California nonprofit corporation. CLR and the
authors are solely responsible for the content of their publications.
* Postdoctoral Research Associate, Center for Information Technology Policy, Princeton
University; Ph.D. 2014, New York University, Department of Media, Culture, and Communication.
This research was supported in part by the Center for Information Technology Policy at Princeton
University.
** Scholar in Residence, Electronic Privacy Information Center; Visiting Researcher,
Georgetown University Law Center; Visiting Fellow, Yale Information Society Project; J.D. 2011,
University of Michigan Law School. The authors would like to thank Jane Bambauer, Alvaro Bedoya,
Marjory Blumenthal, Danielle Citron, James Grimmelmann, Moritz Hardt, Don Herzog, Janine Hiller,
Chris Hoofnagle, Joanna Huey, Patrick Ishizuka, Michael Kirkpatrick, Aaron Konopasky, Joshua
Kroll, Mark MacCarthy, Arvind Narayanan, Helen Norton, Paul Ohm, Scott Peppet, Joel Reidenberg,
David Robinson, Kathy Strandburg, David Vladeck, members of the Privacy Research Group at New
York University, and the participants of the 2014 Privacy Law Scholars Conference for their helpful
comments. Special thanks also to Helen Nissenbaum and the Information Law Institute at New York
University for giving us an interdisciplinary space to share ideas, allowing this paper to come about.
Copyright © 2016 by Solon Barocas and Andrew Selbst. This Essay is available for reuse under the
Creative
Commons
Attribution-ShareAlike
4.0
International
License,
http://creativecommons.org/licenses/by-sa/4.0/. The required attribution notice under the license must
include the article’s full citation information, e.g., “Solon Barocas & Andrew D. Selbst, Big Data's
Disparate Impact, 104 CALIF. L. REV. 671 (2016).”

671

672

CALIFORNIA LAW REVIEW

[Vol. 104:671

VII’s prohibition of discrimination in employment. In the absence of
a demonstrable intent to discriminate, the best doctrinal hope for
data mining’s victims would seem to lie in disparate impact doctrine.
Case law and the Equal Employment Opportunity Commission’s
Uniform Guidelines, though, hold that a practice can be justified as a
business necessity when its outcomes are predictive of future
employment outcomes, and data mining is specifically designed to
find such statistical correlations. Unless there is a reasonably
practical way to demonstrate that these discoveries are spurious,
Title VII would appear to bless its use, even though the correlations it
discovers will often reflect historic patterns of prejudice, others’
discrimination against members of protected groups, or flaws in the
underlying data.
Addressing the sources of this unintentional discrimination and
remedying the corresponding deficiencies in the law will be difficult
technically, difficult legally, and difficult politically. There are a
number of practical limits to what can be accomplished
computationally. For example, when discrimination occurs because
the data being mined is itself a result of past intentional
discrimination, there is frequently no obvious method to adjust
historical data to rid it of this taint. Corrective measures that alter
the results of the data mining after it is complete would tread on
legally and politically disputed terrain. These challenges for reform
throw into stark relief the tension between the two major theories
underlying
antidiscrimination
law:
anticlassification
and
antisubordination. Finding a solution to big data’s disparate impact
will require more than best efforts to stamp out prejudice and bias; it
will require a wholesale reexamination of the meanings of
“discrimination” and “fairness.”
Introduction .................................................................................................... 673
I. How Data Mining Discriminates ................................................................. 677
A. Defining the “Target Variable” and “Class Labels” .................... 677
B. Training Data ............................................................................... 680
1. Labeling Examples ................................................................ 681
2. Data Collection ...................................................................... 684
C. Feature Selection ......................................................................... 688
D. Proxies ......................................................................................... 691
E. Masking ....................................................................................... 692
II. Title VII Liability for Discriminatory Data Mining ................................... 694
A. Disparate Treatment ..................................................................... 694
B. Disparate Impact .......................................................................... 701
C. Masking and Problems of Proof .................................................. 712
III. The Difficulty for Reforms ....................................................................... 714
A. Internal Difficulties ...................................................................... 715

2016]

BIG DATA’S DISPARATE IMPACT

673

1. Defining the Target Variable ................................................. 715
2. Training Data ......................................................................... 716
a. Labeling Examples.......................................................... 716
b. Data Collection ............................................................... 717
3. Feature Selection ................................................................... 719
4. Proxies ................................................................................... 720
B. External Difficulties ..................................................................... 723
Conclusion ...................................................................................................... 729

INTRODUCTION
“Big Data” is the buzzword of the decade.1 Advertisers want data to reach
profitable consumers,2 medical professionals to find side effects of prescription
drugs,3 supply-chain operators to optimize their delivery routes,4 police to
determine where to focus resources,5 and social scientists to study human
interactions.6 Though useful, however, data is not a panacea. Where data is
used predictively to assist decision making, it can affect the fortunes of whole
classes of people in consistently unfavorable ways. Sorting and selecting for
the best or most profitable candidates means generating a model with winners
and losers. If data miners are not careful, the process can result in
disproportionately adverse outcomes concentrated within historically
disadvantaged groups in ways that look a lot like discrimination.
Although we live in the post–civil rights era, discrimination persists in
American society and is stubbornly pervasive in employment, housing, credit,
and consumer markets.7 While discrimination certainly endures in part due to
decision makers’ prejudices, a great deal of modern-day inequality can be
attributed to what sociologists call “institutional” discrimination.8 Unconscious,
implicit biases and inertia within society’s institutions, rather than intentional

1. Contra Sanjeev Sardana, Big Data: It’s Not a Buzzword, It’s a Movement, FORBES (Nov.
20, 2013), http://www.forbes.com/sites/sanjeevsardana/2013/11/20/bigdata [https://perma.cc/9Y37ZFT5].
2. Tanzina Vega, New Ways Marketers Are Manipulating Data to Influence You, N.Y.
TIMES: BITS (June 19, 2013, 9:49 PM), http://bits.blogs.nytimes.com/2013/06/19/new-waysmarketers-are-manipulating-data-to-influence-you [https://perma.cc/238F-9T8X].
3. Nell Greenfieldboyce, Big Data Peeps at Your Medical Records to Find Drug Problems,
NPR (July 21, 2014, 5:15 AM), http://www.npr.org/blogs/health/2014/07/21/332290342/big-datapeeps-at-your-medical-records-to-find-drug-problems [https://perma.cc/GMT4-ECBD].
4. Business
by
Numbers,
ECONOMIST
(Sept.
13,
2007),
http://www.economist.com/node/9795140 [https://perma.cc/7YC2-DMYA].
5. Nadya Labi, Misfortune Teller, ATLANTIC (Jan.–Feb. 2012), http://www.theatlantic.com/
magazine/archive/2012/01/misfortune-teller/308846 [https://perma.cc/7L72-J5L9].
6. David Lazer et al., Computational Social Science, 323 SCI. 721, 722 (2009).
7. Devah Pager & Hana Shepherd, The Sociology of Discrimination: Racial Discrimination
in Employment, Housing, Credit, and Consumer Markets, 34 ANN. REV. SOC. 181, 182 (2008).
8. Id.

674

CALIFORNIA LAW REVIEW

[Vol. 104:671

choices, account for a large part of the disparate effects observed.9 Approached
without care, data mining can reproduce existing patterns of discrimination,
inherit the prejudice of prior decision makers, or simply reflect the widespread
biases that persist in society. It can even have the perverse result of
exacerbating existing inequalities by suggesting that historically disadvantaged
groups actually deserve less favorable treatment.
Algorithms10 could exhibit these tendencies even if they have not been
manually programmed to do so, whether on purpose or by accident.
Discrimination may be an artifact of the data mining process itself, rather than
a result of programmers assigning certain factors inappropriate weight. Such a
possibility has gone unrecognized by most scholars and policy makers, who
tend to fear concealed, nefarious intentions or the overlooked effects of human
bias or error in hand coding algorithms.11 Because the discrimination at issue is
unintentional, even honest attempts to certify the absence of prejudice on the
part of those involved in the data mining process may wrongly confer the
imprimatur of impartiality on the resulting decisions. Furthermore, because the
mechanism through which data mining may disadvantage protected classes is
less obvious in cases of unintentional discrimination, the injustice may be
harder to identify and address.
In May 2014, the White House released a report titled Big Data: Seizing
Opportunities, Preserving Values (Podesta Report), which hinted at the
discriminatory potential of big data.12 The report finds “that big data analytics
have the potential to eclipse longstanding civil rights protections in how
personal information is used in housing, credit, employment, health, education,
and the marketplace.”13 It suggests that there may be unintended discriminatory

9. See Andrew Grant-Thomas & john a. powell, Toward a Structural Racism Framework, 15
POVERTY & RACE 3, 4 (“‘Institutional racism’ was the designation given in the late 1960s to the
recognition that, at very least, racism need not be individualist, essentialist or intentional.”).
10. An “algorithm” is a formally specified sequence of logical operations that provides stepby-step instructions for computers to act on data and thus automate decisions. SOLON BAROCAS ET
AL., DATA & CIVIL RIGHTS: TECHNOLOGY PRIMER (2014), http://www.datacivilrights.org/pubs/20141030/Technology.pdf [https://perma.cc/X3YX-XHNA]. Algorithms play a role in both automating the
discovery of useful patterns in datasets and automating decision making that relies on these
discoveries. This Essay uses the term to refer to the latter.
11. See, e.g., Kate Crawford & Jason Schultz, Big Data and Due Process: Toward a
Framework to Redress Predictive Privacy Harms, 55 B.C. L. REV. 93, 101 (2014) (“[H]ousing
providers could design an algorithm to predict the [race, gender, or religion] of potential buyers or
renters and advertise the properties only to those who [meet certain] profiles.”); Danielle Keats Citron
& Frank Pasquale, The Scored Society: Due Process for Automated Predictions, 89 WASH. L. REV. 1,
4 (2014) (“Because human beings program predictive algorithms, their biases and values are
embedded into the software’s instructions. . . .”); Danielle Keats Citron, Technological Due Process,
85 WASH. U. L. REV. 1249, 1254 (2008) (“Programmers routinely change the substance of rules when
translating them from human language into computer code.”).
12. EXEC. OFFICE OF THE PRESIDENT, BIG DATA: SEIZING OPPORTUNITIES, PRESERVING
VALUES (May 2014), http://www.whitehouse.gov/sites/default/files/docs/big_data_privacy_report
_5.1.14_final_print.pdf [https://perma.cc/ZXB4-SDL9].
13. Id. (introductory letter).

2016]

BIG DATA’S DISPARATE IMPACT

675

effects from data mining but does not detail how they might come about.14
Because the origin of the discriminatory effects remains unexplored, the
report’s approach does not address the full scope of the problem.
The Podesta Report, as one might expect from the executive branch, seeks
to address these effects primarily by finding new ways to enforce existing law.
Regarding discrimination, the report primarily recommends that enforcement
agencies, such as the Department of Justice, Federal Trade Commission,
Consumer Financial Protection Bureau, and Equal Employment Opportunity
Commission (EEOC), increase their technical expertise and “develop a plan for
investigating and resolving violations of law in such cases.”15
As this Essay demonstrates, however, existing law largely fails to address
the discrimination that can result from data mining. The argument is grounded
in Title VII because, of all American antidiscrimination jurisprudence, Title
VII has a particularly well-developed set of case law and scholarship. Further,
there exists a rapidly emerging field of “work-force science,”16 for which Title
VII will be the primary vehicle for regulation. Under Title VII, it turns out that
some, if not most, instances of discriminatory data mining will not generate
liability. While the Essay does not show this to be true outside of Title VII
itself, the problem is likely not particular to Title VII. Rather, it is a feature of
our current approach to antidiscrimination jurisprudence, with its focus on
procedural fairness. The analysis will likely apply to other traditional areas of
discrimination, such as housing or disability discrimination. Similar tendencies
to disadvantage the disadvantaged will likely arise in areas that regulate
legitimate economic discrimination, such as credit and insurance.
This Essay proceeds in three Parts. Part I introduces the computer science
literature and proceeds through the various steps of solving a problem with data
mining: defining the target variable, labeling and collecting the training data,
using feature selection, and making decisions on the basis of the resulting
model. Each of these steps creates possibilities for a final result that has a
disproportionately adverse impact on protected classes, whether by specifying
the problem to be solved in ways that affect classes differently, failing to
recognize or address statistical biases, reproducing past prejudice, or
considering an insufficiently rich set of factors. Even in situations where data
miners are extremely careful, they can still effect discriminatory results with
models that, quite unintentionally, pick out proxy variables for protected
classes. Finally, Part I notes that data mining poses the additional problem of

14. Id. at 64 (“This combination of circumstances and technology raises difficult questions
about how to ensure that discriminatory effects resulting from automated decision processes, whether
intended or not, can be detected, measured, and redressed.”).
15. Id. at 65.
16. Steve Lohr, Big Data, Trying to Build Better Workers, N.Y. TIMES (Apr. 20, 2013),
http://www.nytimes.com/2013/04/21/technology/big-data-trying-to-build-better-workers.html
[https://perma.cc/CEL2-P9XB].

676

CALIFORNIA LAW REVIEW

[Vol. 104:671

giving data miners the ability to disguise intentional discrimination as
accidental.
In Part II, the Essay reviews Title VII jurisprudence as it applies to data
mining. Part II discusses both disparate treatment and disparate impact,
examining which of the various data mining mechanisms identified in Part I
will trigger liability under either Title VII theory. At first blush, either theory is
viable. Disparate treatment is viable because data mining systems treat
everyone differently; that is their purpose. Disparate impact is also viable
because data mining can have various discriminatory effects, even without
intent. But as Part II demonstrates, data mining combines some well-known
problems in discrimination doctrines with new challenges particular to data
mining systems, such that liability for discriminatory data mining will be hard
to find. Part II concludes with a discussion of the new problems of proof that
arise for intentional discrimination in this context.
Finally, Part III addresses the difficulties reformers would face in
addressing the deficiencies found in Part II. These difficulties take two forms:
complications internal to the logic of data mining and political and
constitutional difficulties external to the problem. Internally, the different steps
in a data mining problem require constant subjective and fact-bound
judgments, which do not lend themselves to general legislative resolution.
Worse, many of these are normative judgments in disguise, about which there
is not likely to be consensus. Externally, data mining will force society to
explicitly rebalance the two justifications for antidiscrimination law—rooting
out intentional discrimination and equalizing the status of historically
disadvantaged communities. This is because methods of proof and corrective
measures will often require an explicit commitment to substantive remediation
rather than merely procedural remedies. In certain cases, data mining will make
it simply impossible to rectify discriminatory results without engaging with the
question of what level of substantive inequality is proper or acceptable in a
given context. Given current political realities and trends in constitutional
doctrines, legislation enacting a remedy that results from these discussions
faces an uphill battle. To be sure, data mining also has the potential to help
reduce discrimination by forcing decisions onto a more reliable empirical
foundation and by formalizing decision-making processes, thus limiting the
opportunity for individual bias to affect important assessments.17 In many
situations, the introduction of data mining will be a boon to civil rights, even
where it fails to root out discrimination altogether, and such efforts should be
encouraged. Yet, understanding when and why discrimination persists in cases
of data-driven decision making reveals important and sometimes troubling
limits to the promise of big data, for which there are no ready solutions.

17. Tal Z. Zarsky, Automated Prediction: Perception, Law, and Policy, COMM. ACM,
Sept. 2012, at 33–35.

2016]

BIG DATA’S DISPARATE IMPACT

677

I.
HOW DATA MINING DISCRIMINATES
Although commentators have ascribed myriad forms of discrimination to
data mining,18 there remains significant confusion over the precise mechanisms
that render data mining discriminatory. This Part develops a taxonomy that
isolates and explicates the specific technical issues that can give rise to models
whose use in decision making may have a disproportionately adverse impact on
protected classes. By definition, data mining is always a form of statistical (and
therefore seemingly rational) discrimination. Indeed, the very point of data
mining is to provide a rational basis upon which to distinguish between
individuals and to reliably confer to the individual the qualities possessed by
those who seem statistically similar. Nevertheless, data mining holds the
potential to unduly discount members of legally protected classes and to place
them at systematic relative disadvantage. Unlike more subjective forms of
decision making, data mining’s ill effects are often not traceable to human bias,
conscious or unconscious. This Part describes five mechanisms by which these
disproportionately adverse outcomes might occur, walking through a sequence
of key steps in the overall data mining process.
A. Defining the “Target Variable” and “Class Labels”
In contrast to those traditional forms of data analysis that simply return
records or summary statistics in response to a specific query, data mining
attempts to locate statistical relationships in a dataset.19 In particular, it
automates the process of discovering useful patterns, revealing regularities
upon which subsequent decision making can rely. The accumulated set of
discovered relationships is commonly called a “model,” and these models can
be employed to automate the process of classifying entities or activities of
interest, estimating the value of unobserved variables, or predicting future
outcomes.20 Familiar examples of such applications include spam or fraud
detection, credit scoring, and insurance pricing. These examples all involve
attempts to determine the status or likely outcome of cases under consideration
based solely on access to correlated data.21 Data mining helps identify cases of

18. Solon Barocas, Data Mining and the Discourse on Discrimination, PROC. DATA ETHICS
WORKSHOP (2014), https://dataethics.github.io/proceedings/DataMiningandtheDiscourseOn
Discrimination.pdf [https://perma.cc/D3LT-GS2X].
19. See generally Usama Fayyad, The Digital Physics of Data Mining, 44 COMM. ACM, Mar.
2001, at 62.
20. More formally, classification deals with discrete outcomes, estimation deals with
continuous variables, and prediction deals with both discrete outcomes and continuous variables, but
specifically for states or values in the future. MICHAEL J. A. BERRY & GORDON S. LINOFF, DATA
MINING TECHNIQUES: FOR MARKETING, SALES, AND CUSTOMER RELATIONSHIP MANAGEMENT 8–
11 (2004).
21. Pedro Domingos, A Few Useful Things to Know About Machine Learning, COMM. ACM,
Oct. 2012, at 78–80.

678

CALIFORNIA LAW REVIEW

[Vol. 104:671

spam and fraud and anticipate default and poor health by treating these states
and outcomes as a function of some other set of observed characteristics.22 In
particular, by exposing so-called “machine learning” algorithms to examples of
the cases of interest (previously identified instances of fraud, spam, default, and
poor health), the algorithm “learns” which related attributes or activities can
serve as potential proxies for those qualities or outcomes of interest.23
Two concepts from the machine learning and data mining literature are
important here: “target variables” and “class labels.” The outcomes of interest
discussed above are known as target variables.24 While the target variable
defines what data miners are looking for, “class labels” divide all possible
values of the target variable into mutually exclusive categories.
The proper specification of the target variable is frequently not obvious,
and the data miner’s task is to define it. To start, data miners must translate
some amorphous problem into a question that can be expressed in more formal
terms that computers can parse. In particular, data miners must determine how
to solve the problem at hand by translating it into a question about the value of
some target variable. The open-endedness that characterizes this part of the
process is often described as the “art” of data mining. This initial step requires
a data miner to “understand[] the project objectives and requirements from a
business perspective [and] then convert[] this knowledge into a data mining
problem definition.”25 Through this necessarily subjective process of
translation, data miners may unintentionally parse the problem in such a way
that happens to systematically disadvantage protected classes.
Problem specification is not a wholly arbitrary process, however. Data
mining can only address problems that lend themselves to formalization as
questions about the state or value of the target variable. Data mining works
exceedingly well for dealing with fraud and spam because these cases rely on
extant, binary categories. A given instance either is or is not fraud or spam, and
the definitions of fraud or spam are, for the most part, uncontroversial.26 A
computer can then flag or refuse transactions or redirect emails according to

22.
23.
24.

Id.
Id.
COMM. ON THE ANALYSIS OF MASSIVE DATA ET AL., FRONTIERS IN MASSIVE DATA
ANALYSIS 101 (2013), http://www.nap.edu/catalog.php?record_id=18374 [https://perma.cc/5DNQUFE4]. The machine learning community refers to classification, estimation, and prediction—the
techniques that we discuss in this Essay—as “supervised” learning because analysts must actively
specify a target variable of interest. Id. at 104. Other techniques known as “unsupervised” learning do
not require any such target variables and instead search for general structures in the dataset, rather than
patterns specifically related to some state or outcome. Id. at 102. Clustering is the most common
example of “unsupervised” learning, in that clustering algorithms simply reveal apparent hot spots
when plotting the data in some fashion. Id. We limit the discussion to supervised learning because we
are primarily concerned with the sorting, ranking, and predictions enabled by data mining.
25. PETE CHAPMAN ET AL., CRISP-DM 1.0: STEP-BY-STEP DATA MINING GUIDE 10 (2000).
26. See David J. Hand, Classifier Technology and the Illusion of Progress, 21 STAT. SCI. 1, 10
(2006).

2016]

BIG DATA’S DISPARATE IMPACT

679

well-understood distinctions.27 In these cases, data miners can simply rely on
these simple, preexisting categories to define the class labels.
Sometimes, though, defining the target variable involves the creation of
new classes. Consider credit scoring, for instance. Although now taken for
granted, the predicted likelihood of missing a certain number of loan
repayments is not a self-evident answer to the question of how to successfully
extend credit to consumers.28 Unlike fraud or spam, “creditworthiness” is an
artifact of the problem definition itself. There is no way to directly measure
creditworthiness because the very notion of creditworthiness is a function of
the particular way the credit industry has constructed the credit issuing and
repayment system. That is, an individual’s ability to repay some minimum
amount of an outstanding debt on a monthly basis is taken to be a nonarbitrary
standard by which to determine in advance and all-at-once whether he is
worthy of credit.29
Data mining has many uses beyond spam detection, fraud detection, credit
scoring, and insurance pricing. As discussed in the introduction, this Essay will
focus on the use of data mining in employment decisions. Extending this
discussion to employment, then, where employers turn to data mining to
develop ways of improving and automating their search for good employees,
they face a number of crucial choices.
Like creditworthiness, the definition of a good employee is not a given.
“Good” must be defined in ways that correspond to measurable outcomes:
relatively higher sales, shorter production time, or longer tenure, for example.
When employers mine data for good employees, they are, in fact, looking for
employees whose observable characteristics suggest that they would meet or
exceed some monthly sales threshold, perform some task in less than a certain
amount of time, or remain in their positions for more than a set number of
weeks or months. Rather than drawing categorical distinctions along these
lines, data mining could also estimate or predict the specific numerical value of
sales, production time, or tenure period, enabling employers to rank rather than
simply sort employees.
These may seem like eminently reasonable things for employers to want
to predict, but they are, by necessity, only part of an array of possible
definitions of “good.” An employer may instead attempt to define the target
variable in a more holistic way—by, for example, relying on the grades that
prior employees have received in annual reviews, which are supposed to reflect

27. Though described as a matter of detection, this is really a classification task, where any
given transaction or email can belong to one of two possible classes, respectively: fraud or not fraud,
or spam or not spam.
28. See generally Martha Ann Poon, What Lenders See—A History of the Fair Isaac
Scorecard, (2013) (unpublished Ph.D. dissertation, University of California, San Diego),
http://search.proquest.com/docview/1520318884 [https://perma.cc/YD3S-B9N7].
29. Hand, supra note 26, at 10.

680

CALIFORNIA LAW REVIEW

[Vol. 104:671

an overall assessment of performance. These target variable definitions simply
inherit the formalizations involved in preexisting assessment mechanisms,
which in the case of human-graded performance reviews, may be far less
consistent.30
Thus, the definition of the target variable and its associated class labels
will determine what data mining happens to find. While critics of data mining
have tended to focus on inaccurate classifications (false positives and false
negatives),31 as much—if not more—danger resides in the definition of the
class label itself and the subsequent labeling of examples from which rules are
inferred.32 While different choices for the target variable and class labels can
seem more or less reasonable, valid concerns with discrimination enter at this
stage because the different choices may have a greater or lesser adverse impact
on protected classes. For example, as later Parts will explain in detail, hiring
decisions made on the basis of predicted tenure are much more likely to have a
disparate impact on certain protected classes than hiring decisions that turn on
some estimate of worker productivity. If the turnover rate happens to be
systematically higher among members of certain protected classes, hiring
decisions based on predicted length of employment will result in fewer job
opportunities for members of these groups, even if they would have performed
as well as or better than the other applicants the company chooses to hire.
B. Training Data
As described above, data mining learns by example. Accordingly, what a
model learns depends on the examples to which it has been exposed. The data
that function as examples are known as “training data”—quite literally, the data
that train the model to behave in a certain way. The character of the training
data can have meaningful consequences for the lessons that data mining
happens to learn. As computer science scholars explain, biased training data
leads to discriminatory models.33 This can mean two rather different things,
30. Joseph M. Stauffer & M. Ronald Buckley, The Existence and Nature of Racial Bias in
Supervisory Ratings, 90 J. APPLIED PSYCHOL. 586, 588–89 (2005) (showing evidence of racial bias in
performance evaluations). Nevertheless, devising new target variables can have the salutary effect of
forcing decision makers to think much more concretely about the outcomes that justifiably determine
whether someone is a “good” employee. The explicit enumeration demanded of data mining thus also
presents an opportunity to make decision making more consistent, more accountable, and fairer
overall. This, however, requires conscious effort and careful thinking, and is not a natural consequence
of adopting data mining.
31. Bruce Schneier, Data Mining for Terrorists, SCHNEIER ON SECURITY (Mar. 9, 2006),
https://www.schneier.com/blog/archives/2006/03/data_mining_for.html
[https://perma.cc/ZW44N2KR]; Oscar H. Gandy Jr., Engaging Rational Discrimination: Exploring Reasons for Placing
Regulatory Constraints on Decision Support Systems, 12 ETHICS & INFO. TECH. 29, 39–40 (2010);
Mireille Hildebrandt & Bert-Jaap Koops, The Challenges of Ambient Law and Legal Protection in the
Profiling Era, 73 MOD. L. REV. 428, 433–35 (2010).
32. See infra Part I.B.
33. Bart Custers, Data Dilemmas in the Information Society: Introduction and Overview, in
DISCRIMINATION AND PRIVACY IN THE INFORMATION SOCIETY 3, 20 (Bart Custers et al. eds., 2013).

2016]

BIG DATA’S DISPARATE IMPACT

681

though: (1) if data mining treats cases in which prejudice has played some role
as valid examples to learn from, that rule may simply reproduce the prejudice
involved in these earlier cases; or (2) if data mining draws inferences from a
biased sample of the population, any decision that rests on these inferences
may systematically disadvantage those who are under- or overrepresented in
the dataset. Both can affect the training data in ways that lead to discrimination,
but the mechanisms—improper labeling of examples and biased data
collections—are sufficiently distinct that they warrant separate treatment.
1. Labeling Examples
Labeling examples is the process by which the training data is manually
assigned class labels. In cases of fraud or spam, the data miners draw from
examples that come prelabeled: when individual customers report fraudulent
charges or mark a message as spam, they are actually labeling transactions and
email for the providers of credit and webmail. Likewise, an employer using
grades previously given at performance reviews is also using prelabeled
examples.
In certain cases, however, there may not be any labeled data and data
miners may have to figure out a way to label examples themselves. This can be
a laborious process, and it is frequently fraught with peril.34 Often the best
labels for different classifications will be open to debate. On which side of the
creditworthy line does someone who has missed four credit card payments fall,
for example?35 The answer is not obvious. Even where the class labels are
uncontested or uncontroversial, they may present a problem because analysts
will often face difficult choices in deciding which of the available labels best
applies to a particular example. Certain cases may present some, but not all,
criteria for inclusion in a particular class.36 The situation might also work in
reverse, where the class labels are insufficiently precise to capture meaningful
differences between cases. Such imperfect matches will demand that data
miners exercise judgment.
The unavoidably subjective labeling of examples will skew the resulting
findings such that any decisions taken on the basis of those findings will
characterize all future cases along the same lines. This is true even if such

34. Hand, supra note 26, at 10–11.
35. Id. at 10 (“The classical supervised classification paradigm also takes as fundamental the
fact that the classes are well defined. That is, that there is some fixed clear external criterion, which is
used to produce the class labels. In many situations, however, this is not the case. In particular, when
the classes are defined by thresholding a continuous variable, there is always the possibility that the
defining threshold might be changed. Once again, this situation arises in consumer credit, where it is
common to define a customer as ‘defaulting’ if they fall three months in arrears with repayments. This
definition, however, is not a qualitative one (contrast has a tumor/does not have a tumor) but is very
much a quantitative one. It is entirely reasonable that alternative definitions (e.g., four months in
arrears) might be more useful if economic conditions were to change.”).
36. Id. at 11.

682

CALIFORNIA LAW REVIEW

[Vol. 104:671

characterizations would seem plainly erroneous to analysts who looked more
closely at the individual cases. For all their potential problems, though, the
labels applied to the training data must serve as ground truth.37 Thus, decisions
based on discoveries that rest on haphazardly labeled data or data labeled in a
systematically, though unintentionally, biased manner will seem valid
according to the customary validation methods employed by data miners. So
long as prior decisions affected by some form of prejudice serve as examples of
correctly rendered determinations, data mining will necessarily infer rules that
exhibit the same prejudice.
Consider a real-world example from a different context as to how biased
data labeling can skew results. St. George’s Hospital, in the United Kingdom,
developed a computer program to help sort medical school applicants based on
its previous admissions decisions.38 Those admissions decisions, it turns out,
had systematically disfavored racial minorities and women with credentials
otherwise equal to other applicants’.39 In drawing rules from biased prior
decisions, St. George’s Hospital unknowingly devised an automated process
that possessed these very same prejudices. As editors at the British Medical
Journal noted at the time, “[T]he program was not introducing new bias but
merely reflecting that already in the system.”40 Were an employer to undertake
a similar plan to automate its hiring decisions by inferring a rule from past
decisions swayed by prejudice, the employer would likewise arrive at a
decision procedure that simply reproduces the prejudice of prior decision
makers. Indeed, automating the process in this way would turn the conscious
prejudice or implicit bias of individuals involved in previous decision making
into a formalized rule that would systematically alter the prospects of all future
applicants. For example, the computer may learn to discriminate against certain
female or black applicants if trained on prior hiring decisions in which an
employer has consistently rejected jobseekers with degrees from women’s or
historically black colleges.
Not only can data mining inherit prior prejudice through the mislabeling
of examples, it can also reflect current prejudice through the ongoing behavior
of users taken as inputs to data mining. This is what Professor Latanya
Sweeney discovered in a study that found that Google queries for blacksounding names were more likely to return contextual (i.e., key-word triggered)

37. Id. at 12. Even when evaluating a model, the kinds of subtle mischaracterizations that
happen during training will be impossible to detect because most “evaluation data” is just a small
subset of the training data that has been withheld during the learning process. Any problems with the
training data will be present in the evaluation data.
38. Stella Lowry & Gordon Macpherson, A Blot on the Profession, 296 BRIT. MED. J. 657,
657 (1988).
39. Id. at 657.
40. Id.

[...]

2016]

BIG DATA’S DISPARATE IMPACT

731

thinking about the solution is a duty of care, a theory of negligent
discrimination.290
But if Title VII alone cannot solve these problems, where should society
look for answers? Well, the first answer is to question the status quo. Data
mining takes the existing state of the world as a given and ranks candidates
according to their predicted attributes in that world. Data mining, by its very
nature, treats the target variable as the only item that employers are in a
position to alter; everything else that happens to correlate with different values
for the target variable is assumed stable. But there are many reasons to question
these background conditions. Sorting and selecting individuals according to
their apparent qualities hides the fact that the predicted effect of possessing
these qualities with respect to a specific outcome is also a function of the
conditions under which these decisions are made. Recall the tenure example
from Part III.B. In approaching appropriate hiring practices as a matter of
selecting the “right” candidates at the outset, an employer will fail to recognize
potential changes that he could make to workplace conditions. A more familyfriendly workplace, greater on-the-job training, or a workplace culture more
welcoming to historically underrepresented groups could affect the course of
employees’ tenure and their long-term success in ways that undermine the
seemingly prophetic nature of data mining’s predictions.
These are all traditional goals for reducing discrimination within the
workplace, and they continue to matter even in the face of the eventual
widespread adoption of data mining. But data can play a role here, too. For
example, comparing the performance of equally qualified candidates across
different workplaces can help isolate the formal policies and institutional
dynamics that are more or less likely to help workers flourish. Research of this
sort could also reveal areas for potential reform.291
Education is also important. Employers may take some steps to rectify the
problem on their own if they better understand the cause of the disparity. Right
now, many of the problems described in Part I are relatively unknown. But the
more employers and data miners understand these pitfalls, the more they can
strive to create better models on their own. Many employers switch to datadriven practices for the express purpose of eradicating bias;292 if employers
discover that they are introducing new forms of bias, they can correct course.
Even employers seeking only to increase efficiency or profit may find that
their incentives align with the goals of nondiscrimination. Faulty data and data

290. See generally David Benjamin Oppenheimer, Negligent Discrimination, 141 U. PA. L.
REV. 899 (1993).
291. Solon Barocas, Putting Data to Work, DATA AND DISCRIMINATION: COLLECTED ESSAYS
58, 60 (Seeta Peña Gangadharan, Virginia Eubanks & Solon Barocas eds., 2014).
292. Claire Cain Miller, Can an Algorithm Hire Better than a Human?, N.Y. TIMES (June 25,
2015), http://www.nytimes.com/2015/06/26/upshot/can-an-algorithm-hire-better-than-a-human.html
[https://perma.cc/UR37-83D4].

732

CALIFORNIA LAW REVIEW

[Vol. 104:671

mining will lead employers to overlook or otherwise discount people who are
actually “good” employees. Where the cost of addressing these problems is at
least compensated for by a business benefit of equal or greater value,
employers may have natural incentives to do so.
Finally, employers could also make more effective use of the tools that
computer scientists have begun to develop.293 Advances in these areas will
depend, crucially, on greater and more effective collaboration between
employers, computer scientists, lawyers, advocates, regulators, and policy
makers.294
This Essay is a call for caution in the use of data mining, not its
abandonment. While far from a panacea, data mining can and should be part of
a panoply of strategies for combatting discrimination in the workplace and for
promoting fair treatment and equality. Ideally, institutions can find ways to use
data mining to generate new knowledge and improve decision making that
serves the interests of both decision makers and protected classes. But where
data mining is adopted and applied without care, it poses serious risks of
reproducing many of the same troubling dynamics that have allowed
discrimination to persist in society, even in the absence of conscious prejudice.

293.
294.
2017).

See list supra note 217.
Joshua A. Kroll, et al., Accountable Algorithms, 165 U. PA. L. REV. __ (forthcoming

## Related

- [[2004 - Privacy as Contextual Integrity]]
- [[Christin2020_Article_TheEthnographerAndTheAlgorithm.pdf]]
- [[2018 - Tech Tools Profile, Police, and Pun]]
- [[Research and Papers MOC]]
- [[Big Data’s Disparate Impact — Barocas & Selbst 2016 (Title VII, data mining)]]
