---
name: random-vibration-simulation
description: "Simulate stochastic earthquake motion or apply random vibration theory with explicit source, path, site and duration assumptions. Use for stochastic simulations, not deterministic rupture solvers."
---

# 随机振动模拟 / random-vibration-simulation

## Input contract

Use the user's actual artifacts, purpose and permitted output location. Identify missing inputs that affect the result; label assumptions. Instructions are a workflow, not an embedded numerical engine. Install or use scientific software only when needed and available. Preserve originals and distinguish observed, simulated and historical evidence.

## Workflow

1. Choose the requested product: RVT peak/spectrum estimates or stochastic time histories. State the source spectrum, stress parameter, corner frequency, path attenuation/Q, geometric spreading, kappa/site amplification and duration model with sources and units.
2. Do not interchange Fourier amplitude spectra, power spectral density, oscillator response and pseudo-spectral acceleration. Specify Fourier normalization, one/two-sided conventions and frequency grid.
3. For RVT, document spectral moments, effective duration and peak-factor formulation; account for oscillator duration where required. For time histories, document sampling, envelope, phase construction and random seed.
4. Run an ensemble and assess numerical convergence over grid, time step and realization count. Check energy/spectral targets and compare a published benchmark or trusted implementation.
5. Separate aleatory ensemble variability from uncertain model parameters. State calibration range and flag extrapolation; simulated waveforms are synthetic and do not count as observed records.
6. Preserve parameter manifests and seed lists so the ensemble can be rerun. Do not tune stress drop solely to make an unverified spectrum agree.

## Deliverable

Parameter/source manifest; seeded simulation or RVT results; convergence/benchmark checks; uncertainty distinction and explicit synthetic labels.

Include source locators and environment/method details needed to check the result. State the weakest evidence and the largest remaining gap; use “none identified” when applicable.

## Acceptance scenario

Doubling ensemble size changes upper quantiles strongly: flag unconverged tails. A zero-duration input must be rejected instead of yielding plausible-looking peaks.
