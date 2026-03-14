import pytest

from src.utils.metrics import classification_metrics, regression_metrics


def test_classification_metrics_returns_expected_keys():
    metrics = classification_metrics([0, 1, 0, 1], [0, 1, 0, 0], [0.1, 0.8, 0.3, 0.4])
    assert "accuracy" in metrics
    assert "roc_auc" in metrics
    assert "log_loss" in metrics


def test_regression_metrics_matches_simple_case():
    metrics = regression_metrics([1.0, 2.0, 3.0], [1.0, 2.0, 4.0])
    assert metrics["mae"] == pytest.approx(1 / 3)
    assert metrics["rmse"] > 0
