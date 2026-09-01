# D023 — Derive stability and stopping conditions

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D004, D011
- **Hypotheses:** H7
- **Verification classes:** V1, V2

## Objective

Bound perturbation amplification and define a stopping rule before validation or coefficient norms deteriorate.

## Procedure

1. Derive the linear perturbation map from observations to every stage and final output.
2. Bound it using eigenvalues, singular values, or operator norms under stated assumptions.
3. Identify observable warning signals: conditioning, norm growth, cancellation, validation reversal, and solver stagnation.
4. Define thresholds and precedence for stopping.
5. Implement the rule without test-data access.
6. Generate stable, marginal, and unstable fixtures.
7. Compare predicted warnings with measured perturbation amplification.

## Required checks

- Exercise every stopping branch in tests.
- Verify the H7 perturbation calculation on at least three input scales and solver tolerances.

## Machine verification

`pixi run verify-card -- D023` must compile stated bounds, exercise every stopping branch, and assert measured amplification against the declared thresholds.

## Primary artifact

`theory/stability-and-stopping.md` plus executable stopping-rule tests.

## Acceptance

- Fixed-linear conditions are derived spectrally.
- Adaptive cases state measurable sufficient diagnostics.
- The rule uses no test data and implements the H7 tolerances.

## Failure or escalation

If no useful bound exists, constrain damping/regularization or narrow the operating regime.
