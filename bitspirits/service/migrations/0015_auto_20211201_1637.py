# Generated by Django 3.2.9 on 2021-12-01 10:37

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0014_auto_20211201_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceconfigure',
            name='bg_btn_boarder_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
        migrations.AddField(
            model_name='serviceconfigure',
            name='bg_btn_boarder_width',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='serviceconfigure',
            name='bg_btn_end_hover_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
        migrations.AddField(
            model_name='serviceconfigure',
            name='bg_btn_icon_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
        migrations.AddField(
            model_name='serviceconfigure',
            name='bg_btn_start_hover_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
    ]
