import time

from opentelemetry import trace
from langfuse.openai import AsyncOpenAI

from src.config import settings
from src.observability.cost import TokenUsage
from src.observability.langfuse_compat import observe
from src.observability.metrics import STAGE_LATENCY
from src.pipeline.state import RAGState

SYSTEM_PROMPT = """You are a precise, helpful assistant. Answer the question using ONLY the provided context.
If the context does not contain sufficient information, say so explicitly.
Do not fabricate information."""


@observe(name="generation")
async def generation_node(state: RAGState) -> RAGState:
    span = trace.get_current_span()
    client = AsyncOpenAI(api_key=settings.openai_api_key, max_retries=3)

    context = "\n\n---\n\n".join(
        [f"[Source: {doc.source}]\n{doc.content}" for doc in state["reranked_docs"][:5]]
    )
    user_prompt = f"""Context:
{context}

Question: {state['query']}

Answer:"""

    start = time.perf_counter()
    response = await client.chat.completions.create(
        name="rag-generation",
        model=settings.llm_model,
        max_tokens=1024,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        metadata={
            "langfuse_session_id": state["session_id"],
            "langfuse_user_id": state.get("user_id"),
            "langfuse_tags": ["ragops", "production"],
            "langfuse_metadata": {
                "trace_id": state["trace_id"],
                "context_docs": len(state["reranked_docs"]),
            },
        },
    )

    latency = time.perf_counter() - start
    answer = response.choices[0].message.content or ""

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
