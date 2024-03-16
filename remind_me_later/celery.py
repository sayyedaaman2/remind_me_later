import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'remind_me_later.settings')

# Create a Celery instance.
celery_app = Celery('remind_me_later')

# Configure the Celery broker URL.
celery_app.conf.broker_url = 'amqp://guest:guest@localhost:5672/'

# Load task modules from all registered Django app configs.
celery_app.autodiscover_tasks()
