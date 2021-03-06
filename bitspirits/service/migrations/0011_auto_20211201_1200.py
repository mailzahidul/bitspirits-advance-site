# Generated by Django 3.2.9 on 2021-12-01 06:00

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_serviceconfigure_border_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='learn_more_btn_txt',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='serviceconfigure',
            name='learn_more_btn_hover_color',
            field=colorfield.fields.ColorField(default='#000000', max_length=18),
        ),
    ]
