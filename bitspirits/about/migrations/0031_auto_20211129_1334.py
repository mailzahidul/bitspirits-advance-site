# Generated by Django 3.2.9 on 2021-11-29 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0030_whyusconfigure_bg_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='howwedoitconfigure',
            name='bg_img',
            field=models.ImageField(default='', upload_to='how_to_do_it'),
        ),
        migrations.AddField(
            model_name='howwedoitconfigure',
            name='step_block_1_img',
            field=models.ImageField(default='', upload_to='how_to_do_it'),
        ),
        migrations.AddField(
            model_name='howwedoitconfigure',
            name='step_block_2_img',
            field=models.ImageField(default='', upload_to='how_to_do_it'),
        ),
        migrations.AddField(
            model_name='howwedoitconfigure',
            name='step_block_3_img',
            field=models.ImageField(default='', upload_to='how_to_do_it'),
        ),
        migrations.AddField(
            model_name='howwedoitconfigure',
            name='step_block_4_img',
            field=models.ImageField(default='', upload_to='how_to_do_it'),
        ),
        migrations.AddField(
            model_name='howwedoitconfigure',
            name='steps_section_1_img',
            field=models.ImageField(default='', upload_to='how_to_do_it'),
        ),
    ]