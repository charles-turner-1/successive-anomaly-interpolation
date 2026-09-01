# Execution protocol for implementation models

## Operating assumption

Implementing models may use as much computation, context, and iteration as necessary, but should not be expected to resolve ambiguous goals or fill gaps through expert intuition. Optimize for explicitness, verification, and traceability rather than speed.

## Required behavior for every card

1. Read the card, every dependency artifact, its source brief, and the relevant H-entry in the hypothesis ledger completely.
2. Create an execution log before doing substantive work. Record the card ID, input revisions, assumptions, commands, decisions, failures, and output paths.
3. Copy the card's acceptance criteria into the log as an unchecked list. Do not silently reinterpret them.
4. Execute the card procedure in order. A step may be repeated, but not skipped without recording why.
5. Preserve raw search results, raw numerical results, configurations, seeds, environment versions, and intermediate derivations needed to audit the conclusion.
6. Run the listed checks. Add reasonable checks when helpful, but do not replace the required ones.
7. Compare outputs against every acceptance item and relevant hypothesis threshold.
8. Finish in exactly one state:
   - `done`: every acceptance item passes;
   - `failed`: the work completed and produced a negative scientific result;
   - `blocked`: a named unavailable input or unresolved authority decision prevents completion;
   - `review`: artifacts exist but a specified mathematical or scientific check requires independent review.
9. Update `plan/status.md` and link the primary artifact and execution log.
10. Never call a result successful because it looks interesting. Use the frozen criteria.

## Ambiguity protocol

When an instruction admits multiple materially different interpretations:

1. stop the affected calculation;
2. enumerate the interpretations in the execution log;
3. show the smallest example on which they differ;
4. check the frozen specification and dependency artifacts for a resolution;
5. if unresolved, mark the card `blocked` and request a choice;
6. do not choose the interpretation that gives the best result.

## Research protocol

- Prefer primary papers, official documentation, and official repositories.
- Record exact equations, theorem assumptions, software versions, and source locations.
- Distinguish quotation, established fact, derivation, empirical observation, and conjecture.
- For equivalence claims, compare operators and objectives, not names or prose descriptions.
- A search ending without a match means only “not found under the documented protocol.”

## Implementation protocol

- Implement the frozen specification, not a convenient approximation, unless the approximation is a separately named variant.
- Write a failing test before fixing a discovered discrepancy.
- Use deterministic seeds and canonical serialization.
- Expose intermediate stage state; do not return only final predictions.
- Treat numerical warnings and discarded runs as data.
- Do not weaken baselines or give the proposed estimator more tuning information.
- Follow the [toolchain policy](toolchain-policy.md); never install project packages globally.

## Mathematical protocol

- State spaces, domains, dimensions, norms, and assumptions before a derivation.
- Check dimensions of every matrix product.
- Verify symbolic results numerically on at least one finite example.
- Attempt a counterexample for every generic implication.
- If a theorem cannot be completed, identify the exact unproved lemma rather than writing “appears stable.”

## Completion packet

Every completed card must provide:

- primary artifact;
- execution log;
- machine-readable inputs or configuration;
- raw outputs where applicable;
- verification output;
- acceptance checklist;
- hypothesis verdicts and consequences;
- open issues and follow-on card IDs.
