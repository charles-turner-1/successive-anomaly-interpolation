# D000C — Define the verification-manifest schema

- **State:** blocked
- **Owner:** unassigned
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Depends on:** D000A, D000B
- **Hypotheses:** infrastructure for H0–H12
- **Verification classes:** V2, V4
- **Source policy:** [Verification policy](../verification-policy.md)

## Objective

Translate the per-deliverable verification contract into one versioned machine-readable schema.

## Work

1. Enumerate required fields, state values, verification classes, toolchain records, commands, expected outputs, artifacts, hashes, hypotheses, and provenance.
2. Define the schema in `schemas/verification-manifest.schema.json`.
3. Add one smallest valid manifest and focused invalid fixtures for every rejection rule.
4. Document schema versioning and forward-compatibility rules.

## Required checks

- Confirm the valid fixture passes a standards-compliant JSON Schema validator.
- Confirm fixtures fail for unknown states, absent commands, unpinned toolchains, missing artifacts, and `done` without successful output.
- Confirm unknown top-level fields are handled according to the documented compatibility rule.

## Machine verification

`pixi run verify-card -- D000C` must report every positive and negative fixture with the expected verdict.

## Primary artifact

`schemas/verification-manifest.schema.json`.

## Acceptance

- Every field required by the verification policy is represented unambiguously.
- Each normative rejection rule has a dedicated fixture.
- Schema versioning behavior is documented and tested.

## Failure or escalation

If a policy requirement cannot be represented without prose interpretation, block and propose the smallest policy clarification.

## Completion packet

Follow the [execution protocol](../execution-protocol.md).
