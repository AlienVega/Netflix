# Generated by Django 4.1.2 on 2022-11-09 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_kategori_movie_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
