# SmartCare Clinic Appointment System
# Stage 1 - Version 0.1

appointments = []


def add_appointment(patient, doctor, date, time):

    # Check for a booking conflict
    for appointment in appointments:
        if appointment["doctor"] == doctor and appointment["date"] == date and appointment["time"] == time:
            print("Booking conflict: Doctor is already booked at this time.")
            return

    # Create the appointment
    appointment = {
        "patient": patient,
        "doctor": doctor,
        "date": date,
        "time": time
    }

    appointments.append(appointment)
    print("Appointment added successfully.")


# Original appointments
add_appointment("John", "Dr Smith", "10/10/2026", "10:00 AM")
add_appointment("Sarah", "Dr Jones", "11/10/2026", "2:00 PM")

# Duplicate booking test
add_appointment("Michael", "Dr Smith", "10/10/2026", "10:00 AM")

# Normal booking test
add_appointment("Emma", "Dr Brown", "12/10/2026", "11:00 AM")

# Blank patient name test
add_appointment("", "Dr Brown", "13/10/2026", "1:00 PM")

# Strange input test
add_appointment(None, "Dr Jones", "14/10/2026", None)


# Display appointments
print("\nAppointments:")

for appointment in appointments:
    print(appointment)