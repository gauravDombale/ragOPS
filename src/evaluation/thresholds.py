from src.config import settings


def get_thresholds() -> dict:
    return {
        "faithfulness": settings.eval_faithfulness_min,
        "answer_relevancy": settings.eval_answer_relevancy_min,
        "context_precision": settings.eval_context_precision_min,
        "context_recall": settings.eval_context_recall_min,
    }
