# Generated by Django 3.2.9 on 2021-11-28 10:24

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0022_homesliderconfigure_bg_play_btn_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='homesliderconfigure',
            name='bg_btn_hov_end_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
        migrations.AddField(
            model_name='homesliderconfigure',
            name='bg_btn_hov_start_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
    ]
