from langgraph.graph import END, StateGraph

from src.pipeline.nodes.generator import generation_node
from src.pipeline.nodes.guardrails import guardrails_node
from src.pipeline.nodes.reranker import reranking_node
from src.pipeline.nodes.retriever import retrieval_node
from src.pipeline.state import RAGState


def build_rag_graph():
    graph = StateGraph(RAGState)
    graph.add_node("guardrails", guardrails_node)
    graph.add_node("retrieval", retrieval_node)
    graph.add_node("reranking", reranking_node)
    graph.add_node("generation", generation_node)

    graph.set_entry_point("guardrails")
    graph.add_edge("guardrails", "retrieval")
    graph.add_edge("retrieval", "reranking")
    graph.add_edge("reranking", "generation")
    graph.add_edge("generation", END)

    return graph.compile()


rag_pipeline = build_rag_graph()
