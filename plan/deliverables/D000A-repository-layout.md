# D000A — Define the verification repository layout

- **State:** ready
- **Owner:** unassigned
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Depends on:** none
- **Hypotheses:** infrastructure for H0–H12
- **Verification classes:** V2, V4
- **Source policy:** [Toolchain policy](../toolchain-policy.md)

## Objective

Create and document the directory conventions that every later verification card will use.

## Work

1. Create directories for Python source and tests, Julia source and tests, Lean proofs, schemas, verification manifests, raw results, and reports.
2. Add tracked placeholders only where Git would otherwise omit an intentionally empty directory.
3. Document each path, its permitted contents, and naming rules in `docs/verification-layout.md`.
4. Add a deterministic layout check that reports missing or unexpected required paths.

## Required checks

- Run the layout check once against the valid tree.
- Run it against a fixture with one required path missing and confirm a nonzero exit with the path named.

## Machine verification

`pixi run verify-card -- D000A` must validate the layout record and both fixtures once D000I provides dispatch.

## Primary artifact

`docs/verification-layout.md`.

## Acceptance

- Every required path has one documented purpose and owner class.
- The valid and missing-path fixtures behave deterministically.
- No project dependency is installed globally.

## Failure or escalation

If two planned artifact classes require incompatible ownership or naming rules, record the conflict and block before creating parallel conventions.

## Completion packet

Follow the [execution protocol](../execution-protocol.md).
