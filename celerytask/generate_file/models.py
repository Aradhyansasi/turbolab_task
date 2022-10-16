from gc import callbacks
from django.db import models

from celerytask.tasks import  generate_csv

# Create your models here.

class Datas(models.Model):
    celery_id = models.CharField(max_length=100 , default="0")
    file_name = models.CharField(max_length=100)
    count = models.CharField(max_length=100)
    status = models.CharField(max_length = 150 , default="Pending")

    def __str__(self):
        return self.file_name

    def save(self , *args, **kwargs):
        id = generate_csv.apply_async(args=[self.file_name , self.count])
        self.celery_id = id.task_id
        self.status = id.status
        super(Datas, self).save(*args , **kwargs)

