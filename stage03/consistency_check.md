# Stage 3 Consistency Check

- Patient appears in the CRC cards, UML model and Python skeleton.
- Practitioner appears in the CRC cards, UML model and Python skeleton.
- Appointment appears in the CRC cards, UML model and Python skeleton.
- UML multiplicities: one Patient can have 0..* Appointments; one Practitioner can have 0..* Appointments; each Appointment references exactly one Patient and one Practitioner.
- Appointment status is represented consistently as state/attribute, not a separate class.
- Cancellation is represented as Appointment behaviour, not a separate domain class.
- No full business behaviour has been implemented in Python; method bodies remain skeletons with pass.
- Unsupported NotificationManager, ClinicController and manager classes were not added.
