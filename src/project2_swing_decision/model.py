"""Baseline classifier for swing decisions."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


FEATURE_COLUMNS = [
    "plate_x_clipped",
    "plate_z_clipped",
    "release_speed",
    "horizontal_break_inches",
    "induced_vertical_break_inches",
    "balls",
    "strikes",
    "count",
]


@dataclass
class SwingModelArtifacts:
    model: Pipeline
    X_test: pd.DataFrame
    y_test: pd.Series
    y_pred: pd.Series
    y_prob: pd.Series


def fit_swing_model(df: pd.DataFrame, random_state: int = 42) -> SwingModelArtifacts:
    """Fit a simple logistic regression classifier for swing decisions."""
    X = df[FEATURE_COLUMNS].copy()
    y = df["swing"].astype(int)

    numeric_features = [
        "plate_x_clipped",
        "plate_z_clipped",
        "release_speed",
        "horizontal_break_inches",
        "induced_vertical_break_inches",
        "balls",
        "strikes",
    ]
    categorical_features = ["count"]

    preprocess = ColumnTransformer(
        transformers=[
            (
                "numeric",
                Pipeline(
                    steps=[
                        ("impute", SimpleImputer(strategy="median")),
                        ("scale", StandardScaler()),
                    ]
                ),
                numeric_features,
            ),
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
            ("classifier", LogisticRegression(max_iter=1000, solver="lbfgs")),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=random_state, stratify=y
    )
    model.fit(X_train, y_train)
    y_prob = model.predict_proba(X_test)[:, 1]
    y_pred = (y_prob >= 0.5).astype(int)

    return SwingModelArtifacts(model, X_test, y_test, pd.Series(y_pred), pd.Series(y_prob))
