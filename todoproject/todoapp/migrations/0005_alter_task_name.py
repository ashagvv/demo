# Generated by Django 3.2.14 on 2022-08-12 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_alter_task_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.TextField(),
        ),
    ]
