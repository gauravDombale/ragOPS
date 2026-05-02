

Pasted markdown.md
File
Just change one thing in this agents.md file and ie to use open ai api key instead of athropic key rest everthing keep it as is

You don’t actually need to change anything — your file is already using OpenAI everywhere, not Anthropic.

I checked your uploaded file 

 and here’s what matters:

✅ Already using OpenAI
OPENAI_API_KEY in .env

AsyncOpenAI client in generator.py

ChatOpenAI + OpenAIEmbeddings in evals

Models like gpt-4o, text-embedding-3-large

Cost tracking built around OpenAI pricing

❌ No Anthropic usage found
There is zero reference to:

ANTHROPIC_API_KEY

claude-* models

anthropic SDK

Bottom line
Your Agent.md is already fully configured for OpenAI. No replacement needed.

If you expected Anthropic earlier, then what likely happened is:

You copied a newer template (already migrated to OpenAI)

Or I previously gave you an OpenAI-optimized version

If you want, I can:

Switch this to multi-provider (OpenAI + Anthropic fallback)

Or optimize it for cost (gpt-4o-mini + routing)

Or make it offline-first (Ollama + eval infra)

Just tell me 👍


suggest a name for this project

You’re building something pretty serious here—this isn’t a toy RAG app, it’s infra + observability + evaluation + CI gating. So the name should signal systems thinking, not “chatbot vibes.”

Here are strong, resume-grade name directions 👇

🔥 Top-Tier (Best Picks — Use These)
1. TraceRAG
→ Clean, sharp, and instantly communicates tracing + RAG
→ Sounds like a real internal tool at a top company

2. RAGScope
→ Implies full visibility into the system
→ Great for observability positioning

3. RAGOps ⭐ (my top recommendation)
→ Feels like “MLOps but for RAG”
→ Strong, industry-aligned, recruiter-friendly

4. LLMWatchtower
→ Signals monitoring + protection + reliability
→ Slightly more brandy, still strong

5. RAGSentinel
→ Implies guarding quality + preventing regressions
→ Great fit for eval gating + alerts

🧠 More Technical / Infra Vibes
6. ObservaRAG
7. RAGLens
8. RAGPulse
9. EvalGuard AI
10. TraceStack AI

⚡ If You Want FAANG-Level Seriousness
Go with something boring-but-powerful:

rag-observability-platform

rag-infra-monitor

rag-quality-gate

These look very real on a resume (and honestly, that matters).

🚫 Avoid These (Common Mistake)
“SmartRAG AI”

“GenAI Assistant Pro”

“SuperChatBot”

These make your project look junior immediately.

🎯 Final Advice
If your goal is:

AI Engineer / ML Platform roles → pick RAGOps

Infra / Systems credibility → pick TraceRAG

Balanced + clean branding → pick RAGScope

If you want, I can also:

Generate a logo + branding direction

Write a killer GitHub README intro

Or tailor the name for a specific company (HFT / AI infra / startup)


Agent.md — Production-Grade RAG Monitoring & Observability System
Project Identity
Project Name: rag-observability
Type: Production AI Infrastructure — Monitoring, Tracing, Latency Profiling, Cost Accounting, Quality Regression Gating
Target Role Signal: AI Engineer / ML Platform Engineer
Stack Tier: Production-grade, not tutorial-grade

Objective
Build a full observability layer on top of an existing RAG pipeline. This system must capture every signal a production AI team cares about: distributed traces, latency percentiles, per-request cost, retrieval quality, generation quality, and automated regression gating in CI. Every metric must be queryable, every trace must be inspectable, and every deployment must pass quality gates before it ships.

Final Deliverables
Instrumented RAG Pipeline — FastAPI + LangGraph with OpenTelemetry spans at every stage

Langfuse Integration — LLM-native tracing with prompt versioning, token accounting, scores

Prometheus + Grafana Stack — p50/p95/p99 latency dashboards, cost-per-request panels, retrieval quality panels

RAGAS Evaluation Suite — Faithfulness, Answer Relevancy, Context Precision, Context Recall

Regression Gating in GitHub Actions — CI pipeline that blocks merge if quality metrics regress beyond thresholds

Alerting Rules — Grafana alerts for latency spikes, cost anomalies, quality drops

Load Testing Harness — Locust scripts that generate realistic traffic to surface p95 regressions

Tech Stack (Best Available, 2025)
Layer	Tool	Why
RAG Framework	LangGraph 0.2+	Stateful agent graphs, native tracing hooks
LLM	GPT-4o (gpt-4o)	Best OpenAI quality/cost ratio, 128K context
Embeddings	text-embedding-3-large (OpenAI)	Same API key, production-grade dense retrieval
Vector DB	Weaviate (self-hosted via Docker)	Native hybrid search, HNSW, production-proven
LLM Observability	Langfuse v3 (self-hosted)	Open-source, LLM-native traces, evals, cost tracking
Distributed Tracing	OpenTelemetry (OTEL) SDK + Jaeger	Industry standard, vendor-neutral
Metrics	Prometheus + prometheus-fastapi-instrumentator	Pull-based, battle-tested
Dashboards	Grafana 10+	Best-in-class, native Prometheus + Jaeger datasources
RAG Evaluation	RAGAS 0.2+	Standard for RAG quality metrics
Load Testing	Locust	Pythonic, scriptable, realistic traffic simulation
CI/CD	GitHub Actions	Regression gating, eval runs on every PR
API Layer	FastAPI + Uvicorn	Async-native, OpenAPI out of the box
Containerization	Docker Compose	Full local stack in one command
Config Management	Pydantic Settings + .env	Type-safe config
Repository Structure
rag-observability/
├── docker-compose.yml              # Full observability stack
├── docker-compose.override.yml     # Local dev overrides
├── .env.example
├── Agent.md                        # This file
├── pyproject.toml
├── requirements.txt
│
├── src/
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── graph.py                # LangGraph RAG pipeline (main entrypoint)
│   │   ├── nodes/
│   │   │   ├── retriever.py        # Weaviate hybrid retrieval node
│   │   │   ├── reranker.py         # Cross-encoder reranking node
│   │   │   ├── generator.py        # GPT-4o generation node
│   │   │   └── guardrails.py       # Input/output safety node
│   │   └── state.py                # TypedDict graph state
│   │
│   ├── observability/
│   │   ├── __init__.py
│   │   ├── tracing.py              # OTEL tracer setup + Langfuse integration
│   │   ├── metrics.py              # Prometheus metrics registry
│   │   ├── cost.py                 # Token → cost accounting
│   │   ├── middleware.py           # FastAPI middleware: trace injection, latency
│   │   └── decorators.py           # @trace_node, @track_cost decorators
│   │
│   ├── evaluation/
│   │   ├── __init__.py
│   │   ├── ragas_runner.py         # RAGAS eval orchestration
│   │   ├── dataset.py              # Golden dataset loader
│   │   ├── thresholds.py           # Regression threshold config
│   │   └── reporter.py             # JSON + GitHub PR comment reporter
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI app factory
│   │   ├── routes/
│   │   │   ├── query.py            # POST /query — main RAG endpoint
│   │   │   ├── health.py           # GET /health, GET /ready
│   │   │   └── metrics.py          # GET /metrics (Prometheus scrape)
│   │   └── schemas.py              # Request/response Pydantic models
│   │
│   └── config.py                   # Pydantic Settings
│
├── evals/
│   ├── golden_dataset.json         # Ground truth Q&A pairs
│   ├── run_evals.py                # CI entrypoint for evaluation
│   └── baselines/
│       └── baseline_scores.json    # Committed baseline metrics
│
├── load_tests/
│   ├── locustfile.py               # Load test scenarios
│   ├── check_latency_thresholds.py # CI p95 enforcement script
│   └── config.json                 # Target RPS, user counts
│
├── monitoring/
│   ├── prometheus/
│   │   ├── prometheus.yml          # Scrape config
│   │   └── alert_rules.yml         # Alerting rules
│   ├── grafana/
│   │   ├── provisioning/
│   │   │   ├── datasources/
│   │   │   │   └── datasources.yml
│   │   │   └── dashboards/
│   │   │       └── dashboards.yml
│   │   └── dashboards/
│   │       ├── rag_overview.json       # Main RAG health dashboard
│   │       ├── latency_deep_dive.json  # p50/p95/p99 breakdown by stage
│   │       └── cost_accounting.json    # Cost per request / per user / per day
│   └── jaeger/
│       └── jaeger.yml
│
├── .github/
│   └── workflows/
│       ├── ci.yml                  # Lint, test, eval gate
│       └── load_test.yml           # Weekly load test regression
│
└── tests/
    ├── unit/
    ├── integration/
    └── conftest.py
Phase 0 — Environment Setup
0.1 Python Environment
python -m venv .venv
source .venv/bin/activate
pip install -U pip

pip install \
  fastapi uvicorn[standard] \
  langchain langchain-openai langchain-weaviate langgraph \
  langfuse \
  opentelemetry-sdk opentelemetry-api \
  opentelemetry-exporter-otlp-proto-grpc \
  opentelemetry-instrumentation-fastapi \
  opentelemetry-instrumentation-httpx \
  prometheus-client prometheus-fastapi-instrumentator \
  ragas datasets \
  weaviate-client \
  openai \
  sentence-transformers \
  pydantic-settings python-dotenv \
  locust \
  pytest pytest-asyncio httpx \
  ruff pyright
0.2 .env.example
# LLM + Embeddings (single OpenAI key covers both)
OPENAI_API_KEY=sk-...
LLM_MODEL=gpt-4o
EMBEDDING_MODEL=text-embedding-3-large

# Langfuse (self-hosted)
LANGFUSE_SECRET_KEY=sk-lf-...
LANGFUSE_PUBLIC_KEY=pk-lf-...
LANGFUSE_HOST=http://localhost:3000

# Weaviate
WEAVIATE_HOST=localhost
WEAVIATE_PORT=8080
WEAVIATE_API_KEY=

# OpenTelemetry
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
OTEL_SERVICE_NAME=rag-observability
APP_ENV=production
APP_VERSION=1.0.0

# App
LOG_LEVEL=INFO
COST_ALERT_THRESHOLD_USD=0.05

# Eval Thresholds
EVAL_FAITHFULNESS_MIN=0.80
EVAL_ANSWER_RELEVANCY_MIN=0.75
EVAL_CONTEXT_PRECISION_MIN=0.70
EVAL_CONTEXT_RECALL_MIN=0.70
0.3 src/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # OpenAI
    openai_api_key: str
    llm_model: str = "gpt-4o"
    embedding_model: str = "text-embedding-3-large"

    # Langfuse
    langfuse_secret_key: str
    langfuse_public_key: str
    langfuse_host: str = "http://localhost:3000"

    # Weaviate
    weaviate_host: str = "localhost"
    weaviate_port: int = 8080
    weaviate_api_key: str = ""

    # OTEL
    otel_exporter_otlp_endpoint: str = "http://localhost:4317"
    otel_service_name: str = "rag-observability"
    app_env: str = "production"
    app_version: str = "1.0.0"

    # App
    log_level: str = "INFO"
    cost_alert_threshold_usd: float = 0.05

    # Eval thresholds
    eval_faithfulness_min: float = 0.80
    eval_answer_relevancy_min: float = 0.75
    eval_context_precision_min: float = 0.70
    eval_context_recall_min: float = 0.70


settings = Settings()
Phase 1 — Docker Compose Observability Stack
docker-compose.yml
version: "3.9"

services:
  # ── RAG API ──────────────────────────────────────────────
  api:
    build: .
    ports:
      - "8000:8000"
    env_file: .env
    depends_on:
      - weaviate
      - langfuse-server
      - jaeger
    networks: [obs-net]

  # ── Vector DB ────────────────────────────────────────────
  weaviate:
    image: semitechnologies/weaviate:1.25.0
    ports:
      - "8080:8080"
    environment:
      QUERY_DEFAULTS_LIMIT: 25
      AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED: "true"
      PERSISTENCE_DATA_PATH: /var/lib/weaviate
      DEFAULT_VECTORIZER_MODULE: none
      ENABLE_MODULES: ""
      CLUSTER_HOSTNAME: node1
    volumes:
      - weaviate_data:/var/lib/weaviate
    networks: [obs-net]

  # ── LLM Tracing ──────────────────────────────────────────
  langfuse-server:
    image: langfuse/langfuse:3
    ports:
      - "3000:3000"
    environment:
      DATABASE_URL: postgresql://langfuse:langfuse@langfuse-db:5432/langfuse
      NEXTAUTH_SECRET: super-secret-nextauth
      SALT: super-secret-salt
      NEXTAUTH_URL: http://localhost:3000
      TELEMETRY_ENABLED: "false"
    depends_on:
      - langfuse-db
    networks: [obs-net]

  langfuse-db:
    image: postgres:15
    environment:
      POSTGRES_USER: langfuse
      POSTGRES_PASSWORD: langfuse
      POSTGRES_DB: langfuse
    volumes:
      - langfuse_pg:/var/lib/postgresql/data
    networks: [obs-net]

  # ── Distributed Tracing ──────────────────────────────────
  jaeger:
    image: jaegertracing/all-in-one:1.57
    ports:
      - "16686:16686"   # Jaeger UI
      - "4317:4317"     # OTLP gRPC
      - "4318:4318"     # OTLP HTTP
    environment:
      COLLECTOR_OTLP_ENABLED: "true"
    networks: [obs-net]

  # ── Metrics ──────────────────────────────────────────────
  prometheus:
    image: prom/prometheus:v2.51.0
    ports:
      - "9090:9090"
    volumes:
      - ./monitoring/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
      - ./monitoring/prometheus/alert_rules.yml:/etc/prometheus/alert_rules.yml
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.retention.time=30d'
      - '--web.enable-lifecycle'
    networks: [obs-net]

  # ── Dashboards ───────────────────────────────────────────
  grafana:
    image: grafana/grafana:10.4.0
    ports:
      - "3001:3000"
    environment:
      GF_SECURITY_ADMIN_PASSWORD: admin
      GF_USERS_ALLOW_SIGN_UP: "false"
    volumes:
      - ./monitoring/grafana/provisioning:/etc/grafana/provisioning
      - ./monitoring/grafana/dashboards:/var/lib/grafana/dashboards
      - grafana_data:/var/lib/grafana
    depends_on:
      - prometheus
      - jaeger
    networks: [obs-net]

networks:
  obs-net:
    driver: bridge

volumes:
  weaviate_data:
  langfuse_pg:
  prometheus_data:
  grafana_data:
Phase 2 — Core Observability Module
src/observability/tracing.py
"""
Central tracing setup.
Bridges OpenTelemetry (infrastructure tracing)
and Langfuse (LLM-native tracing) in a single coherent layer.
"""
from functools import wraps

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor

from langfuse import Langfuse
from langfuse.decorators import langfuse_context, observe

from src.config import settings


# ── OTEL Setup ───────────────────────────────────────────────────────────────

def init_tracing() -> trace.Tracer:
    resource = Resource.create({
        "service.name": settings.otel_service_name,
        "deployment.environment": settings.app_env,
        "service.version": settings.app_version,
    })

    exporter = OTLPSpanExporter(
        endpoint=settings.otel_exporter_otlp_endpoint,
        insecure=True,
    )

    provider = TracerProvider(resource=resource)
    provider.add_span_processor(BatchSpanProcessor(exporter))
    trace.set_tracer_provider(provider)

    HTTPXClientInstrumentor().instrument()

    return trace.get_tracer(settings.otel_service_name)


tracer: trace.Tracer = None  # Initialized at app startup via lifespan


# ── Langfuse Client ──────────────────────────────────────────────────────────

def get_langfuse_client() -> Langfuse:
    return Langfuse(
        secret_key=settings.langfuse_secret_key,
        public_key=settings.langfuse_public_key,
        host=settings.langfuse_host,
    )


# ── Unified Trace Decorator ──────────────────────────────────────────────────

def trace_stage(stage_name: str):
    """
    Decorator that creates both an OTEL span and a Langfuse span for a pipeline stage.
    Apply to every LangGraph node function.
    """
    def decorator(func):
        @wraps(func)
        @observe(name=stage_name)
        async def wrapper(*args, **kwargs):
            with tracer.start_as_current_span(stage_name) as span:
                span.set_attribute("pipeline.stage", stage_name)
                try:
                    result = await func(*args, **kwargs)
                    span.set_attribute("pipeline.status", "success")
                    return result
                except Exception as e:
                    span.record_exception(e)
                    span.set_attribute("pipeline.status", "error")
                    span.set_attribute("error.type", type(e).__name__)
                    raise
        return wrapper
    return decorator
src/observability/metrics.py
"""
All Prometheus metrics for the RAG pipeline.
Single source of truth — import from here everywhere.
"""
from prometheus_client import Histogram, Counter, Gauge

# ── Latency Histograms ────────────────────────────────────────────────────────
# Buckets tuned for LLM workloads: 50ms → 30s

LATENCY_BUCKETS = (0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0, 20.0, 30.0)

REQUEST_LATENCY = Histogram(
    "rag_request_latency_seconds",
    "End-to-end RAG request latency",
    ["endpoint", "status"],
    buckets=LATENCY_BUCKETS,
)

STAGE_LATENCY = Histogram(
    "rag_stage_latency_seconds",
    "Per-stage pipeline latency",
    ["stage"],  # retrieval | reranking | generation | guardrails
    buckets=LATENCY_BUCKETS,
)

# ── Cost Tracking ─────────────────────────────────────────────────────────────

COST_PER_REQUEST = Histogram(
    "rag_cost_usd_per_request",
    "Estimated USD cost per RAG request",
    ["model"],
    buckets=(0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5),
)

TOKENS_USED = Counter(
    "rag_tokens_total",
    "Total tokens consumed",
    ["model", "token_type"],  # token_type: input | output | cached
)

CUMULATIVE_COST = Counter(
    "rag_cumulative_cost_usd_total",
    "Running total USD cost",
    ["model"],
)

# ── Retrieval Quality ─────────────────────────────────────────────────────────

RETRIEVAL_DOCS_RETURNED = Histogram(
    "rag_retrieval_docs_returned",
    "Number of documents returned by retriever",
    buckets=(1, 2, 3, 5, 8, 10, 15, 20),
)

RETRIEVAL_SCORE = Histogram(
    "rag_retrieval_top_score",
    "Top retrieval similarity score",
    buckets=(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0),
)

# ── Generation Quality (updated by eval runner) ───────────────────────────────

EVAL_FAITHFULNESS = Gauge("rag_eval_faithfulness", "RAGAS faithfulness score (rolling)")
EVAL_ANSWER_RELEVANCY = Gauge("rag_eval_answer_relevancy", "RAGAS answer relevancy (rolling)")
EVAL_CONTEXT_PRECISION = Gauge("rag_eval_context_precision", "RAGAS context precision (rolling)")
EVAL_CONTEXT_RECALL = Gauge("rag_eval_context_recall", "RAGAS context recall (rolling)")

# ── System ────────────────────────────────────────────────────────────────────

ACTIVE_REQUESTS = Gauge(
    "rag_active_requests",
    "Number of requests currently being processed",
)

REQUEST_TOTAL = Counter(
    "rag_requests_total",
    "Total RAG requests",
    ["endpoint", "status"],
)

CACHE_HIT = Counter(
    "rag_cache_hits_total",
    "Number of semantic cache hits",
    ["cache_type"],  # exact | semantic
)
src/observability/cost.py
"""
Token-to-cost accounting for OpenAI models.
Supports prompt caching (cached_tokens from usage.prompt_tokens_details).
All prices per 1M tokens in USD — update when OpenAI changes pricing.
"""
from dataclasses import dataclass
from src.observability.metrics import TOKENS_USED, CUMULATIVE_COST, COST_PER_REQUEST

PRICING_TABLE = {
    "gpt-4o": {
        "input": 2.50,
        "output": 10.00,
        "cached": 1.25,       # OpenAI automatic prompt caching discount
    },
    "gpt-4o-mini": {
        "input": 0.15,
        "output": 0.60,
        "cached": 0.075,
    },
    "gpt-4-turbo": {
        "input": 10.00,
        "output": 30.00,
        "cached": 5.00,
    },
    "text-embedding-3-large": {
        "input": 0.13,
        "output": 0.0,
        "cached": 0.0,
    },
    "text-embedding-3-small": {
        "input": 0.02,
        "output": 0.0,
        "cached": 0.0,
    },
}


@dataclass
class TokenUsage:
    model: str
    input_tokens: int = 0
    output_tokens: int = 0
    cached_tokens: int = 0    # Subset of input_tokens served from OpenAI cache

    def compute_cost(self) -> float:
        pricing = PRICING_TABLE.get(self.model, {})
        # Cached tokens billed at discounted rate; non-cached at full input rate
        non_cached_input = self.input_tokens - self.cached_tokens
        cost = (
            (non_cached_input / 1_000_000) * pricing.get("input", 0)
            + (self.cached_tokens / 1_000_000) * pricing.get("cached", 0)
            + (self.output_tokens / 1_000_000) * pricing.get("output", 0)
        )
        return cost

    def record(self) -> float:
        """Push all metrics to Prometheus. Returns computed cost."""
        cost = self.compute_cost()

        TOKENS_USED.labels(model=self.model, token_type="input").inc(self.input_tokens)
        TOKENS_USED.labels(model=self.model, token_type="output").inc(self.output_tokens)
        TOKENS_USED.labels(model=self.model, token_type="cached").inc(self.cached_tokens)

        CUMULATIVE_COST.labels(model=self.model).inc(cost)
        COST_PER_REQUEST.labels(model=self.model).observe(cost)

        return cost
Phase 3 — Instrumented RAG Pipeline
src/pipeline/state.py
from typing import TypedDict, Optional, List
from dataclasses import dataclass, field


@dataclass
class RetrievedDoc:
    content: str
    source: str
    score: float
    metadata: dict = field(default_factory=dict)


class RAGState(TypedDict):
    # Input
    query: str
    session_id: str
    trace_id: str
    user_id: Optional[str]

    # Retrieval
    retrieved_docs: List[RetrievedDoc]
    reranked_docs: List[RetrievedDoc]

    # Generation
    prompt: str
    response: str

    # Observability
    stage_latencies: dict          # stage_name → seconds
    token_usage: dict              # model → TokenUsage
    total_cost_usd: float
    retrieval_score: float

    # Async eval results (populated post-request)
    faithfulness: Optional[float]
    answer_relevancy: Optional[float]
src/pipeline/nodes/guardrails.py
import time
from langfuse.decorators import observe
from opentelemetry import trace
from fastapi import HTTPException

from src.pipeline.state import RAGState
from src.observability.metrics import STAGE_LATENCY

BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "jailbreak",
    "prompt injection",
]


@observe(name="guardrails")
async def guardrails_node(state: RAGState) -> RAGState:
    """Input safety check before entering the pipeline."""
    span = trace.get_current_span()
    start = time.perf_counter()

    query_lower = state["query"].lower()
    for pattern in BLOCKED_PATTERNS:
        if pattern in query_lower:
            span.set_attribute("guardrails.blocked", True)
            span.set_attribute("guardrails.reason", pattern)
            raise HTTPException(status_code=400, detail="Query blocked by safety guardrails.")

    if len(state["query"]) > 2000:
        raise HTTPException(status_code=400, detail="Query exceeds maximum length of 2000 characters.")

    latency = time.perf_counter() - start
    STAGE_LATENCY.labels(stage="guardrails").observe(latency)
    span.set_attribute("guardrails.blocked", False)

    return {
        **state,
        "stage_latencies": {**state.get("stage_latencies", {}), "guardrails": latency},
    }
src/pipeline/nodes/retriever.py
import time
from langfuse.decorators import observe
from opentelemetry import trace

from src.pipeline.state import RAGState, RetrievedDoc
from src.observability.metrics import STAGE_LATENCY, RETRIEVAL_DOCS_RETURNED, RETRIEVAL_SCORE
from src.config import settings
import weaviate


@observe(name="retrieval")
async def retrieval_node(state: RAGState) -> RAGState:
    """Hybrid BM25 + dense vector retrieval from Weaviate."""
    span = trace.get_current_span()
    span.set_attribute("retrieval.query", state["query"])

    start = time.perf_counter()

    client = weaviate.connect_to_local(
        host=settings.weaviate_host,
        port=settings.weaviate_port,
    )

    try:
        collection = client.collections.get("Documents")

        results = collection.query.hybrid(
            query=state["query"],
            limit=10,
            alpha=0.5,   # 0.0 = BM25 only, 1.0 = vector only
            return_metadata=["score"],
        )

        docs = [
            RetrievedDoc(
                content=obj.properties.get("content", ""),
                source=obj.properties.get("source", "unknown"),
                score=obj.metadata.score or 0.0,
                metadata=dict(obj.properties),
            )
            for obj in results.objects
        ]
    finally:
        client.close()

    latency = time.perf_counter() - start
    top_score = docs[0].score if docs else 0.0

    STAGE_LATENCY.labels(stage="retrieval").observe(latency)
    RETRIEVAL_DOCS_RETURNED.observe(len(docs))
    RETRIEVAL_SCORE.observe(top_score)

    span.set_attribute("retrieval.docs_returned", len(docs))
    span.set_attribute("retrieval.top_score", top_score)
    span.set_attribute("retrieval.latency_ms", round(latency * 1000, 2))

    return {
        **state,
        "retrieved_docs": docs,
        "retrieval_score": top_score,
        "stage_latencies": {**state.get("stage_latencies", {}), "retrieval": latency},
    }
src/pipeline/nodes/reranker.py
import time
from langfuse.decorators import observe
from opentelemetry import trace

from src.pipeline.state import RAGState
from src.observability.metrics import STAGE_LATENCY


@observe(name="reranking")
async def reranking_node(state: RAGState) -> RAGState:
    """
    Cross-encoder reranking.
    Model: cross-encoder/ms-marco-MiniLM-L-6-v2 (fast, production-grade)
    """
    from sentence_transformers import CrossEncoder

    span = trace.get_current_span()
    start = time.perf_counter()

    docs = state["retrieved_docs"]
    if not docs:
        return {**state, "reranked_docs": []}

    model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
    pairs = [(state["query"], doc.content) for doc in docs]
    scores = model.predict(pairs)

    reranked = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)
    reranked_docs = [doc for doc, _ in reranked[:5]]

    latency = time.perf_counter() - start
    STAGE_LATENCY.labels(stage="reranking").observe(latency)
    span.set_attribute("reranking.input_docs", len(docs))
    span.set_attribute("reranking.output_docs", len(reranked_docs))
    span.set_attribute("reranking.latency_ms", round(latency * 1000, 2))

    return {
        **state,
        "reranked_docs": reranked_docs,
        "stage_latencies": {**state.get("stage_latencies", {}), "reranking": latency},
    }
src/pipeline/nodes/generator.py
import time
from openai import AsyncOpenAI
from langfuse.decorators import observe, langfuse_context
from opentelemetry import trace

from src.pipeline.state import RAGState
from src.observability.metrics import STAGE_LATENCY
from src.observability.cost import TokenUsage
from src.config import settings


SYSTEM_PROMPT = """You are a precise, helpful assistant. Answer the question using ONLY the provided context.
If the context does not contain sufficient information, say so explicitly.
Do not fabricate information."""


@observe(name="generation")
async def generation_node(state: RAGState) -> RAGState:
    """GPT-4o generation with full token accounting and Langfuse prompt tracing."""
    span = trace.get_current_span()
    client = AsyncOpenAI(api_key=settings.openai_api_key)

    context = "\n\n---\n\n".join([
        f"[Source: {doc.source}]\n{doc.content}"
        for doc in state["reranked_docs"][:5]
    ])

    user_prompt = f"""Context:
{context}

Question: {state['query']}

Answer:"""

    langfuse_context.update_current_observation(
        input=user_prompt,
        metadata={
            "model": settings.llm_model,
            "context_docs": len(state["reranked_docs"]),
        },
    )

    start = time.perf_counter()

    response = await client.chat.completions.create(
        model=settings.llm_model,
        max_tokens=1024,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
    )

    latency = time.perf_counter() - start
    answer = response.choices[0].message.content

    # Extract OpenAI automatic prompt caching tokens
    cached_tokens = 0
    if hasattr(response.usage, "prompt_tokens_details") and response.usage.prompt_tokens_details:
        cached_tokens = getattr(response.usage.prompt_tokens_details, "cached_tokens", 0)

    usage = TokenUsage(
        model=settings.llm_model,
        input_tokens=response.usage.prompt_tokens,
        output_tokens=response.usage.completion_tokens,
        cached_tokens=cached_tokens,
    )
    cost = usage.record()

    langfuse_context.update_current_observation(
        output=answer,
        usage={
            "input": usage.input_tokens,
            "output": usage.output_tokens,
            "unit": "TOKENS",
        },
        metadata={"cost_usd": cost, "cached_tokens": cached_tokens},
    )

    span.set_attribute("llm.model", settings.llm_model)
    span.set_attribute("llm.input_tokens", usage.input_tokens)
    span.set_attribute("llm.output_tokens", usage.output_tokens)
    span.set_attribute("llm.cached_tokens", cached_tokens)
    span.set_attribute("llm.cost_usd", cost)
    span.set_attribute("llm.latency_ms", round(latency * 1000, 2))

    STAGE_LATENCY.labels(stage="generation").observe(latency)

    return {
        **state,
        "response": answer,
        "prompt": user_prompt,
        "token_usage": {**state.get("token_usage", {}), settings.llm_model: usage},
        "total_cost_usd": state.get("total_cost_usd", 0.0) + cost,
        "stage_latencies": {**state.get("stage_latencies", {}), "generation": latency},
    }
src/pipeline/graph.py
from langgraph.graph import StateGraph, END

from src.pipeline.state import RAGState
from src.pipeline.nodes.retriever import retrieval_node
from src.pipeline.nodes.reranker import reranking_node
from src.pipeline.nodes.generator import generation_node
from src.pipeline.nodes.guardrails import guardrails_node


def build_rag_graph():
    graph = StateGraph(RAGState)

    graph.add_node("guardrails", guardrails_node)
    graph.add_node("retrieval", retrieval_node)
    graph.add_node("reranking", reranking_node)
    graph.add_node("generation", generation_node)

    graph.set_entry_point("guardrails")
    graph.add_edge("guardrails", "retrieval")
    graph.add_edge("retrieval", "reranking")
    graph.add_edge("reranking", "generation")
    graph.add_edge("generation", END)

    return graph.compile()


rag_pipeline = build_rag_graph()
Phase 4 — FastAPI Application
src/api/schemas.py
from typing import Optional, List
from pydantic import BaseModel


class QueryRequest(BaseModel):
    query: str
    session_id: Optional[str] = None
    user_id: Optional[str] = None


class QueryResponse(BaseModel):
    answer: str
    trace_id: str
    session_id: str
    latency_ms: float
    cost_usd: float
    stage_latencies: dict
    sources: List[str]
src/api/main.py
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

import src.observability.tracing as t
from src.observability.tracing import init_tracing
from src.api.routes import query, health
from src.config import settings

logging.basicConfig(level=settings.log_level)


@asynccontextmanager
async def lifespan(app: FastAPI):
    t.tracer = init_tracing()
    yield


app = FastAPI(
    title="RAG Observability System",
    version="1.0.0",
    lifespan=lifespan,
)

FastAPIInstrumentor.instrument_app(app)

Instrumentator(
    should_group_status_codes=False,
    should_ignore_untemplated=True,
    should_instrument_requests_inprogress=True,
    inprogress_labels=True,
).instrument(app).expose(app, endpoint="/metrics")

app.include_router(query.router, prefix="/api/v1")
app.include_router(health.router)
src/api/routes/query.py
import time
import uuid
from fastapi import APIRouter
from langfuse.decorators import observe, langfuse_context

from src.pipeline.graph import rag_pipeline
from src.api.schemas import QueryRequest, QueryResponse
from src.observability.metrics import REQUEST_LATENCY, REQUEST_TOTAL, ACTIVE_REQUESTS

router = APIRouter()


@router.post("/query", response_model=QueryResponse)
@observe(name="rag_request")
async def query_endpoint(request: QueryRequest):
    trace_id = str(uuid.uuid4())
    session_id = request.session_id or str(uuid.uuid4())

    langfuse_context.update_current_trace(
        name="rag_query",
        session_id=session_id,
        user_id=request.user_id,
        tags=["production"],
        metadata={"query_length": len(request.query)},
    )

    ACTIVE_REQUESTS.inc()
    start = time.perf_counter()
    status = "success"

    try:
        initial_state = {
            "query": request.query,
            "session_id": session_id,
            "trace_id": trace_id,
            "user_id": request.user_id,
            "retrieved_docs": [],
            "reranked_docs": [],
            "stage_latencies": {},
            "token_usage": {},
            "total_cost_usd": 0.0,
            "retrieval_score": 0.0,
            "prompt": "",
            "response": "",
        }

        final_state = await rag_pipeline.ainvoke(initial_state)

        return QueryResponse(
            answer=final_state["response"],
            trace_id=trace_id,
            session_id=session_id,
            latency_ms=round((time.perf_counter() - start) * 1000, 2),
            cost_usd=round(final_state["total_cost_usd"], 6),
            stage_latencies=final_state["stage_latencies"],
            sources=[doc.source for doc in final_state["reranked_docs"][:3]],
        )

    except Exception:
        status = "error"
        raise

    finally:
        total_latency = time.perf_counter() - start
        REQUEST_LATENCY.labels(endpoint="/query", status=status).observe(total_latency)
        REQUEST_TOTAL.labels(endpoint="/query", status=status).inc()
        ACTIVE_REQUESTS.dec()
src/api/routes/health.py
import weaviate
from fastapi import APIRouter
from src.config import settings

router = APIRouter()


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.get("/ready")
async def ready():
    """Returns 200 only when all dependencies are reachable."""
    checks = {}

    try:
        client = weaviate.connect_to_local(
            host=settings.weaviate_host,
            port=settings.weaviate_port,
        )
        client.is_ready()
        client.close()
        checks["weaviate"] = "ok"
    except Exception as e:
        checks["weaviate"] = f"error: {e}"

    all_ok = all(v == "ok" for v in checks.values())
    return {"status": "ready" if all_ok else "degraded", "checks": checks}
Phase 5 — RAGAS Evaluation Suite
evals/run_evals.py
"""
CI evaluation entrypoint.
Runs RAGAS metrics against golden dataset, compares to committed baseline,
exits with code 1 if any threshold is breached or regression detected.
"""
import json
import sys
from pathlib import Path

from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall,
)
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from src.config import settings


GOLDEN_DATASET_PATH = Path("evals/golden_dataset.json")
BASELINE_PATH = Path("evals/baselines/baseline_scores.json")
RESULTS_PATH = Path("evals/results/latest_scores.json")


def load_golden_dataset() -> Dataset:
    with open(GOLDEN_DATASET_PATH) as f:
        data = json.load(f)
    return Dataset.from_list(data)


def run_evaluation(dataset: Dataset) -> dict:
    llm = ChatOpenAI(
        model=settings.llm_model,
        api_key=settings.openai_api_key,
    )
    embeddings = OpenAIEmbeddings(
        model=settings.embedding_model,
        api_key=settings.openai_api_key,
    )

    result = evaluate(
        dataset=dataset,
        metrics=[faithfulness, answer_relevancy, context_precision, context_recall],
        llm=llm,
        embeddings=embeddings,
        raise_exceptions=False,
    )

    return {
        "faithfulness": round(float(result["faithfulness"]), 4),
        "answer_relevancy": round(float(result["answer_relevancy"]), 4),
        "context_precision": round(float(result["context_precision"]), 4),
        "context_recall": round(float(result["context_recall"]), 4),
    }


def check_thresholds(scores: dict) -> list[str]:
    failures = []
    thresholds = {
        "faithfulness": settings.eval_faithfulness_min,
        "answer_relevancy": settings.eval_answer_relevancy_min,
        "context_precision": settings.eval_context_precision_min,
        "context_recall": settings.eval_context_recall_min,
    }
    for metric, threshold in thresholds.items():
        actual = scores.get(metric, 0.0)
        if actual < threshold:
            failures.append(f"❌ {metric}: {actual:.4f} < threshold {threshold:.4f}")
        else:
            print(f"✅ {metric}: {actual:.4f} (threshold: {threshold:.4f})")
    return failures


def check_regression(current: dict, baseline: dict) -> list[str]:
    """Fail if any metric drops more than 5% relative to baseline."""
    regressions = []
    TOLERANCE = 0.05
    for metric, current_score in current.items():
        baseline_score = baseline.get(metric, 0.0)
        if baseline_score > 0:
            relative_drop = (baseline_score - current_score) / baseline_score
            if relative_drop > TOLERANCE:
                regressions.append(
                    f"🔻 REGRESSION {metric}: {current_score:.4f} vs baseline "
                    f"{baseline_score:.4f} ({relative_drop * 100:.1f}% drop)"
                )
    return regressions


def main():
    print("🔍 Loading golden dataset...")
    dataset = load_golden_dataset()

    print("🧪 Running RAGAS evaluation...")
    scores = run_evaluation(dataset)

    print("\n📊 Results:")
    for k, v in scores.items():
        print(f"   {k}: {v}")

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(RESULTS_PATH, "w") as f:
        json.dump(scores, f, indent=2)

    failures = check_thresholds(scores)

    if BASELINE_PATH.exists():
        with open(BASELINE_PATH) as f:
            baseline = json.load(f)
        failures.extend(check_regression(scores, baseline))

    if failures:
        print("\n🚨 EVAL GATE FAILED:")
        for msg in failures:
            print(f"   {msg}")
        sys.exit(1)

    print("\n✅ All eval gates passed. Safe to merge.")
    sys.exit(0)


if __name__ == "__main__":
    main()
evals/golden_dataset.json (structure — populate with ≥ 50 entries)
[
  {
    "question": "What is the refund policy for enterprise customers?",
    "answer": "Enterprise customers receive a 30-day full refund guarantee with no questions asked.",
    "contexts": [
      "Enterprise customers are entitled to a full refund within 30 days of purchase. No documentation is required for refund requests under $10,000.",
      "Refund processing takes 5-7 business days after approval."
    ],
    "ground_truth": "Enterprise customers get a 30-day full refund guarantee with processing in 5-7 business days."
  }
]
evals/baselines/baseline_scores.json (commit after first clean run)
{
  "faithfulness": 0.85,
  "answer_relevancy": 0.82,
  "context_precision": 0.78,
  "context_recall": 0.76
}
Phase 6 — Prometheus Alert Rules
monitoring/prometheus/prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

rule_files:
  - alert_rules.yml

scrape_configs:
  - job_name: rag-api
    static_configs:
      - targets: ["api:8000"]
    metrics_path: /metrics
monitoring/prometheus/alert_rules.yml
groups:
  - name: rag_latency
    rules:
      - alert: HighP95Latency
        expr: histogram_quantile(0.95, rate(rag_request_latency_seconds_bucket[5m])) > 10
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "RAG p95 latency > 10s"
          description: "p95 latency is {{ $value | humanizeDuration }} over last 5 minutes."

      - alert: CriticalP99Latency
        expr: histogram_quantile(0.99, rate(rag_request_latency_seconds_bucket[5m])) > 20
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "RAG p99 latency > 20s — SLA breach imminent"

  - name: rag_cost
    rules:
      - alert: CostAnomalySpike
        expr: rate(rag_cumulative_cost_usd_total[10m]) * 3600 > 10
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "RAG cost burn rate > $10/hour"
          description: "Burn rate: ${{ $value | humanize }}/hour"

      - alert: DailyBudgetBreach
        expr: increase(rag_cumulative_cost_usd_total[24h]) > 50
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "RAG daily spend exceeded $50"

  - name: rag_quality
    rules:
      - alert: FaithfulnessDrop
        expr: rag_eval_faithfulness < 0.75
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "RAG faithfulness score below 0.75 — hallucination risk elevated"

      - alert: HighErrorRate
        expr: >
          rate(rag_requests_total{status="error"}[5m])
          / rate(rag_requests_total[5m]) > 0.05
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "RAG error rate > 5%"
Phase 7 — CI Regression Gating
.github/workflows/ci.yml
name: CI — Quality Gate

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python 3.12
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: pip

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Lint (ruff)
        run: ruff check src/ evals/

      - name: Type check (pyright)
        run: pyright src/

      - name: Unit tests
        run: pytest tests/unit/ -v --tb=short

  eval-gate:
    runs-on: ubuntu-latest
    needs: lint-and-test
    if: github.event_name == 'pull_request'

    services:
      weaviate:
        image: semitechnologies/weaviate:1.25.0
        ports: ["8080:8080"]
        env:
          AUTHENTICATION_ANONYMOUS_ACCESS_ENABLED: "true"
          DEFAULT_VECTORIZER_MODULE: none

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python 3.12
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: pip

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run RAGAS Evaluation Gate
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          LANGFUSE_SECRET_KEY: ${{ secrets.LANGFUSE_SECRET_KEY }}
          LANGFUSE_PUBLIC_KEY: ${{ secrets.LANGFUSE_PUBLIC_KEY }}
          LANGFUSE_HOST: ${{ secrets.LANGFUSE_HOST }}
          LLM_MODEL: gpt-4o
          EMBEDDING_MODEL: text-embedding-3-large
          EVAL_FAITHFULNESS_MIN: "0.80"
          EVAL_ANSWER_RELEVANCY_MIN: "0.75"
          EVAL_CONTEXT_PRECISION_MIN: "0.70"
          EVAL_CONTEXT_RECALL_MIN: "0.70"
        run: python evals/run_evals.py

      - name: Post eval results as PR comment
        if: always()
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const scores = JSON.parse(fs.readFileSync('evals/results/latest_scores.json'));
            const pass = (v, t) => v >= t ? '✅' : '❌';
            const body = `## 📊 RAG Eval Gate Results

            | Metric | Score | Threshold | Status |
            |--------|-------|-----------|--------|
            | Faithfulness | ${scores.faithfulness} | 0.80 | ${pass(scores.faithfulness, 0.80)} |
            | Answer Relevancy | ${scores.answer_relevancy} | 0.75 | ${pass(scores.answer_relevancy, 0.75)} |
            | Context Precision | ${scores.context_precision} | 0.70 | ${pass(scores.context_precision, 0.70)} |
            | Context Recall | ${scores.context_recall} | 0.70 | ${pass(scores.context_recall, 0.70)} |

            > Model: \`gpt-4o\` | Commit: \`${{ github.sha }}\`
            `;
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body
            });

      - name: Upload eval results artifact
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: eval-results-${{ github.sha }}
          path: evals/results/

  load-test-smoke:
    runs-on: ubuntu-latest
    needs: eval-gate
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python 3.12
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: pip

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run Locust headless smoke (60s)
        run: |
          locust -f load_tests/locustfile.py \
            --headless -u 10 -r 2 -t 60s \
            --host http://localhost:8000 \
            --csv=load_tests/results \
            --exit-code-on-error 1

      - name: Enforce p95 latency threshold
        run: python load_tests/check_latency_thresholds.py
Phase 8 — Load Testing
load_tests/locustfile.py
import random
from locust import HttpUser, task, between

SAMPLE_QUERIES = [
    "What is the refund policy for enterprise customers?",
    "How do I reset my password?",
    "What are the SLA guarantees for the Pro plan?",
    "How does the billing cycle work?",
    "What integrations are supported?",
    "Can I export my data at any time?",
    "What happens if I exceed my monthly quota?",
    "Is there a free trial available?",
]


class RAGUser(HttpUser):
    wait_time = between(1, 3)

    @task(8)
    def query(self):
        payload = {
            "query": random.choice(SAMPLE_QUERIES),
            "session_id": f"load-test-{random.randint(1, 100)}",
            "user_id": f"user-{random.randint(1, 20)}",
        }
        with self.client.post(
            "/api/v1/query",
            json=payload,
            catch_response=True,
            name="/query",
        ) as response:
            if response.status_code == 200:
                data = response.json()
                latency = data.get("latency_ms", 0)
                if latency > 15000:
                    response.failure(f"Latency too high: {latency}ms")
                else:
                    response.success()
            else:
                response.failure(f"HTTP {response.status_code}")

    @task(2)
    def health_check(self):
        self.client.get("/health", name="/health")
load_tests/check_latency_thresholds.py
"""
Parses Locust CSV output and fails CI if p95 latency exceeds threshold.
Run after: locust --csv=load_tests/results
"""
import csv
import sys
from pathlib import Path

P95_THRESHOLD_MS = 8000   # 8 seconds
ERROR_RATE_MAX = 0.02     # 2%

stats_file = Path("load_tests/results_stats.csv")

if not stats_file.exists():
    print("❌ Locust stats CSV not found.")
    sys.exit(1)

failures = []

with open(stats_file) as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["Name"] == "Aggregated":
            p95 = float(row.get("95%", 0))
            total = float(row.get("Request Count", 1))
            errors = float(row.get("Failure Count", 0))
            error_rate = errors / max(total, 1)

            if p95 > P95_THRESHOLD_MS:
                failures.append(f"❌ p95 latency {p95}ms > threshold {P95_THRESHOLD_MS}ms")
            else:
                print(f"✅ p95 latency: {p95}ms (threshold: {P95_THRESHOLD_MS}ms)")

            if error_rate > ERROR_RATE_MAX:
                failures.append(f"❌ Error rate {error_rate*100:.1f}% > max {ERROR_RATE_MAX*100:.1f}%")
            else:
                print(f"✅ Error rate: {error_rate*100:.2f}% (max: {ERROR_RATE_MAX*100:.1f}%)")

if failures:
    for msg in failures:
        print(msg)
    sys.exit(1)

print("✅ Load test thresholds passed.")
sys.exit(0)
Phase 9 — Grafana Dashboard Specs
Build these three dashboards. Export as JSON and commit to monitoring/grafana/dashboards/.

Dashboard 1: rag_overview.json
Row 1 — SLOs: Request rate (RPS), Error rate (%), P95 Latency stat panel with threshold coloring

Row 2 — Quality: Faithfulness, Answer Relevancy, Context Precision, Context Recall gauges (red < 0.7, yellow < 0.8, green ≥ 0.8)

Row 3 — Cost: Cost/hour time series, cumulative cost today, cost by model breakdown (gpt-4o vs gpt-4o-mini if applicable)

Dashboard 2: latency_deep_dive.json
Heatmap of request latency distribution over time

P50 / P95 / P99 per pipeline stage as multi-line panel (guardrails, retrieval, reranking, generation)

Top-10 slowest requests table with Jaeger trace links

Dashboard 3: cost_accounting.json
Cost per request histogram

Token split: input vs output vs cached (stacked bar over time)

Daily/weekly cost trend with projected monthly spend

Prompt cache efficiency: cached / input ratio (target > 30% on repeated patterns)

monitoring/grafana/provisioning/datasources/datasources.yml
apiVersion: 1

datasources:
  - name: Prometheus
    type: prometheus
    url: http://prometheus:9090
    isDefault: true
    access: proxy

  - name: Jaeger
    type: jaeger
    url: http://jaeger:16686
    access: proxy
Key PromQL queries:

# P95 end-to-end
histogram_quantile(0.95, sum(rate(rag_request_latency_seconds_bucket[5m])) by (le))

# P95 per pipeline stage
histogram_quantile(0.95, sum(rate(rag_stage_latency_seconds_bucket[5m])) by (le, stage))

# Error rate %
100 * sum(rate(rag_requests_total{status="error"}[5m])) / sum(rate(rag_requests_total[5m]))

# Cost per hour (USD)
rate(rag_cumulative_cost_usd_total[1h]) * 3600

# Average cost per request
rate(rag_cumulative_cost_usd_total[5m]) / rate(rag_requests_total[5m])

# Prompt cache efficiency
rate(rag_tokens_total{token_type="cached"}[5m]) / rate(rag_tokens_total{token_type="input"}[5m])

# Average output tokens per request
rate(rag_tokens_total{token_type="output"}[5m]) / rate(rag_requests_total[5m])

# Throughput RPS
sum(rate(rag_requests_total[1m]))
Phase 10 — Production Hardening Checklist
Observability
Every LangGraph node has an OTEL span with stage, latency, and status attributes

Every GPT-4o call is logged in Langfuse with tokens, cost, input, output, cached_tokens

p50/p95/p99 latency visible per stage in Grafana

Cost-per-request trackable by user_id and session_id

Prompt cache ratio tracked in Grafana (target > 30% on repeated query patterns)

All Prometheus alert rules fire correctly (test by intentionally triggering them)

Eval Gate
Golden dataset has ≥ 50 diverse Q&A pairs covering edge cases and failure modes

Baseline scores committed to evals/baselines/baseline_scores.json

CI blocks merge on any threshold breach or > 5% relative regression

PR comment posts formatted eval table with pass/fail status on every PR

Eval results uploaded as CI artifact for audit trail

Reliability
/ready returns degraded when Weaviate is unreachable

OpenAI client uses built-in retry: AsyncOpenAI(max_retries=3)

Cost circuit breaker: return 429 if hourly burn rate exceeds COST_ALERT_THRESHOLD_USD

Graceful shutdown: drain in-flight requests before stopping

Load Testing
p95 latency under 10 concurrent users < 8s

Zero 5xx errors under normal load

p95 threshold enforced in CI via check_latency_thresholds.py

Load test baseline committed for weekly regression comparison

Commit Sequence
feat: add docker-compose observability stack (Jaeger, Langfuse, Prometheus, Grafana)
feat: implement prometheus metrics registry with cost tracking
feat: add pydantic settings with OpenAI config
feat: instrument LangGraph nodes with OTEL + Langfuse dual tracing
feat: add OpenAI token cost accounting with prompt cache awareness
feat: build guardrails node with input safety checks
feat: build retrieval node with Weaviate hybrid search
feat: build reranking node with cross-encoder
feat: build GPT-4o generation node with full observability
feat: wire LangGraph pipeline graph
feat: implement RAGAS evaluation suite with golden dataset
feat: add CI regression gating with status-table PR comment reporter
feat: add Locust load test harness + p95 threshold enforcement script
feat: provision Grafana datasources and three dashboards
feat: add Prometheus alerting rules (latency, cost, quality, budget)
chore: add pyproject.toml, ruff config, pyright config
docs: update README with architecture diagram and setup instructions
README Sections to Write
Architecture diagram — Mermaid: User → FastAPI → LangGraph (guardrails → retrieval → reranking → generation) → Weaviate / GPT-4o → Langfuse → Prometheus → Grafana

Quick start — cp .env.example .env && docker compose up -d && uvicorn src.api.main:app --reload

Running evals locally — python evals/run_evals.py

Updating the baseline — When and how to commit new baseline scores

Interpreting dashboards — What each panel means, when to be alarmed

CI/CD flow — What runs on every PR, what blocks merge

Cost model — How to read cost panels, prompt caching savings, setting budget alerts

Adding new metrics — Where to add in metrics.py, how to wire to Grafana

Portfolio Framing
One-liner for resume/LinkedIn:

Built end-to-end observability for a production RAG system: distributed tracing (OTEL + Jaeger), LLM-native traces (Langfuse), p50/p95 latency dashboards (Prometheus + Grafana), per-request cost accounting with prompt cache tracking, and automated quality regression gating in CI (RAGAS + GitHub Actions) — powered by GPT-4o.

Proof points to quantify after building:

Eval gate catches X% of prompt/retrieval regressions before production

p95 retrieval: Xms | reranking: Xms | generation: Xs | end-to-end: Xs

Average cost per query: $X | prompt cache hit rate: X%

Load test: sustained X RPS, p95 < 8s, error rate < 0.5%

CI eval run time: ~X min per PR



