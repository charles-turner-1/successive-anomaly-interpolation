# D050 — Populate the evidence ledger

- **State:** blocked
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Protocol:** [execution protocol](../execution-protocol.md)
- **Depends on:** D042, D043 and completed optional tests
- **Hypotheses:** H0–H11
- **Verification classes:** V1, V2, V3, V4

## Objective

Create one auditable table connecting every claim to its derivation, run manifest, result, verdict, and caveat.

## Procedure

1. Discover every verification manifest and hypothesis verdict automatically.
2. Validate artifact existence, hashes, code revisions, and verifier outputs.
3. Join hypotheses, claims, formal theorems, empirical decisions, and provenance records by stable IDs.
4. Mark missing, stale, contradictory, and out-of-scope evidence.
5. Generate the Markdown ledger from the structured ledger; do not edit the table manually.
6. For conflicting evidence, retain both records and apply the preregistered precedence rule.
7. Produce a dependency graph from final claims to raw evidence.

## Required checks

- Delete or alter a fixture artifact and confirm the ledger build fails.
- Confirm every claim has at least one verification class and limitation statement.

## Machine verification

`pixi run verify-card -- D050` must regenerate a hash-identical ledger and claim-evidence graph from manifests.

## Primary artifact

`reports/evidence-ledger.md` with immutable artifact links.

## Acceptance

- Every hypothesis is pass, fail, inconclusive, or explicitly out of scope.
- Deviations and missing runs are visible.
- No claim cites only a summary without underlying evidence.

## Failure or escalation

Missing evidence blocks the associated claim rather than being filled by narrative inference.
