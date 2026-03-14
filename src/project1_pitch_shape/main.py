"""Command-line entry point for pitch shape clustering."""

from __future__ import annotations

import argparse
from datetime import date

from src.project1_pitch_shape.clustering import run_pitch_clustering
from src.project1_pitch_shape.data_pull import fetch_statcast_pitch_data
from src.project1_pitch_shape.features import build_pitch_shape_features
from src.project1_pitch_shape.visuals import plot_pitch_cluster_pca, plot_pitch_movement_clusters
from src.utils.io import write_table
from src.utils.paths import FIGURES_DIR, PROCESSED_DATA_DIR, ensure_repo_dirs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run pitch shape clustering workflow.")
    parser.add_argument(
        "--start-date",
        default="2024-03-28",
        help="Start date in YYYY-MM-DD format. Defaults to 2024 Opening Day.",
    )
    parser.add_argument(
        "--end-date",
        default="2024-04-30",
        help="End date in YYYY-MM-DD format. Defaults to an initial one-month sample.",
    )
    parser.add_argument("--clusters", type=int, default=6, help="Number of KMeans clusters.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ensure_repo_dirs()

    if args.start_date > args.end_date:
        raise ValueError("start-date must be earlier than or equal to end-date.")
    if args.end_date > date.today().isoformat():
        raise ValueError("end-date cannot be in the future.")

    raw = fetch_statcast_pitch_data(args.start_date, args.end_date)
    features = build_pitch_shape_features(raw)
    result = run_pitch_clustering(features, n_clusters=args.clusters)

    write_table(
        result.labeled_data,
        PROCESSED_DATA_DIR / f"pitch_shape_clusters_{args.start_date}_{args.end_date}.csv",
    )
    write_table(
        result.cluster_summary,
        PROCESSED_DATA_DIR / f"pitch_shape_cluster_summary_{args.start_date}_{args.end_date}.csv",
    )
    plot_pitch_movement_clusters(
        result.labeled_data,
        FIGURES_DIR / f"pitch_shape_clusters_{args.start_date}_{args.end_date}.png",
    )
    plot_pitch_cluster_pca(
        result.labeled_data,
        FIGURES_DIR / f"pitch_shape_pca_{args.start_date}_{args.end_date}.png",
    )


if __name__ == "__main__":
    main()
