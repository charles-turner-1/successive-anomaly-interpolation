# GPyTorch spectral mixtures

## Source

- [GPyTorch repository](https://github.com/cornellius-gp/gpytorch)
- [Official spectral mixture regression example](https://docs.gpytorch.ai/en/stable/examples/01_Exact_GPs/Spectral_Mixture_GP_Regression.html)

## Why use it

`SpectralMixtureKernel` implements the Wilson and Adams kernel from [[02 Papers/Wilson Adams 2013 - Spectral mixture kernels]]. It provides a tested comparison for claims about Fourier-domain kernel learning, multidimensional inputs, and uncertainty.

## Experiments

1. Fit a single GP with \(Q\) mixture components.
2. Fit one component at a time to residuals, freezing earlier components.
3. Jointly refit all components after each addition.
4. Compare with fixed dyadic spectral bands.

Record held-out RMSE, log predictive density, component spectra, runtime, and sensitivity to initialization.

## Interpretation test

If stagewise fitting and joint \(Q\)-component fitting reach the same optimum, succession is an optimization strategy rather than a new model class. If freezing stages creates distinct generalization or scale separation, identify the regularization effect that causes it.

