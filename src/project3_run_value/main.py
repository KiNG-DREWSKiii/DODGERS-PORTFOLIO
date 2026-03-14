"""Command-line entry point for run value modeling."""

from __future__ import annotations

import argparse
import json

from src.project3_run_value.data_pull import fetch_run_value_data
from src.project3_run_value.features import build_run_value_table
from src.project3_run_value.model import fit_run_value_model
from src.project3_run_value.visuals import plot_run_value_by_count
from src.utils.io import write_table
from src.utils.metrics import regression_metrics
from src.utils.paths import FIGURES_DIR, PROCESSED_DATA_DIR, ensure_repo_dirs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run run-value decision workflow.")
    parser.add_argument("--start-date", required=True, help="Start date in YYYY-MM-DD format.")
    parser.add_argument("--end-date", required=True, help="End date in YYYY-MM-DD format.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ensure_repo_dirs()

    raw = fetch_run_value_data(args.start_date, args.end_date)
    model_df = build_run_value_table(raw)
    artifacts = fit_run_value_model(model_df)
    metrics = regression_metrics(artifacts.y_test, artifacts.y_pred)

    write_table(
        model_df,
        PROCESSED_DATA_DIR / f"run_value_features_{args.start_date}_{args.end_date}.csv",
    )
    with open(
        PROCESSED_DATA_DIR / f"run_value_metrics_{args.start_date}_{args.end_date}.json",
        "w",
        encoding="utf-8",
    ) as handle:
        json.dump(metrics, handle, indent=2)
    plot_run_value_by_count(
        model_df,
        FIGURES_DIR / f"run_value_by_count_{args.start_date}_{args.end_date}.png",
    )


if __name__ == "__main__":
    main()
