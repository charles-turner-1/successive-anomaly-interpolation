# D012 — Specify the joint multiscale comparator

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D004
- **Hypotheses:** H5
- **Verification classes:** V1, V2, V4
- **Source:** [Multiple length-scale covariance](../../vault/02%20Papers/Mirouze%202016%20-%20Multiple%20length-scale%20covariance.md)

## Objective

Define a joint additive kernel or Whittle–Matérn covariance using exactly the scales available to the successive estimator.

## Procedure

1. Copy the scale set, amplitudes, observation model, and constraints from D004.
2. Define every component covariance (B(L_p)).
3. Define mixture weights and constraints required for positive semidefiniteness.
4. Write the single joint objective and posterior equations.
5. Define tuning search space, validation objective, and budget accounting.
6. Count learned, fixed, and implicit degrees of freedom separately.
7. Specify how to handle a component that becomes numerically redundant.

## Required checks

- Numerically check covariance symmetry and nonnegative eigenvalues over representative configurations.
- Confirm the comparator receives no scale or tuning information unavailable to D033.

## Machine verification

`pixi run verify-card -- D012` must compile PSD-mixture conditions, validate the comparator schema, and pass information-budget checks.

## Primary artifact

`spec/joint-comparator.md` with covariance, constraints on weights, tuning budget, and parameter count.

## Acceptance

- The covariance is positive semidefinite under stated conditions.
- Scale, variance, and tuning information are matched.
- Joint and successive resource accounting is explicit.

## Failure or escalation

If an exact joint DIVAnd implementation is unavailable, specify the closest mathematically equivalent reference implementation and record the gap.
