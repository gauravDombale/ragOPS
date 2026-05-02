from functools import wraps

from langfuse import Langfuse
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from src.config import settings
from src.observability.langfuse_compat import observe


def init_tracing() -> trace.Tracer:
    resource = Resource.create(
        {
            "service.name": settings.otel_service_name,
            "deployment.environment": settings.app_env,
            "service.version": settings.app_version,
        }
    )
    exporter = OTLPSpanExporter(endpoint=settings.otel_exporter_otlp_endpoint, insecure=True)
    provider = TracerProvider(resource=resource)
    provider.add_span_processor(BatchSpanProcessor(exporter))
    trace.set_tracer_provider(provider)
    HTTPXClientInstrumentor().instrument()
    return trace.get_tracer(settings.otel_service_name)


tracer: trace.Tracer | None = None


def get_langfuse_client() -> Langfuse:
    return Langfuse(
        secret_key=settings.langfuse_secret_key,
        public_key=settings.langfuse_public_key,
        host=settings.langfuse_host,
    )


def trace_stage(stage_name: str):
    def decorator(func):
        @wraps(func)
        @observe(name=stage_name)
        async def wrapper(*args, **kwargs):
            active_tracer = tracer or trace.get_tracer(settings.otel_service_name)
            with active_tracer.start_as_current_span(stage_name) as span:
                span.set_attribute("pipeline.stage", stage_name)
                try:
                    result = await func(*args, **kwargs)
                    span.set_attribute("pipeline.status", "success")
                    return result
                except Exception as exc:
                    span.record_exception(exc)
                    span.set_attribute("pipeline.status", "error")
                    span.set_attribute("error.type", type(exc).__name__)
                    raise

        return wrapper

    return decorator
