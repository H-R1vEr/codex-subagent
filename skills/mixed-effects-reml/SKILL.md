---
name: mixed-effects-reml
description: "Fit and diagnose linear mixed models using REML with crossed event and station effects. Use for variance estimation and uncertainty, not choosing fixed effects by REML likelihood."
---

# 混合效应 REML / mixed-effects-reml

## Input contract

Use the user's actual artifacts, purpose and permitted output location. Identify missing inputs that affect the result; label assumptions. Instructions are a workflow, not an embedded numerical engine. Install or use scientific software only when needed and available. Preserve originals and distinguish observed, simulated and historical evidence.

## Workflow

1. Specify response, fixed-effect design and grouping IDs before fitting. For crossed seismic residuals consider r_ij = X_ij beta + eta_i + delta_j + epsilon_ij; distinguish crossed from nested IDs.
2. Audit repeated observations, group sizes, connectivity, rank deficiency and confounding of fixed and random effects. A model cannot recover a site term for an unobserved site.
3. Fit with a documented package/version and optimizer; retain convergence messages, gradients when available, singularity checks and variance boundary estimates. A zero variance is a possible boundary solution, not a reason to invent positive variance.
4. Use ML when comparing different fixed-effect structures by likelihood; REML comparisons require the same fixed-effect design and compatible likelihoods. Return to REML for final variance estimates when justified.
5. Report fixed-effect uncertainty, variance components, residual checks and influence by event/station. For intervals use an explicitly chosen profile or bootstrap method; specify whether bootstrap resamples events, stations, or a crossed design and why.
6. Record BLUP shrinkage and distinguish conditional random-effect estimates from independent observations. Compare implementations using identical design matrices, levels and tolerances, not merely similar formulas.

## Deliverable

Model formula and design summary; variance/uncertainty table; fit diagnostics; package/environment manifest; reproducible fit command and limitations of sparse groups.

Include source locators and environment/method details needed to check the result. State the weakest evidence and the largest remaining gap; use “none identified” when applicable.

## Acceptance scenario

One station occurs in only one event: identify weak event/site separation. Different fixed-effect formulas must not be ranked with REML AIC as though the likelihoods were directly comparable.
