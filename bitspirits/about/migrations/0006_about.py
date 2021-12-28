# Generated by Django 3.2 on 2021-10-30 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_support_supportconfig_technology_technologyconfig'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('img_1', models.ImageField(upload_to='about')),
                ('img_2', models.ImageField(upload_to='about')),
                ('active', models.BooleanField(default=True)),
                ('start_company', models.IntegerField()),
            ],
        ),
    ]
