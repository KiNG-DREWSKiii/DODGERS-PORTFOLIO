# Swing Decision Model

## Question

How much of swing versus take behavior can be explained with a baseline public-data model built from pitch location, movement, velocity, and count context?

## Data

The project uses public pitch-level data pulled through `pybaseball`. The starter table uses pitch description, location, movement, velocity, and count fields that are widely available in Statcast-style extracts.

## Method

- define a binary target for swing versus take based on pitch description
- engineer clipped plate-location features and movement variables
- add count-state context
- fit a logistic regression baseline using a preprocessing pipeline
- evaluate with accuracy, ROC AUC, and log loss

## Preliminary Findings

No finished model results are claimed yet. The current codebase is structured to produce a reproducible baseline classifier and evaluation summary, which can then be extended with richer context or more flexible models.

## Limitations

- the target simplifies a more nuanced swing-decision problem
- no batter-specific context is included in the starter version
- calibration and threshold tuning are not yet emphasized

## Next Steps

- compare against count-only and location-only baselines
- add batter and pitcher handedness
- test gradient boosted models against the linear baseline
- examine decision quality within and outside the strike zone
