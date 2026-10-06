# AI Engineering Log - Stage 4

## AI Pair-Programming Scope
AI assistance was used for the Appointment implementation and review portion of Stage 4. The Patient and Practitioner implementation sections were kept separate because the lab labels those sections AI OFF.

## Prompt / Constraints Used
Implement only the Appointment class from the approved SmartCare design. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions.

## Generated Contribution
AI assisted with the AppointmentStatus enum, Appointment constructor validation, read-only status access, cancel() transition logic, and behaviour-check ideas.

## Decisions
- Accepted: AppointmentStatus enum.
- Accepted: controlled cancel() operation.
- Modified: kept transition handling intentionally small, with only SCHEDULED to CANCELLED required for this stage.
- Rejected: direct public status mutation.
- Rejected: SQL, notification dependencies and unnecessary inheritance.
