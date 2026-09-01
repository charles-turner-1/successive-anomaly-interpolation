# D022 — Test nested-space claims

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D003, D020
- **Hypotheses:** H9
- **Verification classes:** V1, V2

## Objective

Determine whether stage ranges are nested projections, quasi-projections, a stable frame, or merely filters on one state space.

## Procedure

1. Define the ambient space and the range of each stage operator.
2. Test range inclusion analytically; for finite discretizations compute ranks and principal angles.
3. Test idempotence and projection compatibility.
4. If projection claims fail, formulate the synthesis operator and test frame or decomposition bounds.
5. Examine changing centers separately from changing kernel scale.
6. Construct the smallest counterexample to each failed implication.
7. State exactly which MRA words remain licensed by the result.

## Required checks

- Verify finite computations under increasing precision and grid refinement.
- Have a second model check theorem assumptions and counterexamples.

## Machine verification

`pixi run verify-card -- D022` must compile proved claims, execute finite rank/angle/projection tests, and reproduce every counterexample.

## Primary artifact

`theory/nested-space-verdict.md` with range, idempotence, compatibility, and frame tests.

## Acceptance

- Every claimed property is proved, disproved, or reduced to a named open condition.
- A finite matrix counterexample is included for each false generic implication.
- Vocabulary is revised to match the verdict.

## Failure or escalation

Failure of nesting is an H9 result, not a reason to force new spaces into the construction.
