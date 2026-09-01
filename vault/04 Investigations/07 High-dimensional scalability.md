# Investigation 07: High-dimensional scalability

## Delivery card

[D046 — Measure high-dimensional scaling](../../plan/deliverables/D046-high-dimensional-scaling.md)

## Goal

Measure where the method fails as input dimension grows and whether sparse grids, anisotropy, low rank, or additive structure delay that failure.

## Mandatory sources

- [[02 Papers/Georgoulis 2013 - Multilevel sparse kernel interpolation]]
- Rahimi and Recht in [[06 Sources/Bibliography]]
- [[03 Code/VKOGA]]

## Tasks

1. Derive time and memory complexity in \(n,d,L,m\).
2. Test dimensions 1, 2, 4, 8, 16, and 32 on functions with known effective dimension.
3. Separate ambient dimension from intrinsic dimension.
4. Measure distance concentration and kernel-matrix rank.
5. Compare dense kernels, local neighbors, random Fourier features, greedy centers, and sparse grids.
6. Test axis-aligned and rotated anisotropy.

## Deliverables

- Scaling plots and fitted empirical exponents.
- Break-even table by method.
- Memory ceiling estimates.
- Clear statement of the smoothness or low-dimensional structure required.
