# Generated by Django 4.1.2 on 2022-10-16 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generate_file', '0004_auto_20221015_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datas',
            name='count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='datas',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
