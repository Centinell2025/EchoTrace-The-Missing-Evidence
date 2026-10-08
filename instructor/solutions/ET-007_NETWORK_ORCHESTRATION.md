# ET-007 — Instructor Solution: Network / Management-Plane Forensics

## Expected findings
Approved baseline: `O001/O002` with `N001/N002` for ID-01/ID-02 at 02:01 UTC. The unexplained `JOB-X91` sequence begins `O003` at 02:12:01.120 UTC and targets storage, database, backup and application systems. Corresponding flows `N003–N009` corroborate communications, not payload contents or intent.

`O011` records an accepted storage metadata operation at 02:13:41.004 UTC; `O012` an accepted backup catalog operation 205 ms later. Storage event `ST003` records a configuration change in the same second. The precise relationship is a hypothesis requiring more evidence.

## Ten routes
Orchestration event IDs; baseline; job IDs; timing deltas; asset inventory; network flow records; storage metadata; backup catalog; SOC telemetry; alternate initiator attribution evidence.

## Grading
Do not infer that rapid execution proves AI. Do not equate flow bytes with data exfiltration. Do not attribute a service-account event to a human without independent evidence.
