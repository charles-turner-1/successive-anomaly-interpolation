# D047 — Run adversarial failure cases

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D041
- **Hypotheses:** H2, H3, H7
- **Verification classes:** V2, V3

## Objective

Find the smallest counterexamples involving noise, close frequencies, clustered samples, holes, duplicates, discontinuities, outliers, and distance concentration.

## Procedure

1. Encode each adversarial family as a parameterized generator.
2. Define the claim and violation predicate targeted by each family.
3. Search a frozen parameter domain systematically or with a deterministic property-based seed.
4. When a violation appears, minimize it using automated shrinking or bisection.
5. Re-run the minimized case across implementations and numeric precision where applicable.
6. Store the smallest fixture, trace, and violated criterion.
7. Build a safe operating envelope from passed and failed regions without claiming untested space.

## Required checks

- Include deliberate known-bad algorithms to verify each detector fires.
- Reproduce minimized counterexamples independently.

## Machine verification

`pixi run verify-card -- D047` must regenerate every saved counterexample and assert its violation predicate.

## Primary artifact

`reports/adversarial-suite.md` with one minimized counterexample per failed claim and a safe operating envelope.

## Acceptance

- Training and held-out behavior are both shown.
- Coefficient growth, cancellation, conditioning, and spectral leakage are recorded.
- Negative results update the evidence ledger.

## Failure or escalation

An inability to find a counterexample is not proof; report the tested envelope and search budget.
