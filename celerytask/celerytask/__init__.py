from .celery import app as celery_app
from .log import setup_event_listening
setup_event_listening(celery_app)