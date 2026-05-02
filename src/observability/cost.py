from dataclasses import dataclass

from src.observability.metrics import COST_PER_REQUEST, CUMULATIVE_COST, TOKENS_USED

PRICING_TABLE = {
    "gpt-4o": {"input": 2.50, "output": 10.00, "cached": 1.25},
    "gpt-4o-mini": {"input": 0.15, "output": 0.60, "cached": 0.075},
    "gpt-4-turbo": {"input": 10.00, "output": 30.00, "cached": 5.00},
    "text-embedding-3-large": {"input": 0.13, "output": 0.0, "cached": 0.0},
    "text-embedding-3-small": {"input": 0.02, "output": 0.0, "cached": 0.0},
}


@dataclass
class TokenUsage:
    model: str
    input_tokens: int = 0
    output_tokens: int = 0
    cached_tokens: int = 0

    def compute_cost(self) -> float:
        pricing = PRICING_TABLE.get(self.model, {})
        non_cached_input = max(0, self.input_tokens - self.cached_tokens)
        return (
            (non_cached_input / 1_000_000) * pricing.get("input", 0)
            + (self.cached_tokens / 1_000_000) * pricing.get("cached", 0)
            + (self.output_tokens / 1_000_000) * pricing.get("output", 0)
        )

    def record(self) -> float:
        cost = self.compute_cost()
        TOKENS_USED.labels(model=self.model, token_type="input").inc(self.input_tokens)
        TOKENS_USED.labels(model=self.model, token_type="output").inc(self.output_tokens)
        TOKENS_USED.labels(model=self.model, token_type="cached").inc(self.cached_tokens)
        CUMULATIVE_COST.labels(model=self.model).inc(cost)
        COST_PER_REQUEST.labels(model=self.model).observe(cost)
        return cost
