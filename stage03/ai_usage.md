# AI Usage - Stage 3

## AI Design Review
AI was used during the AI-enabled design review to suggest possible classes and relationships based on the confirmed SmartCare requirements. Suggestions were checked against the requirement IDs rather than accepted automatically.

## Compare and Verify
The core Patient, Practitioner and Appointment classes and their relationships were accepted because they were supported by the confirmed requirements. A separate Status class was modified into an Appointment attribute. Extra controller and notification classes were rejected because they were either unnecessary for the Stage 3 domain model or unsupported by confirmed requirements.