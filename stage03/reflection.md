# Stage 3 Reflection

The hardest modelling decision was deciding which candidate concepts should become classes and which should stay as attributes or behaviour. Patient, Practitioner and Appointment were clear classes because they represent the main things SmartCare needs to manage. However, concepts such as Status and Cancellation could have been made into separate classes. I kept status as an Appointment attribute and cancellation as appointment behaviour because the confirmed requirements do not show that they need independent identities or responsibilities.

The AI review could easily over-design the system by suggesting manager, controller, notification and scheduling classes. Some of these might be useful in a larger application, but they are not all supported by the current requirements. NotificationManager was rejected because notifications are not a confirmed requirement. A separate ScheduleEngine was also unnecessary at this stage because practitioner availability can be represented in the Practitioner class.

My final choices were based mainly on the Stage 2 functional requirements and the requirement that SmartCare should remain a small, maintainable system. I used the requirement IDs to check that each important class, attribute and relationship had evidence rather than adding classes.
