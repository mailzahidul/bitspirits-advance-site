# Generated by Django 3.2.9 on 2021-11-24 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0019_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]