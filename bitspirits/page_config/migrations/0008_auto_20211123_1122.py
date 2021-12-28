# Generated by Django 3.2.9 on 2021-11-23 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_config', '0007_pagebanner_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagebanner',
            name='img',
        ),
        migrations.AddField(
            model_name='pagebanner',
            name='about_img',
            field=models.ImageField(default='', upload_to='banner'),
        ),
        migrations.AddField(
            model_name='pagebanner',
            name='blog_img',
            field=models.ImageField(default='', upload_to='banner'),
        ),
        migrations.AddField(
            model_name='pagebanner',
            name='contact_img',
            field=models.ImageField(default='', upload_to='banner'),
        ),
        migrations.AddField(
            model_name='pagebanner',
            name='project_img',
            field=models.ImageField(default='', upload_to='banner'),
        ),
        migrations.AddField(
            model_name='pagebanner',
            name='service_img',
            field=models.ImageField(default='', upload_to='banner'),
        ),
    ]
