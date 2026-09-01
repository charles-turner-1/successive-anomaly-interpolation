# D032 — Implement one-stage baselines

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D030, D031
- **Hypotheses:** H2, H4
- **Verification classes:** V2

## Objective

Implement tuned one-stage kernel ridge and DIVAnd-compatible variational baselines.

## Procedure

1. Implement the common estimator interface and configuration schemas.
2. Implement kernel ridge from stated equations or wrap a pinned library with an equivalence test.
3. Implement/wrap DIVAnd in the committed Julia project with background subtraction and reconstruction explicit.
4. Expose fit, predict, uncertainty where available, residuals, solver state, and resource metrics.
5. Implement validation-only hyperparameter search with deterministic tie-breaking.
6. Add analytic and hand-sized fixtures.
7. Serialize all results through D031.

## Required checks

- Compare kernel ridge against a direct dense solve on small matrices.
- Compare DIVAnd primal/dual or direct/iterative paths where estimator-equivalent.
- Assert no test data enters tuning.

## Machine verification

`pixi run verify-card -- D032` must run Python tests through Pixi and Julia tests with `--project=julia` using committed lockfiles.

## Primary artifact

Baseline modules plus unit tests and a hyperparameter-search manifest.

## Acceptance

- Both fit and predict through one common interface.
- Search spaces and validation budgets are explicit.
- Small noiseless fixtures achieve expected interpolation accuracy.

## Failure or escalation

A baseline that cannot be tuned fairly blocks confirmatory comparison rather than being weakened.
