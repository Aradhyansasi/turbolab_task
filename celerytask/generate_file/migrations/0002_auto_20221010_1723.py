# Generated by Django 2.2 on 2022-10-10 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generate_file', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datas',
            name='celery_id',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AddField(
            model_name='datas',
            name='status',
            field=models.CharField(default='Pending', max_length=150),
        ),
        migrations.AlterField(
            model_name='datas',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
