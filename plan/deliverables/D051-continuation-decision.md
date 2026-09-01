# D051 — Write the continuation decision

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D050
- **Hypotheses:** H2, H4, H5, H9, H11
- **Verification classes:** V3, V4

## Objective

Choose whether to pursue, modify, merge, narrow, or drop the method.

## Procedure

1. Encode the interpretation rules from the hypothesis ledger as a decision table.
2. Feed only validated D050 verdicts into the decision program.
3. Produce the allowed project outcomes and select the unique outcome if rules determine one.
4. If rules permit several outcomes, enumerate the exact unresolved condition rather than choosing by preference.
5. Generate allowed and prohibited claim lists from failed/pass verdicts.
6. Generate the smallest authorized next experiment for an inconclusive core result.
7. Render the prose memo from the structured decision record.

## Required checks

- Unit-test every combination of core H2/H4/H5 verdicts.
- Deliberately feed a contradictory ledger and confirm rejection.

## Machine verification

`pixi run verify-card -- D051` must reproduce the decision and claim lists from D050 without manual choices unless it emits `blocked` with a named unresolved condition.

## Primary artifact

`reports/continuation-decision.md` naming the surviving estimator and allowed claims.

## Acceptance

- The choice follows the preregistered consequences.
- Failed vocabulary—such as MRA or RG—is removed where its hypothesis failed.
- Next investment is bounded and justified.

## Failure or escalation

If evidence is inconclusive, specify the single smallest resolving experiment rather than authorizing an open-ended program.
