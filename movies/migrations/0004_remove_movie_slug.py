# Generated by Django 4.1.2 on 2022-11-09 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='slug',
        ),
    ]
