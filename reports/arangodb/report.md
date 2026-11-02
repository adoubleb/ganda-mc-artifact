## arangodb

MC is the pairwise MC: per case, the union of its compared pairs' symmetric differences, less background and replicate noise.

| | |
|---|---|
| seeds | 190 |
| cases measured | 40470 |
| executable lines | 359667 |
| covered lines | 87405 |
| line coverage % | 24.302 |
| MC lines | 23250 |
| MC % of covered lines | 26.6 |
| MC % of executable lines | 6.464 |
| MC lines before noise | 45496 |
| background lines | 22327 |
| replicate-noise lines | 19172 |
| replicate seeds compared | 190 |
| cases with no MC | 7699 |

| component | executable | covered | covered % | MC | MC % of covered | share of MC % | background | replicate noise |
|---|---|---|---|---|---|---|---|---|
| executor | 40670 | 16181 | 39.786 | 8283 | 51.19 | 35.626 | 4844 | 2394 |
| planner | 18772 | 9329 | 49.696 | 4585 | 49.148 | 19.72 | 2825 | 1912 |
| parser | 11078 | 6562 | 59.235 | 2784 | 42.426 | 11.974 | 2422 | 1127 |
| graph | 8843 | 2419 | 27.355 | 2411 | 99.669 | 10.37 | 0 | 8 |
| expressions | 11558 | 3346 | 28.95 | 1755 | 52.451 | 7.548 | 257 | 331 |
| indexes | 64522 | 6313 | 9.784 | 1684 | 26.675 | 7.243 | 1199 | 1376 |
| storage | 27324 | 10249 | 37.509 | 810 | 7.903 | 3.484 | 3144 | 3066 |
| other | 44907 | 12717 | 28.319 | 516 | 4.058 | 2.219 | 4074 | 4325 |
| transactions | 5772 | 2423 | 41.979 | 222 | 9.162 | 0.955 | 1089 | 742 |
| server | 57338 | 14276 | 24.898 | 196 | 1.373 | 0.843 | 2196 | 3524 |
| catalog | 68883 | 3590 | 5.212 | 4 | 0.111 | 0.017 | 277 | 367 |

| data-model pair | MC lines | pairs |
|---|---|---|
| doc~graph | 21882 | 127264 |
| doc~rel | 14989 | 121541 |
| graph~rel | 20715 | 125013 |

| generator | MC lines | cases |
|---|---|---|
| ir_path | 12421 | 570 |
| ir_select | 7533 | 34200 |
| ir_traversal | 19676 | 5700 |
