# Generated by Django 3.2.9 on 2021-11-23 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_mission_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='expert_team_work',
            field=models.TextField(default=''),
        ),
    ]
