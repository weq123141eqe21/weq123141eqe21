import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data.json"

TITLE_TO_KEY = {
    "[vote] AI Research": "ai",
    "[vote] Computer Vision": "cv",
    "[vote] Long-tail Learning": "lt",
    "[vote] Student": "student",
    "[vote] Collaboration": "collab",
}

title = os.environ.get("ISSUE_TITLE", "")
voter = os.environ.get("VOTER", "").strip()

if title not in TITLE_TO_KEY:
    print("Not a recognized interaction issue.")
    sys.exit(0)

if not voter:
    raise SystemExit("Missing voter login.")

data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
key = TITLE_TO_KEY[title]
entry = data["options"][key]

if voter not in entry["voters"]:
    entry["voters"].append(voter)
    entry["voters"].sort(key=str.lower)
    entry["count"] = len(entry["voters"])
    print(f"Recorded {voter} for {key}.")
else:
    print(f"{voter} already voted for {key}; no duplicate count.")

all_voters = set()
for opt in data["options"].values():
    all_voters.update(opt["voters"])
    opt["count"] = len(opt["voters"])

data["total_unique_interactions"] = len(all_voters)
DATA_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

subprocess.run([sys.executable, str(ROOT / "scripts" / "render_stats.py")], check=True)
