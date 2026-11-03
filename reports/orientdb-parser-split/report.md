## orientdb-parser-split

MC is the pairwise MC: per case, the union of its compared pairs' symmetric differences, less background and replicate noise.

| | |
|---|---|
| seeds | 595 |
| cases measured | 125489 |
| executable lines | 35120 |
| covered lines | 11474 |
| line coverage % | 32.671 |
| MC lines | 6114 |
| MC % of covered lines | 53.286 |
| MC % of executable lines | 17.409 |
| MC lines before noise | 7149 |
| background lines | 436 |
| replicate-noise lines | 951 |
| replicate seeds compared | 592 |
| cases with no MC | 73419 |

| component | executable | covered | covered % | MC | MC % of covered | share of MC % | background | replicate noise |
|---|---|---|---|---|---|---|---|---|
| parser-generated | 15760 | 5695 | 36.136 | 3511 | 61.651 | 57.426 | 0 | 31 |
| parser-ast | 19202 | 5690 | 29.632 | 2533 | 44.517 | 41.43 | 436 | 911 |
| parser-other | 158 | 89 | 56.329 | 70 | 78.652 | 1.145 | 0 | 9 |

| data-model pair | MC lines | pairs |
|---|---|---|
| doc~graph | 5857 | 245999 |
| doc~rel | 4523 | 208843 |
| graph~rel | 5606 | 293066 |

| generator | MC lines | cases |
|---|---|---|
| ir_path | 3177 | 901 |
| ir_select | 3456 | 106638 |
| ir_traversal | 5151 | 17950 |
