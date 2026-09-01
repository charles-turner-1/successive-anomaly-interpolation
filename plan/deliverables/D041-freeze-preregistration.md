# D041 — Freeze preregistration

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D040
- **Hypotheses:** H2–H10 as applicable
- **Verification classes:** V2, V3, V4

## Objective

Freeze datasets, untouched seeds, splits, estimators, search budgets, primary metrics, thresholds, exclusions, and analysis code hashes.

## Procedure

1. Enumerate every active hypothesis and link it to exactly one primary decision program.
2. Generate untouched confirmation seeds without executing estimators on them.
3. Freeze dataset configurations, splits, estimator versions, search spaces, budgets, metrics, thresholds, exclusions, and stopping rules.
4. Freeze the analysis code revision and expected result schema.
5. Store smoke-seed deny lists.
6. Canonicalize and hash the manifest.
7. Make confirmation code reject a changed hash, dirty tree, smoke seed, or undeclared run.
8. Obtain an independent schema and logic review before setting state to done.

## Required checks

- Mutate each frozen field and confirm verification fails.
- Attempt to insert a smoke seed and undeclared metric and confirm rejection.

## Machine verification

`pixi run verify-card -- D041` must validate the canonical manifest, mutation tests, untouched-seed policy, and decision-program bindings.

## Primary artifact

Versioned `experiments/confirmation-manifest` committed before confirmatory execution.

## Acceptance

- Every active hypothesis has a primary test and consequence.
- Smoke-test seeds are excluded.
- The manifest validates and references immutable code revisions.

## Failure or escalation

Any later change marks affected results exploratory and requires a new untouched confirmation set.
