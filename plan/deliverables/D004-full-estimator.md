# D004 — Specify the full estimator

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D003
- **Hypotheses:** H0, H1
- **Verification classes:** V1, V2

## Objective

Specify initialization, recurrence, scale schedule, damping, freezing/backfitting, stopping, and returned uncertainty.

## Procedure

1. Define (b_0), (a_0), and all stored state before the first level.
2. Write the ordered operations for computing (g_\ell), updating (b_\ell), and recomputing (a_{\ell+1}).
3. Give an explicit finite or adaptive scale schedule, including tie and boundary behavior.
4. State whether earlier stages are frozen, refitted, or backfitted.
5. Define damping selection using only allowed information.
6. Specify all stopping conditions and their precedence.
7. Define final prediction and uncertainty outputs at observed and target sites.
8. Derive the first two levels algebraically.

## Required checks

- Execute the pseudocode manually on symbolic (A_0,A_1,H).
- Verify there is no read of validation/test information not declared by D002.

## Machine verification

`pixi run verify-card -- D004` must compile the two-level recurrence statements and pass executable state-transition and information-flow tests.

## Primary artifact

`spec/estimator.md` plus end-to-end pseudocode.

## Acceptance

- Every state transition is defined.
- The first-stage redundancy test is answered algebraically.
- Stopping uses only information available at that point.

## Failure or escalation

If the full estimator collapses to one stage, record H1 failure before modifying it.
