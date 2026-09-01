# Residual correction

## Common recurrence

Many apparently different methods share

\[
f_L=\sum_{\ell=0}^{L}g_\ell,
\qquad
g_\ell=A_\ell\left(y-S_Xf_{\ell-1}\right).
\]

The substance lies in the operator sequence \(A_\ell\). Calling the summands "anomalies" does not create a new method unless their construction differs from established residual fits.

## Closest families

### Multilevel B-splines

Lee, Wolberg, and Shin use a coarse control lattice for the global shape, then successively finer lattices to approximate and remove residual error. See [[02 Papers/Lee 1997 - Multilevel B-splines]]. This is the closest classical algorithmic match found so far.

### Multiscale RBF and kernel interpolation

Compactly supported RBF schemes change the support radius and data resolution by level. Some have convergence and condition-number results. See [[02 Papers/Narcowich Schaback Ward 1999 - Multilevel interpolation]], [[02 Papers/Wendland 2010 - Multiscale RBF approximation]], and [[02 Papers/Georgoulis 2013 - Multilevel sparse kernel interpolation]].

### Hierarchical neural interpolation

HINT uses an initial interpolation block for the main component and later blocks to predict residual components from residuals observed at known points. See [[02 Papers/Ding 2023 - HINT]]. This is very close at the architecture level, though it is learned rather than derived from a fixed spectral kernel.

### Matching pursuit and boosting

Matching pursuit selects one dictionary atom at a time to reduce signal residual energy. Gradient boosting fits a new learner to a functional gradient or residual. These methods prove that stagewise residual reduction is a broad optimization pattern, not by itself a multiresolution construction.

### Multigrid

Multigrid alternates fine-scale relaxation with coarse-grid correction. It is relevant because error components are separated by scale, but its order and purpose differ from a pure coarse-to-fine interpolant.

### Variational background-anomaly correction

DIVAnd analyzes observations after subtracting a background field. Reusing the updated analysis as the next background produces the same residual recurrence, but each stage is a regularized inverse problem with an explicit covariance and observation-error model. For a fixed linear analysis operator (A),

\[
r_{\ell+1}=(I-S_XA)r_\ell.
\]

The sequence is then an iterative spectral filter, not automatically a multiresolution decomposition. See [[01 Concepts/Variational analysis and precision operators]].

## Properties to measure

- Training residual norm by level.
- Held-out error by level.
- Frequency or scale distribution of each \(g_\ell\).
- Correlation between different levels.
- Native-space or RKHS norm of each level.
- Condition number and numerical rank of each level solve.
- Noise amplification after the validation error stops improving.

## Failure modes

- Later stages fit measurement noise.
- Corrections cancel earlier levels, destroying interpretability.
- Scale labels do not match actual Fourier content.
- A non-nested operator sequence produces unstable oblique corrections.
- Exact interpolation creates large excursions between sites.
- High-dimensional distances concentrate, making radial length scales ineffective.
- Repeated variational passes reduce data misfit by silently eroding the effective prior.
