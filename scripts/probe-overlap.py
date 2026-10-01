"""Measure how the six collections actually overlap.

Decides whether a stacked bar can be made non-inflating, and if so how:
by hatching real pairwise overlaps, or by assigning each record a single
primary collection.

    python3 scripts/probe-overlap.py
"""
import itertools
import json
import pathlib
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.adsabs.harvard.edu/v1/search/query"
COLS = ["earthscience", "physics", "general", "astronomy", "planetary", "heliophysics"]


def token():
    return (pathlib.Path.home() / ".ads" / "dev_key").read_text().strip()


def n(tok, q):
    url = API + "?" + urllib.parse.urlencode({"q": q, "rows": 0})
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {tok}"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)["response"]["numFound"]


def main():
    tok = token()
    total = n(tok, "*:*")
    print(f"total records {total:,}\n")

    singles = {c: n(tok, f"collection:{c}") for c in COLS}
    print("single collection counts")
    for c in COLS:
        print(f"  {c:<14}{singles[c]:>12,}")
    print(f"  {'SUM':<14}{sum(singles.values()):>12,}  "
          f"({sum(singles.values())/total-1:+.0%} vs total)\n")

    print("pairwise intersections, largest first")
    pairs = {}
    for a, b in itertools.combinations(COLS, 2):
        v = n(tok, f"collection:{a} AND collection:{b}")
        if v:
            pairs[(a, b)] = v
    for (a, b), v in sorted(pairs.items(), key=lambda kv: -kv[1]):
        print(f"  {a:<14}+ {b:<14}{v:>12,}")

    print("\nhow much of the excess is general science")
    sci = [c for c in COLS if c != "general"]
    sci_sum = sum(singles[c] for c in sci)
    only_general = n(tok, "collection:general NOT (" + " OR ".join(f"collection:{c}" for c in sci) + ")")
    print(f"  science collections sum      {sci_sum:>12,}")
    print(f"  total records                {total:>12,}")
    print(f"  excess without general       {sci_sum-total:>+12,} ({sci_sum/total-1:+.0%})")
    print(f"  records ONLY in general      {only_general:>12,}")

    print("\nrecords carrying more than one SCIENCE label")
    multi = 0
    for a, b in itertools.combinations(sci, 2):
        multi += pairs.get((a, b), 0) or pairs.get((b, a), 0)
    print(f"  sum of science pair intersections {multi:>12,}")
    print("  (an upper bound on double counting if general is dropped)")

    print("\nverdict")
    if sci_sum - total < total * 0.03:
        print("  Dropping general makes the science collections near-disjoint.")
        print("  A plain stack of the five science collections is honest.")
    else:
        print("  Science collections still overlap materially after dropping general.")
        print("  Either hatch the real pairwise overlaps, or assign one primary")
        print("  collection per record by priority so segments sum to the total.")


if __name__ == "__main__":
    main()
