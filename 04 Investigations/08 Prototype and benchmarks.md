# Investigation 08: Prototype and benchmarks

## Goal

Build the smallest reproducible implementation that can distinguish a useful multilevel method from repeated fitting and overfitting.

## Inputs

- [[05 Experiments/Minimum reference algorithm]]
- [[05 Experiments/Benchmark matrix]]
- [[03 Code/Code index]]

## Tasks

1. Implement fixed-scale one-stage baselines.
2. Implement a dyadic residual-correction schedule.
3. Add damping and validation-based stopping.
4. Record per-level corrections and spectra.
5. Compare against RBFInterpolator, a spectral mixture GP, multilevel B-splines if available, and VKOGA.
6. Run seeded repeats and save configuration with each result.

## Deliverables

- Installable or single-command experiment.
- Unit tests for exactness, residual update, and reproducibility.
- Result table with confidence intervals.
- One plot per diagnostic, not only final RMSE.

## Stop condition

Stop when another person can reproduce every table from a clean environment.

