# Dodgers Quant Portfolio

Public baseball analytics portfolio built by Drew Goldman to demonstrate quantitative research ability using Python and public Statcast-style data.

This repository highlights three applied projects in pitch modeling, swing decision analysis, and run value estimation. It is designed to showcase clean analytical workflow, reproducible research habits, and clear technical communication for baseball operations and quantitative analysis roles.

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

## Projects

### 1. Pitch Shape Clustering

Clusters pitch shapes using velocity and movement features derived from public Statcast-style pitch data. The project is meant to show comfort with pitch physics, feature engineering, unsupervised learning, and exploratory baseball research workflow.

### 2. Swing Decision Model

Builds a baseline classifier for swing versus take behavior using location, count, and movement features. The project focuses on decision modeling, feature preparation, and classification evaluation.

### 3. Run Value Decision Engine

Estimates context-aware run value using count state, pitch characteristics, and outcome information. The project highlights strategy-oriented modeling and connects pitch-level outcomes to baseball value.

## Tools and Skills

- Python
- SQL
- MATLAB
- C++
- PyTorch
- machine learning
- statistical analysis
- time-series analysis
- data visualization
- research workflows

## Repository layout

- `src/`: reusable utilities and project modules
- `docs/`: role alignment, roadmap, and resume-oriented summaries
- `data/`: raw and processed data directories
- `reports/`: concise research memos for each project
- `notebooks/`: exploratory and presentation-ready notebooks
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
