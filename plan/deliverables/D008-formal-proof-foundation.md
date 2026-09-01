# D008 — Establish the formal proof foundation

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D000, D003, D004
- **Hypotheses:** H1, H4, H5, H7, H9, H11
- **Verification classes:** V1, V2

## Objective

Create Lean definitions corresponding to the finite-dimensional linear core of the estimator and prove the first foundational lemmas.

## Procedure

1. Define finite-dimensional state and observation spaces over the reals.
2. Define (H), stage operators, residual update, correction accumulation, and a finite stage list.
3. Prove type and dimension-correct forms of the one-stage residual identity.
4. Prove the two-stage expansion.
5. State, but do not yet assume, conditions needed for convergence, PSD mixtures, and nested projections.
6. Create a symbol-correspondence document mapping Lean definitions to D003/D004.
7. Add linting that rejects `sorry`, `admit`, and unexpected axioms.

## Primary artifact

A compiling Lean project, foundational definitions and lemmas, correspondence document, and `verification/D008.yaml`.

## Required checks

- Compile from a clean environment.
- Print axioms for exported theorems and compare them with the allowed list.
- Cross-check the two-stage theorem against D005 numerically.

## Machine verification

`pixi run verify-formal` must compile all declarations with no `sorry` and produce an allowed-axiom report.

## Acceptance

- Formal objects match the written specification.
- One- and two-stage identities are proved.
- No untracked axioms or admitted goals remain.

## Failure or escalation

If the estimator is nonlinear, formalize the linear core and name the extra assumptions needed; do not encode false linearity.
