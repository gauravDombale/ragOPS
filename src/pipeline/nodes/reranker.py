import time

from opentelemetry import trace

from src.observability.langfuse_compat import observe
from src.observability.metrics import STAGE_LATENCY
from src.pipeline.state import RAGState


@observe(name="reranking")
async def reranking_node(state: RAGState) -> RAGState:
    span = trace.get_current_span()
    start = time.perf_counter()

    docs = state["retrieved_docs"]
    if not docs:
        return {**state, "reranked_docs": []}

    # Fast fallback reranker: keep top-5 by retrieval score.
    # This avoids runtime model downloads and keeps local dev stable.
    reranked_docs = sorted(docs, key=lambda d: d.score, reverse=True)[:5]

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
