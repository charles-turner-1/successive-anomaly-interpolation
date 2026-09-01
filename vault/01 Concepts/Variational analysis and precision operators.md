# Variational analysis and precision operators

## Why DIVAnd matters here

DIVAnd supplies an unusually direct bridge among four descriptions of the same reconstruction problem:

1. penalized interpolation on a grid;
2. optimal interpolation or kriging with a prescribed background covariance;
3. a Bayesian Gaussian inverse problem;
4. a spectral low-pass kernel whose inverse is a differential operator.

This is more than a neighboring application. It provides a concrete interpretation of an **anomaly** as an observation minus a background or first-guess field.

## Variational form

Let (x) be the gridded anomaly field, (y) the observed anomalies, (H) the observation operator, (R) the observation-error covariance, and (B) the background covariance. A standard quadratic analysis solves

\[
\widehat x=
\operatorname*{argmin}_x
\left[
x^\top B^{-1}x+(Hx-y)^\top R^{-1}(Hx-y)
\right].
\]

The normal equations are

\[
(B^{-1}+H^\top R^{-1}H)\widehat x=H^\top R^{-1}y.
\]

Thus (B^{-1}) is a **precision operator**: it penalizes implausible or overly rough fields. In DIVAnd it is built from a weighted sum of squared derivatives on a curvilinear grid, with masks and boundary conditions incorporated into the discrete operators.

The posterior or analysis covariance is

\[
P=(B^{-1}+H^\top R^{-1}H)^{-1}.
\]

DIVAnd can estimate its diagonal, although exact diagonal extraction is expensive for large systems.

## Fourier form

For a translation-invariant idealization with a dimensionless derivative ~∇ scaled by a correlation length, the variational inner product has the form

\[
\langle f,g\rangle_B
\propto
\int
\sum_{j=0}^{m}\alpha_j
(\widetilde\nabla^j f)(\widetilde\nabla^j g)\,dx.
\]

The corresponding reproducing kernel is the Green's function of an elliptic operator. In Fourier space,

\[
\widehat K(k)
\propto
\frac{1}{\alpha_0+\alpha_1|k|^2+\cdots+\alpha_m|k|^{2m}}.
\]

With the binomial coefficients used in the DIVAnd construction,

\[
\alpha_j={m\choose j},
\qquad
\widehat K(k)\propto (1+|k|^2)^{-m}.
\]

This is a Bessel-potential or Whittle-Matérn-type spectrum. The correlation length rescales (k); the derivative order controls high-frequency decay and field smoothness. Normalization fixes (K(0)=1), and integrability requires sufficiently large (m) relative to dimension. DIVAnd chooses the derivative order accordingly.

This gives a precise answer to part of the spectral-kernel question: the continuum of Fourier modes need not be represented by an independently learned parameter at every frequency. A short differential operator specifies the whole spectrum.

## Successive background-anomaly analysis

A DIVAnd-compatible succession can be written

\[
b_0=\text{first guess},
\qquad
a_\ell=y-Hb_{\ell-1},
\]

\[
g_\ell=A(L_\ell,R_\ell,C_\ell)a_\ell,
\qquad
b_\ell=b_{\ell-1}+g_\ell,
\]

where (L_\ell) is a correlation-length field, (R_\ell) an error model, and (C_\ell) any physical or geometric constraints.

At the observation sites the residual evolves as

\[
a_{\ell+1}=(I-HA_\ell)a_\ell.
\]

For fixed (A), repeated passes form a polynomial iterative filter. They are generally **not** equivalent to the original single quadratic optimum. They may progressively reduce data misfit while weakening the effective prior, eventually fitting noise. A meaningful multiscale method therefore needs a justified schedule for (L_\ell), (R_\ell), constraints, damping, or stopping.

## What DIVAnd adds to the research program

- a mature baseline for scattered observations in arbitrary dimension;
- explicit background-anomaly semantics;
- a closed Fourier-to-variational correspondence;
- nonuniform and anisotropic length scales;
- masks that prevent interpolation across topological barriers;
- periodic dimensions and curvilinear metrics;
- quadratic, inequality, advection, and derivative constraints;
- primal/grid-space and dual/observation-space solvers;
- approximate posterior error maps;
- cross-validation and parameter-estimation machinery;
- domain decomposition for large analyses.

[[02 Papers/Mirouze 2016 - Multiple length-scale covariance]] supplies a particularly important control: several Whittle-Matérn length scales can be mixed inside one covariance operator and estimated jointly. Any benefit claimed for succession must survive that comparison.

## Important distinction from nested-space methods

Changing (L_\ell) changes a covariance or precision operator, but does not by itself create nested approximation spaces. DIVAnd normally reconstructs in the same gridded state space at every length scale. Its natural mathematical language is a sequence of regularized inverse problems or spectral filters, not automatically an MRA filtration.

## Links

- [[02 Papers/Barth 2014 - DIVAnd]]
- [[03 Code/DIVAnd]]
- [[04 Investigations/11 DIVAnd equivalence and successive anomalies]]
- [[01 Concepts/Spectral kernels and infinite parameters]]
- [[01 Concepts/Residual correction]]
