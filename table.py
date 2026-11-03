"""The paper's coverage tables (Tables 8-11) and per-pair MC, from reports/*/report.json:

    python3 table.py

The paper's MC is the reports' pairwise MC (`mc_pairwise_*`). The per-component tables
fold the reports' components into the paper's rows (`GROUPS`).
"""
import json
import pathlib

ENGINES = ["orientdb", "surrealdb", "arangodb"]
NAMES = {"orientdb": "OrientDB", "surrealdb": "SurrealDB", "arangodb": "ArangoDB"}
TABLE = {"orientdb": 8, "surrealdb": 9, "arangodb": 10}
ROWS = ["parser", "planner", "executor", "expressions", "graph", "indexes", "storage", "other"]
# a report component -> the paper's row; the rest keep their name
GROUPS = {
    "orientdb": {"transactions": "other", "catalog": "other", "server": "other"},
    "surrealdb": {"graph": "executor", "transactions": "storage", "catalog": "other", "server": "other"},
    "arangodb": {"transactions": "other", "catalog": "other", "server": "other"},
}


def pct(n, d):
    return f"{100.0 * n / d:.1f}" if d else "-"


def components(e, r):
    rows = {}
    for name, c in r["components"].items():
        row = rows.setdefault(GROUPS[e].get(name, name), [0, 0, 0])
        row[0] += c["lines"]
        row[1] += c["covered"]
        row[2] += c["mc_pairwise"]
    total, covered, mc = r["executable_lines"], r["covered_lines"], r["mc_pairwise_lines"]
    print(f"Table {TABLE[e]}: {NAMES[e]}, line coverage and MC per component\n")
    print("| component | LoC % | covered % | MC % of covered | MC % of LoC | share of MC % |")
    print("|---|---|---|---|---|---|")
    for name in ROWS:
        if name in rows:
            lines, cov, m = rows[name]
            print(f"| {name} | {pct(lines, total)} | {pct(cov, lines)} | {pct(m, cov)} | {pct(m, lines)} | {pct(m, mc)} |")
    print(f"| total | 100.0 | {pct(covered, total)} | {pct(mc, covered)} | {pct(mc, total)} | 100.0 |\n")


def main():
    here = pathlib.Path(__file__).parent
    reports = {e: json.loads((here / "reports" / e / "report.json").read_text()) for e in ENGINES}
    for e, r in reports.items():
        components(e, r)
    print("Table 11: Ganda's rows\n")
    print("| DBMS | LC % | MC % |")
    print("|---|---|---|")
    for e, r in reports.items():
        print(f"| {NAMES[e]} | {r['line_coverage_pct']:.2f} | {r['mc_pairwise_of_executable_pct']:.2f} |")
    print("\nMC per data-model pair, % of covered lines\n")
    pairs = sorted({p for r in reports.values() for p in r["data_model_pairs"]})
    print("| pair | " + " | ".join(NAMES[e] for e in ENGINES) + " |")
    print("|---" * (len(ENGINES) + 1) + "|")
    for p in pairs:
        print(f"| {p} | " + " | ".join(pct(reports[e]["data_model_pairs"][p]["mc_lines"], reports[e]["covered_lines"]) for e in ENGINES) + " |")
    split = json.loads((here / "reports" / "orientdb-parser-split" / "report.json").read_text())
    print("\nOrientDB's parser package, the generated parser against the AST classes\n")
    print("| part | executable | covered | MC lines | share of the parser's MC % | MC % of covered |")
    print("|---|---|---|---|---|---|")
    for name, c in split["components"].items():
        print(f"| {name} | {c['lines']:,} | {c['covered']:,} | {c['mc_pairwise']:,} | {pct(c['mc_pairwise'], split['mc_pairwise_lines'])} | {pct(c['mc_pairwise'], c['covered'])} |")
    print(f"| total (Table 8's parser row) | {split['executable_lines']:,} | {split['covered_lines']:,} | {split['mc_pairwise_lines']:,} | 100.0 | {pct(split['mc_pairwise_lines'], split['covered_lines'])} |")
    print("\nThe runs\n")
    print("| | " + " | ".join(NAMES[e] for e in ENGINES) + " |")
    print("|---" * (len(ENGINES) + 1) + "|")
    for label, get in (("executable lines", lambda r: r["executable_lines"]), ("covered lines", lambda r: r["covered_lines"]),
                       ("MC lines", lambda r: r["mc_pairwise_lines"]), ("MC % of covered", lambda r: r["mc_pairwise_of_covered_pct"]),
                       ("background lines", lambda r: r["background_lines"]), ("replicate-noise lines", lambda r: r["replicate_noise_lines"]),
                       ("seeds", lambda r: r["seeds"]), ("cases", lambda r: r["cases"]), ("cases with no MC", lambda r: r["zero_mc_pairwise_cases"]),
                       ("twin Jaccard, MC before noise", lambda r: r["agreement"]["mc_pairwise_jaccard_before_noise"]),
                       ("twin Jaccard, covered lines", lambda r: r["agreement"]["covered_jaccard"])):
        print(f"| {label} | " + " | ".join(f"{get(r):,}" if isinstance(get(r), int) else str(get(r)) for r in reports.values()) + " |")


if __name__ == "__main__":
    main()
