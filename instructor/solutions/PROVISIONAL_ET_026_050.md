# EchoTrace Instructor — ET-026 onward

**Private provisional instructor reasoning.** These are evidence-grounded answer notes, not claims of complete practical validation. A scenario lacking artifacts is **not yet fully playable**. For each question use ten applicable forensic paths: primary logs, SQL, filesystem, storage, backup, network, identity, application, independent collection, isolated restore. Mark N/A with justification.

## ET-032 — Directory Replication Evidence

**Primary evidence:** `scenario/ENTERPRISE_ARCHITECTURE.md`

**Expected defensible answer:** No replication topology/status logs supplied; cannot diagnose replication-specific cause.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-033 — Account Lockout Root Cause

**Primary evidence:** `artifacts/monitoring/service_health.csv`

**Expected defensible answer:** Authentication error rate does not establish account lockouts; request lockout and failed-authentication events.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-034 — Privileged Session Attribution

**Primary evidence:** `artifacts/orchestration/orch_events.csv`

**Expected defensible answer:** svc_orch events identify a service principal but not a person or AI agent.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-035 — Identity Recovery Validation

**Primary evidence:** `artifacts/backup/repository_inventory.csv`

**Expected defensible answer:** AUTH-DB backup object is a candidate; clean-room integrity and functional authentication tests remain necessary.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-036 — Memory Process Timeline

**Primary evidence:** `artifacts/forensics/surviving_evidence.csv`

**Expected defensible answer:** No memory image or process extraction supplied; no process tree can be asserted.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-037 — Volatile Network Connection Analysis

**Primary evidence:** `artifacts/network/management_flows.csv`

**Expected defensible answer:** Network flows are persistent collector records, not volatile process-to-socket mappings.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-038 — Injected-Process Evidence Assessment

**Primary evidence:** `artifacts/forensics/surviving_evidence.csv`

**Expected defensible answer:** No memory image exists; process injection is unproven.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-039 — Credential Artifact Preservation

**Primary evidence:** `artifacts/forensics/surviving_evidence.csv`

**Expected defensible answer:** Prioritize lawful preservation of volatile evidence without collecting real secrets in student material.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-040 — Memory Acquisition Triage

**Primary evidence:** `artifacts/forensics/surviving_evidence.csv`

**Expected defensible answer:** Current evidence records are offline; propose acquisition order and document missing volatile sources.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-041 — DNS Timeline Reconstruction

**Primary evidence:** `artifacts/network/management_flows.csv`

**Expected defensible answer:** No DNS queries supplied; flow IP addresses alone cannot establish queried names.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-042 — NetFlow Correlation

**Primary evidence:** `artifacts/network/management_flows.csv`

**Expected defensible answer:** N003-N009 corroborate management communications during JOB-X91; do not infer payload content.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-043 — Proxy Evidence Analysis

**Primary evidence:** `artifacts/network/management_flows.csv`

**Expected defensible answer:** No proxy request/body records supplied; cannot determine HTTP request contents.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-044 — Firewall Session Reconstruction

**Primary evidence:** `artifacts/network/management_flows.csv`

**Expected defensible answer:** Flows corroborate endpoints/ports; firewall policy decisions require firewall logs.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-045 — TLS Metadata Investigation

**Primary evidence:** `artifacts/network/management_flows.csv`

**Expected defensible answer:** TCP/443 flows do not establish TLS SNI, certificate or encrypted payload details.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-046 — Lateral Movement Network Mapping

**Primary evidence:** `artifacts/network/management_flows.csv`

**Expected defensible answer:** ORCH-01 contacted multiple assets; communication does not prove adversarial lateral movement.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-047 — Data Transfer Volume Assessment

**Primary evidence:** `artifacts/network/management_flows.csv`

**Expected defensible answer:** Recorded bytes describe flow volume only; no evidence maps them to specific datasets.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-048 — Network Clock Normalization

**Primary evidence:** `artifacts/network/management_flows.csv`

**Expected defensible answer:** UTC timestamps are supplied; raw source clock offsets are not, so drift cannot be measured.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-049 — Management Plane Forensics

**Primary evidence:** `artifacts/orchestration/orch_events.csv`

**Expected defensible answer:** O003-O012 describe anomalous JOB-X91; originator attribution remains unknown.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-050 — Network Evidence Gap Analysis

**Primary evidence:** `artifacts/forensics/surviving_evidence.csv`

**Expected defensible answer:** Collector survives outage but lacks payload contents and host process attribution.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-051 — RAID Failure Reconstruction

**Primary evidence:** `artifacts/storage/storage_events.csv`

**Expected defensible answer:** Storage fabric latency exists; no RAID member telemetry is supplied.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-052 — SAN Path Failure Analysis

**Primary evidence:** `artifacts/storage/storage_events.csv`

**Expected defensible answer:** ST001 FABRIC-A latency precedes ST004 FABRIC-B reset; root cause remains uncertain.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-053 — Storage Metadata Timeline

**Primary evidence:** `artifacts/storage/storage_events.csv`

**Expected defensible answer:** ST002 metadata read burst precedes ST003 configuration change; causal link is not proven.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-054 — Snapshot Retention Investigation

**Primary evidence:** `artifacts/storage/storage_events.csv`

**Expected defensible answer:** ST003 records a snapshot retention reference modification; snapshot deletion is not independently proven.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-055 — Volume Read-Only Transition

**Primary evidence:** `artifacts/storage/storage_events.csv`

**Expected defensible answer:** ST009 protective read-only at 02:32:51 UTC follows metadata instability ST008.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

## ET-056 — File Recovery Feasibility

**Primary evidence:** `artifacts/data/data_scope.csv`

**Expected defensible answer:** Unavailable or partially unreadable data is not proof of irreversible loss; examine alternate copies.

**Ten-route grading:** Require an evidence citation, timestamp where available, one corroboration attempt, alternative explanation, confidence, limitation and safe recovery implication. No invented evidence or forced ten positive findings.

