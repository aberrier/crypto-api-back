import os
from datetime import timedelta

from dotenv import load_dotenv, find_dotenv
from celery.schedules import crontab
# Load .env
load_dotenv(find_dotenv())
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto.settings')

app = Celery('crypto')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'alerts-send-to-email': {
        'task': 'alerts.send_emails',
        'schedule': crontab(hour=4)
    },
    'check-assets-list': {
        'task': 'coinapi.asset_list',
        'schedule': crontab(hour=23)
    },
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
