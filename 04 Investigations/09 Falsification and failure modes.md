# Investigation 09: Falsification and failure modes

## Goal

Design cases that expose whether the method's scale interpretation, stability, and claimed advantage are real.

## Adversarial cases

- Pure white noise.
- A single smooth scale with no fine detail.
- Two close frequencies that fall inside one nominal band.
- A rotated anisotropic ridge.
- Clustered samples plus a large unsampled hole.
- Duplicate or nearly duplicate sites.
- Discontinuity or cusp.
- Heteroscedastic noise.
- Outliers at a fine scale.
- Function outside the chosen kernel native space.
- High ambient dimension with one active coordinate.
- High intrinsic dimension with equal activity across coordinates.

## Required diagnostics

- Training versus held-out residual by level.
- Operator condition numbers.
- Growth of coefficient and RKHS norms.
- Cancellation between levels.
- Actual Fourier energy of nominally coarse and fine corrections.
- Sensitivity to sample order, coordinate rotation, and scale units.

## Deliverables

- Smallest counterexample for each failed claim.
- Safe operating envelope.
- Default stopping and regularization rules.
- Claims that remain valid after adversarial testing.

