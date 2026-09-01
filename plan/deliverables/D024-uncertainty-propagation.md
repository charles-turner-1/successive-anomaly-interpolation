# D024 — Specify uncertainty propagation

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D004, D010
- **Hypotheses:** H6
- **Verification classes:** V1, V2

## Objective

Define how posterior or approximation uncertainty changes when corrections are fitted and frozen successively.

## Procedure

1. State whether each stage is Bayesian conditioning, a MAP update, or a deterministic fit.
2. Derive the one-stage mean and covariance.
3. Derive cross-level covariance when later residuals depend on earlier fitted stages.
4. Identify any independence approximation and the error it can create.
5. Define observation, latent-field, and predictive uncertainty separately.
6. Specify computable exact and approximate algorithms.
7. Construct a scalar Gaussian example with an analytic posterior.

## Required checks

- Recover the analytic scalar and one-stage cases.
- Verify covariance symmetry and nonnegative eigenvalues within numerical tolerance.

## Machine verification

`pixi run verify-card -- D024` must compile the formal finite Gaussian identities selected for proof and pass analytic posterior and PSD tests.

## Primary artifact

`theory/uncertainty-propagation.md` with covariance recurrence or a documented approximation.

## Acceptance

- Cross-level covariance is included or explicitly approximated.
- The method reduces to standard posterior covariance for the one-stage case.
- Calibration targets for D045 are computable.

## Failure or escalation

If justified uncertainty cannot be produced, remove probabilistic claims and retain point estimates only.
