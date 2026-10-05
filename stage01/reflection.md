# Stage 1 Reflection

Before using AI I created a SmartCare appointment prototype in Python. The program used a list to keep appointments and a function to add appointments that included the patient name, doctor, date and time. The original program could. Show appointments, but it did not check for booking conflicts or bad inputs.

AI helped me learn how to check existing appointments before adding an one. The improvement involved a loop that checked if the same doctor was already scheduled at the date and time. If a conflict was found the program did not allow the appointment.

AI made some guesses about how appointments should work. I still had to choose if the suggested improvement fit the SmartCare requirements. I tested the code with inputs. I tried an appointment, a repeated appointment, a patient name with nothing and None values. The repeated appointment was properly not allowed,. The empty and None inputs were still accepted.

The work left to do involved running the tests looking at the results finding the limits and choosing which change to make next. Later versions could add input checks and other features, for managing appointments.
