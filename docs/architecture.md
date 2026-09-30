# Architecture and execution contract

The package has a flat installable `skills/` tree with seven earthquake workflows, five evidence/reasoning workflows, one router and one optional journal bridge. `catalog.json` is the shared source for validation and skill cards.

Skills are instruction packages. They do not register a new agent runtime, numerical model or tool connector. Triggering remains host-dependent. No required cloud API, credentials or paid model calls are built into the package.

## Artifact contract

Each analysis records input IDs/hashes when appropriate, inclusion rules, method/version, units, environment, output location and source locators. Missing or inaccessible evidence stays marked. Outputs distinguish measured, modeled, simulated and historical values.

## Orchestration

The router constructs a dependency plan. Shared immutable inputs may feed separate audit branches; mutable outputs have one owner. A merge includes provenance and resolves conflicts. Unsupported delegation falls back to sequential work. Dependencies cannot be bypassed merely to increase concurrency.

## Limits

There is no embedded scientific solver, automatic data acquisition pipeline, background monitor or publication action. A user can request those in a task and the agent can use available authorized tools. Real scientific end-to-end acceptance requires supplied data, benchmark comparisons and expert review. Journal constraints are optional and versioned separately.
