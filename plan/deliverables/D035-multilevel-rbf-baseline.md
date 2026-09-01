# D035 — Implement multilevel RBF correction

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D030, D031
- **Hypotheses:** H2, H12
- **Verification classes:** V2, V4

## Objective

Implement the closest classical coarse-to-fine residual-correction baseline.

## Procedure

1. Select one cited multilevel RBF recurrence from D013.
2. Translate its centers, support/bandwidth, regularization, and stopping to the common configuration.
3. Implement each level separately and expose intermediate corrections.
4. Preserve the cited ordering and add deviations only as named options.
5. Match total centers/features and validation information to D033.
6. Implement reference examples from the source where reproducible.
7. Record license and source provenance for reused code.

## Required checks

- Reproduce one published or analytically known example.
- Check residual update and center nesting properties.
- Verify source/license records validate under V4.

## Machine verification

`pixi run verify-card -- D035` must run numerical tests and provenance-schema validation.

## Primary artifact

Multilevel RBF module with documented scale, centers, regularization, and stopping schedule.

## Acceptance

- Recurrence matches a cited primary method or deviations are identified.
- Center and kernel budgets are comparable with D033.
- Per-level residuals and corrections use the common schema.

## Failure or escalation

If an existing maintained implementation is reused, pin its version and wrap rather than reimplementing silently.
