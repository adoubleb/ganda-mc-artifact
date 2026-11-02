## surrealdb

MC is the pairwise MC: per case, the union of its compared pairs' symmetric differences, less background and replicate noise.

| | |
|---|---|
| seeds | 427 |
| cases measured | 90768 |
| executable lines | 174899 |
| covered lines | 39350 |
| line coverage % | 22.499 |
| MC lines | 14588 |
| MC % of covered lines | 37.072 |
| MC % of executable lines | 8.341 |
| MC lines before noise | 18334 |
| background lines | 2261 |
| replicate-noise lines | 3746 |
| replicate seeds compared | 427 |
| cases with no MC | 16013 |

| component | executable | covered | covered % | MC | MC % of covered | share of MC % | background | replicate noise |
|---|---|---|---|---|---|---|---|---|
| executor | 36161 | 11336 | 31.349 | 5704 | 50.318 | 39.101 | 48 | 536 |
| planner | 7993 | 3565 | 44.602 | 2452 | 68.78 | 16.808 | 0 | 0 |
| expressions | 32079 | 5191 | 16.182 | 2262 | 43.575 | 15.506 | 269 | 314 |
| indexes | 18486 | 4364 | 23.607 | 1811 | 41.499 | 12.414 | 0 | 399 |
| parser | 14370 | 3374 | 23.479 | 1185 | 35.122 | 8.123 | 0 | 35 |
| storage | 23751 | 6773 | 28.517 | 799 | 11.797 | 5.477 | 1445 | 2014 |
| other | 6917 | 1437 | 20.775 | 289 | 20.111 | 1.981 | 352 | 225 |
| catalog | 4183 | 534 | 12.766 | 74 | 13.858 | 0.507 | 81 | 208 |
| server | 30959 | 2776 | 8.967 | 12 | 0.432 | 0.082 | 66 | 15 |

| data-model pair | MC lines | pairs |
|---|---|---|
| doc~graph | 13977 | 162173 |
| doc~rel | 10705 | 148436 |
| graph~rel | 12028 | 183720 |

| generator | MC lines | cases |
|---|---|---|
| ir_path | 6506 | 1278 |
| ir_select | 7272 | 76680 |
| ir_traversal | 11586 | 12810 |
