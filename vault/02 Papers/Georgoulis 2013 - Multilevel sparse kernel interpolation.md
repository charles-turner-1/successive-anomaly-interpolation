# Georgoulis, Levesley, and Subhan 2013: Multilevel sparse kernel-based interpolation

**Citation:** Emmanuil H. Georgoulis, Jeremy Levesley, and Fazli Subhan. SIAM Journal on Scientific Computing 35(2), A815-A831, 2013. [DOI](https://doi.org/10.1137/110859610). [arXiv](https://arxiv.org/abs/1204.4153).

## Why it matters

MLSKI targets moderately high-dimensional interpolation. It hierarchically decomposes data sites, interpolates the previous level's residual, uses anisotropically scaled kernels, and combines small problems through a sparse-grid construction.

## Project relevance

This paper joins three threads from the supplied conversation:

- multidimensional interpolation;
- kernels with scale-dependent spectral behavior;
- successive residual correction.

It may be a stronger prior-art match than generic wavelet literature.

## Questions for reproduction

- Which dimensions and sample counts show a real advantage?
- How sensitive is the method to anisotropy and non-grid sampling?
- Does sparse combination cause cancellation or negative weights?
- What are the error bounds in mixed-smoothness spaces?
- Can the level hierarchy be interpreted as a spectral partition?

## Related

- [[05 Experiments/Benchmark matrix]]
- [[04 Investigations/07 High-dimensional scalability]]

