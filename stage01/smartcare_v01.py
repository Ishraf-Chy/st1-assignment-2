appointments = []


def add_appointment(patient, doctor, date, time):
    appointment = {
        "patient": patient,
        "doctor": doctor,
        "date": date,
        "time": time
    }

    appointments.append(appointment)


add_appointment("John", "Dr Smith", "10/10/2026", "10:00 AM")
add_appointment("Sarah", "Dr Jones", "11/10/2026", "2:00 PM")


for appointment in appointments:
    print(appointment)