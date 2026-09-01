# D013 — Build the direct prior-art matrix

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D004
- **Hypotheses:** H12
- **Verification classes:** V4

## Objective

Compare the frozen recurrence line by line with DIVAnd, multilevel B-splines, multiscale RBFs, HINT, boosting, matching pursuit, and diffusion methods.

## Procedure

1. Freeze a comparison schema before filling any rows.
2. For each method, read the primary paper sections defining its objective and recurrence.
3. Extract state space, residual, stage operator, scale rule, fitting order, regularization, stopping, uncertainty, and theorem assumptions.
4. Rewrite each method in the D004 notation where legitimate.
5. Mark each field exact match, conditional match, analogy, mismatch, or unknown.
6. For every exact/conditional match, write the conditions and one example where they fail.
7. Link official code and license information separately from the mathematical comparison.

## Required checks

- A second model audits every “exact match” against the cited equation.
- No row may infer operator equivalence from similar prose alone.

## Machine verification

`pixi run verify-card -- D013` must schema-validate all rows, resolve source identifiers, and ensure every match label has the required equation and audit fields.

## Primary artifact

`research/prior-art-matrix.md` with operator, scale, residual, objective, theorem, and decisive-difference columns.

## Acceptance

- Every row cites a primary paper and official code when available.
- Similarity is separated from exact equivalence.
- Unknowns and negative searches remain visible.

## Failure or escalation

An exact predecessor is a successful deliverable with an H12 failure candidate.
