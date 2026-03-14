import pandas as pd

from src.project1_pitch_shape.clustering import run_pitch_clustering
from src.project1_pitch_shape.features import build_pitch_shape_features


def test_pitch_shape_pipeline_smoke_runs_on_synthetic_data():
    df = pd.DataFrame(
        {
            "pitch_type": ["FF", "FF", "SL", "SL", "CH", "CH"],
            "release_speed": [96.0, 95.2, 84.1, 83.8, 87.2, 86.9],
            "pfx_x": [0.4, 0.35, -0.15, -0.2, 0.1, 0.08],
            "pfx_z": [1.4, 1.35, 0.2, 0.15, 0.75, 0.7],
            "plate_x": [0.1, -0.2, 0.3, -0.1, 0.0, 0.2],
            "plate_z": [2.8, 3.0, 2.2, 2.4, 1.9, 2.1],
        }
    )

    features = build_pitch_shape_features(df)
    result = run_pitch_clustering(features, n_clusters=3, random_state=7)

    assert len(result.labeled_data) == len(df)
    assert result.cluster_summary["cluster"].nunique() == 3
    assert {"pc1", "pc2", "cluster"}.issubset(result.labeled_data.columns)
