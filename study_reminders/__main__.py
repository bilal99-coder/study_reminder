#Start first with loading
import scheduler
import students_manager
import reminder_generator
import reminder_sender
import logger

print("hELLLLSPBKSDKGSN")
scheduler.schedule_reminders(students_manager, reminder_generator, reminder_sender, logger)