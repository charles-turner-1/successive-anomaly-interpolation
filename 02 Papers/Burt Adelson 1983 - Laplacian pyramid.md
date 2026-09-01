# Burt and Adelson 1983: The Laplacian pyramid as a compact image code

**Citation:** Peter J. Burt and Edward H. Adelson. IEEE Transactions on Communications 31(4), 532-540, 1983. [DOI](https://doi.org/10.1109/TCOM.1983.1095851). [PDF](https://www.rctn.org/bruno/public/papers/Laplacian-pyramid-Burt%2BAdelson1983.pdf).

## Why it matters

The Laplacian pyramid repeatedly subtracts an expanded low-pass version from the current image and then applies the same process to the reduced low-pass image. It produces localized band-pass residuals at multiple scales and supports reconstruction.

## Relation to the project

The shared idea of interpolating successive anomalies resembles a synthesis process that accumulates residual bands. The pyramid supplies a concrete test case where the decomposition and reconstruction operators are known.

## Limits

- Classical construction assumes a regular image grid.
- Filters and downsampling define scale explicitly.
- It decomposes known dense data rather than inferring a field from scattered samples.
- The representation may be redundant and need not be an orthonormal projection hierarchy.

## Code

See [[03 Code/Wavelet and pyramid libraries]].

