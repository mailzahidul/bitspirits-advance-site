# Generated by Django 3.2.9 on 2021-11-23 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_config', '0009_whoweareconfigure_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='HowWeDoItConfigure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]