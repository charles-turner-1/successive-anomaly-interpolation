# Coifman and Maggioni 2006: Diffusion wavelets

**Citation:** Ronald R. Coifman and Mauro Maggioni. Applied and Computational Harmonic Analysis 21(1), 53-94, 2006. [DOI](https://doi.org/10.1016/j.acha.2006.04.004). [PDF](https://perception.inrialpes.fr/~Horaud/Courses/www-documents/diffusion-wavelets.pdf).

## Why it matters

Diffusion wavelets lift multiresolution ideas from Euclidean grids to data clouds, graphs, and manifolds. Powers of a diffusion operator provide scale. Compression of those powers constructs scaling functions, wavelets, and downsampling operators adapted to the data geometry.

## Project relevance

If successive anomaly interpolation targets scattered multidimensional locations or irregular domains, a diffusion operator may define scale more naturally than Euclidean kernel bandwidth. It also gives a principled coarse-graining operation, strengthening a possible RG comparison.

## Questions

- Can the project's correlation kernel be normalized into a diffusion operator?
- Do its powers become numerically low rank?
- Can interpolation residuals be expanded in diffusion-wavelet detail spaces?
- Does geometry-adapted scale outperform isotropic Fourier scale on nonuniform samples?

