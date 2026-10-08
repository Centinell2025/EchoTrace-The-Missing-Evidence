# ET-025 — Instructor Solution: Enterprise Capstone (Current Evidence)

## Expected high-confidence observations
- `ST001` storage path latency at 02:10:22 UTC predates unexplained orchestration `O003` at 02:12:01.120 UTC.
- `ST003` metadata configuration change at 02:13:41 UTC precedes identity degradation `H003` at 02:14:18 UTC.
- `H009/H010`: application nodes down at 02:31:07 and 02:31:19 UTC.
- `ST009`: protective read-only transition at 02:32:51 UTC.
- `H011`: DB-01 read-only at 02:33:42 UTC.
- Backup catalog success is contradicted by missing/incomplete repository objects for RESEARCH-DATA and FINANCE-SHARE.
- No evidence proves AI-assisted targeting or permanent loss of all copies.

## Causation caveat
The earliest observed storage anomaly precedes JOB-X91. A targeted change may have aggravated the incident, but the current synthetic evidence does **not** uniquely prove that JOB-X91 caused the entire outage.

## Recovery priorities
Preserve primary and independent evidence; acquire configuration and backup metadata; isolate suspicious management activity under authorized incident command; validate known-good storage/identity state; test backup objects in a clean room; restore foundational dependencies before applications; document residual uncertainty and monitoring.

## Ten forensic routes
Monitoring; storage; orchestration; network; identity dependencies; SQL transaction data; backup catalog; repository validation; surviving evidence; isolated recovery testing.

## Instructor limitation
This is a provisional evidence-based solution, not a completed playtest or proof of functional enterprise recovery.
