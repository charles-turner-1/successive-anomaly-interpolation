# Benchmark matrix

| Benchmark | Purpose | Sampling | Noise | Main metric |
|---|---|---|---|---|
| Sum of dyadic sinusoids | Known separated Fourier scales | Random 1D | None and Gaussian | Band recovery and RMSE |
| Chirp plus trend | Nonstationary frequency | Random 1D | Gaussian | Local spectral recovery |
| Franke function | Standard scattered interpolation | Random and clustered 2D | None | RMSE and max error |
| Multiscale Gaussian bumps | Localized scale components | Random 2D | Gaussian | Per-level localization |
| Rotated ridge | Anisotropy test | Random 2D and 8D | None | Rotation sensitivity |
| Perlin field | HINT-adjacent synthetic field | Random 2D | Optional | RMSE and spectrum |
| Sphere or Swiss roll field | Irregular geometry | Surface samples | None | Geodesic versus Euclidean error |
| Sobol G-function | High-dimensional effective dimension | Quasi-random | None | RMSE versus \(d\) |
| Heteroscedastic field | Uncertainty test | Random 2D | Spatially varying | Log predictive density |
| Step plus smooth background | Smoothness violation | Random 1D and 2D | None | Overshoot and edge error |
| Split-basin field | Topological barrier leakage | Clustered 2D on both sides of a mask | Gaussian | Cross-barrier contamination |
| Advected anisotropic ridge | Physical-constraint test | Sparse 2D or 3D | Gaussian | Along-flow recovery and cross-flow leakage |
| Background plus anomalies | First-guess assimilation test | Scattered nD | Heteroscedastic | Increment accuracy and uncertainty calibration |
| Space-time periodic field | Joint-dimensional test | Sparse 3D or 4D | Gaussian | Temporal continuity and phase error |

## Sampling regimes

Every low-dimensional function should use uniform, clustered, hole-containing, and boundary-poor site sets. Report interpolation inside the convex hull separately from extrapolation.

## Budgets

Compare methods at matched wall time, memory, number of centers or features, and total learned scalar parameters. A hierarchy with \(L\) separate fits must not be compared against a one-stage model with a fraction of its budget.

## Metrics

- RMSE, MAE, and maximum error.
- Negative log predictive density when available.
- Runtime and peak memory.
- Condition number or solver iterations.
- Residual norm and validation error by level.
- Spectral leakage between intended levels.
- Reconstruction stability under perturbation of observations.
