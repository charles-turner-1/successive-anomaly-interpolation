# Successive Anomaly Interpolation

This repository is an experiment in using long-running, machine-checked agent loops to investigate what looks like an interpolatable gap in the mathematics of field reconstruction.

The tentative idea is simple: begin with a background field, measure what the observations say is still missing, interpolate that anomaly at an appropriate scale, add the correction to the background, and repeat. The difficult part is determining whether this procedure is:

- a genuinely useful estimator;
- an established multilevel interpolation method in unfamiliar language;
- an iterative route to an ordinary variational solution;
- an implicit regularization path;
- or a suggestive idea that fails under careful analysis.

This repository is designed to accept any of those outcomes.

## The mathematical question

Suppose observations $y$ are related to a field $b$ through an observation operator $H$. A candidate successive analysis has the form

\[
a_\ell = y-Hb_{\ell-1},
\qquad
g_\ell=A_\ell a_\ell,
\qquad
b_\ell=b_{\ell-1}+\eta_\ell g_\ell.
\]

Here $a_\ell$ is the current anomaly, $A_\ell$ is an interpolation or analysis operator, and $\eta_\ell$ controls the update. The operator might change its correlation length, spectral support, rank, geometry, regularization, or physical constraints from one level to the next.

Many individual pieces are already well developed:

- multilevel splines and radial-basis interpolation fit residuals from coarse to fine;
- wavelets and multiresolution analysis decompose fields into scale-dependent components;
- variational analysis, kriging, and Gaussian processes reconstruct noisy observations using covariance models;
- DIVAnd expresses a covariance kernel through a differential precision operator on multidimensional, constrained domains;
- diffusion operators and Whittle–Matérn covariances connect local differential penalties to global spectral behavior;
- boosting, matching pursuit, and iterative regularization repeatedly reduce residuals.

The possible gap is not “nobody has ever fitted a residual twice.” It is whether these pieces admit a useful unified construction in which successive background anomalies, changing scale, multidimensional geometry, uncertainty, and spectral interpretation all fit together—with an advantage that survives comparison against a single optimal variational solve and a jointly fitted multiscale covariance.

That gap may close into an existing method once the operators are written precisely. Finding that out is part of the experiment.

## Why agent loops?

This project also tests a research process.

The work has been decomposed for agents that can spend a great deal of time on a problem but should not be trusted to fill conceptual gaps through intuition. Each agent receives a bounded deliverable with:

- explicit inputs and dependencies;
- an ordered procedure;
- one primary artifact;
- executable checks;
- scientific success and failure criteria;
- and a required consequence for each verdict.

The intended loop is:

```text
research → specify → formalize → implement → test → falsify → synthesize
     ↑                                                        │
     └──────────────── evidence and unresolved questions ─────┘
```

Agents are allowed to return negative results. They are not allowed to redefine success after seeing the output.

## Machine-checking and formal verification

Every completed deliverable must have a machine-executable verifier. Different claims require different notions of verification:

- mathematical identities and finite-dimensional operator claims are candidates for Lean proofs;
- implementations and numerical properties use deterministic Python, Julia, and cross-language tests;
- empirical performance claims use frozen statistical decision programs over immutable results;
- literature, license, and novelty claims use schema-validated provenance records and reproducible searches.

Formal proof cannot establish that a model describes nature, and a literature audit cannot prove that no unknown precedent exists. The verification system is meant to make assumptions, computations, evidence, and decisions inspectable—not to erase those limits.

The planned toolchain uses Pixi for Python and task orchestration, project-local Julia environments for DIVAnd work, Cargo if Rust is justified, and a pinned Lean/Lake environment for proofs. Global project dependency installation is prohibited.

## What would count as success?

The strongest outcome would be a precisely defined successive estimator that:

1. is mathematically nonredundant;
2. has a defensible scale interpretation;
3. is stable under observation and numerical perturbations;
4. improves accuracy, calibration, or computational cost under matched budgets;
5. beats or complements a single tuned variational analysis and a joint multiscale covariance;
6. handles geometry or physical constraints in a way simpler baselines cannot;
7. and occupies a clearly documented position relative to existing literature.

A useful weaker outcome could be a new continuation strategy, a formally clarified equivalence, a synthesis connecting spectral kernels to variational analysis, or a well-documented negative result.

Failure includes discovering that repeated passes merely reduce effective regularization, fit noise, reproduce a known method at greater cost, or support only metaphorical links to multiresolution or renormalization. Those conclusions are valuable if they are demonstrated cleanly.

## Repository structure

The repository separates research context from executable work:

- [vault/](vault/README.md) is the research knowledge base: concepts, papers, code references, hypotheses, benchmark ideas, and the original high-level investigation briefs. It can be opened directly as an Obsidian vault.
- [plan/](plan/README.md) is the delivery system: 42 bounded work packages, dependencies, procedures, acceptance criteria, and verification requirements.

Useful entry points:

- [Research map](vault/00%20Project/Research%20map.md)
- [Working definition and unresolved assumptions](vault/00%20Project/Working%20definition%20and%20assumptions.md)
- [Hypothesis ledger and decision rules](vault/00%20Project/Hypothesis%20ledger%20and%20decision%20rules.md)
- [Delivery roadmap](plan/roadmap.md)
- [Execution protocol for agents](plan/execution-protocol.md)
- [Machine-verification policy](plan/verification-policy.md)
- [Toolchain and package-management policy](plan/toolchain-policy.md)
- [Investigation-to-deliverable map](plan/investigation-map.md)

## Current status

The project is at verification-foundation and specification lock. It does not yet claim a new algorithm.

The first deliverable is [D000 — Establish the verification architecture](plan/deliverables/D000-verification-architecture.md). It creates the Pixi environment, schemas, language-specific project environments, Lean foundation, continuous verification, and the canonical `pixi run verify` interface. The mathematical vocabulary and estimator are then frozen through D001–D006 before confirmatory implementation begins.

## Contributions and critique

The most useful contributions at this stage are precise counterexamples, operator equivalences, missing primary literature, corrections to assumptions, formalization improvements, and reproducible implementations of the planned baselines.

If the proposed gap is already filled, the best contribution is to identify exactly where, write the operator correspondence, and demonstrate it. If it is not, the same machinery should leave a narrow and testable statement of what remains.
