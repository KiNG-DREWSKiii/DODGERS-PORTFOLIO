import pandas as pd

from src.utils.preprocessing import add_count_features, drop_missing_rows, zscore_columns


def test_drop_missing_rows_filters_required_columns():
    df = pd.DataFrame({"a": [1.0, None, 3.0], "b": [2.0, 2.0, None]})
    result = drop_missing_rows(df, ["a", "b"])
    assert len(result) == 1


def test_add_count_features_creates_expected_flags():
    df = pd.DataFrame({"balls": [0, 3], "strikes": [2, 1]})
    result = add_count_features(df)
    assert list(result["count"]) == ["0-2", "3-1"]
    assert list(result["two_strike"]) == [1, 0]
    assert list(result["hitter_ahead"]) == [0, 1]


def test_zscore_columns_handles_constant_values():
    df = pd.DataFrame({"velo": [90.0, 90.0, 90.0]})
    result = zscore_columns(df, ["velo"])
    assert result["velo_z"].tolist() == [0.0, 0.0, 0.0]
