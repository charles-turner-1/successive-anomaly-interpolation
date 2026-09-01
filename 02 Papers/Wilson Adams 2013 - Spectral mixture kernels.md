# Wilson and Adams 2013: Gaussian process kernels for pattern discovery and extrapolation

**Citation:** Andrew Gordon Wilson and Ryan Prescott Adams. ICML 2013, PMLR 28(3), 1067-1075. [Paper and PDF](https://proceedings.mlr.press/v28/wilson13.html).

## Why it matters

The paper derives stationary kernels by modeling their spectral density as a Gaussian mixture. It connects Fourier-domain structure, flexible covariance learning, interpolation, and extrapolation in a finite analytic kernel family.

## Multidimensional form

Each spectral component has a mean frequency and spectral covariance or axiswise variance. This makes it a useful baseline for a multidimensional spectral-kernel claim.

## Relation to succession

A stage could add one spectral mixture component fitted to the current residual. That would create a spectral matching-pursuit or boosting interpretation. It would not be classical MRA unless component supports and spaces obey stronger structure.

## Risks

- Mixture components can be weakly identifiable.
- Marginal likelihood has local optima.
- A large mixture can fit noise.
- Product or diagonal spectral covariances can miss rotated anisotropy.

## Code

See [[03 Code/GPyTorch spectral mixtures]].

