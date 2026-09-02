# D000 — Integrate the verification architecture

- **State:** blocked
- **Owner:** unassigned
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D000A, D000B, D000C, D000D, D000E, D000F, D000G, D000H, D000I, D000J
- **Hypotheses:** infrastructure for H0–H12
- **Verification classes:** V2, V4

## Objective

Integrate the bounded D000 foundation cards and prove that the resulting verification architecture works from a clean checkout through one canonical command.

## Work

1. Confirm D000A–D000J are each complete with passing manifests.
2. Run the canonical bootstrap and repository-wide verification from a clean checkout.
3. Compare the local structured report with the CI result.
4. Produce D000's aggregate verification manifest and completion packet.
5. Mark D000 `done` only when every acceptance item below is evidenced.

## Required checks

- `pixi run bootstrap` succeeds from a clean checkout.
- `pixi run verify` reports every foundation component and D000 as passing.
- Every deliberate negative fixture fails with its expected diagnostic.
- No verifier silently skips a required toolchain.
- Python uses the Pixi prefix, Julia uses `julia/Project.toml`, Lean uses the pinned toolchain, and Cargo uses `--locked` when Rust is present.

## Machine verification

Run `pixi run verify-card -- D000`, then `pixi run verify`. Both commands must exit zero and the structured report must list D000 as `done`.

## Primary artifact

`verification/D000.yaml`, the aggregate manifest for the runnable verification architecture.

## Acceptance

- Every D000A–D000J manifest passes.
- All canonical Pixi task entry points exist and dispatch correctly.
- CI and a local clean run agree.
- Toolchain versions and required lockfiles are committed.
- No test or build command performs a global package installation.

## Failure or escalation

If any component cannot be pinned or verified reproducibly, keep D000 blocked and name the failing subcard. Do not bypass or weaken that subcard's acceptance criteria.

## Completion packet

Follow the [execution protocol](../execution-protocol.md): aggregate manifest, clean-run output, CI link, acceptance checklist, and open issues.
