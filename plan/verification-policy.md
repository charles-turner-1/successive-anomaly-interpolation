# Machine-verification policy

## Non-negotiable rule

No deliverable is complete if its conclusion can only be checked by reading prose. Every card must ship a machine-executable verifier and a manifest declaring what that verifier establishes.

## Verification classes

### V1 — Formal theorem

Use for algebraic and analytic claims that can be stated without empirical data: recurrence identities, positive-semidefinite closure, projection identities, finite-dimensional convergence conditions, and counterexamples.

- Preferred tool: Lean 4 with mathlib.
- Required output: theorem statement, proof without `sorry`, compiled proof log, and a plain-language correspondence between Lean symbols and the specification.
- Passing condition: the pinned Lean toolchain builds with no admitted axioms beyond those documented in the manifest.

### V2 — Deterministic executable test

Use for implementations, schemas, fixtures, numerical identities, CLI behavior, and reproducibility.

- Preferred tools: Python with pytest/Hypothesis and Julia with `Test`.
- Required output: code, deterministic fixture or generated property domain, and test report.
- Passing condition: tests pass twice from clean processes using pinned dependencies and identical inputs.

### V3 — Preregistered statistical decision

Use for comparative accuracy, calibration, scaling, and adversarial empirical claims.

- Preferred tool: Python analysis code operating only on immutable result bundles.
- Required output: frozen manifest, raw results, decision program, confidence intervals, and machine-readable verdict.
- Passing condition: the program returns pass/fail/inconclusive from the frozen threshold without manual editing or access to excluded smoke-test data.

### V4 — Provenance and search audit

Use for literature coverage, licenses, novelty searches, and traceability.

- Preferred tools: structured YAML/JSON records plus schema and link/identifier validators.
- Required output: query/source records, hashes or stable identifiers, inclusion decisions, and validation report.
- Passing condition: every prose claim resolves to a structured record and every required field validates. This verifies the audit trail, not universal novelty.

## Standard repository interfaces

The verification foundation deliverables must establish these interfaces:

```text
pixi run verify                 # run every available verifier
pixi run verify-formal          # Lean proofs
pixi run verify-python          # Python tests and statistical decision tests
pixi run verify-julia           # DIVAnd and Julia tests
pixi run verify-rust            # Cargo checks, if Rust is used
pixi run verify-schemas         # JSON/YAML artifact validation
pixi run verify-links           # local links and source identifiers
pixi run verify-card -- D000    # verify one delivery card
```

The complete environment and package rules are in the [toolchain policy](toolchain-policy.md). `pixi task list` must expose the canonical task surface.

## Per-deliverable verification manifest

Each card produces `verification/<ID>.yaml` with at least:

```yaml
id: D000
verification_class: [V2, V4]
inputs: []
artifacts: []
commands: []
expected: []
hypotheses: []
toolchain: {}
result: pending
```

The schema must reject unknown states, missing commands, unpinned toolchains, absent artifacts, and a `done` result without successful output.

## Limits of formal verification

- A Lean proof verifies a theorem relative to its definitions and assumptions; it does not prove those definitions model the physical world.
- Numerical tests establish behavior on specified domains and tolerances, not exact real-number identities.
- Statistical verification makes the preregistered decision reproducible; it does not turn finite evidence into a universal theorem.
- Provenance validation makes a search auditable; it cannot prove that no undiscovered prior work exists.

These limits must appear in reports so “formally verifiable” is not overstated.
