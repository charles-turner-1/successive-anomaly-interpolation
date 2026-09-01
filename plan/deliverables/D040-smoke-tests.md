# D040 — Run smoke tests

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D036
- **Hypotheses:** exploratory only
- **Verification classes:** V2

## Objective

Detect broken metrics, unreasonable search ranges, numerical failures, and runtime surprises before preregistration.

## Procedure

1. Reserve and record smoke-only seeds that can never enter confirmation.
2. Use the runner dry-run to enumerate all core estimator/dataset combinations.
3. Execute one minimal and one moderate configuration for every combination.
4. Run automated sanity tests for finite outputs, schema validity, residual identities, uncertainty ordering, and resource capture.
5. Generate standard diagnostic plots from code, not manual spreadsheet edits.
6. Classify every warning/failure and repair implementation defects.
7. Propose any search-range or threshold changes with before/after evidence.
8. Repeat until every core path completes without unexplained failure.

## Required checks

- Assert smoke seed IDs are rejected by confirmation manifests.
- Reproduce the final smoke bundle from its configuration and code hash.

## Machine verification

`pixi run verify-card -- D040` must validate the complete run matrix, result schemas, seed exclusion, and diagnostic invariants.

## Primary artifact

`reports/smoke-tests.md` plus raw results on seeds reserved from confirmation.

## Acceptance

- Every estimator completes every core dataset at least once.
- Metrics and diagnostic plots are manually sanity-checked.
- Proposed threshold or search-range changes are justified and recorded.

## Failure or escalation

Smoke-test results cannot count as confirmatory evidence. Repair failures, rerun smoke tests, then proceed.
