# ET-001 — Instructor Solution: SQL Transaction Forensics

**Evidence:** `training/sql/schema.sql`, `training/sql/seed.sql`; synthetic SQLite records, not native SQL Server LSN/MDF/LDF.

## Verified expected findings from supplied seed data
- `TX-001`: `committed` at 2026-09-28 02:08:00 UTC.
- `TX-002`: `unknown` at 02:24:51 UTC; do **not** claim successful commit.
- `TX-003`: `rolled_back` at 02:26:03 UTC; do **not** claim durable change.
- `SQL-A003`: retention reference update was `accepted`, not independently verified as durable.
- `SQL-A002` and `SQL-A003` share correlation `JOB-X91`; that associates records with a job, not a human or AI operator.

## Read-only validation
```sql
SELECT tx_id,event_time_utc,dataset_id,operation,commit_state FROM transactions ORDER BY event_time_utc;
SELECT event_id,event_time_utc,principal_id,action,result,correlation_id FROM audit_events ORDER BY event_time_utc;
```

## Ten forensic routes
1. Transaction table: direct commit-state evidence.
2. Audit table: link related actions.
3. Correlation ID: establish shared job context.
4. Principal registry: identify account type, not operator.
5. Dataset inventory: map business impact.
6. Backup catalog: identify candidate prior recovery points.
7. Repository object state: test whether candidates are present.
8. Orchestration records: correlate JOB-X91 timeline.
9. Service health: compare operational degradation.
10. Isolated copy validation: require real database integrity tests before recovery approval.

## Grading
Full credit requires distinguishing accepted, committed, rolled back, and unknown. Reject unsupported attribution or permanent-loss claims. Confidence: high for the *synthetic recorded states*, lower for underlying real-world causation.
