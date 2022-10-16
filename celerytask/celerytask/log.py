import threading
# from generate_file.models import Datas
from generate_file.updater import status_updater
def monitor_events(celery_app):
    """
    Calls Upadte function on every event occurences 
    """

    def on_task_started (event):
        status_updater(event['uuid'] , 'PROGRESS')

    def on_task_completed(event):
        status_updater(event['uuid'] , 'COMPLETED')

    
    def on_tak_failed(event):
        status_updater(event['uuid'] , 'FAILED')

    def on_task_received(event):
        status_updater(event['uuid'] , 'RECEIVED')

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
