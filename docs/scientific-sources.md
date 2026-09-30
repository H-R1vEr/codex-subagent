# Scientific reference map

These sources ground method choices; consult the relevant source/implementation for exact equations and conventions. The skills are original workflow instructions, not reproductions of these works.

| Area | Source | What it supports / boundary |
|---|---|---|
| Response spectra | [Newmark (1959), A Method of Computation for Structural Dynamics](https://doi.org/10.1061/JMCEA3.0000098) | Numerical integration; time-step accuracy still needs validation |
| Ground-motion sigma | [Al Atik et al. (2010), The Variability of Ground-Motion Prediction Models and Its Components](https://doi.org/10.1785/gssrl.81.5.794) | Variability terminology; no bundled predictor model |
| REML implementation | [Bates et al. (2015), Fitting Linear Mixed-Effects Models Using lme4](https://doi.org/10.18637/jss.v067.i01) | Model fitting and diagnostics; installed version must be recorded |
| Stochastic simulation | [Boore (2003), Simulation of Ground Motion Using the Stochastic Method](https://doi.org/10.1007/PL00012553) | Source/path/site approach; parameters need regional calibration |
| Nonergodic modeling | [Landwehr et al. (2016), A Nonergodic Ground-Motion Model for California](https://doi.org/10.1785/0120150118) | Spatial effects and nonergodicity; does not establish identifiability in your sample |
| Hazard implementation | [OpenQuake documentation](https://docs.openquake.org/oq-engine/) | Inspect exact model/version and required predictors |
| Rapid event sources | [USGS earthquake feeds](https://earthquake.usgs.gov/earthquakes/feed/) | Preliminary source/revision retrieval; not global sole authority |

Bibliographic pointers are provided for review; live access to full text and model-specific scientific acceptance are outside the V1 structural tests. Cite the exact source used in an actual analysis rather than attaching this whole list to every result.
