---
name: event-path-site-decomposition
description: "Decompose seismic residuals into event, path and site contributions with identifiability checks. Use when physical attribution beyond a residual fit is requested."
---

# 震源—路径—场地分解 / event-path-site-decomposition

## Input contract

Use the user's actual artifacts, purpose and permitted output location. Identify missing inputs that affect the result; label assumptions. Instructions are a workflow, not an embedded numerical engine. Install or use scientific software only when needed and available. Preserve originals and distinguish observed, simulated and historical evidence.

## Workflow

1. Define the physical terms, baseline GMM and equation before estimating components. Declare whether path means a distance trend, regional cell attenuation, source-receiver geometry, or an unexplained residual.
2. Inspect event-station coverage, repeated paths, geographic balance and design connectivity. State zero-mean constraints, reference levels, priors or regularization; expose unidentifiable terms.
3. Separate descriptive random effects from physical mechanism claims. Event effects can absorb magnitude bias; site effects can absorb instrument bias; a leftover residual is not automatically a path effect.
4. Estimate only supported terms and preserve covariance/uncertainty. If path is spatially modeled, document cell/path lengths, smoothness assumptions and resolution tests.
5. Use held-out events/stations/regions according to the prediction target; avoid random record splits that leak group information. Run a synthetic recovery test with known components before causal interpretation.
6. Check sensitivity to baseline model, constraints, sparse groups and regularization. Report locations or terms the data cannot resolve.

## Deliverable

Term definitions and identifiability assessment; coverage matrix/map; estimates with uncertainty; held-out validation; synthetic recovery and a bounded interpretation.

Include source locators and environment/method details needed to check the result. State the weakest evidence and the largest remaining gap; use “none identified” when applicable.

## Acceptance scenario

A site effect appears only because one instrument is miscalibrated: retain instrument checks as an alternative explanation. No repeated paths means separate path estimates may be unidentifiable.
