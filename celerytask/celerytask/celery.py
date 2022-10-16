from __future__ import absolute_import, unicode_literals
from email.mime import base
import os
from celery import Celery
from django.conf import settings
import environ 

env = environ.Env(DEBUG=(bool, False), )
environ.Env.read_env()  # reading .env file
# setting the Django settings module.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerytask.settings')
app = Celery('celerytask' , backend=env('CELERY_BACKEND_URL') , broker=env('CELERY_BACKEND_URL'))
app.config_from_object('django.conf:settings')

# Looks up for task modules in Django applications and loads them
app.autodiscover_tasks(settings.INSTALLED_APPS)
