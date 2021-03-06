# Generated by Django 3.2.9 on 2021-12-01 08:45

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page_config', '0028_pagesetup_title_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoconfigure',
            name='bg_btn_end_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
        migrations.AddField(
            model_name='videoconfigure',
            name='bg_btn_hov_end_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
        migrations.AddField(
            model_name='videoconfigure',
            name='bg_btn_hov_start_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
        migrations.AddField(
            model_name='videoconfigure',
            name='bg_btn_start_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
    ]
