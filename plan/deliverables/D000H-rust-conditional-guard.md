# D000H — Enforce the conditional Rust policy

- **State:** blocked
- **Owner:** unassigned
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Depends on:** D000A, D000B
- **Hypotheses:** infrastructure for later performance work if Rust is introduced
- **Verification classes:** V2, V4
- **Source policy:** [Toolchain policy](../toolchain-policy.md)

## Objective

Implement a guard that is a documented no-op when Rust is absent and enforces every locked-workspace requirement when Rust is present.

## Work

1. Define the repository condition that means Rust is present.
2. Implement checks for the workspace manifest, `Cargo.lock`, pinned toolchain/MSRV, `cargo fmt --check`, `cargo test --locked`, and `cargo clippy --locked -- -D warnings`.
3. Add an absent-Rust passing fixture and focused invalid Rust-workspace fixtures.
4. Wire the conditional behavior to `pixi run verify-rust`.

## Required checks

- Confirm the current no-Rust repository returns success with an explicit `not-applicable` record rather than silently skipping.
- Confirm fixtures fail for missing lockfile, missing toolchain/MSRV, and unlocked Cargo commands.

## Machine verification

`pixi run verify-card -- D000H` must report either a fully passing Rust toolchain or the explicit tested `not-applicable` state.

## Primary artifact

The conditional Rust policy checker and fixture set.

## Acceptance

- Absence of Rust is explicit and machine-readable.
- Presence of Rust activates every required locked check.
- No project task uses global `cargo install`.

## Failure or escalation

If Rust-presence detection is ambiguous, block and define a single repository marker before implementing checks.

## Completion packet

Follow the [execution protocol](../execution-protocol.md).
