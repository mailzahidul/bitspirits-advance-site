# Generated by Django 3.2.9 on 2021-11-29 08:03

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0033_auto_20211129_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='howwedoitconfigure',
            name='item_text_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
    ]
