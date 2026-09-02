# Missing-path fixture — D000A

Negative fixture for the deterministic layout checker (`verification/check_layout.py`).

## What this directory is

A committed directory tree that mirrors the required layout of
`docs/verification-layout.md` **except that the required path `reports/` is
absent**. All other required paths are present (as empty directories, which
the checker accepts because an empty required path with no constrained
immediate entries is valid; the real tree additionally carries `.gitkeep`
placeholders).

## Expected behavior

Run:

```sh
python3 verification/check_layout.py --root verification/fixtures/missing-paths
```

Expected:

- exit code **1** (nonzero), and
- the missing path **named** in the diagnostic: `MISSING required path: reports`,

followed by the summary line `layout check: FAILED (1 violation(s))`.

The exact expected stdout is recorded in `expected.txt`. Re-running the
command against this unchanged directory must produce byte-for-byte identical
output (determinism contract).

## How it is used

- Required check (D000A): "Run it against a fixture with one required path
  missing and confirm a nonzero exit with the path named." — this fixture is
  that fixture.
- Replay (D000I): `pixi run verify-card -- D000A` re-executes both the
  valid-tree check and this fixture check, comparing the fixture output to
  `expected.txt`.

## Invariants

- Exactly one required path is missing (`reports`); no other violation is
  intended. If a future card changes the required-path set, this fixture and
  `expected.txt` must be regenerated in the same commit.
- This directory is a *fixture*, not live layout: the checker's "valid tree"
  check is run against the repository root, never against this directory.
