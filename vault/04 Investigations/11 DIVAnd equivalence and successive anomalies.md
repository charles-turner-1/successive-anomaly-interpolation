# Investigation 11: DIVAnd equivalence and successive anomalies

## Delivery cards

[D010](../../plan/deliverables/D010-divand-operator.md), [D011](../../plan/deliverables/D011-fixed-operator-recurrence.md), [D012](../../plan/deliverables/D012-joint-multiscale-comparator.md), [D024](../../plan/deliverables/D024-uncertainty-propagation.md), [D034](../../plan/deliverables/D034-joint-multiscale-baseline.md), [D043](../../plan/deliverables/D043-divand-equivalence.md), and [D045](../../plan/deliverables/D045-uncertainty-calibration.md)

## Goal

Determine whether successive anomaly interpolation is:

- a standard DIVAnd analysis applied to anomalies from a first guess;
- an iterative solver for a single variational objective;
- a multiscale sequence of distinct variational objectives;
- an implicit way of changing regularization;
- or a genuinely different estimator.

## Mandatory sources

- [[01 Concepts/Variational analysis and precision operators]]
- [[02 Papers/Barth 2014 - DIVAnd]]
- [[02 Papers/Mirouze 2016 - Multiple length-scale covariance]]
- [[03 Code/DIVAnd]]
- [DIVAnd documentation](https://gher-uliege.github.io/DIVAnd.jl/latest/)
- Weaver and Mirouze 2013 in [[06 Sources/Bibliography]]

## Tasks

1. Write one DIVAnd solve as a linear map (A(L,R,C)) from observed anomalies to a gridded correction.
2. Derive the observation-residual recurrence (a_{\ell+1}=(I-HA_\ell)a_\ell).
3. For fixed (A), derive the closed form after (L) passes and identify the effective spectral filter and prior.
4. Decide whether the succession is equivalent to a stationary iteration for one linear system. If so, identify its preconditioner and convergence conditions.
5. For changing correlation lengths, compare sequential fitting with the joint Whittle-Matérn mixture of [[02 Papers/Mirouze 2016 - Multiple length-scale covariance]].
6. Test whether coarse-to-fine and fine-to-coarse orders commute. Quantify the difference.
7. Determine when repeated passes overfit noisy observations.
8. Compare fixed and Desroziers- or cross-validation-based error scaling.
9. Test masks with separated basins, periodic axes, anisotropy, and an advection constraint.
10. Compare DIVAnd error maps with empirical held-out and simulated reconstruction errors at every level.

## Minimal experiments

- 1D periodic sum of separated Fourier modes.
- 2D field split by an impermeable barrier with nearby observations on both sides.
- Anisotropic advected ridge.
- 3D or 4D sparsely observed field with time as a joint dimension.
- Heteroscedastic and spatially correlated observation noise.

## Deliverables

- operator-equivalence derivation;
- Julia script using `DIVAndrun` and `DIVAnd_cv`;
- table comparing single, joint-multiscale, and successive estimates;
- spectral response by pass;
- uncertainty calibration plot;
- verdict: baseline equivalence, useful continuation method, or distinct estimator.

## Falsification conditions

Reject the successive method in its current form if a single correctly specified DIVAnd solve matches it at lower cost, or if its apparent gain is only reduced observation misfit accompanied by worse held-out error or uncertainty calibration.
