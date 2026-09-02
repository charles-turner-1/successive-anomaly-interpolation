# D000B — Establish the Pixi and Python foundation

- **State:** blocked
- **Owner:** unassigned
- **Effort limit:** none; continue until acceptance or an explicit blocker
- **Depends on:** D000A
- **Hypotheses:** infrastructure for H0–H12
- **Verification classes:** V2
- **Source policy:** [Toolchain policy](../toolchain-policy.md)

## Objective

Create the pinned root Pixi environment and minimal Python package/test foundation used by all verification commands.

## Work

1. Add `pixi.toml` with pinned channels, platforms, Python, test dependencies, and task placeholders required by the policy.
2. Add the minimal Python package and pytest layout documented by D000A.
3. Generate and commit `pixi.lock` without using global Python package installation.
4. Add a test proving project imports resolve inside the Pixi prefix.

## Required checks

- `pixi install --locked` succeeds from a clean environment.
- `pixi run verify-python` runs the minimal test suite twice in clean processes.
- The prefix test fails clearly when run outside the expected Pixi environment fixture.

## Machine verification

`pixi run verify-card -- D000B` must report the pinned Python version, Pixi prefix, lockfile hash, and passing tests.

## Primary artifact

The root `pixi.toml` and `pixi.lock` environment bundle.

## Acceptance

- The root environment is reproducible from the committed lockfile.
- Python imports resolve from the Pixi prefix.
- No bare `pip`, user install, virtualenv, or global Conda mutation appears in project commands.

## Failure or escalation

If the declared platforms cannot share one reproducible lock, record the solver conflict and block rather than weakening platform coverage silently.

## Completion packet

Follow the [execution protocol](../execution-protocol.md).
