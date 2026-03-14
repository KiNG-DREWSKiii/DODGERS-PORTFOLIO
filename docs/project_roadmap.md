# Project Roadmap

This roadmap is structured to keep the portfolio realistic, reproducible, and manageable on public baseball data.

## Phase 1: Initial Scaffold

- [x] Create repository structure
- [x] Add shared utility modules
- [x] Add project-level scripts and reports
- [x] Add lightweight tests

## Phase 2: Public Data Ingestion

- [ ] Confirm target date ranges for initial analyses
- [ ] Pull pitch-level Statcast data with `pybaseball`
- [ ] Save raw extracts with clear filenames
- [ ] Document source assumptions in notebooks and reports

## Phase 3: Feature Engineering

- [ ] Standardize column names and basic cleaning
- [ ] Build movement and velocity features for pitch-shape work
- [ ] Build location, count, and handedness features for swing modeling
- [ ] Build count-state and event-value features for run-value work

## Phase 4: Baseline Models

- [ ] Fit KMeans and PCA workflow for pitch clusters
- [ ] Fit logistic regression baseline for swing decisions
- [ ] Fit regression baseline for run value estimation
- [ ] Record model assumptions and tradeoffs

## Phase 5: Evaluation

- [ ] Inspect cluster separation and pitch-family plausibility
- [ ] Measure classification quality with ROC AUC and threshold metrics
- [ ] Measure regression quality with RMSE and MAE
- [ ] Compare baselines against simple null models

## Phase 6: Refinement

- [ ] Add handedness-specific or pitch-type-specific slices
- [ ] Compare linear baselines with tree-based models
- [ ] Improve missing-data handling and calibration checks
- [ ] Add feature importance or sensitivity diagnostics

## Phase 7: Writeups

- [ ] Tighten notebook narratives
- [ ] Export one polished figure per project
- [ ] Update markdown reports with findings and limitations
- [ ] Convert strongest project outcomes into resume bullets
