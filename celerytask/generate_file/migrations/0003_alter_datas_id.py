# Generated by Django 4.1.2 on 2022-10-10 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generate_file', '0002_auto_20221010_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datas',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]