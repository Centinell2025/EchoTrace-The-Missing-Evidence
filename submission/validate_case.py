#!/usr/bin/env python3
"""Read-only, standard-library validation of the EchoTrace Sherlock candidate."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "storage": ROOT / "artifacts/storage/storage_events.csv",
    "health": ROOT / "artifacts/monitoring/service_health.csv",
    "orch": ROOT / "artifacts/orchestration/orch_events.csv",
    "network": ROOT / "artifacts/network/management_flows.csv",
    "catalog": ROOT / "artifacts/backup/backup_catalog.csv",
    "inventory": ROOT / "artifacts/backup/repository_inventory.csv",
}

def load(path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def main():
    d = {name: load(path) for name, path in FILES.items()}
    st = {r["event_id"]: r for r in d["storage"]}
    h = {r["event_id"]: r for r in d["health"]}
    o = {r["event_id"]: r for r in d["orch"]}
    c = {r["backup_id"]: r for r in d["catalog"]}
    inv = {r["object_id"]: r for r in d["inventory"]}
    assert st["ST001"]["timestamp_utc"] == "2026-09-28T02:10:22Z"
    assert o["O003"]["job_id"] == "JOB-X91"
    assert o["O003"]["identity"] == "svc_orch" and o["O003"]["source"] == "ORCH-01"
    assert o["O003"]["target"] == "STORAGE-01"
    assert o["O011"]["action"] == "metadata_operation" and o["O011"]["result"] == "accepted"
    assert h["H003"]["asset"] == "ID-01" and h["H003"]["state"] == "degraded"
    assert st["ST009"]["event"] == "protective_read_only"
    assert h["H009"]["asset"] == "APP-01" and h["H009"]["timestamp_utc"] < h["H010"]["timestamp_utc"]
    fin = inv[c["BKP1003"]["repository_object"]]
    assert fin["present"] == "yes" and fin["object_hash_state"] == "mismatch" and fin["read_test"] == "fail"
    research = inv[c["BKP1004"]["repository_object"]]
    assert research["present"] == "no" and research["read_test"] == "fail"
    assert len(d["network"]) >= 9
    print("PASS: six evidence CSVs parsed and ten Sherlock answers cross-checked.")
    print("NOTE: passing assertions does not substitute for independent student playtesting.")

if __name__ == "__main__":
    main()
