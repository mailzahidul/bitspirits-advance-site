# Generated by Django 3.2.9 on 2021-12-01 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page_config', '0026_pagesetup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagesetup',
            old_name='back_to_top_txt_focus_color',
            new_name='back_to_top_txt_color',
        ),
        migrations.RemoveField(
            model_name='pagesetup',
            name='back_to_top_txt_hover_color',
        ),
    ]
