from typing import Optional

from pydantic import BaseModel


class QueryRequest(BaseModel):
    query: str
    session_id: Optional[str] = None
    user_id: Optional[str] = None


class QueryResponse(BaseModel):
    answer: str
    trace_id: str
    session_id: str
    latency_ms: float
    cost_usd: float
    stage_latencies: dict
    sources: list[str]
