"""Clustering workflow for pitch shape analysis."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


@dataclass
class PitchClusterResult:
    labeled_data: pd.DataFrame
    cluster_summary: pd.DataFrame
    pca_frame: pd.DataFrame
    kmeans: KMeans
    pca: PCA


def run_pitch_clustering(df: pd.DataFrame, n_clusters: int = 6, random_state: int = 42) -> PitchClusterResult:
    """Fit KMeans on standardized pitch-shape features and return summaries."""
    feature_cols = [
        "horizontal_break_inches_z",
        "induced_vertical_break_inches_z",
        "velo_z",
    ]

    kmeans = KMeans(n_clusters=n_clusters, n_init=20, random_state=random_state)
    labels = kmeans.fit_predict(df[feature_cols])

    pca = PCA(n_components=2, random_state=random_state)
    components = pca.fit_transform(df[feature_cols])

    labeled = df.copy()
    labeled["cluster"] = labels
    labeled["pc1"] = components[:, 0]
    labeled["pc2"] = components[:, 1]

    summary = (
        labeled.groupby("cluster", as_index=False)
        .agg(
            pitch_count=("cluster", "size"),
            mean_velocity=("velo", "mean"),
            mean_hb=("horizontal_break_inches", "mean"),
            mean_ivb=("induced_vertical_break_inches", "mean"),
            top_pitch_type=("pitch_type", lambda s: s.mode().iloc[0] if not s.mode().empty else "unknown"),
        )
        .sort_values("pitch_count", ascending=False)
    )

    pca_frame = labeled[["pc1", "pc2", "cluster", "pitch_type"]].copy()
    return PitchClusterResult(labeled, summary, pca_frame, kmeans, pca)
