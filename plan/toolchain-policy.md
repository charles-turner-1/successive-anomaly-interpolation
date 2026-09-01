# Toolchain and package-management policy

## General rule

No project command may depend on packages installed into a user's global Python, Julia, Rust, or Lean environment. Toolchain versions and dependency resolutions must be committed or reproducibly generated from committed lockfiles.

## Python and orchestration: Pixi

Required root files:

- `pixi.toml` — channels, platforms, Python version, conda dependencies, PyPI dependencies, environments, and tasks;
- `pixi.lock` — exact cross-platform resolution committed to Git.

Rules:

- Run Python only through `pixi run ...` or an activated Pixi environment.
- Declare runtime, test, documentation, and optional experiment dependencies in named Pixi environments or features.
- Do not use global `pip`, `pip install --user`, bare virtualenvs, Poetry, or Conda environment mutations outside Pixi.
- If a dependency must come from PyPI, declare it under Pixi's PyPI dependency configuration and lock it.
- CI installs Pixi, restores no mutable environment directory as an authoritative artifact, and runs from `pixi.lock`.
- `pixi run verify` is the canonical repository-wide entry point.

## Julia: project-local Pkg environment

Required files when Julia is used:

- `julia/Project.toml`;
- `julia/Manifest.toml` committed for exact reproducibility;
- Julia compatibility bounds in `Project.toml`.

Rules:

- Run Julia as `julia --project=julia ...`; the Pixi tasks must use that form.
- Instantiate with `julia --project=julia -e 'using Pkg; Pkg.instantiate()'`.
- Add or update packages only while the project environment is active, then commit both project files.
- Do not call `Pkg.add` from library, experiment, or test code.
- Do not rely on packages in Julia's default `@v#.#` environment or a user startup file.
- Tests run with `julia --project=julia -e 'using Pkg; Pkg.test()'` or an equivalent project-local test target.

## Rust: Cargo workspace, only if used

Required files when Rust is introduced:

- root or `rust/Cargo.toml` workspace;
- committed `Cargo.lock` for applications and verification tooling;
- pinned minimum supported Rust version or `rust-toolchain.toml`.

Rules:

- Use Cargo for building, testing, benchmarking, formatting, and linting.
- Declare every crate dependency in `Cargo.toml`; do not copy vendored source without provenance.
- Run `cargo test --locked`, `cargo clippy --locked -- -D warnings`, and `cargo fmt --check` through Pixi tasks.
- Do not install project dependencies globally with `cargo install`. Tool binaries must be declared through Pixi, a workspace crate, or a documented pinned CI bootstrap.
- Do not add Rust merely for prestige; use it only for a measured implementation or verification need.

## Lean: pinned toolchain and Lake

Required files when Lean proofs are used:

- `lean-toolchain`;
- `formal/lakefile.toml` or `lakefile.lean`;
- `formal/lake-manifest.json`;
- pinned mathlib revision.

Rules:

- Use Lake for Lean dependencies and builds.
- Run proofs through the pinned toolchain from Pixi tasks.
- Do not depend on arbitrary globally installed Lean packages.
- CI rejects `sorry`, `admit`, unexpected axioms, and dirty dependency resolutions.

## Canonical task surface

```text
pixi run bootstrap          # instantiate all declared project environments
pixi run verify             # all available verification classes
pixi run verify-formal      # Lean/Lake proofs
pixi run verify-python      # Python tests and statistical decisions
pixi run verify-julia       # Julia project tests
pixi run verify-rust        # Cargo checks, if Rust workspace exists
pixi run verify-schemas     # manifests and result schemas
pixi run verify-links       # local links and source records
pixi run verify-card -- ID  # one deliverable manifest and its commands
```

## Machine enforcement

D000 must implement tests that fail when:

- a Python process imports a project dependency outside the Pixi prefix;
- Julia's active project is not `julia/Project.toml`;
- a Rust workspace exists without its required lock/toolchain files;
- a Lean project exists without pinned Lake/toolchain files;
- a manifest command uses a prohibited global install command;
- a lockfile is missing or inconsistent with its project declaration.
