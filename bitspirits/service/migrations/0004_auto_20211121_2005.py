# Generated by Django 3.2.9 on 2021-11-21 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_service_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='service',
            name='icon',
        ),
        migrations.DeleteModel(
            name='Feature',
        ),
    ]