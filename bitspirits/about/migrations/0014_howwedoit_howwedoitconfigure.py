# Generated by Django 3.2.9 on 2021-11-24 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0013_auto_20211124_1312'),
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
        migrations.CreateModel(
            name='HowWeDoIt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('position', models.IntegerField()),
                ('how_we_do_it_configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='how_we_do_it', to='about.howwedoitconfigure')),
            ],
        ),
    ]
