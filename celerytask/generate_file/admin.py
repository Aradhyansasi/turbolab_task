from django.contrib import admin
from . import models

# Register your models here.
class CreateCsvAdmin(admin.ModelAdmin):
    list_display = ['file_name' , "count" , 'celery_id' , 'status']
    fields = ['file_name' , 'count']

admin.site.register(models.Datas, CreateCsvAdmin)

