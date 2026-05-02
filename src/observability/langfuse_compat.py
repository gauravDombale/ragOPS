from __future__ import annotations

from typing import Any, Callable

try:
    from langfuse.decorators import langfuse_context, observe  # type: ignore
except Exception:
    class _NoopLangfuseContext:
        def update_current_trace(self, **kwargs: Any) -> None:
            return None

        def update_current_observation(self, **kwargs: Any) -> None:
            return None

    def observe(name: str | None = None) -> Callable:
        def _decorator(func: Callable) -> Callable:
            return func

        return _decorator

    langfuse_context = _NoopLangfuseContext()

