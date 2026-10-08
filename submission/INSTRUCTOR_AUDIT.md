# EchoTrace — Instructor Quality Assurance Audit
**Audit date:** 2026-10-07
**Scope:** main README; 25-lab completion matrix; sampled labs 01, 16, 25; Kali, IoT and Windows/Linux tracks; Sherlock case brief, ten questions, instructor writeup, and validation source; six incident CSVs.

## Overall disposition
**Conditional / NOT YET READY FOR FINAL HTB SUBMISSION.** This is a documentary and static source review, not an independent runtime playtest or HTB evaluation.

## Findings
| ID | Priority | Observation | Acceptance condition |
|---|---|---|---|
| QA-01 | Critical | Proposed Insane difficulty is not substantiated: ten questions mostly require simple CSV lookups. | Blind-playtest by senior DFIR analyst; calibrate challenge or redesign harder cross-source questions. |
| QA-02 | High | Existing 25 labs are largely investigation outlines; several require native artifacts not present. | Provide usable synthetic artifacts or explicitly classify as tabletop modules. |
| QA-03 | High | Script asserts known records but does not prove unique, reproducible student solve path. | Execute test, perform independent solve, record evidence and run logs. |
| QA-04 | High | Instructor writeup lacks command-by-command reproductions and screenshots. | Add exact extraction commands, expected output, screenshots and source citations for every answer. |
| QA-05 | High | No confirmed student-only ZIP or separately hosted private instructor writeup. | Build and inspect ZIP; validate password against current HTB Sherlock requirements; provide restricted writeup URL. |
| QA-06 | Medium | SQL training uses synthetic SQLite, not native SQL Server transaction logs/LSN. | Label accurately; add native-derived synthetic log sequence artifacts for LSN labs if required. |
| QA-07 | Medium | Windows EVTX, MFT/USN, Linux journal and IoT firmware exercises rely on CSV-like exports rather than native acquisitions. | Provide representative native artifacts or describe exercises as log-analysis simulations. |
| QA-08 | Medium | Main README says 'complete' although its development section says playtest stage. | Harmonize status claims; never imply full validation. |
| QA-09 | Medium | All answers and writeup are stored in the same private repo as student material. | Maintain strict export allowlist; ensure answer keys never ship in student ZIP. |
| QA-10 | Medium | Cross-source causality must remain qualified: storage warning ST001 predates JOB-X91 O003; accepted metadata operation is not proof of persistence. | Require competing hypotheses and uncertainty in rubric. |

## Student challenge — question review
- Q1–Q8: deterministic, primarily single-record lookup; useful introductory triage but not independently Insane.
- Q9–Q10: require two-file catalog/repository join and are stronger than single-source questions.
- All 10 have instructor-proposed exact answers with record IDs in `submission/instructor/WRITEUP.md`.
- The 'AI-assisted' hypothesis is not supported by current evidence and must not become a required answer.

## Training track review
- Kali: commands and reproducible SQL/CSV analysis outlined; actual execution evidence not yet verified.
- IoT: inventory and gateway-event synthetic CSVs exist; no firmware images or device captures.
- Windows/Linux: Windows-event-like, NTFS-USN-like and Linux-journal-like CSVs exist; not native formats.
- 25 labs: several entries in `training/labs/LAB_COMPLETION_MATRIX.csv` explicitly say 'requires artifacts', 'tabletop only' or 'partial evidence'.

## Minimum release gate
1. Run the supplied validator against a checked-out snapshot.
2. Independently solve all ten questions using only student package.
3. Record reproducible commands and outputs in private writeup.
4. Generate student-only ZIP and inspect it for solutions and accidental sensitive files.
5. Verify archive opens with HTB's current Sherlock-specific required password.
6. Host writeup privately and verify access link.
7. Recalibrate difficulty and complete HTB form truthfully.

## Instructor verdict
The focused Sherlock can become a clean **entry/intermediate evidence-correlation challenge** in its present form. An Insane claim or premium reward expectation needs substantially more technical depth and external playtest. Acceptance and payout are not guaranteed.
