import csv
import sys
from pathlib import Path

P95_THRESHOLD_MS = 8000
ERROR_RATE_MAX = 0.02

stats_file = Path("load_tests/results_stats.csv")
if not stats_file.exists():
    print("Locust stats CSV not found.")
    sys.exit(1)

failures = []
with stats_file.open() as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["Name"] == "Aggregated":
            p95 = float(row.get("95%", 0))
            total = float(row.get("Request Count", 1))
            errors = float(row.get("Failure Count", 0))
            error_rate = errors / max(total, 1)
            if p95 > P95_THRESHOLD_MS:
                failures.append(f"p95 latency {p95}ms > threshold {P95_THRESHOLD_MS}ms")
            if error_rate > ERROR_RATE_MAX:
                failures.append(f"Error rate {error_rate*100:.1f}% > max {ERROR_RATE_MAX*100:.1f}%")

if failures:
    for msg in failures:
        print(msg)
    sys.exit(1)

print("Load test thresholds passed.")
sys.exit(0)
