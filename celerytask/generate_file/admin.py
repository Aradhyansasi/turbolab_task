from django.contrib import admin
from . import models

# Register your models here.
class CreateCsvAdmin(admin.ModelAdmin):
    fields = ['file_name' , 'count']

admin.site.register(models.Datas, CreateCsvAdmin)

