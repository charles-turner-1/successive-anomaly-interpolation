# D011 — Derive fixed-operator succession

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D004, D010
- **Hypotheses:** H1, H4
- **Verification classes:** V1, V2

## Objective

Derive the closed form of repeated residual updates for fixed (A) and identify the effective spectral filter or stationary iteration.

## Procedure

1. Define background, correction, observation residual, (A), and (M=HA).
2. Expand levels zero through three without using ellipses.
3. Prove the finite-(L) residual and accumulated-field formulas by induction.
4. Diagonalize or use Jordan/singular-value analysis under explicitly stated assumptions.
5. Derive convergence, divergence, and nullspace cases.
6. Compare the finite-stage operator with a one-pass regularization path.
7. Identify a stationary linear solver or preconditioned iteration if one is exactly equivalent.

## Required checks

- Verify formulas on random symmetric and nonsymmetric finite matrices.
- Include counterexamples for eigenvalues at zero, one, and outside the convergence region.

## Machine verification

`pixi run verify-card -- D011` must compile the finite-stage Lean proof and pass generated-matrix checks including all boundary counterexamples.

## Primary artifact

`theory/fixed-operator-recurrence.md` with proof and limiting cases.

## Acceptance

- (r_{\ell+1}=(I-HA)r_\ell) is propagated to a finite-stage closed form.
- Convergence conditions are stated in terms of the spectrum of (HA).
- The implied change in regularization is characterized.

## Failure or escalation

Nonlinearity or adaptive choices must be isolated; derive the conditional linear case rather than hiding them.
