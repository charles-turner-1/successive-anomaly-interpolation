# D031 — Define the common result schema

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D002
- **Hypotheses:** H2–H10
- **Verification classes:** V2

## Objective

Ensure every estimator emits comparable predictions, diagnostics, resources, and provenance.

## Procedure

1. Enumerate required outputs from H2–H10 and every planned report.
2. Define scalar, array, per-stage, uncertainty, resource, warning, and provenance fields.
3. Specify units, shapes, nullable behavior, numeric precision, and canonical ordering.
4. Implement JSON Schema plus binary-array storage conventions and content hashes.
5. Write serializer/deserializer pairs in every implementation language used.
6. Create minimal, maximal, and invalid fixtures.
7. Define forward-compatible schema versioning and migration rejection rules.

## Required checks

- Round-trip every fixture without semantic change.
- Cross-language readers must agree on shapes, values, and hashes.

## Machine verification

`pixi run verify-card -- D031` must validate fixtures and reject each malformed result with its expected error code.

## Primary artifact

`spec/result-schema.md` plus serialization and validation code.

## Acceptance

- Schema covers per-stage corrections, residuals, uncertainty, hyperparameters, time, memory, solver diagnostics, code revision, and seed.
- Missing capabilities are explicit nulls, not omitted fields.
- A round-trip serialization test passes.

## Failure or escalation

Estimator-specific extensions are allowed only under a namespaced field.
