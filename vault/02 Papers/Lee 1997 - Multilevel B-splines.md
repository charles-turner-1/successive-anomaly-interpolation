# Lee 1997: Scattered data interpolation with multilevel B-splines

**Citation:** Seungyong Lee, George Wolberg, and Sung Yong Shin. IEEE Transactions on Visualization and Computer Graphics 3(3), 228-244, 1997. [DOI](https://doi.org/10.1109/2945.620490). [Author-hosted PDF](https://cg.postech.ac.kr/papers/scatteredData.pdf).

## Why it matters

This is the closest classical match found. A coarse lattice estimates the global shape. Finer lattices approximate and remove the remaining residual at the data points. The final surface is the sum of the level functions.

## Algorithmic correspondence

The paper states that the coarsest lattice is applied to the original data and that all finer lattices approximate and remove residual error. At level \(k\), it updates the data values by subtracting the current B-spline approximation.

That is structurally the recurrence in [[00 Project/Working definition and assumptions#Minimal mathematical skeleton]].

## Important details

- Uses bicubic B-spline control lattices.
- Produces a \(C^2\)-continuous surface.
- Can refine and combine the hierarchy into an equivalent finest-lattice representation.
- Gives a sufficient condition for exact interpolation when the finest lattice separates nearby data adequately.
- Offers an adaptive representation to avoid storing empty fine-lattice control points.

## What to extract next

- Express its B-spline refinement relation as nested spaces \(V_k\).
- Compare its local weighted assignment with the proposed kernel correlation rule.
- Reproduce its residual decay and smoothness behavior on modern benchmarks.
- Check whether the proposed method reduces to MBA under a compact tensor-product spline kernel.

## Difference to preserve

MBA is grid-hierarchical and spline-specific. A genuinely spectral, irregular-domain, uncertainty-aware, or high-dimensional method may still differ substantially.

