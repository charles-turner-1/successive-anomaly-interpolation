# D000G — Establish the Lean verification foundation

- **State:** blocked
- **Owner:** unassigned
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Depends on:** D000A, D000B
- **Hypotheses:** infrastructure for H0–H5 and H11
- **Verification classes:** V1, V2
- **Source policy:** [Toolchain policy](../toolchain-policy.md)

## Objective

Create and prove the pinned Lean/Lake project used by later formal-verification cards.

## Work

1. Add `lean-toolchain`, `formal/lakefile.toml` or `formal/lakefile.lean`, and a pinned `formal/lake-manifest.json`.
2. Add one minimal theorem and its plain-language symbol correspondence.
3. Add checks rejecting `sorry`, `admit`, unexpected axioms, and dirty dependency resolution.
4. Wire `pixi run verify-formal` to the pinned toolchain.

## Required checks

- Build the theorem from a clean Lake cache.
- Confirm dedicated fixtures reject `sorry`, `admit`, an unexpected axiom, and a mismatched manifest.
- Confirm the build uses the committed Lean toolchain revision.

## Machine verification

`pixi run verify-card -- D000G` must report the toolchain revision, Lake manifest hash, theorem build, and negative-fixture verdicts.

## Primary artifact

The pinned `formal/` Lean/Lake project.

## Acceptance

- The clean proof compiles without admitted axioms.
- Toolchain and mathlib revisions are committed and reproducible.
- Every prohibited proof shortcut has an expected-failure fixture.

## Failure or escalation

If the selected Lean and mathlib revisions cannot resolve together, preserve the resolver output and block D000.

## Completion packet

Follow the [execution protocol](../execution-protocol.md).
