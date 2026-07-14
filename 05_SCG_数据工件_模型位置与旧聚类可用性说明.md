# S/C/G 研究协议、数据工件、模型文件与旧聚类词表的可用性说明

> 版本：2026-07-12  
> 文档性质：论文与复现工作的技术补充说明  
> 仓库根目录：`D:\Dropbox\29. Ampelos\28_dep\final_06_11_2026\09_2026_pipline_ml_06_18\03_Final_Merge_06_26_codex`

## 0. 先给结论

本项目中的 S、C、G 不是三个并列的模型，也不是三个分数。它们分别控制三个不同层次的问题：

1. **S（Pre-Screens）回答“这是不是我们要研究的对象，且请求、决定和深度是否属于正确轨道？”**
2. **C（Checklist）回答“在申请包中，哪些决策相关证据被明确记录并且能够回到来源？”**
3. **G（Go/No-Go Gates）回答“这套分类与抽取仪器是否已经可靠到允许锁定、扩量或支持某类主张？”**

因此，最简洁而准确的表述是：

> **S 决定对象与轨道是否合格；C 逐案审计证据是否被记录；G 决定研究工具拥有什么权限。**

另有四个必须同时说明的事实：

- 最终锁定的历史研究 instrument 是 **v1.4 的 S1–S5 与 C1–C7**；当前 `17_agent` 运行的是另一个 **v1.5-DRAFT 的 CK1–CK4**。二者有继承关系，但并不相同。
- `633`、`10,856` 和 `436` 都来自 2026-06-26 的 v6 冻结口径；其中 `436` 特指 `evidence_guard_quarantine=1`，并不是所有带有 quarantine 标记的行数。
- 当前 agent 实际加载的两个传统 ML 文件位于 `17_agent\backend\artifacts\`：Model A 为 DN prescreen classifier，Model B 为 difficulty proxy regressor。
- 用户提供的 7 类障碍、9 种部署方式和 32 种工具，**可以帮助建立前瞻性的 decision-trace 受控词表**；但从所给代码片段本身只能确认词表，尚不能确认可复现的聚类结果。由于历史记录高度缺失，它们目前不应直接被加入 A/B 或用于判断 effort adequacy。

---

## 1. S、C、G 的总体架构

| 层 | 分析单位 | 核心问题 | 主要输入 | 主要输出 | 失败后的后果 |
|---|---|---|---|---|---|
| S | 单个 case/request/decision/depth track | 对象和轨道是否合格？ | 请求文书、可见勾选框、签字、深度原文、决定主题 | in/out、有效请求深度、被排除候选及理由 | 退出 refusal/effort-adequacy 路径；不能进入 positive pool |
| C | 单个申请包 | 请求时点有哪些可追溯证据？ | 带日期的申请文件、DN 叙述、佐证文书、深度、停止解释、TD | C1–C7 逐项结果及来源指针 | 缺证据即 absent/unknown；不允许模型补写事实 |
| G | 整个抽取 instrument 或研究模块 | 是否可靠到可以锁定、扩量或支持某项主张？ | 盲读、双读、回归负例、覆盖率、敏感性检验 | PASS、procedural lock、DEFERRED 或 BLOCKED | 按预先定义的权限后果停止扩量或关闭某类用途 |

这三个层次依次约束：

```text
原始档案
   ↓
S：对象、决定状态与深度轨道是否正确
   ↓
C：申请包证据是否存在、是否有来源、缺口是什么
   ↓
G：上述抽取是否足够可靠，能够扩量或支持特定研究主张
```

### 1.1 共同的 fail-closed 证据契约

历史 instrument 的重要性不只在于列出了字段，更在于它规定了证据权限。关键字段原则上需要：

- `source_file`：PDF 文件名；
- `page`：页码；
- `verbatim_quote`：原文，或对实际视觉状态的精确描述；
- 深度还必须带 `track tag`，例如 `operator_requested`、`dep_approved`、`certificate_achieved`、`anchor_td`、`plug_geometry`；
- 勾选框必须描述实际可见的 mark，不能因为页面上印有 “Denied” 就判为 denial；
- 日期必须出现在原文中或紧邻原文；推断日期不能满足需要日期的项目；
- 不能把一个文档里的数字与另一个文档里的标签静默拼接。

这意味着：**没有完整来源，不是“模型低置信度地猜一个值”，而是该项记为 absent/unknown。**

---

## 2. S：Pre-Screens 的完整内容与作用

S 在 checklist 之前运行。它的任务不是判断 operator 是否努力充分，而是阻止错误对象、错误决定状态和错误深度进入研究池。

### S1 — Request kind：请求类型是否属于研究范围

**检查内容**：当前有效请求是否为 plugging alternate-method、attainable-bottom 或 stopping-depth request。

**需要排除的对象**包括 inactive status/future utility、restoration report、transmittal/admin form、bonding、coal-owner notification、surface marker 等。

**作用**：避免把“行政文书”或“未来用途请求”误当成 attainable-bottom 决策。v1.4 允许 DEP 在请求文书上的正式 routing annotation（例如手写 “ALT METHOD”）作为 S1 证据，但仍需来源指针。

### S2 — Decision-box visual state：实际哪个决定框被标记

**检查内容**：逐个 decision-capable document 读取真正可见的 mark，而不是读取印刷标签。

最终词表包括：

- `approved_marked`
- `approved_signature_line`
- `denied_marked`
- `reviewed_by_marked`
- `notice_acknowledged`
- `conditions_yes_marked`
- `conditions_no_marked`
- `disapproved_with_comments_marked`
- `approved_transmittal_marked`
- `no_box_marked`
- `form_has_no_decision_box`

**作用**：解决本项目最重要的视觉误读之一——“Reviewed” 不是 denial，空的 “Denied” 框不是 denial，签在 Approved-by line 上也不等于有一个单独的 Approved checkbox 被勾选。

### S3 — Denied versus approved-plus-conditions：批准条件不能被误读为拒绝

**检查内容**：YES/NO 是否位于 “Conditions” 标题之下，以及是否存在 Approved-by 签字。

- `Conditions = NO` + 已签字的 `Approved by` = **无附加条件的批准**；
- `Conditions = YES` + attachment = **附条件批准**；
- 标准 total-depth condition boilerplate 本身不等于 refusal。

**作用**：防止将 “Approved + Conditions: NO” 误判为 denied，也防止把标准批准条件重新包装为 effort-adequacy refusal。

### S4 — Depth-track validity：请求深度是否真的是 operator 的停止深度

**检查内容**：typed depth 是否为 operator 明确提出的 stopping/attainable-bottom value。

应排除：

- floor-clause minimum；
- 法规编号误解析成深度；
- casing cut/shoot depth；
- plug-placement line；
- TD/TMD/LTD 或 “TD or attainable bottom” 的定性 anchor；
- 内部冲突的请求叙述；
- 来自 DEP-approved 或 certificate 字段的数字。

最终保留的结构是：

```text
valid_requested_value_exists: true/false
valid_value_ft: number, if true
rejected_candidates: [{value, reject_reason, pointer}]
```

**关键澄清**：后来退役的是 `rejected` versus `no_typed_value` 这个不稳定的 emission token，**不是退役整个 S4**。S4 的核心二元判断与被拒绝候选仍由 G11 管理。

### S5 — Same request subject matching：前后决定是否针对同一请求

**检查内容**：任何 denial → approval pair 是否针对同一个 stopping-depth request。

例如：

- inactive-status denial 后来出现 plugging approval，不是同一 pair；
- plugging approval 后来出现 restoration rejection，也不是同一 pair；
- 日期顺序与请求主题都必须匹配。

**作用**：防止只因同一井的文件夹中先后出现 “denied” 和 “approved”，就虚构一个监管方改变 attainable-bottom 决定的过程。

---

## 3. C：C1–C7 Checklist 的完整内容与作用

C 的研究对象是 **request package documentation**。它回答“请求时点的档案里记录了什么”，而不是“井下客观上还能不能更深”，也不是法律意义上的 effort adequacy 终局判断。

### 一个重要版本更正

早期 C3 定义为 `pre-request dated effort item`。G6 的随机 denominator 审计得到 0/15，扩展重编码仍接近零方差，说明历史档案无法稳定支持这个字段。因此 v1.3 起，C3 被正式改为 **documented non-routine difficulty（DN）**；最终 v1.4 的 C3 不再要求必须发生在 request 之前，timing 只作为 provenance。

因此，论文或复现文档若把最终 C3 继续写成“请求前有无 dated effort”，将混淆已经退役的旧构念与最终锁定 instrument。

### C1 — Request document identified

**内容**：识别当前 campaign 最早的、带日期的请求文件。

**作用**：建立 request-time cutoff。没有带日期的请求文书就 fail-closed，无法可靠进入后续 Tier 路由。

### C2 — Request target classified

**内容**：把请求目标分为：

- `numeric`
- `qualitative`
- `unclassifiable`

numeric 必须通过 S4。Plug placement、TD anchor 等不能冒充 requested bottom。

**作用**：C2 是 routing field，不是“通过/失败”分数。它决定后续比较能否使用数值 shortfall，还是只能进入定性证据路径。

### C3 — Documented non-routine difficulty（DN）

**内容**：当前 campaign/operator 是否记录至少一个非例行井下困难、障碍或复杂事件。pre-request、post-request 或 undated 都可，但 timing 必须保留。

可能包括：

- junk/fish/lost or stuck tools；
- parted/dropped string；
- lost circulation 或需要补救的循环失败；
- casing collapse、parted casing 或 unable-to-enter；
- 需要非例行 cleanout/milling 的 bridge/fill；
- unable-to-reach planned depth、caving 或 forced shallow stop；
- failed plugging attempt 或 plug did not hold；
- tagged fill/bridge 显著高于预期 TD；
- 因实际遭遇条件而被迫偏离标准方案。

排除 routine work、未来/条件式计划、没有遭遇事件的 bare alternate-method request、单纯 formation-characteristic rationale、prior-era/surface condition。仅凭旧 records、belief 或 inference 也不计 DN，除非同时有当前 campaign 的 attempt-and-failed evidence。

**作用**：C3 记录的是项目定义下的 documented difficulty，不是 effort adequacy，也不是客观工程难度真值。

### C4 — Corroborated difficulty

**内容**：C3 的 DN 是否得到更强文书佐证。最终 level 必须记录为整数：

1. operator asserted；
2. dated daily report；
3. service record 或完成的 dated form；
4. DEP inspected/witnessed。

**作用**：把“operator 自述”与“被独立记录或见证的事件”分开。叙述中说“另有报告”但报告未附上，不能算 corroborated。

### C5 — Depth evidence

**内容**：operator-side observed deepest reached/tagged/max/obstruction depth，包含 number、track 与 source。

排除 TD、tubing/pipe length、DEP-approved bottom、certificate bottom、plug geometry。

**作用**：建立“实际到达/遇阻在哪里”的可核验证据，避免用批准值或结局值替代申请时点观察。

### C6 — Stopping explanation

**内容**：operator 是否在 request package 中实质解释为什么 proposed bottom 是 attainable bottom。

模板语句如 “cement from total depth or attainable bottom to surface” 只能记 `template_only`；certificate 或其他 outcome document 不能补写请求时点原因。

**作用**：保存“为什么停在这里”的最小 decision trace。

### C7 — TD anchor

**内容**：numeric TD anchor，优先使用 drillers/original TD，并保留来源。

**作用**：为 v2 residual、shortfall 或同层比较提供参照；它不是 pass/fail item，也不能被当成 requested bottom 或 C5 reached depth。

---

## 4. G：G1–G11 的作用、指标与生命周期

G 是项目级 gate，不会在每个前端提交时给某个 case 打一个 G 分数。它规定某个抽取模块能否锁定、能否扩量，以及某类结论是否仍然有权被使用。

### 4.1 为什么必须区分三个时间点

1. **2026-07-03 草案**：`DRAFT / NOT LOCKED`，635-scale HOLD，G9 BLOCKED。
2. **2026-07-05 锁定版**：大部分 extraction gates 已由盲读结果锁定，但文件仍明确写着 635-scale 需要单独授权。
3. **随后状态**：635-case single pass 后来获得授权并完成；这不改变 G9 最终仍被 BLOCKED 的事实。

因此，“7 月 3 日时 635-scale 仍 HOLD”是正确的历史叙述，但不能被写成当前从未完成 635 抽取。

### 4.2 G1–G11 当前可报告状态

| Gate | 管什么 | 锁定或后续结果 | 对权限的含义 |
|---|---|---|---|
| G1 | C2 request-type 三分类 | 18/18 agreement，0 bad routing，LOCKED-PASS | numeric/qualitative/unclassifiable 路由可用于该 instrument |
| G2 | S1 request-kind in/out | in/out 17/18 = 94.4%，LOCKED-PASS | 可排除明显错误请求类型，但仍须保留来源 |
| G3 | requested/approved/certificate depth-track 分离 | 58 次盲编码中 0 contamination，LOCKED-PASS | 不允许把结果轨道偷渡为请求轨道 |
| G4 | certificate/achieved-depth coverage | procedural lock；后续 635 抽取的相关 424 案中仅 41/424 = 9.7% | 这是覆盖短板，不是可用缺失值；需要重定 scope 并报告 |
| G5 | TD-anchor availability | procedural lock；后续约 359/424 = 84.7% | TD 比 certificate depth 可得性高，但仍非全覆盖 |
| G6 | C3=DN 与 C4 recoverability | C3 17/18 + 6/6；v1.4 adjudicated FP=0；C4 level 5/5，LOCKED-PASS | 采用 DN；旧 pre-request effort item 因近零方差而废弃 |
| G7 | `later_deeper_evidence_class` typing | DEFERRED，绑定 G9 | pair-built rates 在 G7/G9 解锁前不能恢复权限 |
| G8 | C1–C7 checklist extraction precision | C1 18/18；C2 18/18；C3 17/18+6/6；C4 5/5；C5 18/18、value 9/9；C6 18/18；C7 18/18、value 19/20；LOCKED-PASS | 支持内部 instrument 的规模抽取，不等于外部专家效用验证 |
| G9 | uncensored-set ranking | 后续主对比 7/13 vs 105/411，OR 3.40、nominal p=.0477；cluster-collapsed p=.136、taint-excluded p=.291，BLOCKED | 不能据此恢复 retrospective routing、approval/refusal 或 adverse anomaly 权限 |
| G10 | checkbox-state determination | v1.4 S2 6/6、S3 10/10，LOCKED-PASS | 视觉状态必须由实际 mark 与版面关系决定 |
| G11 | S4 requested-track validity | binary 24/24，0 invalid value admitted；不稳定 token 退役，LOCKED-PASS | S4 核心有效值判断保留 |

G9 尤其重要：主比较的 nominal p-value 不能覆盖预先要求的敏感性检验失败。正确写法是 **G9 remains blocked**，而不是“主分析显著，所以 routing 已验证”。

---

## 5. 历史 S/C/G 与当前 agent 的 CK1–CK4 不是同一套东西

当前运行文件：

`17_agent\backend\app\scoring\checklist.py`

该文件明确标注为 `v1.5-DRAFT`。运行时 checklist 是：

| Runtime item | 当前代码的判断 | 与历史 instrument 的关系 |
|---|---|---|
| CK1 | 是否声明 alternate-method request form | 来源于 C1 的产品化简化，但不等于完整 dated-document identification |
| CK2 | 有 attempt_failed + 日期 + 足够描述并有 evidence/file，或 substantive causal reason | 组合了 R-DN-tense 与 C6 的操作化，不等于完整 C3/C4 双层证据审计 |
| CK3 | 同时有 max reached 与 obstruction/tag depth | 来源于 C5 教训的数值完整性要求 |
| CK4 | 最新 depth measurement 不超过 90 天，且 deterioration 不能晚于测量；否则 re-tag | v1.5 新增的 decision-time timeliness rule，不是历史 C1–C7 中的独立项目 |

当前代码还自带两个警告：

- thresholds 仍为 `v1.5-DRAFT`；
- presence-style bar 在历史 approved cases 中约会使 55% fail，仍需 pilot calibration。

因此：

- 不能写“前端每次提交都完整运行 S1–S5、C1–C7、G1–G11”；
- G 是离线的研究/验证 authority gate，不是在线 case score；
- 当前 CK1–CK4 主要读取 structured intake 字段，尚不能声称完整继承了历史 instrument 的 file + page + quote pointer contract；
- S/C/G 证明的是研究纪律与内部抽取可靠性，当前 agent 仍是待前瞻验证的 prototype。

---

## 6. 633、10,856 与 436 到底在哪里

### 6.1 权威位置与精确口径

| 数字 | 权威文件 | 精确定义 | 复算结果 |
|---|---|---|---|
| 633 | `06_processed_tables_final\case_level_v6.csv` | v6 案例级表的行数与唯一 `case_id` 数 | 633 rows，633 unique case IDs |
| 10,856 | `06_processed_tables_final\depth_evidence_v6.csv` | v6 深度证据表全部行 | 10,856 rows，涉及 552 个 case IDs |
| 436 | 同一个 `depth_evidence_v6.csv` | `evidence_guard_quarantine == 1` 的确定性 evidence-guard 隔离行 | 436 rows，涉及 181 个 cases |

用于复现锁定文件版本的 SHA256 为：`case_level_v6.csv` = `DC703A56A194F6FC142C002D6FB4C386B83BEC869198584A7BA45B825624559B`；`depth_evidence_v6.csv` = `F595ADE988766CFA05E004A1B03286B51E20F8B61CFBBC81E5F0464AC6A0C3BF`。

对应的 QA 文件：

- `07_qa_metrics_regressions\v6_final_after_remove_filter_qa_summary_2026-06-26.csv`
- `07_qa_metrics_regressions\depth_evidence_guard_summary_final_2026-06-26.csv`
- `00_documentation_and_manifest\case_scope_summary_635_vs_632.csv`

`436` **不是一个单独的 CSV 文件**；它是 `depth_evidence_v6.csv` 中由 `evidence_guard_quarantine` 标记出来的子集。

### 6.2 为什么不能把 436 泛称为“全部 quarantine 记录”

同一张深度表里有三种不同语义的标记：

- `quarantine_depth == 1`：5,971 行；
- `depth_numeric_quarantine == 1`：282 行；
- `evidence_guard_quarantine == 1`：436 行。

这些标记有重叠，不能直接相加。论文中与当前图表相对应的准确措辞应是：

> **10,856 depth-evidence rows, of which 436 were excluded by the deterministic evidence guard.**

不宜写成“10,856 行中一共只有 436 行属于任何形式的 quarantine”。

### 6.3 为什么同时会看到 635、633、632 和 656

这四个数字代表不同分析对象：

- **635**：自包含原始 PDF-backed case folders；
- **633**：`case_level_v6.csv` 的唯一案级记录；
- **632**：remove-filter 后的 eligible QA scope；633 表中多出的一案为 `125-28121`；
- **656**：后续 canonical `+21 legacy` 并合后的表格规模，不是原始 PDF case 数。

因此，不能把 “633 unique case-level rows” 改写成 “633 个原始案卷”，也不能把 656 当成多模态原始 PDF 文件夹数。

### 6.4 从原始数据到三个数字的文件链

#### 原始 PDF 档案

`03_raw_inputs_635_cases\raw_case_folders_joined_any_635\<case_id>\`

当前实测包括：

- 635 个 case directories；
- 约 1,700 份 PDF；
- 每案可包含 `_documents-manifest.json` 与 `_well-info.json`；
- 总文件数约 3,332。

#### Legacy 与 v5 输入

`03_raw_inputs_635_cases\legacy_and_v5_inputs\`

关键文件包括：

- `LegacyABWells_923.xlsx`
- `case_level_v5.csv`
- `event_level_v5.csv`
- `depth_evidence_v5.csv`
- `v5_exception_report.csv`

#### OCR 与 provenance

`04_provenance_and_ocr\`

关键文件包括：

- `raw_ocr_pages_v6.jsonl`：8,566 页级 OCR rows；
- `raw_ocr_combined_v6\`：635 个组合文本；
- `provenance_case_ledger.csv`；
- `provenance_document_ledger.csv`。

OCR 的作用是候选定位与审计缓存；扫描图像、勾选框、签字和版面关系仍需回到 PDF/page image。

#### 多模态模型的原始响应

`05_openai_batch_and_model_outputs\v6_extraction_results_openai\`

该目录中包括：

- 633 个 `api_response_*.json`；
- 1,845 个 `chunk_response_*.json`；
- batch input/output/state 与上传缓存。

#### 派生 PDF chunks

`08_generated_pdf_chunks\pdf_chunks_v6\`

这是为了批处理生成的派生分块，不是原始档案的替代品。

#### 处理代码

`01_code_v6_pipeline\`

主要链路是：

- `merge_v6_chunks.py`：合并 chunk-level response；
- `flatten_v6.py`：扁平化、关联 provenance、应用 guard、写出案例/事件/深度表；
- `depth_numeric_guard.py`：数值一致性防护；
- `depth_evidence_guard.py`：证据轨道防护并生成 `evidence_guard_quarantine`；
- `blocker_depth_selection.py`：选择控制性 obstruction candidate。

#### 最终 v6 表

`06_processed_tables_final\`

- `case_level_v6.csv`：633 rows；
- `event_level_v6.csv`：3,421 events；
- `depth_evidence_v6.csv`：10,856 rows；
- `_feature_manifest_v6.json`：特征、quarantine 与用途边界。

### 6.5 一个复现注意事项

复制到当前仓库的 `01_code_v6_pipeline\config_v6.py` 仍保留部分旧上游绝对路径；那些旧路径在当前自包含仓库中并不存在。论文与复现说明应把 `03_raw_inputs_635_cases\` 作为当前权威输入位置。若未来重跑 pipeline，需要显式重定配置，但本次文档工作没有修改任何代码。

---

## 7. 两个传统 ML 模型保存在哪里

### Model A — DN prescreen HGB classifier

**模型文件**：

`17_agent\backend\artifacts\dn_prescreen_form.joblib`

- 文件大小：205,058 bytes；
- SHA256：`597B94758A9DC278D61C8381B27C504214F37C7D779F6D01FA09D61AF711CB71`；
- 训练集：n=424，DN positive=112；
- 官方内部指标：AUC 0.8366 ± 0.1097；
- 权限：只用于 review queue ordering，不批准、不拒绝、不判断 effort adequacy。

### Model B — Difficulty proxy HGB regressor

**模型文件**：

`17_agent\backend\artifacts\difficulty_proxy_form.joblib`

- 文件大小：208,747 bytes；
- SHA256：`1E62AEB59E30423481F5FFD2A14F3E6848211C7E9D44FC9193236D30A060F219`；
- 目标：复现 locked historical shortfall/difficulty ensemble teacher；
- 官方内部指标：Spearman 0.418 ± 0.047；
- 权限：选择 teacher-defined difficulty reference bin，进而参与 tail reference；不代表客观难度真值，也不终裁。

### 配套文件

- 模型卡：`17_agent\backend\artifacts\model_card.json`
- 训练与保存：`17_agent\backend\train_form_models.py`
- 运行时加载：`17_agent\backend\app\scoring\ml.py`
- A/B 训练主表：`06_processed_tables_final\case_level_canonical_plus_checklist_2026-07-06.csv`
- Model B teacher OOF：`16_claude_Fable_5\artifacts\difficulty_ensemble_oof.csv`
- Model B 参照表：`17_agent\backend\artifacts\anomaly_reference_table.json`

两个模型共享 17 个 request-time-compatible fields，但**不包含**用户这次列出的具体障碍类别、部署方式或 32 个具体工具。换言之，旧聚类词表目前不会改变 A/B 的输出，除非重新定义特征、重训并重新验证。

### 不要与另一个研究模型混淆

仓库中还有：

`16_claude_Fable_5\artifacts\635_extraction\DN_triage_model_2026-07-06.joblib`

这是 108-feature 的研究版 DN triage model，不是当前 agent 在线加载的 Model A 文件。当前运行时加载的是上面列出的两个 form models。

---

## 8. 旧聚类/词表是否能帮助当前结果

### 8.1 先界定：目前能确认的是“词表”，还不是可复现的聚类结果

用户提供了三组 JavaScript arrays：

- 7 个 `obstructionClasses`；
- 9 个 `deploymentMethods`；
- 32 个 `allTools`。

但仅从这些数组，无法恢复以下信息：

- 聚类使用了什么样本和特征；
- 距离函数、算法和超参数；
- 每个 case/event 的 cluster assignment；
- 簇稳定性、silhouette 或其他内部指标；
- 专家是否确认每个簇的语义；
- 这些簇对外部 holdout、Model A 或 Model B 是否改善。

在当前仓库的文本和代码中也未定位到这些 exact uppercase class constants 的定义及对应簇成员。因此，在论文里最稳妥的称呼是：

> **an earlier candidate taxonomy / controlled vocabulary derived from exploratory clustering work**

若未来找到原始 cluster assignments、notebook 和验证结果，可以再升级为“previous clustering results”。

### 8.2 与当前 obstruction taxonomy 的对应关系

当前 `event_level_v6.csv` 的 `obstruction_type` 分布为：

| 当前值 | events |
|---|---:|
| unknown | 3,216 |
| formation_collapse | 93 |
| casing_issues | 40 |
| stuck_equipment | 22 |
| debris_fill | 13 |
| other | 11 |
| hole_integrity | 8 |
| junk_fish | 7 |
| cement_related | 6 |
| fluid_pressure | 5 |

即 3,421 个事件中约 94% 为 `unknown`。用户的 7 类可以作为更高层 parent ontology，但目前存在非一一对应：

| 旧候选类别 | 可对应的当前值 | 必须解决的歧义 |
|---|---|---|
| CASING_ISSUES | `casing_issues` | casing failure 与 hole integrity 是否允许多标签 |
| CEMENT_RELATED | `cement_related` | routine cementing 与 failed cement/plug event 必须分开 |
| DEBRIS_AND_FOREIGN_OBJECTS | `debris_fill`、部分 `junk_fish` | fish/lost tool 也可能属于 equipment problem |
| EQUIPMENT_PROBLEMS | `stuck_equipment`、部分 `junk_fish` | 工具本身故障、工具被卡、井下 foreign object 不是同一机制 |
| FLUID_AND_FLOW_ISSUES | `fluid_pressure` | lost circulation、failure to circulate、pressure 应保留子类型 |
| FORMATION_AND_BOTTOM_ISSUES | `formation_collapse`、部分 hard fill | 与 hole collapse 类别明显重叠 |
| HOLE_INTEGRITY_AND_COLLAPSE | `hole_integrity`、部分 `formation_collapse` | 若强制单标签，会把同一事件任意分到两个父类之一 |

**建议**：不要把 7 类做成互斥单标签。更稳妥的是两层、多标签结构：

```text
parent mechanism class
    + observed condition/detail
    + unknown / not documented / other
```

这样既可以保留历史 v6 的细粒度词，又不会因为 `FORMATION_AND_BOTTOM_ISSUES` 与 `HOLE_INTEGRITY_AND_COLLAPSE` 的重叠而强迫编码者作无依据选择。

### 8.3 与当前 deployment method 的对应关系

当前全部 3,421 events 的 `deployment_method` 是：

| 当前值 | events |
|---|---:|
| unknown | 3,216 |
| workover_rig | 64 |
| other | 57 |
| wireline | 49 |
| pump | 26 |
| cable_tool | 7 |
| rotary | 2 |

用户旧词表中的 `Cable Tool` 和 `Wireline` 可以直接建立规范化映射；其余需要审慎处理：

- `Service Rig`、`Pulling Rig` 可能映射到 `workover_rig`，但必须由原文和工程规则确认；
- `Drilling Rig` 可能接近 `rotary` 或另一个 rig family，不能自动等同；
- `Power Swivel` 更像工具/设备，不宜与 rig/deployment platform 混在同一维度；
- `Double Pole`、`Single Pole`、`Dozer Rig` 在当前规范词表中没有直接对应；
- 当前的 `pump`、`rotary`、`workover_rig` 也没有被旧词表完整覆盖。

因此，旧列表很适合作为前端 dropdown 的起点，但必须增加：

- `unknown`；
- `not documented`；
- `other + free text`；
- 当前规范中的 `workover_rig`、`pump`、`rotary`；
- 受版本控制的 synonym/crosswalk table。

历史记录中 deployment method 约 93% unknown，不能通过把 unknown 批量映射到最常见类别来“补齐”数据。

### 8.4 32 个工具列表的价值与边界

在 424-case 建模 cohort 中：

- 共有 2,874 个事件；
- 只有 197 个事件含任何 `tools_used` 记录，即 6.9%；
- 93.15% 的事件没有 tool token；
- 197 个事件中出现 169 个不同 raw tokens，包含同义词、粒度差异、通用词和 OCR 噪声；
- 高频 raw tokens 包括 `wireline` 43、`tubing` 40、`tools` 31、`wireline unit` 27、`CIBP` 20、`CBL` 18、`CBL/CCL` 15、`power swivel` 9。

用户的 32 项列表包含不少高价值工具，如 CCL、CBL、Power Swivel、Bailer、Mill、Overshot、Spear 等，但也存在三个问题：

1. 它没有覆盖当前高频的所有 raw forms，例如 `CBL/CCL`、`wireline unit`、`CIBP`、`sandline`、`cutter`；
2. 同一概念可能有多种拼写、复合写法和 OCR 变体；
3. “工具没有被记录”不能解释为“该工具没有被使用”。

因此，这个列表当前最适合作为：

- 规范化 dictionary；
- synonym expansion 的种子；
- intake 的受控多选项；
- reviewer 检索历史原文的 query vocabulary；
- prospective decision-trace 数据的字段定义。

它暂时不适合作为：

- effort adequacy score；
- “使用工具越多越努力”的简单计数；
- 对历史 missing values 的自动填补；
- A/B 的直接新特征；
- 自动 adverse routing 或 approval/refusal 的依据。

---

## 9. 这些旧词表现在具体能帮什么

### 9.1 对论文主张的帮助

它们最直接支持的不是“我们已经用工具聚类提高了 accuracy”，而是更重要的主张：

> 历史档案有结果和零散叙述，却没有稳定保存结构化的 obstruction–method–tool–attempt–outcome 链。旧词表为前瞻性采集这条 decision trace 提供了可操作的 ontology 起点。

历史数据中 obstruction 约 94% unknown、deployment 约 93% unknown、工具记录只覆盖约 6.9% 的事件，反而构成了“为什么不能从结果态数据库直接恢复努力过程”的量化证据。

### 9.2 对 S/C/G 的帮助

- **对 S**：帮助规范事件和深度属于哪个机制，但不能替代 S1–S5 的对象、决定状态和深度轨验证。
- **对 C3/C4**：若某个 obstruction、deployment 或 tool attempt 带日期、原文和佐证，可帮助记录 DN 及 corroboration；仅有工具名称不能让 C3/C4 自动通过。
- **对 C6**：可以把“为什么停止”从自由文本拆为机制 + 具体叙述，但模板勾选仍不能替代实质说明。
- **对 G**：可以新增 ontology coverage、双读一致性、跨 operator/template 稳定性等 gate；在这些 gate 通过之前，不应扩大其模型权限。

### 9.3 对 Model A 的潜在帮助

Model A 预测的是项目定义下的 DN ranking。稳定、request-time、source-backed 的 obstruction/tool-attempt 记录未来可能改善：

- DN candidate retrieval；
- queue ordering；
- reviewer 对分数原因的理解；
- subgroup error analysis。

但这只能通过前瞻数据和 county/operator/time/template holdout 验证。当前历史自动 flags 高度稀疏，先前 108-feature 研究模型中大量细粒度特征的 permutation importance 约为零；因此不能假设把 32 个工具 one-hot 后 AUC 就会提高。

### 9.4 对 Model B 的潜在帮助

Model B 的作用是选择 teacher-defined historical reference bin。稳定记录的 encountered obstruction 与 deployment context，未来可能帮助“选择哪一组案例更可比”。但必须满足：

- 信息在 request time 已可得；
- 不能使用 certificate/final outcome 反推；
- 类别有足够覆盖率；
- 不把 operator 选择的工具误当成地质难度本身；
- proxy-conditioned tail calibration 经独立 holdout 验证。

在此之前，这些词表只能作为 reviewer context，不能作为客观 difficulty truth。

### 9.5 对当前 agent 的帮助

当前前端可以收集 struggle/remedy 等结构化内容，但相关细粒度面板尚未作为 A/B 输入。旧词表最合理的近期用途是改善数据采集，而不是立即改变评分：

1. operator 选择规范类别，同时保留 raw free text；
2. 每个选择必须绑定 date、depth、purpose、result 与 source；
3. reviewer 明确接受或驳回抽取字段；
4. 积累真实 request-time prospective dataset；
5. 再决定是否重训 A/B。

---

## 10. 建议把三组旧词表升级为 decision-trace schema

建议未来每一次井下尝试保存为一个事件，而不是只在 case 表上保存几个 yes/no flags：

| 字段 | 说明 |
|---|---|
| `attempt_id` | 一次具体尝试的唯一编号 |
| `campaign`、`event_date` | 区分当前 campaign、历史事件和请求前后时点 |
| `objective` | 这次尝试要达到什么目的 |
| `deployment_method_raw/canonical` | 原文与规范部署方式并存 |
| `tools_raw/canonical[]` | 原始工具提及与规范多选并存 |
| `obstruction_parent[]` | 7 类 parent ontology，可多标签 |
| `obstruction_detail[]` | 保留 formation collapse、junk/fish、stuck equipment 等细节 |
| `attempted_depth_ft` | 尝试目标深度，明确 track |
| `max_reached_ft` | 实际到达深度，明确 track |
| `obstruction_ft` | 遇阻位置，明确 track |
| `result` | succeeded / partial / failed / unknown |
| `failure_reason` | 实质因果叙述，不以模板勾选代替 |
| `source_file/page/quote` | 可回放证据 |
| `reviewer_acceptance` | 人类 reviewer 接受、修改或拒绝字段 |
| `missingness_state` | unknown / not documented / not applicable，三者分开 |

这个结构能把“用了什么工具”“遇到什么障碍”“为何没有继续”“监管方在什么信息状态下作出决定”连成一条可回放的链。它比简单增加几十个 one-hot feature 更符合本论文的 decision-trace 主线。

---

## 11. 若要让旧词表进入模型，建议的验证顺序

1. **冻结 ontology 与 crosswalk**：明确 parent、detail、synonym、unknown、other 和多标签规则。
2. **盲法双人编码**：在 source-stratified 样本上验证 obstruction、deployment、tools 的 present-call 与具体值一致性。
3. **来源核验**：每个正值必须回到 file/page/quote；不得从结果态 certificate 静默补入 request-time feature。
4. **缺失机制审计**：区分未发生、未记录、未抽取和不适用。
5. **覆盖与漂移检验**：按 county、operator、time、template/source type 检查分布。
6. **冻结后再做增量建模**：在相同 grouped CV/外部 holdout 下比较原 A/B 与新增词表模型，报告增量性能、校准、queue utility 与 subgroup errors。
7. **前瞻性人机实验**：验证 reviewer time、field acceptance、纠错率和 adverse routing 风险，而不只报告 AUC 或 Spearman。

在第 1–5 步之前，这些词表可以服务于采集、检索、审计和描述性分析；在第 6–7 步之前，不应获得自动路由或审批权限。

---

## 12. 最终判断

### 可以立即采用

- 把 7 类 obstruction 作为候选 parent ontology，但采用多标签并保留细粒度 detail；
- 把 9 种 deployment methods 作为 dropdown 起点，同时补入当前规范类别、unknown/not documented/other；
- 把 32 个 tools 作为 synonym dictionary 和前瞻 intake 多选项；
- 将三组词表嵌入 source-linked attempt event，支持 decision-trace 采集；
- 用它们做 reviewer 检索、描述性统计和误差审计。

### 暂时不能采用

- 不能把这些数组本身称为已经验证的聚类结果；
- 不能据此填补历史 unknown；
- 不能把工具数量解释为 effort adequacy；
- 不能把障碍类别解释为因果难度真值；
- 不能在不重训、不做 grouped/external validation 的情况下声称它们改善 A/B；
- 不能据此恢复 G9 已关闭的 retrospective routing 或 approval/refusal 权限。

最符合本项目证据的总结是：

> **这些旧词表目前最大的价值，不是作为更多模型特征，而是作为未来保存 decision traces 的结构化语言。历史档案中的缺失率说明它们尚不能可靠地重建过去的 effort adequacy；前瞻性 intake、来源绑定和人类接受机制，则可以使它们成为下一阶段真正可验证的数据资产。**

---

## 13. 主要本地证据索引

- S/C 权威 schema：`16_claude_Fable_5\artifacts\v1_checklist_schema_2026-07-03.json`
- G 历史草案：`16_claude_Fable_5\artifacts\go_no_go_gates_v2_DRAFT_2026-07-03.md`
- G 锁定版：`16_claude_Fable_5\artifacts\go_no_go_gates_v2_LOCKED_2026-07-05.md`
- 项目后续状态：`16_claude_Fable_5\artifacts\SUMMARY.md`
- 当前 runtime checklist：`17_agent\backend\app\scoring\checklist.py`
- v6 数据范围核验：`00_documentation_and_manifest\case_scope_summary_635_vs_632.csv`
- v6 QA：`07_qa_metrics_regressions\v6_final_after_remove_filter_qa_summary_2026-06-26.csv`
- 数据全景地图：`DATA_MAP_2026-07-07.md`
- A/B 模型卡：`17_agent\backend\artifacts\model_card.json`
- efforts/tools 统计：`16_claude_Fable_5\publication\efforts_and_tools_distributon\computed_stats.json`
- 字段与稀疏性说明：`16_claude_Fable_5\publication\efforts_and_tools_distributon\FACTS_ML输入元素与efforts_tools分布.md`
