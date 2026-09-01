# DIVAnd.jl

## Repository

- [Source](https://github.com/gher-uliege/DIVAnd.jl)
- [Documentation](https://gher-uliege.github.io/DIVAnd.jl/latest/)
- [Foundational paper](https://doi.org/10.5194/gmd-7-225-2014)
- License: GPL-2.0-or-later in the repository
- Language: Julia

## Relevant entry points

| Entry point | Role in this project |
|---|---|
| `DIVAndrun` | Core n-dimensional gridded variational analysis |
| `DIVAndfun` | Simpler interface returning an interpolation function |
| `diva3D` | Higher-level geophysical workflow with metric and parameter handling |
| `DIVAndgo` | Large-problem solver selection and overlapping domain decomposition |
| `DIVAnd_cv` | Cross-validation of correlation length and observation-error parameters |
| `DIVAnd_errormap` | Analysis-error variance estimates |
| `DIVAnd_heatmap` | Kernel-density rather than field interpolation mode |

The repository includes a four-dimensional example calling

```julia
fi, s = DIVAndrun(mask, metrics, grid, obs_coords, anomalies, len, epsilon2;
                  moddim=[0, 0, 0, 1])
```

where `moddim` makes the final dimension periodic. The observation values are documented as anomalies relative to a background field. A nonzero first guess is subtracted before analysis and added back afterwards.

## Parameters that matter most

- `len`: one or spatially varying correlation length per dimension;
- `epsilon2`: observation-error variance normalized by background variance, with richer forms for heterogeneous or correlated errors;
- `alpha`: derivative-penalty coefficients, normally chosen from a Pascal-triangle row;
- `mask`: valid grid cells and topological barriers;
- grid metrics: convert coordinate increments and length scales to nondimensional derivatives;
- `moddim`: periodic directions;
- optional quadratic, inequality, advection, flux, or derivative constraints.

## Proposed use

Treat DIVAnd as three baselines:

1. **Single optimum:** one cross-validated length scale and error ratio.
2. **Joint multiscale:** one objective whose covariance or constraints encode several scales, if implementable without changing the method's meaning.
3. **Successive anomalies:** repeatedly analyze the current observation-minus-background anomaly with a prespecified coarse-to-fine length schedule.

Compare predictions, held-out residuals, posterior-error calibration, conditioning, solver time, and the effective observation-space filter (HA_\ell).

## Integration caution

The GPL license permits experiments and modification but affects redistribution of combined derivative software. For a language-neutral or permissively licensed final implementation, use the equations and benchmark behavior as the reference and obtain legal guidance before copying source.

