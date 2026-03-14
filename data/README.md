# Data Notes

This repository is designed around public baseball data sources.

Expected sources include:

- `pybaseball` access to MLB Statcast-style pitch-level data
- FanGraphs-aligned concepts for run value and plate discipline framing
- baseball reference material for terminology and validation when needed

## Folder usage

- `raw/`: downloaded or directly queried source extracts
- `processed/`: cleaned modeling tables and derived datasets

Large datasets are not committed to this repository. Raw and processed extracts should be generated locally and kept out of version control unless they are very small reference samples.

Recommended naming pattern:

- `raw/statcast_2024_03_28_2024_04_30.csv`
- `processed/pitch_shape_features_2024_03_28_2024_04_30.parquet`

All modeling code in `src/` assumes public-data-compatible columns and avoids reliance on private team datasets.
