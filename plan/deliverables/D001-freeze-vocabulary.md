# D001 — Freeze vocabulary

- **State:** ready
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** none
- **Hypotheses:** H0
- **Verification classes:** V2, V4
- **Source:** [Working definition](../../vault/00%20Project/Working%20definition%20and%20assumptions.md)

## Objective

Choose one operational meaning for anomaly, background, correction, scale, interpolation, and analysis.

## Procedure

1. Extract every definition or implied use of the six terms from the working definition, DIVAnd notes, residual-correction note, and spectral note.
2. Put competing meanings in a table with required inputs, mathematical expression, and consequences for the estimator.
3. Select one primary meaning per term using consistency with the supplied algorithmic intent; do not select based on expected benchmark performance.
4. Assign a symbol and type to every selected term.
5. Write one positive example and one non-example for each definition.
6. Record every rejected alternative and the card that would need to change to restore it.

## Required checks

- Give the glossary to a fresh model and ask it to compute the anomaly for three concrete inputs.
- Confirm that only one answer is valid under the text.

## Machine verification

`pixi run verify-card -- D001` must validate glossary records and pass all positive, negative, and fresh-model interpretation fixtures.

## Primary artifact

`spec/glossary.md` containing definitions, rejected alternatives, and notation.

## Acceptance

- Every term has one testable definition.
- “Anomaly” can be computed from supplied inputs without interpretation.
- Rejected meanings remain recorded.

## Failure or escalation

If multiple meanings are intentional, split them into explicitly named algorithm variants before D002.
