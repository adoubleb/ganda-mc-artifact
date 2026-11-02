## orientdb

MC is the pairwise MC: per case, the union of its compared pairs' symmetric differences, less background and replicate noise.

| | |
|---|---|
| seeds | 595 |
| cases measured | 125489 |
| executable lines | 183820 |
| covered lines | 45655 |
| line coverage % | 24.837 |
| MC lines | 11404 |
| MC % of covered lines | 24.979 |
| MC % of executable lines | 6.204 |
| MC lines before noise | 16779 |
| background lines | 6808 |
| replicate-noise lines | 5052 |
| replicate seeds compared | 592 |
| cases with no MC | 19118 |

| component | executable | covered | covered % | MC | MC % of covered | share of MC % | background | replicate noise |
|---|---|---|---|---|---|---|---|---|
| parser | 35120 | 11474 | 32.671 | 6114 | 53.286 | 53.613 | 436 | 951 |
| executor | 17886 | 3632 | 20.306 | 1313 | 36.151 | 11.514 | 387 | 739 |
| planner | 3222 | 1923 | 59.683 | 867 | 45.086 | 7.603 | 44 | 176 |
| indexes | 16593 | 5201 | 31.345 | 791 | 15.209 | 6.936 | 186 | 256 |
| other | 38283 | 7081 | 18.496 | 717 | 10.126 | 6.287 | 1641 | 894 |
| storage | 29513 | 9408 | 31.877 | 669 | 7.111 | 5.866 | 3124 | 910 |
| expressions | 5387 | 882 | 16.373 | 350 | 39.683 | 3.069 | 0 | 184 |
| catalog | 7765 | 2939 | 37.849 | 217 | 7.383 | 1.903 | 192 | 148 |
| graph | 954 | 232 | 24.319 | 205 | 88.362 | 1.798 | 0 | 2 |
| server | 27563 | 2332 | 8.461 | 112 | 4.803 | 0.982 | 528 | 748 |
| transactions | 1534 | 551 | 35.919 | 49 | 8.893 | 0.43 | 270 | 44 |

| data-model pair | MC lines | pairs |
|---|---|---|
| doc~graph | 10772 | 245999 |
| doc~rel | 7249 | 208843 |
| graph~rel | 10675 | 293066 |

| generator | MC lines | cases |
|---|---|---|
| ir_path | 5639 | 901 |
| ir_select | 6499 | 106638 |
| ir_traversal | 9134 | 17950 |
