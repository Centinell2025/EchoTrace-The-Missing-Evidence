# EchoTrace Instructor — ET-051 onward

**Private provisional instructor reasoning.** These are evidence-grounded answer notes, not claims of complete practical validation. A scenario lacking artifacts is **not yet fully playable**. For each question use ten applicable forensic paths: primary logs, SQL, filesystem, storage, backup, network, identity, application, independent collection, isolated restore. Mark N/A with justification.

## ET-057 — Deleted Archive Reconstruction

**Primary evidence:** `artifacts/data/data_scope.csv`

**Expected defensible answer:** No file fragments or deleted archive metadata supplied; archive reconstruction cannot yet be performed.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-058 — Entropy Change Assessment

**Primary evidence:** `artifacts/storage/storage_events.csv`

**Expected defensible answer:** No byte-level entropy evidence exists; encryption or compression claims are unsupported.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-059 — Storage Configuration Change

**Primary evidence:** `artifacts/storage/storage_events.csv`

**Expected defensible answer:** ST003 documents configuration change; request before/after config and change authorization.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-060 — Storage Recovery Validation

**Primary evidence:** `artifacts/backup/repository_inventory.csv`

**Expected defensible answer:** Object read-pass does not prove restored storage/application integrity.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-061 — Backup Catalog vs Repository

**Primary evidence:** `artifacts/backup/repository_inventory.csv`

**Expected defensible answer:** FINANCE-SHARE mismatch and RESEARCH-DATA absence contradict catalog success.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-062 — Broken Backup Chain

**Primary evidence:** `artifacts/backup/backup_catalog.csv`

**Expected defensible answer:** No full/incremental dependency chain supplied; chain completeness cannot be proven.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-063 — Missing Restore Point

**Primary evidence:** `artifacts/backup/repository_inventory.csv`

**Expected defensible answer:** obj-rd-0928 is absent despite catalog success.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-064 — Incremental Backup Dependency

**Primary evidence:** `artifacts/backup/backup_catalog.csv`

**Expected defensible answer:** No parent/child backup metadata; cannot establish incremental restore path.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-065 — Backup Hash Mismatch

**Primary evidence:** `artifacts/backup/repository_inventory.csv`

**Expected defensible answer:** obj-fin-0928 is mismatched and incomplete; untrusted for restore.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-066 — Immutable Backup Validation

**Primary evidence:** `artifacts/backup/repository_inventory.csv`

**Expected defensible answer:** No immutability/retention enforcement evidence; cannot assert WORM status.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-067 — Restore Test Forensics

**Primary evidence:** `artifacts/backup/backup_catalog.csv`

**Expected defensible answer:** Past test timestamps exist, but no test report confirms current recoverability.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-068 — Recovery Point Selection

**Primary evidence:** `artifacts/backup/repository_inventory.csv`

**Expected defensible answer:** DB-01 and AUTH-DB objects are candidates; functional restore remains unverified.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-069 — Clean-Room Restore

**Primary evidence:** `artifacts/backup/repository_inventory.csv`

**Expected defensible answer:** Define isolated restore, hash/consistency checks and safe cutover; no actual restore executed.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-070 — Backup Evidence Preservation

**Primary evidence:** `artifacts/forensics/surviving_evidence.csv`

**Expected defensible answer:** Preserve catalog, repository metadata and source hashes before corrective operations.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-071 — Virtual Machine Snapshot Analysis

**Primary evidence:** `scenario/ENTERPRISE_ARCHITECTURE.md`

**Expected defensible answer:** No VM snapshot evidence supplied; request hypervisor exports.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-072 — Hypervisor Event Timeline

**Primary evidence:** `scenario/ENTERPRISE_ARCHITECTURE.md`

**Expected defensible answer:** No hypervisor audit events supplied; VM actions cannot be reconstructed.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-073 — VM Disk Integrity

**Primary evidence:** `scenario/ENTERPRISE_ARCHITECTURE.md`

**Expected defensible answer:** No virtual disk images or hashes supplied; integrity cannot be validated.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-074 — Container Log Correlation

**Primary evidence:** `scenario/ENTERPRISE_ARCHITECTURE.md`

**Expected defensible answer:** No container logs supplied; container-specific findings unsupported.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-075 — Cloud Audit Timeline

**Primary evidence:** `scenario/ENTERPRISE_ARCHITECTURE.md`

**Expected defensible answer:** No cloud control-plane logs supplied; cloud event timeline unavailable.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-076 — Object Storage Recovery

**Primary evidence:** `artifacts/backup/repository_inventory.csv`

**Expected defensible answer:** Repository objects are not documented cloud object versions; cloud recovery requires separate evidence.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-077 — Cloud Identity Correlation

**Primary evidence:** `artifacts/orchestration/orch_events.csv`

**Expected defensible answer:** Service principal evidence is not cloud IAM audit; cloud attribution unsupported.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-078 — Container Volume Data Loss

**Primary evidence:** `artifacts/data/data_scope.csv`

**Expected defensible answer:** No container-volume mapping supplied; container-specific data loss unproven.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-079 — Orchestrator Baseline Analysis

**Primary evidence:** `artifacts/orchestration/orch_baseline.csv`

**Expected defensible answer:** JOB-X91 is outside approved schedules and target scope.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-080 — Adaptive Automation Assessment

**Primary evidence:** `artifacts/orchestration/orch_events.csv`

**Expected defensible answer:** Rapid multi-target execution supports automation; adaptive reasoning not proven.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-081 — AI-Assisted Activity Evidence

**Primary evidence:** `artifacts/orchestration/orch_events.csv`

**Expected defensible answer:** No model traces, agent plans or adaptive decision logs; AI use unproven.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

