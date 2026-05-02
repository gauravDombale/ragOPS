import time
import uuid

from fastapi import APIRouter, HTTPException

from src.api.schemas import QueryRequest, QueryResponse
from src.config import settings
from src.observability.langfuse_compat import langfuse_context, observe
from src.observability.metrics import ACTIVE_REQUESTS, REQUEST_LATENCY, REQUEST_TOTAL
from src.pipeline.graph import rag_pipeline

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
            "faithfulness": None,
            "answer_relevancy": None,
        }

        final_state = await rag_pipeline.ainvoke(initial_state)
        if final_state["total_cost_usd"] > settings.cost_alert_threshold_usd:
            raise HTTPException(status_code=429, detail="Cost circuit breaker triggered.")

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
