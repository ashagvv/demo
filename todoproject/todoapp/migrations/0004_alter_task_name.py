# Generated by Django 3.2.14 on 2022-08-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.TextField(max_length=100),
        ),
    ]