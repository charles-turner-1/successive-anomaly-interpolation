# Working definition and assumptions

## Supplied context

The shared conversation described a multidimensional spectral-kernel method with effectively infinitely many free parameters and a process called successive anomaly interpolation. It proposed possible links to renormalization, multiresolution analysis, wavelets, Laplacian pyramids, and a filtration of nested spaces.

No explicit recurrence, objective function, kernel, data model, or definition of "anomaly" was supplied. DIVAnd makes one candidate substantially more concrete: an anomaly may be an observation after subtracting a background or first-guess field. The notation below remains a neutral placeholder until that match is confirmed.

## Minimal mathematical skeleton

Let observations be

\[
\mathcal D = \{(x_i,y_i)\}_{i=1}^n, \qquad x_i \in \Omega \subseteq \mathbb R^d,
\]

with scalar or vector values \(y_i\). Let \(S_X f=(f(x_1),\ldots,f(x_n))\) be the sampling operator.

Initialize

\[
f_{-1}=0, \qquad r_0=y.
\]

At level \(\ell\), choose a scale-dependent fitting operator \(A_\ell\) and compute

\[
g_\ell=A_\ell r_\ell,
\]

then update

\[
f_\ell=f_{\ell-1}+\eta_\ell g_\ell,
\qquad
r_{\ell+1}=y-S_X f_\ell.
\]

Here \(A_\ell\) may be a kernel interpolator, regularized smoother, local solver, low-rank spectral model, spline fit, learned interpolation block, or projection into a space \(W_\ell\).

## The redundancy test

If \(A_0\) is an exact interpolator on all observation sites and \(\eta_0=1\), then

\[
S_X A_0 y=y,
\]

so \(r_1=0\). Further stages do nothing.

Successive interpolation therefore needs at least one restriction:

- each level is approximate or regularized;
- each level sees only a subset of sites;
- each level has limited resolution, rank, support, or frequency content;
- each level is local and cannot remove the global residual;
- damping uses \(\eta_\ell<1\);
- the residual is measured somewhere other than the fitted sites;
- "anomaly" is not the ordinary interpolation residual.

This is the first issue every investigation must check.

## Three candidate meanings of anomaly

### Residual anomaly

\(a_\ell(x_i)=y_i-f_{\ell-1}(x_i)\). This makes the method a standard residual-correction scheme.

### Statistical anomaly

\(a_\ell\) is a standardized residual, posterior surprise, local outlier score, or deviation from an estimated covariance model. This changes the method from interpolation into adaptive robust fitting.

### Physical anomaly field

"Anomaly" may be domain terminology, such as gravity, magnetic, temperature, or geophysical anomaly data. Then the word describes the measured quantity, not an algorithmic residual.

### Background or first-guess anomaly

Following variational data analysis, let (b_{\ell-1}) be the current background and define

\[
a_\ell=y-Hb_{\ell-1}.
\]

Analyze (a_\ell) with a covariance- or precision-defined operator and add the result back to the background. This resembles residual correction algebraically, but it carries an observation-error model, prior covariance, physical constraints, and posterior uncertainty. See [[01 Concepts/Variational analysis and precision operators]].

## Candidate scale schedules

- Kernel length scale: \(\sigma_{\ell+1}=\rho\sigma_\ell\), with \(0<\rho<1\).
- Frequency cutoff: \(\Lambda_{\ell+1}=\rho^{-1}\Lambda_\ell\).
- Grid spacing or fill distance: \(h_{\ell+1}=\rho h_\ell\).
- Neighborhood radius: \(R_{\ell+1}=\rho R_\ell\).
- Rank or feature count: \(m_{\ell+1}>m_\ell\).
- Nested centers: \(X_0\subset X_1\subset\cdots\subset X_L\).

## Information still needed

1. What exactly is an anomaly?
2. What is the base interpolation or correlation operator?
3. What changes from one succession to the next?
4. Are observations scattered, gridded, periodic, noisy, or incomplete?
5. Is the target an exact interpolant, a smoother, a predictor with uncertainty, or a physical field reconstruction?

## Links

- [[01 Concepts/Residual correction]]
- [[01 Concepts/Nested spaces and projections]]
- [[01 Concepts/Spectral kernels and infinite parameters]]
- [[01 Concepts/Variational analysis and precision operators]]
- [[04 Investigations/11 DIVAnd equivalence and successive anomalies]]
- [[05 Experiments/Minimum reference algorithm]]
