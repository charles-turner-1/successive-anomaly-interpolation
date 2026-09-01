# Status board

Allowed states: `blocked`, `ready`, `in progress`, `review`, `done`, `failed`, `dropped`.

| ID | State | Depends on | Primary artifact |
|---|---|---|---|
| D000 | ready | — | Verification architecture |
| D001 | ready | D000 for completion | Frozen glossary |
| D002 | blocked | D001 | Data/observation specification |
| D003 | blocked | D001, D002 | Typed stage operator |
| D004 | blocked | D003 | Full estimator specification |
| D005 | blocked | D004 | Hand-worked example |
| D006 | blocked | D005 | Reproduction report |
| D007 | blocked | D000, D002, D004 | Machine-readable contracts |
| D008 | blocked | D000, D003, D004 | Lean proof foundation |
| D009 | blocked | D000, D007, D008 | Continuous verification gate |
| D010–D015 | blocked | D004 | Equivalence and prior-art artifacts |
| D020–D025 | blocked | D003/D004 | Theory artifacts |
| D030–D036 | blocked | D004 | Executable prototype |
| D040 | blocked | D036 | Smoke-test report |
| D041 | blocked | D040 | Frozen confirmation manifest |
| D042–D048 | blocked | D041 | Confirmatory evidence |
| D050–D053 | blocked | D042/D043 | Decision and release |

Update individual cards with owner, dates, and artifact links when work begins.
