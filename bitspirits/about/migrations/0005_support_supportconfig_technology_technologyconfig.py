# Generated by Django 3.2 on 2021-10-30 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_remove_videoconfig_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='TechnologyConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='technology')),
                ('technology', models.ManyToManyField(to='about.Technology')),
            ],
        ),
        migrations.CreateModel(
            name='SupportConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='support')),
                ('support', models.ManyToManyField(to='about.Support')),
            ],
        ),
    ]
