# Investigation 04: Spectral-kernel investigation

## Delivery cards

[D020](../../plan/deliverables/D020-spectral-derivation.md), [D021](../../plan/deliverables/D021-stage-scale-diagnostic.md), and [D048](../../plan/deliverables/D048-order-ablations.md)

## Goal

Define the spectral kernel precisely and determine whether succession corresponds to adding frequency bands, mixture components, random features, or basis functions.

## Mandatory sources

- [[01 Concepts/Spectral kernels and infinite parameters]]
- [[02 Papers/Wilson Adams 2013 - Spectral mixture kernels]]
- Rahimi and Recht, and Lázaro-Gredilla et al. in [[06 Sources/Bibliography]]
- [[03 Code/GPyTorch spectral mixtures]]
- [[01 Concepts/Variational analysis and precision operators]]
- [[02 Papers/Barth 2014 - DIVAnd]]

## Tasks

1. Apply Bochner's theorem if stationarity holds.
2. Write the spectral measure for every kernel under consideration.
3. Count learned parameters separately from implicit feature dimension.
4. Determine whether level components have disjoint, overlapping, or adaptive spectral support.
5. Compare stagewise component fitting with joint maximum likelihood or least squares.
6. Test rotated and nonseparable anisotropy in \(d>1\).
7. Analyze identifiability and label switching.
8. Derive and plot the DIVAnd/Whittle-Matérn-type spectrum ((1+|Lk|^2)^{-m}) as a non-mixture baseline.
9. Compare a stagewise length-scale schedule with one joint multiple-length-scale covariance.

## Deliverables

- Spectral equations and parameter-count table.
- Plots of learned spectral densities by level.
- Verdict on the "infinite free parameters" claim.
- Minimal spectral baseline implementation.

## Stop condition

Stop when every degree of freedom has an explicit finite parameter, coefficient, random variable, or measure-theoretic role.
