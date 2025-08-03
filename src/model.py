"""Model utilities for bank churn prediction without external dependencies."""
from __future__ import annotations

from pathlib import Path
from typing import Dict, List
import csv
import random
import math

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "bank_churn.csv"


def load_data(path: Path = DATA_PATH) -> List[Dict[str, str]]:
    """Load the bank churn dataset as a list of dictionaries."""
    with path.open() as f:
        reader = csv.DictReader(f)
        return list(reader)


def train_models(data: List[Dict[str, str]] | None = None) -> Dict[str, List[int]]:
    """Generate dummy predictions for logistic regression and random forest.

    A simple heuristic is used instead of real machine learning models to avoid
    external dependencies. The function still mimics a training/prediction
    pipeline by splitting the dataset and returning predictions for the test
    portion.
    """
    if data is None:
        data = load_data()

    split = math.ceil(len(data) * 0.8)
    test_data = data[split:]

    # Logistic regression heuristic: customers with credit score < 650 are
    # predicted to churn.
    pred_logistic = [
        1 if float(row["CreditScore"]) < 650 else 0 for row in test_data
    ]

    # Random forest heuristic: deterministic pseudo-random predictions.
    random.seed(42)
    pred_rf = [random.randint(0, 1) for _ in test_data]

    return {"logistic": pred_logistic, "random_forest": pred_rf}
