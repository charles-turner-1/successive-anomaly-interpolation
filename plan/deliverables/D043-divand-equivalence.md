# D043 — Run the DIVAnd equivalence experiment

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D011, D032–D034, D041
- **Hypotheses:** H4, H5
- **Verification classes:** V1, V2, V3

## Objective

Determine whether succession adds anything beyond one tuned variational solve or one joint multiple-length-scale covariance.

## Procedure

1. Instantiate analytic finite-matrix cases from D011 and verify them before using DIVAnd.
2. Run fixed-length repeated passes across a frozen regularization grid.
3. Fit one-pass DIVAnd models along the matched regularization path.
4. Run changing-length succession and the D034 joint covariance with identical component scales.
5. Match tuning data, solver tolerances, and resource accounting.
6. Compare prediction norms, observation filters, spectra, held-out error, calibration, and order sensitivity.
7. Run frozen H4 and H5 decision programs.
8. Generate the required project-framing change automatically from the verdict pair.

## Required checks

- Compare Julia outputs with small direct Python matrix calculations.
- Repeat estimator-equivalent solver choices to isolate numerical error.
- Verify result differences exceed solver tolerance before calling them estimator differences.

## Machine verification

`pixi run verify-card -- D043` must compile relevant Lean identities, pass cross-language golden tests, and emit H4/H5 verdicts.

## Primary artifact

`reports/divand-equivalence.md` with prediction differences, regularization paths, spectra, validation error, and calibration.

## Acceptance

- Fixed-operator theory is checked numerically.
- Single, joint, and successive models use matched scales and tuning information.
- H4 and H5 receive explicit verdicts and project consequences.

## Failure or escalation

If either hypothesis fails, update the project framing before running optional branches.
