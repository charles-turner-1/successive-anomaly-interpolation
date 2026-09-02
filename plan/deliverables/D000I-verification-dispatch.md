# D000I — Implement canonical verification dispatch

- **State:** blocked
- **Owner:** unassigned
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Depends on:** D000B, D000D, D000E, D000F, D000G, D000H
- **Hypotheses:** infrastructure for H0–H12
- **Verification classes:** V2
- **Source policy:** [Verification policy](../verification-policy.md)

## Objective

Provide the canonical Pixi task surface and deterministic per-card dispatcher without reimplementing component validators.

## Work

1. Implement `verify-card -- ID` using D000D and D000E.
2. Wire `bootstrap`, `verify`, `verify-formal`, `verify-python`, `verify-julia`, `verify-rust`, `verify-schemas`, and `verify-links` in `pixi.toml`.
3. Define stable ordering, exit-code aggregation, and structured report output.
4. Add dispatch tests for valid, unknown, missing, passing, and failing card IDs.

## Required checks

- `pixi task list` exposes every canonical task exactly once.
- Every component task runs directly and through `pixi run verify`.
- An unknown or missing card ID fails without running unrelated cards.
- A component failure makes the aggregate command nonzero and appears in the report.

## Machine verification

`pixi run verify-card -- D000I` must exercise the dispatcher matrix and verify the canonical task list.

## Primary artifact

The per-card dispatcher and canonical Pixi task definitions.

## Acceptance

- Every policy-mandated command exists with deterministic behavior.
- Dispatch delegates to the component validators rather than duplicating them.
- Aggregate reports preserve each component's result and logs.

## Failure or escalation

If Pixi argument forwarding cannot implement the specified interface portably, record a minimal reproducer and propose one documented equivalent before changing the public command.

## Completion packet

Follow the [execution protocol](../execution-protocol.md).
