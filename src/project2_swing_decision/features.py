"""Feature engineering for swing decision modeling."""

from __future__ import annotations

import pandas as pd

from src.utils.io import require_columns
from src.utils.preprocessing import add_count_features, clip_series, drop_missing_rows


REQUIRED_COLUMNS = [
    "description",
    "plate_x",
    "plate_z",
    "release_speed",
    "pfx_x",
    "pfx_z",
    "balls",
    "strikes",
]

SWING_DESCRIPTIONS = {
    "swinging_strike",
    "swinging_strike_blocked",
    "foul",
    "foul_tip",
    "hit_into_play",
    "hit_into_play_no_out",
    "hit_into_play_score",
}


def build_swing_decision_table(df: pd.DataFrame) -> pd.DataFrame:
    """Build a modeling table for swing vs take classification."""
    require_columns(df, REQUIRED_COLUMNS)
    model_df = drop_missing_rows(df, REQUIRED_COLUMNS).copy()

    model_df["swing"] = model_df["description"].isin(SWING_DESCRIPTIONS).astype(int)
    model_df["plate_x_clipped"] = clip_series(model_df["plate_x"], -2.0, 2.0)
    model_df["plate_z_clipped"] = clip_series(model_df["plate_z"], 0.0, 5.0)
    model_df["horizontal_break_inches"] = model_df["pfx_x"] * 12.0
    model_df["induced_vertical_break_inches"] = model_df["pfx_z"] * 12.0

    model_df = add_count_features(model_df)
    return model_df
