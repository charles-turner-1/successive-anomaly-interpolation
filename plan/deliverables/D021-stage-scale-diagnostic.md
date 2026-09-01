# D021 — Define the stage-scale diagnostic

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D020, D031
- **Hypotheses:** H3
- **Verification classes:** V2

## Objective

Turn “coarse” and “fine” into a computable per-stage diagnostic.

## Procedure

1. Choose Fourier bins for periodic Euclidean data and operator eigenvalue bins for irregular domains.
2. Define energy normalization, spectral centroid, intended band, leakage, and cross-level correlation.
3. Specify treatment of nonuniform sampling and windowing.
4. Implement metrics on a common evaluated grid or basis.
5. Construct fixtures containing one band, two separated bands, overlapping bands, and white noise.
6. Set thresholds without using confirmatory outputs.
7. Produce a standard per-stage diagnostic plot and machine-readable record.

## Required checks

- Recover fixture bands within discretization tolerance.
- Verify diagnostics are invariant to overall amplitude and document any coordinate-unit dependence.

## Machine verification

`pixi run verify-card -- D021` must regenerate synthetic fixtures and assert band recovery, normalization invariance, and threshold behavior.

## Primary artifact

`metrics/stage-scale.md` plus a tested function returning band energy, spectral centroid, leakage, and cross-level correlation.

## Acceptance

- Intended bands are fixed without observing confirmatory results.
- The function recovers known bands on a synthetic fixture.
- Thresholds match H3 or record a preregistered replacement.

## Failure or escalation

If components cannot be assigned stable scales, remove band-language and test only stagewise optimization.
