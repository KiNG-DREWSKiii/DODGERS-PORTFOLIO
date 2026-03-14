"""Evaluation helpers for swing decision modeling."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from sklearn.metrics import RocCurveDisplay

from src.utils.metrics import classification_metrics
from src.utils.plotting import apply_base_style, save_figure


def summarize_swing_model(y_true, y_pred, y_prob):
    """Return standard metrics for swing classification."""
    return classification_metrics(y_true=y_true, y_pred=y_pred, y_prob=y_prob)


def plot_roc_curve(model, X_test, y_test, output_path: str | Path) -> None:
    """Save a ROC curve figure for the fitted classifier."""
    apply_base_style()
    fig, ax = plt.subplots()
    RocCurveDisplay.from_estimator(model, X_test, y_test, ax=ax)
    ax.set_title("Swing Decision ROC Curve")
    save_figure(output_path)
