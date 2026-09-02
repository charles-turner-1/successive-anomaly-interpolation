# Delivery plan

This directory turns the broad research investigations in the [vault](../vault/README.md) into small, reviewable deliverables.

## Rules

- Every implementing model must follow the [execution protocol](execution-protocol.md).
- One card produces one primary artifact or decision.
- A card is not done because research was attempted; its acceptance criteria must be met.
- Scientific claims use the thresholds in the [hypothesis ledger](../vault/00%20Project/Hypothesis%20ledger%20and%20decision%20rules.md).
- Confirmatory work cannot start before [D041](deliverables/D041-freeze-preregistration.md).
- Failed and inconclusive results are valid deliverables when the evidence and consequence are recorded.
- Update the [status board](status.md) when a card changes state.
- There is no time or token budget. Continue until acceptance, a scientific failure result, or a concrete blocker.

## Bounded-agent handoff for D000

- Assign only one D000 subcard to a model session.
- Supply that card, the execution protocol, its linked policy, and its direct dependency artifacts; do not preload unrelated vault material.
- Keep each session in an isolated branch or worktree and forbid cross-card edits.
- Require the execution log before implementation and a final packet containing state, commit, checks, artifacts, and blockers.
- Treat no-tool model output as review material only; an implementing agent must integrate and machine-check it before it changes card state.
- After D000I exists, replay every earlier foundation manifest through `pixi run verify-card -- ID` before D000 integration.

## Execution phases

| Phase | Purpose | Deliverables | Exit condition |
|---|---|---|---|
| Foundation | Make every output machine-verifiable | D000A–D000J, D000, D007–D009 | Verification gate active |
| 0. Specification | Make the method reproducible | D001–D006 | H0 and H1 decided |
| 1. Prior art and equivalence | Bound what is already known | D010–D015 | Comparator set and novelty boundary fixed |
| 2. Theory | Derive only the claims the method needs | D020–D025 | Scale, stability, uncertainty, MRA, and RG claims bounded |
| 3. Prototype | Build interchangeable estimators and harness | D030–D036 | End-to-end deterministic run |
| 4. Evidence | Smoke-test, freeze, and run confirmation | D040–D048 | H2–H10 decided as applicable |
| 5. Synthesis | Decide the surviving contribution | D050–D053 | H12 decision and reproducible release |

## Deliverable index

### Foundation — Machine verification

- [D000A — Define the verification repository layout](deliverables/D000A-repository-layout.md)
- [D000B — Establish the Pixi and Python foundation](deliverables/D000B-pixi-python-foundation.md)
- [D000C — Define the verification-manifest schema](deliverables/D000C-manifest-schema.md)
- [D000D — Implement manifest validation](deliverables/D000D-manifest-validator.md)
- [D000E — Validate artifacts, hashes, and commands](deliverables/D000E-artifact-command-validation.md)
- [D000F — Establish the Julia verification foundation](deliverables/D000F-julia-foundation.md)
- [D000G — Establish the Lean verification foundation](deliverables/D000G-lean-foundation.md)
- [D000H — Enforce the conditional Rust policy](deliverables/D000H-rust-conditional-guard.md)
- [D000I — Implement canonical verification dispatch](deliverables/D000I-verification-dispatch.md)
- [D000J — Prove CI and clean-checkout verification](deliverables/D000J-ci-clean-checkout.md)
- [D000 — Integrate the verification architecture](deliverables/D000-verification-architecture.md)
- [D007 — Encode machine-readable specification contracts](deliverables/D007-machine-readable-specification.md)
- [D008 — Establish the formal proof foundation](deliverables/D008-formal-proof-foundation.md)
- [D009 — Enforce continuous verification](deliverables/D009-continuous-verification.md)

### Phase 0 — Specification

- [D001 — Freeze vocabulary](deliverables/D001-freeze-vocabulary.md)
- [D002 — Specify data and observation model](deliverables/D002-data-observation-model.md)
- [D003 — Specify one stage operator](deliverables/D003-stage-operator.md)
- [D004 — Specify the full estimator](deliverables/D004-full-estimator.md)
- [D005 — Hand-compute a two-level example](deliverables/D005-hand-example.md)
- [D006 — Independent reproduction check](deliverables/D006-independent-reproduction.md)

### Phase 1 — Prior art and equivalence

- [D010 — Extract the DIVAnd operator](deliverables/D010-divand-operator.md)
- [D011 — Derive fixed-operator succession](deliverables/D011-fixed-operator-recurrence.md)
- [D012 — Specify the joint multiscale comparator](deliverables/D012-joint-multiscale-comparator.md)
- [D013 — Build the direct prior-art matrix](deliverables/D013-prior-art-matrix.md)
- [D014 — Run terminology and citation searches](deliverables/D014-terminology-citation-search.md)
- [D015 — Write the provisional novelty boundary](deliverables/D015-novelty-boundary.md)

### Phase 2 — Theory

- [D020 — Derive the spectral kernel](deliverables/D020-spectral-derivation.md)
- [D021 — Define the stage-scale diagnostic](deliverables/D021-stage-scale-diagnostic.md)
- [D022 — Test nested-space claims](deliverables/D022-nested-space-tests.md)
- [D023 — Derive stability and stopping conditions](deliverables/D023-stability-stopping.md)
- [D024 — Specify uncertainty propagation](deliverables/D024-uncertainty-propagation.md)
- [D025 — Decide whether an RG mapping exists](deliverables/D025-rg-decision.md)

### Phase 3 — Prototype

- [D030 — Implement benchmark generators](deliverables/D030-benchmark-generators.md)
- [D031 — Define the common result schema](deliverables/D031-result-schema.md)
- [D032 — Implement one-stage baselines](deliverables/D032-one-stage-baselines.md)
- [D033 — Implement successive anomaly analysis](deliverables/D033-successive-estimator.md)
- [D034 — Implement the joint multiscale baseline](deliverables/D034-joint-multiscale-baseline.md)
- [D035 — Implement multilevel RBF correction](deliverables/D035-multilevel-rbf-baseline.md)
- [D036 — Build the reproducible experiment runner](deliverables/D036-experiment-runner.md)

### Phase 4 — Evidence

- [D040 — Run smoke tests](deliverables/D040-smoke-tests.md)
- [D041 — Freeze preregistration](deliverables/D041-freeze-preregistration.md)
- [D042 — Run the core confirmatory comparison](deliverables/D042-core-confirmatory.md)
- [D043 — Run the DIVAnd equivalence experiment](deliverables/D043-divand-equivalence.md)
- [D044 — Test geometry and physical constraints](deliverables/D044-geometry-constraints.md)
- [D045 — Test uncertainty calibration](deliverables/D045-uncertainty-calibration.md)
- [D046 — Measure high-dimensional scaling](deliverables/D046-high-dimensional-scaling.md)
- [D047 — Run adversarial failure cases](deliverables/D047-adversarial-suite.md)
- [D048 — Run order and ablation tests](deliverables/D048-order-ablations.md)

### Phase 5 — Synthesis

- [D050 — Populate the evidence ledger](deliverables/D050-evidence-ledger.md)
- [D051 — Write the continuation decision](deliverables/D051-continuation-decision.md)
- [D052 — Complete the final novelty search](deliverables/D052-final-novelty-search.md)
- [D053 — Package the reproducible release](deliverables/D053-reproducible-release.md)

## Navigation

- [Roadmap and dependencies](roadmap.md)
- [Status board](status.md)
- [Deliverable template](deliverable-template.md)
- [Execution protocol](execution-protocol.md)
- [Machine-verification policy](verification-policy.md)
- [Toolchain and package-management policy](toolchain-policy.md)
- [Mapping from old investigation briefs](investigation-map.md)
