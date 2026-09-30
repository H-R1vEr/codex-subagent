# Example prompts

Replace file paths and parameters with actual supplied inputs. These are explicit invocation examples; implicit selection is host-dependent. Prompts do not authorize external publishing or delegation unless they say so.

## Waveforms

```text
Use $ground-motion-analysis on the supplied acceleration records.
Units are cm/s²; sampling is 0.005 s. Compute PGA and 5%-damped PSA
at 0.1, 0.2, 1 and 2 s for each provided component. Preserve originals,
record processing settings, check numerical convergence and flag clipped records.
```

## GMM and REML

```text
Use $researchflow-router on these observed/predicted tables and metadata.
Check record/period joins and natural-log units before residual analysis.
Then use $mixed-effects-reml for crossed event/station effects where identifiable.
Report diagnostics, variance boundaries and uncertainty. Do not substitute
missing predictors or call historical logs a current rerun.
```

## Decomposition and simulation

```text
Use $event-path-site-decomposition to assess whether my coverage supports
separate path effects. Identify constraints and test synthetic recovery before
physical attribution. If unidentifiable, return that result and the data needed.
```

```text
Use $random-vibration-simulation with my supplied regional parameter file.
Distinguish RVT from time-history simulation; document units, duration and peak
factor. Use a seeded ensemble, test grid/ensemble convergence and cite benchmarks.
```

## Scenario and rapid assessment

```text
Use $scenario-earthquake for the attached Mw 6.5 rupture geometry and site table.
Provide conditional median/quantiles, distance checks and model-domain limits.
No annual hazard probabilities are requested.
```

```text
Use $earthquake-rapid-analysis for the specified event as of the time I give.
Preserve agency magnitude types/revisions, cite retrieval times and distinguish
observations from modeled shaking. Do not infer casualties from exposure.
```

## Manuscript review with authorized concurrency

```text
Use $researchflow-router on my manuscript, figures and reproducibility package.
You may delegate independent figure-audit and reproducibility-audit branches
if agent tools are available. Give each branch a separate output directory.
Merge evidence by claim/artifact ID, then use $evidence-chain, $reviewer-audit
and $paper-storyline as needed. No changes to scientific source files.
```

## Optional journal layer

```text
Use $journal-bridge for a Nature research article. Check installed journal skills
and current publisher guidance. If absent, identify the installation path and
continue the evidence audit. Do not claim a journal package ran unless it did.
```
