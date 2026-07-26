# Revs Media Intelligence & Prediction System — Complete Architecture Design & Implementation Guide

> **Document version**: v1.0 (2026-07-25)
> **Data source**: Meltwater API (Export / Search / Analytics permissions only, **no Data Streams, no Meltwater MCP**)
> **Serving**: New England Revolution (MLS soccer club, hereafter "Revs") social media team lead + executive leadership
> **Purpose of this document**: The single authoritative guide (single source of truth) handed over to the executing agent. The executing agent should implement strictly according to this document; when encountering situations this document does not cover, first log them under "Open Questions" and then confirm with the user — do not improvise.

---

## 0. Reading Guide for the Incoming Agent (Must Read)

### 0.1 Who You Are and What You're Doing

You are the executing agent taking over this project. Your task is to build, from scratch, a "media monitoring + machine learning prediction + business insight delivery" system based on Meltwater API data. This document has already done all the research and architecture decisions for you; you only need to **execute in Phase order**.

### 0.2 Rules for Using This Document

1. **Execute strictly in Phase order** (Phase 0 → 1 → 2 → 3 → 4 → 5). Each Phase ends with an acceptance checklist (Definition of Done); only when every box is checked may you proceed to the next Phase.
2. **When you encounter a `⚠️ Pitfall` marker, you must stop and read it in full.** These are real API traps; stepping on them wastes quota or produces dirty data.
3. **When you encounter a `🔍 Verify` marker, go check the specified documentation URL before writing code.** API details may have been updated; where this document hard-codes endpoints, the official docs take precedence.
4. **When you encounter a `❓ Ask the user` marker, stop and confirm with the user** — do not guess.
5. All terms are defined in the Appendix B glossary. If you don't understand a word, look it up — do not skip it.

### 0.3 Hard Behavioral Rules (DO / DON'T)

**DO:**
- All data persisted to disk goes into a database (Postgres preferred; SQLite is fine for local development) or Parquet files.
- All calls to the Meltwater API must go through the "quota guard" module (see Phase 2 step 2.2): check the budget first, then call.
- All times in code are stored in UTC; convert to `America/New_York` only at the presentation layer.
- After every API call, write the request parameters, response status, and result count into the `api_call_log` table (audit + quota accounting).
- All DB access must obey Chapter 14's connection budget (hard cap of 10 concurrent connections to the same database): one engine per process, Jobs must call `engine.dispose()` on exit, and `application_name` must always be set.

**DON'T:**
- **Never save data as CSV files** (explicit user preference; the only exception is when the user explicitly requests CSV). Meltwater export templates likewise always use JSON (`api.json`), never the CSV template.
- Never pull data raw without a watermark mechanism (it repeatedly wastes quota).
- Never evaluate any time-series model with a random split; always use a temporal split.
- Never write the API key into code or commit it to git; always use the environment variable `MELTWATER_API_KEY`.
- Never put any RL/bandit policy live on a real account before doing off-policy evaluation.

---

## 1. Project Background & Goals

### 1.1 Client & Audiences

| Audience | Role | What they want | Time granularity |
|---|---|---|---|
| Audience A | Revs social media team lead | Operational signals: what's blowing up right now, whether to escalate, whom to watch closely | Minutes to hours |
| Audience B | Revs executive leadership | Strategic metrics: brand health, share of voice, stadium-project sentiment, sponsorship value | Daily to monthly + real-time in a crisis |

**Core principle: two audiences = two sets of deliverables.** Do not try to satisfy both sides with a single dashboard (details in Chapter 7).

### 1.2 Key Business Context (context you must reference when writing insights)

1. **The Everett stadium project is currently the highest-value public-sentiment topic.** Background facts: Kraft Group (Revs' parent company) reached a formal agreement with the City of Everett and the City of Boston on 2025-12-31 to build an approximately 25,000-seat, roughly $500 million soccer-specific stadium on a decommissioned power-plant parcel along the Mystic River; the project still needs 12–18 months of permitting and environmental review; community opinion will directly affect the terms of the Community Impact Agreement (CIA). **This means Everett/Boston local sentiment is not a PR vanity metric — it is a business variable that directly affects the approval process.**
2. The Revs have shared Gillette Stadium in Foxborough with the NFL's Patriots since 1996; the new stadium is a club-level strategic undertaking.
3. Brand competitive benchmark: Boston's Big Four (Patriots / Celtics / Red Sox / Bruins) + MLS peers.
4. One of the main battlegrounds of sports social-media discussion is X (Twitter), but the Meltwater API only returns tweet IDs (see 2.3 Pitfall #5).

### 1.3 Project Goals (ranked by ROI; do 1 and 2 first)

| # | Project | Audience | One-line definition | Priority |
|---|---|---|---|---|
| 1 | Spike Early Warning | A | Predict whether the current discussion wave will become a major spike in the next 2–6 hours | P0 |
| 2 | Narrative & sentiment trend tracking (incl. Everett stadium dashboard) | B | Sentiment trends broken down by region/stakeholder + 7-day forecast | P0 |
| 3 | Share of Voice competitive benchmark | B | Revs vs. Boston Big Four + MLS volume/sentiment comparison and trends | P1 |
| 4 | Amplification network & cascade-size prediction (GNN) | A+B | Inferred amplification network; early prediction of a story's final size; key-amplifier watchlist | P1 (detailed design in Chapter 15) |
| 5 | [Stage B] Posting impact evaluation & content scoring | A | Causal evaluation of "what impact would posting have" and what-if scoring | Stage B (not implemented now; see 1.5) |
| 6 | Transfer Rumor Graph | A+B | Player × club × media rumor-heat graph + media credibility scoring | P1 (detailed design in Chapter 16) |

### 1.4 Success Criteria

- MVP (end of Phase 3): rule-based spike alerting is live, and the social media team has received at least 1 early alert in Slack that was "confirmed useful after the fact."
- V1 (end of Phase 4): the ML alert's precision@k and average lead time beat the rule-based version; the Everett sentiment dashboard updates automatically every day.
- Long term: the monthly executive scorecard enters regular meeting materials; at least 1 insight gets cited in an actual decision.

### 1.5 Project Scope Statement (Stage A / Stage B — a high-misunderstanding zone; must read)

- **Stage A (current; the body of this document) = pure listening & analysis.** The club **does not publish any posts** at this stage; this system only consumes Meltwater's earned media data, performing monitoring, prediction, and insight delivery on "what the whole world is saying about the team." All deliverables are **information for humans** (alerts, dashboards, reports, lists); the system contains no publishing, replying, or auto-engagement features, and gives no "post at X o'clock / post Y" style instructions.
- **Stage B (future; a separate project) = posting impact evaluation & decision support.** If the club considers posting in the future, the first question to answer is "**if we publish a post, what impact will it have**" — this is a **causal evaluation problem** (see B0 in Phase 5), not an optimization problem. Only if the impact is measurable and positive do we discuss bandit/DPO-style posting optimization. For anything marked [Stage B] in this document, the current policy is: keep the design, write no code, invest nothing.
- **Decision rule for the executing agent**: any requirement involving owned social data, posting suggestions, content generation, or auto-replies → check against this section first; if it belongs to Stage B, park it and log it in Chapter 10 Open Questions.

---

## 2. Key Constraints (They Determine the Entire Architecture — Read First)

### 2.1 Purchased vs. Not-Enabled Capabilities

| Capability | Status | Impact on architecture |
|---|---|---|
| Saved Searches management | ✅ Have | The entry point for all data acquisition |
| One-time Export | ✅ Have | Historical backfill for training data |
| Recurring Export | ✅ Have | Daily reconciliation layer (minimum frequency = daily) |
| Search (pull small batches of mentions) | ✅ Have | The workhorse endpoint of the near-real-time polling layer |
| Analytics | ✅ Have | Aggregated metrics (SOV, top sources, etc.) |
| **Data Streams (streaming/webhook push)** | ❌ Not enabled | **Substitute with "adaptive polling + Alert triggering"** (Chapters 4 & 5) |
| **Meltwater MCP / Mira MCP** | ❌ Not enabled | **Substitute with a self-built FastMCP tool layer** (Chapter 6) |
| Owned Social API | ❓ Unconfirmed | Needed only in Stage B (see 1.5); blocks nothing right now |

> Strategic note: run the polling version first to prove value, accumulate data like "we actually consume X calls per day, and alerts average Y hours of lead time," then decide whether to purchase Data Streams — go negotiate with the account manager armed with usage data.

### 2.2 Rate Limits & Quotas (quota is this system's #1 design variable)

The following comes from documentation research; **you must verify your own contract's actual numbers before executing**:

| Limit | Value | Notes |
|---|---|---|
| Analytics/Search instantaneous rate limit | 5 req/sec, 100 req/min | All earned media analytics endpoints |
| Analytics/Search daily total quota | Per contract (the inclusive tier is only 50/day; paid packages commonly 100+/day) | **Search calls count against the analytics daily quota** |
| Export endpoint rate limit | 20 req/min | |
| Single one-time export cap | 2 million documents | Controllable via the sampling parameter |
| Recurring export minimum frequency | Daily (DAY), no hourly tier | Executes 30 minutes after the window closes |
| Analytics single-query time window | Default max 12 months (contract governs) | |
| Concurrent Data Streams | N/A (not purchased) | |

🔍 Verify: the very first step of Phase 0 is calling the usage endpoint (`GET .../usage/me/requests`; exact path see https://developer.meltwater.com/guides/getting-started/accessing-usage-statistics ) to find your real limits and current usage, fill the numbers into this table, and only then continue.

### 2.3 Meltwater Data Characteristics & the Five Pitfalls

**Data ingestion model**: The Meltwater platform itself continuously crawls/ingests data (3M+ traditional-media articles per day) into a central data store; **your API calls do not trigger crawling** — they only read from this store. Ingestion has latency, and Meltwater does not officially guarantee an article is captured the moment it's published.

**⚠️ Pitfall #1 — Late and duplicate documents**: The same article can appear multiple times because of "ingestion delay / publisher edits & republishes / source-list changes triggering re-crawls," and `document_publish_date` can be up to 31 days earlier than the current time.
→ Countermeasure: all writes UPSERT by `document_id` (overwrite if exists); all feature computation uses event time (publish_date), never arrival time.

**⚠️ Pitfall #2 — The 30-minute ingestion buffer**: recurring exports execute 30 minutes after the time window closes; this is Meltwater's implicit commitment about "when a period's data can be considered complete."
→ Countermeasure: when the polling layer pulls "recent" data, treat data before `now - 30min` as essentially stable, and mark data in `now-30min ~ now` as provisional, to be overwritten in the next cycle.

**⚠️ Pitfall #3 — Recurring exports get silently cancelled**: if nobody accesses the data_url for 30 days, the recurring export is auto-cancelled.
→ Countermeasure: the reconciliation job's once-daily access naturally satisfies this; also add a weekly inspection task that checks export status.

**⚠️ Pitfall #4 — Export data is deleted after 30 days**: one-time export result files are deleted 30 days after execution.
→ Countermeasure: during backfill, ingest into the DB immediately after downloading; never treat data_url as long-term storage.

**⚠️ Pitfall #5 — X/Twitter has only IDs, no body text**: due to X's terms, the API returns only tweet IDs; the body must be completed yourself via the X API (rehydration), and the X API is paid.
→ Countermeasure: Phases 1–4 must **never depend on X body text**. Primary signal sources = news + Reddit + Bluesky + blogs + other social sources with obtainable text; X is used only for "count signals" (mention volume, timestamps, author counts). Whether to purchase the X API for rehydration is a ❓ Ask-the-user budget decision.

### 2.4 Coding Standards Summary

- Python 3.11+; HTTP via `httpx`; DB access via `SQLAlchemy 2.x` + `psycopg`; scheduling via `APScheduler` (simple) or cron.
- Configuration centralized in `config.py` + environment variables; secrets read only from environment variables.
- Every module independently runnable (in the `python -m pipeline.backfill` style).
- Logging via `structlog` or standard logging, JSON-formatted output.
- **To emphasize once more: no CSV output.** Intermediate data → database; ML feature snapshots → Parquet; reports → Markdown/HTML.

---

## 3. Meltwater API Hand-Holding Quick Reference Manual

### 3.1 Authentication

All requests carry the header: `apikey: $MELTWATER_API_KEY`. Base URL: `https://api.meltwater.com`.
Tokens are created inside the Meltwater app (Developer Portal → API Credentials).

```python
# common/mw_client.py — the single exit point for all API calls
import os, httpx

BASE = "https://api.meltwater.com"
HEADERS = {
    "apikey": os.environ["MELTWATER_API_KEY"],
    "Accept": "application/json",
    "Content-Type": "application/json",
}

def mw_request(method: str, path: str, **kwargs) -> httpx.Response:
    """The one and only Meltwater HTTP exit. No module may bypass this function to connect directly.
    Done centrally here: quota checks (see 5.3.4), retries, api_call_log persistence."""
    # TODO: quota_guard.check_and_reserve(path)  # implemented in Phase 2
    with httpx.Client(timeout=60) as c:
        r = c.request(method, BASE + path, headers=HEADERS, **kwargs)
    # TODO: log_api_call(path, r.status_code, ...)  # write to the api_call_log table
    r.raise_for_status()
    return r
```

### 3.2 Core Endpoint List (the verified portion)

| Purpose | Method & path | Key parameters |
|---|---|---|
| List saved searches | `GET /v3/searches` | — |
| Create one-time export | `POST /v3/exports/one-time` | `search_ids`, `start_date`, `end_date` (UTC, ISO8601), `template{name:"api.json"}`, `sample{count,percentage}` |
| Check one-time export status | `GET /v3/exports/one-time/<export_id>` | Status `PENDING`→`FINISHED`; when finished, download the JSON from `data_url` |
| Create recurring export | `POST /v3/exports/recurring` | `window_time_unit` (`DAY`/`WEEK`/`MONTH`), `window_size`, `window_time`, `timezone`, `template` |
| Check recurring export | `GET /v3/exports/recurring/<export_id>` | After status `ACTIVE`, the data_url is continuously overwritten and refreshed |
| List custom categories | `GET /v3/custom_categories` | Usable for categorization/filtering at export time |

🔍 Verify (mandatory before writing code): the exact paths and parameters of the following endpoints are governed by the official pages — open them in a browser and check:
- Search mentions (polling-layer workhorse): https://developer.meltwater.com/guides/listening/searching-mentions
- Analytics: https://developer.meltwater.com/guides/listening/analyzing-mentions
- Managing searches: https://developer.meltwater.com/guides/listening/managing-searches
- Usage statistics: https://developer.meltwater.com/guides/getting-started/accessing-usage-statistics
- Output template field definitions: https://developer.meltwater.com/api-reference/templates/overview

### 3.3 Data Flow Model (one-sentence version)

**Everything starts from a Saved Search**: first there is a Boolean-query saved search (created in-app or via API), then you take its `id` and do three things with it — export (bulk-pull full documents), search (pull small batches of documents), analytics (pull aggregated metrics).

### 3.4 One-time Export In Depth (for historical backfill)

- `start_date`/`end_date` must be UTC ISO8601 (e.g. `2025-01-01T00:00:00Z`); the window includes the start and excludes the end.
- Result cap of 2 million documents; anything beyond gets sampled down to 2 million. You can proactively control this with the `sample` parameter.
- Asynchronous: after creation it enters a queue, taking anywhere from a few minutes to 1 hour; poll the status until `FINISHED`, then download `data_url`.
- Template is always `{"name": "api.json"}` (JSON with all fields; **do not use the CSV template**).
- Returned JSON structure: `{"request": {...}, "docs": [ {per-document object} ]}`.

### 3.5 Recurring Export In Depth (for the reconciliation layer)

- Frequency has only three tiers: `DAY` / `WEEK` / `MONTH`. `window_size` = how many units of data each run includes.
- This project's configuration: `window_time_unit=DAY, window_size=2` (runs daily, each run covers the last 2 days) → creates a 1-day overlap that catches late-arriving documents.
- Execution time = 30 minutes after the window closes. Each run **overwrites** the same data_url.
- A single export can attach at most 5 saved searches.

### 3.6 Document-Object Fields You Will Use (api.json template; field names governed by the template docs)

The minimum fields to map into the DB: `document_id` (dedup primary key), `document_publish_date`, URL, title, body (news/blogs/Reddit have it; X does not), source name & type, author, reach/exposure estimate, engagement metrics, Meltwater's built-in sentiment, country/language, matched keywords.
🔍 Verify: cross-check field by field against the templates/overview page before writing the ORM mapping; do not write field names from memory.


---

## 4. Overall Architecture

### 4.1 Architecture Diagram

```text
┌──────────────────── Meltwater platform (continuous crawling, ~3M docs/day) ────────────────────┐
│   Central data store (news / blogs / Reddit / Bluesky / X-ids / ...)                           │
└──────┬──────────────────────────┬──────────────────────────┬───────────────────────────────────┘
       │ Tier 3 (one-time)        │ Tier 1 (near-real-time)  │ Tier 2 (daily)
       ▼                          ▼                          ▼
  One-time Export           Adaptive polling of the      Recurring Export (DAY, size=2)
  12–24 months history      Search endpoint              Daily reconciliation; fixes
  backfill                  10min–1h dynamic cadence     misses & duplicates
       │                          │        ▲                 │
       │                          │        │ trigger         │
       │                          │   Meltwater Alert        │
       │                          │   → Slack channel        │
       │                          │   → event listener       │
       └──────────────┬───────────┴──────────────────────────┘
                      ▼  everything UPSERTed by document_id
        ┌─────────────────────────────────────┐
        │  PostgreSQL (single source of truth)│
        │  mentions / watermarks / api_call_log│
        │  features / predictions / alerts    │
        └───────┬──────────────┬──────────────┘
                ▼              ▼
        Feature engineering   Rule-based detection (z-score)  ──►  Slack alerts (social media team)
        (rolling windows)
                ▼
        ML layer (GBDT → DL/RL advanced track)
                ▼
   ┌────────────────────┬──────────────────────┐
   ▼                    ▼                      ▼
 Mission Control     Executive Scorecard    Self-built Agent layer (FastMCP)
 (social team, live) (monthly + crisis push) local DB first / API fallback
```

### 4.2 Division of Labor Across the Three Data-Acquisition Tiers (memorize this mental model)

| Tier | Mechanism | Frequency | Role | Latency |
|---|---|---|---|---|
| Tier 1 | Search endpoint polling | Adaptive, 10 minutes – 1 hour | Near-real-time signal; feeds spike detection | Minutes |
| Tier 2 | Recurring export | Once daily (2-day window) | Truth layer: reconciliation, gap-filling, corrections | T+1 |
| Tier 3 | One-time export | Backfill only | Training set: 12–24 months of history | One-off |

**Why this design**: streaming not purchased, and the search endpoint eats the daily analytics quota → polling must be used frugally (adaptive cadence + event triggering); polling inevitably misses things, so a daily export backstops it; ML needs long history, so a one-time backfill. The three tiers complement one another; none can be dropped.

### 4.3 Database Schema (Postgres DDL, directly executable)

```sql
-- 001_init.sql
CREATE TABLE mentions (
    document_id      TEXT PRIMARY KEY,          -- Meltwater dedup primary key
    search_id        BIGINT NOT NULL,            -- which saved search it came from
    publish_date     TIMESTAMPTZ NOT NULL,       -- event time (all analysis uses this)
    first_seen_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
    last_updated_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
    source_name      TEXT,
    source_type      TEXT,                       -- news / reddit / bluesky / twitter / blog ...
    url              TEXT,
    title            TEXT,
    body             TEXT,                       -- NULL for X (ID only)
    author           TEXT,
    reach            BIGINT,
    engagement       JSONB,                      -- per-platform engagement stored as-is
    mw_sentiment     TEXT,                       -- Meltwater's built-in sentiment
    custom_sentiment JSONB,                      -- self-trained ABSA results (filled in Phase 5)
    country          TEXT,
    language         TEXT,
    matched_keywords TEXT[],
    raw              JSONB NOT NULL,             -- the full raw document, guards against missed fields
    ingest_channel   TEXT NOT NULL               -- 'poll' | 'recurring' | 'backfill'
);
CREATE INDEX idx_mentions_pubdate ON mentions (publish_date);
CREATE INDEX idx_mentions_search_pub ON mentions (search_id, publish_date);
CREATE INDEX idx_mentions_srctype ON mentions (source_type);

CREATE TABLE watermarks (          -- per-search polling progress
    search_id     BIGINT PRIMARY KEY,
    watermark_ts  TIMESTAMPTZ NOT NULL,   -- the publish_date confirmed fully pulled up to
    last_poll_at  TIMESTAMPTZ
);

CREATE TABLE api_call_log (        -- quota audit (must write on every call)
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
    payload       JSONB,            -- top-mentions summary, etc.
    outcome       TEXT              -- post-hoc human label: 'useful' | 'noise' | NULL
);

CREATE TABLE predictions (
    id           BIGSERIAL PRIMARY KEY,
    created_at   TIMESTAMPTZ NOT NULL DEFAULT now(),
    model_name   TEXT NOT NULL,     -- 'zscore_v1' | 'gbdt_v1' | ...
    target       TEXT NOT NULL,     -- 'spike_6h' | 'sentiment_7d' ...
    search_id    BIGINT,
    horizon_end  TIMESTAMPTZ,
    value        JSONB,             -- predicted value/distribution
    features_ref TEXT               -- points to the Parquet feature-snapshot path
);
```

### 4.4 Daily Quota Budget Table (assumes daily analytics/search quota = 100 calls; adjust per your actual contract)

| Purpose | Budget | Notes |
|---|---|---|
| Tier 1 polling (4 search groups in rotation) | ≤ 60 calls/day | Every 10 minutes in matchday windows, hourly in daytime on regular days, off at night (0–7 ET) |
| Alert-triggered on-demand pulls | ≤ 15 calls/day | Event-driven; nearly 0 on quiet days |
| Analytics dashboards (SOV, etc.) | ≤ 15 calls/day | One fixed round of aggregate metrics per day |
| Reserved buffer | 10 calls/day | Manual debugging / agent fallback queries |

Quota-guard rules: once the day's usage is ≥ 90%, only Alert-triggered calls are allowed; at ≥ 100%, reject everything and notify the admin on Slack.


---
## 5. Phased Implementation Manual (Hand-Holding Level)

### Phase 0 — Preparation & Inventory (Day 1–2)

**Step 0.1 Obtain and validate the API token**
```bash
curl -s -H "apikey: $MELTWATER_API_KEY" https://api.meltwater.com/v3/searches | head
```
Pass = a JSON response containing a `searches` array. 401/403 → ❓ Ask the user for the correct token.

**Step 0.2 Check the real quotas**: call the usage endpoint (🔍 Verify the path), and record: the daily analytics limit, current usage, and export limits. **Backfill the numbers into the table in 2.2.**

**Step 0.3 Create the 4 groups of Saved Searches** (build in-app or via API; once built, record each `search_id` into `config.py`):

| Group | Name | Boolean query starting point (needs iterative tuning) |
|---|---|---|
| S1 | REVS_BRAND | `"New England Revolution" OR "NE Revolution" OR #NERevs OR ("Revs" NEAR/10 (soccer OR MLS OR Foxborough OR Gillette))` + key player names + head coach's name |
| S2 | STADIUM_EVERETT | `(("Everett" OR "Mystic River") NEAR/15 (stadium OR "soccer stadium")) OR ("Kraft" NEAR/10 (Everett OR stadium)) OR "Community Impact Agreement"` |
| S3 | COMPETITORS | Brand terms for Patriots / Celtics / "Red Sox" / Bruins (recommended: one search per team so SOV is computable; note that a single export attaches at most 5 searches) |
| S4 | SPONSORS_COMENTION | `(<sponsor brand terms>) AND ("New England Revolution" OR #NERevs)` — ❓ Ask the user for the sponsor list |

⚠️ Pitfall: the word `Revs` alone is highly ambiguous (engine revs, etc.); you must anchor the soccer context with the NEAR proximity operator. After writing a query, first run a 7-day preview in the Meltwater app and manually spot-check 50 items; if precision < 80%, keep adding exclusion terms. Coach and player rosters change — 🔍 Verify the current season's roster before filling them in.

**Step 0.4 Stand up basic infrastructure**: Postgres (Docker is fine) → run `001_init.sql` → create the Python project skeleton:
```text
revs-intel/
├── config.py            # search_ids, quota budgets, thresholds
├── common/mw_client.py  # the single API exit from 3.1
├── common/db.py         # SQLAlchemy engine + upsert helpers
├── pipeline/backfill.py # Phase 1
├── pipeline/poller.py   # Phase 2
├── pipeline/reconcile.py# Phase 3
├── detect/zscore.py     # Phase 3
├── ml/                  # Phase 4+
├── agent/               # Phase 6 (self-built MCP)
└── reports/             # scorecard generation
```

**Phase 0 acceptance**: ☐ token works ☐ quota numbers backfilled ☐ 4 search groups built with spot-check precision ≥ 80% ☐ database ready

---

### Phase 1 — Historical Backfill (Week 1)

Goal: load 12–24 months of S1–S4 historical data into the `mentions` table, as the foundation for the training set and baseline statistics.

**Step 1.1** Create one-time exports sliced by "each search × each month" (avoids a single export exceeding 2 million items and makes failure retries easy). Pseudo-flow:

```python
# pipeline/backfill.py (skeleton; field names per the 3.6 verification results)
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
        time.sleep(60)   # PENDING → check once per minute

def run_backfill(search_id: int, months: list[tuple[str, str]]):
    for start_iso, end_iso in months:
        eid = create_export(search_id, start_iso, end_iso)
        data = wait_and_download(eid)
        upsert_mentions(data["docs"], search_id=search_id, channel="backfill")
        # ⚠️ export endpoint rate limit is 20/min: monthly slicing naturally stays under, but don't blast it concurrently
```

**Step 1.2** The only correct way to write `upsert_mentions` (`ON CONFLICT (document_id) DO UPDATE`, updating `last_updated_at` and all content fields). `INSERT ... ON CONFLICT DO NOTHING` is forbidden — it drops article updates (Pitfall #1).

**Step 1.3** Backfill QA SQL (run all three and record the results in the handover notes):
```sql
SELECT search_id, date_trunc('month', publish_date) m, count(*) FROM mentions GROUP BY 1,2 ORDER BY 1,2; -- are monthly volumes continuous, any empty months
SELECT source_type, count(*) FROM mentions GROUP BY 1 ORDER BY 2 DESC;                                    -- is the source mix reasonable
SELECT count(*) FILTER (WHERE body IS NULL) * 1.0 / count(*) FROM mentions;                               -- share with no body (≈ the X share)
```

**Phase 1 acceptance**: ☐ each of the 4 searches has ≥12 months of data in the DB ☐ no empty months (or explained) ☐ QA results recorded

---

### Phase 2 — Near-Real-Time Polling Layer (Week 2)

**Step 2.1 The poller worker's core logic** (watermark + overlap + adaptive cadence):

```python
# pipeline/poller.py (skeleton)
from datetime import datetime, timedelta, timezone

OVERLAP = timedelta(hours=2)          # overlap buffer, catches late-arriving documents

def poll_once(search_id: int):
    wm = get_watermark(search_id)                      # if no record, use now-24h
    start = wm - OVERLAP
    end   = datetime.now(timezone.utc)
    docs  = mw_search_mentions(search_id, start, end)  # 🔍 endpoint per the 3.2 verification list; mind pagination
    upsert_mentions(docs, search_id=search_id, channel="poll")
    # advance the watermark to end-30min (Pitfall #2: the last 30 minutes are treated as provisional and re-pulled/overwritten next cycle)
    set_watermark(search_id, end - timedelta(minutes=30))

def current_cadence() -> timedelta:
    """Adaptive cadence. Matchday window = 3h before kickoff to 3h after the match.
    The match schedule is maintained in config.py (🔍 scrape the current season's schedule from the official MLS site; store in a fixtures table)."""
    if in_matchday_window():   return timedelta(minutes=10)
    if is_daytime_et():        return timedelta(hours=1)    # 7:00–24:00 ET
    return None                                             # no polling at night
```

**Step 2.2 Quota guard** — enable it inside `mw_request`:
```python
def check_and_reserve(quota_class: str):
    used = count_today(quota_class)          # query api_call_log
    budget = DAILY_BUDGET[quota_class]       # the budget table from 4.4
    if used >= budget:            raise QuotaExhausted(quota_class)
    if used >= 0.9 * budget and not is_alert_triggered_context():
        raise QuotaSoftLimit(quota_class)    # only Alert-triggered calls are let through
```

**Step 2.3 Event-driven enhancement (the essence of poor-man's streaming)**:
1. In the Meltwater app, set one spike/every-mention-type Alert for each of S1 and S2, push target = a dedicated Slack channel (Meltwater→Slack is an officially supported one-way push).
2. Write a Slack event listener (Bolt SDK / Events API): on a new message in that channel → immediately trigger one `poll_once` for the corresponding search (with the `alert_triggered` context, which qualifies for the soft-limit exemption).
3. Effect: nearly zero quota during quiet periods; during a burst, response latency ≈ the Meltwater alert latency + one API call.

**Phase 2 acceptance**: ☐ polling ran per the cadence table for 48h with no duplicate-ingestion blow-up (duplicate rate <5%) ☐ the quota guard triggered the soft limit and degraded correctly ☐ one end-to-end drill of Slack alert → pull completed within 5 minutes

---

### Phase 3 — Rule-Based Spike Detection + Reconciliation (Week 3–4) [MVP milestone]

**Step 3.1 z-score spike detection** (rules first, models second — a deliberate architecture decision):

```python
# detect/zscore.py — run every 10 minutes for each search (reads the local DB, costs no API quota)
# Metric: v_t = reach-weighted mention count over the last 60 minutes (sum over mentions of log1p(reach))
# Baseline: mean mu and standard deviation sigma of v for the same search, over the past 28 days, same weekday + same hour (top 2% extremes removed)
# Trigger: z = (v_t - mu) / max(sigma, eps); z >= 3 and v_t >= MIN_VOLUME (default 10) → fire an alert
# Cooldown: no repeat alert for the same search within 90 minutes; write to the spike_alerts table
```
Tuning notes: start at `z>=3`; if false positives exceed 5 per week, raise to 3.5; if misses are obvious, lower to 2.5. **Every alert must be labeled ✅/❌ by the social media team on Slack within 24h afterward and written back to `spike_alerts.outcome` — these are Phase 4's free labels; skipping this is not allowed.**

**Step 3.2 Slack alert format** (written for humans; must include the so-what):
```text
🚨 [Revs Media Intel] Abnormal rise in discussion volume  z=4.2 (last-60min reach-weighted volume vs. the 28-day same-period baseline)
Topic clusters: <top keywords>   Sentiment: negative 62%   Top sources: <source1, source2>
Samples: <title + url> ×3
Recommendation: medium-high volume with negative dominance — recommend completing an assessment within 30 minutes and deciding whether to escalate to management. (Whether/how to respond publicly is the club's own decision; this system provides information only and gives no posting instructions — see 1.5)
[✅ Useful] [❌ Noise]
```

**Step 3.3 Daily reconciliation job** (`pipeline/reconcile.py`):
1. Phase 0 already created the recurring export (DAY, size=2, attached to S1–S4; note the ≤5-search cap).
2. Every day, 45 minutes after the window closes (i.e., the official 30-minute buffer plus 15 minutes of margin), download the data_url and do a full UPSERT (channel=`recurring`).
3. Persist a reconciliation report: today's polling misses (in recurring but not in poll), the update-overwrite count, and the late-document distribution. Miss rate >15% for 3 consecutive days → adjust the polling cadence or OVERLAP.
4. This job naturally satisfies the "must be accessed once every 30 days" anti-cancellation requirement (Pitfall #3).

**Phase 3 acceptance (= MVP complete)**: ☐ a z-score alert fired on a real matchday and was labeled by the social media team ☐ reconciliation miss rate <15% ☐ executives received the first hand-assembled weekly report (using the Chapter 7 template)


---

### Phase 4 — ML Spike Prediction (Week 5–8)

#### 4A. Problem Definition (must be locked in before any hands-on work)

- **Prediction target**: at time t, predict "whether the search's hourly reach-weighted mention volume will enter the top 10% of that search's historical same-period distribution within the next 6 hours" (binary classification).
- **Sample granularity**: one sample point per (search_id, 10 minutes).
- **Label source**: constructed offline from the 12–24 months of history backfilled in Phase 1; the human labels in `spike_alerts.outcome` serve as an auxiliary validation set.
- ⚠️ Pitfall: labels must be computed only from data after t, and features only from data at or before t (leakage prevention). Write an `assert_no_future_leak()` unit test.

#### 4B. Feature Engineering Checklist (store as `features` Parquet snapshots; write the path into predictions.features_ref)

| Group | Features | Notes |
|---|---|---|
| Velocity | Mention counts over the last 10/30/60/180 minutes; first difference (acceleration) | Core signal |
| Breadth | Unique authors and unique sources over the last 60 minutes | Distinguishes "one person spamming" vs. "real spread" |
| Weight | Reach-weighted volume; share of top-tier sources (defined by reach quantile) | Big media entering = a strong signal |
| Sentiment | Positive/negative share over the last 60 minutes and its rate of change (mw_sentiment first; switch to self-trained in Phase 5) | |
| Structure | Entropy of the source_type distribution; news-vs-social ratio | Cross-source spread is a spike precursor |
| Context | Whether inside a matchday window, hours to kickoff, day of week, hour (sin/cos encoding) | |
| Baseline | The current z-score value itself | Lets ML stand on the rules' shoulders |

#### 4C. Training & Evaluation

- Model: LightGBM / XGBoost binary classifier, with class weights for the imbalance.
- **Split**: temporal split. E.g., first 18 months train → next 3 months validation → last 3 months test. **Random splits are forbidden.**
- Metrics: `precision@k` (precision when firing at most k=3 alerts per day) and **average lead time** (first-alert time → actual peak time). Don't look at accuracy.
- Go-live criterion: on the test segment, the ML version improves precision@3 over the z-score rule version by ≥15%, or increases average lead time by ≥30 minutes; otherwise keep using the rule version (the rule version stays running as fallback and control).
- Retraining: rolling monthly retrains; retrain immediately after structural changes such as season start/end or a coaching change (the non-stationarity countermeasure).

**Phase 4 acceptance**: ☐ the leakage unit test passes ☐ the temporal-split backtest report is persisted ☐ after meeting the go-live criterion, ML and rules run dual-track in parallel for 2 weeks

---

### Phase 5 — DL / RL Advanced Track (optional; in order)

> Overall principle: each step's output is the next step's input. **Stage A order = ① ABSA sentiment → ② cascade prediction → ⑤ GNN amplification network (detailed design in Chapter 15)**. ③④⑥ all presuppose "the club posts" and are entirely assigned to Stage B (see 1.5): keep the design, do not implement for now.
> ❓ Ask the user: is the project positioned as a "production system" or "learning/portfolio"? Production → cut ⑤⑥ and concentrate firepower; portfolio → ⑤⑥ are actually the highlights.

#### ① Domain-Fine-Tuned ABSA Sentiment Model (the foundation; do this first)
- Motivation: generic sentiment misjudges fan language — irony, "we suck"-style venting, "FIRE THE COACH" actually coming from high-stickiness fans.
- Approach: a small model (RoBERTa-class or a small LLM) + LoRA fine-tuning, doing aspect-based sentiment. **Aspects are defined by the business**: `coach / roster & signings / ticketing & matchday experience / Everett stadium project / club front office`.
- Labeling: LLM weak-labels 3–5k items + human spot-check of 300 for validation (agreement <85% → fix the prompt and relabel). The training set is stratified-sampled from the `mentions` table (by source_type and month).
- Output: `custom_sentiment` JSONB backfilled across the whole table; it becomes an input to Phase 4 features and the Chapter 7 dashboards. Acceptance = macro-F1 on the human-labeled holdout is significantly better than mw_sentiment.

#### ② Neural Cascade Prediction (the DL flagship)
- Upgrade from "will it spike" to **predicting the entire propagation trajectory**: peak time, peak magnitude, decay speed.
- Technical routes (ordered by implementation difficulty): a) direct multi-target regression (GBDT/MLP predicting peak_time/peak_volume) b) a PatchTST-style time-series transformer c) a neural temporal point process (the neural version of Hawkes; input is the per-mention event stream: timestamp, log-reach, sentiment).
- Value pitch: upgrades the alert from "something is happening" to "this thing peaks in 3 hours at medium magnitude — no need to pull an all-nighter."

---

> **🚧 ③④⑥ below all belong to Stage B (future) and are not to be implemented for now.** Stage B's correct starting point is B0, not jumping straight to bandits.

#### B0 [Stage B starting point] Causal Evaluation of Posting Impact — answering "if we post, what impact will it have"
- If the club starts posting in the future, the first task is not optimizing posting but **measuring a single post's causal impact**: how much did volume/sentiment on related topics change after posting, relative to the counterfactual baseline of "what would have happened without the post."
- Methods: CausalImpact / synthetic control (construct the counterfactual control group from S3 competitors' same-topic time series), interrupted time series analysis (ITS). **The listening database accumulated in Stage A is precisely the future control baseline** — this is the hidden asset value of the pure-listening stage.
- Only when B0 proves that "posting has a measurable positive impact" do we earn the right to enter the optimization problems of ③④.

#### ③ [Stage B] Contextual Bandit (posting decision optimization)
- Decision problem: the combinatorial choice of **posting time × content type × format**. Context = current sentiment-state features + match schedule + time of day; reward = engagement in the 24h after publishing.
- Algorithm: Thompson Sampling (start with LinTS). Exploration budget ≤10% of traffic; the rest follows the current best.
- ⚠️ Doing online exploration on a real brand account = paying for training with brand safety. Therefore: the action space contains **only safe options whitelisted by the social media team**; every exploratory action gets human confirmation before publishing.
- Prerequisite: performance data for owned posts (❓ Ask the user about Owned Social API access, or cold-start from manually exported historical post data).

#### ④ [Stage B] Reward Model + DPO (porting the RLHF paradigm to social copy)
- Construct preference pairs from historical posts' high/low engagement → train a reward model.
- Usage one (immediately usable): an LLM drafts n versions of copy → the RM ranks best-of-n → human final review, then publish.
- Usage two (advanced): DPO fine-tune a dedicated copywriting model.
- Production form: AI drafts, RM ranks, human gives final approval — **the human is always in the loop**.

#### ⑤ Propagation-Graph GNN — promoted from stretch to a **Stage A official project**
- The full detailed design (data reality, story clustering, graph schema, G0–G4 tiered modeling, influence attribution, milestones & acceptance) is in **Chapter 15**; not repeated here.
- One-line summary: an inferred amplification network + early prediction of story cascade size; the by-product "key amplifier watchlist" is used in Stage A to **boost alert weighting + as media-relations intelligence**, unrelated to posting.

#### ⑥ [Stage B] Offline RL + OPE / LLM Fan Simulator (stretch)
- Historical posting logs → learn a policy offline; before going live it **must** pass off-policy evaluation (IPS / doubly robust), then a small-traffic A/B. Skipping OPE and going straight to production = violating the 0.3 DON'Ts.
- LLM agents simulate fan cohorts of different personas reacting to content, building a safely explorable environment (the world-model idea). Good for papers/portfolio; **do not** expect the simulator to be faithful enough to directly guide production decisions.

#### Data Volume & Non-Stationarity (two iron rules shared by all DL/RL projects)
1. **One team's data cannot feed DL** → use saved searches to pull in all of MLS + the Boston Big Four for pre-training/joint training, then fine-tune on the Revs. ⚠️ This eats into the export quota; schedule the backfill plan in advance.
2. **Distributions drift** (season vs. off-season, coaching changes, stadium-project milestones) → always rolling retrains + temporal-split backtests + online monitoring of prediction-distribution drift (see Chapter 8).


---

## 6. Self-Built Agent / MCP Layer (Substitute for the Official Meltwater MCP + Mira)

### 6.1 Background & Positioning

There are two official MCP products (neither enabled): Meltwater MCP (`https://api.meltwater.com/v2/mcp`, a fine-grained tool layer that you orchestrate yourself) and Mira MCP (`https://api.meltwater.com/mcp`, where Meltwater's AI orchestrates the finished product for you). Both require the corresponding package to be included in the subscription.

**Our self-built version is actually stronger**, because the local DB contains things the official MCP will never have: ML prediction results, self-trained sentiment, internal data. Core design principle: **tools read local Postgres first (zero latency, zero quota); the Meltwater API is fallback only**.

### 6.2 FastMCP Server Skeleton

```python
# agent/mcp_server.py — pip install fastmcp
from fastmcp import FastMCP
mcp = FastMCP("revs-intel")

@mcp.tool()
def query_mentions(topic: str, days: int = 7, source_type: str | None = None) -> dict:
    """Query a summary of the last N days of mentions in the local DB (volume, sentiment distribution, top sources, samples).
    topic ∈ {brand, stadium, competitors, sponsors}, mapped to the search_ids of S1–S4."""
    ...  # SELECT ... FROM mentions WHERE search_id=... AND publish_date > now()-interval

@mcp.tool()
def stadium_sentiment_report(days: int = 14) -> dict:
    """Everett stadium topic sentiment: sentiment trends broken down by geography (local vs. national media) and by aspect + the latest predictions."""
    ...

@mcp.tool()
def latest_predictions(target: str = "spike_6h") -> dict:
    """Read the predictions table; return each search's latest model output and confidence."""
    ...

@mcp.tool()
def recent_alerts(days: int = 7) -> dict:
    """Read spike_alerts, including the human-labeled outcome — for questions like 'how good were last week's alerts'."""
    ...

@mcp.tool()
def mw_live_analytics(search_key: str, metric: str, days: int) -> dict:
    """Fallback: hit the Meltwater analytics endpoint directly when local data is insufficient.
    ⚠️ Goes through mw_request → constrained by the quota guard; budget per 4.4 (reserved buffer: 10 calls/day)."""
    ...

if __name__ == "__main__":
    mcp.run()   # stdio by default; use streamable-http for remote deployment
```

Mounting into Claude Desktop (`claude_desktop_config.json`):
```json
{"mcpServers": {"revs-intel": {"command": "python", "args": ["-m", "agent.mcp_server"]}}}
```

### 6.3 DIY Mira: the Daily Morning-Briefing Agent

- On a schedule (7:30 ET daily), trigger a Claude-driven agent: call the 4 local tools above + at most 2 `mw_live_analytics` calls → generate a one-page Markdown morning brief → push to Slack + store in `reports/`.
- Fixed briefing structure: yesterday's total volume and day-over-day change → sentiment highlights (by aspect) → stadium-project developments → a one-line competitor comparison → today's watch items (incl. matchday notes) → every item carries a so-what.
- This is the self-built version of the "orchestrated outcome"; when executives want to probe details, they simply keep asking in Claude (the tools are already mounted).

---
## 7. Business Insight Delivery Layer (Where the Value Is Won or Lost)

### 7.1 Two Deliverable Specifications

**A. Mission Control (social media team, real-time)**
- Vehicle: Slack channel (alerts) + a lightweight web dashboard (can come later).
- Content: spike alerts (the 3.2 format), cascade predictions (after Phase 5②: expected peak time/magnitude), a priority attention queue (high-priority mentions ranked by reach × negativity, for human assessment and escalation), amplifier-watchlist hit notices (Chapter 15).

**B. Executive Scorecard (monthly + crisis pushes)**
- Vehicle: a one-page Markdown/HTML report (exceeding one page is forbidden; details go into appendix links).
- Fixed four sections: ① Brand health index (volume, net sentiment, weighted trend) ② SOV vs. Boston Big Four + MLS (share and change) ③ Everett stadium sentiment column (broken down by geography and stakeholder + 7-day forecast + risk points) ④ Sponsorship exposure value (S4 co-mention volume × reach valuation).
- Crisis push: z≥4 and negative-dominated and lasting >2 hours → push the executive summary directly (thresholds and recipient list: ❓ Ask the user).

### 7.2 The "So What" Writing Standard (mandatory for every insight)

Format: **Observation (number) → Explanation (why) → Recommendation (what to do)**.
- ❌ Bad example: "Negative sentiment rose 12%."
- ✅ Good example: "Negative volume rose 12%, concentrated in Everett local media on the traffic topic (61% of the new negatives); recommend proactively publishing traffic-planning and shuttle-service content before the next community meeting."

### 7.3 Internal Data Join Plan (the source of executive language)

- Target sentence pattern: "The volume peak within 48 hours of a big away win corresponds to an X% lift in single-game ticket sales for the next home match" — the correlation of social signals × revenue metrics is what boardroom language sounds like.
- Needs from the user (❓ Ask the user, ordered by availability): matchday ticketing/single-game ticket sales, merchandise sales, app/website traffic, and (if available) broadcast viewership.
- Implementation: create an `internal_metrics` table (date, metric, value, source); start with lagged correlation analysis (Spearman at 0–7-day lags), and only discuss causality after significance. ⚠️ Correlation ≠ causation; report wording uses "corresponds to / accompanies," never "causes."

---

## 8. Operations, Monitoring & Incident Runbook

### 8.1 Daily Automated Inspection (one daily job does it all; results pushed to the Slack ops channel)

| Check | Threshold | Action |
|---|---|---|
| Quota usage (api_call_log) | >80% warning | Notify + review the cadence config the next day |
| Watermark lag | Any search >3h | Check poller liveness, manually re-pull |
| Reconciliation miss rate | >15% for 3 consecutive days | Adjust OVERLAP / cadence |
| Today's mentions ingested | 60% below the 28-day same-weekday average | Check whether the search was modified/deleted or the export cancelled (Pitfall #3) |
| Duplicate rate (same id across channels) | Monitor only | A normal phenomenon; UPSERT already handles it |
| Model input drift | Feature mean shift >3σ | Trigger a retraining evaluation |
| Recurring export status | Not ACTIVE | Rebuild immediately and alert |

### 8.2 Incident Handling Quick Reference

- **429 (rate limited)**: exponential-backoff retries (base 2s, max 5 attempts); on `QuotaExhausted`, stop until the next day, keeping only the Alert-triggered channel.
- **Export stuck in PENDING for a long time (>2h)**: do not create it again (wastes the queue); check status_reason first, then contact support.
- **Search modified by an in-app user**: a changed Boolean creates a data discontinuity — snapshot the 4 searches' query text weekly into a `search_snapshots` table; diffing out a change triggers an alert.
- **Meltwater platform incident**: subscribe to https://status.api.meltwater.com ; pause polling during the incident, and patch the hole afterward with a one-time export.

---

## 9. Decision Log (why it is designed this way)

| Decision | Rationale | Re-evaluation condition |
|---|---|---|
| No streaming; three-tier polling instead | Data Streams not purchased; the use case only needs minute-level latency | After obtaining real usage data, negotiate the add-on purchase with the account manager |
| Rules first (z-score), then ML | Can go live in two weeks, accumulates labels, builds trust | ML meets the 4C go-live criterion |
| X uses count signals only; no body purchase | X API rehydration is an extra cost | Upgrade after the ❓ user approves the budget |
| Exports always use the JSON template | All fields + the user's no-CSV preference | None |
| Local-DB-first self-built MCP | Zero quota, zero latency + can fuse predictions and internal data | Can coexist once the official MCP is enabled |
| The human is always in the RL loop | Brand safety > exploration efficiency | None (not re-evaluable) |
| Stage A restricted to pure listening, zero posting-side features | The club does not post at this stage; guards against scope creep and brand risk | Club starts posting → enter Stage B, doing the B0 causal evaluation first |

## 10. Open Questions List (ask the user in the very first conversation after taking over)

1. [Needed only in Stage B; not blocking now] Is the Owned Social API included in the package? (the data source for posting impact evaluation and the bandit)
2. The sponsor list (needed for S4); the recipient list and threshold preferences for executive crisis pushes.
3. Is the X API rehydration budget approved?
4. Which internal data (ticketing/merchandise/traffic) can we get, and in what format?
5. Project positioning: production system or portfolio? (determines the Phase 5 trade-offs)
6. The real daily analytics quota number (backfill after checking in Phase 0 step 0.2).
7. [Prerequisite for Chapter 16] The user's already-categorized media list, please provide it in structured form: canonical name / aliases and common spellings / domain or account / type (outlet | journalist) / language / the user's subjective tiering (tier, optional). This list serves both Chapter 15 (media nodes) and Chapter 16 (the credibility prior).

---

## Appendix A — Quick Reference Card

- Base URL `https://api.meltwater.com`; header `apikey: <token>`; all times UTC ISO8601, windows inclusive of the start and exclusive of the end.
- Endpoints: `GET /v3/searches` · `POST /v3/exports/one-time` · `GET /v3/exports/one-time/<id>` · `POST /v3/exports/recurring` · `GET /v3/exports/recurring/<id>` · `GET /v3/custom_categories`
- Docs entry: https://developer.meltwater.com/guides/getting-started/overview · FAQ: https://developer.meltwater.com/help/faqs · Status page: https://status.api.meltwater.com
- Rate limits: analytics/search 5/s · 100/min · daily quota per contract; export 20/min; one-time ≤2 million docs; recurring minimum DAY, executes at window close +30min, cancelled after 30 days without access.

## Appendix B — Glossary

| Term | Definition |
|---|---|
| Saved Search | A Boolean query in Meltwater; the entry point for all export/search/analytics, referenced by `search_id` |
| Mention / Document | One matched piece of content (news article/post/comment), primary key `document_id` |
| Watermark | The "publish_date confirmed fully pulled up to"; the progress pointer for incremental polling |
| UPSERT | Update if exists, insert if not; executed by document_id in this project |
| Reach | Meltwater's estimate of a piece of content's potential exposure, used for weighting |
| SOV | Share of Voice: one brand's share of the total volume of a comparison set |
| Lead time | The gap between the first alert and the actual peak; bigger is better |
| precision@k | With only k alerts allowed per day, the share of alerts that are true spikes |
| ABSA | Aspect-Based Sentiment Analysis: sentiment analysis faceted along business-defined aspects |
| OPE | Off-Policy Evaluation: evaluating a new policy on historical data without going live |
| Provisional data | Unstabilized data from `now-30min ~ now`, overwritten by the next polling cycle |

## Appendix C — The Ten Core Conclusions of This Project (one-screen version)

1. Crawling is the Meltwater platform's job; the API only reads the data. All latency expectations are set around "ingestion delay + the 30-minute buffer."
2. Not buying streaming ≠ no near-real-time: adaptive polling + Alert event triggering + daily reconciliation = a substitute with minute-level latency, and minute-level is entirely sufficient for this use case.
3. Quota is the #1 design variable: every call goes through the single exit `mw_request`, quota guard first.
4. `document_id` UPSERT + event-time handling is the only correct posture against late/duplicate documents.
5. Two audiences, two deliverables: the social media team wants mission control; executives want a one-page scorecard.
6. Everett stadium sentiment is this project's highest-value topic — it directly affects approvals and CIA terms; it is not a vanity metric.
7. Rules before models; the ML go-live criterion = precision@3 +15% or lead time +30min over the rule version.
8. Stage A does listening-side only: ABSA sentiment → cascade prediction → GNN amplification network; bandit/DPO/offline RL belong to Stage B (only discussed once the club posts), with the human always in the loop.
9. One team's data isn't enough → joint training on all of MLS + the Boston Big Four, then fine-tune; always temporal splits + rolling retrains.
10. The self-built MCP is local-DB-first and stronger than the official version (fusing predictions and internal data); insights always follow "observation → explanation → recommendation."


---

## 11. Azure Deployment Architecture (Container Apps + VNet + Azure PostgreSQL)

### 11.1 Deployment Topology

```text
Company Azure VNet
├── ACA Environment (infrastructure subnet)
│   ├── App: frontend (always-on; talks only to the backend, never touches the DB)
│   ├── App: backend API (always-on; DB read path + Slack Events callback + in-memory cache)
│   └── Jobs (cron-triggered, exit when done, all state in the DB):
│       ├── job-poller      cron: */10 * * * *   (internal adaptive cadence, see 11.2)
│       ├── job-reconcile   cron: fixed daily UTC time (recurring window close +45min)
│       ├── job-rollup      cron: hourly at :50   (maintains mentions_hourly, see 12.3)
│       ├── job-briefing    cron: daily 11:30 UTC (≈7:30 ET; mind daylight saving)
│       └── job-inspect     cron: daily inspection (Chapter 8 checklist + 14.5 connection check)
├── Private Endpoint → Azure Database for PostgreSQL Flexible Server
│   └── Private DNS: privatelink.postgres.database.azure.com
└── Key Vault (MELTWATER_API_KEY, Slack token → injected via ACA secret references)
```

Key points:
1. **Schedule with ACA Jobs; do not run APScheduler inside an always-on container** — Jobs are stateless, billed by duration, and retryable by the platform on failure; all progress state lives in Postgres (the watermarks table).
2. **DB authentication via Managed Identity (Entra ID)** — no password management; the Meltwater key is injected from Key Vault.
3. The frontend only ever talks to the backend API and **never connects directly to the DB** (connection-budget reasons; see Chapter 14).

### 11.2 Implementing the Adaptive Cadence in cron (an important trick)

cron cannot express "10 minutes on matchdays, 1 hour on regular days, off at night." The approach: fix cron at `*/10 * * * *`; the Job's first step on startup calls `current_cadence()` for a self-check and does `exit 0` if it is not inside a should-run window. An empty run costs only a few seconds, and the cadence logic stays 100% in code and testable.

### 11.3 Concurrency & Idempotency (double insurance)

- Job `parallelism=1` + a replica timeout (e.g., 8 minutes for the poller) prevents stuck overlapping runs.
- Add a Postgres transaction-level advisory lock in code on top: wrap the task body in one transaction, opening with `SELECT pg_try_advisory_xact_lock(hashtext('poller'))`; exit immediately if the lock isn't acquired. ⚠️ Use the **xact** variant, not the session variant (Chapter 14 explains why).
- **The transactional watermark (this chapter's most important pattern)**: the data UPSERT and the watermark advancement commit in **the same transaction**. DB write fails → the watermark doesn't move → the next cycle automatically re-pulls the same window. Tasks are thereby naturally idempotent and blindly retryable.

### 11.4 The VNet Egress Pitfall

⚠️ An egress allowlist containing only `api.meltwater.com` will break: **the export `data_url` usually points to a different cloud-storage domain (a pre-signed URL)**. Before go-live, manually run one export, confirm the data_url's actual domain, and add it to the allowlist as well. The same applies to Slack and (if enabled) the X API domains.

---

## 12. Data-Growth Governance

Expected scale: the 4 search groups average thousands to tens of thousands of items per day — on the order of tens of millions of rows over two years, which Postgres can handle; **the real bloat source is the `raw JSONB` column (often 70%+ of the volume)**. Four moves:

### 12.1 Monthly Partitioning
Change `mentions` to `PARTITION BY RANGE (publish_date)` with monthly partitions; job-rollup also pre-creates partitions for the coming 2 months along the way. Benefits: query pruning + detaching whole partitions when archiving, no giant DELETEs.

### 12.2 Hot / Warm / Cold Three-Tier Lifecycle
| Tier | Range | Contents | Action (monthly maintenance job) |
|---|---|---|---|
| Hot | 0–90 days | All fields incl. raw, fully indexed | None |
| Warm | 90 days–2 years | Strip raw (first export the month's raw wholesale to a JSON archive in Blob, then `SET raw=NULL`) | Executed monthly |
| Cold | >2 years | Export whole partitions **Parquet → Azure Blob** (lifecycle policy downgrades to Cool/Archive), then drop the partition | Executed monthly |

ML training reads Parquet anyway, so the cold tier is the training tier — two birds, one stone. (Still no CSV output.)

### 12.3 The Rollup Table (an optimization more important than deleting data)
`mentions_hourly(search_id, hour, cnt, reach_sum, pos_cnt, neg_cnt, uniq_authors, ...)`, maintained incrementally by job-rollup (recompute only the last 3 hours, covering the provisional interval). The z-score baseline, dashboards, SOV, and the morning brief **all read the rollup** — query cost fully decoupled from the raw data volume.

### 12.4 Indexes & Bloat
- Use **BRIN indexes** on big tables' time columns (roughly 1% the size of a B-tree, extremely efficient for time-appended data); keep B-tree for high-frequency equality columns.
- Dense UPSERTs → lots of dead tuples: `ALTER TABLE mentions SET (autovacuum_vacuum_scale_factor=0.02)`.
- Weekly inspection of the bloat rate (pgstattuple or estimation SQL); log anything >30% in the ops notes.

---

## 13. Resilience & Degradation Design (the Fallback System)

### 13.0 Core Understanding
The three-tier architecture is inherently self-healing: **a Tier 1 polling failure is only a "delay event," not a "data-loss event"** — a missed window gets patched T+1 by the recurring reconciliation, and larger holes get targeted backfills via one-time export. Fallback goals = on failure, don't waste quota, don't write dirty data, don't affect the read path.

### 13.1 Failure → Mechanism Table
| Failure | Mechanism |
|---|---|
| Meltwater 429/5xx/timeouts | tenacity exponential backoff + jitter, ≤5 attempts; consecutive failures open the **circuit breaker** (during the open period, skip polling and only log; half-open probing for recovery) |
| Quota exhausted | Quota-guard degradation (Alert-triggered channel only → full stop); already designed |
| Postgres unavailable | The watermark doesn't advance = the next cycle re-pulls (idempotent); **data already pulled gets spooled as JSON into the Blob `dead-letter/` container** (don't waste already-spent quota), and job-replay re-ingests it after recovery |
| A single bad document | Per-item try/except; bad documents go to a `quarantine` table (raw payload + error). **Never let one item poison the whole batch** |
| Job stuck / overlapping | xact advisory lock + replica-timeout force kill |
| Slack delivery failure | The `spike_alerts` table is the source of truth; at-least-once retries; missed deliveries backstopped by job-inspect |
| Connections maxed out (53300) | See 14.4 |

### 13.2 The Degradation Ladder (goes into code, not into your head)
- **L0 normal.**
- **L1 quota soft limit**: event-triggered pulls only.
- **L2 Meltwater outage**: stop ingestion; the frontend runs as usual with a "data as of time X" banner (the backend reading the DB is unaffected).
- **L3 DB outage**: the backend returns recently cached aggregates from memory; the poller spools to Blob.
Principle: **the read path and the ingestion path are fully decoupled; the frontend never goes down because ingestion did.**

### 13.3 Platform-Side Guarantees
Azure Monitor alerts: consecutive Job failures, watermark lag >3h, connection count ≥8 (see 14.5). Flexible Server PITR backup retention ≥14 days. Subscribe to the Meltwater status page; pause polling during incidents and patch holes with one-time exports afterward.

---

## 14. Connection Governance (Hard Constraint: at most 10 concurrent connections to the same database)

> Background: the company's Postgres limits the same database to at most 10 concurrent connections; exceeding it causes problems. **Connections are therefore an even scarcer resource than API quota**; this chapter's rules rank at the same level as the 0.3 behavioral rules and must be enforced.

### 14.1 Connection Budget Table (worst-case concurrent total ≤8, 2 reserved)
| Component | Form | Connection strategy | Worst-case usage |
|---|---|---|---|
| backend API | Always-on | SQLAlchemy pool: `pool_size=2, max_overflow=1, pool_timeout=10` | 3 |
| job-poller | Short-lived | Single connection | 1 |
| job-reconcile | Short-lived | Single connection | 1 |
| job-rollup / monthly maintenance | Short-lived | Single connection (staggered scheduling, see below) | 1 |
| job-briefing / inspect | Short-lived | Single connection (staggered) | 1 |
| Manual debugging (psql/DBeaver) | Manual | Disconnect right after use | 1 |
| **Reserved buffer** | — | — | **2** |

**Staggering rule**: the Jobs' cron minute fields are offset (poller :00/:10/…, rollup :50, reconcile at a fixed time, briefing/inspect each at their own fixed time), so that the number of short-lived Jobs running simultaneously is ≤2. Even if everything collides, the budget table's worst case is still only 8.

### 14.2 Code-Level Iron Rules
1. **One engine per process; ad-hoc create_engine inside a function is strictly forbidden.**
2. Always-on API engine parameters: `pool_size=2, max_overflow=1, pool_timeout=10, pool_pre_ping=True, pool_recycle=300` (pre_ping + recycle guard against getting a dead connection after the Azure gateway reclaims idle TCP).
3. Job template (copy verbatim):
```python
# common/db.py
from sqlalchemy import create_engine

def job_engine(app_name: str):
    return create_engine(
        DSN, pool_size=1, max_overflow=0, pool_pre_ping=True,
        connect_args={
            "application_name": app_name,                    # the key to connection accountability
            "options": "-c statement_timeout=120000 "
                       "-c idle_in_transaction_session_timeout=60000",
        },
    )

# pipeline/poller.py entry point
def main():
    eng = job_engine("job-poller")
    try:
        with eng.begin() as conn:                            # single transaction = lock + data + watermark
            if not conn.execute(text(
                "SELECT pg_try_advisory_xact_lock(hashtext('poller'))")).scalar():
                return                                       # another instance is already running; exit immediately
            run_poll(conn)                                   # UPSERT + watermark in the same transaction
    finally:
        eng.dispose()                                        # iron rule: always dispose on exit
```
4. Always use `with eng.begin()/eng.connect()` context managers; a bare `connect()` left unclosed is forbidden.
5. Every component must set `application_name` (api / job-poller / job-reconcile / …); otherwise the accountability query in 14.5 breaks.

### 14.3 Server-Side Backstop (the auto-reclamation net against "forgot to close")
Set in the Flexible Server parameters: `idle_in_transaction_session_timeout=60s`, `idle_session_timeout=10min` (supported on PG14+; admin sessions can be exempted). Meaning: even if code leaks a connection, an idle transaction gets automatically cut server-side after 1 minute and an idle session after 10 minutes.

### 14.4 Degradation When Connections Max Out (FATAL 53300 too_many_connections)
Handle per the L3 flow: back-off retry 3 times (2s/4s/8s) → still failing: in the Job scenario, spool the already-pulled data to Blob dead-letter and exit; in the API scenario, return cached values and alert. **Never hard-retry in a loop** (that makes the storm worse).

### 14.5 Monitoring & Manual Handling
Inspection and alerting share one query (the backend samples every minute; ≥8 triggers a Slack alert):
```sql
SELECT application_name, state, count(*), max(now()-state_change) AS oldest
FROM pg_stat_activity WHERE datname = current_database()
GROUP BY 1,2 ORDER BY 3 DESC;
```
Manual reclamation of zombies (look clearly at application_name before acting):
```sql
SELECT pg_terminate_backend(pid) FROM pg_stat_activity
WHERE datname = current_database() AND state = 'idle'
  AND state_change < now() - interval '15 minutes'
  AND application_name NOT IN ('api');
```

### 14.6 The PgBouncer Decision (revises the related statements in Chapter 11)
- **At the current stage (≤6 components): do not enable PgBouncer; everything connects directly on 5432**, governed by the 14.1 budget table — the simplest possible chain, no compatibility traps.
- **Later, when frontend traffic grows and the API needs greater client concurrency**: only the backend API switches to Flexible Server's built-in PgBouncer (6432, transaction pooling, with the server-side default_pool_size kept at 4–5); **Jobs stay on direct 5432**.
- ⚠️ The reason (and also why 11.3 uses the xact lock): under transaction pooling, session-level features are unreliable — session-variant advisory locks (`pg_try_advisory_lock`) will misbehave, and psycopg's prepared statements also need extra configuration (`prepare_threshold=None`, or confirm the PgBouncer version supports `max_prepared_statements`). Jobs on direct connections + `pg_try_advisory_xact_lock` sidestep these traps entirely.


---
## 15. Amplification-Network GNN Detailed Design (Stage A Official Project)

### 15.1 Goals & the Two Outputs

- **Output 1 (prediction)**: within 30 minutes of a story starting, based on "which nodes have already picked up this story," predict its final size 48 hours later (reach-weighted total volume).
- **Output 2 (the list)**: a data-driven **key-amplifier watchlist**. Its two Stage A uses: ① when a watchlist node appears early in a story → automatically boost that story's alert weight (fed back into the Phase 4 spike model, closing the loop); ② delivered as media-relations intelligence to executives/PR ("which outlets and accounts drive the volume of the stadium topic"). **Unrelated to posting; conforms to the 1.5 scope statement.**

### 15.2 First, a Cold Shower: Data Reality & the Three Sources of Edges

⚠️ The most important honest statement: **Meltwater earned media data contains no true retweet/quote chains** (X even more so — IDs only). What we build is an **inferred** amplification network, with edges in three tiers (of decreasing confidence):

| Edge type | Construction method | Confidence |
|---|---|---|
| E1 citation edges | A hyperlink in the body pointing to another document's URL (normalize URLs first: strip utm parameters / unify the protocol); patterns like "according to <outlet name>" / "per <journalist name>" appearing in the body (rules + NER) | Strong |
| E2 structural edges | Reddit subreddit/thread membership (🔍 Verify whether Reddit documents in api.json contain thread/parent info); Bluesky @mentions | Medium |
| E3 temporal-precedence edges | Within the same story, A reports first and B follows within Δt≤6h; aggregated across all stories into weighted A→B edges | Weak but with the widest coverage |

**De-biasing E3 (mandatory — otherwise all the edges are fake)**: big outlets report everything; preceding ≠ influencing. Use PMI-style normalization: `w(A→B) = log[ observed(# stories where B followed A) / expected(the expectation if A and B participated independently) ]`, truncating negative values to 0. Without this step, PageRank will mistake "the most prolific outlet" for "the most influential outlet."

⚠️ X nodes are "thin" (only IDs and timestamps — no body, no author name) → the graph naturally tilts toward news / Reddit / Bluesky / blogs. That's acceptable for the "media-relations intelligence" use case (outlets are what matter anyway), but it must be written into the deliverable's methodology note; if X rehydration is approved later (Open Question #3), the E1/E2 edges thicken substantially.

### 15.3 Prerequisite G0: The Story-Clustering Pipeline (the truly hard engineering is here, not in the GNN)

**Without a reliable story_id, everything downstream is a castle in the air.** Quality gate: manually sample 50 stories and check purity ≥85%; entering G2 is forbidden until this is met.

```sql
-- 002_stories.sql
CREATE TABLE stories (
    story_id     BIGSERIAL PRIMARY KEY,
    t0           TIMESTAMPTZ NOT NULL,      -- the earliest member's publish_date
    seed_title   TEXT,
    aspect       TEXT,                       -- stadium/roster/match/front office/other (labeled via ABSA or keyword rules)
    final_size   DOUBLE PRECISION,           -- the 48h reach-weighted total (the label; backfilled by a job after t0+48h)
    n_docs       INT DEFAULT 0
);
CREATE TABLE story_members (
    document_id  TEXT PRIMARY KEY REFERENCES mentions(document_id),
    story_id     BIGINT NOT NULL REFERENCES stories(story_id),
    lag_minutes  INT NOT NULL                -- publish_date - t0
);
```

Process (runs incrementally every 10 minutes alongside the detection job):
1. For new documents, embed `title + the first 500 characters of the body` with a multilingual embedding (`bge-m3` or `paraphrase-multilingual-mpnet`; X has no body → excluded from clustering; only attached by time to the most similar existing story, or counted independently).
2. Compare against the centroids of active stories in a rolling 72h window: `cosine ≥ 0.62` (a starting value, tuned by purity) **or** a shared normalized URL **or** ≥2 shared named entities → assign to that story; otherwise open a new story.
3. A story's `final_size` is backfilled by a daily job after t0+48h — this is the GNN's label, at zero human-labeling cost.

### 15.4 Graph Schema (heterogeneous graph)

```sql
-- 003_graph.sql
CREATE TABLE graph_nodes (
    node_id      BIGSERIAL PRIMARY KEY,
    node_key     TEXT UNIQUE NOT NULL,       -- 'source:theathletic.com' / 'author:reddit:u_xxx' / 'subreddit:NewEnglandRevolution'
    node_type    TEXT NOT NULL,              -- source | author | subreddit
    features     JSONB                       -- historical volume, mean reach, aspect distribution, active hours, source_type
);
CREATE TABLE graph_edges (
    src BIGINT, dst BIGINT, etype TEXT,      -- e1_cite | e2_struct | e3_precede
    weight DOUBLE PRECISION,
    window_month DATE,                       -- edges versioned by month, rebuilt over a rolling 12 months (non-stationarity)
    PRIMARY KEY (src, dst, etype, window_month)
);
CREATE TABLE amplifier_scores (
    node_id BIGINT, month DATE, method TEXT, -- pagerank | attribution
    score DOUBLE PRECISION, aspect_affinity JSONB, typical_lag_min INT, hit_rate DOUBLE PRECISION,
    PRIMARY KEY (node_id, month, method)
);
```

Story nodes do not go into `graph_nodes` — stories are dynamically constructed at training time as "early-adopter subgraph + temporal features" samples, avoiding unbounded graph growth.

### 15.5 Tiered Modeling G1–G4 (must be done in order; skipping tiers is forbidden)

**G1 graph baseline (no training; deliverable by week 3)**: run weighted PageRank + k-core + out-degree on the combined E1+E2+E3 graph → **amplifier list v0**. This is already an executive-ready deliverable.

**G2 GBDT baseline (the GNN's beat-me benchmark)**: append graph features to Phase 4's spike/size models — for a story's first-30-minute early adopters: sum of PageRank, watchlist top-20 hit count, mean historical amplification power, cross-source_type entropy, whether an E1 citation edge has appeared. The target changes to regressing `log(final_size)` + classifying `top-decile`.

**G3 static heterogeneous GNN**:
- Self-supervised pre-training: edge prediction / contrastive learning on the heterogeneous graph (PyG's `HeteroConv` + GraphSAGE or HGT), yielding a 64–128-dim embedding per node.
- Cascade head: attention pooling over "the embedding set of the first-30-minute early adopters," concatenated with temporal features (adoption speed, lag distribution, aspect, matchday or not) → a small dual-head MLP output (log-size regression + top-decile classification).
- **Go-live criterion: G3 improves the Spearman correlation or precision@k over G2 by ≥10%; otherwise the production model is G2** (G2 is already using the graph — nothing to be ashamed of).

**G4 temporal graph TGN/TGAT (optional)**: model every (node, story, t) as an event stream. Do this only if G3 clearly wins and there is still capacity left.

Evaluation discipline (same as Phase 4): temporal splits; metrics = Spearman(predicted vs. actual log size), top-decile precision@k, and the gain curve of "prediction at the 30-minute mark vs. at the 6-hour mark."

### 15.6 Influence Attribution → Amplifier List v1

- Method: **counterfactual perturbation** — for each candidate node, remove it from the stories' early-adopter sets and compute the average drop Δ in the model's predicted size; Δ is that node's influence score (attribution).
- Compare against G1's PageRank list: take the union of the two rankings for one human review pass (a 30-minute task); look at nodes with big disagreements case by case.
- List fields: node, type, influence score, aspect affinity (share of stadium/roster/… each), typical lag (how quickly it usually follows), historical hit rate (the share of stories where its early appearance ended up becoming a big story).
- Monthly refresh job (runs together with the 12.2 maintenance job); the output goes into mission control (watchlist hit notices) + the executive monthly report (a "key amplifiers of the Everett topic" column).

### 15.7 Engineering & Compute

- Stack: PyTorch Geometric + sentence-transformers; at this graph's scale (thousands to tens of thousands of nodes, hundreds of thousands of edges), **CPU training suffices**, run on a large-spec ACA Job or a dev machine; the model and node-embedding artifacts are stored in Blob.
- Zero inference burden: embeddings and the list are precomputed monthly; online there is only the cascade head's small MLP, embedded directly into the 10-minute detection job.
- Embedding/clustering inference (G0's embedding computation) is an ongoing cost, but small in volume (thousands of items per day on average); CPU batching suffices.

### 15.8 GNN-Specific Pitfall List

1. Temporal precedence ≠ causality; PMI de-biasing is a mandatory step (15.2).
2. Leakage: the feature window is strictly `[t0, t0+30min]`, the label window strictly `(t0+30min, t0+48h]`; reuse `assert_no_future_leak()`.
3. Story-clustering purity <85% → stop and fix the clustering; training on defective data is forbidden.
4. Cold-start nodes (new accounts/new outlets): fall back to node_type-level average embeddings.
5. One team's stories aren't enough (the Revs have roughly several hundred to two thousand valid stories per year) → joint training on all of MLS + the Boston Big Four (the existing iron rule), fine-tuned to the Revs scenario.
6. Edges are versioned by month and rebuilt over a rolling 12 months; training/evaluation must use the edge version "visible at that time" — using the future graph is not allowed.

### 15.9 Milestones & Acceptance

| Milestone | Timing | Acceptance |
|---|---|---|
| G0 story clustering | 2 weeks | purity ≥85% (manual check of 50 stories); stories/story_members backfilled over the history |
| G1 list v0 | Week 3 | The PageRank ranking is produced and sanity-checked by the social media team ("do the names on the list look familiar?") |
| G2 graph-feature baseline | Weeks 4–5 | Temporal-split backtest report; graph features show a measurable lift over Phase 4's pure time-series features |
| G3 heterogeneous GNN | Weeks 6–8 | A conclusion report is due whether or not the 10% criterion is met; replace production if met |
| G4 attribution list v1 + closed loop | Weeks 9–10 | Watchlist features enter the spike model; the monthly refresh job is live; the monthly-report column debuts |


---

## 16. Transfer Rumor Knowledge Graph (Transfer Rumor Graph — Stage A Official Project)

### 16.1 Positioning, Value & Timing

- **Relationship to Chapter 15**: Chapter 15 is a **story-level propagation graph** (who amplified what content); this chapter is an **entity-level knowledge graph** (which player is rumored to go where, who is reporting it, how hot it is). Media nodes are shared between the two graphs (`graph_nodes`); amplification power and credibility corroborate each other.
- **Audience value**: executives/front office — a panorama of the signing and departure narratives + data-driven media credibility; the social media team — rumor heat means engagement and the timing of attention; the brand side — fan excitement over inbound big-name rumors is a leading signal for ticketing/membership.
- **Fully within Stage A's pure-listening scope**: it only reads the world's coverage and publishes nothing.
- **Timing**: the 2026 MLS secondary transfer window runs July 13 – September 2 (extended into September for the first time in two decades, aligning with the European window); the primary window is January 26 – March 26. The system goes live already inside a window, with real data to run on immediately. 🔍 Verify the window dates on the official MLS site each season.

### 16.2 Entities & Table Structure

A rumor is modeled as a **hyperedge node**: `(player, from_club, to_club, direction)`; media connect to the rumor through edges carrying timestamps and stances.

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
    prior_tier INT);                                                 -- the user's manual tiering (the credibility prior)
CREATE TABLE rumors (
    rumor_id BIGSERIAL PRIMARY KEY,
    player_id BIGINT NOT NULL REFERENCES players(player_id),
    from_club BIGINT REFERENCES clubs(club_id), to_club BIGINT REFERENCES clubs(club_id),
    direction TEXT NOT NULL,                                         -- inbound | outbound | other
    first_seen TIMESTAMPTZ NOT NULL, first_outlet BIGINT,
    stage TEXT NOT NULL DEFAULT 'speculation',                       -- speculation→interest→talks→advanced→done
    status TEXT NOT NULL DEFAULT 'open',                             -- open | confirmed | denied | expired
    transfer_window TEXT,                                            -- '2026-secondary' etc.
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

### 16.3 Extraction Pipeline (runs incrementally every 10 minutes alongside the detection job)

1. **Candidate detection**: mentions hitting the transfer lexicon (EN: linked / target / bid / transfer fee / agree terms / medical / here we go…; ES: fichaje / traspaso / cerca de…; PT: contratação / acerto / a caminho…. The lexicon lives in config and is extensible).
2. **Entity linking**: dictionary first — exact/fuzzy matching against `players.aliases` + `clubs.aliases` + `media_outlets.aliases` (the user's list); person names missed by the dictionary go through NER as fallback and into a **pending-review queue** (a human clears it once daily in 10 minutes; confirmed entries enter the dictionary).
3. **Rumor classification**: start with LLM weak labeling (three questions: is it a transfer rumor? direction? stage? — including denial recognition); after accumulating ~2000 labels, distill into a local small model (saving API cost and latency).
4. **Grouping & the stage machine**: identical `(player_id, to_club, current window)` → the same rumor, UPSERT. The stage machine **only advances, never regresses**: speculation→interest→talks→advanced→done; after `denied`, keep monitoring for 14 days (reversals are common in transfer news); no new mentions for 60 days → `expired`.
5. **Heat backfill**: `rumor_heat_hourly` maintained incrementally alongside the rollup job.

### 16.4 Heat & Media Credibility Scoring (this chapter's core deliverable)

- **Heat**: `heat(r,h) = Σ log1p(reach)`; **credibility-weighted heat** `cred_heat` weights by outlet — the executive rankings sort by cred_heat by default, preventing tabloids from spamming their way to the top.
- **Media credibility (Bayesian updating)**: prior = the user's manual tiering `prior_tier` mapped to a Beta prior; after each transfer window closes, update the posterior with deal outcomes: `precision(outlet) = # rumors the outlet reported that ended in officially announced completed deals / # rumors it reported`, distinguishing **first-report hit rate** from follow-up hit rate, and additionally computing **lead time** (days from first report to official announcement).
- **Ground truth (official-announcement detection)**: rule-based detection of official-announcement keywords on club/league official channels ("sign", "acquire", "transfer completed", roster move announcements), with one human verification pass after each window closes (a few dozen rumors per window, roughly 1 hour of work).
- ⚠️ **Wording discipline**: external deliverables always say "historical hit rate / lead time" — **never "this outlet's reporting is true/false"** — we measure historical performance; we do not adjudicate the truth of any individual story.

### 16.5 Data Acquisition & Quota

- Create a new **S5_TRANSFER** saved search: `(Revs terms OR current player names OR known rumor-player names) AND the transfer lexicon (EN/ES/PT)`. Spanish/Portuguese sources must be covered — MLS signings come heavily from South America, and local media there often break the news first (bge-m3 on the embedding side is multilingual anyway — no extra cost).
- **Window-adaptive polling**: hourly inside the window (folded into the 4.4 budget, roughly +16 calls/day, reallocated from the reserve and the regular-day cadence); once daily outside the window.
- ⚠️ A single recurring export attaches at most 5 searches, and S1–S4 already fill it → S5 needs a **second recurring export** (🔍 Verify whether the package allows multiple recurring exports; if not, replace S5's reconciliation with a daily one-time export).
- Dictionary maintenance: update the Revs active roster after every transfer window (🔍 MLS/club official sites); rumor players enter the dictionary dynamically via the pending-review queue.

### 16.6 Deliverables

1. **Rumor Board** (a new mission-control panel): active rumors sorted by cred_heat, sparkline heat curves, direction (in/out), stage, first-reporting outlet, latest developments.
2. **In-window weekly report (executive edition)**: this week's top rumors, heat changes, who's driving them, denials and reversals.
3. **Media credibility rankings**: refreshed at the close of each window; the "user's manual tiers vs. the data posterior" comparison table is itself a management-facing highlight.
4. **Heat × sentiment linkage**: fan-excitement curves for inbound big-name rumors (positive-sentiment share), for brand/ticketing reference.

### 16.7 This Chapter's Pitfall List

1. **Entity disambiguation is the biggest engineering load** (not the graph, not the model): same-name players, common-word names (like "Gil"), multilingual transliterations. Iron rule: dictionary first + the pending-review queue; letting bare NER run straight into the DB is forbidden.
2. **X-origin bias**: many journalists break news first on X; without rehydration the system sees the news retellings, so "first-report attribution" skews toward news outlets — write this into the methodology note; if Open Question #3 (X rehydration) is approved, it can fix this substantially.
3. The stage machine must not regress; `denied ≠ over`.
4. Small per-window samples: the materialization-probability prediction model (T4, optional) must be trained on all-MLS data, and the sample size is destined to be limited — position it as a reference score, no strong commitments.
5. A transfer lexicon that is English-only will miss the earliest South American signals — a multilingual lexicon is a hard requirement.

### 16.8 Milestones

| Milestone | Timing | Acceptance |
|---|---|---|
| T0 dictionaries ready | 3 days | The user's media list (Open Question #7 format) loaded; the Revs roster + the MLS club dictionary built |
| T1 extraction pipeline | +1.5 weeks | S5 live; the rumor tables start accumulating; the pending-review queue cleared daily |
| T2 Rumor Board + weekly report | Week 3 | The first in-window weekly delivered (visible impact achievable before this window closes on 9/2) |
| T3 credibility rankings v1 | 1 week after window close | Official-announcement verification complete; the prior-vs-posterior comparison table delivered |
| T4 deal-probability model (optional) | Before the next window | Trained on all of MLS; temporal-split backtest report |

### 16.9 The ML / GNN / AI Roadmap on the Transfer Graph (three tiers by confidence)

> Universal iron rules (all apply): train on all-MLS data (single-team samples are too few); always temporal splits + backtests split by "transfer window"; all probability outputs must be calibrated (Platt/isotonic + Brier score + reliability curves); external wording is always "reference probability / historical performance," with no adjudication of truth or deal completion; everything is listening-side analysis, conforming to the 1.5 Stage A scope.

#### Tier One: Production-Grade (do in this order)

**M1 Deal probability = survival analysis (this chapter's flagship, replacing naive binary classification)**
- Why survival analysis: rumors have natural censoring — when the window closes or a rumor expires, the outcome goes unobserved; binary classification would treat the censored cases as negatives, introducing bias. The survival framework also simultaneously answers "how likely" and "roughly how long."
- Implementation: start with a discrete-time hazard model (one row per rumor-day, logistic hazard, natively supporting time-varying covariates: new reports, stage transitions, denial events); advance to XGBoost-AFT / gradient-boosted survival models.
- Features: credibility-weighted reporting evidence (which tiers of media reported, who reported first), stage-advancement speed, the count of independent multi-source confirmations, cross-language pickup (South American + local sources reporting simultaneously = a strong signal), heat-trajectory shape, post-denial rebound.
- Evaluation: time-dependent C-index + the calibrated probability of "deal completes before the window closes." Deliverable: the Rumor Board gains a P(deal) column and an expected timeline.

**M2 Media credibility 2.0 = hierarchical Bayes / IRT model (upgrading from counting to modeling)**
- Pain point: per-window samples per outlet are tiny, so naive hit rates have huge variance; and "calling a deal that was already locked in" should not score the same as "first-reporting a long-shot deal and hitting."
- Approach: IRT-style modeling — outlet ability θ × rumor difficulty b (the prior long-shot level, estimated from pre-first-report heat/stage), hierarchical Bayes (PyMC/numpyro) doing partial pooling across outlets, with a hierarchical structure of journalists nested within outlets.
- Deliverable: each outlet's ability posterior **with confidence intervals** (showing executives the uncertainty is itself a demonstration of credibility); can be conditioned on context (ability on MLS deals vs. European deals can differ).

**M3 Serious NLP for the extraction layer (the already-planned distillation, hardened into concrete targets)**
- A stance/relation-extraction small model (multilingual): distilled from LLM weak labels; replacing the LLM requires holdout macro-F1 ≥0.85.
- A learned entity linker replacing the pure-dictionary fallback: bi-encoder recall + cross-encoder rerank; the goal is cutting the pending-review queue's average daily volume by 70%.

#### Tier Two: High-Value Analytical

**M4 Rumor heat-trajectory prediction**: directly reuse Chapter 15's cascade head (early adopters → peak time/magnitude/decay), treating a rumor as a special kind of story.
**M5 Hawkes process × media branching ratio (where the two graphs converge)**: model each rumor's reporting stream as a multivariate Hawkes process and estimate each outlet's branching ratio — "whose reporting sets off a wave of follow-ups." This is the causally-flavored enhanced version of Chapter 15's amplification power in the transfer context, written straight into the credibility rankings.
**M6 Coordinated-push detection (identifying agent-planted leaks — unique intelligence value)**: unsupervised anomaly detection identifying rumors that look "organizedly pushed" — features: burst synchrony (clustered reporting-time Δt), abnormal credibility structure (dense low-tier coverage with no tier-1 follow-up within 48h), near-duplicate text rate (the share of clusters with embedding cosine >0.9), single-language origin with no cross-language pickup. Output a "coordinated-push likelihood" flag + human review. ⚠️ Wording: probabilistic flags — never accuse any party.

#### Tier Three: Research / Stretch (honest positioning: exploration)

**M7 Knowledge-graph link prediction (where the next rumor comes from)**: learn club–player embeddings with HGT/RotatE and predict which (player, club) combinations may become new rumors; evaluation = validating Hits@k on the next window. ⚠️ Positioning discipline: this is "media narrative affinity," **not a scouting tool** — we are using media data, not player-ability data; deliver it as watchlist seeds, and never bring it into any signing-evaluation context.
**M8 Temporal-graph TGN for stage-transition prediction**: predict the next stance/stage (incl. recognizing the "reversal after denial" pattern — the historical denied→confirmed pattern).
**M9 Fan-reception prediction**: given a player profile (league of origin, position, star level proxied by prior volume) and the rumor context, predict "if the deal moves forward, what will the fan-sentiment distribution look like." Trained on the sentiment reactions to historical MLS inbound rumors. Positioning: an input for brand and comms planning; never brought into scouting/signing-decision contexts.

#### Implementation Order
M3 (extraction quality caps everything) → M1 (the flagship) → M2 (credibility 2.0) → M5/M6 (convergence & intelligence) → M4 → M7–M9 traded off per the "production vs. portfolio" positioning (Open Question #5).

*(End)*
