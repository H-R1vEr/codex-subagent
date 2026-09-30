---
name: figure-audit
description: "Audit scientific figures against source data, uncertainty and manuscript claims. Use for figure correctness and evidence presentation, not cosmetic redesign alone."
---

# 图件审计 / figure-audit

## Input contract

Use the user's actual artifacts, purpose and permitted output location. Identify missing inputs that affect the result; label assumptions. Instructions are a workflow, not an embedded numerical engine. Install or use scientific software only when needed and available. Preserve originals and distinguish observed, simulated and historical evidence.

## Workflow

1. Read the figure, caption, underlying table/code and linked claim. If pixels or source data cannot be inspected, identify that limitation rather than verifying visual correctness.
2. Check axes, units, log bases, sample sizes, aggregation, excluded data, color scales and reference lines. Trace plotted quantities to computations and inspect uncertainty definitions and dependencies.
3. Review panel sequence, readability, accessibility, caption completeness and consistency of symbols. Inspect diagram-internal text, arrows and equations, not just captions.
4. Verify that transformations, clipping, normalization or smoothing do not conceal material results. Compare exports to source plots when available.
5. Separate numerical errors, unsupported interpretation and presentation issues. Propose repairs without altering scientific sources; export formats follow the user's journal/output requirements.

## Deliverable

Panel-by-panel audit with evidence/locators, severity and corrections; visual checks performed and unavailable data; corrected figures only when requested.

Include source locators and environment/method details needed to check the result. State the weakest evidence and the largest remaining gap; use “none identified” when applicable.

## Acceptance scenario

An uncertainty band is SD but the caption calls it a 95% CI: report the mismatch and recompute only with an appropriate sampling model.
