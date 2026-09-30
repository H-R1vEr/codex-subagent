---
name: scenario-earthquake
description: "Construct reproducible earthquake scenarios and conditional ground-motion estimates. Use for scenario planning, not probabilistic hazard or earthquake prediction."
---

# 情景地震 / scenario-earthquake

## Input contract

Use the user's actual artifacts, purpose and permitted output location. Identify missing inputs that affect the result; label assumptions. Instructions are a workflow, not an embedded numerical engine. Install or use scientific software only when needed and available. Preserve originals and distinguish observed, simulated and historical evidence.

## Workflow

1. Define purpose, geographic extent, magnitude scale, rupture geometry, mechanism, depth and scenario rationale. Document coordinates/CRS and source provenance; separate user assumptions from observations.
2. Compute the distance metrics required by the selected model from geometry. Do not substitute epicentral distance for rupture distance without a declared approximation.
3. Choose applicable GMMs, site parameters and component/period definitions. Report median and appropriate quantiles; distinguish conditional scenario exceedance from annual hazard probabilities.
4. For spatial realizations specify inter/intra-event variability and spatial/cross-period correlation, with sensitivity to unknown site terms. Independent per-site draws do not represent a coherent spatial field.
5. Verify geometry, unit conversions and model domain. Map uncovered cells and avoid false precision in sparse site information.
6. If operational or policy decisions are requested, state how the scenario was validated and the uncertainty that matters; do not present a scenario as a forecast or official hazard map.

## Deliverable

Scenario manifest; geometry/distance checks; site-by-period estimates/maps; uncertainty assumptions; reproducible commands and interpretation boundaries.

Include source locators and environment/method details needed to check the result. State the weakest evidence and the largest remaining gap; use “none identified” when applicable.

## Acceptance scenario

An Mw 7 scenario map requests a yearly exceedance probability: explain that scenario conditional estimates cannot supply an annual rate without a recurrence/hazard model.
