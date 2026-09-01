# Search log

## Scope searched

Searches covered:

- multiresolution analysis and wavelet bases;
- Laplacian pyramids;
- multilevel and multiscale kernel or RBF interpolation;
- multilevel B-splines;
- hierarchical residual neural interpolation;
- Fourier and spectral Gaussian-process kernels;
- random Fourier features and sparse spectrum GPs;
- matching pursuit, boosting, and greedy kernel approximation;
- diffusion wavelets on graphs and manifolds;
- renormalization, wavelet RG, and deep-learning/RG mappings;
- source repositories for direct experiments.
- n-dimensional variational analysis, data assimilation, diffusion covariance operators, analysis-error estimation, and the DIVAnd source and documentation.

## Strongest findings

1. Lee et al. 1997 gives an explicit coarse-to-fine residual interpolation algorithm.
2. Narcowich, Schaback, and Ward 1999, plus Wendland 2010, provide approximation-theory foundations for multilevel residual correction with kernels or RBFs.
3. Georgoulis et al. 2013 addresses moderately high-dimensional sparse kernel interpolation with hierarchical residuals and anisotropic scales.
4. Ding et al. 2023 implements learned hierarchical residual refinement on scattered data.
5. Marchand et al. 2023 is the strongest exact bridge among wavelets, coarse-to-fine conditional modeling, and RG.
6. Barth et al. 2014 and DIVAnd.jl provide the strongest bridge between background anomalies, multidimensional scattered interpolation, a differential precision operator, and an explicit Fourier covariance spectrum.
7. Mirouze et al. 2016 provides the necessary joint multiple-length-scale covariance baseline; succession must be tested against it, not only against single-scale smoothers.

## Search gap

The phrase "successive anomaly interpolation" did not return an established method in a focused exact-phrase search. That absence is weak evidence only. "Anomaly" may be private terminology, a domain-specific field name, or a transcription of a different term.

## Work still needed

- Forward citation search from the 1997, 1999, 2010, and 2013 multilevel interpolation papers.
- Patent search after the algorithm is specified.
- Search beyond oceanography once it is confirmed whether “anomaly” means departure from a background field.
- Full theorem extraction from paywalled or scanned primary papers.
- Repository-level reproducibility checks and license review before code reuse.

## Source policy

Paper claims in this vault link to original proceedings, journal DOI pages, author-hosted manuscripts, or official repositories where available. Secondary pages were used only to discover primary sources.
