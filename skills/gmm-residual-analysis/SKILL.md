---
name: gmm-residual-analysis
description: "Compare observed ground motion with published GMM predictions and diagnose residual patterns. Use for model evaluation, not estimating random effects."
---

# GMM 残差分析 / gmm-residual-analysis

## Input contract

Use the user's actual artifacts, purpose and permitted output location. Identify missing inputs that affect the result; label assumptions. Instructions are a workflow, not an embedded numerical engine. Install or use scientific software only when needed and available. Preserve originals and distinguish observed, simulated and historical evidence.

## Workflow

1. Freeze record IDs and inclusion rules. Record model name, implementation/version, region, tectonic regime, intensity measure, period, damping, horizontal component and applicability domain.
2. Build a predictor mapping for magnitude scale, distance definition (Rrup/Rjb/Rhypo), depth, mechanism, Vs30 and basin terms. Missing predictors are missing; a proxy needs a named assumption and sensitivity analysis.
3. Align observations and predictions on a unique record/period key; fail ambiguous joins and produce matched/unmatched/duplicate counts. Distinguish reconstructing a raw cohort from reproducing a frozen prediction table.
4. Convert observations and predictions to common units and natural-log space before computing r = ln(y_obs) - ln(y_pred). Confirm whether a library returns log means or linear medians. Record any log10 conversion.
5. Plot residuals against magnitude, distance and site variables with sample counts; account for event/station dependence in uncertainty. Standardize only with the declared matching sigma definition; total, within-event and between-event sigma are different.
6. Keep out-of-domain predictions separate. Report residual distributions and uncertainty without treating lower residual variance as proof of causal superiority.

## Deliverable

Predictor mapping; row-level observed/predicted/residual table; join diagnostics; domain flags; source/version manifest and residual plots with dependent sampling noted.

Include source locators and environment/method details needed to check the result. State the weakest evidence and the largest remaining gap; use “none identified” when applicable.

## Acceptance scenario

A model returns ln(g) while observations use m/s²: convert observations before subtraction. A duplicate station/date key must not multiply rows silently.
