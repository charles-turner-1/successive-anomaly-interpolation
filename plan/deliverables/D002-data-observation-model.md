# D002 — Specify data and observation model

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D001
- **Hypotheses:** H0
- **Verification classes:** V2

## Objective

Fix the domain, state, observations, observation operator, background, noise, masks, and target output.

## Procedure

1. Define the domain Ω and coordinate type for every in-scope variant.
2. Define state (x), observation locations, values (y), and observation operator (H).
3. Specify background (b_0), observation-error covariance (R), and any background covariance or precision (B^{-1}).
4. State how masks, periodic axes, missing values, duplicate sites, and off-grid sites are represented.
5. Create a symbol table with type, shape, units, allowed values, and source.
6. Define train, validation, test, and truth-only information boundaries.
7. Construct one valid and one invalid serialized example.

## Required checks

- Validate matrix and tensor shapes on the examples.
- Confirm that no test or truth-only value can enter fitting through the declared interfaces.

## Machine verification

`pixi run verify-card -- D002` must validate typed examples, reject invalid shapes/units, and pass information-boundary tests.

## Primary artifact

`spec/data-model.md` with typed symbols and a dimension/shape table.

## Acceptance

- Scalar and vector dimensions are explicit.
- Missing, noisy, periodic, and off-grid observations have declared behavior.
- Training, validation, and test information are separated.

## Failure or escalation

Create separate specifications if gridded and scattered cases require different algorithms.
