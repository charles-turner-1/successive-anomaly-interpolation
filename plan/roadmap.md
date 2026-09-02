# Roadmap and dependencies

## Critical path

```text
D000A → D000B ─┬→ D000C → D000D/D000E ───────┐
                ├→ D000F ──────────────────────┤
                ├→ D000G ──────────────────────┼→ D000I → D000J ─┐
                └→ D000H ──────────────────────┘                  │
                                               ↓
                                              D000 → D001 → D002 → D003 → D004 → D005 → D006
                                                                           └────→ D007 ─┐
                                                                                  D008 ─┼→ D009
                                                                                        │
                                                                D010/D012/D013/D014 ───┤
                                                                                        ↓
D030 → D031 → D032/D033/D034/D035 → D036 → D040 → D041 → D042–D048 → D050 → D051 → D052 → D053
```

The diagram is schematic: D000 integrates D000A–D000J; D007 requires D002 and D004; D008 requires D003 and D004; D009 requires D000, D007, and D008. Foundation subcards ship their own executable checks and manifests during bootstrap; D000I must replay all of them through the canonical dispatcher before D000 can complete. No non-foundation card may be declared complete before D000, and no confirmatory run may begin before D009 is active.

## Parallel work

- D000C begins after D000B supplies the pinned Python validation environment.
- D000D and D000E can run in parallel after D000B and D000C.
- D000F, D000G, and D000H can run in parallel after D000A and D000B.
- D010, D012, D013, D014, D007, and D008 can run in parallel after their specification dependencies are satisfied.
- D020–D024 can run in parallel once D003 and the relevant comparator specification exist.
- D032–D035 can run in parallel after D030 and D031.
- D044–D048 can run in parallel after D041, subject to the branch rules below.

## Branch rules

- Do not run D042 if D006 fails.
- Do not mark any card `done` without a passing verification manifest.
- Do not run D041 or later before D009 passes.
- Do not make a succession claim until D043 decides H4 and H5.
- Run D044 only if irregular geometry or physical constraints remain in scope.
- Run D045 only if probabilistic output remains in scope.
- Run D046 only if scalability is part of the intended contribution.
- D025 may begin as a derivation, but RG language cannot enter the main claim unless H11 passes.
- D052 searches novelty only for the algorithm that survives D051.

## Work-package granularity

Cards are bounded by one primary artifact and one decision, not by time or token budget. Implementing models should continue until every acceptance item is verified. Split a card only when it contains separable outputs or an ambiguity prevents one unambiguous procedure; do not split merely because the work is long.

D000A–D000J are an intentional decomposition of the former D000 card by separable artifact and toolchain boundary. D000 remains the aggregate integration decision, so the split does not weaken its original acceptance criteria.
