# D020 — Derive the spectral kernel

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D003
- **Hypotheses:** H3
- **Verification classes:** V1, V2

## Objective

Derive the spectral response of the stage kernel or precision operator, including length-scale and dimensional dependence.

## Procedure

1. State transform convention, stationarity assumptions, domain, and boundary idealization.
2. Transform each derivative or kernel term separately.
3. Assemble precision and covariance spectra.
4. Normalize the kernel and state integrability conditions in dimension (d).
5. Derive low- and high-frequency asymptotics and length-scale rescaling.
6. Treat anisotropic separable and full-metric cases.
7. State why global Fourier diagonalization fails with masks or spatially varying coefficients and nominate the replacement basis.

## Required checks

- Numerically Fourier-transform a discretized kernel and compare with the analytic spectrum.
- Check limiting values at zero, infinity, and at least two dimensions.

## Machine verification

`pixi run verify-card -- D020` must compile formal finite identities where encoded and pass symbolic/numerical Fourier comparisons over declared tolerances.

## Primary artifact

`theory/spectral-kernel.md` with transform conventions, derivation, and limiting behavior.

## Acceptance

- Learned parameters are separated from infinite feature dimension.
- Stationary and nonstationary cases are not conflated.
- The DIVAnd ((1+|Lk|^2)^{-m}) baseline is included.

## Failure or escalation

If no global spectrum exists, nominate an operator eigenbasis or local spectral diagnostic for D021.
