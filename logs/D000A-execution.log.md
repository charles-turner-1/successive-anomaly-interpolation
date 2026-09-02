# Execution log — D000A: Define the verification repository layout

## Identity

- Card: D000A — Define the verification repository layout
- Branch: `work/qwen-d000a` (isolated worktree `successive-anomaly-interpolation-qwen-d000a`, base `plan/split-d000` @ `2499d43`)
- Implementing agent: Research Bot (OpenClaw, model `ollama/qwen3.8:27b`)
- Parent review/finalization: Research Bot (OpenClaw, model `openai/gpt-5.6-sol`)
- Date started: 2026-09-02 (UTC)
- Effort limit: none; continue until acceptance or an explicit blocker

## Inputs and revisions read (complete)

| Input | Revision read |
|---|---|
| `plan/deliverables/D000A-repository-layout.md` | commit `2499d43` (head of `work/qwen-d000a` base) |
| `plan/execution-protocol.md` | commit `2499d43` |
| `plan/toolchain-policy.md` | commit `2499d43` |
| `plan/verification-policy.md` | commit `2499d43` (V2, V4 class definitions; `verification/<ID>.yaml` manifest contract) |
| `plan/status.md` | commit `2499d43` |
| `plan/README.md`, `plan/roadmap.md` | commit `2499d43` (dependency and phase rules) |
| `vault/00 Project/Hypothesis ledger and decision rules.md` | H0–H12 infrastructure context (D000A declares "infrastructure for H0–H12"; no hypothesis thresholds apply to this card) |
| `README.md` (repository root) | commit `ecbc694` (repository purpose, vault/plan split, toolchain summary) |

## Assumptions

1. **A0 — Required-path set.** The card says "Create directories for Python source and tests, Julia source and tests, Lean proofs, schemas, verification manifests, raw results, and reports" without naming them. Interpretation chosen from the frozen specs:
   - `python/` (Python source) and `tests/` (Python tests) — D000B card names these paths explicitly ("the minimal Python package and pytest layout documented by D000A"), so this choice is anchored to a frozen document.
   - `julia/` — anchored to toolchain policy (`julia/Project.toml`, `julia/Manifest.toml`).
   - `formal/` — anchored to toolchain policy (`formal/lakefile.toml` or `lakefile.lean`, `formal/lake-manifest.json`).
   - `schemas/`, `verification/` (manifests per verification policy `verification/<ID>.yaml`), `results/` (raw results), `reports/` — named by the card's enumeration; names chosen to match the verification policy's phrasing.
   - `docs/` is **not** in the required-path set: the card's own primary artifact (`docs/verification-layout.md`) is a file, and a docs directory cannot be a "permitted contents" path for later cards. It exists in the tree (needed for the primary artifact) but the layout checker does not require it.
   - `rust/` is intentionally **not** a required path: the toolchain policy makes Rust conditional ("only if used", "Do not add Rust merely for prestige") and D000H is the "conditional Rust guard". Requiring `rust/` would contradict the frozen policy.
2. **A1 — Placeholders.** "Add tracked placeholders only where Git would otherwise omit an intentionally empty directory." At D000A completion, `python/`, `tests/`, `julia/`, `formal/`, `rust/`(absent), `schemas/`, `results/`, `reports/` are intentionally empty of later-card content, so each receives one tracked `.gitkeep` placeholder. `verification/` will contain this card's manifest, and `docs/` will contain the primary artifact, so neither needs a placeholder at D000A completion.
3. **A2 — Checker language and determinism.** The toolchain policy mandates Pixi-managed Python, but the D000B environment (and thus `pixi run`) does not exist yet on this branch — D000B is the *dependent* card. To run the required checks at D000A completion without violating "no project dependency is installed globally", the checker is written in Python **standard library only** and is executed directly with the system interpreter (`python3`), which requires no project package. The card's "deterministic standard-library layout checker" phrasing is consistent with this. Once D000B lands, `pixi run verify-layout` can wrap the same script unchanged.
4. **A3 — Missing-path fixture.** The card requires a fixture "with one required path missing" that makes the checker exit nonzero naming that path. Implemented as `verification/fixtures/missing-paths/` — a committed directory tree that mirrors the required layout except `reports/` is absent, plus `verification/fixtures/missing-paths/expected.txt` recording the expected diagnostic (nonzero exit; `reports` named in output). The checker takes `--root` so it can run against both the live tree and the fixture.
5. **A4 — "Unexpected required paths" check.** The checker's positive check verifies every required path exists and holds only permitted content classes (no source files in `schemas/`, no manifests outside `verification/`, etc.); the negative fixture verifies the missing-path diagnostic. Both are deterministic: same input tree → same exit code and same message, no timestamps, no locale-dependent formatting.
6. **A5 — Status board.** The card (via the execution protocol step 9) requires `plan/status.md` to be updated with the new state and links to the primary artifact and execution log.

## Decisions

| ID | Decision | Rationale |
|---|---|---|
| D1 | Required paths: `python/`, `tests/`, `julia/`, `formal/`, `schemas/`, `verification/`, `results/`, `reports/` | A0; anchored to frozen policy text where possible |
| D2 | One `.gitkeep` placeholder per intentionally-empty required path at D000A time | Card work item 2 |
| D3 | Checker = `verification/check_layout.py`, stdlib only, deterministic, `--root` parameter, stable sorted diagnostics, exit 0/1 | A2, A4; required checks of the card |
| D4 | Valid fixture = the live repository tree; missing-path fixture = `verification/fixtures/missing-paths/` | A3 |
| D5 | Manifest = `verification/D000A.yaml`, a bootstrap record with `result: review` until the D000C schema and D000I dispatcher can validate it | verification-policy manifest contract; avoids claiming an unavailable canonical check passed |
| D6 | No pixi.toml/pixi.lock added by this card | Those are D000B's primary artifacts; adding them here would cross the card boundary |
| D7 | No packages installed anywhere; checker uses stdlib only | Card acceptance + toolchain policy |

## Commands (chronological)

1. `ls` workspace; located worktree at `/home/ct/.openclaw/workspace/successive-anomaly-interpolation-qwen-d000a`, branch `work/qwen-d000a`, clean tree.
2. Read the three mandated plan documents + verification policy, status board, roadmap, hypothesis ledger, root README (complete).
3. Verified no `docs/`, `verification/`, `python/`, `tests/`, `julia/`, `formal/`, `schemas/`, `results/`, `reports/` exist yet; `git log --oneline main -3`; confirmed `main` head `ecbc694`, branch head `2499d43`.
4. `mkdir -p logs verification/fixtures`
5. Wrote the primary artifact, checker, missing-path fixture, required placeholders, and bootstrap manifest.
6. Ran the valid-tree checker twice and compared byte-identical stdout; both exits were `0`.
7. Ran the missing-path fixture twice, captured exit `1` both times, compared byte-identical stdout, and matched `expected.txt` exactly.
8. Ran `python3 -m py_compile verification/check_layout.py`, local Markdown-link validation, `git diff --check`, and inspected status/diff.
9. Updated the status board to `review`: card acceptance checks pass, but the canonical `pixi run verify-card -- D000A` gate does not exist until D000B/D000I.

## Failures

- The implementing model stopped twice before producing the manifest, final checks, status update, or commit. The parent review completed those bounded items without expanding scope.
- The first fixture draft used empty directories without tracked placeholders; `.gitkeep` files were added so the fixture survives a fresh checkout.

## Output paths

- `docs/verification-layout.md` (primary artifact)
- `verification/check_layout.py` (deterministic stdlib layout checker)
- `verification/fixtures/missing-paths/` (missing-path fixture + expected diagnostic)
- `verification/D000A.yaml` (verification manifest)
- `plan/status.md` (status board update)
- `.gitkeep` in: `python/`, `tests/`, `julia/`, `formal/`, `schemas/`, `results/`, `reports/`
- `logs/D000A-execution.log.md` (this file)

## Acceptance criteria (copied verbatim from the card)

- [x] Every required path has one documented purpose and owner class.
- [x] The valid and missing-path fixtures behave deterministically.
- [x] No project dependency is installed globally.

## Required checks (copied verbatim from the card)

- [x] Run the layout check once against the valid tree.
- [x] Run it against a fixture with one required path missing and confirm a nonzero exit with the path named.

## Machine verification (copied verbatim from the card)

> `pixi run verify-card -- D000A` must validate the layout record and both fixtures once D000I provides dispatch.

- [x] Not runnable at D000A bootstrap completion: `verify-card` is provided by D000I and the Pixi environment by D000B. The direct deterministic checks pass, and the card remains in `review` until its manifest is validated and replayed through that canonical interface.

## Final state

`review` — the bounded D000A artifact and direct checks satisfy the card acceptance criteria. Promotion to `done` is deferred until D000B supplies the pinned environment and D000I replays `verification/D000A.yaml` through `pixi run verify-card -- D000A`.
