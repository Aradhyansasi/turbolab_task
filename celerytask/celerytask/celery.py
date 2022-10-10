from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# setting the Django settings module.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerytask.settings')
app = Celery('celerytask')
app.config_from_object('django.conf:settings')

# Looks up for task modules in Django applications and loads them
app.autodiscover_tasks(settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))