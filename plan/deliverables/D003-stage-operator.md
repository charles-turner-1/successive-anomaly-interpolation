# D003 — Specify one stage operator

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D001, D002
- **Hypotheses:** H0, H1
- **Verification classes:** V1, V2

## Objective

Define (A_\ell), its objective, inputs, outputs, hyperparameters, solver tolerance, and level-dependent quantities.

## Procedure

1. Copy all typed inputs from D002 and add level index ℓ only where a quantity changes by stage.
2. Write the stage objective before writing solver pseudocode.
3. Derive the stage normal equations or optimization conditions.
4. Define initialization, solver, tolerance, maximum iterations, and failure behavior.
5. List returned correction, uncertainty, residual diagnostics, and solver state.
6. Identify exactly which restriction prevents (S_XA_\ell) from being the identity.
7. Give deterministic pseudocode with no phrases such as “choose appropriately.”

## Required checks

- Check every expression dimensionally and with a small numeric matrix.
- Run the unrestricted exact-interpolator counterexample and show why the chosen stage differs.

## Machine verification

`pixi run verify-card -- D003` must compile formal type/algebra checks and pass numerical objective/normal-equation equivalence tests.

## Primary artifact

`spec/stage-operator.md` with equations and typed pseudocode.

## Acceptance

- An implementer can evaluate one stage without an unstated choice.
- The restriction preventing trivial exact interpolation is named.
- Deterministic behavior is specified for fixed inputs and seed.

## Failure or escalation

If more than one stage operator is plausible, nominate one primary variant and move others to an ablation list.
