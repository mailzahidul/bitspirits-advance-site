# Generated by Django 3.2.9 on 2021-11-23 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_config', '0012_homesliderconfigure'),
    ]

    operations = [
        migrations.AddField(
            model_name='somefactsconfigure',
            name='img',
            field=models.ImageField(default='', upload_to='fact'),
        ),
    ]