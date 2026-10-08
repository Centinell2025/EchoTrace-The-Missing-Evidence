# EchoTrace Instructor — ET-076 onward

**Private provisional instructor reasoning.** These are evidence-grounded answer notes, not claims of complete practical validation. A scenario lacking artifacts is **not yet fully playable**. For each question use ten applicable forensic paths: primary logs, SQL, filesystem, storage, backup, network, identity, application, independent collection, isolated restore. Mark N/A with justification.

## ET-082 — Human vs Script vs Adaptive Automation

**Primary evidence:** `artifacts/orchestration/orch_events.csv`

**Expected defensible answer:** Millisecond cadence is consistent with scripts; not diagnostic of AI.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-083 — Machine-Speed Event Sequencing

**Primary evidence:** `artifacts/orchestration/orch_events.csv`

**Expected defensible answer:** O003-O010 occur within about two seconds; compare with approved baseline.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-084 — Automated Target Selection Analysis

**Primary evidence:** `artifacts/orchestration/orch_events.csv`

**Expected defensible answer:** Targets span storage, database, backup and apps; selection rationale not recorded.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-085 — AI Claim Evidentiary Limits

**Primary evidence:** `artifacts/orchestration/orch_events.csv`

**Expected defensible answer:** No evidence uniquely attributes activity to AI; defensible answer is inconclusive.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-086 — Chain of Custody Engineering

**Primary evidence:** `artifacts/forensics/surviving_evidence.csv`

**Expected defensible answer:** Source collection timestamps and limitations exist; cryptographic chain-of-custody manifest not yet finalized.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-087 — Evidence Hash Verification

**Primary evidence:** `artifacts/forensics/surviving_evidence.csv`

**Expected defensible answer:** No final SHA-256 manifest published; do not fabricate digests.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-088 — Acquisition Strategy Under Outage

**Primary evidence:** `artifacts/forensics/surviving_evidence.csv`

**Expected defensible answer:** Prioritize volatile and independent evidence, preserve originals before recovery.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-089 — Timeline Conflict Resolution

**Primary evidence:** `artifacts/monitoring/service_health.csv`

**Expected defensible answer:** ST001 precedes JOB-X91; do not force all failure causation onto JOB-X91.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-090 — Evidence Source Reliability

**Primary evidence:** `artifacts/forensics/surviving_evidence.csv`

**Expected defensible answer:** SOC mirror and collector provide independent corroboration with stated limitations.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-091 — Data Loss Classification

**Primary evidence:** `artifacts/data/data_scope.csv`

**Expected defensible answer:** Separate unavailable, partial, backup-incomplete and unverified from permanent loss.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-092 — Breach Scope Engineering

**Primary evidence:** `artifacts/network/management_flows.csv`

**Expected defensible answer:** No payload or external data evidence establishes breach/exfiltration.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-093 — Root Cause vs Symptom Analysis

**Primary evidence:** `artifacts/storage/storage_events.csv`

**Expected defensible answer:** ST001 early degradation; ST003 change; H009 application outage are distinct phases.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-094 — Forensic Recovery Sequencing

**Primary evidence:** `scenario/ENTERPRISE_ARCHITECTURE.md`

**Expected defensible answer:** Validate storage and identity/database dependencies before application restoration.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-095 — Post-Recovery Validation

**Primary evidence:** `artifacts/backup/repository_inventory.csv`

**Expected defensible answer:** Require clean-room integrity, consistency, service tests and monitored cutover.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-096 — Business Continuity Evidence

**Primary evidence:** `scenario/ASSET_INVENTORY.csv`

**Expected defensible answer:** P1 foundational services precede P2 apps; business RTO/RPO must be approved separately.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-097 — Disaster Recovery Decision

**Primary evidence:** `artifacts/data/data_scope.csv`

**Expected defensible answer:** Recovery priority must consider evidence integrity and unknown restore feasibility.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-098 — Critical Dependency Restoration

**Primary evidence:** `scenario/ENTERPRISE_ARCHITECTURE.md`

**Expected defensible answer:** Restore foundational identity/storage/data dependencies before apps; validate each gate.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-099 — Executive Incident Reconstruction

**Primary evidence:** `artifacts/monitoring/service_health.csv`

**Expected defensible answer:** Report observed outage and backup gaps, avoid unproven AI attribution and permanent loss.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-100 — Full Enterprise Forensic Capstone

**Primary evidence:** `artifacts/forensics/surviving_evidence.csv`

**Expected defensible answer:** Integrated finding: storage degradation precedes suspicious orchestration, backup inconsistencies exist, causation and AI attribution remain uncertain.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

