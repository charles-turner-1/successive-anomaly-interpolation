# Experimental program

All confirmatory experiments follow [[00 Project/Hypothesis ledger and decision rules]]. The execution sequence and branch decisions are in [[00 Project/Next steps]].

## Phase 0: definition lock

Complete [[04 Investigations/01 Formal specification audit]]. No serious benchmark is interpretable until the stage restriction and meaning of anomaly are fixed.

## Phase 1: deterministic proof of concept

Implement [[05 Experiments/Minimum reference algorithm]] with Gaussian kernel ridge stages. Use the first four rows of [[05 Experiments/Benchmark matrix]]. The goal is to observe when stage corrections align with known scales.

## Phase 2: compare model classes

Run one-stage, joint additive, stagewise additive, greedy, GP, and DIVAnd baselines at matched budgets. Compare a single variational optimum with successive background-anomaly updates and a joint multiple-length-scale model. This distinguishes a new hypothesis class from an optimizer or regularizer.

## Phase 3: mathematical diagnostics

Estimate stage-operator spectra, subspace angles, frame stability, and perturbation amplification. Connect results to [[04 Investigations/03 Nested-space theorem audit]].

## Phase 4: dimensionality and geometry

Run [[04 Investigations/06 Irregular-domain multiresolution]] and [[04 Investigations/07 High-dimensional scalability]]. Promote diffusion or sparse-grid machinery only if Euclidean dense kernels fail in a way those methods address.

## Phase 5: RG branch

Attempt [[04 Investigations/05 Renormalization correspondence]] after the deterministic operator sequence is stable. If uncertainty and conditional detail distributions become central, compare with [[02 Papers/Marchand 2023 - Wavelet conditional RG]].

## Evidence gates

- **Gate A:** recurrence is nonredundant and reproducible.
- **Gate B:** improvement survives matched-budget baselines.
- **Gate C:** scale labels match measured correction content.
- **Gate D:** stability or convergence is proved under stated assumptions.
- **Gate E:** novelty survives direct prior-art comparison.
- **Gate F:** succession improves held-out reconstruction or calibrated uncertainty over one tuned variational solve, rather than merely lowering observation residuals.

The gates are shorthand only. The operational pass/fail thresholds and consequences are the H0–H12 entries in [[00 Project/Hypothesis ledger and decision rules]].
