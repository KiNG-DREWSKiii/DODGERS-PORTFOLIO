"""Input and output helpers for tabular baseball data."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd


def read_table(path: str | Path, **kwargs) -> pd.DataFrame:
    """Read a CSV or parquet file based on suffix."""
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if file_path.suffix == ".csv":
        return pd.read_csv(file_path, **kwargs)
    if file_path.suffix == ".parquet":
        return pd.read_parquet(file_path, **kwargs)
    raise ValueError(f"Unsupported file type: {file_path.suffix}")


def write_table(df: pd.DataFrame, path: str | Path, index: bool = False, **kwargs) -> None:
    """Write a DataFrame to CSV or parquet based on suffix."""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if file_path.suffix == ".csv":
        df.to_csv(file_path, index=index, **kwargs)
        return
    if file_path.suffix == ".parquet":
        df.to_parquet(file_path, index=index, **kwargs)
        return
    raise ValueError(f"Unsupported file type: {file_path.suffix}")


def require_columns(df: pd.DataFrame, columns: Iterable[str]) -> None:
    """Raise if a DataFrame is missing required columns."""
    missing = [column for column in columns if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
