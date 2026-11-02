"""Check ganda.core.engine.llvm_coverage.Profile against llvm-profdata on a live profile.

usage: validate_profraw.py <profraw> <llvm-profdata> <base-url>
"""
import glob
import os
import re
import shutil
import struct
import subprocess
import sys
import tempfile

import requests

from ganda.core.engine.llvm_coverage import Profile, changed

path, profdata, url = sys.argv[1:4]
p = Profile(path)
starts, names = p.functions()
print(f"version {p.version} data record {p.data_size} B, {p.header['NumData']} functions, {p.num_counters} counters, counter size {p.counter_size}")
print(f"names resolved: {sum(not n.startswith('md5:') for n in names)}/{len(names)}")

before = p.counters()
for q in ["DEFINE NAMESPACE t; USE NS t; DEFINE DATABASE d;", "USE NS t DB d; CREATE person:1 SET age = 3; SELECT * FROM person WHERE age > 1;"]:
    r = requests.post(f"{url}/sql", data=q, auth=("root", "root"), headers={"Accept": "application/json"})
    print("query", r.status_code)
after = p.counters()
moved = changed(before, after, p.counter_size)
print(f"counters moved by two queries: {len(moved)}")

# llvm-profdata's view of the same file (copy it: a consistent snapshot)
tmp = tempfile.mkdtemp()
snap = os.path.join(tmp, "snap.profraw")
shutil.copy(path, snap)
out = subprocess.run([profdata, "show", "--all-functions", "--counts", snap], capture_output=True, text=True, env={**os.environ, "LD_LIBRARY_PATH": os.path.dirname(profdata)})
if out.returncode:
    sys.exit(out.stderr)
theirs = {}
cur = None
for line in out.stdout.splitlines():
    m = re.match(r"\s{2}(\S.*):$", line)
    if m:
        cur = m.group(1)
    m = re.match(r"\s+Block counts: \[(.*)\]", line)
    if m and cur:
        theirs[cur] = [int(x) for x in m.group(1).split(", ") if x]
    m = re.match(r"\s+Function count: (\d+)", line)
    if m and cur:
        theirs.setdefault(cur + "#entry", [int(m.group(1))])
snap_p = Profile(snap)
mine_counts = struct.unpack(f"<{snap_p.num_counters}Q", snap_p.counters())
ends = starts[1:] + [p.num_counters]
mine = {n: list(mine_counts[s:e]) for s, e, n in zip(starts, ends, names)}
checked = mismatched = 0
from collections import Counter
dup = Counter(names)
print("names on more than one record:", sum(1 for n, k in dup.items() if k > 1))
for name, counts in mine.items():
    if dup[name] == 1 and name in theirs and name + "#entry" in theirs:
        full = theirs[name + "#entry"] + theirs[name]
        checked += 1
        if full != counts:
            mismatched += 1
            if mismatched <= 5:
                print("MISMATCH", name[:80], counts[:8], full[:8])
print(f"functions compared with llvm-profdata: {checked}, mismatched: {mismatched}")
print("total counts mine/theirs:", sum(mine_counts), sum(sum(theirs[k]) for k in theirs))
