# Investigation 01: Formal specification audit

## Delivery cards

[D001](../../plan/deliverables/D001-freeze-vocabulary.md) → [D002](../../plan/deliverables/D002-data-observation-model.md) → [D003](../../plan/deliverables/D003-stage-operator.md) → [D004](../../plan/deliverables/D004-full-estimator.md) → [D005](../../plan/deliverables/D005-hand-example.md) → [D006](../../plan/deliverables/D006-independent-reproduction.md)

## Goal

Turn the user's actual algorithm into an unambiguous operator recurrence and determine why more than one interpolation stage is nontrivial.

## Required input

- [[00 Project/Working definition and assumptions]]
- Any equations, pseudocode, notebooks, or verbal definition supplied later

## Tasks

1. Define domain, observations, target, noise assumptions, and output.
2. Define "anomaly" operationally.
3. Write one full stage as an operator \(A_\ell\).
4. List every level-dependent quantity.
5. Apply the redundancy test: does the first stage annihilate training residuals?
6. State the objective minimized by one stage and by the full sum.
7. Determine whether stages are frozen, jointly refit, or backfitted.
8. Identify invariances: translation, rotation, scaling, permutation of sites, and coordinate reparameterization.

## Deliverables

- Two pages of definitions.
- Typed pseudocode.
- Shape table for every matrix and tensor.
- One toy example with three observations and two levels, computed by hand.
- List of ambiguities that change the method class.

## Stop condition

Stop when an independent implementer could reproduce the same predictions without asking a semantic question.
