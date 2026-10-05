# Human vs AI Comparison

| Question | Human Version | AI Version |
|---|---|---|
| Easy to understand? | Yes, because the code was simple and only added appointments to a list. | Mostly yes, but the booking conflict check added more logic. |
| Runs successfully? | Yes. | Yes. |
| Meets required features? | Partly. It could add and display appointments but did not prevent booking conflicts. | Better. It could add appointments and prevent the same doctor from being booked at the same date and time. |
| Makes assumptions? | Yes. It assumed all appointment information entered was valid. | Yes. It assumed a duplicate booking should be identified using the doctor, date and time. |
| Errors or limitations? | It allowed duplicate bookings and did not validate blank or None values. | It prevented duplicate bookings, but still accepted blank and None values. |
| Can I explain it? | Yes. | Yes. I understand that the loop checks existing appointments before a new appointment is added. |