# Verification repository layout

Primary artifact of [D000A — Define the verification repository layout](../plan/deliverables/D000A-repository-layout.md). This page is the single source of truth for the directory conventions that every later verification card uses. When a card adds a path or content class not covered here, that card must update this page in the same commit; the layout checker (below) then enforces the updated contract.

## Ground rules

1. **One purpose per path.** Every required path has exactly one documented purpose and one owner class (the class of card responsible for its contents).
2. **No cross-ownership.** A file belongs to the path whose permitted contents list admits it. Two paths may not both claim the same artifact.
3. **Deterministic enforcement.** The layout is checked by `verification/check_layout.py`, a deterministic standard-library-only Python checker. It reports missing required paths and unexpected content, in stable sorted order, with a nonzero exit on any violation.
4. **Placeholders are the only permitted emptiness markers.** `.gitkeep` is tracked solely so Git preserves an intentionally empty directory. It carries no meaning and is never a content violation.
5. **Toolchain files live at the root or in their language root** exactly as pinned by the [toolchain policy](../plan/toolchain-policy.md) (`pixi.toml`, `pixi.lock` at root; `julia/Project.toml` + `julia/Manifest.toml`; `formal/` Lake files; Rust workspace only if D000H admits it).

## Required paths

The checker requires exactly this set of paths to exist in the repository root. The set is intentionally minimal: it names where work *lives*, not how it is named inside.

| Path | Purpose | Owner class | Permitted contents | Naming rules |
|---|---|---|---|---|
| `python/` | Python source for the verification toolchain, estimators, and analysis programs. | D000B establishes the package skeleton; later implementation cards (D030–D036) add modules. | Python modules and packages (`.py`, `__init__.py`), plus `.gitkeep` while empty. | Lowercase `snake_case` module names; importable package layout rooted at `python/`. |
| `tests/` | Python tests: unit, deterministic V2 tests, statistical-decision tests (V3). | D000B establishes the pytest skeleton; each implementation card owns tests for its own code. | `test_*.py` files and test fixtures in `tests/fixtures/`. | Test files named `test_<module>_<behavior>.py`; fixtures under `tests/fixtures/` with stable, collision-free names. |
| `julia/` | Julia project-local environment and source (DIVAnd work, numerical checks). | D000F owns `Project.toml`/`Manifest.toml` and test scaffolding; later Julia cards add source. | `Project.toml`, `Manifest.toml`, Julia source (`src/`, `test/` per Julia conventions), `.gitkeep` while empty. | Julia project conventions; `src/<module>.jl`, `test/test_<module>.jl`. |
| `formal/` | Lean 4 formal proofs and Lake project. | D000G owns toolchain pin and Lake scaffolding; proof cards (D008 and successors) add modules. | `lean-toolchain`, `lakefile.toml` or `lakefile.lean`, `lake-manifest.json`, `src/` Lean modules, `.gitkeep` while empty. | Lean module names in `PascalCase`, one proof concept per module. |
| `schemas/` | JSON/YAML schemas for verification manifests, result bundles, and other structured records. | D000C owns the manifest schema; D031 owns the result schema; later cards add their own. | `*.schema.json` / `*.schema.yaml` files only. | `<artifact-kind>.schema.json` (e.g. `manifest.schema.json`, `result.schema.json`). |
| `verification/` | Machine-verification artifacts: per-card manifests, the layout checker, fixtures, and validator programs. | D000A owns the layout checker and this directory's conventions; every card owns its own `<ID>.yaml` manifest; D000D–D000I own validators and dispatch. | `<ID>.yaml` card manifests, `check_*.py` / `verify_*.py` tooling, `fixtures/` for negative tests. | Manifests named exactly `<CARD_ID>.yaml` (e.g. `D000A.yaml`); checkers `check_<what>.py`; fixture directories kebab-case describing the violation. |
| `results/` | Raw, immutable experimental results (runs, seeds, timings, intermediates). | Each experiment card (D030–D048) writes; D041 freezes; no later card edits frozen bundles. | Result bundles in stable subdirectories per experiment. | `<card-id>_<run-id>_<seed>/` directories containing machine-readable outputs; frozen bundles are byte-stable. |
| `reports/` | Human-readable reports and syntheses derived from frozen results. | Reporting cards (D040, D046–D053) write; each report cites the frozen result bundles it reads. | Markdown/HTML reports and their small embedded assets. | `<card-id>_<topic>.md` (e.g. `D040_smoke-tests.md`); one report per decision. |
| `docs/` *(present, not required)* | Specification and convention documentation, including this file. | D000A owns this file; specification cards (D001–D004) own their specification docs. | Markdown documents and diagrams. | `docs/<topic>.md`; kebab-case topics. It exists because the primary artifact lives here; it is not a *required* layout path and the checker does not demand it. |

Paths the layout checker does **not** require: `rust/` (conditional on D000H), `vault/` and `plan/` (pre-existing repository structure, not verification layout), and any root-level files (`pixi.toml`, `pixi.lock`, `README.md`, etc.).

## Provenance

- Required-path names derive from the [toolchain policy](../plan/toolchain-policy.md) (language roots), the [verification policy](../plan/verification-policy.md) (`verification/<ID>.yaml`, schemas), and the D000A card's enumeration (source, tests, schemas, manifests, raw results, reports).
- `docs/` is documented but not required (see above).
- This layout is infrastructure for hypotheses H0–H12; it imposes no scientific constraint and must never be used to steer a hypothesis outcome.

## Layout check

- **Program:** `verification/check_layout.py` (Python 3 standard library only; deterministic).
- **Run against a valid tree:** `python3 verification/check_layout.py --root .` → exit `0`, prints `layout check: OK (<N> required paths present, no violations)`.
- **Run against a missing-path fixture:** `python3 verification/check_layout.py --root verification/fixtures/missing-paths` → exit `1`, prints each missing required path (e.g. `MISSING required path: reports`) in stable sorted order, then `layout check: FAILED (<M> violation(s))`.
- **Determinism contract:** identical input tree ⇒ identical stdout and exit code. No timestamps, no environment-dependent output, no network, no non-stdlib imports. The checker reads only the directory names of the required paths and their immediate content classes; it never follows symlinks and never mutates the tree.
- **Replay:** once D000B (Pixi) and D000I (`verify-card`) exist, `pixi run verify-card -- D000A` must replay both the valid-tree and missing-path checks declared in `verification/D000A.yaml`.

## Acceptance traceability

| Acceptance item | Where satisfied |
|---|---|
| Every required path has one documented purpose and owner class | "Required paths" table: 8 required paths, each with exactly one purpose and one owner class. |
| The valid and missing-path fixtures behave deterministically | "Layout check" section + `verification/fixtures/missing-paths/` + checker determinism contract; executed in the execution log. |
| No project dependency is installed globally | Checker is stdlib-only; no package manager is invoked by this card; recorded in the execution log. |

## Related

- [D000A card](../plan/deliverables/D000A-repository-layout.md)
- [Toolchain policy](../plan/toolchain-policy.md)
- [Verification policy](../plan/verification-policy.md)
- [Execution protocol](../plan/execution-protocol.md)
- [Verification manifest for this card](../verification/D000A.yaml)
