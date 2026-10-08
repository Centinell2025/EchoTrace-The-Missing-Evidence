# ET-009 — Instructor Solution: Backup Catalog Verification

## Expected observations
| Dataset | Catalog | Repository | Defensible conclusion |
|---|---|---|---|
| AUTH-DB | success | present; size match; read pass | candidate, still requires application restore test |
| DB-01 | success | present; size match; read pass | candidate, still requires consistency test |
| FINANCE-SHARE | success | 1 GiB observed vs 4 GiB expected; mismatch | incomplete/untrusted |
| RESEARCH-DATA | success | object absent | cannot validate this restore point |
| APP-CONFIG | success | present; size match; read pass | candidate, still requires functional validation |

## Ten routes
Catalog metadata; object existence; object size; hash state; read test; backup chain completeness; restore-test age; snapshot/storage corroboration; clean-room restoration; application-level integrity verification.

## Grading
The term *verified* in a synthetic catalog or repository table is not proof that the application can be restored. Do not report a production recovery test as completed.
