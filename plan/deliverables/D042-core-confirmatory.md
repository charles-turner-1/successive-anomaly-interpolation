# D042 — Run the core confirmatory comparison

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D041
- **Hypotheses:** H2, H3, H7
- **Verification classes:** V3

## Objective

Compare successive, one-stage, joint multiscale, and multilevel RBF estimators on the frozen core suite.

## Procedure

1. Verify D041 hash and clean execution environment.
2. Expand the declared run matrix and compare it with expected run count.
3. Execute all runs without inspecting aggregate outcomes midstream.
4. Validate and hash each raw result.
5. Run the frozen decision programs for H2, H3, and H7.
6. Generate tables and figures entirely from immutable results.
7. Emit machine-readable verdicts and a prose rendering from the same values.
8. Account for every failed, missing, and excluded run under the frozen rule.

## Required checks

- Recompute decisions in a fresh process from raw results only.
- Confirm prose numbers equal machine-readable values.
- Confirm no smoke or test-forbidden information appears in fit logs.

## Machine verification

`pixi run verify-card -- D042` must reproduce all verdict files and report pass/fail/inconclusive without manual inputs.

## Primary artifact

`reports/core-confirmatory.md`, raw immutable results, and paired uncertainty estimates.

## Acceptance

- All manifest runs are accounted for.
- Accuracy and resources are matched and reported together.
- H2, H3, and H7 receive pass, fail, or inconclusive verdicts without threshold changes.

## Failure or escalation

Unexpected failures count under the preregistered rule; exploratory diagnosis belongs in a separate run set.
