# Generated by Django 3.2.9 on 2021-11-25 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_config', '0022_delete_somefactsconfigure'),
    ]

    operations = [
        migrations.AddField(
            model_name='faqconfigure',
            name='sub_title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
