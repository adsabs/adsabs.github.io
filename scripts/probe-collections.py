"""Find out what collection values the API really exposes, and on which host.

The first facet attempt came back with facet.field empty in the echoed params,
so the parameter was being dropped. This tries several spellings and both the
ADS and SciX hosts, then reports what actually works.

    python3 scripts/probe-collections.py
"""
import json
import pathlib
import urllib.error
import urllib.parse
import urllib.request

HOSTS = [
    ("ADS", "https://api.adsabs.harvard.edu/v1/search/query"),
    ("SciX", "https://api.scixplorer.org/v1/search/query"),
]


def token():
    return (pathlib.Path.home() / ".ads" / "dev_key").read_text().strip()


def get(tok, base, params):
    url = base + "?" + urllib.parse.urlencode(params, doseq=True)
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {tok}"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r), None
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code} {e.read().decode('utf-8','replace')[:160]}"
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"


def main():
    tok = token()

    for name, base in HOSTS:
        print(f"\n=== {name}: {base}")
        d, err = get(tok, base, {"q": "*:*", "rows": 0})
        if err:
            print(f"  reachable? no. {err}")
            continue
        print(f"  reachable. total records {d['response']['numFound']:,}")

        # facet spellings, in order of likelihood
        attempts = [
            {"q": "*:*", "rows": 0, "facet": "on", "facet.field": "collection", "facet.limit": 50, "facet.mincount": 1},
            {"q": "*:*", "rows": 0, "facet": "true", "facet.field": ["collection"], "facet.limit": 50},
            {"q": "*:*", "rows": 0, "json.facet": json.dumps({"collection": {"type": "terms", "field": "collection", "limit": 50}})},
        ]
        for i, params in enumerate(attempts, 1):
            d, err = get(tok, base, params)
            if err:
                print(f"  facet attempt {i}: {err}")
                continue
            fc = d.get("facet_counts", {}).get("facet_fields", {}).get("collection")
            if fc:
                print(f"  facet attempt {i} WORKED, values:")
                for v, n in zip(fc[0::2], fc[1::2]):
                    print(f"    {v:<20} {n:>12,}")
                break
            jf = d.get("facets", {}).get("collection", {}).get("buckets")
            if jf:
                print(f"  facet attempt {i} WORKED (json.facet), values:")
                for b in jf:
                    print(f"    {b['val']:<20} {b['count']:>12,}")
                break
            print(f"  facet attempt {i}: no facet block in response")

    # whatever the facet says, confirm the two the user asked about directly
    print("\n=== direct counts for the disciplines in question")
    for name, base in HOSTS[:1]:
        print(f"  on {name}:")
        cands = ["astronomy", "earthscience", "heliophysics", "planetary", "physics",
                 "general", "biophysical", "bps", "biological", "lifescience",
                 "solarphysics", "spacephysics", "geophysics", "climate", "ocean",
                 "engineering", "computerscience", "cs", "math", "chemistry",
                 "education", "history", "instrumentation", "software", "data"]
        for q in [f"collection:{c}" for c in cands]:
            d, err = get(tok, base, {"q": q, "rows": 0})
            if err:
                continue
            n = d["response"]["numFound"]
            if n:
                print(f"    {q:<32} {n:>12,}")


if __name__ == "__main__":
    main()
