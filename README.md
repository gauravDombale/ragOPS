# rag-observability

Production-grade RAG monitoring and observability system using FastAPI, LangGraph, OpenAI, Prometheus, Grafana, Jaeger, and Langfuse.

## Quick start

```bash
cp .env.example .env
docker compose up -d
uvicorn src.api.main:app --reload
```

## Run evals

```bash
python evals/run_evals.py
```

## Architecture

User -> FastAPI -> LangGraph (guardrails -> retrieval -> reranking -> generation) -> Weaviate/OpenAI -> Langfuse + OTEL -> Prometheus -> Grafana
