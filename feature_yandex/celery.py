import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feature_yandex.settings')

app = Celery('feature_yandex')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_email_link_task': {
        'task': 'reports.tasks.send_email_link_task',
        'schedule': crontab(minute=1)
    },
    'send_report_task': {
        'task': 'reports.tasks.send_report_task',
        'schedule': crontab(minute=2)
    },
    'send_report_period_task': {
        'task': 'reports.tasks.send_report_period_task',
        'schedule': crontab(minute=10)
    },
}
