---
name: ground-motion-analysis
description: "Analyze accelerograms, intensity measures, and response spectra with explicit units and processing provenance. Use for seismic waveform analysis, not GMM fitting."
---

# 地震动分析 / ground-motion-analysis

## Input contract

Use the user's actual artifacts, purpose and permitted output location. Identify missing inputs that affect the result; label assumptions. Instructions are a workflow, not an embedded numerical engine. Install or use scientific software only when needed and available. Preserve originals and distinguish observed, simulated and historical evidence.

## Workflow

1. Read waveform format, station/component IDs, sampling interval, acceleration units, orientation, instrument correction and clipping flags. Preserve input bytes; write processed copies to a separate output directory.
2. Check time spacing, gaps, saturation and baseline drift before computing measures. Treat record rejection as an inspectable selection table, not a silent drop.
3. Record detrending, taper, filter type/order/corners, padding and integration choices. Show sensitivity when processing controls long-period motion; do not infer a filter from a desired result.
4. Compute only requested measures: PGA, PGV, Arias intensity, significant duration or damped pseudo-spectral acceleration. Define each measure, damping, period grid and horizontal combination (component, geometric mean, RotD50/100). Do not relabel a component spectrum as RotD50.
5. Validate spectra against a documented solver or benchmark with step-size checks. Report usable period range and units. Keep invalid samples distinct from physical zeros.

## Deliverable

A record-quality table; processing manifest; intensity/spectrum table with record ID, component, period, damping and units; plots and sensitivity notes. Report numerical checks, rejected records and reasons.

Include source locators and environment/method details needed to check the result. State the weakest evidence and the largest remaining gap; use “none identified” when applicable.

## Acceptance scenario

Two identical acceleration series arrive as g and cm/s²: convert explicitly and compare computed measures. A clipped record must be flagged before calculating a trustworthy PGA.
