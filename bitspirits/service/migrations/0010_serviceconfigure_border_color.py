# Generated by Django 3.2.9 on 2021-11-29 06:41

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_serviceconfigure_dot_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceconfigure',
            name='border_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
    ]
