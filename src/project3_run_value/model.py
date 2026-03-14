"""Baseline regression model for run value estimation."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


FEATURE_COLUMNS = [
    "release_speed",
    "horizontal_break_inches",
    "induced_vertical_break_inches",
    "plate_x",
    "plate_z",
    "balls",
    "strikes",
    "count",
]


@dataclass
class RunValueArtifacts:
    model: Pipeline
    X_test: pd.DataFrame
    y_test: pd.Series
    y_pred: pd.Series


def fit_run_value_model(df: pd.DataFrame, random_state: int = 42) -> RunValueArtifacts:
    """Fit a baseline tree-based regressor for pitch-level run value."""
    X = df[FEATURE_COLUMNS].copy()
    y = df["run_value_target"].astype(float)

    numeric_features = [
        "release_speed",
        "horizontal_break_inches",
        "induced_vertical_break_inches",
        "plate_x",
        "plate_z",
        "balls",
        "strikes",
    ]
    categorical_features = ["count"]

    preprocess = ColumnTransformer(
        transformers=[
            ("numeric", SimpleImputer(strategy="median"), numeric_features),
            (
                "categorical",
                Pipeline(
                    steps=[
                        ("impute", SimpleImputer(strategy="most_frequent")),
                        ("encode", OneHotEncoder(handle_unknown="ignore")),
                    ]
                ),
                categorical_features,
            ),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocess", preprocess),
            (
                "regressor",
                RandomForestRegressor(
                    n_estimators=200,
                    max_depth=8,
                    min_samples_leaf=25,
                    random_state=random_state,
                    n_jobs=-1,
                ),
            ),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=random_state
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return RunValueArtifacts(model, X_test, y_test, pd.Series(y_pred))
