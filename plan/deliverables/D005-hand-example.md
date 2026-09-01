# D005 — Hand-compute a two-level example

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D004
- **Hypotheses:** H0, H1
- **Verification classes:** V1, V2

## Objective

Evaluate the entire estimator on three observations and two levels using numbers simple enough to verify manually.

## Procedure

1. Choose rational-valued coordinates, observations, background, noise parameters, and two stage operators.
2. Write all input matrices explicitly.
3. Compute the first anomaly, first correction, updated background, and second anomaly.
4. Compute the second correction, final field, observation residual, and stopping decision.
5. Repeat using high-precision software without reusing implementation code from D033.
6. Store inputs and expected intermediate values in a machine-readable fixture.

## Required checks

- Hand and high-precision values must agree at the H0 tolerance.
- Substitute the final output back into every stated equation.

## Machine verification

`pixi run verify-card -- D005` must reproduce every stored intermediate exactly or within its declared numeric tolerance and check the formal two-stage identity.

## Primary artifact

`spec/hand-example.md` with every matrix, residual, correction, and final prediction.

## Acceptance

- Intermediate values are shown to at least eight significant digits.
- A small machine-readable fixture contains the expected values.
- At least one later-stage correction is nonzero for the stated reason.

## Failure or escalation

A zero or undefined second correction is an H1 failure, not an example to discard.
