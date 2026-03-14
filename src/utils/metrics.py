"""Shared model evaluation helpers."""

from __future__ import annotations

from typing import Mapping

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    log_loss,
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    roc_auc_score,
)


def classification_metrics(y_true, y_pred, y_prob=None) -> Mapping[str, float]:
    """Return a compact classification metric dictionary."""
    metrics = {
        "accuracy": float(accuracy_score(y_true, y_pred)),
    }
    if y_prob is not None:
        metrics["roc_auc"] = float(roc_auc_score(y_true, y_prob))
        metrics["log_loss"] = float(log_loss(y_true, np.clip(y_prob, 1e-6, 1 - 1e-6)))
    return metrics


def regression_metrics(y_true, y_pred) -> Mapping[str, float]:
    """Return common regression metrics."""
    rmse = float(np.sqrt(mean_squared_error(y_true, y_pred)))
    return {
        "rmse": rmse,
        "mae": float(mean_absolute_error(y_true, y_pred)),
        "r2": float(r2_score(y_true, y_pred)),
    }
