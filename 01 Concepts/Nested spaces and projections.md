# Nested spaces and projections

## Filtration

A nested approximation hierarchy is

\[
V_0\subset V_1\subset\cdots\subset V_L\subset H,
\]

where \(H\) is a Hilbert or Banach function space. Each finer space can express every function in the coarser space plus additional detail.

For orthogonal projections \(P_\ell:H\to V_\ell\), define

\[
Q_0=P_0, \qquad Q_\ell=P_\ell-P_{\ell-1}.
\]

Then

\[
P_Lf=\sum_{\ell=0}^{L}Q_\ell f.
\]

In an orthogonal multiresolution analysis, the detail space \(W_\ell\) satisfies \(V_{\ell+1}=V_\ell\oplus W_\ell\).

## Tests for the proposed algorithm

### Range inclusion

Find \(V_\ell=\operatorname{range}(A_\ell)\). Test whether \(V_\ell\subseteq V_{\ell+1}\). Changing the bandwidth of a kernel does not automatically produce nested finite-dimensional spaces.

### Idempotence

A projection satisfies \(P_\ell^2=P_\ell\). A regularized smoother usually does not.

### Compatibility

Nested orthogonal projections satisfy \(P_jP_k=P_{\min(j,k)}\). Failure means the levels are not a classical projection filtration.

### Orthogonality or frame stability

If orthogonality fails, look for stable frame bounds or a uniformly bounded decomposition. A useful nonorthogonal method does not need to be forced into wavelet language.

### Approximation and density

For a full MRA, the union of spaces should be dense in the target space and the intersection should contain only the limiting coarse content, often zero under the classical convention.

## Kernel-specific complication

For centers \(X_\ell\) and kernel \(k_\ell\), a finite interpolation space is

\[
V_\ell=\operatorname{span}\{k_\ell(\cdot,x):x\in X_\ell\}.
\]

Nested centers alone imply nested spaces only when the kernel is fixed. Changing the kernel scale changes the generators and can break inclusion. One research route is to construct kernels or refinement relations that restore exact or approximate nesting.

## Precision-operator complication

In DIVAnd-like analyses, changing the correlation length or derivative penalty usually changes the norm, prior covariance, and smoother while leaving the discrete state space fixed. The operator ranges may therefore all be the full grid space even though their effective spectral passbands differ. This is a scale sequence, but not a nontrivial nested-space filtration. Analyze eigenvalue response and effective rank before applying MRA terminology.

## Relevant sources

- [[02 Papers/Mallat 1989 - Multiresolution analysis]]
- [[02 Papers/Coifman Maggioni 2006 - Diffusion wavelets]]
- [[02 Papers/Narcowich Schaback Ward 1999 - Multilevel interpolation]]
- [[01 Concepts/Variational analysis and precision operators]]
