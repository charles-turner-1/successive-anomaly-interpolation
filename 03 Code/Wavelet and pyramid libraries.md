# Wavelet and pyramid libraries

## PyWavelets

[Repository](https://github.com/PyWavelets/pywt) and [multilevel documentation](https://pywavelets.readthedocs.io/en/stable/regression/multilevel.html).

Useful operations:

- `wavedec`, `waverec` for 1D;
- `wavedec2`, `waverec2` for images;
- `wavedecn`, `waverecn` for n-dimensional arrays;
- stationary wavelet transforms for undecimated comparisons;
- coefficient packing for direct residual-band inspection.

Use it to establish an ideal case where nested multiresolution and exact reconstruction are known. Compare the learned or kernel-stage corrections with true wavelet bands by subspace angle, spectral energy, and correlation.

## pyrtools

[Repository](https://github.com/LabForComputationalVision/pyrtools).

It implements Laplacian, wavelet, QMF, and steerable pyramids for 1D and 2D signals. Use the Laplacian pyramid as the main coarse-to-fine residual reconstruction baseline.

## Proposed diagnostic

Generate a field with known separated scales. Decompose it with PyWavelets or a Laplacian pyramid. Sample it irregularly. Run the successive kernel method. Compare each learned correction with the known bands after evaluation on the dense grid.

