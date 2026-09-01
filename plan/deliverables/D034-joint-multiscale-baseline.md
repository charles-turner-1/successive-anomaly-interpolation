# D034 — Implement the joint multiscale baseline

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D012, D030, D031
- **Hypotheses:** H2, H5
- **Verification classes:** V1, V2

## Objective

Fit all nominated length scales jointly using an additive kernel or valid mixture covariance.

## Procedure

1. Implement the D012 component covariance and weight constraints.
2. Assemble the joint covariance/objective without sequential freezing.
3. Implement fitting, prediction, uncertainty, and diagnostics through the common interface.
4. Use the identical component scale list supplied to D033.
5. Implement deterministic validation-only tuning of weights and regularization.
6. Detect redundant components and ill-conditioning explicitly.
7. Serialize component and aggregate quantities separately.

## Required checks

- Check PSD numerically and prove nonnegative weighted PSD closure in Lean.
- Compare a one-component mixture with D032.
- Check permutation invariance of component order.

## Machine verification

`pixi run verify-card -- D034` must compile the PSD theorem and pass numeric equivalence and permutation tests.

## Primary artifact

Joint baseline module, positive-semidefiniteness tests, and matched-budget tuning configuration.

## Acceptance

- It uses the same component scales and observation information as D033.
- Mixture constraints are enforced.
- Parameter and compute accounting is comparable with D033.

## Failure or escalation

Numerical failure triggers conditioning work; it does not automatically count as evidence for succession.
