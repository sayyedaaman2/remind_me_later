from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
from pytz import timezone
from reminder.models import Reminder

# Incompleted task
@shared_task
def send_email_task(reminder_id):
    print(reminder_id)
    try:
        reminder = Reminder.objects.get(id=reminder_id)

        from_email = settings.EMAIL_HOST_USER
        recipient_list = [reminder.user.email]

        subject = "This email is from Django server"
        message_template = """Hello {},
        This is a Notification via the Django server.
        We are notifying you with the following message:

        {}
        
        Thank you """
        formatted_message = message_template.format(reminder.user.username, reminder.message)

        # Send email
        send_mail(subject, formatted_message, from_email, recipient_list)

        # Update status to indicate that email has been sent
        reminder.status = 'completed'
        reminder.save()

    except Reminder.DoesNotExist:
        print("Reminder with id {} does not exist.".format(reminder_id))
    except Exception as e:
        print("An error occurred while sending email:", str(e))

def schedule_email(reminderObject):
    if reminderObject is None:
        raise ValueError('reminderObject is None!')

    reminder_time_utc = reminderObject.schedule_time
    current_time_utc = datetime.now(timezone('UTC'))  # Get current time in UTC

    # Calculate delay in seconds
    delay = (reminder_time_utc - current_time_utc).total_seconds()
    print("Delay until sending email:", delay)

    # Schedule sending email task
    send_email_task.apply_async((reminderObject.id,), countdown=delay)
