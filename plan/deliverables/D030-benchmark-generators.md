# D030 — Implement benchmark generators

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D002, D004
- **Hypotheses:** H2, H3, H6, H8, H10
- **Verification classes:** V2
- **Source:** [Benchmark matrix](../../vault/05%20Experiments/Benchmark%20matrix.md)

## Objective

Create deterministic generators for the smallest datasets needed to distinguish the competing claims.

## Procedure

1. Translate every selected benchmark row into a schema containing domain, truth function, background, sampling, noise, masks, and split rules.
2. Implement pure generator functions taking only configuration and seed.
3. Generate train, validation, test, and dense truth evaluation sets without shared random draws unless explicitly required.
4. Implement analytic spectra or high-resolution reference calculations where available.
5. Add boundary values: zero noise, maximal allowed noise, empty mask component, periodic seam, and duplicate sites.
6. Serialize canonical fixtures and hashes.
7. Document each generator's assumptions and which hypotheses it can test.

## Required checks

- Property-test shapes, finiteness, repeatability, split disjointness, and empirical noise moments.
- Confirm identical seed/configuration yields byte-identical canonical output.

## Machine verification

`pixi run verify-card -- D030` must regenerate fixture hashes and pass all generator properties.

## Primary artifact

Tested generators for dyadic sinusoids, Franke, split-basin, background-plus-anomalies, and anisotropic ridge cases.

## Acceptance

- Every generator accepts an explicit seed and emits truth, observations, background, noise metadata, and splits.
- Units and coordinate transforms are recorded.
- Fixtures verify known spectra, masks, and noise moments.

## Failure or escalation

Split any generator whose scientific assumptions cannot be stated independently of an estimator.
