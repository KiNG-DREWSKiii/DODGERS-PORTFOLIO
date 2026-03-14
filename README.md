# Dodgers Quant Portfolio

Author: Drew Goldman  
Santa Monica, CA

This repository contains a collection of baseball analytics projects built using Python and public Statcast-style data. The goal of the portfolio is to demonstrate quantitative research skills relevant to baseball operations, including data ingestion, feature engineering, machine learning modeling, visualization, and clear analytical reporting.

The projects explore questions related to pitch movement, swing decisions, and run value estimation using reproducible workflows designed for research environments.

## Featured Project

**Pitch Shape Clustering**  
Unsupervised modeling of pitch movement and velocity features to identify pitch-shape groupings and explore how public tracking data can support pitch design and player evaluation.

## Why this repo

The Los Angeles Dodgers Junior Quantitative Analyst role calls for strong quantitative thinking, clean implementation, and the ability to turn baseball questions into usable models and research outputs. This repo is organized around those signals:

- baseball-facing modeling projects using public data
- readable and testable Python code
- reproducible folder structure and reports
- concise writeups that communicate methods and limitations
- a workflow that supports iterative research rather than one-off notebooks

## Featured Projects

### 1. Pitch Shape Clustering

Clusters pitch shapes using velocity and movement features derived from public Statcast-style pitch data. The project is meant to show comfort with pitch physics, feature engineering, unsupervised learning, and exploratory baseball research workflow.

### 2. Swing Decision Model

Builds a baseline classifier for swing versus take behavior using location, count, and movement features. The project focuses on decision modeling, feature preparation, and classification evaluation.

### 3. Run Value Decision Engine

Estimates context-aware run value using count state, pitch characteristics, and outcome information. The project highlights strategy-oriented modeling and connects pitch-level outcomes to baseball value.

## Tools Used

- Python
- pandas
- NumPy
- scikit-learn
- pybaseball
- matplotlib
- SQL
- MATLAB
- C++
- PyTorch
- statistical modeling and machine learning

## Repository layout

- `src/`: reusable utilities and project modules
- `notebooks/`: exploratory analysis and project narratives
- `reports/`: concise research summaries
- `data/`: raw and processed datasets
- `docs/`: role alignment, roadmap, and resume-oriented summaries
- `tests/`: lightweight validation for shared utilities

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

Run the featured project:

```bash
python -m src.project1_pitch_shape.main
```

## Running Project 1

```bash
python -m src.project1_pitch_shape.main
```

Or:

```bash
bash scripts/run_project1.sh
```

Optional explicit runs:

```bash
python -m src.project1_pitch_shape.main --start-date 2024-03-28 --end-date 2024-04-30 --clusters 6
python -m src.project2_swing_decision.main --start-date 2024-03-28 --end-date 2024-04-30
python -m src.project3_run_value.main --start-date 2024-03-28 --end-date 2024-04-30
```

Shell helper:

```bash
bash scripts/run_project1.sh
```

## Example Output

Generated from the Project 1 clustering workflow on a small March 2024 Statcast sample.

![Pitch Clusters](figures/pitch_shape_clusters.png)

## Application Note

This repository was created as a public demonstration of quantitative research workflows applied to baseball data. It is intended to showcase analytical thinking, reproducible modeling practices, and clear technical communication for baseball operations and quantitative analysis roles.

## Research approach

Each project follows the same basic pattern:

1. Pull public pitch-level data.
2. Apply explicit cleaning and feature engineering.
3. Fit a baseline model.
4. Save outputs and figures in a consistent structure.
5. Summarize findings, limitations, and next steps in markdown.

## Future Work

- expand pitcher and batter handedness adjustments
- compare simple baselines with gradient boosted and neural models
- add calibration analysis for classification projects
- incorporate season-over-season stability checks
- build more polished report figures for application materials

## License

This repository is released under the MIT License.
