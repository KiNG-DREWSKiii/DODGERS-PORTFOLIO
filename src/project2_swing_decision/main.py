"""Command-line entry point for swing decision modeling."""

from __future__ import annotations

import argparse
import json

from src.project2_swing_decision.data_pull import fetch_swing_decision_data
from src.project2_swing_decision.evaluate import plot_roc_curve, summarize_swing_model
from src.project2_swing_decision.features import build_swing_decision_table
from src.project2_swing_decision.model import fit_swing_model
from src.utils.io import write_table
from src.utils.paths import FIGURES_DIR, PROCESSED_DATA_DIR, ensure_repo_dirs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run swing decision classification workflow.")
    parser.add_argument("--start-date", required=True, help="Start date in YYYY-MM-DD format.")
    parser.add_argument("--end-date", required=True, help="End date in YYYY-MM-DD format.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ensure_repo_dirs()

    raw = fetch_swing_decision_data(args.start_date, args.end_date)
    model_df = build_swing_decision_table(raw)
    artifacts = fit_swing_model(model_df)
    metrics = summarize_swing_model(artifacts.y_test, artifacts.y_pred, artifacts.y_prob)

    write_table(
        model_df,
        PROCESSED_DATA_DIR / f"swing_decision_features_{args.start_date}_{args.end_date}.csv",
    )
    with open(
        PROCESSED_DATA_DIR / f"swing_decision_metrics_{args.start_date}_{args.end_date}.json",
        "w",
        encoding="utf-8",
    ) as handle:
        json.dump(metrics, handle, indent=2)
    plot_roc_curve(
        artifacts.model,
        artifacts.X_test,
        artifacts.y_test,
        FIGURES_DIR / f"swing_decision_roc_{args.start_date}_{args.end_date}.png",
    )


if __name__ == "__main__":
    main()
