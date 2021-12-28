# Generated by Django 3.2 on 2021-10-28 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_service_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.CharField(choices=[('mei-settings', 'mei-settings'), ('mei-pie-chart', 'Digital Product'), ('mei-transfer', 'Marketing'), ('mei-web-design', 'Web Design'), ('mei-computer-graphic', 'Graphics'), ('mei-development-1', 'Digital Marketing'), ('mei-development', 'Seo'), ('mei-app-development', 'Mobile App Development')], default='mei-settings', max_length=30),
        ),
    ]