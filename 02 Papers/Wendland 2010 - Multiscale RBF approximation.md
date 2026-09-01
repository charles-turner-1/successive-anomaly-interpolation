# Wendland 2010: Multiscale analysis in Sobolev spaces on bounded domains

**Citation:** Holger Wendland. Numerische Mathematik 116, 493-517, 2010. [DOI](https://doi.org/10.1007/s00211-010-0313-8).

Related boundary-constrained variant: Alex Townsend and Holger Wendland, IMA Journal of Numerical Analysis 33(3), 1095-1114, 2013. [DOI](https://doi.org/10.1093/imanum/drs036).

## Why it matters

The method uses scattered sites and scaled compactly supported RBFs. It constructs the approximation through successive residual corrections, changing support radii to capture different scales. The paper proves convergence and reports level-independent conditioning under its assumptions.

## Likely theorem template

The analysis relates spatial resolution, often measured through fill distance \(h_j\), to kernel scale \(\delta_j\), then proves contraction in a Sobolev or native-space norm. This is more directly useful to the proposed method than an analogy to quantum mechanics.

## Questions to resolve

- Is the scaled native space the same at every level up to norm equivalence?
- What ratios between \(h_j\) and \(\delta_j\) are allowed?
- Does the proof cover noisy data or exact samples only?
- Can anisotropic or full spectral scale matrices replace scalar radii?
- What breaks as dimension grows?

## Code route

Use [[03 Code/SciPy and RBF libraries]] for a clean-room prototype, then compare with [[03 Code/VKOGA]].

