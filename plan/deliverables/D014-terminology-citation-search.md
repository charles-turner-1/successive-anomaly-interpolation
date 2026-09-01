# D014 — Run terminology and citation searches

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D001, D004
- **Hypotheses:** H12
- **Verification classes:** V4

## Objective

Search exact and neighboring terminology plus backward and forward citations from the closest papers.

## Procedure

1. Build query families from every chosen and rejected term in D001.
2. Search exact phrases, operator descriptions, application-domain synonyms, and mathematical recurrence fragments.
3. Traverse references and citing works for the five closest primary papers.
4. Search official source hosts and code for matching update patterns.
5. Deduplicate results by DOI, title, and repository identity.
6. Screen title/abstract, then methods/equations for retained candidates.
7. Record a reason for every exclusion and an unresolved status for inaccessible work.
8. Repeat until one full query-family pass produces no new retained method.

## Required checks

- Re-run a sample of queries from the saved log.
- Have a second model rescreen the closest exclusions.

## Machine verification

`pixi run verify-card -- D014` must validate query/result/exclusion records, deduplication, stopping-rule evidence, and independent-rescreen coverage.

## Primary artifact

`research/search-log.md` containing queries, databases, dates, candidate matches, exclusions, and unresolved sources.

## Acceptance

- Searches cover anomaly analysis, successive corrections, multiscale covariance, residual interpolation, and domain terminology.
- Candidate matches are checked against the actual recurrence.
- The search is reproducible from recorded queries.

## Failure or escalation

Paywalls or inaccessible sources are listed for later retrieval rather than silently omitted.
