# Generated by Django 3.2.9 on 2021-12-01 06:06

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_auto_20211201_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceconfigure',
            name='learn_more_btn_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
    ]
