# Generated by Django 3.2.9 on 2021-12-01 05:49

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0025_somefactsconfigure_item_bg_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='homesliderconfigure',
            name='border_play_btn_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
        migrations.AddField(
            model_name='homesliderconfigure',
            name='triangle_play_btn_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
    ]