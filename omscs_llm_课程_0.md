# 入职前沿大模型厂或顶级 AI lab 的学习路线图与 syllabus

我会把目标定义成一句话：

**你不是在准备“懂大模型”，而是在准备成为一个能在前沿团队里独立发现问题、写出可靠代码、设计实验、理解系统瓶颈、并把想法推进到结果的人。**

上面架构综述的核心是：2026 年的大模型竞争已经从单纯扩大参数，转向长上下文、KV cache、稀疏注意力、MoE、推理系统、后训练、Agent 和评测体系的整体竞争。附件中的求职经验也指向同一个结论：顶级 lab 面试不只看论文经历，技术知识和技术实现能力会被非常高频地考察；她总结的面试类型包括 ML coding、普通 coding、技术讨论、研究讨论、行为面、数学和 job talk，其中 ML coding 是最常见的一类，并且 PyTorch 熟练度几乎是硬要求。

下面给你一套 **24 周主线 syllabus**。全职准备可以按 6 个月执行；在职或在读可以拉长到 9 到 12 个月。

## 1. 目标岗位画像

你可以把前沿大模型厂的岗位分成四类，学习路线不同，但底层能力重叠。

## 1.1 Research Scientist

核心要求是提出新想法、判断问题是否重要、设计长期研究议程、做出可规模化的结果。OpenAI 对 Research Scientist 的描述强调“提出新想法或改进已有想法”，并能自主选择有影响力的问题、推进长期项目。([OpenAI][1])

你需要证明三件事：

1. 你能提出一个清晰的 research bet。
2. 你能把实验做严谨，而不是只跑 benchmark。
3. 你能解释为什么这个方向在 scale 后仍然成立。

适合主攻方向：架构、后训练、推理、数据、评测、Agent、可解释性、安全。

## 1.2 Research Engineer

核心要求是把想法变成能跑、能扩、能复现、能被团队依赖的系统。OpenAI 对 Research Engineer 的描述明确提到大规模分布式机器学习系统、无明显缺陷的机器学习代码，以及构建算法背后的科学。([OpenAI][2])

你需要证明三件事：

1. 你能写深度学习代码，而且知道每一行 tensor shape。
2. 你理解训练和推理系统瓶颈。
3. 你能在复杂工程中调试性能、数值稳定性和分布式问题。

适合主攻方向：训练系统、推理服务、GPU kernel、数据管线、评测基础设施、Agent sandbox。

## 1.3 Applied Research 或 Post Training

核心要求是把模型能力变成可验证的产品能力。你需要懂 SFT、DPO、PPO、GRPO、reward model、数据合成、评测、红队、工具调用、Agent 轨迹。

OpenAI 当前公开岗位中有 RL 与 reasoning、post training、retrieval、frontier evals、agents、alignment、interpretability 等方向，说明顶级 lab 的岗位已经明显细分到“训练前、训练中、训练后、评测、安全、Agent、检索、实时模型”等链路。([OpenAI][3])

## 1.4 Early career 或 Residency

如果你还没有强论文或工业经历，路线不是“等背景变强”，而是做出强 artifact。OpenAI Emerging Talent 面向 0 到 3 年经验人群，覆盖研究、应用工程和产品方向；Residency 则面向已经在探索 AI 或来自数学、物理、神经科学等相关领域的人，强调真实研究经验、导师制和自驱构建能力。([OpenAI][4]) ([OpenAI][5])

你的目标应是：用项目、复现、技术博客、开源贡献和推荐人，弥补传统履历不足。

# 2. 总体学习策略

附件作者的经验非常有参考价值：她面试了 11 家公司，经历 57 场 interview，另有 46 次 recruiter call 和 16 次 offer 后沟通；这说明顶级岗位求职不是一次考试，而是一场持续几个月的项目管理。

你的准备要同时推进五条线：

1. **基础线**：数学、PyTorch、普通 coding、深度学习基本功。
2. **大模型线**：tokenizer、Transformer、训练、推理、长上下文、MoE、后训练。
3. **系统线**：分布式训练、KV cache、FlashAttention、Triton、vLLM、量化、服务吞吐。
4. **研究线**：读论文、复现、提出假设、做 ablation、写报告。
5. **求职线**：networking、面试、job talk、行为面、谈 offer。

附件作者还特别强调：Stanford CS336 帮她把零散概念组织成完整图景，Homework 1 中实现和调试 Transformer 非常关键，而且练习 coding 时要关闭 AI 辅助，避免低估自己对工具的依赖。 Stanford CS336 2026 官方课程也说明，它会从数据收集清洗、预训练、Transformer 构建、训练到部署前评测，带学生完整走过语言模型开发流程。([Stanford CS336][6])

# 3. 24 周 syllabus

## 第 1 到 4 周：基本功与 Transformer 肌肉记忆

目标：不再“看懂 Transformer”，而是能从零实现、训练、调试一个小语言模型。

## 第 1 周：数学与 PyTorch 基础

主题：

1. 线性代数：矩阵乘法、特征值、SVD、范数、低秩近似。
2. 概率：MLE、cross entropy、KL divergence、采样、温度。
3. 微积分：链式法则、softmax 梯度、LayerNorm 梯度。
4. PyTorch：autograd、nn.Module、Dataset、DataLoader、mixed precision、torch.compile 基础。

实作：

1. 只用 numpy 写线性回归、softmax 回归、两层 MLP。
2. 手推并实现 cross entropy backward。
3. 用 PyTorch 写一个极小字符级语言模型。
4. 记录每个 tensor 的 shape，并写 shape assert。

面试训练：

1. 每天 1 道普通 coding。
2. 每天 1 道 ML coding 小题，例如 softmax、cross entropy、LayerNorm、Adam。

验收标准：

1. 你能在白板上推导 softmax 加 cross entropy 的梯度。
2. 你能解释 autograd 在何处省事，也能在没有 autograd 时写 backward。
3. 你能在 30 分钟内写出一个可训练 MLP。

## 第 2 周：Tokenizer 与数据管线

主题：

1. BPE、unigram、sentencepiece 思想。
2. tokenization 对 multilingual、代码、数学、长上下文的影响。
3. 数据清洗、去重、质量过滤、污染检测。
4. packing、attention mask、label shift、样本边界。

实作：

1. 从零写一个 BPE tokenizer。
2. 训练一个小 tokenizer，并比较字符级、BPE、现成 tokenizer 的长度差异。
3. 写 causal LM 数据集，支持 packing 和不 packing 两种模式。
4. 人为制造 packing 边界泄漏 bug，并写测试抓出来。

面试训练：

1. 实现 top p sampling、top k sampling、temperature sampling。
2. 解释为什么 tokenizer 是一个研究方向，而不只是预处理工具。附件作者也提到自己最后两年的 tokenization 专长帮助她在求职中形成了可识别的研究主线。

验收标准：

1. 你能解释 tokenizer 如何影响训练效率、稀有词、代码补全和数学推理。
2. 你能 debug label shift 和 padding mask 问题。
3. 你能写出一页 tokenizer 技术说明。

## 第 3 周：从零实现 GPT 类模型

主题：

1. token embedding、position embedding、causal mask。
2. MHA、MLP、残差、归一化。
3. Pre Norm 与 Post Norm。
4. RoPE、RMSNorm、SwiGLU。
5. AdamW、learning rate schedule、gradient clipping、weight decay。

实作：

1. 从零写一个小 GPT。
2. 加入 RoPE、RMSNorm、SwiGLU。
3. 训练在小 corpus 上收敛。
4. 画 loss curve、梯度范数、activation 统计。

面试训练：

1. 现场实现 masked attention。
2. 现场实现 RoPE。
3. 现场解释为什么 RMSNorm 比 LayerNorm 更轻。
4. 现场解释 Pre Norm 为什么更利于深层训练。

验收标准：

1. 你能从空文件写出一个可训练 Transformer。
2. 你能解释每个模块的计算复杂度和显存占用。
3. 你能定位训练 loss 不下降的 10 种常见原因。

## 第 4 周：生成、KV cache 与调试

主题：

1. greedy、beam、top k、top p、temperature。
2. prefill 与 decode 的区别。
3. KV cache 的 shape 和显存公式。
4. MQA、GQA、MLA 的动机。
5. 单元测试、数值误差、profile。

实作：

1. 为第 3 周模型加入 KV cache。
2. 比较有无 KV cache 的 decode 速度。
3. 加入 MQA 和 GQA。
4. 写一个 profile 报告：prefill 时间、decode 时间、显存、吞吐。

面试训练：

1. 给定 batch、layer、head、seq length、head dim，估算 KV cache 显存。
2. 解释为什么长上下文 decode 常受显存带宽限制。
3. 解释 MHA、MQA、GQA 的质量与速度 tradeoff。

验收标准：

1. 你能在 10 分钟内画出推理流程图。
2. 你能解释为什么百万 token 上下文不是简单把 context window 调大。
3. 你的代码有测试，有 README，有复现实验命令。

# 4. 第 5 到 8 周：2026 架构主线

目标：把上面的大模型架构综述变成可实现、可比较、可讨论的能力。

前面附件中的架构截图把 2025 到 2026 的核心矛盾概括为长上下文成本，并把注意力路线分成线性压缩、滑窗截断、稀疏压缩等几派；另一个截图也列出了 RoPE、RMSNorm、SwiGLU、GQA、MoE 等 2024 年前后的常见底盘。 

## 第 5 周：现代 Transformer 底盘

主题：

1. RoPE 与位置外推。
2. RMSNorm 与归一化效率。
3. SwiGLU 与 FFN 参数效率。
4. MQA、GQA、MLA。
5. partial RoPE、attention sink、sliding window mask。

实作：

1. 在自己的 GPT 中加入 GQA。
2. 写 RoPE 外推实验。
3. 比较 MHA、MQA、GQA 的显存和速度。
4. 写一篇短报告：为什么 2024 底盘会收敛到这些组件。

验收标准：

1. 你能解释 RoPE 为什么适合相对位置。
2. 你能解释 GQA 为什么是 MHA 与 MQA 的折中。
3. 你能在面试中说清每个组件的取舍。

## 第 6 周：长上下文三派

主题：

1. 线性递归压缩：Gated DeltaNet、Mamba 类状态空间思想。
2. 滑窗加全局：SWA 与周期性 global attention。
3. 稀疏压缩：indexer、Top K 历史选择、compressed KV。
4. 长上下文评测：needle、RULER、LongBench、代码仓库级任务。
5. packing 边界、状态重置、长程召回失败模式。

现实参照：

Qwen3.5 9B 模型卡显示其 32 层中使用 8 组 “3 层 Gated DeltaNet 加 1 层 Gated Attention” 的混合布局，这正是线性递归与全注意力混合的代表。([Hugging Face][7]) MiMo V2 Flash 采用 SWA 与 global attention 交错结构，128 token 窗口，5 比 1 混合比例，并使用 MTP 做推理解码加速。([arXiv][8]) DeepSeek V4 则把 CSA 与 HCA 结合，用压缩稀疏注意力和重压缩注意力支持百万 token 上下文。([arXiv][9])

实作：

1. 实现 sliding window attention mask。
2. 实现 toy linear attention recurrent state。
3. 实现一个 toy sparse retrieval attention：先打分，再选 Top K，再 attention。
4. 对同一任务比较三种方法的速度、显存和准确率。

验收标准：

1. 你能解释三派的适用场景和失败模式。
2. 你能说清“压缩历史”和“截断历史”的区别。
3. 你能设计一个实验判断模型是否真正利用远距信息。

## 第 7 周：MoE 与稀疏参数

主题：

1. dense FFN 与 MoE 的区别。
2. router、Top K experts、capacity factor。
3. shared expert、routed expert、expert parallel。
4. 负载均衡、expert collapse、通信瓶颈。
5. MoE 与后训练稳定性。

现实参照：

GLM 5 公开资料显示其从 GLM 4.5 的 355B 总参数和 32B active 扩展到 744B 总参数和 40B active，并集成 DSA 以降低部署成本同时保留长上下文能力。([GitHub][10]) DeepSeek V4 报告显示 V4 Pro 为 1.6T 参数和 49B active，V4 Flash 为 284B 参数和 13B active，并结合 MoE、MTP、CSA、HCA、Muon 和 FP4 相关后训练基础设施。([arXiv][9])

实作：

1. 写一个 tiny MoE layer。
2. 实现 Top K router 和 load balancing loss。
3. 画出每个 expert 的 token 分布。
4. 人为制造 router collapse，并尝试修复。

验收标准：

1. 你能解释为什么 MoE 提高总参数但不等比例提高每 token FLOPs。
2. 你能解释 expert parallel 为什么会受通信影响。
3. 你能把 MoE 的训练问题讲成系统问题，而不是只讲公式。

## 第 8 周：推理系统与 GPU 视角

主题：

1. FlashAttention 的 IO aware 思想。
2. paged KV cache、prefix cache、continuous batching。
3. Triton 基础。
4. speculative decoding、MTP、draft model。
5. 量化：FP8、INT8、INT4、KV cache quantization。
6. 服务指标：TTFT、TPOT、tokens per second、吞吐、延迟、成本。

实作：

1. 用现成推理框架部署一个小模型。
2. 打开 continuous batching，测不同 batch 下吞吐。
3. 实现一个简化 speculative decoding。
4. 写一个 KV cache 管理实验，比较长上下文下的显存增长。

验收标准：

1. 你能解释 prefill 和 decode 的性能瓶颈。
2. 你能解释为什么 MTP 能加速，但接受率决定真实收益。
3. 你能读懂一个推理 profile，而不是只看最终速度。

# 5. 第 9 到 12 周：训练系统与 scaling

目标：从“会训练小模型”升级到“理解大规模训练为什么难”。

## 第 9 周：数据工程与预训练配方

主题：

1. 数据混合比例：网页、代码、数学、合成数据、多语言。
2. 去重、质量分类、污染检测。
3. curriculum、继续预训练、domain adaptive training。
4. tokenizer 与数据分布互动。
5. eval leakage 与 benchmark contamination。

实作：

1. 构建一个小型混合数据集。
2. 做质量过滤前后的 loss 与下游任务比较。
3. 对一个公开 benchmark 做污染检查思路设计。
4. 写数据卡：来源、过滤、风险、覆盖面。

验收标准：

1. 你能解释“数据质量”和“数据多样性”的冲突。
2. 你能设计数据 ablation。
3. 你能讨论合成数据的收益和风险。

## 第 10 周：分布式训练

主题：

1. DDP、FSDP、ZeRO。
2. tensor parallel、pipeline parallel、sequence parallel、context parallel、expert parallel。
3. 5D parallelism 的含义。
4. activation checkpointing、gradient accumulation。
5. 通信与计算重叠。

实作：

1. 用 DDP 训练第 3 周的小模型。
2. 用 FSDP 或 ZeRO 跑一次多 GPU 训练。
3. 分析通信时间和计算时间。
4. 写一页纸解释 5D parallelism。

面试训练：

技术讨论中常会出现“什么是 5D parallelism”“如何训练更长 context”“如何 debug 分布式 loss 不一致”等问题。附件作者也提到技术讨论可能是一个深入 topic，也可能是 rapid fire breadth check，例如位置编码、5D parallelism、PPO 与 GRPO 的区别。

验收标准：

1. 你能解释每种 parallelism 切的是什么维度。
2. 你能估算显存由哪些部分组成。
3. 你能说出 loss spike、NaN、deadlock 的排查路径。

## 第 11 周：训练稳定性与优化器

主题：

1. AdamW、Adafactor、Muon。
2. learning rate warmup、cosine decay、weight decay。
3. gradient clipping、loss scaling、BF16、FP8。
4. normalization、residual scaling、SwiGLU clamping。
5. checkpoint、resume、determinism。

实作：

1. 复现实验：改变 LR、batch size、warmup，看 loss。
2. 制造 NaN，并定位来源。
3. 比较 BF16 与 FP32。
4. 写一个训练稳定性 checklist。

验收标准：

1. 你能解释为什么大模型训练里 optimizer 是系统设计的一部分。
2. 你能解释 loss spike 的常见来源。
3. 你能写出训练事故复盘模板。

## 第 12 周：Scaling law 与实验设计

主题：

1. 参数、数据、算力的 scaling law。
2. ablation 与控制变量。
3. 小模型代理实验如何预测大模型。
4. 评测置信区间与统计显著性。
5. 成本估算和实验优先级。

实作：

1. 训练多个小模型，拟合 loss 与参数量、token 数的关系。
2. 设计一个“是否值得上大规模”的研究 proposal。
3. 写实验计划：hypothesis、metric、baseline、risk、stop criteria。

验收标准：

1. 你能解释为什么不是所有小模型结论都能 scale。
2. 你能设计实验预算。
3. 你能在研究讨论中被追问后仍然守住逻辑。

# 6. 第 13 到 16 周：后训练、RL、Agent 与安全

目标：理解今天模型能力的很大一部分来自后训练，而不只是预训练架构。

## 第 13 周：SFT、Preference、DPO

主题：

1. instruction tuning。
2. preference data。
3. reward model。
4. DPO、IPO、KTO 的直觉。
5. 数据质量、拒答、风格、格式遵循。

实作：

1. 对一个小模型做 LoRA SFT。
2. 构建 preference pair。
3. 实现 DPO loss。
4. 评测 helpfulness、format following、toxicity 或 refusal。

验收标准：

1. 你能解释 SFT 与 preference optimization 的区别。
2. 你能解释 DPO 为什么不需要显式 reward model。
3. 你能设计一个 preference 数据集质量检查流程。

## 第 14 周：PPO、GRPO 与推理模型

主题：

1. policy gradient。
2. PPO 的 clipping、KL penalty、value function。
3. GRPO 的 group relative 思想。
4. outcome reward 与 process reward。
5. reasoning token、test time scaling。
6. RL 训练中的 mode collapse、reward hacking、长度偏置。

实作：

1. 在简单数学任务上做 policy gradient toy experiment。
2. 实现一个简化 GRPO 或 PPO 训练环。
3. 比较不同 reward 对输出长度和正确率的影响。
4. 写一页“PPO vs GRPO”技术说明。

资源：

附件作者推荐的学习资源中包括 “Introduction to Policy Gradient for LMs” 和 GRPO 原理指南；OpenAI 面试指南也推荐 Deep Learning Book 和 Spinning Up in Deep RL 作为技术阅读材料。 ([OpenAI][11])

验收标准：

1. 你能推导 policy gradient。
2. 你能解释 PPO 与 GRPO 的核心差异。
3. 你能解释 reasoning model 的训练为什么更像系统工程。

## 第 15 周：评测、红队与安全

主题：

1. benchmark 设计。
2. contamination、overfitting、leaderboard gaming。
3. long context eval、agent eval、code eval。
4. robustness、misuse、privacy、jailbreak。
5. human eval 与自动 eval 的取舍。

实作：

1. 为一个 Agent 任务设计 eval harness。
2. 做 pass at k、exact match、LLM judge 三种评测对比。
3. 写一个红队 prompt set。
4. 写一份 eval report，包含失败样例和误差分析。

验收标准：

1. 你能解释为什么 eval 是研究的一部分。
2. 你能识别一个 benchmark 可能被污染的路径。
3. 你能在面试中设计 follow up experiment。

## 第 16 周：Agent、工具调用与长程任务

主题：

1. tool calling schema。
2. planner、executor、memory、reflection。
3. code agent、browser agent、search agent。
4. sandbox、trajectory logging、rollback、resume。
5. 长程任务的 credit assignment。

实作：

1. 写一个能调用 shell、搜索本地文档、编辑文件的 mini code agent。
2. 为它设计任务集和自动评测。
3. 加入轨迹记录和失败复盘。
4. 尝试用 SFT 或 preference 数据改进行为。

验收标准：

1. 你能解释为什么 Agent 不只是 prompt engineering。
2. 你能讨论工具调用失败、状态污染、长程规划崩溃。
3. 你有一个可展示的 Agent 项目。

# 7. 第 17 到 20 周：选择一个主攻方向，做出强 portfolio

目标：从“学过很多”变成“有一个别人愿意追问的方向”。

附件作者提到，建立一个明确专长帮助她在求职中脱颖而出；研究讨论准备时，也要能说清为什么选择这些问题、形成了什么 insight、未来方向是什么。 

你应选择下面一个主线项目。

## 方向 A：架构与长上下文

项目题目示例：

1. 比较 sliding window、linear attention、sparse retrieval attention 在长文档 QA 上的质量和成本。
2. 实现 toy MLA 或 compressed KV，并测 KV cache 降低幅度。
3. 对 RoPE 外推、partial RoPE、位置插值做系统实验。
4. 做一个 “1M context 成本估算器”。

最终产物：

1. GitHub repo。
2. 8 到 12 页技术报告。
3. 20 分钟 job talk。
4. 一篇中文或英文技术博客。

## 方向 B：推理系统

项目题目示例：

1. 在 vLLM 或 SGLang 上做长上下文推理 profile。
2. 实现简化 paged KV cache。
3. 实现 speculative decoding，并分析接受率。
4. 做 INT4 或 KV cache quantization 的质量与速度实验。

最终产物：

1. benchmark 脚本。
2. profile 可视化。
3. 成本模型。
4. 对一个开源项目提交 issue 或 PR。

## 方向 C：后训练与 reasoning

项目题目示例：

1. 在数学任务上比较 SFT、DPO、GRPO。
2. 构建 process reward 数据。
3. 做 thinking budget 与正确率曲线。
4. 分析 reward hacking 和长度偏置。

最终产物：

1. 训练代码。
2. 数据构建说明。
3. eval report。
4. 错误分析集。

## 方向 D：评测与 Agent

项目题目示例：

1. 设计一个代码仓库级 Agent benchmark。
2. 做 terminal task 的自动评分器。
3. 分析 LLM judge 和真实执行结果的偏差。
4. 做长程任务失败分类 taxonomy。

最终产物：

1. 可复现 eval harness。
2. 任务集。
3. 失败样例库。
4. 技术博客。

## 方向 E：数据与 tokenizer

项目题目示例：

1. 比较 tokenizer 对代码、数学、多语言、长文本的影响。
2. 做数据去重与污染检测工具。
3. 分析 synthetic data 在某一任务上的收益边界。
4. 训练一个 domain tokenizer，并测试压缩率和 downstream 效果。

最终产物：

1. 数据管线。
2. tokenizer 训练脚本。
3. contamination report。
4. 一页研究主张。

# 8. 第 21 到 24 周：面试系统训练

目标：把知识转换成面试表现。

OpenAI interview guide 明确说，面试会考察候选人的工作经历、动机、技能评估，可能包括 pair coding、家庭项目、技术测试，最后面试通常覆盖专业能力并把候选人推到舒适区之外；工程面会看设计质量、代码质量、性能和测试覆盖。([OpenAI][11]) 这与附件作者的经验高度一致。

## 第 21 周：ML coding 高频题

每天练 2 小时，关闭 AI 辅助。

题型清单：

1. 实现 softmax、cross entropy、LayerNorm、RMSNorm。
2. 实现 multi head attention。
3. 实现 causal mask、padding mask、sliding window mask。
4. 实现 RoPE。
5. 实现 KV cache decode。
6. 实现 beam search、top k、top p。
7. 实现 AdamW。
8. 实现 DPO loss。
9. 实现 tiny MoE router。
10. 实现 BPE merge。
11. 实现 logistic regression backward。
12. 实现 k means 或 PCA。

验收标准：

1. 每题 30 到 45 分钟内完成。
2. 有 shape assert。
3. 有简单测试。
4. 能边写边解释复杂度。

## 第 22 周：普通 coding 与数学

普通 coding：

1. LeetCode 75 或 Neetcode Blind 75。
2. 数组、哈希表、双指针、栈、队列、树、图、动态规划。
3. 每天 2 题，复盘错题模式。

数学：

1. 概率：贝叶斯、条件概率、期望、方差、常见分布。
2. 线代：投影、特征分解、SVD、低秩。
3. 优化：凸性、梯度下降、动量、二阶直觉。
4. 深度学习推导：softmax、attention、LayerNorm、policy gradient。

附件作者也建议复习概率、线性代数和微积分，因为部分公司会有数学面。

## 第 23 周：技术讨论与研究讨论

技术讨论题库：

1. 为什么标准 attention 在长上下文下贵。
2. prefill 和 decode 的瓶颈分别是什么。
3. MQA、GQA、MLA 的差异。
4. RoPE 如何外推。
5. sliding window attention 为什么会损失远程信息。
6. linear attention 为什么省 KV，但会损失可寻址历史。
7. sparse attention 的 indexer 如何训练。
8. MoE 为什么会 expert collapse。
9. 5D parallelism 如何组合。
10. PPO 和 GRPO 的区别。
11. 怎样设计一个数学 reasoning 的 RL 实验。
12. 怎样评测一个 code agent。
13. 怎样发现数据污染。
14. 为什么 benchmark 高不等于产品好。
15. 如何 debug 大模型训练 loss spike。

研究讨论准备：

1. 准备 3 分钟、7 分钟、15 分钟三个版本的 self pitch。
2. 准备一个主项目的深讲版本。
3. 准备三个失败实验，以及你从中学到什么。
4. 准备未来 6 个月、2 年、5 年的 research agenda。
5. 针对不同 lab 改写关键词，例如 architecture、reasoning、agent、alignment、inference、data。

附件作者提醒，研究讨论不只是讲过去项目，还要能解释为什么选择这些问题、形成了什么观点、未来什么方向有前景，并且要根据岗位调整 research pitch。

## 第 24 周：job talk、行为面、networking 与 offer

Job talk：

1. 15 到 20 分钟主讲一个方向。
2. 结构为：问题、为什么重要、已有方法、你的洞察、实验、失败、下一步。
3. 每 3 页就回答一次“为什么听众应该在意”。
4. 结尾给出 3 个你入职后可以推进的问题。

行为面：

准备 8 个故事：

1. 最困难的 debug。
2. 和合作者冲突。
3. 项目失败。
4. 你改变研究方向。
5. 你说服别人。
6. 你承认错误。
7. 你处理压力。
8. 你考虑 AI 安全或社会影响。

附件作者明确说，行为面需要提前把 PhD 或项目经历映射到常见问题，否则现场回忆会非常痛苦。

Networking：

1. 列 50 个联系人：同学、导师、合作者、会议认识的人、开源项目维护者、目标团队成员。
2. 每周联系 5 到 8 人。
3. 每次只问一个具体问题，例如“你们组现在最需要什么背景的人”。
4. 准备一页 PDF：你是谁、做过什么、主攻方向、代表项目、想找什么岗位。

Offer 与谈判：

附件作者提醒，收到 offer 后还会有大量 teammate、manager、recruiter 沟通；谈判不是可有可无，初始 offer 往往留有空间，需要朋友和市场数据帮助校准，并在 recruiter call 前写清楚什么能说、什么不能说。

# 9. 每周节奏建议

按全职准备计算：

1. 周一到周三：上午 coding，下午课程或论文，晚上复盘。
2. 周四：项目实现和实验。
3. 周五：写技术报告、画图、整理 README。
4. 周六：mock interview，一场 ML coding，一场技术讨论。
5. 周日：休息半天，复盘半天，制定下周计划。

时间比例：

1. 40% 写代码和做实验。
2. 25% 读课程和论文。
3. 15% 面试训练。
4. 10% 写作和 portfolio。
5. 10% networking 和岗位研究。

不要把全部时间花在读论文上。顶级 lab 更看重你能不能把想法变成结果。附件作者也说，技术面试所测试的技能需要在研究之外专门训练，而求职准备几乎像一份全职工作。

# 10. 最小 portfolio 标准

到第 24 周结束，你应该至少有这些东西：

1. 一个从零实现的小 GPT repo。
2. 一个长上下文或推理系统项目。
3. 一个后训练或 Agent 项目。
4. 一份 8 到 12 页研究报告。
5. 两篇技术博客。
6. 一个 15 到 20 分钟 job talk deck。
7. 一份面向 Research Engineer 的简历。
8. 一份面向 Research Scientist 的简历。
9. 一页 networking PDF。
10. 一个面试错题本。

其中最重要的是前 4 个。没有 artifact 的学习路线，容易变成“知识收集”；有 artifact，才会变成可被推荐、可被追问、可被雇佣的能力。

# 11. 你的阅读与资源清单

## 11.1 主课程

1. Stanford CS336：Language Modeling from Scratch。
   这是主线课程，优先级最高。官方介绍显示它覆盖数据、预训练、Transformer 构建、模型训练和部署前评测，与你的目标高度匹配。([Stanford CS336][6])

2. OpenAI interview guide。
   用于理解面试流程、技术评估、工程面关注点和准备材料。([OpenAI][11])

3. Deep Learning Book 与 Spinning Up in Deep RL。
   这两项也是 OpenAI 面试指南推荐的技术阅读。([OpenAI][11])

## 11.2 附件作者推荐资源

1. LeetCode 75 或 Neetcode Blind 75。
2. Stanford CS336。
3. Self Attention and Transformers。
4. The Illustrated GPT 2。
5. Backpropagation。
6. Introduction to Policy Gradient for LMs。
7. GRPO 与 RL 原理指南。
8. How to Scale Your Model。

## 11.3 论文主题清单

按顺序读，不要一次读完所有。

1. Transformer 原论文。
2. GPT 系列和 causal LM。
3. BPE 与 tokenizer。
4. RoPE、RMSNorm、SwiGLU。
5. MQA、GQA、MLA。
6. FlashAttention。
7. vLLM 与 paged attention。
8. Switch Transformer、DeepSeekMoE。
9. Qwen3.5 的 Gated DeltaNet 混合架构。
10. MiMo V2 的 SWA 与 MTP。
11. GLM 5 的 DSA。
12. DeepSeek V4 的 CSA 与 HCA。
13. DPO、PPO、GRPO。
14. Agent eval、code agent、long horizon task。
15. interpretability、alignment、red teaming。

# 12. 最终路线图

把它压缩成一句执行路线：

**前 4 周把 Transformer 写到肌肉记忆；第 5 到 8 周吃透 2026 架构主线；第 9 到 12 周理解训练与 scaling；第 13 到 16 周掌握后训练、RL、Agent 和 eval；第 17 到 20 周做出一个可展示的研究项目；第 21 到 24 周集中打磨面试、job talk、简历和推荐网络。**

你真正要建立的护城河不是“知道最新模型名字”，而是能回答这类问题：

1. 这个架构为什么解决了长上下文成本？
2. 它牺牲了什么能力？
3. 你会如何验证它？
4. 如果实验失败，你怎么定位？
5. 如果要把它放到真实服务里，瓶颈在哪里？
6. 如果给你 3 个月和一小组 GPU，你能推进什么？

能稳定回答这些问题，再加上扎实 coding、一个清晰主攻方向和可展示项目，你就已经非常接近前沿大模型厂或顶级 AI lab 的候选人画像。

[1]: https://openai.com/careers/research-scientist-san-francisco/ "Research Scientist | OpenAI"
[2]: https://openai.com/careers/research-engineer-san-francisco/ "Research Engineer | OpenAI"
[3]: https://openai.com/careers/search/ "Careers | OpenAI"
[4]: https://openai.com/careers/emerging-talent/ "OpenAI"
[5]: https://openai.com/residency/ "OpenAI Residency | OpenAI"
[6]: https://cs336.stanford.edu/ "Stanford CS336 | Language Modeling from Scratch"
[7]: https://huggingface.co/Qwen/Qwen3.5-9B?utm_source=chatgpt.com "Qwen/Qwen3.5-9B"
[8]: https://arxiv.org/abs/2601.02780?utm_source=chatgpt.com "MiMo-V2-Flash Technical Report"
[9]: https://arxiv.org/html/2606.19348v1 "DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence"
[10]: https://github.com/zai-org/GLM-5?utm_source=chatgpt.com "zai-org/GLM-5: GLM-5: From Vibe Coding to Agentic ..."
[11]: https://openai.com/interview-guide/ "OpenAI interview guide | OpenAI"
