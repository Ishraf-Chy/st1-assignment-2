from __future__ import annotations
from datetime import datetime
from enum import Enum


def _require_text(value: str, field_name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")
    return value.strip()


class Patient:
    def __init__(self, patient_id: str, name: str, contact_details: str | None = None) -> None:
        self.patient_id = _require_text(patient_id, "patient_id")
        self.name = _require_text(name, "name")
        self.contact_details = contact_details

    def update_details(self, name: str | None = None, contact_details: str | None = None) -> None:
        if name is not None:
            self.name = _require_text(name, "name")
        if contact_details is not None:
            self.contact_details = contact_details


class Practitioner:
    def __init__(self, practitioner_id: str, name: str, specialty: str) -> None:
        self.practitioner_id = _require_text(practitioner_id, "practitioner_id")
        self.name = _require_text(name, "name")
        self.specialty = _require_text(specialty, "specialty")

    def update_specialty(self, specialty: str) -> None:
        self.specialty = _require_text(specialty, "specialty")


class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"


class Appointment:
    def __init__(
        self,
        appointment_id: str,
        patient: Patient,
        practitioner: Practitioner,
        date_time: datetime,
    ) -> None:
        self.appointment_id = _require_text(appointment_id, "appointment_id")
        if not isinstance(patient, Patient):
            raise TypeError("patient must be a Patient")
        if not isinstance(practitioner, Practitioner):
            raise TypeError("practitioner must be a Practitioner")
        if not isinstance(date_time, datetime):
            raise TypeError("date_time must be a datetime")
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time
        self._status = AppointmentStatus.SCHEDULED

    @property
    def status(self) -> AppointmentStatus:
        return self._status

    def cancel(self) -> None:
        if self._status is not AppointmentStatus.SCHEDULED:
            raise ValueError("Only a scheduled appointment can be cancelled")
        self._status = AppointmentStatus.CANCELLED
