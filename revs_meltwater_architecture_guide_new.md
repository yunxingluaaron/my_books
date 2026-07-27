# Revs 舆情智能与预测系统 — 完整架构设计与实施指南

> **文档版本**: v1.0（2026-07-25）
> **数据源**: Meltwater API（仅 Export / Search / Analytics 权限，**无 Data Streams、无 Meltwater MCP**）
> **服务对象**: New England Revolution（MLS 足球俱乐部，下称 Revs）社媒团队负责人 + 高管层
> **本文档用途**: 交接给执行 agent 的唯一权威指南（single source of truth）。执行 agent 应严格按本文档实施，遇到文档未覆盖的情况时先记录到「开放问题」再向用户确认，不要自行发挥。

---

## 0. 给接手 Agent 的阅读指南（必读）

### 0.1 你是谁、你要做什么

你是接手本项目的执行 agent。你的任务是把一套基于 Meltwater API 数据的「舆情监测 + 机器学习预测 + 商业洞察交付」系统从零搭起来。本文档已经替你做完了所有的调研和架构决策，你只需要**按 Phase 顺序执行**。

### 0.2 本文档的使用规则

1. **严格按 Phase 顺序执行**（Phase 0 → 1 → 2 → 3 → 4 → 5）。每个 Phase 末尾有验收清单（Definition of Done），全部打勾才能进入下一 Phase。
2. **遇到 `⚠️ 陷阱` 标记必须停下来读完**。这些是真实的 API 坑，踩了会浪费配额或产生脏数据。
3. **遇到 `🔍 核实` 标记，先去指定的文档 URL 核对再写代码**。API 细节可能更新，本文档写死的端点以官方文档为准。
4. **遇到 `❓ 问用户` 标记，停下来向用户确认**，不要猜。
5. 所有术语在附录 B 术语表中有定义。看不懂一个词就去查，不要跳过。

### 0.3 硬性行为准则（DO / DON'T）

**DO：**
- 所有数据落盘一律进数据库（Postgres 优先，本地开发可用 SQLite）或 Parquet 文件。
- 所有对 Meltwater API 的调用必须经过「配额守护」模块（见 Phase 2 步骤 2.2），先检查预算再调用。
- 所有代码中的时间一律用 UTC 存储，展示层再转 `America/New_York`。
- 每次调用 API 后把请求参数、返回状态、返回条数写入 `api_call_log` 表（审计 + 配额核算）。
- 所有 DB 访问必须遵守第 14 章的连接预算（同库并发连接硬上限 10）：每进程一个 engine、Job 退出必 `engine.dispose()`、必设 `application_name`。

**DON'T：**
- **禁止把数据保存为 CSV 文件**（用户明确偏好；仅当用户明确要求 CSV 时例外）。Meltwater 导出模板也一律选 JSON（`api.json`），不选 CSV 模板。
- 禁止在没有水位线（watermark）机制的情况下裸拉数据（会重复消耗配额）。
- 禁止用随机切分（random split）评估任何时序模型，一律用时间切分（temporal split）。
- 禁止把 API key 写进代码或提交到 git，一律走环境变量 `MELTWATER_API_KEY`。
- 禁止在未做 off-policy evaluation 之前把任何 RL/bandit 策略直接上线到真实账号。

---

## 1. 项目背景与目标

### 1.1 客户与受众

| 受众 | 角色 | 他们要什么 | 时间粒度 |
|---|---|---|---|
| 受众 A | Revs 社媒团队负责人 | 操作层信号：什么正在爆、要不要升级上报、该重点盯谁 | 分钟～小时级 |
| 受众 B | Revs 高管层（executive leadership） | 战略层指标：品牌健康、声量份额、球场项目舆情、赞助价值 | 日～月级 + 危机时刻实时 |

**核心原则：两套受众 = 两套交付物**。不要试图用一个 dashboard 同时满足两边（详见第 7 章）。

### 1.2 关键业务背景（写洞察时必须引用的上下文）

1. **Everett 球场项目是当前最高价值的舆情议题**。背景事实：Kraft Group（Revs 母公司）于 2025-12-31 与 Everett 市和 Boston 市达成正式协议，将在 Mystic River 沿岸一块退役电厂地块建约 25,000 座、约 5 亿美元的足球专用球场；项目仍需 12–18 个月的许可与环评流程；社区意见会直接影响社区影响协议（Community Impact Agreement, CIA）条款。**这意味着 Everett/Boston 本地舆情不是 PR 虚荣指标，而是直接影响审批进程的商业变量。**
2. Revs 自 1996 年起与 NFL 的 Patriots 共用 Foxborough 的 Gillette Stadium，新球场是俱乐部级战略工程。
3. 品牌竞争基准：波士顿四大（Patriots / Celtics / Red Sox / Bruins）+ MLS 同行。
4. 体育社媒讨论的主战场之一是 X（Twitter），但 Meltwater API 只返回 tweet ID（见 2.3 陷阱 #5）。

### 1.3 项目目标（按 ROI 排序，先做 1 和 2）

| # | 项目 | 受众 | 一句话定义 | 优先级 |
|---|---|---|---|---|
| 1 | 爆点早期预警（Spike Early Warning） | A | 预测当前讨论波会不会在未来 2–6 小时变成大爆点 | P0 |
| 2 | 叙事与舆情走势追踪（含 Everett 球场仪表盘） | B | 按地域/利益相关方分解的情绪走势 + 7 天预测 | P0 |
| 3 | Share of Voice 竞争基准 | B | Revs vs 波士顿四大 + MLS 的声量/情绪对比与趋势 | P1 |
| 4 | 放大网络与级联规模预测（GNN） | A+B | 推断式放大网络；故事早期预判最终规模；产出关键放大者 watchlist | P1（详设见第 15 章） |
| 5 | 【阶段 B】发帖影响评估与内容打分 | A | 「如果发帖会有什么影响」的因果评估与 what-if 打分 | 阶段 B（当前不实施，见 1.5） |
| 6 | 转会绯闻知识图谱（Transfer Rumor Graph） | A+B | 球员×俱乐部×媒体的绯闻热度图谱 + 媒体可信度评分 | P1（详设见第 16 章） |

### 1.4 成功标准

- MVP（Phase 3 结束）：规则版爆点告警上线，社媒团队在 Slack 收到过至少 1 次「事后被证实有用」的提前告警。
- V1（Phase 4 结束）：ML 版告警 precision@k 和平均提前量（lead time）优于规则版；Everett 舆情仪表盘每日自动更新。
- 长期：月度高管 scorecard 进入例会材料；至少 1 条洞察被引用于实际决策。

### 1.5 项目范围声明（阶段 A / 阶段 B —— 误解高发区，必读）

- **阶段 A（当前，本文档主体）＝ 纯监听与分析。** 俱乐部现阶段**不发布任何帖子**；本系统只消费 Meltwater 的 earned media 数据，对「全世界关于球队的讨论」做监测、预测与洞察交付。所有交付物都是**给人看的信息**（告警、看板、报告、名单），系统不包含任何发布、回复、自动互动功能，也不给出「几点发帖/发什么」类指令。
- **阶段 B（未来，另行立项）＝ 发帖影响评估与决策支持。** 若俱乐部未来考虑发帖，第一个要回答的问题是「**如果发一条帖，会产生什么影响**」——这是**因果评估问题**（见 Phase 5 的 B0），不是优化问题。只有影响可测且为正，才谈 bandit/DPO 等发帖优化。凡本文档标注【阶段 B】的内容，当前一律：保留设计、不写代码、不投入。
- **对执行 agent 的判定规则**：任何涉及 owned social 数据、发帖建议、内容生成、自动回复的需求 → 先对照本节；属阶段 B 即挂起，并记录到第 10 章开放问题。

---

## 2. 关键约束（决定一切架构，必须先读）

### 2.1 已购权限 vs 未开通权限

| 能力 | 状态 | 对架构的影响 |
|---|---|---|
| Saved Searches 管理 | ✅ 有 | 一切数据获取的入口 |
| One-time Export | ✅ 有 | 历史回填训练数据 |
| Recurring Export | ✅ 有 | 每日对账层（最小频率=每天） |
| Search（拉少量 mentions） | ✅ 有 | 准实时轮询层的主力端点 |
| Analytics | ✅ 有 | 聚合指标（SOV、top sources 等） |
| **Data Streams（streaming/webhook 推送）** | ❌ 未开通 | **用「自适应轮询 + Alert 触发」平替**（第 4、5 章） |
| **Meltwater MCP / Mira MCP** | ❌ 未开通 | **用 FastMCP 自建工具层平替**（第 6 章） |
| Owned Social API | ❓ 未确认 | 仅阶段 B 需要（见 1.5），当前不阻塞任何工作 |

> 战略备注：先用轮询版把价值跑出来，积累「我们每天真实消耗 X 次调用、告警平均提前 Y 小时」的数据，再决定是否加购 Data Streams——带着使用数据去和 account manager 谈判。

### 2.2 速率限制与配额（配额是本系统第一设计变量）

以下为文档调研所得，**执行前必须核实自己合同的具体数字**：

| 限制项 | 数值 | 备注 |
|---|---|---|
| Analytics/Search 瞬时限流 | 5 次/秒，100 次/分钟 | 所有 earned media analytics 端点 |
| Analytics/Search 每日总额度 | 合同规定（inclusive 级仅 50 次/天，付费包常见 100+/天） | **Search 调用计入 analytics 每日额度** |
| Export 端点限流 | 20 次/分钟 | |
| 单次 one-time export 上限 | 200 万条文档 | 可用 sampling 参数控制 |
| Recurring export 最小频率 | 每天（DAY），无小时级 | 窗口结束后 30 分钟才执行 |
| Analytics 单次查询时间窗 | 默认最长 12 个月（以合同为准） | |
| 并发 Data Streams | N/A（未购） | |

🔍 核实：Phase 0 第一步就是调用 usage 端点（`GET .../usage/me/requests`，确切路径见 https://developer.meltwater.com/guides/getting-started/accessing-usage-statistics ）查出自己的真实限额和当前用量，把数字填进本表再继续。

### 2.3 Meltwater 数据特性与五大陷阱

**数据摄入模型**：Meltwater 平台自己持续爬取/摄入数据（每天 300 万+ 篇传统媒体文章）到中央数据存储；**你的 API 调用不触发抓取**，只是读取这个存储。摄入有延迟，官方不保证文章一发布就被抓到。

**⚠️ 陷阱 #1 — 迟到与重复文档**：同一篇文章会因「摄入延迟 / 出版方修改重发 / 来源列表调整触发重抓」而多次出现，且 `document_publish_date` 可能比当前时间早最多 31 天。
→ 对策：所有写入一律按 `document_id` 做 UPSERT（存在则覆盖）；特征计算一律用事件时间（publish_date）而非到达时间。

**⚠️ 陷阱 #2 — 30 分钟摄入缓冲**：recurring export 在时间窗口结束后 30 分钟才执行，这是官方对「一个时间段的数据何时算齐」的隐性承诺。
→ 对策：轮询层拉「最近」数据时，把窗口右边界设为 `now - 30min` 之前的数据视为基本稳定，`now-30min ~ now` 的数据标记为 provisional（临时），下轮覆盖。

**⚠️ 陷阱 #3 — Recurring export 会被静默取消**：30 天无人访问 data_url，recurring export 自动取消。
→ 对策：对账 job 每天访问一次即可天然满足；另加一个每周检查 export 状态的巡检任务。

**⚠️ 陷阱 #4 — Export 数据 30 天删除**：one-time export 的结果文件在执行后 30 天删除。
→ 对策：回填时下载后立刻入库，不要把 data_url 当长期存储。

**⚠️ 陷阱 #5 — X/Twitter 只有 ID 没有正文**：受 X 条款限制，API 只返回 tweet ID，正文需自行调 X API 补全（rehydration），而 X API 是付费的。
→ 对策：Phase 1–4 一律**不依赖 X 正文**。主信号来源 = 新闻 + Reddit + Bluesky + 博客 + 其他可得正文的社交源；X 只用「计数信号」（提及量、时间戳、作者数）。是否购买 X API 做 rehydration 是一个 ❓ 问用户 的预算决策。

### 2.4 编码规范摘要

- Python 3.11+；HTTP 用 `httpx`；DB 访问用 `SQLAlchemy 2.x` + `psycopg`；调度用 `APScheduler`（简单）或 cron。
- 配置集中在 `config.py` + 环境变量；密钥只从环境变量读。
- 每个模块可独立运行（`python -m pipeline.backfill` 这种形式）。
- 日志用 `structlog` 或标准 logging，JSON 格式输出。
- **再次强调：不产出 CSV。** 中间数据 → 数据库；ML 特征快照 → Parquet；报告 → Markdown/HTML。

---

## 3. Meltwater API 保姆级速查手册

### 3.1 认证

所有请求带 header：`apikey: $MELTWATER_API_KEY`。Base URL：`https://api.meltwater.com`。
Token 在 Meltwater 应用内创建（Developer Portal → API Credentials）。

```python
# common/mw_client.py — 所有 API 调用的唯一出口
import os, httpx

BASE = "https://api.meltwater.com"
HEADERS = {
    "apikey": os.environ["MELTWATER_API_KEY"],
    "Accept": "application/json",
    "Content-Type": "application/json",
}

def mw_request(method: str, path: str, **kwargs) -> httpx.Response:
    """唯一的 Meltwater HTTP 出口。任何模块不得绕过此函数直连。
    在这里统一做：配额检查（见 5.3.4）、重试、api_call_log 落库。"""
    # TODO: quota_guard.check_and_reserve(path)  # Phase 2 实现
    with httpx.Client(timeout=60) as c:
        r = c.request(method, BASE + path, headers=HEADERS, **kwargs)
    # TODO: log_api_call(path, r.status_code, ...)  # 落 api_call_log 表
    r.raise_for_status()
    return r
```

### 3.2 核心端点清单（已核实的部分）

| 用途 | 方法与路径 | 关键参数 |
|---|---|---|
| 列出 saved searches | `GET /v3/searches` | — |
| 创建 one-time export | `POST /v3/exports/one-time` | `search_ids`, `start_date`, `end_date`(UTC, ISO8601), `template{name:"api.json"}`, `sample{count,percentage}` |
| 查 one-time export 状态 | `GET /v3/exports/one-time/<export_id>` | 状态 `PENDING`→`FINISHED`，完成后从 `data_url` 下载 JSON |
| 创建 recurring export | `POST /v3/exports/recurring` | `window_time_unit`(`DAY`/`WEEK`/`MONTH`), `window_size`, `window_time`, `timezone`, `template` |
| 查 recurring export | `GET /v3/exports/recurring/<export_id>` | 状态 `ACTIVE` 后 data_url 持续被覆盖刷新 |
| 列出 custom categories | `GET /v3/custom_categories` | 可用于导出时分类/过滤 |

🔍 核实（写代码前必做）：以下端点确切路径与参数以官方页面为准，用浏览器打开核对——
- Search mentions（轮询层主力）：https://developer.meltwater.com/guides/listening/searching-mentions
- Analytics：https://developer.meltwater.com/guides/listening/analyzing-mentions
- 管理 searches：https://developer.meltwater.com/guides/listening/managing-searches
- Usage 统计：https://developer.meltwater.com/guides/getting-started/accessing-usage-statistics
- 输出模板字段definition：https://developer.meltwater.com/api-reference/templates/overview

### 3.3 数据流模型（一句话版）

**一切从 Saved Search 开始**：先有一个布尔查询式的 saved search（应用内或 API 创建），然后拿它的 `id` 去做三件事——export（批量拉原文）、search（少量拉原文）、analytics（拉聚合指标）。

### 3.4 One-time Export 详解（历史回填用）

- `start_date`/`end_date` 必须 UTC ISO8601（如 `2025-01-01T00:00:00Z`）；窗口含头不含尾。
- 结果上限 200 万条；超出会被采样到 200 万。可用 `sample` 参数主动控制。
- 异步：创建后进队列，几分钟到 1 小时不等；轮询状态到 `FINISHED` 再下载 `data_url`。
- 模板一律 `{"name": "api.json"}`（JSON 全字段；**不要用 CSV 模板**）。
- 返回 JSON 结构：`{"request": {...}, "docs": [ {每篇文档对象} ]}`。

### 3.5 Recurring Export 详解（对账层用）

- 频率只有 `DAY` / `WEEK` / `MONTH` 三档。`window_size` = 每次运行包含多少个单位的数据。
- 本项目配置：`window_time_unit=DAY, window_size=2`（每天跑、每次含最近 2 天）→ 制造 1 天重叠，接住迟到文档。
- 执行时间 = 窗口结束后 30 分钟。每次运行**覆盖**同一个 data_url。
- 单个 export 最多挂 5 个 saved searches。

### 3.6 文档对象里你会用到的字段（api.json 模板，字段名以模板文档为准）

最少需要映射入库的字段：`document_id`（去重主键）、`document_publish_date`、URL、标题、正文（新闻/博客/Reddit 有，X 无）、来源名称与类型、作者、reach/曝光估计、engagement 指标、Meltwater 自带 sentiment、国家/语言、matched keywords。
🔍 核实：逐字段对照 templates/overview 页面后再写 ORM 映射，不要凭记忆写字段名。


---

## 4. 总体架构

### 4.1 架构图

```text
┌─────────────────────────── Meltwater 平台（持续爬取，~3M 篇/天）───────────────────────────┐
│   中央数据存储（news / blogs / Reddit / Bluesky / X-ids / ...）                            │
└──────┬──────────────────────────┬──────────────────────────┬─────────────────────────────┘
       │ Tier 3（一次性）          │ Tier 1（准实时）            │ Tier 2（每日）
       ▼                          ▼                          ▼
  One-time Export           Search 端点自适应轮询          Recurring Export (DAY, size=2)
  12–24 个月历史回填          10min~1h 动态节奏              每日对账，修漏抓/去重复
       │                          │        ▲                 │
       │                          │        │ 触发             │
       │                          │   Meltwater Alert        │
       │                          │   → Slack 频道            │
       │                          │   → 事件监听器             │
       └──────────────┬───────────┴──────────────────────────┘
                      ▼  全部按 document_id UPSERT
        ┌─────────────────────────────────────┐
        │  PostgreSQL（唯一真相源）              │
        │  mentions / watermarks / api_call_log│
        │  features / predictions / alerts     │
        └───────┬──────────────┬───────────────┘
                ▼              ▼
        特征工程 (滚动窗口)   规则版检测 (z-score)  ──►  Slack 告警（社媒团队）
                ▼
        ML 层 (GBDT → DL/RL 进阶)
                ▼
   ┌────────────────────┬──────────────────────┐
   ▼                    ▼                      ▼
 Mission Control     高管 Scorecard        自建 Agent 层 (FastMCP)
 (社媒团队实时)        (月度 + 危机推送)      本地 DB 优先 / API 兜底
```

### 4.2 三层数据获取的分工（记住这个心智模型）

| 层 | 手段 | 频率 | 角色 | 延迟 |
|---|---|---|---|---|
| Tier 1 | Search 端点轮询 | 10 分钟～1 小时自适应 | 准实时信号，喂爆点检测 | 分钟级 |
| Tier 2 | Recurring export | 每天一次（窗口 2 天） | 真相层：对账、补漏、修正 | T+1 |
| Tier 3 | One-time export | 仅回填时 | 训练集：12–24 个月历史 | 一次性 |

**为什么这样设计**：未购 streaming，search 端点吃每日 analytics 配额 → 轮询必须省着用（自适应节奏 + 事件触发）；轮询必有漏，所以要每日 export 兜底；ML 需要长历史，所以要一次性回填。三层互为补充，缺一不可。

### 4.3 数据库 Schema（Postgres DDL，可直接执行）

```sql
-- 001_init.sql
CREATE TABLE mentions (
    document_id      TEXT PRIMARY KEY,          -- Meltwater 去重主键
    search_id        BIGINT NOT NULL,            -- 来自哪个 saved search
    publish_date     TIMESTAMPTZ NOT NULL,       -- 事件时间（一切分析用它）
    first_seen_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
    last_updated_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
    source_name      TEXT,
    source_type      TEXT,                       -- news / reddit / bluesky / twitter / blog ...
    url              TEXT,
    title            TEXT,
    body             TEXT,                       -- X 的为 NULL（只有 ID）
    author           TEXT,
    reach            BIGINT,
    engagement       JSONB,                      -- 各平台 engagement 原样存
    mw_sentiment     TEXT,                       -- Meltwater 自带情绪
    custom_sentiment JSONB,                      -- 自训 ABSA 结果（Phase 5 填充）
    country          TEXT,
    language         TEXT,
    matched_keywords TEXT[],
    raw              JSONB NOT NULL,             -- 完整原始文档，防字段遗漏
    ingest_channel   TEXT NOT NULL               -- 'poll' | 'recurring' | 'backfill'
);
CREATE INDEX idx_mentions_pubdate ON mentions (publish_date);
CREATE INDEX idx_mentions_search_pub ON mentions (search_id, publish_date);
CREATE INDEX idx_mentions_srctype ON mentions (source_type);

CREATE TABLE watermarks (          -- 每个 search 的轮询进度
    search_id     BIGINT PRIMARY KEY,
    watermark_ts  TIMESTAMPTZ NOT NULL,   -- 已确认拉齐到的 publish_date
    last_poll_at  TIMESTAMPTZ
);

CREATE TABLE api_call_log (        -- 配额审计（每次调用必写）
    id           BIGSERIAL PRIMARY KEY,
    called_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
    endpoint     TEXT NOT NULL,
    quota_class  TEXT NOT NULL,     -- 'analytics_daily' | 'export' | 'other'
    status_code  INT,
    result_count INT,
    params       JSONB
);

CREATE TABLE spike_alerts (
    id            BIGSERIAL PRIMARY KEY,
    fired_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    search_id     BIGINT,
    window_start  TIMESTAMPTZ,
    metric        TEXT,             -- 'volume_z' | 'ml_prob' ...
    value         DOUBLE PRECISION,
    threshold     DOUBLE PRECISION,
    payload       JSONB,            -- top mentions 摘要等
    outcome       TEXT              -- 事后人工标注: 'useful' | 'noise' | NULL
);

CREATE TABLE predictions (
    id           BIGSERIAL PRIMARY KEY,
    created_at   TIMESTAMPTZ NOT NULL DEFAULT now(),
    model_name   TEXT NOT NULL,     -- 'zscore_v1' | 'gbdt_v1' | ...
    target       TEXT NOT NULL,     -- 'spike_6h' | 'sentiment_7d' ...
    search_id    BIGINT,
    horizon_end  TIMESTAMPTZ,
    value        JSONB,             -- 预测值/分布
    features_ref TEXT               -- 指向 Parquet 特征快照路径
);
```

### 4.4 每日配额预算表（假设每日 analytics/search 额度 = 100 次；按实际合同调整）

| 用途 | 预算 | 说明 |
|---|---|---|
| Tier 1 轮询（4 组 search 轮流） | ≤ 60 次/天 | 比赛日窗口每 10 分钟、平日白天每小时、夜间(0–7 点 ET)停 |
| Alert 触发的按需拉取 | ≤ 15 次/天 | 事件驱动，安静日几乎为 0 |
| Analytics 看板（SOV 等） | ≤ 15 次/天 | 聚合指标每天固定拉一轮 |
| 预留缓冲 | 10 次/天 | 人工调试 / agent 兜底查询 |

配额守护规则：当日已用 ≥ 90% 时，只允许 Alert 触发类调用；≥ 100% 时全部拒绝并 Slack 通知管理员。


---

## 5. 分阶段实施手册（保姆级）

### Phase 0 — 准备与盘点（Day 1–2）

**步骤 0.1 拿到并验证 API token**
```bash
curl -s -H "apikey: $MELTWATER_API_KEY" https://api.meltwater.com/v3/searches | head
```
返回 JSON 且含 `searches` 数组即通过。401/403 → ❓ 问用户要正确 token。

**步骤 0.2 查真实配额**：调用 usage 端点（🔍 核实路径），记录：每日 analytics 限额、当前已用量、export 限制。**把数字回填到 2.2 的表格里**。

**步骤 0.3 创建 4 组 Saved Searches**（应用内建或 API 建均可；建完记录 `search_id` 到 `config.py`）：

| 组 | 名称 | Boolean 查询起点（需迭代调优） |
|---|---|---|
| S1 | REVS_BRAND | `"New England Revolution" OR "NE Revolution" OR #NERevs OR ("Revs" NEAR/10 (soccer OR MLS OR Foxborough OR Gillette))` + 主力球员名 + 主教练名 |
| S2 | STADIUM_EVERETT | `(("Everett" OR "Mystic River") NEAR/15 (stadium OR "soccer stadium")) OR ("Kraft" NEAR/10 (Everett OR stadium)) OR "Community Impact Agreement"` |
| S3 | COMPETITORS | Patriots / Celtics / "Red Sox" / Bruins 的品牌词（建议按队各建一个 search，SOV 才好算；注意单 export 最多挂 5 个 search） |
| S4 | SPONSORS_COMENTION | `(<赞助商品牌词>) AND ("New England Revolution" OR #NERevs)` — ❓ 问用户要赞助商名单 |

⚠️ 陷阱：`Revs` 单词歧义极大（引擎转速等），必须用 NEAR 邻近算子锚定足球语境。查询写完先在 Meltwater 应用里跑 7 天预览，人工抽查 50 条，precision < 80% 就继续加排除词。教练与球员名单会变，🔍 核实当前赛季名单后填入。

**步骤 0.4 起基础设施**：Postgres（Docker 即可）→ 执行 `001_init.sql` → 建 Python 项目骨架：
```text
revs-intel/
├── config.py            # search_ids, 配额预算, 阈值
├── common/mw_client.py  # 3.1 的唯一 API 出口
├── common/db.py         # SQLAlchemy engine + upsert helpers
├── pipeline/backfill.py # Phase 1
├── pipeline/poller.py   # Phase 2
├── pipeline/reconcile.py# Phase 3
├── detect/zscore.py     # Phase 3
├── ml/                  # Phase 4+
├── agent/               # Phase 6（自建 MCP）
└── reports/             # scorecard 生成
```

**Phase 0 验收**：☐ token 通 ☐ 配额数字已回填 ☐ 4 组 search 建好且抽查 precision≥80% ☐ 数据库就绪

---

### Phase 1 — 历史回填（Week 1）

目标：把 12–24 个月的 S1–S4 历史数据灌入 `mentions` 表，作为训练集与基线统计的地基。

**步骤 1.1** 按「每个 search × 每个月」切片创建 one-time export（避免单次超 200 万条、也便于失败重试）。伪流程：

```python
# pipeline/backfill.py（骨架，字段名以 3.6 核实结果为准）
import time, itertools
from common.mw_client import mw_request
from common.db import upsert_mentions

def create_export(search_id: int, start_iso: str, end_iso: str) -> str:
    body = {"onetime_export": {
        "search_ids": [search_id],
        "start_date": start_iso, "end_date": end_iso,
        "template": {"name": "api.json"}}}
    r = mw_request("POST", "/v3/exports/one-time", json=body)
    return r.json()["onetime_export"]["id"]

def wait_and_download(export_id: str) -> dict:
    while True:
        j = mw_request("GET", f"/v3/exports/one-time/{export_id}").json()["onetime_export"]
        if j["status"] == "FINISHED":
            import httpx
            return httpx.get(j["data_url"], timeout=300).json()  # {"request":..., "docs":[...]}
        if j["status"] in ("CANCELLED",):
            raise RuntimeError(f"export {export_id} cancelled: {j.get('status_reason')}")
        time.sleep(60)   # PENDING → 每分钟查一次

def run_backfill(search_id: int, months: list[tuple[str, str]]):
    for start_iso, end_iso in months:
        eid = create_export(search_id, start_iso, end_iso)
        data = wait_and_download(eid)
        upsert_mentions(data["docs"], search_id=search_id, channel="backfill")
        # ⚠️ export 端点 20 次/分钟限流：月切片场景天然不会超，但不要并发轰
```

**步骤 1.2** `upsert_mentions` 的唯一正确写法（`ON CONFLICT (document_id) DO UPDATE`，更新 `last_updated_at` 与全部内容字段）。禁止 `INSERT ... ON CONFLICT DO NOTHING`——会丢掉文章更新（陷阱 #1）。

**步骤 1.3** 回填质检 SQL（三条都要跑并把结果记录到交接笔记）：
```sql
SELECT search_id, date_trunc('month', publish_date) m, count(*) FROM mentions GROUP BY 1,2 ORDER BY 1,2; -- 月度量级是否连续、有无空月
SELECT source_type, count(*) FROM mentions GROUP BY 1 ORDER BY 2 DESC;                                    -- 源结构是否合理
SELECT count(*) FILTER (WHERE body IS NULL) * 1.0 / count(*) FROM mentions;                               -- 无正文占比（≈X 占比）
```

**Phase 1 验收**：☐ 4 组 search 各 ≥12 个月数据入库 ☐ 无空月（或已解释）☐ 质检结果已记录

---

### Phase 2 — 准实时轮询层（Week 2）

**步骤 2.1 轮询 worker 核心逻辑**（水位线 + 重叠 + 自适应节奏）：

```python
# pipeline/poller.py（骨架）
from datetime import datetime, timedelta, timezone

OVERLAP = timedelta(hours=2)          # 重叠缓冲，接住迟到文档

def poll_once(search_id: int):
    wm = get_watermark(search_id)                      # 无记录则取 now-24h
    start = wm - OVERLAP
    end   = datetime.now(timezone.utc)
    docs  = mw_search_mentions(search_id, start, end)  # 🔍 端点见 3.2 核实清单；注意分页
    upsert_mentions(docs, search_id=search_id, channel="poll")
    # 水位线推进到 end-30min（陷阱 #2：最近 30 分钟视为 provisional，下轮重拉覆盖）
    set_watermark(search_id, end - timedelta(minutes=30))

def current_cadence() -> timedelta:
    """自适应节奏。matchday 窗口 = 开球前 3h 到赛后 3h。
    比赛日程表在 config.py 维护（🔍 从 MLS 官网抓当季赛程,存 fixtures 表）。"""
    if in_matchday_window():   return timedelta(minutes=10)
    if is_daytime_et():        return timedelta(hours=1)    # 7:00–24:00 ET
    return None                                             # 夜间停轮询
```

**步骤 2.2 配额守护（quota guard）**——在 `mw_request` 里启用：
```python
def check_and_reserve(quota_class: str):
    used = count_today(quota_class)          # 查 api_call_log
    budget = DAILY_BUDGET[quota_class]       # 4.4 的预算表
    if used >= budget:            raise QuotaExhausted(quota_class)
    if used >= 0.9 * budget and not is_alert_triggered_context():
        raise QuotaSoftLimit(quota_class)    # 仅放行 Alert 触发的调用
```

**步骤 2.3 事件驱动增强（穷人版 streaming 的精髓）**：
1. 在 Meltwater 应用内为 S1、S2 各设一个 spike/every-mention 类 Alert，推送目标 = 专用 Slack 频道（Meltwater→Slack 是官方支持的单向推送）。
2. 写一个 Slack 事件监听器（Bolt SDK / Events API）：监听该频道新消息 → 立刻对相应 search 触发一次 `poll_once`（带 `alert_triggered` 上下文，可用软限额豁免）。
3. 效果：安静时段几乎不花配额，突发时响应延迟 ≈ Meltwater alert 延迟 + 一次 API 调用。

**Phase 2 验收**：☐ 轮询按节奏表运行 48h 无重复入库暴涨（重复率 <5%）☐ 配额守护触发过软限并正确降级 ☐ Slack alert → 拉取链路 5 分钟内完成一次端到端演练

---

### Phase 3 — 规则版爆点检测 + 对账（Week 3–4）【MVP 里程碑】

**步骤 3.1 z-score 爆点检测**（先规则后模型，这是刻意的架构决策）：

```python
# detect/zscore.py — 每 10 分钟对每个 search 跑一次（读本地 DB，不花 API 配额）
# 指标: v_t = 最近 60 分钟 reach 加权提及数（sum over mentions of log1p(reach)）
# 基线: 同一 search、过去 28 天、同星期几+同小时的 v 的均值 mu 和标准差 sigma（去掉 top 2% 极值）
# 触发: z = (v_t - mu) / max(sigma, eps) ；z >= 3 且 v_t >= MIN_VOLUME(默认10) → 发告警
# 冷却: 同一 search 90 分钟内不重复告警；写入 spike_alerts 表
```
调参说明：`z>=3` 起步；若一周误报 >5 次上调到 3.5；漏报明显下调到 2.5。**每条告警事后 24h 内由社媒团队在 Slack 上点 ✅/❌，写回 `spike_alerts.outcome`——这是 Phase 4 的免费标签，不许省略。**

**步骤 3.2 Slack 告警格式**（写给人看的，必须含 so-what）：
```text
🚨 [Revs 舆情] 讨论量异常上升  z=4.2（近60min reach加权量 vs 28天同时段基线）
主题聚类: <top keywords>   情绪: 负面 62%   Top 来源: <source1, source2>
样例: <title + url> ×3
建议: 量级中等偏上、负面主导，建议 30 分钟内完成评估并决定是否上报管理层。（是否/如何对外回应由俱乐部自行决定；本系统只提供信息，不给发帖指令——见 1.5）
[✅ 有用] [❌ 噪音]
```

**步骤 3.3 每日对账 job**（`pipeline/reconcile.py`）：
1. Phase 0 已创建 recurring export（DAY, size=2, 挂 S1–S4，注意 ≤5 个 search 上限）。
2. 每天在窗口结束 +45 分钟后（即官方 30 分钟缓冲再加 15 分钟余量）下载 data_url，全量 UPSERT（channel=`recurring`）。
3. 对账报告落库：当日轮询漏抓数（recurring 有而 poll 无）、更新覆盖数、迟到文档分布。漏抓率连续 3 天 >15% → 调整轮询节奏或 OVERLAP。
4. 该 job 天然满足「30 天必须访问一次」的防取消要求（陷阱 #3）。

**Phase 3 验收（= MVP 完成）**：☐ z-score 告警在真实比赛日触发且被社媒团队标注过 ☐ 对账漏抓率 <15% ☐ 高管收到第一份手工整理的周报（用第 7 章模板）


---

### Phase 4 — ML 版爆点预测（Week 5–8）

#### 4A. 问题定义（必须先写死再动手）

- **预测目标**：在时刻 t，预测「未来 6 小时内该 search 的小时级 reach 加权提及量是否会进入该 search 历史同期分布的 top 10%」（二分类）。
- **样本粒度**：每 (search_id, 10 分钟) 一个样本点。
- **标签来源**：用 Phase 1 回填的 12–24 个月历史数据离线构造；`spike_alerts.outcome` 的人工标注用作辅助校验集。
- ⚠️ 陷阱：标签必须只用 t 之后的数据算，特征必须只用 t 及之前的数据算（防泄漏）。写一个 `assert_no_future_leak()` 单测。

#### 4B. 特征工程清单（存 `features` Parquet 快照，路径写入 predictions.features_ref）

| 组 | 特征 | 说明 |
|---|---|---|
| 速度 | 近 10/30/60/180 分钟提及数；一阶差分（加速度） | 核心信号 |
| 广度 | 近 60 分钟独立作者数、独立来源数 | 区分「一人刷屏」vs「真扩散」 |
| 权重 | reach 加权量；top-tier 来源(按 reach 分位定义)占比 | 大媒体进场 = 强信号 |
| 情绪 | 近 60 分钟正/负占比及其变化率（先用 mw_sentiment，Phase 5 换自训） | |
| 结构 | source_type 分布熵；新闻 vs 社交比例 | 跨源扩散是爆点前兆 |
| 上下文 | 是否 matchday 窗口、距开球小时数、星期几、小时（sin/cos 编码） | |
| 基线 | 当前 z-score 值本身 | 让 ML 站在规则肩膀上 |

#### 4C. 训练与评估

- 模型：LightGBM / XGBoost 二分类，class weight 处理不平衡。
- **切分**：时间切分。例：前 18 个月训练 → 之后 3 个月验证 → 最后 3 个月测试。**禁止随机切分**。
- 指标：`precision@k`（每天最多发 k=3 条告警时的准确率）与 **平均提前量 lead time**（首次告警时刻 → 实际峰值时刻）。不看 accuracy。
- 上线判据：在测试段上，ML 版相对 z-score 规则版 precision@3 提升 ≥15% 或平均 lead time 增加 ≥30 分钟，否则继续用规则版（规则版保持运行作为 fallback 与对照）。
- 重训：每月滚动重训一次；赛季开始/结束、换帅等结构变化后立即重训（非平稳性对策）。

**Phase 4 验收**：☐ 泄漏单测通过 ☐ 时间切分回测报告落盘 ☐ 达到上线判据后 ML/规则双轨并行运行 2 周

---

### Phase 5 — DL / RL 进阶路线（选做，按顺序）

> 总原则：每一步的产出是下一步的输入。**阶段 A 顺序 = ①ABSA 情绪 → ②级联预测 → ⑤GNN 放大网络（详设第 15 章）**。③④⑥ 均以「俱乐部发帖」为前提，全部划入阶段 B（见 1.5）：保留设计、当前不实施。
> ❓ 问用户：项目定位是「生产系统」还是「学习/作品集」？生产 → 砍掉 ⑤⑥ 集中火力；作品集 → ⑤⑥ 反而是亮点。

#### ① 领域微调 ABSA 情绪模型（地基，先做）
- 动机：通用 sentiment 判不准球迷语言——反讽、"we suck" 式发泄、"FIRE THE COACH" 其实是高粘性球迷。
- 方案：小模型（如 RoBERTa 级或小型 LLM）+ LoRA 微调，做 aspect-based sentiment。**aspect 按业务定义**：`教练 / 阵容引援 / 票务与比赛日体验 / Everett 球场项目 / 俱乐部管理层`。
- 标注：LLM 弱标注 3–5k 条 + 人工抽检 300 条校验（一致率 <85% 则修 prompt 重标）。训练集从 `mentions` 表分层抽样（按 source_type 与月份）。
- 产出：`custom_sentiment` JSONB 回填全表；成为 Phase 4 特征与第 7 章仪表盘的输入。验收 = 在人工标注 holdout 上 macro-F1 显著优于 mw_sentiment。

#### ② 神经级联预测（DL 旗舰）
- 从「会不会爆」升级为**预测整条传播轨迹**：峰值时间、峰值量级、衰减速度。
- 技术路线（按实现难度排序）：a) 直接回归多目标（GBDT/MLP 预测 peak_time/peak_volume）b) PatchTST 类时序 transformer c) neural temporal point process（Hawkes 的神经版，输入逐条 mention 事件流：时间戳、log-reach、情绪）。
- 价值话术：把告警从「有事发生了」升级为「这事 3 小时后到顶、量级中等、可以不熬夜」。

---

> **🚧 以下 ③④⑥ 均属阶段 B（未来），当前一律不实施。** 阶段 B 的正确起点是 B0，而不是直接上 bandit。

#### B0【阶段 B 起点】发帖影响的因果评估 —— 回答「如果发帖，会有什么影响」
- 未来俱乐部若开始发帖，第一件事不是优化发帖，而是**度量单条帖子的因果影响**：发帖后相关话题的声量/情绪，相对「没发会怎样」的反事实基线变化了多少。
- 方法：CausalImpact / 合成控制（用 S3 竞品同话题时序构造反事实对照组）、中断时序分析（ITS）。**阶段 A 攒下的监听数据库正是未来的对照基线**——这是纯监听阶段的隐藏资产价值。
- 只有 B0 证明「发帖有可测的正向影响」，才有资格进入 ③④ 的优化问题。

#### ③【阶段 B】Contextual Bandit（发帖决策优化）
- 决策问题：**发帖时机 × 内容类型 × 格式** 的组合选择。context = 当前舆情状态特征 + 比赛日程 + 时段；reward = 发布后 24h 互动。
- 算法：Thompson Sampling（LinTS 起步）。探索预算 ≤10% 流量，其余走当前最优。
- ⚠️ 真实品牌账号上做 online 探索 = 拿品牌安全当训练成本。所以：动作空间只含**已获社媒团队白名单的安全选项**；每条探索动作先人工确认再发。
- 前置依赖：owned posts 的表现数据（❓ 问用户 Owned Social API 权限，或先用人工导出的历史帖子数据冷启动）。

#### ④【阶段 B】Reward Model + DPO（RLHF 范式迁移到社媒文案）
- 用历史帖子高/低 engagement 构造 preference pairs → 训 reward model。
- 用法一（立刻可用）：LLM 起草 n 版文案 → RM 排序 best-of-n → 人终审后发布。
- 用法二（进阶）：DPO 微调专属文案模型。
- 上线形态：AI 起草、RM 排序、人终审——**人永远在环内**。

#### ⑤ 传播图 GNN —— 已从 stretch 提升为**阶段 A 正式项目**
- 完整详设（数据现实、故事聚类、图 schema、G0–G4 分级建模、影响力归因、里程碑与验收）见**第 15 章**，此处不重复。
- 一句话摘要：推断式放大网络 + 故事级联规模早期预测；副产品「关键放大者 watchlist」在阶段 A 的用法是**提升告警权重 + 媒体关系情报**，与发帖无关。

#### ⑥【阶段 B】Offline RL + OPE / LLM 球迷模拟器（stretch）
- 历史发帖日志 → 离线学策略；上线前**必须**过 off-policy evaluation（IPS / doubly robust），再小流量 A/B。跳过 OPE 直接上线 = 违反 0.3 DON'T。
- LLM agents 模拟不同画像球迷群体对内容的反应，构建可安全探索的环境（world model 思路）。适合出 paper/portfolio，**不要**指望模拟器保真到能直接指导生产决策。

#### 数据量与非平稳性（所有 DL/RL 项目共用的两条军规）
1. **单队数据喂不饱 DL** → 用 saved searches 把全 MLS + 波士顿四大都拉进来做预训练/联合训练，再在 Revs 上微调。⚠️ 这会吃 export 限额，回填计划提前排期。
2. **分布会漂移**（赛季 vs 休赛期、换帅、球场项目节点）→ 一律滚动重训 + 时间切分回测 + 线上监控预测分布漂移（见第 8 章）。


---

## 6. 自建 Agent / MCP 层（平替官方 Meltwater MCP + Mira）

### 6.1 背景与定位

官方有两个 MCP 产品（均未开通）：Meltwater MCP（`https://api.meltwater.com/v2/mcp`，细粒度工具层，你自己编排）和 Mira MCP（`https://api.meltwater.com/mcp`，Meltwater 的 AI 替你编排出成品）。两者都需要订阅内含相应 package。

**我们的自建版反而更强**，因为本地 DB 里有官方 MCP 永远没有的东西：ML 预测结果、自训情绪、内部数据。核心设计原则：**工具优先读本地 Postgres（零延迟、零配额），Meltwater API 只做兜底**。

### 6.2 FastMCP Server 骨架

```python
# agent/mcp_server.py — pip install fastmcp
from fastmcp import FastMCP
mcp = FastMCP("revs-intel")

@mcp.tool()
def query_mentions(topic: str, days: int = 7, source_type: str | None = None) -> dict:
    """查询本地库中最近 N 天的 mentions 摘要（量级、情绪分布、top 来源、样例）。
    topic ∈ {brand, stadium, competitors, sponsors}，映射到 S1–S4 的 search_id。"""
    ...  # SELECT ... FROM mentions WHERE search_id=... AND publish_date > now()-interval

@mcp.tool()
def stadium_sentiment_report(days: int = 14) -> dict:
    """Everett 球场议题舆情：按地域(本地媒体 vs 全国)与 aspect 分解的情绪走势 + 最新预测。"""
    ...

@mcp.tool()
def latest_predictions(target: str = "spike_6h") -> dict:
    """读 predictions 表，返回各 search 最新模型输出与置信度。"""
    ...

@mcp.tool()
def recent_alerts(days: int = 7) -> dict:
    """读 spike_alerts，含人工标注 outcome，用于'上周告警质量如何'类问题。"""
    ...

@mcp.tool()
def mw_live_analytics(search_key: str, metric: str, days: int) -> dict:
    """兜底：本地数据不足时直连 Meltwater analytics 端点。
    ⚠️ 走 mw_request → 受配额守护约束，预算见 4.4（预留缓冲 10 次/天）。"""
    ...

if __name__ == "__main__":
    mcp.run()   # 默认 stdio；远程部署用 streamable-http
```

挂载到 Claude Desktop（`claude_desktop_config.json`）：
```json
{"mcpServers": {"revs-intel": {"command": "python", "args": ["-m", "agent.mcp_server"]}}}
```

### 6.3 DIY 版 Mira：每日晨报 Agent

- 定时（每天 7:30 ET）触发一个 Claude 驱动的 agent：调用上面 4 个本地工具 + 至多 2 次 `mw_live_analytics` → 生成一页纸 Markdown 晨报 → 推 Slack + 存 `reports/`。
- 晨报固定结构：昨日总量与环比 → 情绪要点（按 aspect）→ 球场项目动态 → 竞品对比一句话 → 今日关注点（含比赛日提示）→ 每条都带 so-what。
- 这就是「orchestrated outcome」的自建版；高管想追问细节时直接在 Claude 里继续问（工具已挂载）。

---

## 7. Business Insight 交付层（价值成败在此）

### 7.1 两套交付物规格

**A. Mission Control（社媒团队，实时）**
- 载体：Slack 频道（告警）+ 轻量 web 看板（可后置）。
- 内容：spike 告警（3.2 格式）、级联预测（Phase 5②后：预计峰值时间/量级）、关注优先级队列（按 reach×负面度排序的高优先 mentions，供人工评估与上报）、放大者 watchlist 命中提示（第 15 章）。

**B. 高管 Scorecard（月度 + 危机推送）**
- 载体：一页纸 Markdown/HTML 报告（禁止超过一页；细节放附录链接）。
- 固定四栏：① 品牌健康指数（量级、净情绪、加权趋势）② SOV vs 波士顿四大+MLS（份额与变化）③ Everett 球场舆情专栏（按地域与利益相关方分解 + 7 天预测 + 风险点）④ 赞助曝光价值（S4 共现量 × reach 估值）。
- 危机推送：z≥4 且负面主导且持续 >2 小时 → 直接推高管版摘要（阈值与名单 ❓ 问用户）。

### 7.2 「so what」写作规范（每条洞察强制执行）

格式：**观察（数字）→ 解释（为什么）→ 建议（做什么）**。
- ❌ 坏例：「负面情绪上升 12%。」
- ✅ 好例：「负面声量上升 12%，集中在 Everett 本地媒体的交通议题（占新增负面的 61%）；建议在下次社区会议前主动发布交通规划与接驳方案内容。」

### 7.3 内部数据 Join 计划（高管语言的来源）

- 目标句式：「客场大胜后 48 小时内的声量峰值对应下一主场散票销售提升 X%」——社媒信号 × 收入指标的相关性才是董事会语言。
- 需要用户提供（❓ 问用户，按易得性排序）：比赛日票务/散票销售、商品销售、App/官网流量、（如有）转播收视。
- 实施：新建 `internal_metrics` 表（date, metric, value, source），先做滞后相关性分析（0–7 天 lag 的 Spearman），显著后再谈因果。⚠️ 相关≠因果，报告措辞用「对应/伴随」，不用「导致」。

---

## 8. 运维、监控与故障手册

### 8.1 每日自动巡检（一个 daily job 全做完，结果推 Slack 运维频道）

| 检查 | 阈值 | 动作 |
|---|---|---|
| 配额用量（api_call_log） | >80% 预警 | 通知 + 次日复盘节奏配置 |
| 水位线滞后 | 任一 search >3h | 检查 poller 存活，手动补拉 |
| 对账漏抓率 | >15% 连续 3 天 | 调整 OVERLAP / 节奏 |
| mentions 当日入库量 | 比 28 天同星期均值低 60% | 检查 search 是否被改/删、export 是否被取消（陷阱 #3） |
| 重复率（同 id 多 channel） | 仅监控 | 正常现象，UPSERT 已处理 |
| 模型输入漂移 | 特征均值偏移 >3σ | 触发重训评估 |
| recurring export 状态 | 非 ACTIVE | 立即重建并告警 |

### 8.2 故障处理速查

- **429（限流）**：指数退避重试（base 2s, max 5 次）；`QuotaExhausted` 则停到次日，只留 Alert 触发通道。
- **export 长时间 PENDING（>2h）**：不要重复创建（浪费队列），先查 status_reason，再联系支持。
- **search 被应用内用户改动**：boolean 变了会造成数据断层——把 4 组 search 的查询文本每周快照进 `search_snapshots` 表，diff 出变化即告警。
- **Meltwater 平台事故**：订阅 https://status.api.meltwater.com ，事故期间暂停轮询、事后用 one-time export 补洞。

---

## 9. 决策日志（为什么是这样设计的）

| 决策 | 理由 | 重新评估条件 |
|---|---|---|
| 不用 streaming，用三层轮询 | 未购 Data Streams；用例只需分钟级延迟 | 拿到真实用量数据后与 account manager 谈加购 |
| 先规则（z-score）后 ML | 两周可上线、积累标签、建立信任 | ML 达到 4C 上线判据 |
| X 只用计数信号不买正文 | X API rehydration 是额外付费 | ❓ 用户批准预算后升级 |
| Export 一律 JSON 模板 | 全字段 + 用户禁 CSV 偏好 | 无 |
| 本地 DB 优先的自建 MCP | 零配额零延迟 + 能融合预测与内部数据 | 官方 MCP 开通后可并存 |
| 人永远在 RL 环内 | 品牌安全 > 探索效率 | 无（不可重新评估） |
| 阶段 A 限定纯监听，零发帖侧功能 | 俱乐部当前不发帖；防范围蔓延与品牌风险 | 俱乐部启动发帖 → 进入阶段 B，先做 B0 因果评估 |

## 10. 开放问题清单（接手后第一次对话就问用户）

1. 【阶段 B 才需要，当前不阻塞】Owned Social API 是否在套餐内？（发帖影响评估与 bandit 的数据来源）
2. 赞助商名单（S4 需要）；高管危机推送的名单与阈值偏好。
3. 是否批准 X API rehydration 预算？
4. 内部数据（票务/商品/流量）能拿到哪些、什么格式？
5. 项目定位：生产系统还是作品集？（决定 Phase 5 的取舍）
6. 每日 analytics 真实限额数字（Phase 0 步骤 0.2 查完回填）。
7. 【第 16 章前置】用户已归类的媒体名单，请以结构化形式提供：规范名 / 别名与常用写法 / 域名或账号 / 类型（机构 outlet｜记者 journalist）/ 语言 / 用户主观分层（tier，可选）。此名单同时服务第 15 章（media 节点）与第 16 章（可信度先验）。

---

## 附录 A — 快速参考卡

- Base URL `https://api.meltwater.com`；header `apikey: <token>`；时间一律 UTC ISO8601，窗口含头不含尾。
- 端点：`GET /v3/searches` · `POST /v3/exports/one-time` · `GET /v3/exports/one-time/<id>` · `POST /v3/exports/recurring` · `GET /v3/exports/recurring/<id>` · `GET /v3/custom_categories`
- 文档入口：https://developer.meltwater.com/guides/getting-started/overview · FAQ：https://developer.meltwater.com/help/faqs · 状态页：https://status.api.meltwater.com
- 限流：analytics/search 5/s·100/min·每日额度看合同；export 20/min；one-time ≤200 万条；recurring 最小 DAY、窗口结束 +30min 执行、30 天不访问被取消。

## 附录 B — 术语表

| 术语 | 定义 |
|---|---|
| Saved Search | Meltwater 里的布尔查询，一切 export/search/analytics 的入口，用 `search_id` 引用 |
| Mention / Document | 一条匹配内容（新闻/帖子/评论），主键 `document_id` |
| Watermark（水位线） | 「已确认拉齐到的 publish_date」，轮询增量的进度指针 |
| UPSERT | 存在则更新、不存在则插入；本项目按 document_id 执行 |
| Reach | Meltwater 对内容潜在曝光的估计值，用作加权 |
| SOV | Share of Voice，某品牌声量占对比集合总声量的比例 |
| Lead time | 首次告警时刻到实际峰值时刻的时间差，越大越好 |
| precision@k | 每天只允许 k 条告警时，告警中真爆点的比例 |
| ABSA | Aspect-Based Sentiment Analysis，按业务维度分面的情绪分析 |
| OPE | Off-Policy Evaluation，用历史数据评估新策略而不上线 |
| Provisional 数据 | `now-30min ~ now` 的未稳定数据，下轮轮询覆盖 |

## 附录 C — 本项目十条核心结论（一屏版）

1. 抓取是 Meltwater 平台侧的事，API 只是读数；一切延迟预期围绕「摄入延迟 + 30 分钟缓冲」设定。
2. 未购 streaming ≠ 做不了准实时：自适应轮询 + Alert 事件触发 + 每日对账 = 分钟级延迟的平替，而分钟级对本用例完全够用。
3. 配额是第一设计变量：所有调用过唯一出口 `mw_request`，配额守护先行。
4. `document_id` UPSERT + 事件时间处理，是对抗迟到/重复文档的唯一正确姿势。
5. 两套受众两套交付物：社媒团队要 mission control，高管要一页纸 scorecard。
6. Everett 球场舆情是本项目最高价值议题——它直接影响审批与 CIA 条款，不是虚荣指标。
7. 先规则后模型；ML 上线判据 = 相对规则版 precision@3 +15% 或 lead time +30min。
8. 阶段 A 只做监听侧：ABSA 情绪 → 级联预测 → GNN 放大网络；bandit/DPO/offline RL 属阶段 B（俱乐部发帖后才谈），人永远在环内。
9. 单队数据不够 → 全 MLS + 波士顿四大联合训练再微调；一律时间切分 + 滚动重训。
10. 自建 MCP 本地 DB 优先，比官方版更强（融合预测与内部数据）；洞察一律「观察→解释→建议」。


---

## 11. Azure 部署架构（Container Apps + VNet + Azure PostgreSQL）

### 11.1 部署拓扑

```text
公司 Azure VNet
├── ACA Environment（infrastructure subnet）
│   ├── App: frontend（常驻，仅访问 backend，不碰 DB）
│   ├── App: backend API（常驻；DB 读路径 + Slack Events 回调 + 内存缓存）
│   └── Jobs（cron 触发，跑完即退，状态全在 DB）:
│       ├── job-poller      cron: */10 * * * *   （内部自适应节奏，见 11.2）
│       ├── job-reconcile   cron: 每日 UTC 固定时刻（recurring 窗口结束+45min）
│       ├── job-rollup      cron: 每小时 :50     （维护 mentions_hourly，见 12.3）
│       ├── job-briefing    cron: 每日 11:30 UTC（=7:30 ET 前后，注意夏令时）
│       └── job-inspect     cron: 每日巡检（第 8 章清单 + 14.5 连接检查）
├── Private Endpoint → Azure Database for PostgreSQL Flexible Server
│   └── Private DNS: privatelink.postgres.database.azure.com
└── Key Vault（MELTWATER_API_KEY、Slack token → ACA secret reference 注入）
```

要点：
1. **调度用 ACA Jobs，不在常驻容器里跑 APScheduler**——Job 无状态、按时长计费、失败可由平台重试；一切进度状态存 Postgres（watermarks 表）。
2. **DB 认证用 Managed Identity（Entra ID）**，不管理密码；Meltwater key 从 Key Vault 注入。
3. 前端永远只访问 backend API，**绝不直连 DB**（连接预算原因见第 14 章）。

### 11.2 自适应节奏在 cron 里的实现（重要技巧）

cron 表达不了「比赛日 10 分钟、平日 1 小时、夜间停」。做法：cron 固定 `*/10 * * * *`，Job 启动第一步调 `current_cadence()` 自检，不在应跑窗口则 `exit 0`。空跑成本仅数秒，节奏逻辑 100% 留在代码里、可测试。

### 11.3 并发与幂等（双保险）

- Job `parallelism=1` + replica timeout（如 poller 8 分钟）防卡死重叠。
- 代码内再加 Postgres 事务级咨询锁：任务体包在一个事务里，开头 `SELECT pg_try_advisory_xact_lock(hashtext('poller'))`，拿不到立即退出。⚠️ 用 **xact 版**而非 session 版（第 14 章解释）。
- **事务性水位线（本章最重要模式）**：数据 UPSERT 与水位线推进在**同一事务**提交。DB 写失败 → 水位线不动 → 下轮自动重拉同窗口。任务因此天然幂等、可盲重试。

### 11.4 VNet 出网陷阱

⚠️ 出网 allowlist 只放 `api.meltwater.com` 会挂：**export 的 `data_url` 通常指向另一个云存储域名（预签名 URL）**。上线前手动跑一次 export，确认 data_url 实际域名后连同加白。Slack、（如启用）X API 域名同理。

---

## 12. 数据增长治理

量级预期：4 组 search 日均数千～数万条，两年千万行级——Postgres 扛得住；**真正的膨胀源是 `raw JSONB` 列（常占体积 70%+）**。四招：

### 12.1 按月分区
`mentions` 改为 `PARTITION BY RANGE (publish_date)`，月分区；job-rollup 顺带提前建好未来 2 个月分区。收益：查询剪枝 + 归档时整分区 detach，不做大 DELETE。

### 12.2 热 / 温 / 冷 三层生命周期
| 层 | 范围 | 内容 | 动作（每月维护 Job） |
|---|---|---|---|
| 热 | 0–90 天 | 全字段含 raw，全索引 | 无 |
| 温 | 90 天–2 年 | 剥离 raw（先整体导出该月 raw 到 Blob 的 JSON 归档，再 `SET raw=NULL`） | 月度执行 |
| 冷 | >2 年 | 整分区导出 **Parquet → Azure Blob**（生命周期策略降 Cool/Archive）后 drop 分区 | 月度执行 |

ML 训练本来就读 Parquet，冷层即训练层，一举两得。（依旧不产出 CSV。）

### 12.3 Rollup 表（比删数据更重要的优化）
`mentions_hourly(search_id, hour, cnt, reach_sum, pos_cnt, neg_cnt, uniq_authors, ...)`，job-rollup 增量维护（只重算最近 3 小时，覆盖 provisional 区间）。z-score 基线、看板、SOV、晨报**一律读 rollup**——查询成本与原始数据量彻底脱钩。

### 12.4 索引与膨胀
- 大表时间列用 **BRIN 索引**（体积约为 B-tree 的 1%，对按时间追加的数据极高效）；高频等值列继续 B-tree。
- UPSERT 密集 → 死元组多：`ALTER TABLE mentions SET (autovacuum_vacuum_scale_factor=0.02)`。
- 每周巡检膨胀率（pgstattuple 或估算 SQL），>30% 记录到运维笔记。

---

## 13. 韧性与降级设计（Fallback 体系）

### 13.0 核心认知
三层架构天生自愈：**Tier 1 轮询失败只是「延迟事件」，不是「丢数据事件」**——漏窗 T+1 由 recurring 对账补齐，更大的洞用 one-time export 定向回填。Fallback 目标 = 失败时不浪费配额、不写脏数据、不影响读路径。

### 13.1 故障→机制对照表
| 故障 | 机制 |
|---|---|
| Meltwater 429/5xx/超时 | tenacity 指数退避+抖动，≤5 次；连续失败开**熔断器**（熔断期跳过轮询只记日志，半开探测恢复） |
| 配额耗尽 | 配额守护降级（仅 Alert 触发通道 → 全停），已有设计 |
| Postgres 不可用 | 水位线不前进=下轮重拉（幂等）；**已拉到手的数据 spool 成 JSON 写 Blob `dead-letter/` 容器**（不浪费已花配额），恢复后 job-replay 回灌 |
| 单条坏文档 | 逐条 try/except，坏档进 `quarantine` 表（原始 payload+错误），**绝不让一条毒死整批** |
| Job 卡死/重叠 | xact 咨询锁 + replica timeout 强杀 |
| Slack 投递失败 | `spike_alerts` 表为真相源，at-least-once 重试，漏投由 job-inspect 兜底 |
| 连接数打满（53300） | 见 14.4 |

### 13.2 降级阶梯（写进代码，不留在脑子里）
- **L0 正常**。
- **L1 配额软限**：仅事件触发拉取。
- **L2 Meltwater 故障**：停摄入；前端照常，界面挂「数据截至 X 时刻」横幅（backend 读 DB 不受影响）。
- **L3 DB 故障**：backend 返回内存缓存的最近聚合值；poller spool 到 Blob。
原则：**读路径与摄入路径彻底解耦，前端永远不因摄入挂而挂。**

### 13.3 平台侧保障
Azure Monitor 告警：Job 连续失败、水位线滞后>3h、连接数≥8（见 14.5）。Flexible Server PITR 备份保留期 ≥14 天。订阅 Meltwater 状态页，事故期停轮询、事后 one-time 补洞。

---

## 14. 连接治理（硬约束：同库最多 10 个并发连接）

> 背景：公司 Postgres 限制同一数据库最多 10 个并发连接，超限即出问题。因此**连接是比 API 配额更稀缺的资源**，本章规则与 0.3 行为准则同级，必须执行。

### 14.1 连接预算表（最坏并发合计 ≤8，预留 2）
| 组件 | 形态 | 连接策略 | 最坏占用 |
|---|---|---|---|
| backend API | 常驻 | SQLAlchemy 池：`pool_size=2, max_overflow=1, pool_timeout=10` | 3 |
| job-poller | 短命 | 单连接 | 1 |
| job-reconcile | 短命 | 单连接 | 1 |
| job-rollup / 月度维护 | 短命 | 单连接（错峰调度，见下） | 1 |
| job-briefing / inspect | 短命 | 单连接（错峰） | 1 |
| 人工调试（psql/DBeaver） | 手动 | 用完即断 | 1 |
| **预留缓冲** | — | — | **2** |

**错峰规则**：Jobs 的 cron 分钟位错开（poller :00/:10/…，rollup :50，reconcile 固定时刻，briefing/inspect 各自固定），使短命 Job 同时在跑的数量 ≤2。即便全部撞车，预算表最坏也只有 8。

### 14.2 代码级铁律
1. **每进程一个 engine，严禁函数内临时 create_engine**。
2. 常驻 API engine 参数：`pool_size=2, max_overflow=1, pool_timeout=10, pool_pre_ping=True, pool_recycle=300`（pre_ping+recycle 防 Azure 网关回收空闲 TCP 后拿到死连接）。
3. Job 模板（照抄）：
```python
# common/db.py
from sqlalchemy import create_engine

def job_engine(app_name: str):
    return create_engine(
        DSN, pool_size=1, max_overflow=0, pool_pre_ping=True,
        connect_args={
            "application_name": app_name,                    # 连接追责的关键
            "options": "-c statement_timeout=120000 "
                       "-c idle_in_transaction_session_timeout=60000",
        },
    )

# pipeline/poller.py 入口
def main():
    eng = job_engine("job-poller")
    try:
        with eng.begin() as conn:                            # 单事务 = 锁+数据+水位线
            if not conn.execute(text(
                "SELECT pg_try_advisory_xact_lock(hashtext('poller'))")).scalar():
                return                                       # 已有实例在跑，直接退出
            run_poll(conn)                                   # UPSERT + 水位线同事务
    finally:
        eng.dispose()                                        # 铁律：退出必 dispose
```
4. 一律 `with eng.begin()/eng.connect()` 上下文管理器，禁止裸 `connect()` 不关。
5. 所有组件必须设 `application_name`（api / job-poller / job-reconcile / …），否则 14.5 的追责查询失效。

### 14.3 服务器端兜底（防「忘关」的自动回收网）
在 Flexible Server 参数里设：`idle_in_transaction_session_timeout=60s`、`idle_session_timeout=10min`（PG14+ 支持；管理员会话可豁免）。含义：即使代码泄漏连接，空闲事务 1 分钟、空闲会话 10 分钟后被服务端自动断开。

### 14.4 连接打满（FATAL 53300 too_many_connections）的降级
按 L3 流程处理：退避重试 3 次（2s/4s/8s）→ 仍失败：Job 场景把已拉数据 spool 到 Blob dead-letter 后退出；API 场景返回缓存值并告警。**绝不循环硬重试**（那会让风暴更糟）。

### 14.5 监控与人工处置
巡检与告警共用一条查询（backend 每分钟采样，≥8 触发 Slack 告警）：
```sql
SELECT application_name, state, count(*), max(now()-state_change) AS oldest
FROM pg_stat_activity WHERE datname = current_database()
GROUP BY 1,2 ORDER BY 3 DESC;
```
人工回收僵尸（先看清 application_name 再动手）：
```sql
SELECT pg_terminate_backend(pid) FROM pg_stat_activity
WHERE datname = current_database() AND state = 'idle'
  AND state_change < now() - interval '15 minutes'
  AND application_name NOT IN ('api');
```

### 14.6 PgBouncer 决策（修订第 11 章相关表述）
- **现阶段（组件 ≤6 个）：不启用 PgBouncer，全部直连 5432**，靠 14.1 预算表管住——链路最简单、无兼容性坑。
- **后期前端流量增长、API 需要更大客户端并发时**：仅 backend API 改走 Flexible Server 内置 PgBouncer（6432，transaction pooling，服务端 default_pool_size 控制在 4–5）；**Jobs 保持直连 5432**。
- ⚠️ 原因（也是 11.3 用 xact 锁的原因）：transaction pooling 下 session 级特性不可靠——session 版咨询锁（`pg_try_advisory_lock`）会错乱，psycopg 的 prepared statements 也需额外配置（`prepare_threshold=None` 或确认 PgBouncer 版本支持 `max_prepared_statements`）。Jobs 直连 + `pg_try_advisory_xact_lock` 可完全绕开这些坑。


---

## 15. 放大网络 GNN 详设（阶段 A 正式项目）

### 15.1 目标与两个产出

- **产出 1（预测）**：一个故事（story）开始后 30 分钟内，根据「哪些节点已经接住了这个故事」，预测它 48 小时后的最终规模（reach 加权总声量）。
- **产出 2（名单）**：数据驱动的**关键放大者 watchlist**。阶段 A 的两个用法：① watchlist 节点在故事早期出现 → 自动提升该故事的告警权重（回灌 Phase 4 spike 模型，形成闭环）；② 作为媒体关系情报交付高管/公关（「球场议题的声量由哪些媒体和账号驱动」）。**与发帖无关，符合 1.5 范围声明。**

### 15.2 先泼冷水：数据现实与边的三种来源

⚠️ 最重要的诚实声明：**Meltwater earned media 数据不包含真实的转发/引用链**（X 更是只有 ID）。我们构建的是**推断式**放大网络，边分三级（可信度递减）：

| 边类型 | 构建方法 | 可信度 |
|---|---|---|
| E1 引用边 | 正文中的超链接指向另一文档的 URL（先做 URL 归一化：去 utm 参数/统一协议）；正文出现「according to <媒体名>」「per <记者名>」类模式（规则 + NER） | 强 |
| E2 结构边 | Reddit 的 subreddit/thread 归属（🔍 核实 api.json 里 Reddit 文档的字段是否含 thread/parent 信息）；Bluesky 的 @提及 | 中 |
| E3 时间先行边 | 同一 story 中，A 先报道、B 在 Δt≤6h 内跟进；跨全部 stories 聚合成 A→B 的加权边 | 弱但覆盖最广 |

**E3 的去偏（必须做，否则全是假边）**：大媒体什么都报，先行≠影响。用 PMI 风格归一化：`w(A→B) = log[ observed(B 在 A 后跟进的 story 数) / expected(A、B 独立参与时的期望值) ]`，负值截断为 0。没有这一步，PageRank 会把「产量最高的媒体」误判为「影响力最大的媒体」。

⚠️ X 节点是「瘦」的（只有 ID 与时间戳，无正文无作者名）→ 图天然偏向 news / Reddit / Bluesky / 博客。对「媒体关系情报」这个用例可接受（重要的本来就是 outlets），但必须写进交付物的方法论说明；若未来批准 X rehydration（开放问题 #3），E1/E2 边会显著增厚。

### 15.3 前置依赖 G0：故事聚类管道（真正难的工程在这，不在 GNN）

**没有可靠的 story_id，后面全是空中楼阁。** 质量门槛：人工抽 50 个 story 检查 purity ≥85%，不达标不许进 G2。

```sql
-- 002_stories.sql
CREATE TABLE stories (
    story_id     BIGSERIAL PRIMARY KEY,
    t0           TIMESTAMPTZ NOT NULL,      -- 最早成员的 publish_date
    seed_title   TEXT,
    aspect       TEXT,                       -- 球场/阵容/比赛/管理层/其他（ABSA 或关键词规则打标）
    final_size   DOUBLE PRECISION,           -- 48h reach 加权总量（标签，t0+48h 后由 job 回填）
    n_docs       INT DEFAULT 0
);
CREATE TABLE story_members (
    document_id  TEXT PRIMARY KEY REFERENCES mentions(document_id),
    story_id     BIGINT NOT NULL REFERENCES stories(story_id),
    lag_minutes  INT NOT NULL                -- publish_date - t0
);
```

流程（每 10 分钟随检测 job 增量运行）：
1. 新文档取 `title + 正文前 500 字` 做多语 embedding（`bge-m3` 或 `paraphrase-multilingual-mpnet`；X 无正文 → 不参与聚类，仅按时间挂到已存在的最近似 story 或独立计数）。
2. 与滚动 72h 窗口内的活跃 story 质心比对：`cosine ≥ 0.62`（起始值，按 purity 调）**或** 共享归一化 URL **或** 共享 ≥2 个命名实体 → 归入该 story；否则开新 story。
3. story 的 `final_size` 在 t0+48h 后由每日 job 回填——这就是 GNN 的标签，零人工标注成本。

### 15.4 图 Schema（异构图）

```sql
-- 003_graph.sql
CREATE TABLE graph_nodes (
    node_id      BIGSERIAL PRIMARY KEY,
    node_key     TEXT UNIQUE NOT NULL,       -- 'source:theathletic.com' / 'author:reddit:u_xxx' / 'subreddit:NewEnglandRevolution'
    node_type    TEXT NOT NULL,              -- source | author | subreddit
    features     JSONB                       -- 历史量、均值 reach、aspect 分布、活跃时段、source_type
);
CREATE TABLE graph_edges (
    src BIGINT, dst BIGINT, etype TEXT,      -- e1_cite | e2_struct | e3_precede
    weight DOUBLE PRECISION,
    window_month DATE,                       -- 边按月版本化，滚动 12 个月重建（非平稳性）
    PRIMARY KEY (src, dst, etype, window_month)
);
CREATE TABLE amplifier_scores (
    node_id BIGINT, month DATE, method TEXT, -- pagerank | attribution
    score DOUBLE PRECISION, aspect_affinity JSONB, typical_lag_min INT, hit_rate DOUBLE PRECISION,
    PRIMARY KEY (node_id, month, method)
);
```

Story 节点不入 `graph_nodes`——story 在训练时动态构造为「早期采用者子图 + 时间特征」的样本，避免图无限膨胀。

### 15.5 分级建模 G1–G4（必须按序，禁止跳级）

**G1 图基线（无训练，第 3 周即可交付）**：在 E1+E2+E3 合成图上跑加权 PageRank + k-core + 出度 → **放大者名单 v0**。这已经是可以给高管看的交付物。

**G2 GBDT 基线（GNN 的 beat-me 基准）**：给 Phase 4 的 spike/规模模型追加图特征——故事前 30 分钟早期采用者的：PageRank 之和、watchlist top-20 命中数、历史放大力均值、跨 source_type 熵、E1 引用边是否已出现。目标改为回归 `log(final_size)` + 分类 `top-decile`。

**G3 静态异构 GNN**：
- 自监督预训练：在异构图上做边预测/对比学习（PyG 的 `HeteroConv` + GraphSAGE 或 HGT），得到每个节点 64–128 维 embedding。
- 级联头：对「前 30 分钟早期采用者的 embedding 集合」做 attention pooling，拼接时间特征（采用速度、lag 分布、aspect、是否 matchday）→ 小 MLP 双头输出（log 规模回归 + top-decile 分类）。
- **上线判据：G3 相对 G2 的 Spearman 相关或 precision@k 提升 ≥10%，否则生产模型就是 G2**（G2 也已经在用图了，这不丢人）。

**G4 时间图 TGN/TGAT（选做）**：把每条 (节点, story, t) 当事件流建模。仅当 G3 明显胜出且仍有余力时做。

评估纪律（与 Phase 4 相同）：时间切分；指标 = Spearman(预测 vs 实际 log size)、top-decile precision@k、以及「30 分钟时点预测 vs 6 小时时点预测」的增益曲线。

### 15.6 影响力归因 → 放大者名单 v1

- 方法：**反事实扰动**——对每个候选节点，把它从各故事的早期采用集合中移除，计算模型预测规模的平均下降 Δ；Δ 即该节点的影响分（attribution）。
- 与 G1 的 PageRank 名单对比：两榜取并集人工审一遍（30 分钟的事），分歧大的节点单独看案例。
- 名单字段：节点、类型、影响分、aspect 亲和（球场/阵容/…各占比）、典型滞后（它一般多快跟进）、历史命中率（它早期出现的故事中最终成为大故事的比例）。
- 月度刷新 job（随 12.2 的维护 job 一起跑）；产出进 mission control（watchlist 命中提示）+ 高管月报（「Everett 议题的关键放大者」专栏）。

### 15.7 工程与算力

- 栈：PyTorch Geometric + sentence-transformers；本图规模（数千～数万节点、数十万边）**CPU 即可训练**，跑在大规格 ACA Job 或开发机上；模型与 node embedding 产物存 Blob。
- 推理零负担：embedding 与名单是月度预计算的，在线只有级联头的小 MLP，直接嵌进 10 分钟检测 job。
- 嵌入/聚类推理（G0 的 embedding 计算）是持续成本，量小（日均数千条），CPU batch 即可。

### 15.8 GNN 专属陷阱清单

1. 时间先行 ≠ 因果，PMI 去偏是硬性步骤（15.2）。
2. 泄漏：特征窗严格 `[t0, t0+30min]`，标签窗严格 `(t0+30min, t0+48h]`；复用 `assert_no_future_leak()`。
3. 故事聚类 purity <85% → 停下修聚类，禁止带病训练。
4. 冷启动节点（新账号/新媒体）：回退到 node_type 级平均 embedding。
5. 单队故事量不够（Revs 一年约数百～两千个有效 story）→ 全 MLS + 波士顿四大联合训练（既有军规），Revs 场景微调。
6. 边按月版本化、滚动 12 个月重建；训练/评估必须使用「当时可见」的边版本，不能用未来的图。

### 15.9 里程碑与验收

| 里程碑 | 时间 | 验收 |
|---|---|---|
| G0 故事聚类 | 2 周 | purity ≥85%（50 story 人工抽检）；stories/story_members 回填完历史 |
| G1 名单 v0 | 第 3 周 | PageRank 榜单产出并经社媒团队 sanity check（「榜上的名字眼熟吗」） |
| G2 图特征基线 | 第 4–5 周 | 时间切分回测报告；图特征相对 Phase 4 纯时序特征有可测提升 |
| G3 异构 GNN | 第 6–8 周 | 达到/未达 10% 判据都要出结论报告；达标则替换生产 |
| G4 归因名单 v1 + 闭环 | 第 9–10 周 | watchlist 特征进 spike 模型；月度刷新 job 上线；月报专栏首发 |


---

## 16. 转会绯闻知识图谱（Transfer Rumor Graph，阶段 A 正式项目）

### 16.1 定位、价值与时机

- **与第 15 章的关系**：15 章是**故事级传播图**（谁放大了什么内容）；本章是**实体级知识图谱**（哪个球员被传去哪、谁在报、有多热）。Media 节点两图共享（`graph_nodes`），放大力与可信度互相印证。
- **受众价值**：高管/管理层——引援与流失叙事的全景图 + 数据化的媒体可信度；社媒团队——绯闻热度即互动与关注时机；品牌侧——inbound 大牌绯闻的粉丝兴奋度是票务/会员的先行信号。
- **完全在阶段 A 纯监听范围内**：只读全世界的报道，不发布任何内容。
- **时机**：2026 赛季 MLS 二级转会窗为 7 月 13 日–9 月 2 日（二十年来首次延至 9 月、与欧洲窗对齐），主窗为 1 月 26 日–3 月 26 日。系统上线即在窗内，立刻有真实数据可跑。窗口日期每季 🔍 核实 MLS 官网。

### 16.2 实体与表结构

Rumor 建模为**超边节点**：`(player, from_club, to_club, direction)`，媒体通过带时间戳与立场的边连接到 rumor。

```sql
-- 004_transfer.sql
CREATE TABLE clubs (club_id BIGSERIAL PRIMARY KEY, canonical TEXT UNIQUE, aliases TEXT[], league TEXT, country TEXT);
CREATE TABLE players (
    player_id BIGSERIAL PRIMARY KEY, canonical TEXT NOT NULL, aliases TEXT[],
    current_club BIGINT REFERENCES clubs(club_id), position TEXT,
    dict_source TEXT, updated_at TIMESTAMPTZ DEFAULT now());        -- roster | rumor_added
CREATE TABLE media_outlets (
    outlet_id BIGSERIAL PRIMARY KEY, canonical TEXT UNIQUE, aliases TEXT[],
    domain TEXT, otype TEXT, language TEXT,                          -- outlet | journalist
    prior_tier INT);                                                 -- 用户人工分层（可信度先验）
CREATE TABLE rumors (
    rumor_id BIGSERIAL PRIMARY KEY,
    player_id BIGINT NOT NULL REFERENCES players(player_id),
    from_club BIGINT REFERENCES clubs(club_id), to_club BIGINT REFERENCES clubs(club_id),
    direction TEXT NOT NULL,                                         -- inbound | outbound | other
    first_seen TIMESTAMPTZ NOT NULL, first_outlet BIGINT,
    stage TEXT NOT NULL DEFAULT 'speculation',                       -- speculation→interest→talks→advanced→done
    status TEXT NOT NULL DEFAULT 'open',                             -- open | confirmed | denied | expired
    transfer_window TEXT,                                            -- '2026-secondary' 等
    UNIQUE (player_id, to_club, transfer_window));
CREATE TABLE rumor_mentions (
    document_id TEXT PRIMARY KEY REFERENCES mentions(document_id),
    rumor_id BIGINT NOT NULL REFERENCES rumors(rumor_id),
    outlet_id BIGINT, stance TEXT,                                   -- report | advance | deny | confirm
    reported_at TIMESTAMPTZ NOT NULL);
CREATE TABLE rumor_heat_hourly (
    rumor_id BIGINT, hour TIMESTAMPTZ, cnt INT,
    reach_sum DOUBLE PRECISION, cred_weighted DOUBLE PRECISION,
    PRIMARY KEY (rumor_id, hour));
```

### 16.3 抽取管道（每 10 分钟随检测 job 增量运行）

1. **候选检出**：mention 命中转会词表（英：linked / target / bid / transfer fee / agree terms / medical / here we go…；西：fichaje / traspaso / cerca de…；葡：contratação / acerto / a caminho…。词表放 config，可增补）。
2. **实体链接**：词典优先——`players.aliases` + `clubs.aliases` + `media_outlets.aliases`（用户名单）精确/模糊匹配；词典未命中的人名走 NER 兜底并进**待审队列**（人工每日 10 分钟清一次，确认后入词典）。
3. **Rumor 分类**：起步用 LLM 弱标注（三问：是否转会传闻？方向？阶段？含否认识别）；攒到 ~2000 条标注后蒸馏成本地小模型（省 API 成本与延迟）。
4. **归组与阶段机**：`(player_id, to_club, 当前窗)` 相同 → 同一 rumor，UPSERT。阶段机**只进不退**：speculation→interest→talks→advanced→done；`denied` 后仍监控 14 天（转会新闻反转常见）；60 天无新提及 → `expired`。
5. **热度回填**：`rumor_heat_hourly` 随 rollup job 增量维护。

### 16.4 热度与媒体可信度评分（本章核心交付）

- **热度**：`heat(r,h) = Σ log1p(reach)`；**可信度加权热度** `cred_heat` 按 outlet 权重加权——高管榜单默认按 cred_heat 排序，避免小报刷屏霸榜。
- **媒体可信度（贝叶斯更新）**：先验 = 用户的人工分层 `prior_tier` 映射为 Beta 先验；每个转会窗结束后，用成交结果更新后验：`precision(outlet) = 该 outlet 报道过且最终官宣成交的 rumor 数 / 它报道过的 rumor 数`，并区分**首报命中率**与跟进命中率，另计 **lead time**（首报 → 官宣的天数）。
- **Ground truth（官宣检测）**：规则检测俱乐部/联盟官方渠道的官宣关键词（"sign", "acquire", "transfer completed", roster move 公告），每窗结束后人工核对一遍（每窗几十条 rumor，约 1 小时工作量）。
- ⚠️ **措辞纪律**：对外交付物一律说「历史命中率 / lead time」，**不说「该媒体报道为真/假」**——我们度量的是历史表现，不裁决单条新闻真伪。

### 16.5 数据获取与配额

- 新建 **S5_TRANSFER** saved search：`(Revs 词 OR 现役球员名 OR 已知绯闻球员名) AND 转会词表(英/西/葡)`。西语/葡语来源必须覆盖——MLS 引援大量来自南美，当地媒体往往先爆料（embedding 侧 bge-m3 本就多语，无额外成本）。
- **窗口自适应轮询**：窗内每小时一次（并入 4.4 预算，约 +16 次/天，从预留与平日节奏里腾挪）；窗外每日一次。
- ⚠️ recurring export 单个最多挂 5 个 search，S1–S4 已满 → S5 需要**第二个 recurring export**（🔍 核实套餐是否允许多个 recurring export；不允许则 S5 的对账用每日 one-time export 代替）。
- 词典维护：Revs 现役名册每转会窗后更新（🔍 MLS/俱乐部官网）；绯闻球员经待审队列动态入典。

### 16.6 交付物

1. **Rumor Board**（mission control 新栏）：活跃 rumor 按 cred_heat 排序，火花线热度曲线、方向（in/out）、阶段、首报媒体、最新动态。
2. **窗内周报（高管版）**：本周 top rumors、热度变化、谁在推动、否认与反转。
3. **媒体可信度榜**：每窗结束刷新；「用户人工分层 vs 数据后验」对照表本身就是给管理层看的亮点。
4. **热度×情绪联动**：inbound 大牌绯闻的粉丝兴奋度曲线（正面情绪份额），供品牌/票务参考。

### 16.7 本章陷阱清单

1. **实体消歧是最大的工程量**（不是图也不是模型）：同名球员、常用词姓名（如 "Gil"）、多语转写。铁律：词典优先 + 待审队列，禁止纯 NER 裸奔入库。
2. **X 起源偏差**：大量记者在 X 首发，无 rehydration 时系统看到的是新闻转述，「首报归因」会偏向 news outlets——写进方法论说明；开放问题 #3（X rehydration）若批准可显著修复。
3. 阶段机不许倒退；`denied ≠ 结束`。
4. 单窗样本少：materialization 概率预测模型（T4，选做）必须用全 MLS 数据训练，且样本量注定有限——定位为参考分，不做强承诺。
5. 转会词表若只有英文，会漏掉最早的南美信号——多语词表是硬要求。

### 16.8 里程碑

| 里程碑 | 时间 | 验收 |
|---|---|---|
| T0 词典就绪 | 3 天 | 用户媒体名单（开放问题 #7 格式）入库；Revs 名册 + MLS 俱乐部词典建好 |
| T1 抽取管道 | +1.5 周 | S5 上线；rumor 表开始积累；待审队列日清 |
| T2 Rumor Board + 周报 | 第 3 周 | 首份窗内周报交付（本窗 9/2 结束前即可见效） |
| T3 可信度榜 v1 | 窗口结束后 1 周 | 官宣核对完成；先验 vs 后验对照表交付 |
| T4 成交概率模型（选） | 下一窗前 | 全 MLS 训练；时间切分回测报告 |

### 16.9 转会图谱上的 ML / GNN / AI 路线图（按可信度分三档）

> 通用军规（全部适用）：全 MLS 数据训练（单队样本太少）；一律时间切分 + 按「转会窗」切分回测；所有概率输出必须做校准（Platt/isotonic + Brier 分数 + 可靠性曲线）；对外措辞一律「参考概率/历史表现」，不做真伪与成交裁决；全部为监听侧分析，符合 1.5 阶段 A 范围。

#### 档一：生产级（按此顺序做）

**M1 成交概率 = 生存分析（本章旗舰，取代朴素二分类）**
- 为什么是生存分析：rumor 有天然的删失（censoring）——窗口关闭、rumor 过期时结局未观测，二分类会把删失当负样本引入偏差；生存框架还能同时回答「概率多大」和「大概多久」。
- 实现：离散时间 hazard 模型（每个 rumor-day 一行，logistic hazard，天然支持时变协变量：新增报道、阶段跃迁、否认事件）起步；进阶用 XGBoost-AFT / 梯度提升生存模型。
- 特征：可信度加权的报道证据（哪些 tier 的媒体报了、首报是谁）、阶段推进速度、多源独立确认数、跨语言 pickup（南美源+本地源同时在报=强信号）、热度轨迹形态、否认后反弹。
- 评估：time-dependent C-index + 「窗口截止前成交」的校准概率。交付：Rumor Board 增加 P(成交) 列与预计时间线。

**M2 媒体可信度 2.0 = 分层贝叶斯 / IRT 模型（从计数升级为建模）**
- 痛点：单窗每家媒体样本极少，朴素命中率方差巨大；且「报中一桩本来就板上钉钉的交易」不该与「首报冷门交易并命中」同分。
- 方案：IRT 式建模——outlet 能力 θ × rumor 难度 b（先验冷门程度，用首报前热度/阶段估计），分层贝叶斯（PyMC/numpyro）做媒体间部分池化（partial pooling），journalist 嵌套于 outlet 的层级结构。
- 交付：每家媒体的能力后验 **带置信区间**（对高管展示不确定性本身就是可信度的体现）；可按语境条件化（对 MLS 交易 vs 欧洲交易的能力可以不同）。

**M3 抽取层的正经 NLP（已规划的蒸馏，落实为硬指标）**
- 立场/关系抽取小模型（多语）：从 LLM 弱标注蒸馏，holdout macro-F1 ≥0.85 才准替换 LLM。
- 学习型实体链接器替代纯词典兜底：bi-encoder 召回 + cross-encoder 重排，目标是把待审队列日均量压掉 70%。

#### 档二：高价值分析型

**M4 rumor 热度轨迹预测**：直接复用第 15 章级联头（early adopters → 峰值时间/量级/衰减），rumor 当作一种特殊 story。
**M5 Hawkes 过程 × 媒体分支比（两张图在此合流）**：把每条 rumor 的报道流建为多元 Hawkes 过程，估计每家媒体的 branching ratio——「谁的报道会引发跟进潮」。这是第 15 章放大力在转会语境下的因果味增强版，直接写进可信度榜。
**M6 协同推动检测（agent 放料识别，独有情报价值）**：无监督异常检测识别「疑似有组织推动」的 rumor——特征：爆发同步性（报道时间 Δt 聚集）、可信度结构异常（低 tier 密集而 48h 内无 tier-1 跟进）、文本近重复率（embedding 余弦 >0.9 的簇占比）、单语言起源无跨语言 pickup。输出「协同推动可能性」标记 + 人工复核。⚠️ 措辞：概率标记，绝不指控任何主体。

#### 档三：研究向 / stretch（诚实定位：探索）

**M7 知识图谱链接预测（下一个绯闻从哪来）**：HGT/RotatE 学 club–player 嵌入，预测哪些 (球员, 俱乐部) 组合可能成为新 rumor；评估 = 在下一窗上验证 Hits@k。⚠️ 定位纪律：这是「媒体叙事亲和度」，**不是球探工具**——我们用的是媒体数据，不是球员能力数据；交付为 watchlist 种子，不进任何引援评估语境。
**M8 时间图 TGN 做阶段跃迁预测**：预测下一个 stance/stage（含「否认后反转」模式识别——denied→confirmed 的历史模式）。
**M9 球迷接受度预测**：给定球员画像（联赛来源、位置、赛前声量代理的球星级别）与 rumor 语境，预测「若交易推进，球迷情绪分布如何」。训练自历史 MLS inbound rumor 的情绪反应。定位：品牌与传播预案输入，不进球探/引援决策语境。

#### 落地顺序
M3（抽取质量是一切上限）→ M1（旗舰）→ M2（可信度 2.0）→ M5/M6（合流与情报）→ M4 → M7–M9 按「生产 vs 作品集」定位取舍（开放问题 #5）。

*（完）*
