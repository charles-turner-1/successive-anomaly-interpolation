# Spectral kernels and infinite parameters

## Three distinct infinities

### Infinite feature representation

For a stationary positive-definite kernel \(k(x-x')\), Bochner's theorem gives

\[
k(\tau)=\int_{\mathbb R^d}e^{i\omega^\top\tau}\,d\mu(\omega),
\]

where \(\mu\) is a finite nonnegative spectral measure. This is an integral over a continuum of Fourier features. It does not mean a fitted model has an unconstrained free parameter at every frequency. The measure may be fixed or described by a few hyperparameters.

### Infinite-dimensional RKHS or GP prior

A kernel can define an infinite-dimensional function space or Gaussian-process prior. Given \(n\) observations and a standard regularized empirical objective, the representer theorem often reduces the fitted mean to

\[
f(x)=\sum_{i=1}^{n}\alpha_i k(x,x_i),
\]

with finitely many coefficients.

### Nonparametric spectral density

If the spectral measure itself is learned without a fixed finite family, the model may carry an increasing number of effective degrees of freedom. This is the version most plausibly related to an "infinite number of free parameters."

## Finite approximations

- Random Fourier features sample \(m\) frequencies from \(\mu\).
- Sparse spectrum GPs optimize a finite set of frequencies.
- Spectral mixture kernels model the density as a finite Gaussian mixture.
- Grid and Toeplitz or Kronecker methods exploit structure without treating every basis weight as free.

## Multilevel spectral construction

A candidate successive scheme would partition or progressively reveal the spectrum:

\[
d\mu(\omega)=\sum_{\ell=0}^{L}d\mu_\ell(\omega),
\qquad
k=\sum_{\ell=0}^{L}k_\ell.
\]

If the supports of \(\mu_\ell\) are disjoint bands, the components have a clear scale meaning. If Gaussian bands overlap, the decomposition may still be a stable frame but is not orthogonal.

An alternative is adaptive residual fitting in frequency space, where the next spectral component is chosen from the residual periodogram or marginal likelihood. This resembles matching pursuit more than classical MRA unless the bands obey a refinement relation.

## Differential operators specify continuous spectra compactly

DIVAnd provides another finite description of an infinite feature representation. A derivative penalty with binomial coefficients has Fourier precision

\[
\widehat{B^{-1}}(k)\propto (1+|Lk|^2)^m,
\]

and therefore covariance spectrum

\[
\widehat B(k)\propto (1+|Lk|^2)^{-m}.
\]

Only the length scales, derivative order, amplitudes, metrics, and boundary model need to be specified; no independent coefficient is learned for every (k). This representation also supports spatially varying and anisotropic correlation structure after discretization, although the simple global Fourier diagonalization then no longer applies.

## Questions that decide the theory

1. Is the kernel stationary?
2. Is the spectral measure fixed, sampled, optimized, or inferred nonparametrically?
3. Are frequencies global Fourier modes or localized atoms?
4. Does each stage add a band, shrink a length scale, or refit the whole spectrum?
5. Are dimensions modeled isotropically, as products, or with a full spectral covariance?

## Sources and code

- [[02 Papers/Wilson Adams 2013 - Spectral mixture kernels]]
- [[03 Code/GPyTorch spectral mixtures]]
- [[01 Concepts/Variational analysis and precision operators]]
- [[02 Papers/Barth 2014 - DIVAnd]]
- Rahimi and Recht, and Lázaro-Gredilla et al. in [[06 Sources/Bibliography]]
