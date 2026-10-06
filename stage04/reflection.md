# Stage 4 Reflection

The main design choice in Stage 4 was to let the Appointment class handle its status rules and keep it free from features that do not belong there. The AI helped with creating the AppointmentStatus enum and the cancel operation. The generated code still needed to be reviewed against the approved model and the constraints from Stage 4.

I turned down ideas like adding SQL logic or notification behavior into the Appointment class because those were outside the approved domain design and would have made the class too big. I also kept the status field protected so no other part of the program can change it directly and skip the rules, for changing states. A scheduled appointment can be cancelled,. If someone tries to cancel it a second time the system shows an error.

The approved design guided the implementation by focusing on Patient, Practitioner and Appointment as the core domain classes and using associations of unnecessary inheritance. Manual testing showed that valid objects can be created invalid inputsre rejected cancellation works as expected and repeated transitions that are not allowed are blocked.