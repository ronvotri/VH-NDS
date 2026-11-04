"""Check local batch counts, duplicate IDs, and progress manifest without the source ROM."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "TIEN_DO.json").read_text(encoding="utf-8"))
seen = set()
total = 0
for batch in data["batches"]:
    path = ROOT / batch["repo_file"]
    lines = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(lines) == batch["done"], f"{path}: count mismatch"
    for item in lines:
        assert isinstance(item.get("id"), str) and isinstance(item.get("translation"), str) and item["translation"].strip()
        assert item["id"] not in seen, f"Duplicate ID: {item['id']}"
        seen.add(item["id"])
    total += len(lines)
assert total == data["translated_total"], f"Manifest {data['translated_total']} vs data {total}"
print(f"PASS: {total} entries, unique IDs, counts aligned across {len(data['batches'])} batches")
