"""Render the growth chart from _data/collection_growth.yml.

Writes _includes/_about/growth-chart.html.

The data is a true partition: every record counted once, assigned to its most
specific collection, so the stack sums to the number of records actually
loaded and nothing is inflated.

Two things the drawing has to be honest about:

1. The axis is linear and must stay linear. Stacked bars cannot use a log
   axis, because segments on a log scale do not add up to the height of the
   stack. If the early years look small it is because they are.

2. entdate is when a record was LOADED. Collection labels were applied
   retroactively across the whole corpus, so a bar says "records loaded that
   year, by the collection they belong to today". It is a picture of the work
   of building the collection, not of when a field was founded.
"""
import pathlib
import re

W, H = 900, 350
L, R, T, B = 58, 12, 18, 44
SM_W, SM_H = 900, 250

# bottom of the stack first
COLS = [
    ("earthscience", "Earth science", "#2e9c8a"),
    ("physics", "Physics", "#1c459b"),
    ("general", "General science", "#8fa3bb"),
    ("astronomy", "Astronomy", "#049dd9"),
    ("planetary", "Planetary", "#e08a2e"),
    ("heliophysics", "Heliophysics", "#c2185b"),
]


def nice_ceiling(v):
    """Round up to a readable axis top: 1, 1.5, 2, 2.5, 3, 4, 5, 6, 8 or 10 x a power of ten."""
    if v <= 0:
        return 1
    import math
    power = 10 ** math.floor(math.log10(v))
    for mult in (1, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10):
        if v <= mult * power:
            return mult * power
    return 10 * power


def fmt(v):
    if v >= 1_000_000:
        t = f"{v/1_000_000:.1f}".rstrip("0").rstrip(".")
        return f"{t}M"
    if v >= 1_000:
        return f"{v/1_000:.0f}k"
    return str(int(v))


def load():
    text = pathlib.Path("_data/collection_growth.yml").read_text()
    rows, cur = [], None
    for line in text.splitlines():
        m = re.match(r"\s*- year: (\d+)", line)
        if m:
            cur = {"year": int(m.group(1))}
            rows.append(cur)
            continue
        m = re.match(r"\s{4}([a-z_]+): (\d+)", line)
        if m and cur is not None:
            cur[m.group(1)] = int(m.group(2))
    return [r for r in rows if r.get("all", 0) > 0]


def main():
    rows = load()
    top = max(r["all"] for r in rows)
    axis_max = (int(top // 2_000_000) + 1) * 2_000_000

    plot_w, plot_h = W - L - R, H - T - B
    step = plot_w / len(rows)
    bar_w = min(step * 0.7, 22)

    def y(v):
        return T + plot_h - (v / axis_max) * plot_h

    o = []
    o.append('<figure class="about-chart">')
    o.append(f'  <svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="gc-t gc-d">')
    o.append('    <title id="gc-t">Records added to the collection each year, by discipline</title>')
    o.append('    <desc id="gc-d">From 1995 to 2022 the collection takes in '
             'between fifty thousand and a million records a year. In 2023 that rises to '
             '2.4 million, in 2024 to 5.5 million, and in 2025 and 2026 to about 7.5 million. '
             'Earth science accounts for most of the increase.</desc>')
    o.append('    <defs><pattern id="gc-hatch" width="5" height="5" patternUnits="userSpaceOnUse" '
             'patternTransform="rotate(45)">'
             '<line x1="0" y1="0" x2="0" y2="5" stroke="#1c459b" stroke-width="2.2" '
             'stroke-opacity="0.55"/></pattern></defs>')

    for v in range(0, axis_max + 1, 2_000_000):
        o.append(f'    <line class="gc-grid" x1="{L}" y1="{y(v):.1f}" x2="{W-R}" y2="{y(v):.1f}" />')
        o.append(f'    <text class="gc-ylab" x="{L-8}" y="{y(v)+4:.1f}" text-anchor="end">{v//1_000_000}M</text>')

    for i, r in enumerate(rows):
        x = L + i * step + (step - bar_w) / 2
        base = 0.0
        for key, _, colour in COLS:
            v = r.get(key, 0)
            if v <= 0:
                continue
            h = (v / axis_max) * plot_h
            o.append(f'    <rect x="{x:.1f}" y="{y(base)-h:.1f}" width="{bar_w:.1f}" '
                     f'height="{h:.1f}" fill="{colour}" />')
            if key == "earthscience":
                # the slice of Earth science that is also physics
                ep = min(r.get("earth_physics", 0), v)
                if ep > 0:
                    eh = (ep / axis_max) * plot_h
                    o.append(f'    <rect x="{x:.1f}" y="{y(base)-eh:.1f}" width="{bar_w:.1f}" '
                             f'height="{eh:.1f}" fill="url(#gc-hatch)" />')
            base += v
        yr = r["year"]
        if yr % 5 == 0 or yr == rows[-1]["year"] or yr == rows[0]["year"]:
            o.append(f'    <text class="gc-xlab" x="{x + bar_w/2:.1f}" y="{H-B+18}" '
                     f'text-anchor="middle">{yr}</text>')

    o.append(f'    <line class="gc-axis" x1="{L}" y1="{y(0):.1f}" x2="{W-R}" y2="{y(0):.1f}" />')
    o.append('  </svg>')

    # per-discipline panels, each on its own scale
    cols_n, rows_n = 3, 2
    pw, ph = SM_W / cols_n, SM_H / rows_n
    o.append(f'  <svg class="gc-sm" viewBox="0 0 {SM_W} {SM_H}" role="img" '
             f'aria-label="Each discipline on its own scale, records added per year from 1995 to 2026">')
    for idx, (key, label, colour) in enumerate(COLS):
        cx, cy = (idx % cols_n) * pw, (idx // cols_n) * ph
        peak = max(r.get(key, 0) for r in rows) or 1
        top_ = nice_ceiling(peak)
        # plot box inside the panel, leaving a gutter for the y labels
        px0, px1 = cx + 46, cx + pw - 14
        py0, py1 = cy + 24, cy + ph - 28
        inner = py1 - py0
        bw = (px1 - px0) / len(rows)

        o.append(f'    <text class="gc-sm-title" x="{cx+8:.0f}" y="{cy+15:.0f}">{label}</text>')

        # y axis: top, midpoint and zero
        for frac in (1.0, 0.5, 0.0):
            val = top_ * frac
            yy = py1 - frac * inner
            if frac > 0:
                o.append(f'      <line class="gc-sm-grid" x1="{px0:.0f}" y1="{yy:.1f}" x2="{px1:.0f}" y2="{yy:.1f}" />')
            o.append(f'      <text class="gc-sm-ylab" x="{px0-6:.0f}" y="{yy+3.5:.1f}" text-anchor="end">{fmt(val)}</text>')

        for i, r in enumerate(rows):
            h = (r.get(key, 0) / top_) * inner
            o.append(f'      <rect x="{px0 + i*bw:.1f}" y="{py1-h:.1f}" '
                     f'width="{max(bw-1.1,0.9):.1f}" height="{max(h,0.5):.1f}" fill="{colour}" />')

        o.append(f'    <line class="gc-sm-axis" x1="{px0:.0f}" y1="{py1:.0f}" x2="{px1:.0f}" y2="{py1:.0f}" />')
        o.append(f'    <text class="gc-sm-lab" x="{px0:.0f}" y="{py1+14:.0f}">1995</text>')
        o.append(f'    <text class="gc-sm-lab" x="{px1:.0f}" y="{py1+14:.0f}" text-anchor="end">2026</text>')
    o.append('  </svg>')
    o.append('  <p class="gc-sm-note">Each subject on its own scale, so the smaller ones '
             'can be seen. Note the different y axes: compare the shapes, not the heights.</p>')

    o.append('  <ul class="gc-legend">')
    for _, label, colour in COLS:
        o.append(f'    <li><i style="background:{colour}"></i>{label}</li>')
    o.append('    <li><i class="gc-legend-hatch"></i>Earth science that is also physics</li>')
    o.append('  </ul>')
    o.append('  <figcaption>Records are counted by the year they joined the collection, '
             'not the year they were published. Hatching marks papers that are both Earth '
             'science and physics.</figcaption>')
    o.append('</figure>')

    dest = pathlib.Path("_includes/_about/growth-chart.html")
    dest.write_text("\n".join(l for l in o if l) + "\n")
    print(f"wrote {dest}: {len(rows)} years, {rows[0]['year']} to {rows[-1]['year']}")
    print(f"axis max {axis_max:,}, peak year {top:,}")


if __name__ == "__main__":
    main()
