from django.db import models

from celerytask.tasks import generate_csv

# Create your models here.

class Datas(models.Model):
    # celery_id = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)
    count = models.CharField(max_length=100)

    def __str__(self):
        return self.file_name

    def save(self , *args, **kwargs):
        generate_csv.delay(self.file_name , self.count)
        super(Datas, self).save(*args , **kwargs)