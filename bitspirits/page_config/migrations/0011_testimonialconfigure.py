# Generated by Django 3.2.9 on 2021-11-23 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_config', '0010_howwedoitconfigure'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestimonialConfigure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]