# Generated by Django 3.1.7 on 2021-10-25 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20211025_1815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='name',
            new_name='first_name',
        ),
    ]