#!/usr/bin/env python3
"""EchoTrace read-only structural QA. Run from any working directory."""
import csv
import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = [
 "artifacts/storage/storage_events.csv",
 "artifacts/monitoring/service_health.csv",
 "artifacts/orchestration/orch_events.csv",
 "artifacts/network/management_flows.csv",
 "artifacts/backup/backup_catalog.csv",
 "artifacts/backup/repository_inventory.csv",
 "submission/student/QUESTIONS.md",
 "submission/student/CASE_BRIEF.md",
 "submission/student/ADVANCED_INVESTIGATION.md",
 "submission/instructor/WRITEUP.md",
 "submission/instructor/ADVANCED_GRADING_RUBRIC.md",
]
def main():
    errors = []
    for rel in FILES:
        path = ROOT / rel
        if not path.is_file():
            errors.append("MISSING: " + rel)
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        print(digest + "  " + rel)
        if path.suffix == ".csv":
            with path.open(encoding="utf-8", newline="") as f:
                rows = list(csv.DictReader(f))
            if not rows:
                errors.append("EMPTY CSV: " + rel)
    q = ROOT / "submission/student/QUESTIONS.md"
    if q.exists():
        questions = [line for line in q.read_text().splitlines() if line[:2].strip(".").isdigit() and line[1:3] == ". "]
        if len(questions) != 10:
            errors.append("EXPECTED 10 questions, found " + str(len(questions)))
    for e in errors:
        print("FAIL:", e, file=sys.stderr)
    if errors:
        return 1
    print("PASS: static file inventory and nonempty CSV checks.")
    print("NOT VERIFIED: blind playtest, native artifact fidelity, password ZIP or hosted writeup.")
    return 0
if __name__ == "__main__":
    sys.exit(main())
