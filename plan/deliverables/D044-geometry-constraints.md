# D044 — Test geometry and physical constraints

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D041
- **Hypotheses:** H8
- **Verification classes:** V2, V3

## Objective

Test masks, disconnected regions, periodicity, anisotropy, and advection only where each has known ground truth.

## Procedure

1. Generate a separate frozen fixture for each constraint with an analytic or high-resolution truth.
2. Define constraint-specific primary metrics before running models.
3. Fit constrained and unconstrained estimators with matched validation and resource budgets.
4. Evaluate cross-barrier leakage, seam error, anisotropic orientation error, and physical residual separately.
5. Evaluate ordinary RMSE inside each connected region.
6. Run H8 decision code per constraint and for the declared aggregate rule.
7. Store fields and masks needed to reproduce every metric.

## Required checks

- Rotate/reflect fixtures where symmetry predicts invariant results.
- Verify masks truly disconnect the discrete operator graph.

## Machine verification

`pixi run verify-card -- D044` must regenerate fixtures, validate graph topology, recompute metrics, and emit H8 verdicts.

## Primary artifact

`reports/geometry-constraints.md` with leakage and physical-consistency metrics.

## Acceptance

- Constrained and unconstrained models receive matched tuning budgets.
- Split-basin and advected-ridge cases quantify the H8 thresholds.
- Accuracy within valid connected regions is reported separately.

## Failure or escalation

Failure keeps constraints optional; it does not get hidden inside aggregate RMSE.
