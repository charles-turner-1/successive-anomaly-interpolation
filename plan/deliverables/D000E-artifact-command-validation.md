# D000E — Validate artifacts, hashes, and commands

- **State:** blocked
- **Owner:** unassigned
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Depends on:** D000B, D000C
- **Hypotheses:** infrastructure for H0–H12
- **Verification classes:** V2, V4

## Objective

Implement verification of declared artifact existence, stored hashes, command exit status, and prohibited global-install commands.

## Work

1. Implement path-safe artifact existence and digest checks.
2. Implement command execution with captured exit status, stdout, stderr, and bounded timeout.
3. Reject prohibited global installation commands defined by the toolchain policy.
4. Add one passing and one focused failing fixture for each validator.

## Required checks

- Detect a missing artifact, altered hash, nonzero command, timed-out command, path traversal, and prohibited install command.
- Confirm each failure names the relevant artifact or command and returns nonzero.
- Confirm valid checks are deterministic across two clean runs.

## Machine verification

`pixi run verify-card -- D000E` must run the complete validator fixture matrix and emit a structured report.

## Primary artifact

The artifact/hash/command validation module.

## Acceptance

- All declared failure modes have isolated fixtures.
- Command logs preserve enough information for audit without leaking environment secrets.
- Artifact paths cannot escape the repository root.

## Failure or escalation

If safe command execution cannot be bounded consistently on a supported platform, block that platform and record the exact limitation.

## Completion packet

Follow the [execution protocol](../execution-protocol.md).
