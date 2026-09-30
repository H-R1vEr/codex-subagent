# Synthetic residual example

All four records are invented arithmetic fixtures, not observations, a validated GMM or a REML acceptance dataset. The 2×2 design is too small to justify a scientific variance decomposition.

```bash
python scripts/demo_residuals.py --output local-results/demo.json
```

The script reads [records.csv](records.csv), rejects duplicate IDs/nonpositive values and computes `ln(observed_g) - ln(predicted_g)`. It compares every result with [expected.json](expected.json) at absolute tolerance `1e-12`, records the input SHA-256 and writes only to a new user-selected output file.

Ask `$gmm-residual-analysis` to inspect the fixture, explain units/joins, and identify why this is insufficient for model validation. Ask `$mixed-effects-reml` whether the design supports reliable estimation; an honest answer should expose the sparse-data limit.
