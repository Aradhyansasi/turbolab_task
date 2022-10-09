from django.db import models

# Create your models here.

class Datas(models.Model):
    file_name = models.CharField(max_length=100)
    count = models.CharField(max_length=100)

    def __str__(self):
        return self.file_name

    # def save(self , *args, **kwargs):
    #     print(data , 'data')