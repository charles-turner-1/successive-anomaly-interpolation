# Investigation 03: Nested-space theorem audit

## Goal

Decide whether the level sequence is a filtration, an orthogonal MRA, a frame decomposition, a stable subspace correction, or none of these.

## Mandatory sources

- [[01 Concepts/Nested spaces and projections]]
- [[02 Papers/Mallat 1989 - Multiresolution analysis]]
- [[02 Papers/Narcowich Schaback Ward 1999 - Multilevel interpolation]]

## Tasks

1. Define \(V_\ell=\operatorname{range}(A_\ell)\).
2. Prove or disprove \(V_\ell\subseteq V_{\ell+1}\).
3. Test idempotence and compatibility of stage operators.
4. If inclusion fails, measure subspace angles numerically.
5. Look for frame bounds or contraction estimates instead of orthogonality.
6. Establish conditions for convergence of \(f_L\).
7. Separate infinite-domain, bounded-domain, and finite-sample claims.

## Deliverables

- Proposition list with assumptions.
- Proofs or smallest counterexamples.
- Correct mathematical label for the hierarchy.
- Recommendation on whether wavelet terminology is justified.

## Stop condition

Stop once every MRA axiom has a proof, a counterexample, or a declared nonapplicability.

