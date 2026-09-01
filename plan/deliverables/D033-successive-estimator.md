# D033 — Implement successive anomaly analysis

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D004, D030, D031
- **Hypotheses:** H1–H7
- **Verification classes:** V2

## Objective

Implement exactly the frozen estimator specification with inspectable per-level state.

## Procedure

1. Implement configuration parsing only through D007 contracts.
2. Implement initialization and one stage as separate pure or inspectable units.
3. Implement recurrence, damping, scale schedule, freezing/backfitting rule, and stopping in the specified order.
4. Emit a result record after every stage before proceeding to the next.
5. Preserve solver failures and warnings without converting them to silent NaNs.
6. Implement prediction at observation and target sites.
7. Run D005, randomized small linear cases, and all branch conditions.

## Required checks

- Compare every D005 intermediate against the golden fixture.
- Property-test the residual identity and deterministic replay.
- Use mutation tests or deliberate defects to show tests catch wrong update order, sign, damping, and stopping.

## Machine verification

`pixi run verify-card -- D033` must pass golden, property, branch, and mutation-sensitivity checks.

## Primary artifact

Successive estimator module and tests against D005.

## Acceptance

- Hand-example outputs meet H0 tolerances.
- Every correction, residual, scale, damping value, and stopping event is serialized.
- No test-set information enters fitting or stopping.

## Failure or escalation

Implementation-driven changes require a new specification revision and invalidate earlier confirmation manifests.
