import weaviate
from fastapi import APIRouter

from src.config import settings

router = APIRouter()


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.get("/ready")
async def ready():
    checks = {}
    try:
        client = weaviate.connect_to_local(host=settings.weaviate_host, port=settings.weaviate_port)
        client.is_ready()
        client.close()
        checks["weaviate"] = "ok"
    except Exception as exc:
        checks["weaviate"] = f"error: {exc}"

    all_ok = all(v == "ok" for v in checks.values())
    return {"status": "ready" if all_ok else "degraded", "checks": checks}
