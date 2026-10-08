# EchoTrace Instructor — ET-001 onward

**Private provisional instructor reasoning.** These are evidence-grounded answer notes, not claims of complete practical validation. A scenario lacking artifacts is **not yet fully playable**. For each question use ten applicable forensic paths: primary logs, SQL, filesystem, storage, backup, network, identity, application, independent collection, isolated restore. Mark N/A with justification.

## ET-003 — SQL Privilege and Job Investigation

**Primary evidence:** `training/sql/seed.sql`

**Expected defensible answer:** Correlate SQL-A002 and SQL-A003 via JOB-X91; svc_orch is a service principal; human attribution is unproven.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-004 — Database Timeline from LSNs

**Primary evidence:** `training/sql/seed.sql`

**Expected defensible answer:** No native SQL Server LSN records are supplied; a true LSN-based ordering cannot be proven from SQLite timestamps.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-005 — Stored Procedure Change

**Primary evidence:** `training/sql/schema.sql`

**Expected defensible answer:** No stored-procedure definition/history is supplied. The correct conclusion is insufficient evidence; request DDL audit and signed schema baseline.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-006 — SQL Audit Gap Reconstruction

**Primary evidence:** `training/sql/seed.sql`

**Expected defensible answer:** Available audit records are sparse; absence of an event does not prove absence of activity. Require independent audit retention and database engine logs.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-008 — Database File Integrity

**Primary evidence:** `training/sql/schema.sql`

**Expected defensible answer:** MDF/LDF physical corruption cannot be tested against SQLite schema and seed data; request valid SQL Server forensic images.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-010 — SQL Agent Job Forensics

**Primary evidence:** `artifacts/orchestration/orch_events.csv`

**Expected defensible answer:** JOB-X91 is not listed as approved in orchestration baseline; it is not established to be a native SQL Agent job.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-012 — Transaction Rollback Investigation

**Primary evidence:** `training/sql/seed.sql`

**Expected defensible answer:** TX-003 is recorded rolled_back; TX-002 is unknown. Do not infer durable changes from unknown state.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-013 — Database Snapshot Integrity

**Primary evidence:** `artifacts/backup/backup_catalog.csv`

**Expected defensible answer:** Catalog metadata does not establish snapshot integrity; require snapshot chain and isolated mount/consistency validation.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-014 — Sensitive Table Access Scoping

**Primary evidence:** `training/sql/seed.sql`

**Expected defensible answer:** No table-level query access logs are supplied; cannot determine sensitive-row access from job metadata.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-015 — Database Recovery Point Analysis

**Primary evidence:** `artifacts/backup/repository_inventory.csv`

**Expected defensible answer:** DB-01 object is present and read-pass; application-consistent recovery is unverified.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-016 — Windows Event Correlation

**Primary evidence:** `artifacts/monitoring/service_health.csv`

**Expected defensible answer:** Monitoring events are not native Windows EVTX; Windows event attribution requires separately collected Security/System logs.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-017 — NTFS MFT Reconstruction

**Primary evidence:** `artifacts/forensics/surviving_evidence.csv`

**Expected defensible answer:** No native MFT image exists in the current set; require offline image or clearly labeled MFT-like export.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-018 — USN Journal Timeline

**Primary evidence:** `artifacts/forensics/surviving_evidence.csv`

**Expected defensible answer:** No USN journal records are supplied; a USN-specific sequence cannot be reconstructed.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-019 — Prefetch Execution Analysis

**Primary evidence:** `artifacts/forensics/surviving_evidence.csv`

**Expected defensible answer:** No Prefetch artifacts are supplied; process execution requires independent collection.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-020 — Amcache Program Evidence

**Primary evidence:** `artifacts/forensics/surviving_evidence.csv`

**Expected defensible answer:** No Amcache hive is supplied; installation/execution conclusions cannot be established.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-021 — Registry Persistence Investigation

**Primary evidence:** `artifacts/forensics/surviving_evidence.csv`

**Expected defensible answer:** No registry hive or autorun evidence exists in the current dataset; persistence is unproven.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-022 — Windows Service Change Analysis

**Primary evidence:** `artifacts/monitoring/service_health.csv`

**Expected defensible answer:** Service health is not a Windows service configuration audit; request service-control and registry evidence.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-023 — Scheduled Task Forensics

**Primary evidence:** `artifacts/orchestration/orch_events.csv`

**Expected defensible answer:** Orchestration jobs are not evidence of Windows Scheduled Tasks; request TaskScheduler logs and task definitions.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-024 — PowerShell Evidence Correlation

**Primary evidence:** `artifacts/orchestration/orch_events.csv`

**Expected defensible answer:** Management connections do not prove PowerShell execution; request PowerShell operational and process telemetry.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-026 — Active Directory Authentication Timeline

**Primary evidence:** `artifacts/monitoring/service_health.csv`

**Expected defensible answer:** ID-01 authentication degradation begins H003 at 02:14:18 UTC; authentication user/session records are not supplied.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-027 — Kerberos Event Correlation

**Primary evidence:** `artifacts/monitoring/service_health.csv`

**Expected defensible answer:** No Kerberos event records supplied; cannot claim ticket abuse or protocol-specific failure.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-028 — Privileged Group Change Investigation

**Primary evidence:** `artifacts/orchestration/orch_baseline.csv`

**Expected defensible answer:** Service account baseline is present; no AD group membership change events supplied.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-029 — Service Account Baseline Deviation

**Primary evidence:** `artifacts/orchestration/orch_events.csv`

**Expected defensible answer:** JOB-X91 falls outside the documented ORCH-01 schedule; deviation does not prove compromise.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-030 — Identity Outage Dependency Analysis

**Primary evidence:** `scenario/ENTERPRISE_ARCHITECTURE.md`

**Expected defensible answer:** Identity services depend on AUTH-DB, which depends on storage; correlate H003/H004 and ST001/ST003.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-031 — GPO Change Forensics

**Primary evidence:** `scenario/ENTERPRISE_ARCHITECTURE.md`

**Expected defensible answer:** No GPO modification logs are supplied; do not assert policy tampering.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

