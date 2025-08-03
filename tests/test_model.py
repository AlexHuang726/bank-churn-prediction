import math
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.model import load_data, train_models


def test_load_data():
    data = load_data()
    expected_columns = [
        "RowNumber",
        "CustomerId",
        "Surname",
        "CreditScore",
        "Geography",
        "Gender",
        "Age",
        "Tenure",
        "Balance",
        "NumOfProducts",
        "HasCrCard",
        "IsActiveMember",
        "EstimatedSalary",
        "Exited",
    ]
    assert list(data[0].keys()) == expected_columns
    assert len(data) == 10


def test_train_models():
    data = load_data()
    preds = train_models(data)
    expected_rows = math.ceil(len(data) * 0.2)
    assert set(preds.keys()) == {"logistic", "random_forest"}
    for p in preds.values():
        assert len(p) == expected_rows
