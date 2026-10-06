

class Patient:
    def __init__(self, patient_id, name, contact_details=None):
        self.patient_id = patient_id
        self.name = name
        self.contact_details = contact_details

    def update_details(self, name=None, contact_details=None):
        pass


class Practitioner:
    def __init__(self, practitioner_id, name, availability=None):
        self.practitioner_id = practitioner_id
        self.name = name
        self.availability = availability

    def update_availability(self, availability):
        pass


class Appointment:
    def __init__(self, appointment_id, patient, practitioner, date_time, status="booked"):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time
        self.status = status

    def cancel(self):
        pass

    def update_status(self, status):
        pass
