import time

from fastapi import HTTPException
from opentelemetry import trace

from src.observability.metrics import STAGE_LATENCY
from src.observability.langfuse_compat import observe
from src.pipeline.state import RAGState

BLOCKED_PATTERNS = ["ignore previous instructions", "jailbreak", "prompt injection"]


@observe(name="guardrails")
async def guardrails_node(state: RAGState) -> RAGState:
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

    return {**state, "stage_latencies": {**state.get("stage_latencies", {}), "guardrails": latency}}
