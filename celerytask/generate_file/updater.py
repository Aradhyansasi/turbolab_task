
def status_updater(uuid,  status):
    from .models import Datas
    Datas.objects.filter(celery_id = uuid).update(status = status)