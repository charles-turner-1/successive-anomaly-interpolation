# D006 — Independent reproduction check

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D005
- **Hypotheses:** H0
- **Verification classes:** V2

## Objective

Have two independent implementations reproduce the hand case and one fixed-seed small dataset.

## Procedure

1. Freeze D001–D005 revisions and give them to two fresh implementation models.
2. Require different implementation languages or independently written modules.
3. Run both implementations on the hand fixture.
4. Generate one fixed-seed dataset from the written data specification and run both without exchanging outputs.
5. Compare every intermediate stage value, not only final predictions.
6. Classify discrepancies as specification, implementation, numerical, or environment errors.
7. Repair only the responsible layer and rerun both from clean state.

## Required checks

- Compute maximum absolute and relative discrepancies for every output field.
- Verify the implementations do not import or copy each other's estimator logic.

## Machine verification

`pixi run verify-card -- D006` must run both implementations in isolated processes and compute the H0 tolerance verdict automatically.

## Primary artifact

`reports/reproduction.md` with implementation hashes, outputs, discrepancies, and H0 verdict.

## Acceptance

- Agreement meets the H0 tolerances.
- Neither implementation imports the other's core estimator.
- All semantic questions are recorded and resolved in the specification.

## Failure or escalation

Return to the earliest ambiguous specification card; do not tune tolerances after inspecting discrepancies.
