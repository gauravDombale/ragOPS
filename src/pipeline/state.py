from dataclasses import dataclass, field
from typing import Optional, TypedDict


@dataclass
class RetrievedDoc:
    content: str
    source: str
    score: float
    metadata: dict = field(default_factory=dict)


class RAGState(TypedDict):
    query: str
    session_id: str
    trace_id: str
    user_id: Optional[str]
    retrieved_docs: list[RetrievedDoc]
    reranked_docs: list[RetrievedDoc]
    prompt: str
    response: str
    stage_latencies: dict
    token_usage: dict
    total_cost_usd: float
    retrieval_score: float
    faithfulness: Optional[float]
    answer_relevancy: Optional[float]
