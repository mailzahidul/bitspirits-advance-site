# Generated by Django 3.2 on 2021-10-28 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='name',
            field=models.CharField(default='', max_length=250),
        ),
    ]