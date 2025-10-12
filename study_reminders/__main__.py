#Start first with loading
import scheduler
from students_manager import StudentsManager
import reminder_generator 
import reminder_sender
import logger
import datetime

print(StudentsManager().students)
print(StudentsManager().get_students())


scheduler.schedule_reminders(StudentsManager(), reminder_generator.generate_reminder, reminder_sender.send_reminder, logger.log_reminder)
