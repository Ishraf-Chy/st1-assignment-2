# SmartCare v0.2 - Requirements Specification

## 1. Problem and Scope

SmartCare Community Clinic currently uses spreadsheets and paper records to manage patients and appointments. This has caused problems such as duplicate bookings, difficulty finding patient information, inconsistent appointment status and limited appointment history.

The purpose of SmartCare is to provide a small and maintainable system for managing patients, practitioners and appointments.

### In Scope

- Store and manage patient information.
- Store and manage practitioner information.
- Create appointments.
- Search for patient information.
- View appointments.
- Cancel appointments.
- Reschedule appointments.
- Check practitioner availability.
- Prevent duplicate bookings.
- Maintain appointment status.
- Maintain appointment history.

### Out of Scope

- AI diagnosis or treatment recommendations.
- Hospital or emergency department management.
- Prescription management.
- Advanced medical record management.

### Provisional Features

The following features have not been confirmed and require clarification:

- Online appointment booking by patients.
- SMS or email appointment reminders.
- Online payments.
- Insurance processing.
- Detailed management reports.

---

## 2. Stakeholders

| Stakeholder | Need | Evidence |
|---|---|---|
| Receptionist / Clinic Staff | Manage patients and appointments and avoid booking conflicts. | The client reports duplicate bookings, difficulty finding patient information and appointment-management problems. |
| Patient | Have their information and appointments recorded accurately. | The client wants the system to manage patients and appointments. |
| Practitioner | Have their appointments and availability managed accurately. | The client wants the system to manage practitioners and appointments. |
| Clinic Management | Have a small and maintainable system that improves the current process. | Management specifically wants a small and maintainable patient, practitioner and appointment system. |

---

## 3. Functional Requirements

**FR-01:** The system shall allow authorised clinic staff to register patient information.

**FR-02:** The system shall allow authorised clinic staff to search for patient information.

**FR-03:** The system shall allow authorised clinic staff to update patient information.

**FR-04:** The system shall store practitioner information.

**FR-05:** The system shall record practitioner availability.

**FR-06:** The system shall allow authorised clinic staff to create an appointment for a patient with a practitioner.

**FR-07:** The system shall check practitioner availability before confirming an appointment.

**FR-08:** The system shall prevent duplicate bookings for the same practitioner at the same appointment time.

**FR-09:** The system shall allow authorised clinic staff to view appointments.

**FR-10:** The system shall allow authorised clinic staff to cancel an appointment.

**FR-11:** The system shall allow authorised clinic staff to reschedule an appointment.

**FR-12:** The system shall maintain appointment status and appointment history.

---

## 4. Non-Functional Requirements

**NFR-01 - Reliability:**  
The system should reliably retain patient, practitioner and appointment information during normal operation.

**NFR-02 - Maintainability:**  
The system should be structured so that patient, practitioner and appointment functionality can be maintained without unnecessary changes to unrelated parts of the system.

**NFR-03 - Usability:**  
The system should provide a simple interface for common patient and appointment management tasks.

**NFR-04 - Data Integrity:**  
The system should maintain consistent patient, practitioner and appointment information and prevent conflicting appointment records.

**NFR-05 - Testability:**  
Core appointment-management behaviour should be independently testable so that booking, cancellation and conflict-handling behaviour can be verified.

---

## 5. User Stories

**US-01:** As a receptionist, I want to log an appointment for a patient so that the patient can see a doctor.

**US-02:** As a receptionist, I want to search for patient information so that I can find the correct patient's details.

**US-03:** As a receptionist, I want to check practitioner availability so that I can select an available appointment time for the patient.

**US-04:** As a patient, I want to book an appointment so that I can have a consultation with a practitioner.

**US-05:** As a receptionist, I want to reschedule an appointment so that the patient is able to attend the appointment without conflict.

**US-06:** As a practitioner, I want my appointments to be recorded accurately so that I can practice on a schedule without conflicts.

---

## 6. Acceptance Criteria

### Successful Appointment Booking

**GIVEN** a patient exists and the selected practitioner is available at the requested time  
**WHEN** the receptionist creates the appointment  
**THEN** the system records the appointment for the patient and practitioner.

### Duplicate Booking - Failure Scenario

**GIVEN** a practitioner already has an appointment at a particular time  
**WHEN** the receptionist attempts to create another appointment for the same practitioner at that time  
**THEN** the system rejects the new appointment.

### Cancel Appointment

**GIVEN** an appointment exists in the system  
**WHEN** the receptionist cancels the appointment  
**THEN** the system updates the appointment to show that it has been cancelled.

### Reschedule Appointment

**GIVEN** an appointment exists and the requested new appointment time is available  
**WHEN** the receptionist reschedules the appointment  
**THEN** the system updates the appointment to the new time.

---

## 7. Assumptions and Open Questions

### Assumptions

- SmartCare is intended for a small community clinic.
- Patient, practitioner and appointment management are the main functions of the system.
- Clinic staff will be responsible for managing appointments.
- A practitioner should not have conflicting appointments at the same time.

### Open Questions

1. What patient information must SmartCare store?
2. What practitioner information must SmartCare store?
3. How long is a standard appointment?
4. What appointment statuses are required?
5. Should patients be able to book or manage their own appointments?
6. Should SmartCare send SMS or email appointment reminders?
7. Should cancelled appointments remain in appointment history?
8. Are online payments or insurance processing required?
9. Does clinic management require any reports?

---

## 8. AI Requirements Review Record

### AI Review

The requirements were reviewed for ambiguity, inconsistency, missing clarification questions and testability.

| AI Suggestion | Evidence? | Decision | Reason | Verification |
|---|---|---|---|---|
| Clarify exactly what patient information must be stored. | Requires clarification | Accepted | The requirement to manage patients is confirmed, but the required patient fields are not specified. | Added as an open question. |
| Clarify the appointment statuses required by SmartCare. | Requires clarification | Accepted | The client identifies inconsistent appointment status as a problem but does not define the required statuses. | Added as an open question. |
| Prevent conflicting practitioner appointments. | Supported by evidence | Accepted | Duplicate bookings are identified as an existing problem. | Included in FR-08 and the failure acceptance criterion. |
| Add SMS or email appointment reminders. | No confirmed evidence | Unverified | Appointment reminders are not confirmed in the client brief. | Kept as a provisional feature and open question. |
| Add online payment functionality. | No confirmed evidence | Rejected | Payment functionality is not part of the confirmed SmartCare requirements. | Not added as a functional requirement. |
| Add AI treatment recommendations. | No evidence | Rejected | This is outside the purpose of the SmartCare appointment-management system. | Kept outside the system scope. |

### Verification Summary

The AI review was compared against the original SmartCare client information. Suggestions supported by the client information were accepted, the ones requiring more information were kept as open questions features, and finally, the ones without supporting evidence or outside the purpose of SmartCare were rejected.