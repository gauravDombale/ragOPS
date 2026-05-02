import json
import sys
from pathlib import Path

from datasets import Dataset
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from ragas import evaluate
from ragas.metrics import answer_relevancy, context_precision, context_recall, faithfulness

from src.config import settings
from src.observability.metrics import (
    EVAL_ANSWER_RELEVANCY,
    EVAL_CONTEXT_PRECISION,
    EVAL_CONTEXT_RECALL,
    EVAL_FAITHFULNESS,
)

GOLDEN_DATASET_PATH = Path("evals/golden_dataset.json")
BASELINE_PATH = Path("evals/baselines/baseline_scores.json")
RESULTS_PATH = Path("evals/results/latest_scores.json")


def load_golden_dataset() -> Dataset:
    with GOLDEN_DATASET_PATH.open() as f:
        data = json.load(f)
    return Dataset.from_list(data)


def run_evaluation(dataset: Dataset) -> dict:
    llm = ChatOpenAI(model=settings.llm_model, api_key=settings.openai_api_key)
    embeddings = OpenAIEmbeddings(model=settings.embedding_model, api_key=settings.openai_api_key)

    result = evaluate(
        dataset=dataset,
        metrics=[faithfulness, answer_relevancy, context_precision, context_recall],
        llm=llm,
        embeddings=embeddings,
        raise_exceptions=False,
    )

    scores = {
        "faithfulness": round(float(result["faithfulness"]), 4),
        "answer_relevancy": round(float(result["answer_relevancy"]), 4),
        "context_precision": round(float(result["context_precision"]), 4),
        "context_recall": round(float(result["context_recall"]), 4),
    }

    EVAL_FAITHFULNESS.set(scores["faithfulness"])
    EVAL_ANSWER_RELEVANCY.set(scores["answer_relevancy"])
    EVAL_CONTEXT_PRECISION.set(scores["context_precision"])
    EVAL_CONTEXT_RECALL.set(scores["context_recall"])
    return scores


def check_thresholds(scores: dict) -> list[str]:
    failures = []
    thresholds = {
        "faithfulness": settings.eval_faithfulness_min,
        "answer_relevancy": settings.eval_answer_relevancy_min,
        "context_precision": settings.eval_context_precision_min,
        "context_recall": settings.eval_context_recall_min,
    }
    for metric, threshold in thresholds.items():
        actual = scores.get(metric, 0.0)
        if actual < threshold:
            failures.append(f"{metric}: {actual:.4f} < threshold {threshold:.4f}")
    return failures


def check_regression(current: dict, baseline: dict) -> list[str]:
    regressions = []
    tolerance = 0.05
    for metric, current_score in current.items():
        baseline_score = baseline.get(metric, 0.0)
        if baseline_score > 0:
            relative_drop = (baseline_score - current_score) / baseline_score
            if relative_drop > tolerance:
                regressions.append(
                    f"REGRESSION {metric}: {current_score:.4f} vs {baseline_score:.4f} ({relative_drop * 100:.1f}% drop)"
                )
    return regressions


def main():
    dataset = load_golden_dataset()
    scores = run_evaluation(dataset)

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with RESULTS_PATH.open("w") as f:
        json.dump(scores, f, indent=2)

    failures = check_thresholds(scores)

    if BASELINE_PATH.exists():
        with BASELINE_PATH.open() as f:
            baseline = json.load(f)
        failures.extend(check_regression(scores, baseline))

    if failures:
        for msg in failures:
            print(msg)
        sys.exit(1)

    print("All eval gates passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
