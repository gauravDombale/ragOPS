from prometheus_client import Counter, Gauge, Histogram

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
    ["stage"],
    buckets=LATENCY_BUCKETS,
)

COST_PER_REQUEST = Histogram(
    "rag_cost_usd_per_request",
    "Estimated USD cost per RAG request",
    ["model"],
    buckets=(0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5),
)

TOKENS_USED = Counter("rag_tokens_total", "Total tokens consumed", ["model", "token_type"])
CUMULATIVE_COST = Counter("rag_cumulative_cost_usd_total", "Running total USD cost", ["model"])

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

EVAL_FAITHFULNESS = Gauge("rag_eval_faithfulness", "RAGAS faithfulness score")
EVAL_ANSWER_RELEVANCY = Gauge("rag_eval_answer_relevancy", "RAGAS answer relevancy")
EVAL_CONTEXT_PRECISION = Gauge("rag_eval_context_precision", "RAGAS context precision")
EVAL_CONTEXT_RECALL = Gauge("rag_eval_context_recall", "RAGAS context recall")

ACTIVE_REQUESTS = Gauge("rag_active_requests", "Number of requests currently being processed")
REQUEST_TOTAL = Counter("rag_requests_total", "Total RAG requests", ["endpoint", "status"])
CACHE_HIT = Counter("rag_cache_hits_total", "Semantic cache hits", ["cache_type"])
