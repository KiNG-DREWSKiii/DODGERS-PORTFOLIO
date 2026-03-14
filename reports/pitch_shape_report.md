# Pitch Shape Clustering

## Question

Can public pitch-tracking features be used to identify interpretable pitch-shape clusters that may help frame pitch design and evaluation questions?

## Data

Public Statcast-style pitch data pulled through `pybaseball`-compatible workflows.

## Features

Release speed, horizontal movement, vertical movement, and plate location.

## Method

Movement and velocity features were cleaned, standardized, and clustered with KMeans. PCA was used for two-dimensional visualization.

## Results

The initial clustering separates broad pitch-shape families based on movement and velocity. The current output is most useful as a starting point for pitcher-level review, outcome analysis, and feature refinement.

## Limitations

Public data is incomplete relative to proprietary team datasets. Cluster structure is sensitive to feature selection, preprocessing, and the chosen number of clusters.

## Next steps

Incorporate pitcher handedness, compare cluster stability, and connect pitch-shape groups to outcome metrics such as whiff rate, chase rate, and run value.
