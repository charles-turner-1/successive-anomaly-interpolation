# D000F — Establish the Julia verification foundation

- **State:** blocked
- **Owner:** unassigned
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Depends on:** D000A, D000B
- **Hypotheses:** infrastructure for H4–H10
- **Verification classes:** V2
- **Source policy:** [Toolchain policy](../toolchain-policy.md)

## Objective

Create and prove the project-local Julia environment required for later DIVAnd and numerical verification.

## Work

1. Add `julia/Project.toml` with explicit compatibility bounds and the minimal test target.
2. Resolve and commit `julia/Manifest.toml`.
3. Add a deterministic Julia smoke test and a check that the active project is the committed `julia/Project.toml`.
4. Wire `pixi run verify-julia` without relying on Julia's default environment or startup file.

## Required checks

- Instantiate with `julia --project=julia` from a clean depot fixture.
- Run the Julia test target twice.
- Confirm the wrong-active-project fixture fails with a clear diagnostic.

## Machine verification

`pixi run verify-card -- D000F` must report the Julia version, project path, manifest hash, and test result.

## Primary artifact

The pinned `julia/Project.toml` and `julia/Manifest.toml` environment bundle.

## Acceptance

- Julia resolves exclusively through the committed local project.
- Compatibility bounds and the manifest are committed.
- No source or test calls `Pkg.add`.

## Failure or escalation

If Julia or a required package cannot be pinned on a supported platform, capture the resolver output and block D000.

## Completion packet

Follow the [execution protocol](../execution-protocol.md).
