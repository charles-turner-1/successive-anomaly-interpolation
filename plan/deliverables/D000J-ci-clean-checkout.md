# D000J — Prove CI and clean-checkout verification

- **State:** blocked
- **Owner:** unassigned
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Depends on:** D000C, D000I
- **Hypotheses:** infrastructure for H0–H12
- **Verification classes:** V2, V4

## Objective

Configure continuous verification and prove that a local clean checkout and CI execute the same locked foundation checks.

## Work

1. Add CI configuration that installs pinned Pixi and runs bootstrap plus repository verification.
2. Add a clean-checkout harness that excludes mutable environment directories and uses only committed declarations and lockfiles.
3. Record local and CI toolchain identities and structured verification outputs.
4. Produce `verification/D000J.yaml` with links or hashes for both runs.

## Required checks

- Run the clean-checkout harness locally from a temporary clone or worktree.
- Confirm CI runs on every change and fails when a known negative fixture is promoted to the active manifest set.
- Compare task names, toolchain versions, and final verdicts between local and CI reports.

## Machine verification

`pixi run verify-card -- D000J` must validate the workflow, clean-run report, CI evidence, and their declared equivalence fields.

## Primary artifact

The CI workflow and paired clean-checkout verification report.

## Acceptance

- CI and local clean verification use the same committed task surface.
- Mutable caches are not treated as authoritative artifacts.
- A deliberate active failure makes both environments fail.

## Failure or escalation

If the hosted CI platform cannot provide a required pinned toolchain, preserve the failing job evidence and keep D000 blocked until the platform matrix is resolved.

## Completion packet

Follow the [execution protocol](../execution-protocol.md).
