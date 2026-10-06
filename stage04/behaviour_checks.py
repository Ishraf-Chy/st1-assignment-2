from datetime import datetime
from smartcare_v04 import Patient, Practitioner, Appointment, AppointmentStatus

print("1. Create valid objects")
patient = Patient("P001", "Alex Smith", "0400 000 000")
practitioner = Practitioner("PR001", "Dr Lee", "General Practice")
appointment = Appointment("A001", patient, practitioner, datetime(2026, 10, 20, 10, 0))
print("PASS:", appointment.status is AppointmentStatus.SCHEDULED)

print("2. Test invalid patient name")
try:
    Patient("P002", "   ")
    print("FAIL: blank name was accepted")
except ValueError as error:
    print("PASS:", error)

print("3. Cancel scheduled appointment")
appointment.cancel()
print("PASS:", appointment.status is AppointmentStatus.CANCELLED)

print("4. Attempt illegal repeated cancellation")
try:
    appointment.cancel()
    print("FAIL: repeated cancellation was accepted")
except ValueError as error:
    print("PASS:", error)
