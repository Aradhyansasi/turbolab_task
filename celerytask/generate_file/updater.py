
def status_updater(uuid,  status):
    from generate_file.models import Datas
    Datas.objects.filter(celery_id = uuid).update(status = status)