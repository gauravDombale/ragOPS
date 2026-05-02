import time

import weaviate
from opentelemetry import trace
from openai import AsyncOpenAI

from src.config import settings
from src.observability.langfuse_compat import observe
from src.observability.metrics import RETRIEVAL_DOCS_RETURNED, RETRIEVAL_SCORE, STAGE_LATENCY
from src.pipeline.state import RAGState, RetrievedDoc


@observe(name="retrieval")
async def retrieval_node(state: RAGState) -> RAGState:
    span = trace.get_current_span()
    span.set_attribute("retrieval.query", state["query"])

    start = time.perf_counter()
    oai = AsyncOpenAI(api_key=settings.openai_api_key, max_retries=3)
    docs: list[RetrievedDoc] = []
    client = None
    try:
        client = weaviate.connect_to_local(host=settings.weaviate_host, port=settings.weaviate_port)
        collection = client.collections.get("Documents")
        query_vector = (
            await oai.embeddings.create(
                model=settings.embedding_model,
                input=state["query"],
            )
        ).data[0].embedding
        results = collection.query.hybrid(
            query=state["query"],
            vector=query_vector,
            limit=10,
            alpha=0.5,
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
    except Exception as exc:
        span.record_exception(exc)
        span.set_attribute("retrieval.error", str(exc))
    finally:
        if client is not None:
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
