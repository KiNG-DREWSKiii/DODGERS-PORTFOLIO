# Run Value Decision Engine

## Question

Can a simple context-aware public-data model provide a useful first approximation of pitch-level run value for strategy-oriented analysis?

## Data

The workflow uses public Statcast-compatible pitch-level data. The starter target maps observed events to approximate run-value weights to create a simple supervised learning target.

## Method

- clean pitch records with movement, location, and count information
- derive a simple event-to-run-value target
- build count and movement features
- fit a baseline regression model
- summarize prediction error and inspect grouped run value by count

## Preliminary Findings

No finished results are claimed. The current repository provides a transparent baseline framework that can be turned into a more realistic expected value model with better state definition and richer target construction.

## Limitations

- event-based weights are a simplification of full run expectancy modeling
- the current target ignores base-out state and inning context
- public data may require more filtering to isolate decision-relevant observations

## Next Steps

- construct a proper run expectancy table
- compare direct regression against grouped empirical value estimates
- add base-out state and pitch sequencing information
- test whether pitch types or locations carry stable incremental signal within count states
