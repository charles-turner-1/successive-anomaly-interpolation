# D052 — Complete the final novelty search

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D051
- **Hypotheses:** H12
- **Verification classes:** V4

## Objective

Search literature, code, terminology variants, forward/backward citations, and patents for the exact surviving estimator and contribution.

## Procedure

1. Generate query terms from the final structured estimator and surviving claims.
2. Freeze databases, APIs, search dates, query strings, and stopping rule.
3. Execute and archive result metadata permitted by source terms.
4. Deduplicate and screen using the D013 schema.
5. Require equation/operator inspection for every close candidate.
6. Link each surviving claim to nearest matches and decisive differences.
7. Have an independent model rescreen exclusions near the decision boundary.
8. Generate the H12 report from structured records.

## Required checks

- Schema-validate every query, result, inclusion, and exclusion.
- Re-run a sample of API/search queries and compare stable identifiers.
- Check that every novelty sentence resolves to evidence records.

## Machine verification

`pixi run verify-card -- D052` verifies audit completeness and traceability; its output must explicitly avoid claiming universal absence.

## Primary artifact

`research/final-novelty-report.md` with search protocol, claim chart, nearest references, and H12 verdict.

## Acceptance

- Search targets the final recurrence and assumptions, not the abandoned initial concept.
- Every claimed distinction has demonstrated consequence.
- Exact predecessors trigger a merge/synthesis recommendation.

## Failure or escalation

Novelty remains “not found in the documented search,” never proof of universal absence.
