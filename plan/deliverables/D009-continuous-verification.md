# D009 — Enforce continuous verification

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D000, D007, D008
- **Hypotheses:** H0–H12 infrastructure
- **Verification classes:** V1, V2, V3, V4

## Objective

Make it impossible to merge or release a completed card whose declared verifier fails or is absent.

## Procedure

1. Discover all `verification/*.yaml` manifests in CI.
2. Validate each manifest and run its commands in dependency order.
3. Enforce artifact existence and content hashes.
4. Fail if a card marked `done` lacks a manifest, verification output, or acceptance checklist.
5. Add caches without allowing cache hits to bypass execution.
6. Upload proof, test, statistical, and provenance reports as CI artifacts.
7. Test CI using branches/fixtures with a missing manifest, stale hash, failed theorem, failed test, and altered frozen threshold.

## Primary artifact

A CI verification gate and `verification/D009.yaml`.

## Required checks

- Every deliberate violation must fail CI for the expected reason.
- A clean repository must pass locally and in CI.

## Machine verification

The meta-test suite runs the deliberate violations in isolated fixtures and asserts nonzero status plus diagnostic codes.

## Acceptance

- Completion state and verifier state cannot disagree.
- Frozen confirmatory manifests are hash-protected.
- Verification reports are retained as build artifacts.

## Failure or escalation

If repository permissions cannot enforce branch protection, document the limitation; the CI gate must still fail visibly.
