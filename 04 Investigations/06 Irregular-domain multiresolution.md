# Investigation 06: Irregular-domain multiresolution

## Goal

Find a principled scale hierarchy for scattered points, graphs, manifolds, or bounded irregular domains.

## Mandatory sources

- [[02 Papers/Coifman Maggioni 2006 - Diffusion wavelets]]
- Townsend and Wendland in [[02 Papers/Wendland 2010 - Multiscale RBF approximation]]
- [[03 Code/SciPy and RBF libraries]]
- [[03 Code/DIVAnd]]

## Tasks

1. Compare Euclidean bandwidth, fill distance, graph diffusion time, and adaptive neighborhood radius as scale variables.
2. Test nonuniform sampling density and holes in the domain.
3. Determine boundary behavior.
4. Compare isotropic, anisotropic, and geometry-adapted kernels.
5. Construct a diffusion operator from the correlation kernel and inspect numerical rank across powers.
6. Determine whether its compressed ranges form useful nested spaces.
7. Test whether masks and grid topology prevent leakage across barriers more reliably than Euclidean distance alone.
8. Compare diffusion time with DIVAnd correlation length on the same discrete domain.

## Deliverables

- Recommended scale operator for each domain type.
- Synthetic counterexample where Euclidean bandwidth fails.
- Complexity estimate for graph construction and multilevel evaluation.
- Decision on whether diffusion wavelets belong in the first prototype or a later branch.
