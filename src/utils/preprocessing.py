"""Shared preprocessing helpers."""

from __future__ import annotations

from typing import Iterable

import numpy as np
import pandas as pd


def drop_missing_rows(df: pd.DataFrame, columns: Iterable[str]) -> pd.DataFrame:
    """Drop rows missing values in required columns."""
    return df.dropna(subset=list(columns)).reset_index(drop=True)


def clip_series(series: pd.Series, lower: float, upper: float) -> pd.Series:
    """Clip a numeric series to a fixed range."""
    return series.clip(lower=lower, upper=upper)


def add_count_features(df: pd.DataFrame, balls_col: str = "balls", strikes_col: str = "strikes") -> pd.DataFrame:
    """Add simple derived count-state features."""
    result = df.copy()
    result["count"] = result[balls_col].astype(str) + "-" + result[strikes_col].astype(str)
    result["two_strike"] = (result[strikes_col] >= 2).astype(int)
    result["hitter_ahead"] = (result[balls_col] > result[strikes_col]).astype(int)
    return result


def zscore_columns(df: pd.DataFrame, columns: Iterable[str]) -> pd.DataFrame:
    """Z-score selected numeric columns."""
    result = df.copy()
    for column in columns:
        values = result[column].astype(float)
        std = values.std(ddof=0)
        if np.isclose(std, 0.0):
            result[f"{column}_z"] = 0.0
        else:
            result[f"{column}_z"] = (values - values.mean()) / std
    return result
