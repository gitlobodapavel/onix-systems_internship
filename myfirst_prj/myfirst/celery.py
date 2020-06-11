import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myfirst.settings')

app = Celery('myfirst', broker='redis://0.0.0.0:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'print-every-minute': {
        'task': 'locations.tasks.print_runtime',
        'schedule': crontab(minute='*/1'),
    }
}