"""Feature engineering for run value estimation."""

from __future__ import annotations

import pandas as pd

from src.utils.io import require_columns
from src.utils.preprocessing import add_count_features, drop_missing_rows


REQUIRED_COLUMNS = [
    "events",
    "release_speed",
    "pfx_x",
    "pfx_z",
    "plate_x",
    "plate_z",
    "balls",
    "strikes",
]

EVENT_RUN_VALUES = {
    "single": 0.47,
    "double": 0.78,
    "triple": 1.09,
    "home_run": 1.40,
    "walk": 0.33,
    "hit_by_pitch": 0.34,
    "field_out": -0.27,
    "strikeout": -0.29,
    "grounded_into_double_play": -0.60,
}


def build_run_value_table(df: pd.DataFrame) -> pd.DataFrame:
    """Create a simple run-value modeling table from pitch-level data."""
    require_columns(df, REQUIRED_COLUMNS)
    model_df = drop_missing_rows(df, REQUIRED_COLUMNS).copy()
    model_df = add_count_features(model_df)

    model_df["horizontal_break_inches"] = model_df["pfx_x"] * 12.0
    model_df["induced_vertical_break_inches"] = model_df["pfx_z"] * 12.0
    model_df["run_value_target"] = model_df["events"].map(EVENT_RUN_VALUES).fillna(0.0)
    return model_df
