import json
from pathlib import Path

from datasets import Dataset


def load_dataset(path: str = "evals/golden_dataset.json") -> Dataset:
    with Path(path).open() as f:
        data = json.load(f)
    return Dataset.from_list(data)
