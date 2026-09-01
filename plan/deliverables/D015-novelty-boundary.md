# D015 — Write the provisional novelty boundary

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D011, D012, D013, D014
- **Hypotheses:** H12
- **Verification classes:** V4

## Objective

State the narrowest features not already accounted for by known methods.

## Procedure

1. List every feature in the frozen estimator.
2. Map each feature to matching prior-art rows from D013.
3. Remove features already disclosed alone or in the same operative combination.
4. For each survivor, state the smallest causal experiment or theorem showing consequence.
5. Classify the candidate as estimator, solver, regularizer, implementation, application, or synthesis contribution.
6. Write prohibited broader claims that the evidence cannot support.

## Required checks

- Trace every novelty sentence to a matrix cell and a planned hypothesis test.
- Ask an adversarial reviewer to identify overclaiming and record the response.

## Machine verification

`pixi run verify-card -- D015` must confirm every candidate and prohibited claim resolves to D013/D014 records and a planned hypothesis test.

## Primary artifact

`research/provisional-novelty.md` with one paragraph per candidate contribution and its required evidence.

## Acceptance

- No novelty claim rests on terminology alone.
- Every candidate feature maps to H2, H5, H8, H9, or H10.
- Equivalent known components are explicitly conceded.

## Failure or escalation

If no candidate remains, pivot the project to synthesis or comparative evaluation before more implementation.
