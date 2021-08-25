from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'circle.config')

app = Celery('circle')


app.config_from_object('django.conf:settings', namespace='CELERY')
# app.config_from_object(Config, namespace='CELERY')
app.autodiscover_tasks()
