import json
from pathlib import Path


def write_json_report(scores: dict, path: str = "evals/results/latest_scores.json") -> None:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w") as f:
        json.dump(scores, f, indent=2)
