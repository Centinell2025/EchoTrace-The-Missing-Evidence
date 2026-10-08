# ET-002 — Instructor Solution: SQL Data Loss & Recovery

**Sources:** `training/sql/seed.sql`, `artifacts/backup/backup_catalog.csv`, `artifacts/backup/repository_inventory.csv`, `artifacts/data/data_scope.csv`.

## Expected findings
- TRANSACTIONS / DB-01: backup object `obj-db-0927` is present, expected-sized and marked hash-match/read-pass in synthetic repository evidence. Functional consistency and successful restoration are **not proven**.
- FINANCE-SHARE: catalog expects 4,294,967,296 bytes; repository inventory shows 1,073,741,824 bytes and mismatch/read failure. Do not treat as verified recovery point.
- RESEARCH-DATA: catalog success but repository object `obj-rd-0928` absent. This is not proof that all copies are permanently lost.
- `TX-002` unknown; `TX-003` rolled back. Neither proves a durable destructive transaction.

## Read-only query
```sql
SELECT c.backup_id,c.dataset_id,c.status,c.expected_bytes,r.present,r.observed_bytes,r.integrity_state
FROM backup_catalog c LEFT JOIN repository_objects r ON c.object_id=r.object_id
ORDER BY c.backup_id;
```

## Ten forensic routes
Catalog; repository inventory; size reconciliation; integrity state; read test; transaction state; dataset availability; independent storage metadata; acquisition of alternate copies; clean-room restore validation.

## Grading
Separate **unavailable**, **unverified**, **incomplete backup**, **recoverable candidate**, and **permanent loss**. The supplied evidence cannot prove permanent loss.
