# Minimum reference algorithm

## Purpose

This prototype tests the residual-correction idea without neural training or RG language.

## Data

Use scattered observations \((X,y)\), a validation subset, and target points \(X_*\). Standardize coordinates per dimension and preserve the transform.

## Algorithm

Choose scales \(\sigma_0>\sigma_1>\cdots>\sigma_L\). Initialize \(f=0\) and \(r=y\).

For each level \(\ell\):

1. Fit a deliberately restricted model \(g_\ell\) to \((X,r)\). Start with kernel ridge regression using a Gaussian kernel of width \(\sigma_\ell\) and fixed regularization \(\lambda_\ell>0\).
2. Choose damping \(\eta_\ell\) using validation data or a closed-form line search.
3. Update \(f\leftarrow f+\eta_\ell g_\ell\).
4. Update \(r\leftarrow y-f(X)\).
5. Store the level model, training residual, validation error, coefficient norm, and evaluated spectrum on a diagnostic grid.
6. Stop when validation error fails to improve, the correction norm is too small, or conditioning exceeds a threshold.

## Baselines

- One-stage kernel ridge model with every candidate scale.
- Joint additive multiscale kernel \(k=\sum_\ell k_\ell\).
- Same additive kernel with all coefficients fit jointly.
- SciPy RBF interpolation or smoothing.
- Spectral mixture GP.
- VKOGA with the same basis budget.
- Wavelet reconstruction when data lie on a grid.
- One cross-validated DIVAnd analysis of observation-minus-background anomalies.
- Successive DIVAnd analyses with the same total solver and hyperparameter budget.
- A joint multiple-length-scale covariance or additive-kernel approximation.

## Key ablations

- Freeze previous levels versus backfit them.
- Fixed versus learned scale schedule.
- Disjoint spectral bands versus overlapping Gaussian kernels.
- Exact interpolation versus regularization.
- Isotropic versus anisotropic scales.
- All centers versus nested center subsets.
- Zero background versus a supplied first guess.
- Single variational optimum versus repeatedly updated background anomalies.
- Fixed versus decreasing correlation lengths.
- Free Euclidean interpolation versus masks, periodicity, and physical constraints.

## Success criterion

The successive method should beat a jointly tuned one-stage or additive baseline in a measurable dimension such as computation, conditioning, sample efficiency, uncertainty calibration, adaptivity, or interpretability. Lower training error alone is not enough.
