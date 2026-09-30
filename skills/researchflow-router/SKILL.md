---
name: researchflow-router
description: "Route multi-step earthquake research and manuscript tasks to relevant ResearchFlow skills with dependency-aware parallel suggestions. Use for combined workflows, not every single-task request."
---

# 科研任务路由 / researchflow-router

## Input contract

Use the user's actual artifacts, purpose and permitted output location. Identify missing inputs that affect the result; label assumptions. Instructions are a workflow, not an embedded numerical engine. Install or use scientific software only when needed and available. Preserve originals and distinguish observed, simulated and historical evidence.

## Workflow

1. Read the user's requested outcome, supplied artifacts and side-effect boundaries. For a fully specified task proceed; ask one focused clarification only if a missing input changes the analysis materially.
2. Read references/routing.md to map the task to skill names. Select the smallest relevant set; do not run every audit for a simple waveform request.
3. Build a dependency plan listing each task's input, selected skill, output, owner/output directory and prerequisites. Data selection and predictor mapping precede model comparisons; a storyline follows verified results.
4. Suggest independent branches (e.g. figure audit and reproducibility inventory) for concurrency. Execute delegated branches only when tools are available and delegation is authorized by the user/environment. Otherwise perform them sequentially and state that concurrency was a suggestion. A SKILL.md does not provide a scheduler.
5. Read selected SKILL.md entrypoints from the sibling installed directories; read their own references only as needed. Do not assume optional journal skills or numerical packages are installed.
6. Give each worker an immutable input boundary and distinct outputs; merge by stable artifact/record/claim IDs. Resolve conflicting results using inspectable sources, not majority voting.
7. Return an integrated result with links, checks, blockers and next steps. Never claim skills executed, results verified or a rerun completed merely because a plan lists them.

For routing choices read [routing reference](references/routing.md).

## Deliverable

Compact task/dependency table; selected skills and availability; concurrency eligibility; integrated artifact/evidence ledger and unresolved blockers.

Include source locators and environment/method details needed to check the result. State the weakest evidence and the largest remaining gap; use “none identified” when applicable.

## Acceptance scenario

A request combines residual fitting and figure review: fit-dependent plots wait for the residual table; an audit of pre-existing figure exports can proceed independently.
