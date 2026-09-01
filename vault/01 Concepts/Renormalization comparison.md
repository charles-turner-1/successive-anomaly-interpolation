# Renormalization comparison

## What RG does

A Wilsonian renormalization-group step usually:

1. separates fine and coarse degrees of freedom;
2. integrates out or marginalizes the fine variables;
3. rescales the remaining description;
4. tracks how effective couplings change.

Repeated steps define a flow in model or coupling space. Fixed points and relevant directions explain scale-invariant behavior and universality.

## What residual interpolation does

A typical multilevel interpolator starts with a coarse approximation, computes what it missed, and adds progressively finer corrections. It retains or reconstructs detail rather than integrating it out.

This is the main directional mismatch:

\[
\text{RG: fine}\to\text{coarse effective theory}
\]

\[
\text{residual reconstruction: coarse estimate}\to\text{fine reconstruction}
\]

## Plausible precise bridges

### Analysis and synthesis duality

An analysis transform can decompose a field from fine to coarse. A synthesis transform reconstructs it from coarse to fine. If successive anomaly interpolation is the synthesis side of a multiresolution transform, RG may resemble part of the analysis side.

### Conditional factorization

A joint field distribution can factor into a coarse marginal and conditional detail distributions. [[02 Papers/Marchand 2023 - Wavelet conditional RG]] uses this structure explicitly and generates from coarse to fine while retaining an RG interpretation.

### Parameter flow under scale change

If the algorithm re-estimates kernel parameters at each scale, their trajectory may be called a flow. It becomes RG-like only if there is a defined coarse-graining map, rescaling operation, and invariant prediction under changes of resolution.

### Relevant and irrelevant residual modes

One could classify residual components by how they change under coarse-graining. This requires an operator acting on both functions and model parameters. Frequency magnitude alone is not enough.

## Falsification criteria

Do not claim an RG correspondence unless the work identifies:

- the degrees of freedom being eliminated;
- the coarse-graining map;
- the rescaling map;
- the running couplings or parameters;
- an invariant or fixed point;
- the direction corresponding to reconstruction.

Without those elements, "RG-inspired" or "multiscale" is more accurate.

## Sources

- Wilson and Kogut in [[06 Sources/Bibliography]]
- [[02 Papers/Marchand 2023 - Wavelet conditional RG]]
- Mehta and Schwab, and Stottmeister et al. in [[06 Sources/Bibliography]]

