# EchoTrace — Private Instructor Writeup

**CONFIDENTIAL ANSWER KEY — DO NOT SHIP IN STUDENT ZIP**

## Evidence-grounded answers

1. `ST001|2026-09-28T02:10:22Z` — `storage_events.csv` ST001. Service-health baseline H002 at 02:08:00Z.
2. `JOB-X91` — `orch_events.csv` O003–O012 (`approved_job=no`).
3. `svc_orch|ORCH-01` — `orch_events.csv` O003.
4. `STORAGE-01` — O003 at 02:12:01.120Z.
5. `O011` — O011 `metadata_operation`, target STORAGE-01, result `accepted`; accepted does not establish durable application.
6. `H003` — `service_health.csv` H003 at 02:14:18Z.
7. `ST009` — `storage_events.csv` ST009 at 02:32:51Z.
8. `APP-01|H009` — H009 02:31:07Z precedes APP-02 H010 02:31:19Z.
9. `BKP1003` — `backup_catalog.csv` BKP1003 refers to `obj-fin-0928` expected 4294967296 bytes; `repository_inventory.csv` reports present yes, observed 1073741824, mismatch, read fail.
10. `BKP1004` — catalog BKP1004 `success` for `obj-rd-0928`; repository inventory says present no, observed 0, unavailable, read fail.

## Forensic reconstruction
Healthy baseline H001/H002 at 02:08Z; first storage warning ST001 at 02:10:22Z; JOB-X91 begins O003 at 02:12:01.120Z; storage config change ST003 02:13:41Z and orchestration accepted operation O011 02:13:41.004Z; ID-01 degrades H003 02:14:18Z; APP-01 down H009 02:31:07Z; protective storage read-only ST009 02:32:51Z; DB-01 read-only H011 02:33:42Z.

**Interpretation:** storage warning predates JOB-X91, so do not infer the job initiated all faults. Subsecond orchestration intervals may suggest automation, not AI or a human attacker. Network flow logs show internal management communication, not external exfiltration. Catalog success is not evidence of a restorable backup. Repository absence does not establish irreversible loss.

## Reproduction
Run `python3 submission/validate_case.py` from the repository root. Confirm answer values independently with a CSV reader. All artifacts are synthetic.
