# Generated by Django 3.2.9 on 2021-11-28 09:30

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0019_auto_20211128_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSliderConfigure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('video', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='video')),
                ('description', models.CharField(max_length=250)),
                ('bg_start_color', colorfield.fields.ColorField(default='#000000', max_length=18)),
                ('bg_end_color', colorfield.fields.ColorField(default='#000000', max_length=18)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
    ]
