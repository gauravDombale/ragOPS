from collections.abc import Awaitable, Callable

from src.observability.tracing import trace_stage


def trace_node(name: str):
    return trace_stage(name)


def track_cost(func: Callable[..., Awaitable[dict]]):
    return func
