from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'circle.settings')

app = Celery('circle')


app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.broker_url = 'redis://192.168.2.211:6379/0'
app.conf.result_backend = 'redis://192.168.2.211:6379/0'
app.conf.accept_content = ['json']
result_accept_content = ['json']
app.conf.timezone = 'Asia/Jakarta'
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'
# app.conf.task_annotations = {'*': {'rate_limit': '10/s'}}

# app.conf.beat_schedule = {
#     'add-every-40': {
#         'task': 'save_data_items',
#         'schedule': 40.0,

#     },
# }


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
