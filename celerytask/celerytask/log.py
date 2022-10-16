import threading
# from generate_file.models import Datas

def monitor_events(celery_app):
    """
    adds a 'task-log' event listener to the celery app, which will log these
    worker event as python log messages.
    """
    print('monitor events')

    def on_event(event):
        if(event['type'] != 'worker-heartbeat'):
            print('on_event' , event['type'] , event['uuid'] )

    def on_task_started (event):
        print('on task started' , event['uuid'])

    def on_task_completed(event):
        print('on_task completd' , event['uuid'])

    
    def on_tak_failed(event):
        print('on task failed' , event['uuid'])

    def on_task_received(event):
        print('on_task_received' , event['uuid'])

    with celery_app.connection() as conn:
        recv = celery_app.events.Receiver(conn, handlers={ 
            'task-started':on_task_started ,
            'task-succeeded':on_task_completed,
            'task-failed' : on_tak_failed,
            'task-received' : on_task_received,
            '*' : on_event
         })
        recv.capture(limit=None, timeout=None, wakeup=True)


def setup_event_listening(celery_app):
    """
    capture celery log events in the background
    """
    thread = threading.Thread(target=monitor_events, args=[celery_app])
    thread.daemon = True
    thread.start()
