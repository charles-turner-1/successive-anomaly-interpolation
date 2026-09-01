# D000 — Establish the verification architecture

- **State:** ready
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** none
- **Hypotheses:** infrastructure for H0–H12
- **Verification classes:** V2, V4

## Objective

Create the toolchain, directory conventions, manifest schema, and single command required to machine-check every later deliverable.

## Procedure

1. Implement the [toolchain policy](../toolchain-policy.md): root Pixi environment, project-local Julia Pkg environment, Lean/Lake project, and an optional locked Cargo workspace only if Rust is used.
2. Create directories for Python source/tests, Julia source/tests, Lean proofs, schemas, verification manifests, raw results, and reports.
3. Define the verification-manifest schema from the policy.
4. Implement validators for manifests, required artifacts, command exit status, and stored hashes.
5. Create every canonical Pixi task, including per-card dispatch and a conditional Rust verifier.
6. Add one deliberately passing and one deliberately failing fixture for each validator.
7. Configure CI to run the foundation checks on every change.
8. Produce D000's own verification manifest and verify it through the same interface.

## Primary artifact

A runnable verification skeleton with pinned toolchains, CI configuration, schemas, validators, and `pixi run verify`.

## Required checks

- Bootstrap and run verification from a clean checkout.
- Confirm each deliberate failing fixture causes a nonzero exit and clear diagnostic.
- Confirm no verifier silently skips a missing toolchain.
- Confirm Python imports resolve inside the Pixi prefix, Julia reports the committed active project, Lean uses the pinned toolchain, and Cargo uses `--locked` if present.

## Machine verification

Run `pixi run verify`; its structured report must list D000 as `done` and all negative fixtures as expected failures.

## Acceptance

- All canonical Pixi task entry points exist.
- Manifest validation is itself tested.
- CI and a local clean run agree.
- Toolchain versions and lockfiles are committed.
- No test or build command performs a global package installation.

## Failure or escalation

If one language cannot be pinned reproducibly, mark D000 blocked and resolve that toolchain before cards depending on it begin.
