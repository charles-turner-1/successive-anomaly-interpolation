# D045 — Test uncertainty calibration

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D024, D041
- **Hypotheses:** H6
- **Verification classes:** V2, V3

## Objective

Measure coverage and predictive density under homogeneous, heterogeneous, and correlated observation noise.

## Procedure

1. Generate latent truth and observation noise using independent RNG streams.
2. Freeze homoscedastic, heteroscedastic, and correlated regimes plus replicate count.
3. Fit every uncertainty-producing estimator without truth access.
4. Compute interval coverage, width, standardized residuals, calibration curves, and NLPD.
5. Stratify by sampling density, noise regime, and stage.
6. Compare with analytic small Gaussian cases and tuned GP/variational baselines.
7. Run the frozen H6 decision program.

## Required checks

- Test metric implementations on simulated perfectly calibrated and deliberately miscalibrated predictors.
- Verify covariance matrices and interval quantiles are finite and valid.

## Machine verification

`pixi run verify-card -- D045` must reproduce calibration metrics and emit the H6 verdict from immutable simulation bundles.

## Primary artifact

`reports/uncertainty-calibration.md` with reliability curves, coverage, interval width, and NLPD.

## Acceptance

- Truth is generated independently from fitting code.
- Coverage is stratified by noise and sampling regime.
- H6 is decided using frozen tolerances.

## Failure or escalation

Failed calibration removes probabilistic claims unless a revised method is tested on untouched simulations.
