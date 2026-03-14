"""Public-data pull helpers for swing decision modeling."""

from __future__ import annotations

import pandas as pd

from src.project1_pitch_shape.data_pull import fetch_statcast_pitch_data


def fetch_swing_decision_data(start_date: str, end_date: str) -> pd.DataFrame:
    """Reuse a Statcast pull for swing decision modeling."""
    return fetch_statcast_pitch_data(start_date, end_date, cache=True)
