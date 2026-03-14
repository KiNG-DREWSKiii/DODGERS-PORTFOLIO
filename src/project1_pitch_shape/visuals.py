"""Visualization helpers for pitch shape clustering."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from src.utils.plotting import apply_base_style, save_figure


def plot_pitch_movement_clusters(df: pd.DataFrame, output_path: str | Path) -> None:
    """Plot horizontal and vertical movement by assigned cluster."""
    apply_base_style()
    fig, ax = plt.subplots()
    scatter = ax.scatter(
        df["horizontal_break_inches"],
        df["induced_vertical_break_inches"],
        c=df["cluster"],
        cmap="tab10",
        alpha=0.6,
        s=18,
    )
    ax.set_xlabel("Horizontal Break (inches)")
    ax.set_ylabel("Induced Vertical Break (inches)")
    ax.set_title("Pitch Shape Clusters")
    fig.colorbar(scatter, ax=ax, label="Cluster")
    save_figure(output_path)


def plot_pitch_cluster_pca(df: pd.DataFrame, output_path: str | Path) -> None:
    """Plot PCA projection of pitch-shape features."""
    apply_base_style()
    fig, ax = plt.subplots()
    scatter = ax.scatter(df["pc1"], df["pc2"], c=df["cluster"], cmap="tab10", alpha=0.6, s=18)
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.set_title("Pitch Shape PCA Projection")
    fig.colorbar(scatter, ax=ax, label="Cluster")
    save_figure(output_path)
