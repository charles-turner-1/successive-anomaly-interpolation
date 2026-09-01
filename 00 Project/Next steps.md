# Next steps

## Stage 1 — Lock the object being tested

1. Complete [[04 Investigations/01 Formal specification audit]].
2. Choose one operational meaning of anomaly.
3. Freeze the recurrence, background, stage operator, scale schedule, damping, error model, and stopping rule.
4. Produce the three-observation hand calculation.
5. Pass H0 and H1 in [[00 Project/Hypothesis ledger and decision rules]].

Do not start a broad benchmark sweep before this stage passes.

## Stage 2 — Implement the smallest comparison

Implement [[05 Experiments/Minimum reference algorithm]] with deterministic seeds and four estimators:

1. one tuned variational or DIVAnd solve;
2. successive DIVAnd-compatible background-anomaly updates;
3. one joint multiple-length-scale covariance or additive kernel;
4. classical multilevel RBF residual correction.

Use the dyadic-sinusoid, Franke, split-basin, and background-plus-anomalies rows of [[05 Experiments/Benchmark matrix]]. Store predictions, residuals, spectra, uncertainty, time, memory, and solver diagnostics in a common result schema.

## Stage 3 — Resolve the central equivalence question

Run [[04 Investigations/11 DIVAnd equivalence and successive anomalies]]. Evaluate H4 and H5 before investing in neural, high-dimensional, or RG extensions.

Possible decisions:

- **H4 and H5 pass:** retain succession as the core estimator.
- **H4 passes, H5 fails:** use a joint multiscale covariance and treat succession as an implementation option.
- **H4 fails:** describe the method as a regularization path or iterative solver.
- **H2 also fails:** stop method development and retain the vault as a negative comparative result.

## Stage 4 — Establish scale and stability claims

Run [[04 Investigations/04 Spectral-kernel investigation]] and [[04 Investigations/09 Falsification and failure modes]]. Evaluate H3 and H7. Freeze the confirmatory thresholds and seeds after smoke tests but before full runs.

## Stage 5 — Expand only along surviving claims

- If irregular geometry matters, run [[04 Investigations/06 Irregular-domain multiresolution]] and H8.
- If nested-space language remains plausible, run [[04 Investigations/03 Nested-space theorem audit]] and H9.
- If scaling is part of the target contribution, run [[04 Investigations/07 High-dimensional scalability]] and H10.
- If probabilistic output is claimed, complete H6.
- Pursue [[04 Investigations/05 Renormalization correspondence]] only if a concrete operator sequence survives; evaluate H11.

## Stage 6 — Novelty and write-up

Run the final prior-art and terminology pass only against the surviving algorithm. Evaluate H12, record negative results, and choose one outcome:

- new estimator;
- new solver or continuation strategy;
- synthesis connecting spectral kernels and variational analysis;
- domain-specific application of an established method;
- or documented negative result.

