# 重新规划后的学习路线

我核对了两门课的官方页面。Stanford CS336 2026 版是一条完整的工程主线，五个 assignment 依次覆盖：

1. 从零实现 tokenizer、Transformer 和 optimizer
2. GPU profiling、Triton、FlashAttention2 和分布式训练
3. Scaling law
4. Common Crawl 数据清洗、过滤和去重
5. SFT、Reasoning RL，以及可选的 DPO 安全对齐

这门课明确要求很强的 Python、PyTorch、GPU 与 memory hierarchy 基础，而且代码量远高于普通 AI 课程。([Stanford CS336][1])

Georgia Tech CS 8803 LLM 则更像一张 2026 年前沿研究地图，覆盖 pretraining、embedding、MoE、reasoning、DPO、Agent harness、long context、MLA、GRPO、DAPO、self play、test time scaling、linear Transformer、diffusion LM、safety、mechanistic interpretability、calibration 和 scaling law。([CocoXu][2])

因此，新的路线不应该是“先学完 Stanford，再读 Georgia Tech”，也不应该机械照抄 Georgia Tech 的日历顺序。最合理的结构是：

> **以 Stanford CS336 作为纵向实现主干，以 Georgia Tech CS 8803 作为横向论文和研究扩展。**

Stanford 决定你先实现什么，Georgia Tech 决定你在实现之后继续追问什么。

---

# 一、相比原来的 24 周路线，应该修改什么

## 1. 从 24 周扩展到 32 周

你现在是全职 Senior AI Developer，不是全职学生。CS336 本身就是 Stanford 5 unit 的高强度实现课，官方强调 minimal scaffolding、代码量大、需要 GPU 系统优化经验。把 A1 到 A5、前沿论文、项目和面试全部压入 24 周，容易出现每个模块都“接触过”，但没有一个模块能在面试中独立实现。([Stanford CS336][1])

我建议采用：

**32 周，每周 14 到 16 小时。**

其中：

1. 每周 7 小时实现
2. 每周 3 小时课程和论文
3. 每周 2 小时 ML coding
4. 每周 1 小时技术写作
5. 每周 1 到 3 小时实验、复盘或 networking

高峰期，例如 FlashAttention2、分布式训练和 RLVR，可以增加到每周 18 小时。

## 2. 不再单独花四周复习普通 ML 基础

以你的 PhD、Georgia Tech OMSCS、统计和机器学习研究背景，没有必要重新完整学习线性代数、概率论、普通深度学习。

新的处理方式是：

1. 数学变成每周一次 interview refresh
2. PyTorch 基础只保留两周诊断和补缺
3. 更多时间放在 tensor shape、GPU memory、distributed training、Triton、KV cache 和 RL training loop

你的短板不是“是否知道梯度下降”，而是能否在没有模板和 AI 辅助的情况下，实现并调试一个语言模型训练系统。

## 3. 把 Stanford A1 和 A2 设为绝对核心

前一份求职经验中，作者明确指出 ML coding 是出现频率最高的面试类型，PyTorch 熟练度几乎是必需品；技术讨论则可能直接问位置编码、5D parallelism、PPO 与 GRPO。

她还特别强调，CS336 Homework 1 的 Transformer 实现与 debugging 应该练到肌肉记忆，并且练习时要关闭 AI assistance。

所以新的优先级是：

1. A1 必须完整完成
2. A2 必须至少完成核心部分
3. A3 到 A5 可以控制实验规模，但不能只看讲义
4. Georgia Tech 论文不能取代实现

## 4. 不平均学习 Georgia Tech 的所有主题

Georgia Tech 的 syllabus 很新，但它包含多个彼此独立的职业方向：

1. Foundation model architecture
2. Post Training 和 reasoning
3. Agent training
4. Embedding 和 retrieval
5. Safety
6. Mechanistic interpretability
7. Diffusion LM
8. Calibration

这些不应该全部成为你的主攻方向。

对你而言，最合适的组合是：

**主方向：训练与推理系统、长上下文和 Agent infrastructure**

**副方向：Post Training、RLVR 和 reasoning evaluation**

Embedding、mechanistic interpretability、diffusion LM 和专门的 safety research 保留为理解层面的选修，除非申请对应团队。

## 5. 面试准备从第一周开始，而不是最后四周才开始

课程能力和面试能力并不完全相同。前一份求职记录指出，技术知识和实现能力往往比研究经历更频繁地受到直接考察，研究经历更像是获得面试机会的入口。

所以每周都要保留：

1. 一道普通 coding
2. 一道 ML coding
3. 一个五分钟技术解释
4. 每两周一次无 AI 的 closed book implementation

---

# 二、32 周详细 syllabus

# 第一阶段：准备与能力诊断

## 第 1 周：PyTorch、einops 与 tensor reasoning

### 学习内容

1. Tensor shape 追踪
2. Broadcasting
3. einsum 和 einops
4. autograd graph
5. contiguous、view、reshape、transpose
6. parameter、buffer 和 optimizer state
7. PyTorch module、hook 和 state dict
8. 单元测试与 numerical tolerance

### 实现任务

1. 只用 PyTorch tensor operation 实现 linear layer
2. 实现 softmax
3. 实现 cross entropy
4. 实现 LayerNorm
5. 实现 RMSNorm
6. 手写一个两层 MLP
7. 为每个模块写 forward correctness test
8. 用 finite difference 检查一个 backward

### 面试任务

在关闭 AI 的环境下，四十五分钟内完成：

1. softmax
2. cross entropy
3. RMSNorm
4. top k sampling

### 验收标准

你应该能解释：

1. 每个 tensor 的 shape
2. 哪些 operation 会复制内存
3. 哪些 operation 只创建 view
4. autograd 保存了哪些中间结果
5. 为什么 activation 会占用大量训练显存

---

## 第 2 周：FLOPs、memory 与 arithmetic intensity

这是新版 CS336 在 Transformer 之前就加入的关键内容。课程把 FLOPs、memory 和 arithmetic intensity 放在第二讲，说明 2026 年理解模型不能只停留在数学结构，还要从硬件成本理解每个 operation。([Stanford CS336][1])

### 学习内容

1. FLOPs 估算
2. 参数显存
3. gradient 显存
4. optimizer state 显存
5. activation 显存
6. HBM 与片上 memory
7. arithmetic intensity
8. compute bound 与 memory bound
9. prefill 与 decode 的初步区别

### 实现任务

为一个 decoder model 写 resource estimator，输入：

1. 层数
2. hidden dimension
3. FFN dimension
4. attention heads
5. KV heads
6. context length
7. batch size
8. data type

输出：

1. 参数量
2. 每 token FLOPs
3. 训练 FLOPs
4. 参数显存
5. KV cache 显存
6. optimizer state 显存

### 面试任务

口头估算：

1. 为什么 FFN 经常占主要训练 FLOPs
2. 为什么 decode 可能 memory bound
3. 为什么 GQA 能降低 KV cache
4. context 从 32K 增长到 1M 时哪些成本线性增长，哪些成本平方增长

---

# 第二阶段：CS336 Assignment 1

## 第 3 周：Tokenizer 与文本表示

### Stanford 主线

1. Unicode
2. byte representation
3. BPE
4. vocabulary
5. special token
6. encode 与 decode
7. tokenizer training

### Georgia Tech 扩展

精读：

1. Parity Aware Byte Pair Encoding

略读：

1. Chameleon 中涉及 token 和 data mixture 的部分

### 实现任务

1. 从零实现 byte level BPE
2. 实现 vocabulary training
3. 实现 encode
4. 实现 decode
5. 支持 special token
6. 测试 Unicode round trip
7. 比较英文、中文、代码和数学文本的 compression ratio

### 研究问题

1. tokenizer 是否对不同语言产生不公平的 token 成本
2. vocabulary 增大如何影响 embedding 参数量
3. tokenizer 如何影响训练 FLOPs
4. byte fallback 如何影响罕见词和多语言能力

### 输出

一份两页 tokenizer report，包含：

1. compression ratio
2. multilingual disparity
3. vocabulary size tradeoff
4. failure examples

---

## 第 4 周：数据加载、packing 与 causal training

### 学习内容

1. document boundary
2. sequence packing
3. causal mask
4. padding mask
5. shifted label
6. EOS 处理
7. random sampling
8. deterministic data loading
9. train validation split

### 实现任务

1. 实现 language modeling dataset
2. 实现不 packing 的 batch
3. 实现 packing 的 batch
4. 实现 shifted label
5. 实现 causal attention mask
6. 检查跨样本信息泄漏
7. 检查最后一个 token 的 label
8. 固定随机种子后复现 batch

### 必须主动制造的 bug

1. label shift 错一位
2. EOS 丢失
3. padding token 进入 loss
4. packing 后跨 document attention
5. validation 数据泄漏进入 training

你应该为这些 bug 写自动测试，而不是依赖肉眼观察 loss。

---

## 第 5 周：标准 Transformer

### 学习内容

1. token embedding
2. causal self attention
3. MHA
4. residual connection
5. normalization
6. position representation
7. FFN
8. weight tying
9. initialization

### 实现顺序

第一步先按照 assignment 的标准结构实现。

第二步再加入现代变体：

1. RMSNorm
2. RoPE
3. SwiGLU
4. GQA

这样你才能回答：

1. 原始结构是什么
2. 现代结构改变了什么
3. 为什么改变
4. 对参数、FLOPs 和 KV cache 有什么影响

### 单元测试

1. attention 与 naive reference 对齐
2. causal mask 正确
3. RoPE shape 正确
4. GQA repeat 或 grouped computation 正确
5. 单个 batch 可以 overfit
6. dropout 训练和评估行为不同

---

## 第 6 周：Optimizer、training loop 与 generation

### 学习内容

1. AdamW
2. weight decay
3. warmup
4. cosine decay
5. gradient clipping
6. mixed precision
7. checkpoint
8. resume
9. greedy decoding
10. temperature
11. top k
12. top p

### 实现任务

1. 从零实现 AdamW
2. 实现 learning rate scheduler
3. 实现 gradient norm logging
4. 实现 checkpoint save
5. 实现 checkpoint resume
6. 实现 deterministic evaluation
7. 实现 KV cache 之前的 naive generation
8. 实现 sampling

### 训练监控

至少记录：

1. training loss
2. validation loss
3. learning rate
4. gradient norm
5. tokens per second
6. peak memory
7. parameter update norm

---

## 第 7 周：训练最小模型与闭卷重写

### 完成内容

1. 训练一个 minimal language model
2. 进行至少三个 ablation
3. 记录训练成本
4. 做 error analysis
5. 整理 README 和运行命令

### 建议的 ablation

1. LayerNorm 对比 RMSNorm
2. GELU 对比 SwiGLU
3. absolute position 对比 RoPE
4. MHA 对比 GQA
5. 不同 learning rate
6. 不同 context length

### 闭卷考试

关闭 Copilot、Cursor 和 ChatGPT，从空文件完成：

1. RMSNorm
2. RoPE
3. causal multi head attention
4. SwiGLU
5. sampling loop

目标不是完整训练，而是测试你能否在九十分钟内写出正确的核心模块。

Stanford 官方也明确鼓励在 assignment 中关闭 AI autocomplete，避免失去对代码和概念的深度参与。([Stanford CS336][1])

---

# 第三阶段：CS336 Assignment 2

这是整个路线中最重要、也最可能填补你当前能力缺口的阶段。

## 第 8 周：GPU 架构与 profiling

### 学习内容

1. GPU SM
2. warp
3. block
4. global memory
5. shared memory
6. register
7. memory coalescing
8. kernel launch overhead
9. occupancy
10. roofline model

### 实现任务

1. 使用 PyTorch profiler 分析训练 step
2. 区分 forward、backward 和 optimizer 时间
3. 分析 attention 和 FFN 时间
4. 测量不同 sequence length
5. 测量不同 batch size
6. 测量 BF16 与 FP32
7. 画 FLOPs、latency 和 memory 曲线

### 输出

一份 performance diagnosis：

1. 当前瓶颈是什么
2. 是 compute bound 还是 memory bound
3. 哪个 kernel 最贵
4. 增大 batch 后为什么变化
5. context length 增长后为什么变化

---

## 第 9 周：Triton 基础

### 实现任务

依次实现：

1. vector addition
2. fused activation
3. row wise softmax
4. matrix multiplication
5. RMSNorm kernel

### 必须理解

1. program id
2. block size
3. mask
4. load 与 store
5. shared memory 思想
6. autotune
7. numerical precision
8. backward kernel

### 验收标准

每个 Triton kernel 都必须有：

1. correctness test
2. performance benchmark
3. 不同 shape 测试
4. 与 PyTorch baseline 的比较
5. 边界 shape 测试

---

## 第 10 周：FlashAttention2

### 学习重点

1. 标准 attention 为什么需要大量 HBM 读写
2. online softmax
3. tiling
4. blockwise Q、K、V
5. causal masking
6. numerical stability
7. backward recomputation

### 实现任务

按照 CS336 A2 的要求，实现所需的 FlashAttention2 路径。

至少测试：

1. causal 与 noncausal
2. 不同 head dimension
3. 不同 sequence length
4. 不同 batch size
5. forward correctness
6. backward correctness
7. peak memory
8. runtime

### 面试问题

1. FlashAttention 是否改变 attention 的数学结果
2. 为什么它能降低 memory IO
3. 为什么它不消除全注意力的理论平方计算
4. 为什么不同 sequence length 下加速比不同

---

## 第 11 周：分布式训练与内存优化

### 学习内容

1. data parallel
2. DDP
3. tensor parallel
4. pipeline parallel
5. sequence parallel
6. context parallel
7. expert parallel
8. FSDP
9. ZeRO
10. activation checkpointing
11. gradient accumulation
12. communication computation overlap

### 实现任务

1. 将 A1 模型改造成 DDP
2. 尝试 FSDP 或等价 sharding
3. 加入 activation checkpointing
4. 测量不同 world size
5. 测量 scaling efficiency
6. 检查不同 rank 的 loss 一致性
7. 测试 checkpoint 恢复

### 你必须能够解释的 5D parallelism

一个常见的五维组合是：

1. data parallel
2. tensor parallel
3. pipeline parallel
4. context 或 sequence parallel
5. expert parallel

重点不是背名称，而是说明：

1. 每个维度切分什么
2. 产生什么通信
3. 节省什么显存
4. 什么时候值得使用

---

## 第 12 周：Mixture of Experts

### Stanford 主线

1. router
2. expert
3. token dispatch
4. capacity
5. load balancing
6. communication

### Georgia Tech 精读

1. Outrageously Large Neural Networks
2. DeepSeek V2 中与 MLA 和 MoE 有关的指定部分

### Georgia Tech 略读

1. Your Mixture of Experts LLM Is Secretly an Embedding Model for Free

### 实现任务

1. 实现 tiny MoE FFN
2. 实现 Top K routing
3. 实现 shared expert
4. 实现 routed expert
5. 记录 expert utilization
6. 人为制造 expert collapse
7. 尝试 auxiliary loss 或其他平衡方法
8. 测量 MoE 的通信与计算成本

### 面试问题

1. 总参数和 active 参数有什么区别
2. MoE 为什么能提高容量但不等比例提高每 token FLOPs
3. expert parallel 为什么可能受 all to all 通信限制
4. router collapse 如何出现
5. shared expert 解决什么问题

---

## 第 13 周：现代 attention 与长上下文

这是连接前面“2026 Transformer 架构综述”和课程实现的关键一周。

### Georgia Tech 重点阅读

1. Efficient Streaming Language Models with Attention Sinks
2. DeepSeek V3.2 指定架构部分
3. TransMLA
4. Linear Transformers Are Secretly Fast Weight Programmers
5. Parallelizing Linear Transformers with the Delta Rule

### 实现三个 toy variant

1. Sliding Window Attention
2. recurrent linear attention state
3. Top K sparse retrieval attention

### 比较维度

1. training FLOPs
2. prefill latency
3. decode latency
4. KV memory
5. long range retrieval
6. local dependency
7. state reset
8. packing boundary

### 你应该形成的架构观点

1. 全注意力保留精确历史，但成本高
2. 滑窗截断大部分历史，依靠层间传播和少量全局层
3. 线性注意力把历史压入固定状态
4. 稀疏注意力保留可寻址历史，但依赖 indexer 或 selection quality
5. 真实模型往往混合多种机制，而不是纯粹采用单一路线

---

## 第 14 周：Inference system

### 学习内容

1. prefill
2. decode
3. KV cache
4. continuous batching
5. PagedAttention
6. prefix caching
7. speculative decoding
8. MTP
9. TTFT
10. TPOT
11. throughput
12. tail latency

### 实现任务

1. 为 A1 模型加入 KV cache
2. 实现 GQA KV cache
3. 比较 naive decode 和 cached decode
4. 实现简化 continuous batching simulator
5. 实现简化 speculative decoding
6. 记录 acceptance rate
7. 测量长 context 下的 memory growth

### A2 最终输出

一份系统报告，至少包含：

1. PyTorch baseline
2. Triton 或 FlashAttention2 结果
3. distributed training 结果
4. attention variant 结果
5. inference benchmark
6. cost and limitation discussion

---

# 第四阶段：CS336 Assignment 3

## 第 15 周：Scaling law 基础

### 学习内容

1. parameter scaling
2. data scaling
3. compute scaling
4. power law
5. undertraining
6. overtraining
7. compute optimal allocation
8. loss prediction

### Georgia Tech 精读

1. Training Compute Optimal Large Language Models

### 实现任务

1. 收集多个模型规模的训练结果
2. 改变参数量
3. 改变训练 token 数
4. 拟合 power law
5. 估计固定 compute 下的最优参数与数据规模
6. 给出不确定性和 residual analysis

---

## 第 16 周：Precision scaling

### Georgia Tech 精读

1. Scaling Laws for Precision

### 学习问题

1. 低精度如何改变训练吞吐
2. precision 降低何时损失质量
3. 参数、activation、gradient、optimizer state 是否应采用相同 precision
4. FP8、FP4、INT8 和 INT4 分别适合哪些阶段
5. KV cache quantization 如何影响推理

### 实现任务

做一个小规模 precision experiment：

1. FP32
2. BF16
3. 可行时加入一种更低精度方案
4. 比较 loss、throughput、memory 和稳定性

---

## 第 17 周：Inference economics 与 scaling memo

### 最终任务

假设你有固定训练预算，写一份研究经理可以阅读的 memo：

1. 应训练多大的模型
2. 使用多少 token
3. 选择什么 precision
4. 预计训练时间
5. 预计推理成本
6. 模型部署的 KV cache 成本
7. 哪些结论来自实测
8. 哪些结论来自 scaling extrapolation
9. 最大的不确定性是什么

这比单纯复述 Chinchilla 更接近前沿实验团队的工作方式。

---

# 第五阶段：CS336 Assignment 4

## 第 18 周：Common Crawl 数据处理

### 学习内容

1. WARC
2. HTML extraction
3. text normalization
4. language identification
5. document metadata
6. streaming processing
7. fault tolerance

### 实现任务

1. 下载一个小型 Common Crawl subset
2. 解析 WARC
3. 提取正文
4. 保存 provenance
5. 记录处理失败原因
6. 设计可恢复的数据 pipeline

---

## 第 19 周：Filtering、deduplication 与 contamination

### 学习内容

1. heuristic quality filter
2. classifier based filtering
3. exact deduplication
4. near duplicate detection
5. MinHash
6. benchmark contamination
7. PII 与隐私风险

### 实现任务

1. exact hash dedup
2. MinHash 或等价 near duplicate 方法
3. language filter
4. quality scoring
5. benchmark overlap 检测
6. before after 数据统计

### 必须回答

1. 去重为什么可能提升模型效果
2. 过强过滤为什么会降低 diversity
3. benchmark contamination 为什么会夸大能力
4. 数据 quality score 是否可能引入价值偏差

---

## 第 20 周：Data mixing、tokenization fairness 与 embedding

### Georgia Tech 精读

1. Chameleon
2. Parity Aware BPE

### 选读

1. Improving Text Embeddings with Large Language Models
2. NV Embed
3. MMTEB

Embedding 在你的主路线中只占一周，因为你已经有较强的 RAG 和 embedding 应用经验。这里的目标不是重新学 embedding，而是理解：

1. representation 如何评测
2. multilingual benchmark 如何设计
3. embedding model 与 generative LM 的训练目标有何不同
4. MoE hidden representation 是否可以复用于 embedding

### 实现任务

设计三个 data mixture：

1. general text dominant
2. code dominant
3. math dominant

训练小模型后比较：

1. validation loss
2. code task
3. math task
4. general language task
5. multilingual compression ratio

---

## 第 21 周：Data ablation 与 data card

### 输出

1. 可重复的数据 pipeline
2. filtering statistics
3. deduplication statistics
4. mixture configuration
5. contamination audit
6. data card
7. 三个小模型的 ablation report

### 研究讨论练习

回答：

1. 如果质量过滤提高 benchmark，但降低少数语言表现，你如何处理
2. 如果 synthetic data 提升 reasoning，但导致表达同质化，你如何验证
3. 如果数据来源不透明，如何做风险管理
4. 小规模 data ablation 是否能外推到大模型

---

# 第六阶段：CS336 Assignment 5

## 第 22 周：Supervised Fine Tuning

### 学习内容

1. instruction dataset
2. chat template
3. response masking
4. sequence packing
5. loss normalization
6. LoRA 与 full finetuning
7. catastrophic forgetting
8. evaluation before and after SFT

### 实现任务

1. 构建一个数学或代码 instruction dataset
2. 进行 SFT
3. 比较 base model 与 SFT model
4. 分析 formatting、correctness 和 verbosity
5. 检查 training data memorization

---

## 第 23 周：DPO 与 preference optimization

### Georgia Tech 精读

1. Direct Preference Optimization

### 学习内容

1. preference pair
2. reference policy
3. implicit reward
4. beta
5. KL regularization
6. chosen 与 rejected log probability
7. reward margin
8. preference data noise

### 实现任务

1. 从零实现 DPO loss
2. 构建 chosen rejected pair
3. 对比 SFT 和 DPO
4. 改变 beta
5. 分析 reward margin
6. 检查 length bias

### 面试问题

1. DPO 为什么不需要显式 reward model
2. reference model 的作用是什么
3. beta 过大或过小会怎样
4. preference pair 噪声会产生什么影响

---

## 第 24 周：PPO、GRPO 与 DAPO

### Georgia Tech 核心内容

1. GRPO
2. DAPO
3. Understanding R1 Zero Like Training

### 学习内容

1. policy gradient
2. advantage
3. importance ratio
4. clipping
5. KL penalty
6. value model
7. group relative baseline
8. reward normalization
9. entropy
10. off policy issue

### 实现任务

先完成一个小型 policy gradient 环境，再实现：

1. 简化 PPO
2. 简化 GRPO
3. group sampling
4. reward normalization
5. KL monitoring
6. output length monitoring

### 必须解释

1. PPO 为什么需要 critic 或 value estimate
2. GRPO 如何构造 relative advantage
3. GRPO 省掉了什么
4. GRPO 没有自动解决哪些问题
5. DAPO 在训练稳定性或数据利用上试图改进什么

---

## 第 25 周：RLVR 与 reasoning

### Stanford 主线

1. verifiable reward
2. math reasoning
3. outcome reward
4. sampling
5. group update
6. evaluation

### Georgia Tech 扩展

选读：

1. Training a Generally Curious Agent
2. BIRD
3. Optimas
4. CWM

### 实现任务

1. 选择可以自动验证的数学或代码任务
2. 建立 verifier
3. 训练一个小模型
4. 记录 pass rate
5. 记录 response length
6. 记录 reward variance
7. 检查 reward hacking
8. 比较 SFT、DPO 和 RLVR

---

## 第 26 周：Self Play、test time scaling 与安全评测

### Georgia Tech 精读

1. Absolute Zero
2. Scaling LLM Test Time Compute Optimally
3. Learning to Discover at Test Time

### Georgia Tech 选读

1. SPICE
2. SWE RL
3. Emergent Misalignment

### 实验任务

1. 固定模型，改变采样数量
2. 比较 majority vote
3. 比较 verifier reranking
4. 比较不同 thinking budget
5. 画 test time compute 与正确率曲线
6. 检查高 compute 是否只增加长度而不增加正确率
7. 做一次 narrow finetuning 后的安全行为测试

### A5 最终报告

1. SFT baseline
2. DPO 结果
3. RLVR 结果
4. test time scaling
5. reward hacking analysis
6. mode collapse analysis
7. safety regression analysis

---

# 第七阶段：Agent 与主项目

## 第 27 周：Agent harness

Stanford CS336 对模型训练链路覆盖很强，但 Georgia Tech 在 Agent harness、workflow memory、self play software agents 和 compound AI systems 上提供了重要补充。Georgia Tech 官方课表把 Agent Workflow Memory 和 OpenHands Software Agent SDK 单独列为一个主题。([CocoXu][2])

### 阅读

1. Agent Workflow Memory
2. OpenHands Software Agent SDK

### 实现一个 mini agent harness

至少包含：

1. model adapter
2. tool schema
3. shell tool
4. file read tool
5. file write tool
6. trajectory logger
7. token budget
8. timeout
9. sandbox
10. retry
11. checkpoint
12. resume

### 不要只实现一个聊天循环

必须能回答：

1. 一个 task 的 state 存在哪里
2. tool error 如何返回
3. 执行失败如何恢复
4. trajectory 如何重放
5. 如何防止不同任务状态污染
6. 如何自动评分

---

## 第 28 周：推荐给你的主项目

结合你的背景，我最推荐的不是再做一个普通 RAG Agent，而是：

# Budgeted Long Context Agent Systems

## 核心研究问题

在固定 KV memory 或固定 inference cost 下，不同历史建模机制对长程 Agent 任务有什么影响？

比较：

1. GQA full attention
2. Sliding Window Attention 加周期性 global attention
3. recurrent linear state
4. Top K sparse history retrieval

## 实验任务

1. 长文档检索
2. 多文件代码定位
3. 长 trajectory tool use
4. 中间错误恢复
5. 早期信息在后期任务中的引用

## 评测指标

1. task success
2. exact evidence retrieval
3. TTFT
4. TPOT
5. peak KV memory
6. total tokens
7. tool calls
8. recovery rate
9. long range recall
10. cost per successful task

这个项目可以把你前面学到的：

1. attention architecture
2. KV cache
3. Triton 与 profiling
4. long context
5. Agent harness
6. evaluation

串成一条清晰研究主线。

---

## 第 29 周：Ablation 与 failure taxonomy

### 必做 ablation

1. 相同参数量
2. 相同训练 token
3. 相同 context budget
4. 相同 inference token budget
5. 不同 memory architecture
6. 不同窗口
7. 不同 Top K
8. 不同 global layer frequency

### Failure taxonomy

至少区分：

1. 没有检索到证据
2. 检索到但没有使用
3. 早期证据被遗忘
4. tool output 被错误解析
5. planning failure
6. execution failure
7. repeated loop
8. context pollution
9. state leakage
10. verifier failure

---

## 第 30 周：研究报告与开源产物

### 最终 artifact

1. 一个完整 GitHub repository
2. reproducible environment
3. unit tests
4. benchmark scripts
5. experiment configuration
6. raw result
7. figure generation code
8. 10 到 15 页技术报告
9. 20 分钟 job talk
10. 5 分钟项目 pitch

### 报告结构

1. Problem
2. Motivation
3. Related Work
4. Method
5. Complexity
6. Experimental Design
7. Results
8. Ablations
9. Failure Analysis
10. Limitations
11. Future Work

前一份求职经验指出，建立一个清晰的专业方向能够帮助候选人脱颖而出，而 job talk 也通常围绕一个连贯方向展开。 

---

# 第八阶段：面试与申请转化

## 第 31 周：ML coding 集训

### 必会题目

1. BPE
2. softmax
3. cross entropy
4. RMSNorm
5. RoPE
6. causal attention
7. GQA
8. KV cache
9. top k sampling
10. top p sampling
11. AdamW
12. DPO loss
13. GRPO advantage
14. tiny MoE
15. sliding window mask
16. beam search
17. logistic regression backward
18. k means
19. PCA
20. simple distributed gradient averaging

### 训练方式

1. 全程关闭 AI
2. 每题限制四十五分钟
3. 写完后自己设计测试
4. 主动解释 shape
5. 主动解释复杂度
6. 主动处理 edge case
7. 每天复盘一个 bug pattern

---

## 第 32 周：技术讨论、研究讨论与 job talk

### 技术讨论题库

1. 标准 attention 为什么昂贵
2. FlashAttention2 优化了什么
3. prefill 和 decode 的瓶颈为什么不同
4. GQA 与 MLA 分别如何减少 KV 成本
5. sliding window、linear attention 和 sparse attention 的取舍
6. MoE router 如何训练
7. 5D parallelism 如何组合
8. scaling law 如何指导预算
9. data dedup 为什么重要
10. SFT、DPO、PPO 和 GRPO 的区别
11. RLVR 为什么适合数学与代码
12. test time scaling 什么时候有效
13. Agent harness 为什么不只是 prompt
14. 如何评测长程 Agent
15. 如何发现 reward hacking
16. 如何发现 benchmark contamination
17. 如何 debug distributed loss divergence
18. 如何 debug training loss spike

### Research discussion

为主项目准备：

1. 三分钟版本
2. 七分钟版本
3. 二十分钟版本
4. 三个失败实验
5. 三个关键 insight
6. 两个可能的 follow up
7. 一个 scale up 方案
8. 一个安全或社会影响讨论

---

# 三、Georgia Tech 论文应该怎样分层阅读

不要尝试对 syllabus 中每篇论文做同等深度阅读。

## 第一层：必须精读

这些论文直接服务于你的主线：

1. Chameleon
2. Parity Aware BPE
3. DeepSeek V2 指定部分
4. Outrageously Large Neural Networks
5. DPO
6. Attention Sinks
7. TransMLA
8. GRPO 与 DAPO 材料
9. Linear Transformers Are Secretly Fast Weight Programmers
10. Delta Rule Parallelization
11. Test Time Compute Scaling
12. Training Compute Optimal Large Language Models
13. Scaling Laws for Precision
14. OpenHands Software Agent SDK

每篇精读后写一页笔记：

1. 研究问题
2. baseline
3. 核心机制
4. 关键公式
5. 复杂度
6. 训练设置
7. 主要结果
8. ablation
9. failure mode
10. 你会如何复现

## 第二层：根据主方向选择

### Post Training 与 reasoning 方向

1. Training a Generally Curious Agent
2. Absolute Zero
3. SPICE
4. SWE RL
5. Optimas
6. CWM
7. Learning to Discover at Test Time

### Safety 与 interpretability 方向

1. Emergent Misalignment
2. Attention Heads in LLM Safety
3. Scaling and Evaluating Sparse Autoencoders
4. Sparse Crosscoders

### Embedding 与 multilingual 方向

1. Improving Text Embeddings with LLMs
2. NV Embed
3. MMTEB

### Calibration 与 routing 方向

1. Active Task Disambiguation
2. Confidence Tokens

## 第三层：了解即可

1. Diffusion LM
2. Large Language Diffusion Models
3. Artificial Hivemind
4. BIRD

这些主题很有价值，但在你的当前目标中，不应该挤占 A1、A2、A5 和主项目的时间。

---

# 四、每周固定训练机制

## 1. 无 AI 实现时间

每周至少安排一次两小时 session：

1. 关闭 AI autocomplete
2. 不查看已有实现
3. 从空文件写模块
4. 自己写测试
5. 结束后再与参考实现比较

这是同时服务于课程理解和面试准备的最高回报活动。Stanford 课程和前述求职经验都明确强调了这一点。([Stanford CS336][1]) 

## 2. 一篇论文的三种表达

每篇核心论文都准备：

1. 一句话版本
2. 五分钟版本
3. 十五分钟白板版本

五分钟版本必须回答：

1. 问题是什么
2. 为什么旧方法不够
3. 新方法改变了什么
4. 成本是什么
5. 结果是否可信
6. 下一步怎么做

## 3. 每两周一次 seeded bug debugging

在自己的代码中随机加入一个 bug：

1. mask 错位
2. label shift
3. wrong normalization dimension
4. KV cache position 错误
5. distributed gradient 未同步
6. optimizer state 未恢复
7. padding 进入 loss
8. mixed precision overflow
9. MoE expert imbalance
10. Agent state leakage

限制一小时定位。

## 4. 每四周发布一个可见产物

1. 第 7 周：从零 Transformer
2. 第 14 周：GPU 与 inference benchmark
3. 第 17 周：Scaling memo
4. 第 21 周：Data pipeline
5. 第 26 周：Post Training report
6. 第 30 周：Capstone

这样不需要等到第 32 周才拥有可以 networking 的材料。

---

# 五、申请时间不必等到课程全部结束

建议节奏如下：

## 第 1 到 12 周

1. 完成基础与 systems
2. 暂不大规模投递
3. 联系熟悉的研究人员和工程师
4. 了解目标团队在招什么

## 第 13 到 20 周

1. 发布 A1 和 A2 结果
2. 每周联系两到三位相关从业者
3. 寻找 mock interview partner
4. 开始准备两版简历

## 第 21 到 26 周

1. 申请少量次优先级岗位
2. 用真实面试校准准备
3. 开始 recruiter call
4. 根据具体职位强化相应模块

## 第 27 到 32 周

1. 主项目达到可展示状态
2. 集中申请高优先级团队
3. 安排完整 mock loop
4. 完成 job talk
5. 尽量让多个流程时间接近

前述求职记录也提醒，内部推荐、合作网络和招聘团队是否有 headcount，可能比多学一篇论文更直接影响能否得到第一次面试。

---

# 六、针对不同岗位的时间调整

## 1. Research Engineer

时间比例：

1. 40% CS336 A2
2. 20% A1
3. 15% inference 与 long context
4. 10% A3
5. 10% A5
6. 5% paper discussion

重点：

1. Triton
2. FlashAttention2
3. distributed training
4. profiling
5. KV cache
6. serving
7. test coverage
8. performance debugging

## 2. Post Training Research Engineer

时间比例：

1. 25% A1 与基础系统
2. 15% A2
3. 10% data
4. 35% A5
5. 15% evaluation 和 Agent

重点：

1. SFT
2. DPO
3. PPO
4. GRPO
5. RLVR
6. verifier
7. sampling infrastructure
8. distributed rollout
9. reward hacking
10. test time scaling

## 3. Research Scientist

时间比例：

1. 25% implementation fundamentals
2. 20%核心论文
3. 35% capstone research
4. 10% technical discussion
5. 10% research writing

必须在主项目中增加：

1. 明确 hypothesis
2. 更强 baseline
3. 更完整 ablation
4. statistical uncertainty
5. scaling argument
6. novel extension
7. related work positioning

---

# 七、最适合你的最终定位

结合你已有的 AI application、RAG、医疗研究、推荐系统规划、当前企业 AI 工作和 Georgia Tech AI 背景，我不建议你把自己包装成一个刚开始学语言模型的通才。

更有竞争力的定位是：

> **Research Engineer 或 Applied Researcher，专注于长上下文模型、推理系统、Agent infrastructure 和可验证 Post Training。**

你的叙事可以是：

1. 你已经做过真实企业 AI 系统
2. 你理解 applied problem 和 deployment constraint
3. 你通过 CS336 补齐了从 tokenizer 到 distributed training 的模型底层
4. 你通过 Georgia Tech 的前沿论文体系补齐了长上下文、MoE、reasoning RL 和 Agent research
5. 你有一个能够连接架构、系统和 Agent evaluation 的研究型 capstone

这比同时声称自己擅长 embedding、diffusion LM、interpretability、safety、robotics、recommendation 和 post training 更容易让目标团队理解你的核心价值。

# 八、完成路线后的最低毕业标准

32 周结束时，你至少应该做到：

1. 无 AI 实现 tokenizer、Transformer、AdamW 和 generation
2. 无 AI 实现 attention、RoPE、RMSNorm、GQA 和 KV cache
3. 完成一个 Triton attention kernel
4. 完成一次分布式训练
5. 能估算 FLOPs、memory 和 KV cache
6. 能 profile prefill 和 decode
7. 能解释 MoE 和 5D parallelism
8. 能拟合并解释 scaling law
9. 能构建 Common Crawl 数据 pipeline
10. 能完成 SFT、DPO 和一个 RLVR experiment
11. 能解释 PPO、GRPO、DAPO 和 test time scaling
12. 能搭建 Agent harness 和自动 evaluation
13. 有一个包含 baseline、ablation 和 failure analysis 的主项目
14. 能完成二十分钟 job talk
15. 能通过无 AI 的 ML coding mock interview

真正的目标不是“看完两门课”，而是把 Stanford 的实现链路、Georgia Tech 的研究前沿和你的真实工程经历，合并成一个可以被前沿大模型团队清楚识别的能力主线。

[1]: https://cs336.stanford.edu/ "https://cs336.stanford.edu/"
[2]: https://cocoxu.github.io/CS8803-LLM-spring2026/calendar/ "https://cocoxu.github.io/CS8803-LLM-spring2026/calendar/"
