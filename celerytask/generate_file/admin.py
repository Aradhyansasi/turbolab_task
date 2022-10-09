from django.contrib import admin
from . import models

# Register your models here.
class CreateCsvAdmin(admin.AdminSite):
    site_header = 'Create CSV Admin'


create_file = CreateCsvAdmin(name='CreateAdmin')

create_file.register(models.Datas)
