# Successive Anomaly Interpolation research vault

This vault turns the initial idea into a research program. Start with [[00 Project/Research map]], then read [[00 Project/Working definition and assumptions]] and [[01 Concepts/Bridge matrix]].

Executable work has been decomposed into bounded cards in the sibling [delivery plan](../plan/README.md). This directory remains the knowledge base and can be opened directly as an Obsidian vault.

## What the research currently says

The project now has two equally important lines of prior art. Multilevel interpolation methods fit a coarse component, evaluate the residual at observations, fit that residual at a finer scale, and sum the corrections. Variational analysis methods interpret observations as anomalies from a background and reconstruct them using a covariance or its inverse differential operator. The strongest matches found so far are:

- [[02 Papers/Lee 1997 - Multilevel B-splines]]
- [[02 Papers/Narcowich Schaback Ward 1999 - Multilevel interpolation]]
- [[02 Papers/Wendland 2010 - Multiscale RBF approximation]]
- [[02 Papers/Georgoulis 2013 - Multilevel sparse kernel interpolation]]
- [[02 Papers/Ding 2023 - HINT]]
- [[02 Papers/Barth 2014 - DIVAnd]]

DIVAnd is particularly important because its derivative penalty has an explicit Fourier spectrum proportional to ((1+|k|^2)^{-m}). It therefore connects the spectral-kernel idea, regularized interpolation, kriging, and a practical multidimensional solver. See [[01 Concepts/Variational analysis and precision operators]].

Wavelet multiresolution analysis supplies a clean mathematical language for nested approximation spaces and detail spaces. Renormalization supplies a useful comparison about scale flow, but the direction and semantics differ. See [[01 Concepts/Renormalization comparison]].

## Vault structure

- [[00 Project/Research map]]: navigation and current synthesis
- [[00 Project/Working definition and assumptions]]: explicit mathematical placeholder for the proposed method
- [[00 Project/Hypothesis ledger and decision rules]]: preregistered claims, nulls, tests, thresholds, and consequences
- [[00 Project/Next steps]]: gated execution order
- [[01 Concepts/Bridge matrix]]: what is genuinely shared across fields and what is only analogous
- [[02 Papers/Paper index]]: primary literature with reading priorities
- [[03 Code/Code index]]: reusable implementations and what each can test
- [[04 Investigations/Investigation index]]: bounded briefs for smaller models
- [[05 Experiments/Experimental program]]: prototype and benchmark plan
- [[06 Sources/Bibliography]]: canonical links and citation metadata
- [[06 Sources/Search log]]: queries, scope, and gaps

## Status

This is a scaffold, not a novelty claim. The name "successive anomaly interpolation" has not yet been tied to a precise algorithm in the supplied material. The vault therefore separates established facts, working assumptions, and conjectures, and uses [[00 Project/Hypothesis ledger and decision rules]] to prevent post-hoc success criteria.
