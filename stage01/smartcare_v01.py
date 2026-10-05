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


# Add appointments
add_appointment("John", "Dr Smith", "10/10/2026", "10:00 AM")
add_appointment("Sarah", "Dr Jones", "11/10/2026", "2:00 PM")

# Try to book Dr Smith at the same date and time
add_appointment("Michael", "Dr Smith", "10/10/2026", "10:00 AM")


# Display appointments
print("\nAppointments:")

for appointment in appointments:
    print(appointment)