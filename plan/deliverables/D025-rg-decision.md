# D025 — Decide whether an RG mapping exists

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D004, D020
- **Hypotheses:** H11
- **Verification classes:** V1, V2, V4

## Objective

Attempt an explicit mapping among interpolation stages, coarse-graining, rescaling, and parameter flow.

## Procedure

1. Define the interpolation state, scale transformation, and direction of stage flow.
2. Define candidate fine-degree elimination or introduction operator.
3. Define rescaling and effective parameters.
4. Write a diagram containing every space and operator.
5. Test whether each square commutes exactly, approximately with a bound, or not at all.
6. Evaluate the mapping on a Gaussian/free solvable example.
7. Compare with wavelet conditional RG and ordinary MRA without borrowing their conclusions.
8. Issue the H11 verdict and an allowed-vocabulary list.

## Required checks

- Verify all operators have compatible domains and codomains.
- Produce the smallest explicit mismatch if the diagram fails.

## Machine verification

`pixi run verify-card -- D025` must type-check every formalized diagram, compile commuting claims, and reproduce numeric witnesses or counterexamples.

## Primary artifact

`theory/rg-verdict.md` containing a commuting diagram or the smallest decisive mismatch.

## Acceptance

- Degrees of freedom and direction of scale flow are explicit.
- Exact, approximate, dual, and metaphorical relationships are distinguished.
- H11 receives a pass, fail, or inconclusive verdict.

## Failure or escalation

If only a multiscale analogy remains, remove RG from the technical framing.
