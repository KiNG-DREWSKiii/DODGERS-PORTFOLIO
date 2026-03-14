"""Public-data pull helpers for pitch shape clustering."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.utils.io import write_table
from src.utils.paths import RAW_DATA_DIR


def fetch_statcast_pitch_data(start_date: str, end_date: str, cache: bool = True) -> pd.DataFrame:
    """Fetch Statcast pitch-level data for a date range.

    This function uses `pybaseball.statcast` when available. It keeps the
    interface simple so the same pull logic can support all three projects.
    """
    try:
        from pybaseball import statcast
    except ImportError as exc:
        raise ImportError("pybaseball is required for live Statcast pulls.") from exc

    df = statcast(start_dt=start_date, end_dt=end_date)
    if cache:
        output = RAW_DATA_DIR / f"statcast_pitch_shape_{start_date}_{end_date}.csv"
        write_table(df, output)
    return df


def load_cached_pitch_data(start_date: str, end_date: str) -> pd.DataFrame:
    """Load a cached pitch extract if it exists."""
    path = RAW_DATA_DIR / f"statcast_pitch_shape_{start_date}_{end_date}.csv"
    if not Path(path).exists():
        raise FileNotFoundError(f"Cached data not found: {path}")
    return pd.read_csv(path)
