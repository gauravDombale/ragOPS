from src.evaluation.dataset import load_dataset
from evals.run_evals import run_evaluation


def run() -> dict:
    return run_evaluation(load_dataset())
