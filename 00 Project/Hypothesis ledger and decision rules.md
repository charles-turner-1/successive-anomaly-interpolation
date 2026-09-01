# Hypothesis ledger and decision rules

## Purpose

This is the canonical preregistration document for the project. Every investigator should cite hypothesis IDs from this page. Results may revise a hypothesis, but the original criterion must remain visible so that a failed test cannot be relabeled as success after the fact.

The numerical thresholds below are **provisional defaults**. They may be changed once, before confirmatory runs, using only smoke-test results. The smoke-test data and seeds must then be excluded from confirmation.

## Global comparison rules

- Use identical train, validation, and test splits for paired comparisons.
- Tune every baseline with the same validation information and a declared search budget.
- Match at least two resource budgets: wall time and either peak memory, centers/features, or effective parameters.
- Report all seeds and datasets, not only the best run.
- Separate interpolation from extrapolation and in-domain holes.
- A training-residual improvement is never primary evidence.
- Report effect sizes and paired bootstrap confidence intervals, not only (p)-values.
- Any numerical failure, nonconvergence, or excluded run counts against robustness unless the same exclusion rule was preregistered for every method.

## Core hypotheses

### H0 — The method is well-defined and reproducible

**Claim.** An independent implementer can reproduce the same stage operators and predictions from the specification.

**Test.** Two implementations run the hand-computed toy case and one fixed-seed benchmark without exchanging code.

**Success.** They agree to (10^{-10}) on the toy case and (10^{-7}) relative error on the benchmark, or to a looser tolerance justified before comparison by the solver accuracy.

**Failure.** A semantic choice changes predictions, or the recurrence, anomaly, scale schedule, objective, or stopping rule remains ambiguous.

**Decision.** No performance or novelty claim proceeds until H0 passes. Owner: [[04 Investigations/01 Formal specification audit]].

### H1 — Succession is mathematically nonredundant

**Claim.** More than one stage changes the estimator for a stated reason.

**Test.** Derive (S_XA_0), the first residual, and the full finite-stage operator. Compare with an exact unrestricted first-stage interpolator.

**Success.** A declared restriction—regularization, scale, rank, locality, data subset, damping, constraints, or a different residual domain—provably leaves a nonzero admissible correction.

**Failure.** The first stage exactly annihilates the relevant residual, or later stages reproduce a one-stage estimator with no computational or statistical advantage.

**Decision.** Failure kills the proposed recurrence but may motivate a modified restricted stage. Owners: [[04 Investigations/01 Formal specification audit]] and [[04 Investigations/11 DIVAnd equivalence and successive anomalies]].

### H2 — Succession provides out-of-sample value

**Claim.** The successive estimator improves a predeclared practical axis over tuned one-stage and joint-additive baselines.

**Test.** Paired benchmark comparison at matched tuning and resource budgets.

**Success.** Before confirmatory runs, nominate one primary axis. For accuracy, require the 95% paired bootstrap interval for relative test RMSE improvement to lie above zero on at least two benchmark families, with median improvement at least 5%, and no unexplained regression above 10% on another in-scope family. For computation, require at least 20% reduction in the nominated resource while test RMSE remains within 2% of the best matched baseline.

**Failure.** Gains occur only in training residual, disappear under matched tuning, depend on one seed, or are dominated by a joint baseline.

**Decision.** Failure merges the practical method into known regularization or optimization machinery unless another preregistered advantage passes. Owner: [[04 Investigations/08 Prototype and benchmarks]].

### H3 — Stages have genuine scale meaning

**Claim.** Nominally coarse and fine corrections occupy measurably different scales.

**Test.** Measure Fourier or operator-eigenbasis energy, cross-level correlation, and sensitivity to reversing the scale schedule.

**Success.** At least 80% of each correction's energy lies in its preregistered band or operator eigenspace on separated-scale synthetic data, and absolute correlation between nonadjacent level corrections is below 0.3.

**Failure.** Corrections strongly overlap, cancel, exchange labels across seeds, or their measured frequency ordering contradicts their nominal ordering.

**Decision.** Failure removes multiresolution and band-decomposition language; the method may remain a stagewise optimizer. Owner: [[04 Investigations/04 Spectral-kernel investigation]].

### H4 — The method is not merely repeated DIVAnd regularization erosion

**Claim.** Successive background-anomaly analysis is distinct from repeatedly reducing the influence of the prior.

**Test.** Derive the fixed-operator polynomial filter and compare fixed-length repeated passes with one DIVAnd optimum along a regularization path.

**Success.** A changing, independently justified operator schedule produces held-out or calibrated-uncertainty gains that no matched single-pass regularization setting reproduces.

**Failure.** A one-pass setting matches the successive predictions within (10^{-6}) relative norm, or successive gains are explained entirely by lower effective regularization and worse calibration.

**Decision.** Failure recasts succession as a regularization path or iterative solver, not a new estimator. Owner: [[04 Investigations/11 DIVAnd equivalence and successive anomalies]].

### H5 — Stagewise scales add value beyond a joint multiscale covariance

**Claim.** Fitting scale components successively has an advantage over combining the same scales in one covariance or additive kernel.

**Test.** Compare with [[02 Papers/Mirouze 2016 - Multiple length-scale covariance]] and a jointly fitted additive kernel using identical component scales.

**Success.** H2 passes against the joint model, or succession reaches a statistically noninferior result within 2% RMSE using at least 20% less nominated computation or memory.

**Failure.** The joint model is equal or better at matched budget, or stage ordering introduces avoidable instability.

**Decision.** Failure favors the joint covariance and removes succession from the core claim. Owner: [[04 Investigations/11 DIVAnd equivalence and successive anomalies]].

### H6 — Uncertainty remains calibrated across levels

**Claim.** Stagewise corrections admit useful uncertainty propagation rather than treating the final field as deterministic.

**Test.** Simulated fields from the assumed prior plus held-out observations under homoscedastic, heteroscedastic, and correlated noise.

**Success.** Empirical coverage of nominal 90% intervals lies between 85% and 95% in each preregistered noise regime, and negative log predictive density is not worse than the tuned variational or GP baseline by more than its paired 95% interval.

**Failure.** Intervals systematically narrow with each pass while held-out errors do not, or coverage falls outside the tolerance without a diagnosed model-misspecification boundary.

**Decision.** Failure restricts claims to point reconstruction and blocks probabilistic claims. Owners: [[04 Investigations/08 Prototype and benchmarks]] and [[04 Investigations/11 DIVAnd equivalence and successive anomalies]].

### H7 — The recurrence is numerically stable

**Claim.** Later corrections do not amplify observation or roundoff perturbations uncontrollably.

**Test.** Track coefficient norms, condition numbers, empirical Lipschitz amplification, cancellation, and solver iterations as levels increase.

**Success.** The preregistered stopping rule halts before validation loss worsens by more than 2%, and a (10^{-6}) relative input perturbation does not cause more than (10^{-3}) relative output change on well-posed benchmark regimes.

**Failure.** Norms diverge, adjacent stages substantially cancel, results depend strongly on solver tolerance, or small perturbations cause macroscopic prediction changes.

**Decision.** Failure requires stronger regularization, damping, orthogonalization, or dropping the affected regime. Owner: [[04 Investigations/09 Falsification and failure modes]].

### H8 — Geometry-aware constraints solve a real failure of Euclidean kernels

**Claim.** Masks, topology, periodicity, or advection constraints materially improve reconstruction on relevant irregular domains.

**Test.** Split-basin, periodic space-time, and advected-ridge benchmarks against unconstrained Euclidean kernels.

**Success.** Cross-barrier leakage is reduced by at least 50% with no more than 5% degradation inside connected regions, or the corresponding preregistered physical-consistency error improves with noninferior RMSE.

**Failure.** Constraints do not change the relevant error, or improvements arise only from extra tuning budget.

**Decision.** Failure keeps geometry machinery optional rather than foundational. Owner: [[04 Investigations/06 Irregular-domain multiresolution]].

### H9 — The hierarchy is a nested-space or stable-frame construction

**Claim.** The levels form a genuine filtration, projection decomposition, or stable nonorthogonal frame.

**Test.** Establish range inclusion, idempotence or quasi-projection bounds, compatibility, density, and frame or reconstruction bounds.

**Success.** A theorem with explicit assumptions proves the claimed structure and constants do not deteriorate uncontrollably with level.

**Failure.** All stages have the same full range, changing kernels break inclusion, or only empirical coarse-to-fine appearance remains.

**Decision.** Failure removes MRA, projection, and filtration claims but does not by itself reject the estimator. Owner: [[04 Investigations/03 Nested-space theorem audit]].

### H10 — The method scales beyond low-dimensional dense interpolation

**Claim.** The proposed representation remains useful as sample count or dimension grows.

**Test.** Scaling curves in (n), ambient dimension, and effective dimension at matched accuracy.

**Success.** Demonstrate a preregistered regime with better empirical time or memory scaling than the dense baseline and no more than 2% RMSE degradation; report fitted log-log slopes and uncertainty.

**Failure.** Distance concentration destroys scale separation, cost remains dense-cubic or dense-quadratic without a compensating accuracy advantage, or only low-effective-dimensional examples work without stating that restriction.

**Decision.** Failure narrows the method's domain rather than automatically killing its low-dimensional use. Owner: [[04 Investigations/07 High-dimensional scalability]].

### H11 — The renormalization correspondence is structural, not metaphorical

**Claim.** A defined coarse-graining, rescaling, and effective-parameter flow corresponds to the successive interpolation operators.

**Test.** Construct an explicit commuting diagram or algebraic mapping and verify it on a solvable example.

**Success.** The mapping identifies degrees of freedom being eliminated or introduced, a scale transformation, and a parameter flow, with the relevant operations commuting exactly or under a proved approximation bound.

**Failure.** The connection consists only of both methods using multiple scales or proceeding in opposite directions without a duality map.

**Decision.** Failure removes RG framing from the technical claim. Owner: [[04 Investigations/05 Renormalization correspondence]].

### H12 — A defensible novelty claim survives

**Claim.** The final specified combination is not already disclosed and its distinguishing feature causes a measured or proved benefit.

**Test.** Exact operator comparison, forward and backward citation search, terminology variants, code search, and later patent search.

**Success.** No equivalent method is found after the documented search, and at least one distinguishing feature passes H2, H5, H8, H9, or H10.

**Failure.** An earlier method has the same recurrence and assumptions, or the only differences are terminology and implementation details without demonstrated consequence.

**Decision.** Failure changes the output from a novelty claim to a synthesis, implementation, application, or comparative study. Owners: [[04 Investigations/02 Direct prior-art comparison]] and [[04 Investigations/10 Novelty and terminology search]].

## Interpretation rules

- H0 and H1 are entry gates.
- H2 or another clearly nominated practical/theoretical contribution must pass for the method to be worth developing as more than a reproduction.
- H4 and H5 decide whether succession remains central.
- H3, H9, and H11 govern vocabulary; their failure must remove the corresponding spectral-band, MRA, or RG claims.
- H6, H8, and H10 are scope claims and may fail in declared regimes without invalidating all uses.
- H12 is evaluated last because novelty depends on the final, not provisional, specification.

## Links

- [[00 Project/Next steps]]
- [[05 Experiments/Benchmark matrix]]
- [[05 Experiments/Experimental program]]
- [[04 Investigations/Investigation index]]

