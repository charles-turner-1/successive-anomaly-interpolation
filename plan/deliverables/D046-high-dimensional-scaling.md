# D046 — Measure high-dimensional scaling

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D041
- **Hypotheses:** H10
- **Verification classes:** V2, V3

## Objective

Separate scaling in observation count, ambient dimension, and effective dimension.

## Procedure

1. Freeze geometric sequences of observation counts and dimensions within a resource ceiling.
2. Define separate low-effective- and full-effective-dimensional truth generators.
3. Warm up compilers/JITs under a declared rule and exclude or include compilation consistently.
4. Run repeated measurements in randomized method order.
5. Capture time, peak memory, iterations, failures, and accuracy.
6. Fit scaling slopes with uncertainty only over measured non-saturated regimes.
7. Run the frozen H10 noninferiority/resource decision.

## Required checks

- Calibrate measurement tooling on known sleep/allocation fixtures.
- Repeat a subset on a clean machine or isolated CI runner.
- Detect and exclude no outlier except by the frozen rule.

## Machine verification

`pixi run verify-card -- D046` must validate run coverage, fit slopes, and emit the bounded H10 verdict.

## Primary artifact

`reports/scaling.md` with time, memory, iterations, accuracy, and fitted log-log slopes.

## Acceptance

- Low-effective- and high-effective-dimensional cases are distinct.
- Every method is stopped by the same resource ceiling.
- H10 is decided for an explicitly bounded regime.

## Failure or escalation

Report the tractable domain honestly; do not extrapolate slopes past measured ranges.
