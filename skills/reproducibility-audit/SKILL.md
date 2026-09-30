---
name: reproducibility-audit
description: "Audit whether scientific outputs can be traced and rerun from inputs, code and environments. Use for provenance, rerun and delivery checks."
---

# 可复现性审计 / reproducibility-audit

## Input contract

Use the user's actual artifacts, purpose and permitted output location. Identify missing inputs that affect the result; label assumptions. Instructions are a workflow, not an embedded numerical engine. Install or use scientific software only when needed and available. Preserve originals and distinguish observed, simulated and historical evidence.

## Workflow

1. Inventory the claimed outputs and source boundaries. Hash available inputs, code/config and outputs; record environment, commands, seed, versions and data access/licensing requirements.
2. Classify each claim as reproducible from supplied inputs, partially reproducible or blocked. Frozen-output reproduction and rebuilding the raw cohort are separate gates.
3. Run only authorized reruns in an isolated output directory. Record stdout/stderr, return code, elapsed time and differences using declared tolerances. Preserve failure evidence and originals.
4. Check record IDs, selection counts, numerical deltas and plots. A successful import or unit test is not a successful scientific reproduction.
5. Document external downloads, missing credentials/data, hardware dependencies and non-determinism without exposing secrets. Historical logs are historical evidence, not a current rerun.
6. Deliver a manifest and rerun recipe with exact blockers and the untested work. Do not convert partial evidence into unconditional PASS.

## Deliverable

Artifact inventory/hashes; environment and rerun commands; selection and comparison diagnostics; PASS/PASS_WITH_LIMITATIONS/BLOCKED per output; exact missing requirements.

Include source locators and environment/method details needed to check the result. State the weakest evidence and the largest remaining gap; use “none identified” when applicable.

## Acceptance scenario

Frozen predictions reproduce but 30% of raw IDs are missing: pass only frozen-output reproduction and keep cohort reconstruction blocked.
