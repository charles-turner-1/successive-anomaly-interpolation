# SciPy and RBF libraries

## SciPy RBFInterpolator

[Source](https://github.com/scipy/scipy/blob/main/scipy/interpolate/_rbfinterp.py) supports scattered interpolation in \(N\) dimensions, smoothing, local-neighbor restriction, and several kernels.

Use it for conventional one-stage baselines and a minimal multistage wrapper. Gaussian and inverse multiquadric kernels require a shape parameter; compact polyharmonic choices provide useful scale-free contrasts.

## treverhines/RBF

[Repository](https://github.com/treverhines/RBF) includes RBF evaluation, exact derivatives, noisy scattered interpolation, RBF-FD, node generation, and Gaussian-process tools.

Use it when experiments need derivatives, irregular boundaries, or PDE-flavored benchmarks.

## Implementation warning

A wrapper that repeatedly applies an exact global RBF interpolator to the same data will terminate after the first level. Each stage must deliberately restrict bandwidth, neighborhood, centers, rank, smoothing, or sites.

