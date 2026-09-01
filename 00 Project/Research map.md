# Research map

## Central question

Can successive anomaly interpolation be expressed as a stable multilevel approximation method in which each stage fits the residual left by the preceding stage, with the stagewise hypothesis spaces organized by scale?

The answer breaks into four progressively stronger claims:

1. **Additive residual form.** The algorithm can be written as a sum of stagewise corrections.
2. **Scale organization.** Each correction targets a controlled band, length scale, resolution, or locality range.
3. **Nested-space form.** The stage spaces form a filtration, such as \(V_0 \subset V_1 \subset \cdots\).
4. **Projection or frame form.** Corrections are projections, stable quasi-projections, or frame coefficients with a reconstruction theorem.

Claim 1 is easy to satisfy. Claims 3 and 4 are mathematically restrictive and must be proved rather than inferred from coarse-to-fine behavior.

## Main routes

### Route A: direct prior art

Start here. [[01 Concepts/Residual correction]] connects the proposed recurrence to multilevel B-splines, compactly supported RBFs, sparse kernel interpolation, matching pursuit, boosting, and HINT.

Key notes:

- [[02 Papers/Lee 1997 - Multilevel B-splines]]
- [[02 Papers/Narcowich Schaback Ward 1999 - Multilevel interpolation]]
- [[02 Papers/Wendland 2010 - Multiscale RBF approximation]]
- [[02 Papers/Ding 2023 - HINT]]

### Route B: nested spaces and multiresolution

[[01 Concepts/Nested spaces and projections]] states the tests needed to decide whether the method is an MRA-like decomposition. [[02 Papers/Mallat 1989 - Multiresolution analysis]] is the canonical source. [[02 Papers/Coifman Maggioni 2006 - Diffusion wavelets]] extends the idea to graphs, manifolds, and irregular data clouds.

### Route C: Fourier and spectral kernels

[[01 Concepts/Spectral kernels and infinite parameters]] separates three ideas that are easy to conflate:

- a kernel as an integral over infinitely many Fourier features;
- a finite kernel expansion over data sites;
- a finite approximation to the spectral measure.

The main sources are [[02 Papers/Wilson Adams 2013 - Spectral mixture kernels]] and Rahimi and Recht in [[06 Sources/Bibliography]].

### Route D: renormalization

[[01 Concepts/Renormalization comparison]] treats renormalization as a hypothesis to test. RG typically removes fine degrees of freedom and studies the flow of an effective model toward coarse scales. Residual interpolation usually reconstructs from coarse to fine. The relationship may be dual, adjoint, or merely architectural.

The strongest modern bridge is [[02 Papers/Marchand 2023 - Wavelet conditional RG]], which explicitly combines conditional coarse-to-fine modeling, wavelets, and RG.

### Route E: variational analysis and data assimilation

[[01 Concepts/Variational analysis and precision operators]] is now a central route. [[02 Papers/Barth 2014 - DIVAnd]] defines a covariance kernel through a weighted differential penalty, reconstructs scattered noisy anomalies on an arbitrary-dimensional curvilinear grid, respects barriers and periodicity, and supplies analysis-error estimates.

This route creates the sharpest baseline question so far: does a succession of anomaly analyses produce anything that one correctly specified global variational solve does not? [[04 Investigations/11 DIVAnd equivalence and successive anomalies]] is designed to answer it.

## Decision tree

1. Write the actual algorithm using the schema in [[00 Project/Working definition and assumptions]].
2. If every stage uses the same unrestricted exact interpolator, succession is redundant. Investigate why it is not exact or unrestricted.
3. Identify what changes by stage: kernel bandwidth, centers, data subset, regularization, frequency band, grid, rank, or neighborhood.
4. Compute or characterize each stage operator's range.
5. Test range inclusion, idempotence, commutation, stability, and reconstruction.
6. Compare against the baselines in [[05 Experiments/Benchmark matrix]].
7. Compare the recurrence with one DIVAnd optimum and with a joint multiscale covariance.
8. Use [[04 Investigations/Investigation index]] to parallelize literature, proof, and code work.

## Likely contribution zones

The generic idea of fitting residuals at successive scales is established. A defensible new contribution would need to live in one or more of these narrower zones:

- a new rule for choosing scale, bandwidth, or support from the anomaly field;
- a multidimensional spectral kernel whose stagewise residuals have a provable band interpretation;
- a stable nested or approximately nested RKHS construction;
- an adaptive stopping rule that separates signal from noise;
- better accuracy or complexity in high dimensions;
- uncertainty propagation across residual levels, benchmarked against variational posterior error maps;
- a reverse-RG interpretation with an exact operator correspondence;
- a method that works on irregular domains or non-Euclidean data without a fixed grid.

## Immediate next action

Follow [[00 Project/Next steps]]. First pass H0 and H1 in [[00 Project/Hypothesis ledger and decision rules]], then run [[04 Investigations/11 DIVAnd equivalence and successive anomalies]]. The DIVAnd comparison can resolve several remaining design choices empirically.
