import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from prometheus_fastapi_instrumentator import Instrumentator

import src.observability.tracing as t
from src.api.routes import health, query
from src.config import settings
from src.observability.middleware import RequestMetricsMiddleware
from src.observability.tracing import init_tracing

logging.basicConfig(level=settings.log_level)


@asynccontextmanager
async def lifespan(app: FastAPI):
    t.tracer = init_tracing()
    yield


app = FastAPI(title="RAG Observability System", version="1.0.0", lifespan=lifespan)
app.add_middleware(RequestMetricsMiddleware)
FastAPIInstrumentor.instrument_app(app)

Instrumentator(
    should_group_status_codes=False,
    should_ignore_untemplated=True,
    should_instrument_requests_inprogress=True,
    inprogress_labels=True,
).instrument(app).expose(app, endpoint="/metrics")

app.include_router(query.router, prefix="/api/v1")
app.include_router(health.router)
