# VKOGA

## Source

[GabrieleSantin/VKOGA](https://github.com/GabrieleSantin/VKOGA) is a Python implementation of the Vectorial Kernel Orthogonal Greedy Algorithm with a scikit-learn-style estimator.

## Why it matters

VKOGA greedily selects kernel centers or basis functions based on an error criterion. It offers a strong alternative explanation for "successive anomaly interpolation": the method may be a greedy kernel approximation where each stage attacks the largest remaining residual.

## Comparison axes

- Selection by residual magnitude versus fixed coarse-to-fine schedule.
- One center per iteration versus a whole scale-specific subspace.
- Orthogonalized versus plain residual updates.
- Sparsity and evaluation cost.
- Stability as selected centers cluster.
- Vector-valued output support.

## Decisive experiment

Give both methods the same kernel dictionary and coefficient budget. If adaptive greedy selection dominates a fixed scale succession, the contribution must justify why scale organization matters beyond sparsity.

