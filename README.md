# Ganda: metamorphic coverage reports

The metamorphic coverage (MC) reports behind Section 4.4 of the paper (Tables 8-11) for
OrientDB 3.2.57, SurrealDB 3.3.4 and ArangoDB 3.12.11, and the environment that produced
them. The raw window logs the reports are computed from (about 30 GB) are published
separately.

## What MC is

Every test case asks one question in several variants, one or more per data model. The
oracle compares pairs of variants from different data models with the same concrete
syntax, and each variant's covered lines are recorded per case. The MC of a case is the
union of its compared pairs' symmetric differences (Equation 2 of the paper):

    MC(t) = U_{(a,b) in P_t} Cov(a) △ Cov(b)

A run's MC is the union over its cases, less two kinds of noise. **Background** lines
are what the server ran while no case was running (5 idle seconds every 15 minutes).
**Replicate noise** is the lines a twin run (same seeds, same code) covered differently
for the same variant of the same case.

In `report.json` the MC is the `mc_pairwise_*` fields (and `mc_pairwise` per component),
and `data_model_pairs.<pair>.mc_lines` is the MC of that pair alone.

## The runs

Each engine ran for 12 hours as twins A and B, the same seeds (from 40000) and code at the
same time, with `--coverage variant --workers 1`, every axis on, the known-bug guards off,
no bundles, and `--shared-physical-design true` (every data model gets the same indexes,
id index kind and storage choice). The reports are of twin A, with B used for the
replicate noise; B's seeds, cases and coverage are under `twin` in each `report.json`.
`env/env.txt` has the exact commands.

## The paper's tables

`python3 table.py` prints Tables 8, 9 and 10 (line coverage and MC per component), Ganda's
rows of Table 11, the MC of each data-model pair and the runs' counts from the
`report.json` files. The per-component tables fold the reports' components into the
paper's rows (`GROUPS` in `table.py`: transactions, catalog and server are `other`;
SurrealDB's graph traversal is part of its executor and its transactions part of storage).

| | OrientDB | SurrealDB | ArangoDB |
|---|---|---|---|
| executable lines | 183,820 | 174,899 | 359,667 |
| covered lines | 45,655 | 39,350 | 87,405 |
| line coverage % | 24.84 | 22.50 | 24.30 |
| MC lines | 11,404 | 14,588 | 23,250 |
| MC % of covered lines | 24.98 | 37.07 | 26.60 |
| MC % of executable lines | 6.20 | 8.34 | 6.46 |
| background lines | 6,808 | 2,261 | 22,327 |
| replicate-noise lines | 5,052 | 3,746 | 19,172 |
| seeds | 595 | 427 | 190 |
| cases | 125,489 | 90,768 | 40,470 |
| twin Jaccard, MC before noise | 0.9415 | 0.9866 | 0.757 |

ArangoDB's twins agree less on MC than the other engines' do (Jaccard 0.757 before the
replicate noise is taken out), while their covered lines agree at 0.9987. Every line on
which they differ for the same variant is removed as replicate noise, so its figure is
the conservative one.

## Layout

```
reports/<engine>/report.json     every number, per component, generator and data-model pair
reports/<engine>/report.md       the same as tables
table.py                         the paper's tables from the report.json files
env/env.txt                      host, Python, image ids, the exact campaign commands
env/code.tgz                     the code that ran the campaigns (code.tgz.sha256 is the run's own record)
env/reports.txt                  every report command run (ArangoDB's names the tree's commit; the earlier ones are the attempts before the memory fix)
env/images.tsv                   the Docker images, by id and digest
env/binaries.sha256              the coverage builds of surreal and arangod, and the JaCoCo agent
env/builds/                      how the coverage builds were made (build scripts, patch, image Dockerfiles, logs)
env/maps/probe-lines-*.jsonl.gz  OrientDB's map from JaCoCo probes to source lines
env/python.txt                   the Python packages of the campaigns' environment
MANIFEST.sha256                  every file's checksum
```

## Code versions

- The campaigns ran the code in `env/code.tgz`, the `metamorphic-coverage` branch at
  `d9bc68f`.
- The reports: OrientDB and SurrealDB were computed with `53c5e8e`, and ArangoDB with
  `0891a12`. The commits in between change only how the report is computed (a dead
  worker's jobs run again, a seed's counters are summed in as it is read, a bounded
  cache), not what it computes. A test checks that the output is unchanged.

## Recomputing a report

From a checkout of the code, with the logs in `$EVAL/eval12h-shared/<engine>-{A,B}/`:

```bash
WORKERS=24 scripts/coverage/report_twins.sh eval12h-shared [orientdb surrealdb arangodb]
```

The report script prints more fields than are kept here; the paper's MC is its
`mc_pairwise_*` fields. OrientDB maps lines through `env/maps/`. SurrealDB and ArangoDB
map them through their coverage binaries (`env/builds/`), and ArangoDB's report runs in
the build image. On the ArangoDB logs (11 GB per twin) the report used about 155 GB of
memory at 24 workers, and took about 2 hours 20 minutes on a shared 128-core host. Fewer
workers use less memory.
