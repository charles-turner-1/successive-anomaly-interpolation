# Mallat 1989: Multiresolution approximations and wavelet bases

**Citation:** Stéphane G. Mallat. Transactions of the American Mathematical Society 315(1), 69-87, 1989. [DOI and PDF](https://www.ams.org/journals/tran/1989-315-01/S0002-9947-1989-1008470-5/).

Companion signal-processing paper: "A Theory for Multiresolution Signal Decomposition: The Wavelet Representation," IEEE TPAMI 11(7), 674-693, 1989. [Author publication page](https://www.di.ens.fr/~mallat/biblio.html).

## Why it matters

Mallat formalizes a multiresolution approximation as a sequence of embedded spaces and derives wavelet detail spaces and fast decomposition algorithms. This is the correct reference for the filtration idea raised in the shared conversation.

## What can transfer

- Nested spaces indexed by resolution.
- Scaling and refinement relations.
- Approximation plus detail decomposition.
- Stable reconstruction from level coefficients.
- Localization in both position and frequency.

## What cannot be assumed

A sequence of kernel fits with shrinking bandwidth is not automatically an MRA. The spaces must satisfy inclusion, scaling, density, intersection, and basis or frame conditions. See [[01 Concepts/Nested spaces and projections]].

