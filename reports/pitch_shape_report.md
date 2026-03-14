# Pitch Shape Clustering

## Question

Can public pitch-tracking features be used to identify interpretable pitch-shape clusters that may help frame pitch design and evaluation questions?

## Data

Public Statcast-style pitch data pulled through `pybaseball`-compatible workflows.

## Method

Features included release speed, horizontal and vertical movement, location features, and selected release characteristics where available. After cleaning and standardization, KMeans clustering was used to group similar pitch shapes. PCA was used for low-dimensional visualization.

## Preliminary Findings

This workflow is designed to surface pitch families with similar shape characteristics and provide a foundation for downstream analysis such as whiff tendency, command profile, or pitcher-specific design questions. Current outputs are exploratory and intended as a baseline rather than a final production model.

## Limitations

Public data is incomplete relative to proprietary team datasets. Cluster structure is sensitive to feature selection, preprocessing, and the chosen number of clusters.

## Next Steps

Incorporate pitcher handedness, compare cluster stability, and connect pitch-shape groups to outcome metrics such as whiff rate, chase rate, and run value.
