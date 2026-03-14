"""Visualization helpers for run value modeling."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from src.utils.plotting import apply_base_style, save_figure


def plot_run_value_by_count(df: pd.DataFrame, output_path: str | Path) -> None:
    """Plot average observed run value by count state."""
    summary = df.groupby("count", as_index=False)["run_value_target"].mean().sort_values("run_value_target")
    apply_base_style()
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(summary["count"], summary["run_value_target"], color="#1f77b4")
    ax.set_xlabel("Count")
    ax.set_ylabel("Average Run Value Target")
    ax.set_title("Average Run Value by Count")
    save_figure(output_path)
