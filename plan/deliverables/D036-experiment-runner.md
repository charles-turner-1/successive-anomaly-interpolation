# D036 — Build the reproducible experiment runner

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D030–D035
- **Hypotheses:** H0, H2–H10
- **Verification classes:** V2

## Objective

Run any registered estimator on any registered dataset from a frozen configuration.

## Procedure

1. Define a run configuration referencing dataset, estimator, tuning, resources, seed, and output location.
2. Resolve and validate all referenced schemas before executing.
3. Isolate fit, validation, final evaluation, and reporting phases.
4. Capture stdout, stderr, warnings, exit status, wall time, CPU time, peak memory, and environment metadata.
5. Write outputs atomically and hash them.
6. Implement resume by content-addressed completed runs, never by filename alone.
7. Implement a dry-run that expands the complete run matrix.
8. Add local and CI smoke configurations.

## Required checks

- Repeat an identical run in clean processes and compare hashes.
- Interrupt and resume a run; confirm no mixed or partial result is accepted.
- Deliberately alter an input and confirm cache invalidation.

## Machine verification

`pixi run verify-card -- D036` must pass deterministic, interruption, cache, schema, and provenance tests.

## Primary artifact

Command-line runner, configuration schema, result validator, and environment lockfile.

## Acceptance

- A clean process reproduces a result from one command.
- Interrupted runs resume without mixing configurations.
- Outputs include code revision, dependency versions, seed, and input hashes.

## Failure or escalation

Manual notebook-only execution does not satisfy this card.
