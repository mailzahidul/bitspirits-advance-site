# Generated by Django 3.2.9 on 2021-11-29 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0024_homesliderconfigure_social_box_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='somefactsconfigure',
            name='item_bg_img',
            field=models.ImageField(default='', upload_to='fact'),
        ),
    ]