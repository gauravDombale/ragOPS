# rag-observability

Production-grade RAG monitoring and observability system using FastAPI, LangGraph, OpenAI, Prometheus, Grafana, Jaeger, and Langfuse.

## Quick start

```bash
cp .env.example .env
docker compose up -d api weaviate
uvicorn src.api.main:app --reload
```

## Low-resource mode (recommended on laptop)

Uses only remote OpenAI models and no local reranker model:
- `LLM_MODEL=gpt-4o-mini`
- `EMBEDDING_MODEL=text-embedding-3-small`
- `OTEL_EXPORTER_OTLP_ENDPOINT=` (disabled)
- `LANGFUSE_HOST=` (disabled)

## Full observability stack (optional)

```bash
docker compose --profile obs up -d
```

## Run evals

```bash
python evals/run_evals.py
```

## Architecture

User -> FastAPI -> LangGraph (guardrails -> retrieval -> reranking -> generation) -> Weaviate/OpenAI -> Langfuse + OTEL -> Prometheus -> Grafana
