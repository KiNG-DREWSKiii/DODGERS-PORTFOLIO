"""Public-data pull helpers for run value modeling."""

from __future__ import annotations

import pandas as pd

from src.project1_pitch_shape.data_pull import fetch_statcast_pitch_data


def fetch_run_value_data(start_date: str, end_date: str) -> pd.DataFrame:
    """Reuse a Statcast pull for run value research."""
    return fetch_statcast_pitch_data(start_date, end_date, cache=True)
