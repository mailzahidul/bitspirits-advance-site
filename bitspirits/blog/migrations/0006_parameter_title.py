# Generated by Django 3.2 on 2021-11-18 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_parameter_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='title',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]
