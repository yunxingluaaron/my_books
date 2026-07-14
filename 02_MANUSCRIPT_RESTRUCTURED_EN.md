# From Outcome Archives to Decision Traces: Multimodal Evidence Engineering, Target Auditing, and Failure-Gated Regulatory AI

## A Retrospective Methods Study of Pennsylvania Well-Plugging Records

## Abstract

### Background

As foundation models, multimodal systems, and AI agents enter operational workflows, data must support not only model training but also runtime state, organizational memory, and accountable action. Many institutions possess abundant outcomes while lacking replayable **decision traces**: who knew what at the index time, which policy version applied, what alternatives were attempted, what evidence was accepted, and why an exception or disposition followed. Regulated case decisions are often path-dependent endpoints of submissions, field observations, revision, and professional judgment, whereas structured systems commonly privilege current or final state. Raw archives may retain fragments, but they seldom connect decision-time state, evidence, reasons, authority, and later outcome as one auditable unit.

### Objective

Using Pennsylvania well-plugging attainable-bottom review as a retrospective case study, we tested whether outcome-oriented archives could support partial decision-trace reconstruction, which missing trace elements made effort adequacy unidentifiable, and how a regulatory agent should be redesigned to produce prospective traces rather than infer unrecorded reasons.

### Methods

We defined an ideal trace as case, index time, actor, observed state, request/action, attempted alternatives, source evidence, rule/version, decision/reason, uncertainty/override, and separately linked later outcome. We then audited multimodal PDF extraction, file-page-quotation-visual provenance, requested/approved/final-state tracks, deterministic guards, quarantine, county-grouped cross-validation, leakage/censoring audits, version-controlled protocol freezing, internally blinded AI-agent reading with investigator adjudication, and consequence-specified failure gates. Processing covered 635 PDF-backed folders and approximately 1,700 PDFs. The frozen shortfall cohort contained 631 cases across 29 counties; DN/Model-A analyses used 424 cases and Model-B teacher-available analysis 423.

### Results

The pipeline produced 633 unique case rows, 10,856 depth rows, and 436 quarantine records, but only partial traces. Three predefined fields achieved precision and recall of 1.0 on a targeted 40-case regression set, not a corpus-wide sample. A nongeographic profile mixing request evidence with TD, age, casing, water, and coal covariates achieved county-grouped AUC 0.740 (SD 0.009); a county/formation geography-only profile achieved 0.625 (SD 0.006). This was not a causal decomposition of effort and geographic difficulty. An earlier within-case AUC of 0.916 was circular because a zero-parameter deepest-event rule recovered 79/103 labels. An 89-case censoring audit changed shortfall-risk AUC from 0.757 to 0.742 after exclusion and 0.689 after negative relabeling, precluding an effort-adequacy interpretation.

Within 424 cases, 423 had at least one dated event, but explicit attempted-and-failed evidence appeared in 6.1%, obstruction depth in 14.6%, and maximum reached depth in 18.9%; 93.15% of events had no tool token. Comparable difficulty concepts were recorded approximately 3–74 times more often in request narratives than in separately aggregated work records. These are documentation patterns, not proof of absent effort. Internal adjudication yielded 112 DN-positive cases. Model A, a 17-field DN-prescreen HGB classifier, achieved internally grouped AUC 0.8366 (fold SD 0.1097) and was restricted to queue ordering. Model B, a 17-field HGB regressor trained to approximate a locked historical shortfall teacher, achieved five-fold county-grouped Spearman 0.418 (fold SD 0.047), with 35.5% exact-bin and 72.3% within-one-bin agreement; it selected an empirical reference stratum and thereby influenced the preliminary route indirectly through a subsequent tail flag. Neither model had approval authority. A nominal refused-versus-approved-status DN association failed two frozen sensitivities; checklist augmentation failed its 0.764 performance gate; and retrospective routing sent five of seven depth-related refusals to a fast lane.

### Conclusions

These findings support a shift from outcome prediction to decision-trace infrastructure. Under 25 Pa. Code §78.1, attainable bottom requires Department approval and is defined relative to **reasonable effort**, not maximum or greatest effort [3]. The archive supported two descriptive channels—documented effort/action evidence and difficulty context—but neither automatically measured adequacy. Model A only allocated attention to documented difficulty; Model B only selected a coarse historical reference stratum; rules exposed explicit gaps; and a qualified reviewer retained normative authority. The proposed architecture would capture requests, revisions, accepted fields, rule versions, reasons, overrides, and later outcomes prospectively. Independent experts, external holdouts, and prospective human-system experiments remain necessary.

**Keywords:** regulatory AI; decision traces; decision provenance; multimodal document intelligence; organizational memory; selective labels; temporal leakage; target validity; human oversight; well plugging

---

## 1. Introduction

Modern AI raises a data problem that is not reducible to sample size: whether the record preserves the world as it was known when an action was justified. Foundation-model development emphasizes pretraining and post-training corpora; operational agents additionally require state, memory, precedent, and accountability. A transaction table may preserve a 20% discount while omitting the policy version, approver, exception rationale, alternatives, and discussions that produced it. Human teams can sometimes reconstruct such context from organizational memory and scattered communications. An agent given only the final value cannot reliably distinguish an authorized exception from a mistake or an arbitrary deviation.

We call this missing process layer the **decision-trace deficit**. A decision trace is not an ordinary log or a post-hoc model explanation. It is a time-indexed, source-linked, and authority-bearing record of actors, observed state, claims, attempted alternatives, evidence, applicable rules, revisions, reasons, uncertainty, overrides, and subsequent effects. This framing builds on decision provenance, which exposes chains of decision inputs, actions, and downstream consequences for accountability [20].

Institutions are not necessarily devoid of reasons. Process evidence may be scattered across PDFs, email, meeting records, field logs, and individual memory. The structured layer, however, commonly privileges current state and outcome, while the links needed to replay the decision moment remain incomplete. High-consequence document intelligence is therefore not only an extraction-and-prediction problem. Each value must also have a source, time of availability, construct, actor, rule context, and permissible consequence. If any link fails, discrimination can be real while the decision interpretation is false.

This problem is acute in administrative archives. A single case file can contain an operator request, agency correspondence, a revised work plan, an approval, subsequent field activity, and a final certificate. Collapsing those layers enables temporal leakage. Treating the historical outcome as normative truth creates a selective-label problem because the archive records only the path that was observed under prior policy and documentation practices [8]. Geographic or template dependence can further inflate random cross-validation, motivating group-aware evaluation [9].

We studied Pennsylvania oil-and-gas well-plugging records. Under 25 Pa. Code §78.1, attainable bottom is the Department-approved depth achievable after reasonable effort is expended to clean out to total depth [3]. The regulation does not say maximum or greatest effort. An operator may request to stop above TD after encountering an obstruction or other non-routine condition. The prospective question is not simply where a historical plug ended. It concerns what was known and attempted, what constrained attainability, which evidence and rule applied, why the request changed, and who authorized the disposition.

The project underwent three corrections. First, locating a historically selected event within approved cases was not equivalent to predicting a regulatory decision. Second, historical depth shortfall or difficulty was not effort adequacy. Third, final-state files could not reliably reconstruct the request-time information set. A related correction narrowed an initially broad effort concept to documented non-routine difficulty (DN): absence of documentation could not be interpreted as absence of effort.

These corrections showed that a final state cannot uniquely invert to the decision-time world. They motivate a conjunctive validity framework:

1. **Measurement validity:** Was the fact read correctly from its source?
2. **Temporal validity:** Was it available at the modeled index time?
3. **Construct validity:** Does the target represent the intended decision concept?
4. **Generalization validity:** Does evaluation reflect actual group and distribution shifts?
5. **Authority validity:** Do the preceding results justify the proposed consequence?

Our contribution is not a higher-scoring approval model or an LMM-generated reconstruction of unrecorded reasoning. We distinguish outcome archives, structured state, and decision traces; reconstruct provenance-bearing fragments; audit what remains unidentifiable; separate documented effort evidence from difficulty context; and propose a hybrid architecture that produces versioned prospective traces while withholding unsupported authority.

### 1.1 Relation to prior work and regulatory context

The study is situated at the intersection of document understanding, process/decision provenance, selective-label prediction, and high-consequence AI governance. Process mining begins from event logs, but log suitability and trustworthy linkage constrain what processes can be recovered [21]. Decision provenance extends beyond events to the inputs, actions, entities, and downstream effects needed for accountability [20]. OCR-free and multimodal document models can preserve visual structure that text-only pipelines lose [6,7], but source-grounded extraction does not itself establish a complete trace or target validity. Selective labels make historical decisions incomplete supervision for counterfactual policy questions [8], while spatial and hierarchical dependence require evaluation designs that reflect the intended shift [9]. Calls for interpretable high-stakes systems and the NIST AI Risk Management Framework motivate explicit authority boundaries [10,11]. Datasheets, model cards, TRIPOD+AI, data-cascade analysis, and reproducibility guidance inform our artifact discipline [12–16]; local version freezing is distinguished from formal preregistration [17]. Implementations used scikit-learn estimators [18,19]. Domain interpretation remains subordinate to current Pennsylvania forms, regulation, attainable-bottom proceedings, and AI policy [1–5].

## 2. Study design and research questions

### 2.1 Data scopes

The corpus had several nonexchangeable denominators.

**Table 1. Data scopes and analytic roles**

| Scope | N | Role |
|---|---:|---|
| Raw directories | 913 | 912 roster/in-scope folders plus one known stray |
| PDF-backed folders | 635 | Source-available extraction universe; approximately 1,700 PDFs |
| Folders without local PDFs | 277 | Potential digital-availability selection mechanism; not negative evidence |
| v6 unique case table | 633 | Extracted case rows before the principal stray/eligibility filter |
| v6 QA scope | 632 | Eligible case rows after known-stray exclusion |
| Frozen shortfall cohort | 631 | 250 positive, 381 negative, 29 counties |
| DN/plugging stratum | 424 | DN and form-model research cohort |
| Model-B teacher-available cases | 423 | Difficulty-proxy evaluation |
| Anomaly reference set | 354 | Operationally defined scoreable, non-audited-refused, non-suspect-TD records |
| Canonical merged schema | 656 × 170 | Research inventory including identity, provenance, QA, checklist, and outcomes—not 170 serving features |

The 354-record anomaly set should not be called 354 independently confirmed approvals. The code-defined inclusion rule did not require a newly verified approved outcome.

### 2.2 Research questions

- **RQ1:** Which provenance-bearing decision-trace fragments can multimodal extraction, deterministic guards, and internal multi-agent review recover, and which elements remain unidentifiable?
- **RQ2:** Under group-aware evaluation, what internal associations are observed for a mixed nongeographic evidence/well-context profile versus a county/formation geography prior? This is not a causal contribution decomposition.
- **RQ3:** Which missing effort/action and deliberation traces prevent historical shortfall/difficulty from identifying effort adequacy, and how do censoring and selective labels alter the interpretation?
- **RQ4:** Which checklist and DN signals survive frozen definitions, internally blinded reading, source adjudication, and bidirectional audit?
- **RQ5:** How should failed G9, Path-B, and retrospective-routing tests constrain system authority?

This was a retrospective methods and system-development study. Conversation histories and 57 Git commits were used to reconstruct decision chronology and withdrawn interpretations, not as quantitative outcome data.

### 2.3 Decision-trace framework and evidentiary decomposition of reasonable effort

For case \(i\) at index time \(t\), an idealized trace is:

\[
T_i(t)=\{S_i(t),E_i(t),D_i(t),L_i(t),P_t,R_i(t),A_i(t),U_i(t),\Pi_i(t)\},
\]

where \(S\) is visible state, \(E\) source-linked effort/action evidence, \(D\) well and observed difficulty context, \(L\) request-feedback-revision deliberation, \(P_t\) the applicable rule/policy version, \(R\) the request or claim, \(A\) the authorized action and reason, \(U\) uncertainty/override, and \(\Pi\) provenance. Later outcome \(O_i\) is linked separately and must not overwrite \(T_i(t)\).

The historical structured table observes only an incomplete projection \(X_i\) and mixes in later \(O_i\). Consequently, training \(P(O_i\mid X_i)\) is generally not equivalent to estimating request-time reasonable-effort adequacy:

\[
A_i^*=H\{E_i(t),D_i(t),L_i(t),P_t,accepted\ evidence,qualified\ expert\ standard\}.
\]

We therefore retained two descriptive evidence channels without treating them as an automated measure of \(A_i^*\):

1. a **documented effort/evidence channel** containing dated attempts, methods, tools, reached depths, obstructions, remedies, results, and sources; and
2. a **difficulty-context channel** containing request-time TD, well age, casing, coal, freshwater, reached depth, and observed impediments.

County/formation geography was a separate group background. TD, age, casing, water, and coal were nongeographic well/environmental covariates. Both descriptive channels still require a deliberation/rule gate and a qualified reviewer. This is a functional decomposition for review, not a causal factorization of latent effort and difficulty.

### 2.4 Evaluation design and statistical reporting

The experiments used nonexchangeable cross-validation and uncertainty summaries; we do not interpret every “±” as the same quantity.

- The 631-case historical-shortfall analysis used five-fold `StratifiedGroupKFold` by county over five split seeds. Each seed produced a complete out-of-fold (OOF) vector, and means and SDs were calculated across the five repeat-level metrics. Thus, 0.7400±0.0090 reports split-level AUC dispersion, not a confidence interval.
- Model A used `StratifiedGroupKFold(county)`, five seeds×five folds. The training script summarized valid held-out-fold AUCs; 0.8366±0.1097 contains fold-AUC dispersion, not repeat-level SD or a confidence interval.
- Model B permuted rows for five seeds and then called `GroupKFold(shuffle=False)`; the held-out county sets did not change. We therefore treat 0.418±0.047 as a Spearman fold summary from one effective five-fold county-grouped partition, not independent 5×5 repeated CV.
- The repeat-0 evidence-versus-geography comparison used a shared OOF vector with case and county-cluster bootstraps. It is not the difference between five-repeat mean AUCs.
- G9 used a two-sided Fisher exact test plus repository-frozen refused-side cluster-collapse and tuning-untainted sensitivities. A probability-ordered discrete p value and an equal-tail exact interval need not be strict duals.
- Naive Clopper–Pearson intervals for checklist panels displayed small-denominator uncertainty. Repeated model readers were nested within cases and potentially correlated, precluding independent-Bernoulli interpretation.
- Path B used paired AUC differences on 25 shared grouped folds and a frozen two-part absolute-plus-incremental gate.

Classification results prioritized ROC AUC, with average precision, Brier score, and top-of-queue precision where retained. The proxy regressor used Spearman correlation and bin agreement. Except where bootstrap or exact intervals are explicitly reported, SDs are not population confidence intervals; the broader exploratory model search was not a multiplicity-adjusted confirmatory analysis.

### 2.5 Terminology and internal identifiers

- **LMM:** large multimodal model, used for candidate extraction or visual reconciliation.
- **HGB:** histogram gradient boosting; Model A is a classifier and Model B a regressor.
- **OOF:** out-of-fold prediction generated for records held out from the corresponding fit.
- **v6:** the sixth major internal revision of the multimodal extraction/modeling pipeline, not an external standard.
- **G8:** the internal blind-reader reliability gate for track separation, vocabularies, and field emissions.
- **G9:** the frozen DN association gate contrasting audited refusals with historical approved-status cases; the primary test and two sensitivities all had to pass.
- **Path B:** the frozen checklist-augmentation ceiling-break backtest on the old `y_needed_short` task.
- **D1:** normalized shortfall relative to TD; historical-reference and current-request D1 use different depth sources and must be labeled separately.
- **CK1–CK4:** four draft runtime-checklist items covering request-form presence, effort narrative/evidence, decision-relevant depth numbers, and depth-number timeliness.
- **Quadrant:** the 2×2 preliminary triage label defined by checklist pass/fail and tail yes/no; it is not an approval decision.
- **Decision trace:** a replayable unit organized by case, time, source, action, rule, reason, and authority. This study reconstructed fragments, not complete deliberation.

---

## 3. Part I—Multimodal, multi-agent reconstruction of partial decision traces

### 3.1 Multimodality was a measurement requirement

The source files contained scanned text, handwriting, checkboxes, stamps, diagrams, tables, and cross-page relationships. OCR was useful for candidate retrieval but could flatten visual state. The v6 pipeline therefore supplied PDFs to a multimodal API and designed visual fields to carry a source file, page pointer, quotation, evidence type, and temporal/depth track. A later full-corpus pass reviewed all 635 source-backed folders and pre-rendered 17 oversized PDFs across 14 cases at 150 dpi.

The configured multimodal model used a floating alias, and not all batch-generation parameters were completely pinned. We therefore do not describe extraction as deterministic. Reproducibility depends on archived raw responses, derived artifacts, and code history rather than the assumption that a future model call will reproduce identical text (Fig. 1).

### 3.2 Provenance was part of the output

For visual evidence, the intended unit was:

\[
E=(case,source\ file,page,quotation,visual\ state,track,timing).
\]

Some well attributes and labels originated in a legacy Excel register, so the accurate claim is that a field should resolve to a PDF page, legacy register, or deterministic derived ledger—not that every feature came from a PDF page. Later pointer repairs showed that value correctness and citation correctness are distinct endpoints.

This provenance tuple is an **evidence object**, not a complete decision trace. A full trace would also require actors, attempted alternatives, request-feedback revisions, the applicable rule version, the authorized reason, and any override. Extraction can make a recorded fragment visible; it cannot create deliberation that was never recorded.

### 3.3 Requested, approved, and final-state tracks were separated

To replay the index-time world, the pipeline emitted operator-requested depth, agency-approved depth, and certificate/final-state depth separately. TD anchors, observed obstructions, maximum reached depth, and proposed stop also retained timing and source attributes. A certificate can corroborate what eventually occurred but is not request-time evidence. An approved attainable-bottom value is an outcome of the reviewed process and can become circular if used as a prospective feature. Track separation prevents later outcome from overwriting decision state.

### 3.4 Deterministic guards and quarantine created negative authority

Post-processing checked numeric plausibility, source support, current-job context, and temporal/track consistency. Suspicious outputs were quarantined rather than silently coerced. The final v6 artifacts contained 10,856 depth rows, 436 quarantine records, and 21 current-job guard events.

The resulting authority chain was asymmetric. OCR could propose a candidate; a rendered page could disconfirm an OCR-only interpretation; deterministic guards could withhold a field from downstream use; and an investigator or reviewer could accept, correct, or reject it. Multiple components were valuable because errors remained localizable, not because a vote converted correlated models into truth.

### 3.5 Internal blind-agent reading was not expert ground truth

The project used independently executed AI-agent reads, frozen emission vocabularies, source-page adjudication, and investigator/user rulings. The main G8 exercise produced 23 cases × 2 reads = 46 outputs. Its reliability subset was 18 cases × 2 = 36 outputs; five anchors × 2 = 10 outputs were excluded from that denominator. A six-case confirmation panel added 12 outputs. Counts such as 11/18, 14/18, 6/6, and 4/6 represented agreement, not correctness. The reported absence of contamination across 58 outputs also involved nested and correlated reads.

These exercises identified unstable tokens, source-pointer failures, and definition reversals. They did not constitute validation by independent human domain experts. We therefore use the phrase *internally blinded AI-agent reading with investigator adjudication*.

### 3.6 What the pipeline established

The v6 merge produced 633 unique case rows and 10,856 depth rows. Two large batches returned 818/818 and 483/483 successful HTTP responses; those were transport counts, not case-accuracy counts. On a fixed 40-case targeted regression set, observed-depth presence, physical-blocker presence, and historical-seal presence each achieved precision and recall of 1.0. Because that set was designed around known failure modes rather than sampled from the corpus, it established internal regression stability for those fields, not corpus-wide or external accuracy.

RQ1 is therefore a bounded affirmative: the workflow produced auditable and quarantinable evidence artifacts. It did not establish expert reference accuracy or reviewer utility.

### 3.7 Trace-completeness audit: abundant records, sparse action detail

The 170-column schema revealed a stratified trace-coverage landscape (Figs. 2–3). Administrative and well fields were common—operator request 96.0%, alternative-method filed 94.8%, and coal-seam indicator 90.8%. Request narratives had intermediate coverage: any request evidence 41.0%, causal reason 36.8%, and any struggle 31.8%. Depth evidence was generally 15%–30%. Fine-grained work-record difficulty, remedy, and obstruction flags were almost all below 2.5%.

This was not an absence of event records. The 424-case cohort contained 2,874 dated events; 423/424 cases had at least one, with median six and maximum 30. However, 2,375/2,874 (82.6%) were assigned only to the coarse phase *other*, versus 457 plugging and 42 cleanout events.

Comparable difficulty concepts appeared more often in request narratives than in separately aggregated work records: cave-in/collapse 17.45% versus 0.24% (approximately 74-fold), hard fill/no progress 12.5% versus 2.36% (5.3-fold), stuck/lost tools 5.90% versus 1.89% (3.1-fold), and casing failure 3.77% versus 1.18% (3.2-fold). Mine-through was 7.31% versus zero. These are trace-coverage or extraction prevalences, not event-incidence estimates (Fig. 4).

Only 197/2,874 events had a tool token; 93.15% had none. Deployment method was unknown in 2,687/2,874 (93.49%). The 169 raw tool strings included synonyms, mixed granularity, and OCR noise. Absence of a tool token does not establish that no tool was used, and the historical sample cannot currently support reliable tool/remedy inference (Fig. 5).

The empirical consequence was construct contraction. The archive could support documented-evidence retrieval and triage; it could not directly supervise effort adequacy. An integrated coverage panel shows that 99.8% of cases had a ledger row but only 6.1% had explicit attempted-and-failed evidence (Fig. 6). Having records was not equivalent to having a replayable action trace.

---

## 4. Part II—Choosing the correct model requires choosing the correct task

### 4.1 Leakage ladder and the retirement of step location

The earliest task sought the historically selected event within an already approved case. The final audit included 103 cases and 379 event rows with case-grouped cross-validation. A depth/TD gradient-boosting model achieved AUC 0.916; depth relative to approved attainable bottom reached 0.954–0.958. Yet a zero-parameter deepest-event rule recovered 79/103 labels (76.7%). The first score largely reproduced label construction; the second used an outcome anchor. The task was retired as a forward-decision model.

This result illustrates why a leakage ladder should begin with free baselines. If rank, maximum, or an outcome-derived denominator already recovers the label, additional modeling cannot confer prospective meaning.

### 4.2 RQ2: grouped generalization and feature ceilings

The next task used a 631-case historical shortfall proxy. Primary evaluation used five-fold StratifiedGroupKFold with county as group, repeated over five split seeds.

**Table 2. Principal frozen-cohort classification results**

| Evaluation | Profile | Model | AUC mean (SD) |
|---|---|---|---:|
| County-grouped | Nongeographic request evidence + well-context covariates | HGB | 0.7400 (0.0090) |
| County-grouped | v6 predecision depth | HGB | 0.7383 (0.0080) |
| County-grouped | Legacy 11 | Logistic L2 | 0.7353 (0.0039) |
| County-grouped | Geography only | HGB | 0.6247 (0.0061) |
| Random stratified | v6 predecision depth | HGB | 0.7858 (0.0071) |

In retained repeat-0 shared out-of-fold vectors, the nongeographic profile achieved AUC 0.7454 versus 0.6207 for geography alone, a paired difference of 0.1247 with county-cluster bootstrap interval 0.0578–0.2244. Three concepts must remain distinct: the geography-only profile was county/formation; TD, age, casing, water, and coal were nongeographic well/environmental context; and request narratives, events, and depth evidence were document evidence. Because the `evidence/covariates` profile mixed the latter two, it was not an effort-only profile and the 0.1247 difference did not estimate whether “effort matters more than geography.”

The commonly cited nonlinear-versus-linear increment of approximately 0.056 came from a separate random-stratified shared-OOF bootstrap and is secondary to the grouped evaluation. A three-model ensemble yielded a five-split summary AUC of 0.759 (SD 0.005); the strongest directly retained repeat-0 artifact had AUC 0.7567, AP 0.6943, and Brier 0.1921.

Evidence/covariates carried more ranking information than geography alone, random splitting was optimistic, and richer v6 features did not materially exceed simpler profiles. Those are empirical associations, not a decomposition of causal contribution.

### 4.3 RQ3: censoring broke the effort-adequacy interpretation

An exploratory audit identified 89 cases in which certificate depth approximately matched approved attainable bottom. The retained shortfall model had AUC 0.7567 under the original label, 0.7423 after exclusion, and 0.6885 after negative relabeling. The sensitivity analysis did not estimate a new deployable model. It showed that the historical target could not stably distinguish difficult-but-completed cases from inadequate effort.

The score was consequently renamed historical shortfall-risk/difficulty ranking. Documented effort/action evidence and difficulty context can be presented separately, but they cannot be added into a historical adequacy score. A reasonable-effort judgment also requires the contemporaneous rule version, deliberation, accepted evidence, and a qualified reviewer.

### 4.4 RQ4: checklist and DN survived only after narrowing

The request checklist separated factual extraction from normative judgment and preserved the three depth tracks. The research instrument evolved from v1 through v1.4 in response to frozen-panel failures. The current runtime CK1–CK4 implementation is labeled **v1.5-DRAFT** and adds engineering rules for depth-number presence and timeliness; it has not undergone legal or independent-expert validation and should not be conflated with the completed v1.4 internal reads.

**Table 3. Checklist and DN signals that survived, were revised, or were retired**

| Signal/rule | Main panel | Confirmation/audit | Disposition | Permitted interpretation |
|---|---:|---:|---|---|
| Request A/B track separation | 17/18 agreement | Not separately re-estimated | Retained | Internally stable track definition |
| S2 strict vocabulary | 11/18 | 6/6 after clarification | Retained after revision | Vocabulary required narrowing |
| S4 exact token set | 14/18 | 4/6 | Unstable token retired | Not suitable for downstream rules |
| S4 parent binary | 18/18 | 6/6 | Binary parent retained | Only the coarser construct survived |
| C3 | One adjudicated false positive in development | 6/6 agreement; zero adjudicated false positives | Cautiously retained | Small-sample internal stability, not population specificity |
| Cross-track contamination | 0/46 outputs | 0/58 outputs in total | Track rule retained | Outputs were nested and correlated |
| DN positive construct | 112/424 positives; each positive internally reviewed | Five positive-to-negative, one negative-to-positive, 15 pointer repairs | Retained as documented difficulty | Not effort or adequacy |
| DN negative side | Not exhaustively reviewed | Zero flips in a 20-case blind sample | Sample support only | No claim of complete negative validation |

DN was defined as documented non-routine difficulty, not effort, diligence, compliance, approval, or refusal. Internal adjudication identified 112/424 positives, including 105/411 historical approved-status and 7/13 audited-refused cases. All positive calls were individually reviewed internally; only a blinded 20-case negative sample was audited. The enumerated trail contained five positive-to-negative changes, one negative-to-positive change, and 15 pointer repairs. One narrative source said six positive-to-negative changes but listed five; we report the enumerated value.

### 4.5 From 108 archival variables to 17 trace-compatible fields

The archival DN model used 108 variables, including certificate/completion-presence fields, and was therefore not request-time valid. In a full-refit permutation-importance calculation, only seven features had reported positive values; 101 were approximately zero in that calculation. These values were tiny and descriptive, not causal effects or formal significance tests.

The 108-feature archival model had internally grouped AUC 0.8412 (fold SD 0.1136). A 17-field request-time-compatible DN model had AUC 0.8366 (fold SD 0.1097). The point estimates were close, but no equivalence test was performed (Fig. 7).

Both form models implemented in the research prototype use the same 17 fields: six well descriptors (TD, well age, casing count, deepest casing depth, coal, freshwater); four file/event counts; three request-evidence indicators (alternative-method form, attempted-and-failed narrative, causal reason); and four depth-evidence variables (maximum reached, obstruction, maximum-reached/TD, and presence of a proposed stop). The first six are well/environmental context, not a geographic profile. The file, event, and narrative indicators are only a small projection of an effort trace, not a complete effort history. The models do not consume the proposed-stop numeric value; that value enters the subsequent D1 calculation. County, operator, permit identity, certificate, and completion fields are excluded.

“Request-time/trace-compatible” means that the variables can be collected at submission. It does not mean that 17 fields represent a complete decision trace or have been validated on a prospective intake cohort.

### 4.6 Model A: documented-difficulty trace triage

Model A is an HGB classifier trained on the project DN label. It writes a DN prescreen score and orders the human review queue from high to low. Under `StratifiedGroupKFold(county)` with five seeds×five folds, its official internally grouped AUC was 0.8366 (valid-held-out-fold SD 0.1097). That SD is neither repeat-level dispersion nor a confidence interval. AUC is not percent accuracy, and the score should not be represented as a calibrated probability.

Model A does not enter the current 2×2 quadrant formula. It estimates whether the available record resembles internally adjudicated documented non-routine difficulty—not whether the action trace is complete. It does not estimate engineering difficulty, effort adequacy, compliance, or approval probability. Queue ordering nonetheless allocates attention and can affect waiting burden; prospective use therefore requires subgroup and document-quality audits.

### 4.7 Model B: empirical context and reference selection

Model B is an HGB regressor trained to approximate a locked historical shortfall ensemble, not an objective expert difficulty label. It does not consume the county/formation geography-only profile and does not recover causal geologic difficulty. It estimates the teacher score and selects one of five teacher-defined reference strata using frozen cutpoints. The current training loop shuffled rows but reused `GroupKFold(shuffle=False)` county assignments across seeds. Its 0.418 (fold SD 0.047) is therefore the fold-mean Spearman correlation from one five-fold county-grouped partition, not 5×5 independent repeated CV or a confidence interval. Exact-bin agreement with the teacher was 35.5%; agreement within one bin was 72.3% (Fig. 8).

For a current request, the application separately calculates

\[
D1_{request}=clip[(TD-proposed\ stop)/TD,0,1]
\]

and compares it with the P90 of the stratum selected by Model B. The resulting tail flag combines with the checklist in the preliminary routing formula. Model B therefore has indirect routing influence: it does not make the final decision, but selecting the wrong ruler can change the flag.

The concise functional division is: **Model A determines who is seen first; Model B proposes which historical ruler to use.** It is not a causal factorization of effort and geography.

### 4.8 Teacher-conditioned comparison was a proof of concept, not deployed calibration

The anomaly reference comprised 354 operationally defined scoreable, non-audited-refused records with nonsuspect TD. The locked teacher formed strata of 70–71 records. Median historical outcome-label shortfall increased from 0.037 in Q1 to 0.281 in Q5 (7.6-fold), while DN prevalence increased from 8.5% to 40.8% (4.8-fold). This established internal association, not objective difficulty validity (Fig. 9).

Historical reference shortfall was calculated using the outcome field `label_bottom_of_plug`:

\[
D1_{ref}=(TD-label\_bottom\_of\_plug)/TD.
\]

The current request uses proposed stop. Their comparability is an unvalidated transport assumption.

Teacher-stratum P90 values were 0.332, 0.276, 0.415, 0.456, and 0.552. A hypothetical request D1 of 0.45 therefore fell at approximately the 95.6th, 99.5th, 91.7th, 89.5th, and 73.8th percentiles across Q1–Q5. The nonmonotonic Q1/Q2 P90 also reveals finite-sample noise (Fig. 10).

A pooled P90 of 0.455 flagged 4.2%, 1.4%, 8.6%, 11.3%, and 25.4% across teacher strata. Defining P90 within each teacher stratum produced nominal tail masses near 10% (Fig. 11). This is a counterfactual review-allocation demonstration, not proof of legal fairness. Moreover, Figs. 9–11 use the locked teacher to assign strata, whereas runtime uses Model B. They must be described as a **teacher-conditioned proof of concept; end-to-end proxy-conditioned calibration remains unvalidated**.

### 4.9 RQ5: failure gates removed authority

The nominal G9 comparison was 7/13 DN-positive audited refusals versus 105/411 historical approved-status cases, sample OR 3.40, conditional equal-tail exact 95% interval 0.951–12.500, and two-sided Fisher p=0.0477. The refused-side duplicate-cluster sensitivity yielded 5/10 and p=0.136; the tuning-untainted sensitivity yielded 4/10, OR 1.94, and p=0.291. Because both frozen sensitivities failed, G9 was blocked.

**Table 4. Failure gates and their authority consequences**

| Gate | Result | Frozen interpretation | Authority consequence |
|---|---|---|---|
| G9 primary | 7/13 vs 105/411; OR 3.40; exact interval 0.951–12.500; p=0.0477 | Nominal primary signal with small denominator | Insufficient alone |
| G9 cluster sensitivity | 5/10; p=0.136 | Required supportive p<0.10 | Failed |
| G9 tuning-untainted sensitivity | 4/10; OR 1.94; p=0.291 | Required supportive p<0.10 | Failed; G9 blocked |
| Path B | AUC 0.6841; increment 0.0107; 11/25 positive folds | Required combined AUC >0.764 plus increment | Ceiling-break claim closed |
| Anomaly | 10.17% OOF tail at nominal 10% | Implementation check only | Explanation flag only |
| Routing smoke | Five of seven depth refusals in fast lane | Direction should be operationally sensible | Final-state routing rejected |

Path-B checklist augmentation achieved combined AUC 0.6841, increment 0.0107 (SD 0.0431), with 11/25 folds positive; it failed the required combined AUC above 0.764. A nominal 10% anomaly implementation produced a 10.17% internal OOF tail, which checked code behavior rather than substantive insufficiency. Finally, retrospective routing sent five of seven depth-related refusals to a fast lane because approved/completed final-state evidence made them resemble successful records.

No thresholds were retuned after these results. DN lost approval/refusal interpretation; checklist augmentation did not establish a repaired adequacy target; anomaly retained only an explanation-needed meaning; and final-state retrospective routing was rejected.

---

## 5. Part III—An agent architecture that turns trace-poor consumption into prospective trace production

### 5.1 Research multi-agent work and runtime components were distinct

During research, multiple agent roles performed case extraction, independent blind reading, source reconciliation, and audit support, followed by investigator adjudication. The current runtime is not an autonomous planner with agent delegation or negotiated decisions. It is a hybrid pipeline containing two optional LMM functions, two conventional ML models, deterministic rules, retrieval, and a reviewer interface.

The architectural contribution is authority separation and prospective trace production, not the number of models.

### 5.2 Current implemented sequence

The optional prefill service renders up to 30 PDF pages and proposes editable values with `{file,page}` pointers. Structured intake is then validated for attestations, depth≤TD, dates, measurement method, attempted-work narrative, and future-date conflicts. At submission, the application immediately computes compliance flags, CK1–CK4, Model A, Model B, an in-bin anomaly, a preliminary quadrant, and retrieval/supplement context.

Model A is stored as `dn_prescreen` and orders the submission list; it does not enter the quadrant. Model B selects a bin and indirectly affects the route through the tail flag. Compliance red overrides the displayed quadrant. Retrieval does not directly modify the quadrant.

Files are uploaded and LMM reconciliation is queued after the initial route. That reconciliation checks the existence, date, tense, and depth of DN claims, but is currently Stage-1 advisory: it does not alter CK2, the original quadrant, or the Model-A queue. A reviewer separately records a final action. The current record does not consistently link all request-feedback revisions, policy versions, field acceptances, and mandatory rationales; it is not yet a complete decision-trace ledger.

The current effort-path 2×2 is:

**Table 5. Preliminary 2×2 routing in the current prototype**

| v1.5-DRAFT checklist | Tail in the Model-B-selected stratum | Current preliminary label | Permitted manuscript meaning |
|---|---|---|---|
| Pass | No | `FAST_LANE` | Lower nominal escalation priority; not approval |
| Pass | Yes | `DEEP_REVIEW` | Documentation passes, but shortfall lies in the selected reference tail |
| Fail | No | `SUPPLEMENT` | Checklist-specified material should be requested |
| Fail | Yes | `PUSHBACK` | Missing evidence plus a tail flag; higher-level human review only |

A compliance red flag overrides these labels with `COMPLIANCE_REVIEW`. If the anomaly is unscoreable, the code uses checklist status alone. These are current software strings; the `FAST_LANE` action text remains approval-like and must not be treated as an authorized regulatory action.

### 5.3 Proposed consequence-bounded sequence

The evidence-constrained design reverses the critical authority order (Fig. 12):

```text
request-time intake
→ claim-to-source reconciliation
→ qualified reviewer accepts relevant fields
→ bounded models, checklist, rules, and retrieval
→ non-decisional review routing
→ human action with mandatory reasons
→ versioned decision-trace ledger
→ prospective labels derived only after validation
```

Human control is substantive only if source review and field acceptance occur before an adverse or expedited consequence becomes operative. A post-hoc signature after an automated lane has already shaped the case is insufficient. Each request, agency response, supplement, revision, field observation, rule version, field acceptance, override, decision reason, and later outcome should be stored as a separately versioned event. The system thereby becomes data infrastructure that produces future decision traces rather than merely consuming historical outcomes.

### 5.4 Component authority matrix

| Component | Permitted role | Prohibited interpretation |
|---|---|---|
| Prefill LMM | Propose editable source-linked candidates | Establish facts or approve |
| Reconciliation LMM | Return verified/mismatch/not-found flags | Exercise veto or claim external validation |
| Model A | Allocate review-queue attention | Difficulty, adequacy, compliance, approval probability |
| Model B | Select an empirical reference stratum | Objective difficulty, effort, approval probability |
| Anomaly table | Flag a tail requiring explanation | Misconduct, insufficiency, or refusal |
| Checklist | Expose missing or conflicting documentation | Complete legal standard or unreviewed veto |
| Compliance rules | Make explicit declarations visible | Validated exhaustive legal adjudication |
| Retrieval | Present similar text for context | Verified precedent or approval likelihood |
| Qualified reviewer | Accept evidence, interpret standards, act, and give reasons | Delegate accountability to the model |
| Decision-trace ledger | Version state, sources, rules, revisions, acceptance, reason, override, and later outcome | Claim that current logs are complete deliberation or clean gold |

### 5.5 Current implementation gaps

The present software does not yet enforce the proposed boundary. Preliminary quadrants are calculated before reconciliation and reviewer acceptance. Reconciliation does not gate CK2 or routing. Field-level provenance sent by the front end is not yet fully persisted by the current submission schema. Declared or placeholder filenames can affect file count and checklist logic without guaranteeing a corresponding uploaded file. Compliance red overrides a route but does not short-circuit or hide Model-A/B and anomaly outputs. Some lane text still contains approval-like language. Reviewer actions do not require field-level acceptance, bin override, mandatory reasons, a frozen evidence/rule/model snapshot, or a linked request-feedback-revision chain.

The RAG prototype also lacks a completed 20-query validation and has known metadata/filtering defects. Decision logs are structured prototype feedback, not complete decision traces or clean prospective labels. These gaps mean that the current quadrant is a preliminary research label, not an authorized approval, refusal, veto, or expedited action.

### 5.6 Expert escalation and dormant authority

Source absence, visual/OCR disagreement, track conflict, bin-boundary sensitivity, consequential compliance flags, or disagreement among Model A, Model B, checklist, and rules should trigger qualified review. The system should preserve index-time state, source pages, rule/policy version, request-feedback-revision links, model version, uncertainty, acceptance, override, reason, and later outcome. Reconciliation gating, adverse or expedited routing, RAG evidentiary authority, and retraining from reviewer decisions should remain dormant until their own frozen validation gates pass.

---

## 6. Discussion

### 6.1 Decision traces are the missing layer of agent-ready data

The project was a trace-completeness stress test. Among 424 cases, 99.8% had a dated ledger row, yet only 6.1% had explicit attempted-and-failed evidence; only 197/2,874 dated events contained a tool token; administrative variables covered roughly 90%–96%, while most fine-grained action flags were below 2.5%. The institution did not lack records. It lacked a consistently time-indexed, source-linked, actor-aware, rule-versioned, and reason-bearing representation sufficient to replay a reasonable-effort decision.

Decision provenance emphasizes decision pipelines rather than isolated algorithm outputs [20]. Our findings add an empirical asymmetry: multimodal methods can recover recorded fragments, but no extraction model can create an unrecorded meeting judgment, phone exchange, rejected alternative, or policy version. Agent-ready data therefore require a write path, not only a better read path. The prospective contribution of the system is to capture future request, revision, acceptance, reason, override, and outcome events as a versioned trace.

### 6.2 AUCs from different tasks are not a progress curve

The project generated apparently strong numbers—approximately 0.916 for step location, 0.759 for shortfall ranking, 0.841 for archival DN triage, and 0.837 for request-time-compatible DN prescreening. They belong to different units, index times, targets, evidence windows, and actions. The first was circular; the second ranked a historical shortfall proxy; the third included post-work availability; and the fourth reproduced an internally adjudicated documentation construct.

Every score should be reported with:

\[
(unit,index\ time,target,evidence\ window,permitted\ action).
\]

Without that tuple, a performance number is not a decision claim.

### 6.3 Negative results were architectural inputs

Richer features did not break the grouped ceiling. Refusal ground truth collapsed under source review. G9 failed sensitivity requirements. Path B missed its threshold. Retrospective routing inverted the intended logic. Each failure removed a permission before deployment rather than becoming a limitation after deployment. We call this failure-gated authority.

### 6.4 Provenance and trace correctness should be evaluated as endpoints

Document AI needs separate measures of field-value accuracy, citation correctness, track correctness, and time correctness. Decision-trace systems additionally require actor, action, rule-version, revision-link, reason, and override correctness. A numerically correct value from the wrong page or a completion certificate is not valid request-time evidence. OCR should have recall authority, page vision disconfirming authority, and the qualified reviewer evidence-acceptance authority.

### 6.5 Difficulty conditioning allocates review burden; it does not decide adequacy

Within-teacher-stratum percentiles illustrate why a pooled threshold can concentrate review burden in historically difficult strata. They do not define reasonable effort or prove fairness. The historical-to-current D1 transport assumption and Model-B bin error must be evaluated prospectively. If adjacent plausible bins change the tail flag, the safe response is escalation, not silent certainty.

### 6.6 Hybrid accountability is not merely “model plus rules”

LMMs are useful for candidate evidence and reconciliation; statistical models for ranking and approximation; deterministic rules for explicit, reviewable conditions; and qualified humans for contextual and normative judgment. The contribution lies in ensuring that each component cannot inherit authority from another component's strength.

## 7. Limitations

The archive did not completely preserve meetings, calls, email, policy versions, rejected alternatives, or unrecorded human reasons. We reconstructed provenance-bearing fragments, not the full deliberation; an LMM must not fill such absences with generated facts. No independent external expert standard was available for checklist, DN, or refusal mechanisms. The same document universe informed schema revision, coding, model development, anomaly analysis, and prototype construction. County grouping did not hold out operators, related wells, templates, form revisions, or time. The 277 folders without local PDFs may be systematically selected. Refusal samples were small and heterogeneous. Fold SDs are not confidence intervals.

The anomaly reference was operationally non-refused, not entirely reverified as approved, and used an outcome-label depth rather than proposed stop. Model A and Model B were trained from retrospective archives despite trace-compatible inputs; their functional division is not causal identification of effort and difficulty. Historical and production event vocabularies remain incompletely aligned (Fig. 13). Proprietary model aliases and runtime parameters were not fully pinned. No prospective reviewer study has shown time savings, improved decisions, or resistance to automation bias.

## 8. Required prospective evaluation

The next study should acquire a locked request-time decision-trace cohort before outcome documents exist. Each request, agency response, supplement, revision, field observation, field acceptance, rule/policy version, override, decision reason, and later outcome should be saved as a separate actor- and time-stamped event with source links. Two independent oil-and-gas/DEP experts should code primary fields, DN, documentation completeness, difficulty strata, and decision reasons, with a third expert adjudicating. Evaluation should include exact and tolerance-based depth error, citation correctness, track/time contamination, trace-field capture, revision-chain completeness, false linkage, reason completeness, and disagreement—not only adjudicated labels.

External validation should hold out operator, time, template family, and geography. Model B requires end-to-end proxy-conditioned calibration and subgroup review-burden analysis. A reviewer crossover should compare unaided review, evidence retrieval only, evidence plus checklist, and the full bounded interface, measuring review time, missed evidence, agreement, override, recovery from deliberately incorrect suggestions, confidence calibration, and contestability.

Each new authority requires a separate gate. Extraction accuracy must not automatically authorize routing; routing utility must not automatically authorize adverse recommendations; and approval/refusal assistance requires legal, engineering, differential-impact, and automation-bias review.

## 9. Reproducibility, ethics, and governance

The project preserved raw responses, derived tables, protocols, out-of-fold artifacts, and version history. Historical specifications were frozen in local Git before corresponding runs, but were not demonstrated to have been prospectively deposited in an immutable third-party registry. We therefore use *version-controlled prospective protocol freezing*, not formal preregistration [17].

An independently reviewable release should freeze environments and hashes; preserve model identifiers, prompts, rendering parameters, fold assignments, and OOF vectors; and include a de-identified data dictionary, model card, intended/prohibited-use table, and claim-evidence ledger. Decision traces can be more sensitive than ordinary outcome tables because they may contain identities, internal discussions, contested reasons, and policy interpretations. Prospective capture therefore requires purpose limitation, data minimization, role-based access, tiered retention, disclosure review, and correction/appeal mechanisms. No IRB or non-human-subject determination was documented in the reconstructed record; prospective reviewer/operator research requires one before initiation.

AI systems assisted extraction, coding, historical reconstruction, software development, and drafting. They cannot be authors or bear accountability. Human authors must verify every analysis, disclose assistance under journal policy, and assume responsibility for all claims.

## 10. Conclusion

Outcome data are not necessarily decision data. Historical regulatory archives can make a model accurate for the wrong question without preserving the state, action, rules, and reasons that justified the original disposition. In this study, an early high score reproduced a circular label, a case-level model ranked historical shortfall rather than reasonable-effort adequacy, and final-state routing sent known depth-related refusals toward a fast lane. The appropriate response was neither unconstrained feature expansion nor LMM-generated rationales. It was to recover source-linked fragments, expose what remained unidentifiable, separate evidence, time, construct, generalization, and authority, and let failures remove permissions.

The resulting prototype is an evidence, attention-allocation, and prospective trace-production system—not an approval system. It can produce candidate fields and preliminary labels, but current software does not yet enforce a complete trace ledger. Under the proposed architecture, LMM services would propose source-linked candidates; Model A would suggest who should be reviewed first; Model B would suggest which historical ruler to use; rules would expose explicit issues; a qualified reviewer would accept evidence and retain responsibility; and a versioned ledger would preserve rules, revisions, reasons, and overrides. The principal contribution is a reproducible discipline: first determine whether the decision trace can support the question, then determine what the model is entitled to do.

## References

1. Pennsylvania Department of Environmental Protection. Oil and Gas Forms. Accessed 11 July 2026.
2. Pennsylvania Department of Environmental Protection. Oil and Gas Reports and Data. Accessed 11 July 2026.
3. Pennsylvania Code. 25 Pa. Code §78.1, Definitions: attainable bottom. https://www.pacodeandbulletin.gov/display/pacode?d=reduce&file=%2Fsecure%2Fpacode%2Fdata%2F025%2Fchapter78%2FsubchapAtoc.html. Accessed 12 July 2026.
4. Pennsylvania Environmental Quality Board. Rulemaking petition concerning attainable-bottom determinations. Pennsylvania Bulletin. 2025.
5. Commonwealth of Pennsylvania. Artificial Intelligence Policy. 2026.
6. Kim G, Hong T, Yim M, et al. OCR-free document understanding transformer. ECCV. 2022.
7. Ma Z, et al. Large language model extraction of information from historical well records. Scientific Reports. 2024;14.
8. Lakkaraju H, Kleinberg J, Leskovec J, Ludwig J, Mullainathan S. The selective labels problem. KDD. 2017.
9. Roberts DR, Bahn V, Ciuti S, et al. Cross-validation strategies for structured data. Ecography. 2017;40:913–929.
10. Rudin C. Stop explaining black-box machine-learning models for high-stakes decisions and use interpretable models instead. Nature Machine Intelligence. 2019;1:206–215.
11. National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework 1.0. 2023.
12. Gebru T, Morgenstern J, Vecchione B, et al. Datasheets for datasets. Communications of the ACM. 2021;64:86–92.
13. Mitchell M, Wu S, Zaldivar A, et al. Model cards for model reporting. FAT*. 2019.
14. Collins GS, Dhiman P, Andaur Navarro CL, et al. TRIPOD+AI statement. BMJ. 2024;385:e078378.
15. Sambasivan N, Kapania S, Highfill P, Akrong D, Paritosh P, Aroyo LM. Data cascades in high-stakes AI. CHI. 2021.
16. Pineau J, Vincent-Lamarre P, Sinha K, et al. Improving reproducibility in machine learning research. JMLR. 2021;22:1–20.
17. Hofman JM, et al. Pre-registration for predictive modeling. arXiv:2311.18807. 2023.
18. Pedregosa F, Varoquaux G, Gramfort A, et al. Scikit-learn: machine learning in Python. JMLR. 2011;12:2825–2830.
19. Friedman JH. Greedy function approximation: a gradient boosting machine. Annals of Statistics. 2001;29:1189–1232.
20. Singh J, Cobbe J, Norval C. Decision provenance: harnessing data flow for accountable systems. IEEE Access. 2019;7:6562–6574. doi:10.1109/ACCESS.2018.2887201.
21. van der Aalst WMP, Adriansyah A, de Medeiros AKA, et al. Process Mining Manifesto. In: Business Process Management Workshops. Lecture Notes in Business Information Processing. 2012;99:169–194. doi:10.1007/978-3-642-28108-2_19.
