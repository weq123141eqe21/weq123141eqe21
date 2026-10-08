import json
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "data.json").read_text(encoding="utf-8"))
OUT = ROOT / "assets" / "interaction-stats.svg"

items = list(DATA["options"].values())
total_votes = sum(x["count"] for x in items)
unique_people = DATA.get("total_unique_interactions", 0)

W, H = 700, 300
left = 210
bar_w = 385
bar_h = 18
start_y = 105
gap = 36

def pct(n):
    return (n / total_votes * 100) if total_votes else 0.0

rows = []
for i, item in enumerate(items):
    y = start_y + i * gap
    p = pct(item["count"])
    fill_w = bar_w * p / 100
    label = f'{item["emoji"]} {item["label"]}'
    rows.append(
        f'<text x="38" y="{y+14}" class="label">{escape(label)}</text>'
        f'<rect x="{left}" y="{y}" rx="9" ry="9" width="{bar_w}" height="{bar_h}" class="track"/>'
        f'<rect x="{left}" y="{y}" rx="9" ry="9" width="{fill_w:.1f}" height="{bar_h}" class="fill"/>'
        f'<text x="{left+bar_w+15}" y="{y+14}" class="value">{item["count"]} · {p:.0f}%</text>'
    )

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Profile interaction statistics">
<style>
  .bg {{ fill: #ffffff; }}
  .title {{ font: 700 22px -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif; fill:#24292f; }}
  .sub {{ font: 400 13px -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif; fill:#57606a; }}
  .label {{ font: 600 14px -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif; fill:#24292f; }}
  .value {{ font: 600 13px -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif; fill:#57606a; }}
  .track {{ fill:#eaeef2; }}
  .fill {{ fill:#2f81f7; }}
  .border {{ fill:none; stroke:#d0d7de; }}
  @media (prefers-color-scheme: dark) {{
    .bg {{ fill:#0d1117; }}
    .title,.label {{ fill:#e6edf3; }}
    .sub,.value {{ fill:#8b949e; }}
    .track {{ fill:#21262d; }}
    .fill {{ fill:#58a6ff; }}
    .border {{ stroke:#30363d; }}
  }}
</style>
<rect width="{W}" height="{H}" rx="16" class="bg"/>
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="15.5" class="border"/>
<text x="36" y="43" class="title">Community pulse</text>
<text x="36" y="68" class="sub">{total_votes} selections · {unique_people} unique GitHub visitors</text>
{''.join(rows)}
</svg>
'''
OUT.write_text(svg, encoding="utf-8")
print(f"Wrote {OUT}")
