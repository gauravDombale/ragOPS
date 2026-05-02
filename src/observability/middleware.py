import time

from starlette.middleware.base import BaseHTTPMiddleware

from src.observability.metrics import REQUEST_LATENCY, REQUEST_TOTAL


class RequestMetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.perf_counter()
        status = "success"
        try:
            response = await call_next(request)
            if response.status_code >= 400:
                status = "error"
            return response
        except Exception:
            status = "error"
            raise
        finally:
            latency = time.perf_counter() - start
            REQUEST_LATENCY.labels(endpoint=request.url.path, status=status).observe(latency)
            REQUEST_TOTAL.labels(endpoint=request.url.path, status=status).inc()
