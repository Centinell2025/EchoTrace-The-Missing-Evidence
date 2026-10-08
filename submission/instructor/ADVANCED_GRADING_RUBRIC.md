# Instructor-only — Advanced Investigation Grading Rubric

**Do not include in the student ZIP.** Score out of 100.

## A. Causality and timeline — 25
- 12: chronology includes H002 02:08; ST001 02:10:22; O003 02:12:01.120; ST003 02:13:41; H003 02:14:18; H009 02:31:07; ST009 02:32:51; H011 02:33:42. Allow a ninth correctly cited event.
- 9: compares competing hypotheses without confusing temporal order and causation; ST001 precedes O003.
- 4: O011 'accepted' is not confirmed durable write or malicious attribution.

## B. Automation and network — 20
- 8: correlates O003–O009 with N003–N009 on host and coarse time; flows do not preserve millisecond ordering.
- 6: approved O001/O002 at 26,000 ms versus rapid JOB-X91 intervals (187,204,181,312,407,388 ms), distinct targets.
- 6: identifies scheduler logs, process lineage, identity/authentication records, configuration diffs and independent network captures as additional evidence; does not claim AI.

## C. Backup — 25
- 12: catalog to inventory join: BKP1001 AUTH-DB match/read pass; BKP1002 DB-01 match/pass; BKP1003 FINANCE-SHARE expected 4294967296 observed 1073741824, mismatch/fail; BKP1004 RESEARCH-DATA absent/fail; BKP1005 APP-CONFIG match/pass.
- 4: FINANCE-SHARE 25% observed versus expected (75% deficit).
- 4: read/hash are not proof of transactional consistency or successful restore.
- 5: clean-room restore, hash validation, service/application checks, RPO/RTO and rollback gates.

## D. Cross-platform / IoT — 15
- 7: collector timestamps are UTC; device offsets +42s, -15s, +7s in inventory; don't apply device offset to already-normalized collector timestamps.
- 8: synthetic event-like exports cannot establish raw EVTX provenance, NTFS MFT/USN sequence fidelity or original journald integrity.

## E. Reporting — 15
- 8: fact/inference/hypothesis/unknown boundaries, no invented exfiltration/AI/permanent loss.
- 7: targeted additional acquisition and non-destructive recovery validation.

## Instructor acceptance gates
Require 85+ points and no critical evidentiary misstatement for a passing expert report. For an Insane difficulty label, independent blind playtest and calibration against actual HTB submissions are still necessary.
