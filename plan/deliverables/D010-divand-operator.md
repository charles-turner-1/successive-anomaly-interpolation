# D010 — Extract the DIVAnd operator

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D004
- **Hypotheses:** H4
- **Verification classes:** V1, V2, V4
- **Source:** [DIVAnd note](../../vault/03%20Code/DIVAnd.md)

## Objective

Write a DIVAnd solve as (g=A(L,R,C)a) in both grid-space and observation-space form.

## Procedure

1. Read the foundational paper, current API documentation, core call path, and minimal example.
2. Extract the cost function and define every matrix in repository terminology.
3. Derive grid-space normal equations.
4. Derive observation-space/dual form using the same symbols.
5. Map `mask`, metrics, coordinates, `f`, `len`, `epsilon2`, `alpha`, constraints, and solver choices to the equations.
6. Separate estimator-equivalent solver choices from options that change the estimator.
7. Trace background subtraction, returned field, residuals, and error covariance.

## Required checks

- Reproduce the documented four-dimensional call and annotate every argument.
- Verify primal and dual predictions agree on one small problem within solver tolerance.

## Machine verification

`pixi run verify-card -- D010` must validate source mappings, compile the finite operator statements, and pass Julia primal/dual comparison tests.

## Primary artifact

`theory/divand-operator.md` mapping mathematical objects to documented Julia arguments and outputs.

## Acceptance

- Normal equations, sampling operator, prior precision, and error covariance are explicit.
- Background subtraction/addition is shown.
- Solver approximations are separated from estimator definition.

## Failure or escalation

Document any behavior that cannot be inferred from the paper, docs, or a minimal source trace as an open code-reading task.
