# Code index

## Immediate baselines

- [[03 Code/SciPy and RBF libraries]] for deterministic scattered interpolation.
- [[03 Code/Wavelet and pyramid libraries]] for exact multiscale analysis and reconstruction.
- [[03 Code/GPyTorch spectral mixtures]] for learned spectral kernels and uncertainty.
- [[03 Code/VKOGA]] for greedy kernel approximation.
- [[03 Code/DIVAnd]] for n-dimensional variational analysis, barriers, constraints, and uncertainty.
- [HINT](https://github.com/DingShizhe/HINT) for learned hierarchical residual interpolation.

## Repositories

| Repository | Use in this project | License or maturity note |
|---|---|---|
| [PyWavelets/pywt](https://github.com/PyWavelets/pywt) | 1D, 2D, and nD multilevel DWT; coefficient and reconstruction tests | Mature, MIT |
| [LabForComputationalVision/pyrtools](https://github.com/LabForComputationalVision/pyrtools) | Laplacian and steerable pyramid baselines | Research library, Python 3 |
| [scipy/scipy RBFInterpolator](https://github.com/scipy/scipy/blob/main/scipy/interpolate/_rbfinterp.py) | Stable conventional RBF baseline in \(N\) dimensions | Mature SciPy component |
| [treverhines/RBF](https://github.com/treverhines/RBF) | RBFs, derivatives, scattered interpolation, GP tools | Focused scientific package |
| [GabrieleSantin/VKOGA](https://github.com/GabrieleSantin/VKOGA) | Greedy vector-valued kernel approximation | GPL-3.0 |
| [cornellius-gp/gpytorch](https://github.com/cornellius-gp/gpytorch) | Spectral mixture GP and scalable kernels | Mature PyTorch ecosystem |
| [DingShizhe/HINT](https://github.com/DingShizhe/HINT) | Direct neural residual-refinement comparison | Old Python and CUDA stack |
| [gher-uliege/DIVAnd.jl](https://github.com/gher-uliege/DIVAnd.jl) | Variational background-anomaly baseline and spectral precision-operator reference | Mature Julia research code, GPL-2.0-or-later |
| [qi-rub/pyfermions](https://github.com/qi-rub/pyfermions) | Concrete wavelet and entanglement-RG connection | Specialized physics code |
| [wangbolun300/Scattered_Points_Interpolation](https://github.com/wangbolun300/Scattered_Points_Interpolation) | Contains a multilevel B-spline comparison implementation | C++ research code |

## Selection rule

Do not begin by reproducing HINT. First build the small deterministic experiment in [[05 Experiments/Minimum reference algorithm]]. It will reveal whether the proposed recurrence adds value before training or dependency complexity obscures the result.
