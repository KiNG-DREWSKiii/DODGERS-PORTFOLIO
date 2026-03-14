"""Feature engineering for pitch shape clustering."""

from __future__ import annotations

import pandas as pd

from src.utils.io import require_columns
from src.utils.preprocessing import drop_missing_rows, zscore_columns


PITCH_SHAPE_COLUMNS = [
    "pitch_type",
    "release_speed",
    "pfx_x",
    "pfx_z",
    "plate_x",
    "plate_z",
]


def build_pitch_shape_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create a pitch-shape modeling table from raw pitch data."""
    require_columns(df, PITCH_SHAPE_COLUMNS)

    features = drop_missing_rows(df, PITCH_SHAPE_COLUMNS).copy()
    features["horizontal_break_inches"] = features["pfx_x"] * 12.0
    features["induced_vertical_break_inches"] = features["pfx_z"] * 12.0
    features["velo"] = features["release_speed"]

    features = zscore_columns(
        features,
        ["horizontal_break_inches", "induced_vertical_break_inches", "velo"],
    )
    return features
