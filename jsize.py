import sys
import json
import gzip
from tabulate import tabulate

def friendly_size(n):
    return str(n / 1000.)

def both_sizes(j):
    bs = json.dumps(j).encode()
    return (len(bs), len(gzip.compress(bs)))

with open(sys.argv[1], 'r') as f:
    j = json.load(f)
    tab = []
    (a, b) = both_sizes(j)
    total_bs = a
    tab.append(("total", friendly_size(a), friendly_size(b), 1))
    subs = []
    for k in j.keys():
        (a, b) = both_sizes(j[k])
        subs.append((k, a, b))
    subs = sorted(subs, key=lambda x: -x[1])
    for (k, n, n2) in subs:
        tab.append((k, friendly_size(n), friendly_size(n2), "{0:.2f}".format(n / float(total_bs))))
    print(tabulate(tab, headers=("key", "kb", "gzip", "frac")))
