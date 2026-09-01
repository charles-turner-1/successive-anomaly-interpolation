# Bridge matrix

| Field | Stage object | Residual or detail | Scale mechanism | Nested spaces required? | Main caution |
|---|---|---|---|---|---|
| Multilevel B-splines | Spline on a control lattice | Sample residual | Finer lattice spacing | Refinable spline spaces often support it | Approximation is not automatically orthogonal |
| Multiscale RBF interpolation | Kernel interpolant | Sample residual | Kernel support radius and site density | Not always | Scaled RKHSs and finite spans may not be nested |
| Wavelet MRA | Projection into \(V_j\) | Detail in \(W_j\) | Dilation | Yes, by definition | Requires refinement and stability conditions |
| Laplacian pyramid | Low-pass image and band-pass difference | Difference of adjacent pyramid levels | Filter and downsample | Operator hierarchy, not necessarily an orthonormal MRA | Redundant implementations are common |
| Matching pursuit | Selected dictionary atom | Remaining signal | Adaptive atom scale | No | Greedy sparsity is not coarse-to-fine by default |
| Gradient boosting | Weak learner | Negative gradient or residual | Iteration, sometimes learner depth | No | Iteration is optimization time, not physical scale |
| Spectral mixture GP | Kernel component | Statistical covariance component | Spectral mean and variance | No | Components can overlap and be unidentifiable |
| HINT | Neural interpolation block | Residual at observed sites | Hierarchical attention locality | No explicit function-space theorem | Learned blocks may not correspond to frequency bands |
| Diffusion wavelets | Compressed basis for powers of a diffusion operator | Operator-adapted detail | Diffusion time | Constructed multiresolution | Depends on geometry and operator choice |
| DIVAnd / variational analysis | Posterior or MAP anomaly field | Observation minus background | Correlation length and derivative precision | No; normally the same grid state space | Repeated passes may only weaken regularization |
| Renormalization group | Effective action or Hamiltonian | Eliminated fast degrees of freedom | Coarse-grain plus rescale | Often a scale hierarchy, not necessarily nested linear spaces | Flow is in theory space, not simply function approximation |

## Strongest bridge

The chain with the least conceptual strain is:

\[
\text{successive residual fit}
\leftrightarrow
\text{multilevel B-spline/RBF interpolation}
\leftrightarrow
\text{multiresolution or frame decomposition}
\leftrightarrow
\text{analysis/synthesis view of scale}
\]

The variational route adds a second rigorous chain:

\[
\text{background anomaly}
\leftrightarrow
\text{quadratic inverse problem}
\leftrightarrow
\text{precision differential operator}
\leftrightarrow
\text{Fourier covariance kernel}.
\]

Renormalization should be attached only after the coarse-graining and parameter-flow objects are specified.
