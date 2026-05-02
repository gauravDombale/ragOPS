from __future__ import annotations

from typing import Any, Callable

try:
    from langfuse.decorators import langfuse_context, observe  # type: ignore
except Exception:
    try:
        from langfuse import get_client, observe  # type: ignore
    except Exception:
        get_client = None  # type: ignore

        def observe(name: str | None = None) -> Callable:
            def _decorator(func: Callable) -> Callable:
                return func

            return _decorator

    class _CompatLangfuseContext:
        """Best-effort wrapper across Langfuse SDK versions."""

        def update_current_trace(self, **kwargs: Any) -> None:
            if get_client is None:
                return None
            try:
                client = get_client()
                # v3 client helper to attach I/O to current trace
                if hasattr(client, "set_current_trace_io"):
                    trace_input = kwargs.get("input")
                    trace_output = kwargs.get("output")
                    if trace_input is not None or trace_output is not None:
                        client.set_current_trace_io(input=trace_input, output=trace_output)
            except Exception:
                return None

        def update_current_observation(self, **kwargs: Any) -> None:
            if get_client is None:
                return None
            try:
                client = get_client()
                if hasattr(client, "update_current_generation"):
                    client.update_current_generation(**kwargs)
                    return None
                if hasattr(client, "update_current_span"):
                    client.update_current_span(**kwargs)
            except Exception:
                return None

    langfuse_context = _CompatLangfuseContext()
