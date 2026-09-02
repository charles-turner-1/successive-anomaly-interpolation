# D000D — Implement manifest validation

- **State:** blocked
- **Owner:** unassigned
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Depends on:** D000B, D000C
- **Hypotheses:** infrastructure for H0–H12
- **Verification classes:** V2

## Objective

Implement the deterministic CLI that validates verification manifests against the D000C schema and emits stable diagnostics.

## Work

1. Implement one Python manifest-validation entry point.
2. Return nonzero for every invalid fixture and zero for valid fixtures.
3. Emit machine-readable results plus concise human diagnostics containing the manifest path and violated rule.
4. Add unit and CLI tests for every D000C fixture.

## Required checks

- Run all positive fixtures twice in clean processes.
- Run each negative fixture and assert its exact error code and diagnostic fragment.
- Confirm malformed YAML/JSON never produces a traceback-only failure.

## Machine verification

`pixi run verify-card -- D000D` must execute the validator test matrix and store its structured report.

## Primary artifact

The manifest-validator CLI module.

## Acceptance

- Every D000C fixture receives its expected verdict.
- Diagnostics are stable enough for CI assertions.
- Validation never mutates the manifest or artifact tree.

## Failure or escalation

If schema-library behavior differs across locked platforms, add a minimal reproducer and block until the divergence is resolved.

## Completion packet

Follow the [execution protocol](../execution-protocol.md).
