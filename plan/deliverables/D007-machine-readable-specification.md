# D007 — Encode the specification as machine-readable contracts

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D000, D002, D004
- **Hypotheses:** H0, H1
- **Verification classes:** V2

## Objective

Translate the glossary, shapes, data model, stage configuration, and full estimator configuration into schemas and executable contracts.

## Procedure

1. Enumerate every object and invariant in D001–D004.
2. Create JSON Schemas for datasets, estimator configuration, stage configuration, and expected outputs.
3. Implement runtime shape, unit, range, and information-boundary checks not expressible in JSON Schema.
4. Encode D005 as a canonical fixture.
5. Generate valid boundary cases and one invalid case per constraint.
6. Ensure error messages name the violated specification clause.

## Primary artifact

Versioned schemas, contract validators, fixtures, and `verification/D007.yaml`.

## Required checks

- Property-generate valid and invalid configurations.
- Confirm every written invariant is linked to at least one executable check.

## Machine verification

`pixi run verify-schemas` must accept all canonical valid fixtures and reject every invalid fixture for the expected reason.

## Acceptance

- No configurable estimator choice remains prose-only.
- The hand example passes contracts.
- All constraint branches have tests.

## Failure or escalation

If a concept cannot be encoded, return to the responsible specification card and make it operational.
