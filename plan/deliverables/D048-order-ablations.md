# D048 — Run order and ablation tests

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D041
- **Hypotheses:** H2, H3, H4, H5, H7
- **Verification classes:** V2, V3

## Objective

Measure which components matter and whether coarse-to-fine order is essential.

## Procedure

1. Enumerate one-factor ablations and define the unchanged control configuration.
2. Generate reversed, random, and sorted scale orders from frozen seeds.
3. Test damping, backfitting, exact/regularized stages, fixed/adaptive scales, and component removal separately.
4. Match tuning and compute budgets after each structural change.
5. Compute paired effects on primary error, resources, scale diagnostics, stability, and calibration.
6. Test component-order invariance where the corresponding joint model predicts it.
7. Run frozen hypothesis decision code and label undeclared interactions exploratory.

## Required checks

- Configuration diffs must prove only the intended factor changed.
- Repeat null ablations that should produce identical results.

## Machine verification

`pixi run verify-card -- D048` must validate configuration diffs, reproduce paired effects, and emit all declared verdicts.

## Primary artifact

`reports/ablations.md` covering reversed/random scale order, damping, backfitting, fixed scales, exact versus regularized fits, and matched component removal.

## Acceptance

- Each ablation changes one factor.
- Interaction effects are labeled exploratory unless preregistered.
- Order sensitivity is linked to the joint-versus-stagewise verdict.

## Failure or escalation

If no component matters independently, simplify the estimator before further claims.
