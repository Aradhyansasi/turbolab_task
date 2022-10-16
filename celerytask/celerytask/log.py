import threading
# from generate_file.models import Datas
from generate_file.updater import status_updater
def monitor_events(celery_app):
    """
    adds a 'task-log' event listener to the celery app, which will log these
    worker event as python log messages.
    """

    def on_task_started (event):
        status_updater(event['uuid'] , 'PROGRESS')
        print('on task started' , event['uuid'])

    def on_task_completed(event):
        status_updater(event['uuid'] , 'COMPLETED')
        print('on_task completd' , event['uuid'])

    
    def on_tak_failed(event):
        status_updater(event['uuid'] , 'FAILED')
        print('on task failed' , event['uuid'])

    def on_task_received(event):
        status_updater(event['uuid'] , 'RECEIVED')
        print('on_task_received' , event['uuid'])

    with celery_app.connection() as conn:
        recv = celery_app.events.Receiver(conn, handlers={ 
            'task-started':on_task_started ,
            'task-succeeded':on_task_completed,
            'task-failed' : on_tak_failed,
            'task-received' : on_task_received,
         })
        recv.capture(limit=None, timeout=None, wakeup=True)


def setup_event_listening(celery_app):
    """
    capture celery log events in the background
    """
    thread = threading.Thread(target=monitor_events, args=[celery_app])
    thread.daemon = True
    thread.start()
